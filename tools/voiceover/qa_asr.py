#!/usr/bin/env python3
"""Proofread a rendered voiceover by ear, automatically.

    python qa_asr.py episodes/01-vending-machines/voiceover

Transcribes voiceover.wav with Whisper and lists every place where what was heard differs from
the script (timings.json), with timestamps, so you only need to listen to the flagged spots.
Differences in how numbers are *written* are normalized away; what's left is usually a real slip
(mispronounced name, dropped word) or a harmless homophone (to/too).
"""
from __future__ import annotations

import difflib
import json
import sys
from pathlib import Path

import librosa
from faster_whisper import WhisperModel

sys.path.insert(0, str(Path(__file__).resolve().parent))
from score_voices import clean  # noqa: E402

HOMOPHONES = {frozenset(p) for p in [("to", "too"), ("two", "to"), ("two", "too"), ("dollar", "dollars"), ("its", "it's"),
                                     ("theyre", "their"), ("whos", "whose")]}


def main(vo_dir: Path, model_name: str = "small.en"):
    timing = json.loads((vo_dir / "timings.json").read_text())
    ref = clean(" ".join(p["text"] for p in timing["paragraphs"])).split()
    y, _ = librosa.load(vo_dir / "voiceover.wav", sr=16000)
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segs, _ = model.transcribe(y, language="en", beam_size=5, word_timestamps=True)
    words = [w for s in segs for w in s.words]
    hyp, stamps = [], []
    for w in words:
        for tok in clean(w.word).split():
            hyp.append(tok)
            stamps.append(w.start)
    issues = []
    for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, ref, hyp, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        said, heard = " ".join(ref[a1:a2]), " ".join(hyp[b1:b2])
        if frozenset((said, heard)) in HOMOPHONES or (not said and heard in {"dollars", "dollar"}):
            continue
        t = stamps[min(b1, len(stamps) - 1)] if stamps else 0
        ctx = " ".join(ref[max(0, a1 - 4):a2 + 4])
        issues.append(dict(time=f"{int(t // 60)}:{int(t % 60):02}", script=said, heard=heard, context=ctx))
    accuracy = 1 - sum(max(len(i["script"].split()), len(i["heard"].split())) for i in issues) / max(1, len(ref))
    report = [f"# Voiceover QA ({timing.get('engine')} / {timing.get('voice')})", "",
              f"{len(ref)} script words, {len(issues)} flagged spots, ~{accuracy:.1%} word accuracy (Whisper {model_name}).", "",
              "| time | script says | Whisper heard | context |", "|---|---|---|---|"]
    report += [f"| {i['time']} | {i['script'] or '—'} | {i['heard'] or '—'} | {i['context']} |" for i in issues]
    (vo_dir / "qa-report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))


if __name__ == "__main__":
    main(Path(sys.argv[1]), *(sys.argv[2:3]))
