#!/usr/bin/env python3
"""Make light 1080p proxies, one per shot, exactly as long as the shot, for the browser player.

    python tools/video/proxies.py episodes/01-vending-machines
Reads render/player/edit.json, writes render/player/shots/sNN.mp4 (blur boxes and grade baked in).
"""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

FPS = 30


def dur_of(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                                capture_output=True, text=True, check=True).stdout)


def one(ep, s):
    out = ep / "render" / "player" / "shots" / f"s{s['n']:02d}.mp4"
    clip = ep / "footage" / s["clip"]
    t_in = s.get("in") or 0.0
    dur = s["dur"]
    slow = min(max(1.0, dur / max(0.5, dur_of(clip) - t_in - 0.05)), 1.5)
    vf = (f"setpts={slow:.4f}*(PTS-STARTPTS),fps={FPS},scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
          f"eq=saturation=0.86:contrast=1.03,tpad=stop_mode=clone:stop_duration={dur + 1:.2f}")
    chain = "[0:v]" + vf
    for i, (x, y, w, h) in enumerate(s.get("blur") or []):
        chain += f"[b{i}];[b{i}]split[m{i}][c{i}];[c{i}]crop={w}:{h}:{x}:{y},boxblur=luma_radius=24:luma_power=2:chroma_radius=10:chroma_power=2[z{i}];[m{i}][z{i}]overlay={x}:{y}"
    chain += "[v]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t_in:.3f}", "-t", f"{dur / slow + 1:.3f}", "-i", str(clip),
                    "-filter_complex", chain, "-map", "[v]", "-t", f"{dur:.3f}", "-r", str(FPS), "-c:v", "libx264",
                    "-preset", "veryfast", "-crf", "28", "-g", "30", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", str(out)], check=True)
    return s["n"]


def main():
    ep = Path(sys.argv[1]).resolve()
    edit = json.load(open(ep / "render" / "player" / "edit.json"))
    shots = [s for s in edit["shots"] if s.get("clip")]
    with ThreadPoolExecutor(4) as ex:
        for n in ex.map(lambda s: one(ep, s), shots):
            print("proxy", n, flush=True)


if __name__ == "__main__":
    main()
