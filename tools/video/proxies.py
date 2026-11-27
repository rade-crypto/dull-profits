#!/usr/bin/env python3
"""Background footage for each shot, exactly as long as the shot (1080p, graded, blur boxes baked in).

    python tools/video/proxies.py episodes/01-vending-machines      # light copies for the browser preview

A shot uses `clip` + `in`, or `clips`: a list of (file, in, seconds[, options]) pieces joined with short crossfades
or hard cuts (the last piece's seconds may be None: it fills the rest). Pieces never freeze: a clip may be slowed
at most 1.1x; if it is still too short the build stops with an error. render.py calls make_bg() for the final version.
"""
import hashlib
import json
import math
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

FPS = 30
XF = 0.5  # crossfade between pieces


def dur_of(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                                capture_output=True, text=True, check=True).stdout)


_FPS = {}
def src_fps(f):
    """Frame rate of a footage file (cached)."""
    if f not in _FPS:
        r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", str(f)],
                           capture_output=True, text=True).stdout.strip() or "30/1"
        a, b = (r.split("/") + ["1"])[:2]
        _FPS[f] = float(a) / float(b or 1)
    return _FPS[f]


def _sources(s):
    if s.get("bg") and s["bg"] != "prev":
        b = s["bg"]; return [x[0] for x in ([b] if not isinstance(b[0], (list, tuple)) else b)]
    if s.get("clips"):
        return [x[0] for x in s["clips"]]
    return [s["clip"]] if s.get("clip") else []


def shot_key(s):
    """Stable file name for a shot's background: changes only when its footage, length or look changes."""
    ep = Path(__file__).resolve().parents[2] / "episodes" / "01-vending-machines" / "footage"
    low = any(src_fps(ep / f) < 29 for f in _sources(s) if (ep / f).exists())   # 24/25 fps sources are motion-interpolated
    spec = json.dumps([s.get("clip"), s.get("clips"), s.get("in"), round(s["dur"], 3), s.get("blur")] + ([s["zoom"]] if s.get("zoom") else []) + (["shade-" + s["shade"]] if s.get("shade") else []) + ([True] if s.get("flip") else [])
                      + ([s["bg"], s.get("rack"), s.get("soft"), s.get("dim")] if s.get("bg") else [])
                      + [s.get("rack_open"), s.get("push"), "v3"] + (["rk2"] if s.get("bg") and s.get("rack") else []) + (["mi1"] if low else []), sort_keys=True)
    return hashlib.sha1(spec.encode()).hexdigest()[:12]


def pieces_of(s):
    """(file, in, seconds or None, options). Options: flip (mirror so a person sits clear of the text),
    until (last usable second of the source, to stop before a cut inside a stock clip), cut (hard cut into this
    piece instead of the 0.5 s crossfade)."""
    base = {"flip": True} if s.get("flip") else {}
    if s.get("clips"):
        return [(p[0], p[1], p[2] if len(p) > 2 else None, dict(base, **(p[3] if len(p) > 3 else {}))) for p in s["clips"]]
    return [(s["clip"], s.get("in") or 0.0, None, base)]


def has_bg(s):
    return bool(s.get("clip") or s.get("clips") or s.get("bg"))


MAX_SLOW = 1.1  # footage may be slowed this much at most; never frozen (editing playbook, rule 3)


def rack_cmds(path, dur, sigma, dim, sat, opening=False, start=0.0):
    """sendcmd lines for a real focus pull: sharp -> soft and dim over `dur` (soft -> sharp when opening). Sine ease."""
    n = max(1, round(dur * FPS))
    lines = []
    for f in range(n + 1):
        e = -(math.cos(math.pi * f / n) - 1) / 2
        if opening:
            e = 1 - e
        d = 1 - (1 - dim) * e
        lines.append(f"{start + f / FPS:.4f} gblur sigma {0.01 + sigma * e:.3f}, colorchannelmixer rr {d:.3f}, "
                     f"colorchannelmixer gg {d:.3f}, colorchannelmixer bb {d:.3f}, eq saturation {1 - (1 - sat) * e:.3f};")
    Path(path).write_text("\n".join(lines))


def push_filter(z, dur):
    """Sub-pixel push-in from 1.0 to 1+z over the shot (perspective samples between pixels, so it never jitters)."""
    Z = f"(1+{z:.4f}*in/{max(1, round(dur * FPS))})"
    a, b = f"W*(1-1/{Z})/2", f"H*(1-1/{Z})/2"
    return (f"perspective=x0='{a}':y0='{b}':x1='W-{a}':y1='{b}':x2='{a}':y2='H-{b}':x3='W-{a}':y3='H-{b}'"
            f":interpolation=linear:eval=frame")


