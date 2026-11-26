#!/usr/bin/env python3
"""Background footage for each shot, exactly as long as the shot (1080p, graded, blur boxes baked in).

    python tools/video/proxies.py episodes/01-vending-machines      # light copies for the browser preview

A shot uses `clip` + `in`, or `clips`: a list of (file, in, seconds) pieces joined with short crossfades
(the last piece's seconds may be None: it fills the rest). Pieces never freeze: if a clip is too short it is
slowed (at most 1.5x), and only then held. render.py calls make_bg() for the final, higher-quality version.
"""
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

FPS = 30
XF = 0.5  # crossfade between pieces


def dur_of(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                                capture_output=True, text=True, check=True).stdout)


def shot_key(s):
    """Stable file name for a shot's background: changes only when its footage or length changes."""
    spec = json.dumps([s.get("clip"), s.get("clips"), s.get("in"), round(s["dur"], 3), s.get("blur")] + ([True] if s.get("flip") else [])
                      + ([s["bg"]] if s.get("bg") else []), sort_keys=True)
    return hashlib.sha1(spec.encode()).hexdigest()[:12]


def pieces_of(s):
    """(file, in, seconds or None, options). Options: flip (mirror so a person sits clear of the text panel),
    until (last usable second of the source, to stop before a cut inside a stock clip)."""
    base = {"flip": True} if s.get("flip") else {}
    if s.get("clips"):
        return [(p[0], p[1], p[2] if len(p) > 2 else None, dict(base, **(p[3] if len(p) > 3 else {}))) for p in s["clips"]]
    return [(s["clip"], s.get("in") or 0.0, None, base)]


def has_bg(s):
    return bool(s.get("clip") or s.get("clips") or s.get("bg"))


def make_still_bg(ep, s, out, crf):
    """A graphic's own background: one frame of a clip, blurred and darkened, drifting slowly sideways."""
    f, t = s["bg"][0], s["bg"][1]
    dim = s["bg"][2] if len(s["bg"]) > 2 else 0.42
    dur = s["dur"]
    vf = (f"scale=2208:1242:force_original_aspect_ratio=increase,crop=2208:1242,boxblur=luma_radius=22:luma_power=2:chroma_radius=12:chroma_power=2,"
          f"colorchannelmixer=rr={dim}:gg={dim}:bb={dim},eq=saturation=0.75,"
          f"crop=1920:1080:x='(iw-1920)*(0.15+0.7*t/{dur:.3f})':y=(ih-1080)/2,fps={FPS},format=yuv420p")
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", str(ep / "footage" / f), "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"]
    png = subprocess.run(cmd, capture_output=True, check=True).stdout
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-f", "image2pipe", "-i", "-", "-vf", vf, "-t", f"{dur:.3f}",
                        "-c:v", "libx264", "-preset", "veryfast" if crf >= 24 else "medium", "-crf", str(crf), "-g", "30", "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", "-an", str(out)], input=png, capture_output=True)
    if r.returncode:
        raise RuntimeError(f"shot {s['n']}: {r.stderr[-1500:].decode(errors='ignore')}")
    return s["n"]


def make_bg(ep, s, out, crf=28):
    if s.get("bg"):
        return make_still_bg(ep, s, out, crf)
    dur = s["dur"]
    ps = pieces_of(s)
    n = len(ps)
    lens = [p[2] for p in ps]
    fixed = sum(L for L in lens[:-1] if L) if n > 1 else 0
    lens[-1] = dur - fixed + XF * (n - 1) if n > 1 else dur
    cmd, chains = ["ffmpeg", "-v", "error", "-y"], []
    for i, ((f, t_in, _, opt), L) in enumerate(zip(ps, lens)):
        clip = ep / "footage" / f
        avail = max(0.5, min(dur_of(clip), opt.get("until", 1e9)) - t_in - 0.05)
        slow = min(max(1.0, L / avail), 1.5)
        cmd += ["-ss", f"{t_in:.3f}", "-t", f"{L / slow + 1:.3f}", "-i", str(clip)]
        chains.append(f"[{i}:v]setpts={slow:.4f}*(PTS-STARTPTS),fps={FPS},scale=1920:1080:force_original_aspect_ratio=increase,"
                      f"crop=1920:1080,setsar=1,{'hflip,' if opt.get('flip') else ''}format=yuv420p,eq=saturation=0.86:contrast=1.03,"
                      f"tpad=stop_mode=clone:stop_duration={L + 1:.2f},trim=duration={L:.3f},setpts=PTS-STARTPTS[p{i}]")
    last, off = "p0", 0.0
    for i in range(1, n):
        off += lens[i - 1] - XF
        chains.append(f"[{last}][p{i}]xfade=transition=fade:duration={XF}:offset={off:.3f}[x{i}]")
        last = f"x{i}"
    tail = f"[{last}]"
    for i, (x, y, w, h) in enumerate(s.get("blur") or []):
        chains.append(f"{tail}split[m{i}][c{i}];[c{i}]crop={w}:{h}:{x}:{y},boxblur=luma_radius=24:luma_power=2:chroma_radius=10:chroma_power=2[z{i}];"
                      f"[m{i}][z{i}]overlay={x}:{y}[b{i}]")
        tail = f"[b{i}]"
    chains.append(f"{tail}null[v]")
    cmd += ["-filter_complex", ";".join(chains), "-map", "[v]", "-t", f"{dur:.3f}", "-r", str(FPS), "-c:v", "libx264",
            "-preset", "veryfast" if crf >= 24 else "medium", "-crf", str(crf), "-g", "30", "-pix_fmt", "yuv420p",
            "-movflags", "+faststart", "-an", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"shot {s['n']}: {r.stderr[-1500:]}")
    return s["n"]


def one(ep, s):
    out = ep / "render" / "player" / "shots" / f"{shot_key(s)}.mp4"
    if out.exists():
        return s["n"]
    return make_bg(ep, s, out)


def main():
    ep = Path(sys.argv[1]).resolve()
    edit = json.load(open(ep / "render" / "player" / "edit.json"))
    only = {int(x) for x in sys.argv[2].split(",")} if len(sys.argv) > 2 else None
    shots = [s for s in edit["shots"] if has_bg(s) and (not only or s["n"] in only)]
    with ThreadPoolExecutor(4) as ex:
        for n in ex.map(lambda s: one(ep, s), shots):
            print("proxy", n, flush=True)


if __name__ == "__main__":
    main()
