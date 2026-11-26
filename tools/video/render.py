#!/usr/bin/env python3
"""Render an episode, or its first N seconds, to MP4 from <episode>/edit.py and the voiceover.

    python tools/video/render.py episodes/01-vending-machines --until 63.6 --out first-minute.mp4

Per shot: the clip is trimmed, scaled to 1920x1080 and (if needed) slowed or held so it covers the shot;
the shot's graphic is rendered frame by frame in headless Chromium and laid on top. Shots are joined with
plain cuts, then the voiceover (−14 LUFS) and a quiet, ducked music bed are mixed in.
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from stills import resolve  # noqa: E402
from proxies import make_bg  # noqa: E402

FPS = 30


def probe_dur(f: Path) -> float:
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                                capture_output=True, text=True, check=True).stdout)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"command failed: {' '.join(map(str, cmd))[:400]}\n{r.stderr[-2000:]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("--until", type=float, default=None, help="stop at this many seconds")
    ap.add_argument("--out", default="episode.mp4")
    ap.add_argument("--music", default="music/Meditation_Impromptu_02.mp3")
    ap.add_argument("--music-db", type=float, default=-31.0, help="music loudness before ducking (LUFS)")
    ap.add_argument("--redo", default="", help="with an existing render/work: only re-render these shot numbers, e.g. 85 or 3,7")
    args = ap.parse_args()
    ep = Path(args.episode).resolve()
    work = ep / "render" / "work"
    redo = {int(x) for x in args.redo.split(",") if x.strip()}
    if work.exists() and not redo:
        shutil.rmtree(work)
    work.mkdir(parents=True, exist_ok=True)
    shots, _ = resolve(ep)
    end_t = args.until or shots[-1]["end"]
    shots = [s for s in shots if s["start"] < end_t - 0.01]
    shots[-1]["end"] = min(shots[-1]["end"], end_t)
    for s in shots:
        s["f0"], s["f1"] = round(s["start"] * FPS), round(s["end"] * FPS)
        s["frames"] = s["f1"] - s["f0"]

    # 1) graphics
    jobs = [dict(scene=s["scene"], frames=s["frames"], fps=FPS, dir=str(work / f"g{s['n']:02d}"), transparent=bool(s.get("clip") or s.get("clips") or s.get("bg")))
            for s in shots if s.get("scene") and (not redo or s["n"] in redo)]
    for j in jobs:
        if redo and Path(j["dir"]).exists():
            shutil.rmtree(j["dir"])
    (work / "gfx.json").write_text(json.dumps(jobs))
    if jobs:
        run(["node", str(HERE / "render_gfx.js"), str(work / "gfx.json"), str(HERE / "gfx" / "scenes.html")])

    # 2) one video segment per shot
    segs = []
    for s in shots:
        n, dur = s["n"], s["frames"] / FPS
        out = work / f"s{n:02d}.mp4"
        if redo and n not in redo and out.exists():
            segs.append(out)
            continue
        cmd, chains = ["ffmpeg", "-v", "error", "-y"], []
        if s.get("clip") or s.get("clips") or s.get("bg"):
            bg = work / f"bg{n:02d}.mp4"
            make_bg(ep, dict(s, dur=dur), bg, crf=16)
            cmd += ["-i", str(bg)]
            if s.get("scene"):
                cmd += ["-framerate", str(FPS), "-i", str(work / f"g{n:02d}" / "%05d.png")]
                chains.append("[1:v]format=rgba[fg];[0:v][fg]overlay=0:0:format=auto,format=yuv420p[v]")
            else:
                chains.append("[0:v]format=yuv420p[v]")
        else:
            cmd += ["-framerate", str(FPS), "-i", str(work / f"g{n:02d}" / "%05d.png")]
            chains.append("[0:v]format=yuv420p[v]")
        cmd += ["-filter_complex", ";".join(chains), "-map", "[v]", "-frames:v", str(s["frames"]), "-r", str(FPS),
                "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-an", str(out)]
        run(cmd)
        segs.append(out)
        print(f"shot {n:02d} {s['kind']:2} {dur:5.2f}s {s.get('clip') or '(graphic)'}", flush=True)
    (work / "list.txt").write_text("".join(f"file '{p}'\n" for p in segs))
    video = work / "video.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(work / "list.txt"), "-c", "copy", str(video)])

    # 3) audio: voice at −14 LUFS, music bed ducked under the voice
    total = sum(s["frames"] for s in shots) / FPS
    voice = ep / "voiceover" / "voiceover-clean.wav"
    music = ep / args.music
    fc = (f"[0:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,aresample=48000,apad=whole_dur={total + 3:.3f},loudnorm=I=-15:TP=-1.5:LRA=11,aresample=48000,asplit[v1][v2];"
          f"[1:a]atrim=0:{total + 5:.3f},asetpts=PTS-STARTPTS,aresample=48000,loudnorm=I={args.music_db}:LRA=7,aresample=48000,"
          f"afade=t=in:d=2,afade=t=out:st={max(0, total - 3):.3f}:d=3[m];"
          f"[m][v2]sidechaincompress=threshold=0.03:ratio=5:attack=40:release=700[md];"
          f"[v1][md]amix=inputs=2:duration=first:normalize=0,apad=pad_dur=5,loudnorm=I=-14:TP=-1:LRA=11,aresample=48000,atrim=0:{total:.3f}[a]")
    audio = work / "audio.m4a"
    if not (redo and audio.exists()):
      run(["ffmpeg", "-v", "error", "-y", "-i", str(voice), "-stream_loop", "-1", "-i", str(music), "-filter_complex", fc, "-map", "[a]",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(audio)])
    out = ep / "render" / args.out
    run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-i", str(audio), "-map", "0:v", "-map", "1:a", "-c", "copy",
         "-shortest", "-movflags", "+faststart", str(out)])
    print("wrote", out, f"{total:.2f}s")


if __name__ == "__main__":
    main()