def _retime(clip, slow, soft, crf):
    """Get to 30 fps without repeated frames: footage shot at 24/25 fps would otherwise judder (every 5th-6th frame
    shown twice). Sharp footage gets motion-compensated in-between frames; softened backgrounds get frame blends.
    Previews interpolate at 720p (fast); the final render at full size."""
    if src_fps(clip) / slow >= 29:
        return f"fps={FPS},scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080"
    if soft:
        return f"scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,framerate=fps={FPS}"
    mi = f"minterpolate=fps={FPS}:mi_mode=mci:mc_mode=obmc:me_mode=bilat:me=epzs:mb_size=16:search_param=16"
    if crf >= 24:
        return f"scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,{mi},scale=1920:1080"
    return f"scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,{mi}"


def _piece_chain(i, clip, t_in, L, avail, opt, s, soft=False, crf=28):
    slow = max(1.0, L / avail)
    if slow > MAX_SLOW + 1e-6:
        raise RuntimeError(f"shot {s['n']}: {clip.name} from {t_in}s has {avail:.2f}s, needs {L:.2f}s (would slow {slow:.2f}x). "
                           f"Chain another clip or start earlier.")
    return slow, (f"[{i}:v]setpts={slow:.4f}*(PTS-STARTPTS),{_retime(clip, slow, soft, crf)},"
                  f"setsar=1,{'hflip,' if opt.get('flip') else ''}format=yuv420p,eq=saturation=0.86:contrast=1.03,"
                  f"trim=duration={L:.3f},setpts=PTS-STARTPTS,fps={FPS},settb=1/{FPS}[p{i}]")   # one timebase for every piece (xfade needs it)


def _join(chains, lens, joins):
    """Join pieces p0..pn: crossfade (XF) or hard cut. Returns the label of the joined stream."""
    last, t = "p0", lens[0]
    for i in range(1, len(lens)):
        if joins[i] == 0:
            chains.append(f"[{last}][p{i}]concat=n=2:v=1:a=0[x{i}]")
            t += lens[i]
        else:
            chains.append(f"[{last}][p{i}]xfade=transition=fade:duration={joins[i]}:offset={t - joins[i]:.3f}[x{i}]")
            t += lens[i] - joins[i]
        last = f"x{i}"
    return last


