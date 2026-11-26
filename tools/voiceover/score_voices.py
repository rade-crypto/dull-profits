#!/usr/bin/env python3
"""Score voice auditions objectively (no ears required).

    python score_voices.py <auditions_dir>      # each subdir holds hook.wav + timings.json

Per voice:
  wer        word error rate of Whisper's transcript vs the script (lower = clearer diction)
  asr_conf   Whisper's mean word probability (higher = cleaner, more natural-sounding speech)
  f0_med     median pitch in Hz (lower = deeper, more "mature" male voice)
  f0_var     pitch variability in semitones (too low = monotone; ~2.5-4 = lively but calm)
  wpm        speaking rate
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import jiwer
import librosa
import numpy as np
from faster_whisper import WhisperModel

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize import normalize  # noqa: E402

MARKUP = re.compile(r"\[([^\]]+)\]\(/[^)]*/\)")


def clean(t: str) -> str:
    t = MARKUP.sub(r"\1", normalize(t)).lower().replace("-", " ")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9' ]", " ", t)).strip()


def main(root: Path):
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    rows = []
    for d in sorted(p for p in root.iterdir() if (p / "hook.wav").exists()):
        timing = json.loads((d / "timings.json").read_text())
        ref = clean(" ".join(p["text"] for p in timing["paragraphs"]))
        y, sr = librosa.load(d / "hook.wav", sr=16000)  # pass samples: avoids PyAV version issues
        segs, _ = model.transcribe(y, language="en", word_timestamps=True, beam_size=5)
        words = [w for s in segs for w in s.words]
        hyp = clean(" ".join(w.word for w in words))
        f0, voiced, _ = librosa.pyin(y, fmin=60, fmax=300, sr=sr, frame_length=1024)
        f0 = f0[voiced & ~np.isnan(f0)]
        semis = 12 * np.log2(f0 / np.median(f0))
        rows.append(dict(voice=d.name, wer=jiwer.wer(ref, hyp), asr_conf=float(np.mean([w.probability for w in words])),
                         f0_med=float(np.median(f0)), f0_var=float(np.std(semis)), wpm=timing["wpm"]))
        print(f"scored {d.name}", flush=True)
    rows.sort(key=lambda r: (-r["asr_conf"]))
    print(f"\n{'voice':34} {'WER':>6} {'conf':>6} {'f0Hz':>6} {'f0var':>6} {'wpm':>6}")
    for r in rows:
        print(f"{r['voice']:34} {r['wer']:6.3f} {r['asr_conf']:6.3f} {r['f0_med']:6.0f} {r['f0_var']:6.2f} {r['wpm']:6.1f}")
    (root / "scores.json").write_text(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main(Path(sys.argv[1]))
