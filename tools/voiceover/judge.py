#!/usr/bin/env python3
"""Score how good speech sounds, without listening: the channel's "ears".

    python judge.py file1.wav file2.mp3 ...     # or a directory

UTMOS  = UTMOSv2 naturalness (predicted human Mean Opinion Score, 1–5; VoiceMOS Challenge winner).
         Real human recordings typically score ~3.5–4.5; obviously synthetic speech scores lower.
PQ     = Meta Audiobox Aesthetics "production quality" (1–10): clean, studio-like sound.
CE     = Audiobox "content enjoyment" (1–10): how pleasant/engaging it is to listen to.

Setup (one time): uv venv --python 3.11 /opt/tts/judge-env && source /opt/tts/judge-env/bin/activate &&
  uv pip install torch torchaudio "git+https://github.com/sarulab-speech/UTMOSv2.git" audiobox_aesthetics soundfile librosa
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

import librosa
import soundfile as sf


def collect(args: list[str]) -> list[Path]:
    out = []
    for a in args:
        p = Path(a)
        out += sorted(x for x in p.iterdir() if x.suffix.lower() in {".wav", ".mp3", ".flac"}) if p.is_dir() else [p]
    return out


def main(paths: list[Path]) -> list[dict]:
    import utmosv2
    from audiobox_aesthetics.infer import initialize_predictor

    ut = utmosv2.create_model(pretrained=True, device="cpu")
    ab = initialize_predictor()
    rows = []
    with tempfile.TemporaryDirectory() as td:
        for p in paths:
            y, sr = librosa.load(p, sr=16000, mono=True)  # both judges work on 16 kHz mono
            wav = Path(td) / (p.stem + ".wav")
            sf.write(wav, y, 16000)
            mos = float(ut.predict(input_path=str(wav), device="cpu"))
            a = ab.forward([{"path": str(wav)}])[0]
            rows.append(dict(file=p.name, utmos=round(mos, 2), pq=round(a["PQ"], 2), ce=round(a["CE"], 2)))
            print(f"{p.name:45} UTMOS {mos:4.2f}   PQ {a['PQ']:4.2f}   CE {a['CE']:4.2f}", flush=True)
    return rows


if __name__ == "__main__":
    res = main(collect(sys.argv[1:]))
    Path("judge-results.json").write_text(json.dumps(res, indent=1))
