#!/usr/bin/env python3
"""Render a stills storyboard: one frame per shot (real clip + our graphic in its final state).

    python tools/video/stills.py episodes/01-vending-machines [--only 1-10]

Reads <episode>/edit.py (SHOTS, CHAPTERS), resolves each shot's start time from the voiceover timings,
grabs a frame from the shot's clip, draws the graphic on top with headless Chromium, and writes
<episode>/render/stills/NN.jpg plus one contact sheet per chapter: <episode>/render/stills/sheet-CC.png.
"""
import argparse
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from timing import Timeline  # noqa: E402

CUE_DELAY = 0.2  # seconds after the word's start that its graphic appears


def load_edit(ep: Path):
    spec = importlib.util.spec_from_file_location("edit", ep / "edit.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def resolve(ep: Path):
    """Return shots with start/end/dur and @phrase cues turned into seconds from shot start."""
    m = load_edit(ep)
    tl = Timeline(ep / "voiceover" / "timings-clean.json")
    shots, prev = [], 0.0
    for i, s in enumerate(m.SHOTS):
        a, off = s.get("at"), 0.0
        mm = re.match(r"^(.*?)([+-]\d+(?:\.\d+)?)$", a) if isinstance(a, str) else None
        if mm:   # "phrase+0.8": cut 0.8 s after the phrase starts
            a, off = mm[1].rstrip(), float(mm[2])
        start = 0.0 if a is None else round(tl.at(a, after=max(0.0, prev - 0.05)) + off, 3)
        shots.append(dict(s, n=i + 1, start=start))
        prev = start
    tail = getattr(m, "END_TAIL", 20.0)
    for a, b in zip(shots, shots[1:] + [None]):
        a["end"] = b["start"] if b else tl.duration + tail
        a["dur"] = round(a["end"] - a["start"], 3)

    def rel(phrase, s0):
        # Whisper word starts run a little early; graphics land just after the word begins.
        # "@phrase+0.4" lands 0.4 s after the phrase (for staggered builds).
        m = re.match(r"^(.*?)([+-]\d+(?:\.\d+)?)$", phrase)
        off = float(m[2]) if m else 0.0
        phrase = m[1] if m else phrase
        return round(max(0.0, tl.at(phrase, after=s0 - 0.05) - s0 + CUE_DELAY + off), 3)

    def span(phrase, s0):
        # "@@phrase" -> [start, end] of the spoken phrase, relative to the shot (for word-by-word reveals)
        a = tl.at(phrase, after=s0 - 0.05)
        return [round(a - s0 + CUE_DELAY, 3), round(tl.end(phrase, after=s0 - 0.05) - s0 + CUE_DELAY, 3)]

    def fix(v, s0):
        if isinstance(v, str) and v.startswith("@@"):
            return span(v[2:], s0)
        if isinstance(v, str) and v.startswith("@"):
            return rel(v[1:], s0)
        if isinstance(v, str) and 'data-cue="@' in v:
            return re.sub(r'data-cue="@([^"]+)"', lambda m: f'data-cue="{rel(m[1], s0)}"', v)
        if isinstance(v, dict):
            return {k: fix(x, s0) for k, x in v.items()}
        if isinstance(v, list):
            return [fix(x, s0) for x in v]
        return v

    img_dir = ep / "render" / "player" / "img"
    def still(v):
        # scene param img=(clip, t): a frame of the clip saved as a jpg the page can load
        f, tt = v
        import hashlib
        out = img_dir / (hashlib.sha1(f"{f}@{tt}".encode()).hexdigest()[:12] + ".jpg")
        if not out.exists():
            img_dir.mkdir(parents=True, exist_ok=True)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{tt:.3f}", "-i", str(ep / "footage" / f), "-frames:v", "1", "-vf",
                            "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,eq=saturation=0.86:contrast=1.03", "-q:v", "2", str(out)], check=True)
        return out.resolve().as_uri()

    # Backgrounds that continue the footage the previous shot was playing (bg="prev" or a ("prev", 0) piece), the focus
    # pull (rack) when a graphic's background is the clip that was just on screen, and the rack back to sharp after one.
    def last_piece(p):
        """(clip, second where the shot's footage ended) for a footage or graphic shot; assumes no slow-down."""
        if p.get("clip"):
            return p["clip"], (p.get("in") or 0.0) + p["dur"]
        if p.get("clips"):
            cl = p["clips"]
            joins = sum(0 if (len(x) > 3 and x[3].get("cut")) else 0.5 for x in cl[1:])
            fixed = sum(x[2] for x in cl[:-1] if len(x) > 2 and x[2])
            return cl[-1][0], cl[-1][1] + p["dur"] - fixed + joins
        if p.get("bg"):
            b = p["bg"]
            pcs = [tuple(x) for x in b] if isinstance(b[0], (list, tuple)) else [tuple(b)]
            n = len(pcs)
            fixed = [x[2] if len(x) > 2 and x[2] else None for x in pcs]
            free = [i for i in range(n) if fixed[i] is None]
            rest = p["dur"] + 0.6 * (n - 1) - sum(x for x in fixed if x)
            L = fixed[-1] if fixed[-1] else rest / max(1, len(free))
            return pcs[-1][0], pcs[-1][1] + L
        return None
    for i, s in enumerate(shots):
        if s.get("kind") == "D" and not s.get("bg") and i:
            s["bg"], s["soft"], s["dim"] = "prev", 14.0, 0.42
    for i, s in enumerate(shots):
        prev = shots[i - 1] if i else None
        b = s.get("bg")
        if b and prev:
            lp = last_piece(prev)
            if b == "prev":
                s["bg"] = b = lp
            elif isinstance(b, list) and b and b[0][0] == "prev":
                s["bg"] = b = [lp + tuple(b[0][2:])] + [tuple(x) for x in b[1:]]
            first = b[0] if isinstance(b[0], (list, tuple)) else b
            if "rack" not in s:
                s["rack"] = not s.get("carry")   # always start sharp and pull focus; a carried graphic keeps its soft picture
        # no automatic soft opening after a graphic: footage starts sharp on the cut (owner: "why is it blurry from the start")
    for i, s in enumerate(shots):
        nxt = shots[i + 1] if i + 1 < len(shots) else None
        if s.get("scene"):
            s["scene"]["hasBg"] = bool(s.get("bg") or s.get("clip") or s.get("clips"))
            s["scene"]["exit"] = not (nxt and nxt.get("carry"))
            s["scene"]["kind"] = s["kind"]
            if s.get("carry"):
                s["scene"]["carry"] = True
    for s in shots:
        if s.get("scene") and isinstance(s["scene"].get("params", {}).get("img"), (list, tuple)):
            s["scene"]["params"]["img"] = still(s["scene"]["params"]["img"])
        if s.get("scene"):
            s["scene"]["dur"] = s["dur"]
        if s.get("scene"):
            s["scene"] = fix(s["scene"], s["start"])
        vo = " ".join(w["w"] for w in tl.words if s["start"] - 0.01 <= w["start"] < s["end"] - 0.01)
        s["vo"] = re.sub(r"\s+([.,%]|-in\b)", r"\1", vo)
    chapters = []
    for title, phrase in m.CHAPTERS:
        chapters.append((title, 0.0 if phrase is None else tl.at(phrase)))
    return shots, chapters


