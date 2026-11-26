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
        start = 0.0 if s.get("at") is None else tl.at(s["at"], after=max(0.0, prev - 0.05))
        shots.append(dict(s, n=i + 1, start=start))
        prev = start
    tail = getattr(m, "END_TAIL", 20.0)
    for a, b in zip(shots, shots[1:] + [None]):
        a["end"] = b["start"] if b else tl.duration + tail
        a["dur"] = round(a["end"] - a["start"], 3)

    def rel(phrase, s0):
        return round(max(0.0, tl.at(phrase, after=s0 - 0.05) - s0), 3)

    def fix(v, s0):
        if isinstance(v, str) and v.startswith("@"):
            return rel(v[1:], s0)
        if isinstance(v, str) and 'data-cue="@' in v:
            return re.sub(r'data-cue="@([^"]+)"', lambda m: f'data-cue="{rel(m[1], s0)}"', v)
        if isinstance(v, dict):
            return {k: fix(x, s0) for k, x in v.items()}
        if isinstance(v, list):
            return [fix(x, s0) for x in v]
        return v

    for s in shots:
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
        if s.get("clip"):
            frame(ep / "footage" / s["clip"], s.get("in", 0) + min(2.0, s["dur"] / 2), out / f"bg-{s['n']:02d}.jpg")
    jobs = [dict(n=s["n"], bg=str(out / f"bg-{s['n']:02d}.jpg") if s.get("clip") else None, scene=s.get("scene"),
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
            <span class="k k{s['kind']}">{dict(F='FOOTAGE', GF='GRAPHIC ON FOOTAGE', G='GRAPHIC', D='DEAL FILE')[s['kind']]}</span>
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
