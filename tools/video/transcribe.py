#!/usr/bin/env python3
"""Word timings for a finished voiceover.

    python tools/video/transcribe.py episodes/01-vending-machines/voiceover/voiceover.mp3

Writes timings.json next to the audio: every word with start/end seconds, plus Whisper's segments.
The video is cut to these timings (numbers appear on screen as they're spoken).
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from faster_whisper import WhisperModel

audio = Path(sys.argv[1])
model_name = sys.argv[2] if len(sys.argv) > 2 else "medium.en"
model = WhisperModel(model_name, device="cpu", compute_type="int8")
# Decode with ffmpeg (avoids PyAV version issues): 16 kHz mono float32
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(audio), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                     check=True, capture_output=True).stdout
segs, info = model.transcribe(np.frombuffer(pcm, np.float32), language="en", beam_size=5, word_timestamps=True, vad_filter=False)
out = {"audio": audio.name, "duration": info.duration, "model": model_name, "segments": [], "words": []}
for s in segs:
    out["segments"].append({"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip()})
    for w in s.words:
        out["words"].append({"w": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3), "p": round(w.probability, 3)})
    print(f"{s.start:7.2f} {s.text.strip()}", flush=True)
(audio.parent / "timings.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print(f"wrote {len(out['words'])} words")
