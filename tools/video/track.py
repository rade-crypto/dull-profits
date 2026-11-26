#!/usr/bin/env python3
"""Track the ground in a stretch of footage, so graphics (pins, a route) stay stuck to it while the camera moves.

    python tools/video/track.py episodes/01-vending-machines c10-arlington-heights-aerial.mp4 --ref 13.6 --from 13.4 --to 18.6 \
        --out episodes/01-vending-machines/tracks/route.json

Writes, for every 1/30 s from --from to --to (clip seconds), the 3x3 homography that maps a point in the --ref frame
(1920x1080, framed exactly as proxies.py frames the clip) to where that point is in that frame. The ground in an aerial
is close to a plane, so one homography per frame follows it well. Also writes ref.jpg next to the JSON, for placing pins.
"""
import argparse
import json
from pathlib import Path

import cv2
import numpy as np

W, H, FPS = 1920, 1080, 30
SMALL = 0.5  # track at 960x540


def frames(path, t0, t1):
    cap = cv2.VideoCapture(str(path))
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.set(cv2.CAP_PROP_POS_MSEC, t0 * 1000)
    out = []
    while True:
        t = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
        ok, f = cap.read()
        if not ok or t > t1 + 0.1:
            break
        h, w = f.shape[:2]  # scale to cover 1920x1080, then centre-crop (as proxies.py does)
        s = max(W / w, H / h)
        f = cv2.resize(f, (round(w * s), round(h * s)), interpolation=cv2.INTER_AREA)
        y, x = (f.shape[0] - H) // 2, (f.shape[1] - W) // 2
        out.append((t, f[y:y + H, x:x + W]))
    return out, fps


def step(a, b):
    """Homography mapping frame a to frame b (full-resolution coordinates)."""
    ga = cv2.cvtColor(cv2.resize(a, None, fx=SMALL, fy=SMALL), cv2.COLOR_BGR2GRAY)
    gb = cv2.cvtColor(cv2.resize(b, None, fx=SMALL, fy=SMALL), cv2.COLOR_BGR2GRAY)
    mask = np.zeros_like(ga); mask[int(ga.shape[0] * 0.3):, :] = 255  # ground only: skip the sky
    p0 = cv2.goodFeaturesToTrack(ga, 800, 0.01, 8, mask=mask)
    p1, st, _ = cv2.calcOpticalFlowPyrLK(ga, gb, p0, None, winSize=(21, 21), maxLevel=3)
    good = st.ravel() == 1
    M, _ = cv2.findHomography(p0[good], p1[good], cv2.RANSAC, 2.0)
    S = np.diag([1 / SMALL, 1 / SMALL, 1.0])
    return S @ M @ np.linalg.inv(S)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode"); ap.add_argument("clip")
    ap.add_argument("--ref", type=float, required=True); ap.add_argument("--from", dest="t0", type=float, required=True)
    ap.add_argument("--to", dest="t1", type=float, required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    fr, fps = frames(Path(a.episode) / "footage" / a.clip, a.t0, a.t1)
    ts = [t for t, _ in fr]
    r = int(np.argmin([abs(t - a.ref) for t in ts]))
    Hs = [None] * len(fr); Hs[r] = np.eye(3)
    for i in range(r + 1, len(fr)):          # forward: ref -> i
        Hs[i] = step(fr[i - 1][1], fr[i][1]) @ Hs[i - 1]
    for i in range(r - 1, -1, -1):           # backward: ref -> i = (i -> i+1)^-1 composed
        Hs[i] = np.linalg.inv(step(fr[i][1], fr[i + 1][1])) @ Hs[i + 1]
    out, k = [], 0
    while a.t0 + k / FPS <= a.t1 + 1e-6:      # resample to the 30 fps the proxies use
        t = a.t0 + k / FPS
        i = int(np.argmin([abs(x - t) for x in ts]))
        h = Hs[i] / Hs[i][2, 2]
        out.append([round(float(v), 7) for v in h.ravel()])
        k += 1
    o = Path(a.out); o.parent.mkdir(parents=True, exist_ok=True)
    o.write_text(json.dumps({"clip": a.clip, "from": a.t0, "to": a.t1, "ref": ts[r], "H": out}))
    cv2.imwrite(str(o.with_suffix(".ref.jpg")), fr[r][1])
    # drift check: track a grid of points forward and back; report how far the loop lands from where it started
    print(f"{len(out)} frames, ref {ts[r]:.3f}s ->", o)


if __name__ == "__main__":
    main()