def make_still_bg(ep, s, out, crf):
    """A graphic's own background: real footage, kept playing, softened (gblur) and dimmed so text reads, with a slow
    push-in. If the background continues the clip the previous shot was playing (s["rack"]), the lens pulls focus from
    sharp to soft over 0.6 s; otherwise it cuts straight to the soft picture. bg is (clip, t) or a list of (clip, t[, seconds])
    pieces joined with 0.6 s crossfades, so a long graphic gets a new picture every few seconds."""
    bg = s["bg"]
    pieces = [tuple(x) for x in bg] if isinstance(bg[0], (list, tuple)) else [tuple(bg)]
    dur, XB = s["dur"], 0.6
    sigma, dim, sat = s.get("soft") or 8.0, s.get("dim") or 0.6, 0.75
    n = len(pieces)
    fixed = [p[2] if len(p) > 2 and p[2] else None for p in pieces]
    free = [i for i in range(n) if fixed[i] is None]
    rest = dur + XB * (n - 1) - sum(x for x in fixed if x)
    lens = [fixed[i] if fixed[i] else rest / len(free) for i in range(n)]
    cmd, chains = ["ffmpeg", "-v", "error", "-y"], []
    for i, (p, L) in enumerate(zip(pieces, lens)):
        f, t = p[0], p[1]
        clip = ep / "footage" / f
        avail = max(0.3, dur_of(clip) - t - 0.05)
        # a focus pull starts sharp: no frame blending on that piece (it ghosts), real in-between frames instead
        slow, ch = _piece_chain(i, clip, t, L, avail, {}, s, soft=not (i == 0 and s.get("rack")), crf=crf)
        cmd += ["-ss", f"{t:.3f}", "-t", f"{L / slow + 1:.3f}", "-i", str(clip)]
        chains.append(ch)
    last = _join(chains, lens, [0] + [XB] * (n - 1))
    look = f"gblur=sigma={sigma}:steps=2,colorchannelmixer=rr={dim}:gg={dim}:bb={dim},eq=saturation={sat}"
    if s.get("rack"):
        cf = out.with_suffix(".rack.txt")
        rack_cmds(cf, 0.6, sigma, dim, sat)
        look = f"sendcmd=f='{cf}'," + look
    chains.append(f"[{last}]trim=duration={dur:.3f},setpts=PTS-STARTPTS,{look},{push_filter(0.05, dur)},format=yuv420p[v]")
    cmd += ["-filter_complex", ";".join(chains), "-map", "[v]", "-t", f"{dur:.3f}", "-r", str(FPS), "-c:v", "libx264",
            "-preset", "veryfast" if crf >= 24 else "medium", "-crf", str(crf), "-g", "30", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", str(out)]
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode:
        raise RuntimeError(f"shot {s['n']}: {r.stderr[-1500:].decode(errors='ignore')}")
    return s["n"]


def shade_png(ep, side):
    """Black gradient, 62% at the text edge fading to nothing by 60% of the width (smoothstep)."""
    out = ep / "render" / "player" / "img" / f"shade-{side}.png"
    if not out.exists():
        from PIL import Image
        import numpy as np
        x = np.linspace(0, 1, 1920)
        if side == "right":
            x = x[::-1]
        u = np.clip(x / 0.6, 0, 1)
        a = (0.62 * (1 - u * u * (3 - 2 * u)) * 255).astype(np.uint8)
        rgba = np.zeros((1080, 1920, 4), np.uint8)
        rgba[..., 3] = a[None, :]
        out.parent.mkdir(parents=True, exist_ok=True)
        Image.fromarray(rgba, "RGBA").save(out)
    return out


def make_bg(ep, s, out, crf=28):
    if s.get("bg"):
        return make_still_bg(ep, s, out, crf)
    dur = s["dur"]
    ps = pieces_of(s)
    n = len(ps)
    joins = [0] + [0 if ps[i][3].get("cut") else XF for i in range(1, n)]
    lens = [p[2] for p in ps]
    fixed = sum(L for L in lens[:-1] if L) if n > 1 else 0
    lens[-1] = dur - fixed + sum(joins)
    cmd, chains = ["ffmpeg", "-v", "error", "-y"], []
    for i, ((f, t_in, _, opt), L) in enumerate(zip(ps, lens)):
        clip = ep / "footage" / f
        avail = max(0.3, min(dur_of(clip), opt.get("until", 1e9)) - t_in - 0.05)
        slow, ch = _piece_chain(i, clip, t_in, L, avail, opt, s, soft=bool(s.get('rack_open') and False), crf=crf)
        cmd += ["-ss", f"{t_in:.3f}", "-t", f"{L / slow + 1:.3f}", "-i", str(clip)]
        chains.append(ch)
    last = _join(chains, lens, joins)
    tail = f"[{last}]"
    for i, (x, y, w, h) in enumerate(s.get("blur") or []):
        chains.append(f"{tail}split[m{i}][c{i}];[c{i}]crop={w}:{h}:{x}:{y},boxblur=luma_radius=24:luma_power=2:chroma_radius=10:chroma_power=2[z{i}];"
                      f"[m{i}][z{i}]overlay={x}:{y}[b{i}]")
        tail = f"[b{i}]"
    post = []
    if s.get("zoom"):  # crop in (z, x0, y0 = top-left of the kept area) instead of blurring billboards and logos
        z, zx, zy = s["zoom"]
        post.append(f"crop={1920 / z:.0f}:{1080 / z:.0f}:{zx}:{zy},scale=1920:1080:flags=lanczos")
    if s.get("push"):  # a gentle push-in for clips whose camera barely moves
        post.append(push_filter(s["push"], dur))
    if s.get("rack_open"):  # after a graphic: start soft and dim, pull focus to sharp (one focus move across the cut)
        ro, cf = s["rack_open"], out.with_suffix(".open.txt")
        rack_cmds(cf, ro, 8.0, 0.6, 0.75, opening=True)
        post.append(f"sendcmd=f='{cf}',gblur=sigma=0.01:steps=2,colorchannelmixer=rr=1:gg=1:bb=1,eq=saturation=1")
    if s.get("shade"):  # the style guide's text-side darkening: a soft left-to-right (or right-to-left) gradient, no box
        cmd += ["-loop", "1", "-i", str(shade_png(ep, s["shade"]))]
        chains.append(f"{tail}{','.join(post) if post else 'null'}[pv];[pv][{n}:v]overlay=0:0:shortest=1,format=yuv420p[v]")
    else:
        chains.append(f"{tail}{','.join(post) if post else 'null'}[v]")
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
    tmp = out.with_name(out.stem + ".part.mp4")   # never leave a broken file under the final name
    try:
        make_bg(ep, s, tmp)
        tmp.replace(out)
    finally:
        tmp.unlink(missing_ok=True)
    return s["n"]


def main():
    ep = Path(sys.argv[1]).resolve()
    edit = json.load(open(ep / "render" / "player" / "edit.json"))
    only = {int(x) for x in sys.argv[2].split(",")} if len(sys.argv) > 2 else None
    shots = [s for s in edit["shots"] if has_bg(s) and (not only or s["n"] in only)]
    errs = []
    def safe(s):
        try:
            return one(ep, s)
        except Exception as e:  # report every bad shot, not just the first
            errs.append(str(e)[:400])
            return f"{s['n']} FAILED"
    with ThreadPoolExecutor(4) as ex:
        for n in ex.map(safe, shots):
            print("proxy", n, flush=True)
    if errs:
        sys.exit("\n".join(errs))


if __name__ == "__main__":
    main()