def frame(clip: Path, t: float, out: Path):
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(clip)],
                               capture_output=True, text=True, check=True).stdout)
    t = max(0.0, min(t, dur - 0.2))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(clip), "-frames:v", "1",
                    "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080", "-q:v", "3", str(out)], check=True)


def mmss(t):
    return f"{int(t // 60)}:{int(t % 60):02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("--only", help="shot range, e.g. 1-10")
    args = ap.parse_args()
    ep = Path(args.episode).resolve()
    out = ep / "render" / "stills"
    out.mkdir(parents=True, exist_ok=True)
    shots, chapters = resolve(ep)
    if args.only:
        a, b = (int(x) for x in args.only.split("-"))
        shots = [s for s in shots if a <= s["n"] <= b]
    for s in shots:
        bgp = s.get("bg")
        if bgp and isinstance(bgp[0], (list, tuple)): bgp = bgp[0]
        src = s.get("clip") or (s.get("clips") or [[None]])[0][0] or (bgp or [None])[0]
        t_in = s.get("in") if s.get("clip") else (s["clips"][0][1] if s.get("clips") else 0)
        if src:  # the shot's built background (mirroring, multi-clip) near its end; raw clip if not built yet
            import proxies
            built = ep / "render" / "player" / "shots" / f"{proxies.shot_key(s)}.mp4"
            if built.exists():
                frame(built, max(0.0, s["dur"] - 0.4), out / f"bg-{s['n']:02d}.jpg")
            else:
                frame(ep / "footage" / src, (t_in or 0) + min(2.0, s["dur"] / 2), out / f"bg-{s['n']:02d}.jpg")
    jobs = [dict(n=s["n"], bg=str(out / f"bg-{s['n']:02d}.jpg") if (s.get("clip") or s.get("clips") or s.get("bg")) else None, scene=s.get("scene"),
                 t=s.get("still_t", s["dur"]), out=str(out / f"{s['n']:02d}.png")) for s in shots]
    (out / "jobs.json").write_text(json.dumps(jobs))
    subprocess.run(["node", str(HERE / "stills.js"), str(out / "jobs.json"), str(HERE / "gfx" / "scenes.html")], check=True)
    # Contact sheets, one per chapter
    for ci, (title, c0) in enumerate(chapters):
        c1 = chapters[ci + 1][1] if ci + 1 < len(chapters) else 1e9
        cs = [s for s in shots if c0 - 0.01 <= s["start"] < c1 - 0.01]
        if not cs:
            continue
        cells = "".join(
            f"""<div class="cell"><img src="file://{out}/{s['n']:02d}.png"><div class="cap"><span class="t">{mmss(s['start'])}</span>
            <span class="k k{s['kind']}">{dict(F='FOOTAGE', GF='GRAPHIC ON FOOTAGE', B='GRAPHIC ON IMAGE', G='GRAPHIC', D='DEAL FILE')[s['kind']]}</span>
            <span class="n">#{s['n']}</span><div class="vo">“{s['vo']}”</div>{f'<div class="note">{s["note"]}</div>' if s.get('note') else ''}</div></div>"""
            for s in cs)
        html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
        body{{margin:0;background:#15171B;color:#F2EFE8;font-family:Inter,sans-serif;width:1920px}}
        h1{{font:900 56px 'Inter Display';margin:48px 48px 8px}} .sub{{font:500 28px Inter;color:#8B93A1;margin:0 48px 28px}}
        .grid{{display:grid;grid-template-columns:1fr 1fr;gap:36px;padding:0 48px 56px}}
        .cell img{{width:100%;display:block;border-radius:10px}} .cap{{padding:14px 4px 0;font:500 24px Inter;color:#B9BEC7;line-height:1.35}}
        .t{{font:800 26px Inter;color:#F2EFE8;margin-right:12px}} .n{{float:right;color:#6B7280}}
        .k{{font:800 18px Inter;letter-spacing:2px;padding:4px 10px;border-radius:6px;background:#343944;color:#F2EFE8}}
        .kGF{{background:#4C8DD6;color:#15171B}} .kG{{background:#F2EFE8;color:#15171B}} .kD{{background:#F5D547;color:#15171B}}
        .vo{{margin-top:8px;color:#F2EFE8}} .note{{margin-top:6px;color:#C9A227}}</style></head>
        <body><h1>{ci + 1} · {title}</h1><div class="sub">Net to Owner, Episode 1, stills storyboard, {len(cs)} shots</div>
        <div class="grid">{cells}</div></body></html>"""
        (out / f"sheet-{ci + 1:02d}.html").write_text(html, encoding="utf-8")
    subprocess.run(["node", str(HERE / "sheets.js"), str(out)], check=True)


if __name__ == "__main__":
    main()
