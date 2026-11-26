#!/usr/bin/env python3
"""Build the browser player/renderer page for an episode.

    python tools/video/build_player.py episodes/01-vending-machines

Writes <episode>/render/player/index.html: plays the whole edit live (proxy clips + the same graphics engine as
the server render) and has a Render MP4 button that encodes the video frame by frame in the browser
(WebCodecs) and offers it as a download. Needs render/player/{edit.json,audio.m4a,shots/*.mp4}.
"""
import base64
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ep = Path(sys.argv[1]).resolve()
P = ep / "render" / "player"
scenes = (HERE / "gfx" / "scenes.html").read_text()
css = re.search(r"<style>(.*?)</style>", scenes, re.S).group(1)
js = re.search(r"<script>(.*?)</script>", scenes, re.S).group(1)

fonts = HERE / "gfx" / "fonts"
def b64(p):
    return base64.b64encode(p.read_bytes()).decode()
for name in ["LibreFranklin-400", "LibreCaslonDisplay-400", "LibreCaslonText-400", "LibreCaslonText-700"]:
    css = css.replace(f"url(fonts/{name}.woff2)", f"url(data:font/woff2;base64,{b64(fonts / (name + '.woff2'))})")
# scope the 1920x1080 canvas rules to .frame instead of html/body
css = css.replace("html,body{width:1920px;height:1080px;background:transparent;overflow:hidden}", "")
css = css.replace("body{color:var(--ink);", ".frame{width:1920px;height:1080px;overflow:hidden;color:var(--ink);")
js = js.replace("const S = document.getElementById('stage');", "const S = document.getElementById('stage');")
js = js.replace("if (scene.opaque) document.body.style.background = 'var(--bg)';", "S.style.background = scene.opaque ? 'var(--bg)' : '';")

sys.path.insert(0, str(HERE))
from stills import resolve  # noqa: E402
from proxies import shot_key  # noqa: E402
shots, _ = resolve(ep)
edit = {"shots": [], "duration": shots[-1]["end"]}
for s in shots:
    d = {k: s.get(k) for k in ("n", "kind", "start", "end", "dur", "clip", "clips", "in", "blur", "scene")}
    if d["clip"] or d["clips"]:
        d["key"] = shot_key(d)
    edit["shots"].append(d)
(P / "edit.json").write_text(json.dumps(edit))
logo = "data:image/png;base64," + b64(ep.parents[1] / "brand" / "wordmark.png")
for s in edit["shots"]:
    if s.get("scene") and s["scene"].get("type") == "end":
        s["scene"]["params"]["logo"] = logo
data = json.dumps(edit).replace("<", "\\u003c")

page = (HERE / "player_template.html").read_text()
page = page.replace("/*SCENE_CSS*/", css).replace("/*SCENE_JS*/", js).replace("/*EDIT_JSON*/null", data)
(P / "index.html").write_text(page, encoding="utf-8")
print("wrote", P / "index.html", round(len(page) / 1024), "KB")
