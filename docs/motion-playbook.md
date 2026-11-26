# Net to Owner: motion playbook

How the graphics in a Net to Owner video move. This is written for the AI editor that builds shots in
`tools/video/gfx/scenes.html`, so it explains things from the start and gives exact numbers: seconds, pixels,
easing curves, and which property animates. Every number is a default. Use it unless a shot has a stated reason not to.

Frame: 1920×1080 at 30 fps. Graphics are drawn by `draw(t)` (a pure function of time), so everything here is
written as "property X goes from A to B over N seconds with curve E". Never use CSS transitions, `@keyframes`,
`requestAnimationFrame` or the clock. The renderer screenshots `draw(t)` frame by frame, and anything not driven by `t` breaks.

Owner's rules still apply to everything below: Libre Caslon Display for numbers, Libre Franklin for labels, white text
only, never smaller than 46 px, square corners, no boxes or dark layers behind text on footage, and data colours
rose `#B65A86`, blue `#4F7EC2`, ochre `#B88E30`, teal `#16998A`, white, plus highlighter `#FFE14D`.

---

## 0. Why the current cut looks stuck (measured)

I ran every graphic shot of Episode 1 through the engine's own frame key. A frame counts as "moving" only if some
tween is changing; the key is what `render_gfx.js` uses to decide whether to copy the previous frame.

| What | Measured on Episode 1 |
|---|---|
| Graphic screen time | 525 s across 51 graphic shots |
| Time the graphic layer is frozen | **400 s (76%)**; the median shot is frozen 78% of its length |
| Shots with a frozen stretch of 5 s or more | 22 of 51 |
| Worst frozen stretches | #86 Split recap **15.1 s**, #27 Deal File 9.5 s (the *whole frame* is frozen: flat navy desk, no footage), #44 quote 8.5 s, #59 bars 8.1 s, #22 Split and #45 clipping 7.7 s |
| Hold after the last movement | #86 15.2 s, #44 8.6 s, #59 8.1 s, #82 7.4 s, #89 6.6 s, #26 6.4 s, #16 6.0 s |
| Wait before the first number | #19 bars: first bar at 6.1 s of an 18.6 s shot. #27 doc: highlight at 10.1 s of 12.2 s |

Backgrounds are not the problem. Every B shot's footage covers its full length (at most 1.47× slow-down, never a
freeze). The causes are in the graphic layer and the cuts:

1. **Nothing moves once an element lands.** The engine has entrances only: no camera, no parallax, no motion during a hold.
2. **Entrances are too small and too soft to read as motion.** `up` moves 30 px over 0.6 s with ease-in-out, so the
   first third barely moves. `pop` scales 0.98→1, a 2% change nobody can see. On a TV across the room these read as fades.
3. **No exits and no transitions.** Graphics vanish with the cut. The only transition is the background focus pull.
4. **The focus pull isn't really a focus pull.** `make_still_bg` cross-fades a pre-blurred copy over the sharp
   footage (alpha 0→1 in 0.6 s), so the middle frames show a ghosted double image instead of a lens racking.
5. **Background drift depends on shot length.** It is always 202 px in total: 41 px/s on a 5 s shot, 7 px/s
   (invisible) on the 28 s Split. It also moves the picture left, while text-left layouts want to drift right.
6. **The route line is too thin.** A 12 px yellow line with a 22 px navy edge at 75% is 0.6% of the frame width.
   After YouTube compression it melts into the rooftops ("barely visible").
7. **Spoken items get no visual event** ("you're not showing what the video is saying"). In #86 the voice walks
   through the supplier, the building, the payment companies and the operator, but the Split is complete at 0 s and does
   nothing. In #44 the quote is fully on screen at 1.3 s while it is read for about 4 s.
8. **Consecutive shots restart.** #23 re-wipes the Split bar that #22 just showed, and its background jumps back
   to the start of the bottling-line clip. In #7 none of the three pitch lines has `strikeAt` or `strikeDelay`,
   so with the current code none of them is ever struck.

### Words used below
- **Tween**: one property changing over time, e.g. opacity 0→1 over 0.5 s.
- **Easing**: how speed changes during a tween. *Out* starts fast and slows into place (use it for arrivals).
  *In* starts slow and speeds away (use it for exits). *In-out* is slow, then fast, then slow (moving from one resting place
  to another). *Linear* is constant speed (only for continuous drift).
- **Stagger**: the delay between similar items starting.
- **Cue**: the moment a word is spoken. In the engine, a cue is the word's start plus 0.2 s (`CUE_DELAY`).
- **Hold**: the time after a graphic has built while the voice keeps talking.
- **Camera move**: moving or scaling the whole graphic as if a camera were drifting or pushing in.
- **Parallax**: layers at different depths move by different amounts during a camera move, with near layers moving more.
  It makes a flat graphic feel like a physical space.
- **Rack focus**: the lens pulling the background from sharp to soft, or back.

---

## 1. Motion principles

### 1.1 Calm, but always alive: three clocks
A graphic shot has three independent clocks. **At least one is moving in every frame, and the first two never stop.**

| Clock | What it is | Rule |
|---|---|---|
| Footage | The background footage plays | Never a still frame. A still (`routeMap`) must carry a camera move. |
| Camera | The whole graphic drifts and pushes in, slowly | Starts on frame 0, never stops, never reverses within a shot |
| Events | Something new appears, counts, highlights, or the camera reframes | **No more than 2.5 s without an event**, and every event is tied to a word |

*Calm* comes from slow camera speeds (8 px/s at most), short decisive entrances (0.6–0.9 s), one hero move at a time, and no
bounce, whoosh, spin or flash. *Alive* comes from the three clocks never all stopping.

### 1.2 Motion tokens: the defaults

**Easing.** The engine uses the JS functions; the CSS values are for reference only.

| Name | JS (p = 0..1) | CSS equivalent | Use for |
|---|---|---|---|
| `out` (expo) | `1 - 2^(-10p)` | `cubic-bezier(.16,1,.3,1)` | Arrivals: text, numbers, paper, count-ups |
| `outQuint` | `1 - (1-p)^5` | `cubic-bezier(.22,1,.36,1)` | Things that grow: bars, rules, leader lines |
| `outCubic` | `1 - (1-p)^3` | `cubic-bezier(.33,1,.68,1)` | Opacity |
| `in` (cubic) | `p^3` | `cubic-bezier(.32,0,.67,0)` | Exits |
| `inOut` (cubic) | the current `ease` | `cubic-bezier(.65,0,.35,1)` | A move from one resting place to another (a slice detaching, re-layout) |
| `sine` (in-out) | `-(cos(πp)-1)/2` | `cubic-bezier(.37,0,.63,1)` | Camera reframes, route drawing, highlighter, wipes |
| `linear` | `p` | `linear` | Continuous drift and push only |

Never use linear for an entrance, bounce or elastic curves, or overshoot on text. Pins and dots may overshoot by up to 8%.

**Durations**

| Token | Seconds | Use |
|---|---|---|
| xs | 0.25 | Opacity of small marks (pins, dots), word reveals |
| s | 0.35–0.45 | Exits, short highlights, label fades |
| m | 0.6–0.7 | Text and number rise, rules |
| l | 0.9–1.0 | Bars, paper landing |
| xl | 1.2–1.4 | Count-ups, ring arc, camera reframes |
| Drawn path | length ÷ speed, clamped to 1.2–4.5 s | Routes (700 px/s), chart lines (900 px/s) |
| Drift, push | the whole shot | Camera |

**Distances** (at 1920×1080)

| Move | Distance |
|---|---|
| Label rise | 32 px |
| Number or line rise | 48 px (64 px for serif text 150 px or larger) |
| Word reveal (quotes) | 14 px |
| Paper landing | 140 px plus a 3° turn |
| Exit | 20–24 px up |
| Replacing one item with the next | old item goes up 32 px, new item rises 48 px |
| Blur on arrival | 6 px → 0 over 0.45 s (text) |
| Camera drift | 6 px/s, at most 48 px per shot |
| Camera push | 0.35% per second, at most 3% per shot |
| Camera reframe | 12–35% of the way to the target, ≤ 60 px, +0.5% to +4% scale |
| Document read-push | up to +12% |

**Stagger**

| Situation | Stagger |
|---|---|
| Parts of one element | rule at t0 → text +0.12 s → number or count +0.1 s → sub +0.25 s → source +0.9 s |
| Siblings with no cue of their own | 0.12 s each (up to 5 items), 0.08 s (6–12) |
| Large sets (dots, grids) | the whole set spreads over 0.8–1.2 s, whatever the count |
| Items with their own cues | on the cue. If two cues fall less than 0.3 s apart, push the second to +0.3 s |
| Exits | near layer first, then mid, then far, 0.05 s apart |

**Speed limits.** Text never moves faster than 1500 px/s at its peak. The camera never drifts faster than 8 px/s.
Anything moving more than 40 px in one frame gets 4–6 px of blur while it moves. At 30 fps it otherwise strobes.

### 1.3 What moves during a hold, and what never does
**Keeps moving:** the footage; the camera drift and push (all layers); camera reframes on cues; markers that
are not text (the light pulse on a route, a ring pulse on an end dot every 2.4 s, the active-row marker sliding);
highlighter sweeps; shapes stepping back and forward (spotlight, 2.11).

**Never moves after it lands:** the glyphs of text and numbers. No wobble, pulse, shimmer, glow, colour cycling or
re-counting. Source lines sit on the "glass", outside the camera, and never move. Nothing goes in the bottom 15% (y > 918).

**Timing rules for every graphic shot**
- **Lead-in:** the first data element lands within 1.5 s of the cut. If the script needs a longer lead, start the
  graphic shot later (stay on footage longer) or draw the scaffolding first (axis, empty tracks, outlines) at 0.3–0.6 s.
- **No gap over 2.5 s** without an event (a new element, a count, a highlight, a spotlight change, a camera reframe).
  Drift and push stop the picture looking frozen, but they don't count as events.
- **Tail:** after the last event, hold for at most 3 s. That is long enough to read the last element (1 s + 0.3 s per word).
  After that, cut back to footage or add a closing event: a recap spotlight, or a pull-back of 1.5 s.

### 1.4 Camera moves on graphics
The graphic lives in a camera group (`#cam`). Moving the group is the camera.

| Move | Spec |
|---|---|
| Drift | Linear, 6 px/s, at most 48 px per shot. Moves toward the side with more empty space (text-left layouts drift right). Never toward an edge. |
| Push | Linear scale +0.35% per second, at most +3% (B, G and D shots) or +1.5% (text on footage). The origin is the centre of the content, so it grows in place. |
| Reframe on a cue | `sine`, 1.2–1.6 s, starting with the new element. Move 12–35% of the way toward its centre, +0.5% to +4% scale. At most one reframe starting every 2 s. |
| Document read-push | Toward each highlight: 50% of the way, +8–12% scale, 1.4 s `sine`, starting 0.3 s before the sweep |
| Pull-back (optional) | −2% over 1.5 s before a long tail ends |
| Safe area | Content stays 96 px from the sides and above y = 918. The camera code limits push and drift to fit, and the prototype held 98 px on the full-width Split. |
| Text on footage (GF) | Push only (≤ 1.5%), or drift in the *same* direction the footage pans. Never against the footage. |
| Still image (`routeMap`) | Arrive with a 1.14→1.0 zoom over 1.0 s `out`, then +6% over the shot plus a 30 px pan toward the route. The route sits inside the image's group, so it sticks to the ground. |

### 1.5 Parallax
Four planes. When the camera drifts by x, each layer moves by x × depth (scale works the same way).

| Layer | Depth | What goes on it |
|---|---|---|
| Glass | 0 | Source lines, anything that must stay put |
| Far | 0.7 | Rules, axes, empty tracks, outlines, the big quote mark, ghost bars, grids |
| Mid | 1.0 | Labels, bars, numbers, lists (the default) |
| Near | 1.25 | Paper documents, hero numbers in a sky, pins and markers on a route |

The blurred footage behind a B graphic is the farthest plane. It drifts **the same way** as the graphic at about half the speed
(3 px/s), plus its own motion. Today it drifts the opposite way, which feels like sliding rather than depth. Keep depth
differences small (0.7 to 1.25). The aim is a felt sense of space, not a visible 3D effect.

### 1.6 Showing what the voice is saying
- **One spoken item, one visual event.** If the voice names five things, the screen has five events.
- An element starts on its cue (word start + 0.2 s). An `out` count-up reaches 90% of its value 0.4 s after it starts,
  so the number is readable while the word is still being said.
- **Never show a number before it is spoken.** Scaffolding (axes, outlines, empty tracks) may appear early.
- Strikes and highlights land at the *end* of the phrase they react to, plus 0.2 s.
- When the voice moves to an item that is already on screen, the item gets the event: the spotlight (2.11) or a camera reframe.
- Quotes are revealed word by word as they are read (2.3).

### 1.7 Built for a TV
- Line weights on 1920×1080: rules ≥ 4 px (6 px for coloured data rules), chart lines 8–10 px, routes on aerials
  16 px with a 34 px edge. A 2 px line vanishes after compression.
- Never scale text below 0.94 of its size (the 46 px floor holds during animation).
- Text always ends at 100% white. Never leave text at partial opacity: it reads as grey, which breaks "white text only".
  To step an item back, dim *shapes* only (2.11).

### 1.8 Never
Whip pans, spins, flips, zoom-punches, camera shake, glitch, light leaks, film burns, lens flares, a whoosh on every cut
(the style guide already bans these). Also never: ffmpeg's built-in `circlecrop`, `pixelize`, `radial` or `slide*`
transitions (they are linear and look like templates), bouncing text, typewriter text, text that keeps pulsing, rounded
"pill" shapes, or dark plates behind text on footage.

---

## 2. Entrances, builds and exits: recipes

Format: **property: from → to, duration, easing, start**. t0 is the element's cue.

### 2.1 Hero numbers (Libre Caslon Display, 120–230 px)
- opacity: 0 → 1, 0.35 s, `outCubic`, t0
- translateY: +48 px → 0 (+64 px if 180 px or larger), 0.7 s, `out`, t0
- filter blur: 6 px → 0, 0.45 s, linear, t0
- **Count-up**, if the number is spoken: from 0 (or from the previous value when a number changes) to the target, 1.2 s (0.9 s
  below 10), `out`, t0. Prefix and suffix (`$`, `¢`, `%`, `B`) stay fixed. The decimals stay at full width (tabular numerals
  are already on). Don't count years, ranges, "~" values or anything not spoken.
- **Accountant's double underline** (net or final figures only: "$197 kept", "nets $20–175", "2.8×"): two white
  rules, 5 px each, 9 px apart, as wide as the number. scaleX 0 → 1 from the left, 0.5 s `outQuint`, starting at
  t0 + 0.9 (as the count lands), the second rule 0.1 s after the first. It is the brand mark for a final figure (see the logo).

### 2.2 Labels, kickers, sublines (Libre Franklin, 46–58 px)
- opacity 0 → 1, 0.35 s `outCubic`; translateY +32 px → 0, 0.6 s `out`; blur 4 px → 0, 0.35 s.
- A label under a number: t0 + 0.25. A sub: t0 + 0.5. A source: on the glass, fade 0.6 s at t0 + 0.9.
- A kicker that isn't spoken: t0 − 0.15, just ahead of its number. A spoken kicker: on its cue.
- Labels on several lines go line by line, 0.08 s apart.

### 2.3 Names, headlines and quotes
- **Masked rise** (company names, chapter-like titles): the line rises from behind its own baseline. Wrap it in a clip,
  translateY 120% → 0, 0.7 s `out`. No opacity fade is needed, because the clip hides it.
- **Tracking settle** at the same time: letter-spacing +6 px → −1 px over 1.2 s `out`. This is the premium title move.
- **Quote, word by word**: each word gets opacity 0 → 1, 0.25 s, and translateY +14 px → 0, 0.45 s `out`, starting
  0.05 s after it is spoken. Times come from the voiceover span of the quote, spread by characters (see change 9).
  Unrevealed words are hidden, not grey.

### 2.4 Rules and hairlines
- scaleX 0 → 1 from the left, 0.6 s `outQuint` (0.5 s under 400 px, 0.8 s over 1200 px).
- A rule always draws **before** the text it introduces: the rule at t0, the text at t0 + 0.12.
- Weight ≥ 4 px on footage. Coloured data rules are 6 px.

### 2.5 Bars
- scaleX 0 → 1 from the baseline, 1.0 s `outQuint` (0.8 s for bars under 300 px; never more than 1.2 s), at t0 + 0.1.
- **The value rides the tip of the bar.** translateX follows the bar's width on the same curve, and the value counts up on that curve too.
  Its opacity goes 0 → 1 in the first 0.12 s. (Prototyped and working: see 5.6.)
- Range bars: the pale part (35%) grows first, over 0.6 s. The solid part starts 0.1 s later.
- Several bars on one cue: 0.15 s stagger.
- An unknown value ("That airport"): a 4 px dashed outline bar grows past the right edge of the frame over 1.4 s `outQuint`,
  and the camera reframes 40 px toward it. That is "bigger still", shown.

### 2.6 Lines and routes (SVG paths)
- Draw with `stroke-dashoffset` at a steady speed: 700 px/s on aerials, 900 px/s for chart lines. `sine` overall.
  Duration = length ÷ speed, clamped to 1.2–4.5 s.
- **Route on an aerial**: a 16 px `#FFE14D` line over a 34 px navy edge at 0.55 opacity, round joins, glow
  `drop-shadow(0 0 10px rgba(255,225,77,.55))`. While it starts, grade the photo down: brightness 1 → 0.85,
  saturation 1 → 0.8, 0.8 s. That grades the whole picture; it is not a layer behind text.
- **Head**: a 28 px white dot with a 6 px yellow ring rides the tip (`getPointAtLength`). It fades 0.3 s after the line completes.
- **Stops timed to the voice**: the head arrives at each named stop 0.3 s before its word and eases in and out of
  the stop (`sine` between stops), like the van stopping there.
- **After a loop closes** (+0.4 s): a 160 px white light pulse at 0.9 opacity travels the loop at 600 px/s for
  the rest of the shot. It shows "drives a loop" and keeps the hold alive.
- Chart lines (growth): the head dot carries the value label, counting as it climbs (4.13).

### 2.7 Pins, dots and markers
- Pin: scale 0.6 → 1, 0.35 s `outQuint`, when the head reaches it, plus one ring pulse: a 4 px ring scales 1 → 2.4 while its
  opacity goes 0.8 → 0, 0.9 s `outCubic`.
- Dot fields: scale 0.6 → 1, 0.25 s, with the whole set spread over 0.8–1.2 s in order of distance from the cluster
  centre (a ripple), not left-to-right.
- End-of-line marker during a hold: a ring pulse every 2.4 s. It is the only thing allowed to pulse.

### 2.8 Paper (doc, receipt, clipping, papers) and the highlighter
- **Landing**: translateY +140 px → 0 and rotate (final − 3°) → final, 0.9 s `out`. Opacity 0 → 1 over 0.3 s. The shadow
  tightens as it settles: `0 50px 120px rgba(0,0,0,.35)` → `0 30px 80px rgba(0,0,0,.55)` (prototyped as `anim: 'land'`).
- **Hold**: the paper keeps turning by +0.04° per second (at most 0.5°), and the camera read-pushes (1.4).
- **Highlighter sweep**: left to right at 900 px/s (0.5–1.2 s), `sine`. Multi-line phrases sweep line by line
  (the current inline gradient already does this). The camera starts moving to the phrase 0.3 s before the sweep.
- **Exit**: translateY 0 → +80 px and opacity → 0, 0.4 s `in`.

### 2.9 Lists (ranked, columns, receipt lines, costs)
- Each item: its rule draws (0.5 s `outQuint`), the content rises at +0.1 s (0.6 s `out`), and the number counts at +0.1 s.
- Items with no cue of their own: 0.12 s stagger.
- The voice's place in the list is shown by the active marker (2.11), never by greying text.

### 2.10 Replacing one item with the next (num items, strike lines)
- Outgoing: opacity → 0, translateY 0 → −32 px, blur 0 → 6 px, 0.35 s `in`, starting at the next cue − 0.15.
- Incoming: the normal rise (2.1 or 2.2) at the next cue − 0.05, so the two overlap by about 0.25 s. It reads as one roll, not a blink.

### 2.11 Spotlight: which item the voice is on
- **Shapes** (bars, slices, dots): when a later item is spoken, the earlier ones step back to filter `opacity(0.4)`
  over 0.4 s `sine`. At the summary phrase they all return over 0.5 s. Use the CSS *filter* opacity, so it never
  conflicts with the entrance tween's own opacity. Opacity keeps the hue; saturate plus brightness turned the rose bar muddy brown in testing.
- **Text** (lists, rows): never dim it. A 6 px bar in the item's colour, as tall as the row, sits 28 px left of the
  text and slides to the row being spoken, 0.6 s `out`. For columns, the spoken column's top rule thickens 6 → 12 px (0.4 s `outQuint`).
- Rows that appear without being spoken don't take the marker.

### 2.12 Exits
- At the end of a shot, unless the next shot continues the graphic: the whole group exits over the last 0.45 s.
  Opacity → 0, translateY 0 → −20 px, blur 0 → 6 px, `in`, with the near layer first, then mid and far 0.05 s apart. Source lines
  fade with it. (Prototyped inside the camera code; see 5.1.)
- Paper exits downward instead (2.8).
- Exits are always faster than entrances (about 60% of the length) and always use `in`.

---

## 3. Transitions

### 3.1 Which transition, where

| From → to | Transition | Length | How it looks |
|---|---|---|---|
| Footage → footage | **Cut on the word** (default) | 0 | The backbone of the edit |
| Footage → footage, time jump or archive (e.g. "And none of this is new", 1929 film) | **Dissolve** | 0.5 s | Soft cross-fade |
| Chapter change (12 per episode at most) | **Ledger wipe** | 0.7 s | A 6 px white hairline crosses the frame left to right (`sine`), revealing the next shot behind it. The one branded transition. |
| Footage → text on footage (GF) | None | 0 | The number enters on its cue |
| Footage → graphic on its own background (B) | **Rack in** | 0.6 s | The background *continues the clip that was just playing* (no cut), the lens racks to soft (σ 0 → 18) and dims (1 → 0.42), `sine`. The first graphic element lands no earlier than 0.25 s. |
| Graphic (B) → footage | **Rack out** | 0.45 + 0.5 s | The graphic exits over the last 0.45 s. The next footage starts soft and dim, and racks to sharp over 0.5 s. Both sides of the cut are soft, so it reads as one focus move. |
| Graphic → the same graphic (#22 → #23) | **Carry** | 0 | Nothing restarts: the elements stay, the background clip continues, the camera continues, and new elements enter on cue |
| Graphic → a different graphic | **Hand-off** | 0.6 s | A exits (0.45 s). B's background starts already soft and dissolves from A's (0.6 s, no second rack). B's elements enter from 0.3 s. |
| Anything → Deal File (D) | **Paper lands** | 0.9 s | The previous footage continues, racked deeper (σ 22, dim 0.32), and the paper lands at 0.15 s. This replaces the flat navy desk. |
| Deal File → footage | Paper exits down (0.4 s) + rack out | 0.4 + 0.5 s | |
| Aerial footage → route map (G) | **Match frame** | 0 | The still is the last frame of the aerial, so the first frame matches exactly. Then the camera pushes. |
| Last shot → end screen | **Dip to navy** | 0.8 s | Fade to `#0B1422`, then the wordmark rises (0.8 s `out`) |

### 3.2 Rack in, built as a real focus pull (`proxies.py`)
Drive `gblur` sigma, the dim and the saturation per frame with `sendcmd`. This is verified on ffmpeg 6.1 here:
frame 0 is sharp, frame 9 half soft, frame 18 fully soft and dim, with no ghosting.

```python
import math

def rack_cmds(path, start=0.0, dur=0.6, sigma=18.0, dim=0.42, sat=0.75, opening=False):
    """sendcmd lines that pull focus sharp -> soft and dim (or soft -> sharp when opening). easeInOutSine."""
    n = max(1, round(dur * FPS))
    lines = []
    for f in range(n + 1):
        e = -(math.cos(math.pi * f / n) - 1) / 2 if dur > 0 else 1.0
        if opening:
            e = 1 - e
        d = 1 - (1 - dim) * e
        lines.append(f"{start + f / FPS:.4f} gblur sigma {0.01 + sigma * e:.3f}, colorchannelmixer rr {d:.3f}, "
                     f"colorchannelmixer gg {d:.3f}, colorchannelmixer bb {d:.3f}, eq saturation {1 - (1 - sat) * e:.3f};")
    Path(path).write_text("\n".join(lines))
```

In `make_still_bg`, replace the three chains from `split[a][b]` onward (the blurred copy, its alpha fade, and the crop) with:

```python
cmd_file = out.with_suffix(".rack.txt")
rack_cmds(cmd_file, dur=0.6 if s.get("rack", True) else 0.0)          # rack=False: start already soft (hand-off)
v = min(3.0, (2208 - 1920) / dur)       # px/s: half the graphic's 6 px/s (it is farther away), constant, not tied to shot length
chains.append(f"[{lastl}]trim=duration={dur:.3f},setpts=PTS-STARTPTS,sendcmd=f={cmd_file},"
              f"gblur=sigma=0.01:steps=2,colorchannelmixer=rr=1:gg=1:bb=1,eq=saturation=1,"
              f"crop=1920:1080:x='(iw-1920)-{v:.3f}*t':y=(ih-1080)/2,format=yuv420p[v]")  # picture moves right, with the text
```

`gblur` σ 18–22 matches today's `boxblur` radius 22. Check it once side by side. On a blurred background, the 1 px steps of an integer
crop can't be seen. For a push-in on **sharp** footage, use `perspective` with `eval=frame` instead: it samples at
sub-pixel positions and doesn't jitter (verified here). For example, zoom z = 1 + 0.015·t:

```
perspective=x0='W*(1-1/Z)/2':y0='H*(1-1/Z)/2':x1='W-W*(1-1/Z)/2':y1='H*(1-1/Z)/2':x2='W*(1-1/Z)/2':y2='H-H*(1-1/Z)/2':x3='W-W*(1-1/Z)/2':y3='H-H*(1-1/Z)/2':interpolation=linear:eval=frame
```
with every `Z` written out as `(1+0.015*in/30)` (`in` is the frame number).

### 3.3 Continue the clip that was just playing (`stills.resolve`)
Let a B or D shot say `bg="prev"`, and work out where the previous shot's footage ended:

```python
for i, s in enumerate(shots):
    prev = shots[i - 1] if i else None
    if s.get("bg") == "prev" and prev:
        if prev.get("clip"):
            s["bg"] = (prev["clip"], (prev.get("in") or 0.0) + prev["dur"])
        elif prev.get("clips"):                         # last piece of a chained shot
            f, t_in, *_ = prev["clips"][-1]
            fixed = sum(p[2] for p in prev["clips"][:-1] if len(p) > 2 and p[2])
            s["bg"] = (f, t_in + prev["dur"] - fixed + 0.5 * (len(prev["clips"]) - 1))
```
This assumes no slow-down, which holds whenever the clip is long enough (slow = 1). Use it for most F → B pairs. The cut then
becomes a focus pull on the same moving picture. #2 → #3 is nearly there by hand: same clip, but it jumps 0.6 s ahead (5.4 s → 6.0 s).

### 3.4 Rack out (`make_bg`)
When a footage shot follows a B or D shot, set `rack_open=0.5` (or have `resolve` set it), and add before
`chains.append(f"{tail}null[v]")`:

```python
if s.get("rack_open"):
    ro = s["rack_open"]; cmd_file = out.with_suffix(".open.txt")
    rack_cmds(cmd_file, dur=ro, opening=True)
    chains.append(f"{tail}sendcmd=f={cmd_file},gblur=sigma=18:steps=2:enable='lt(t,{ro + 0.05:.2f})',"
                  f"colorchannelmixer=rr=.42:gg=.42:bb=.42:enable='lt(t,{ro + 0.05:.2f})',"
                  f"eq=saturation=.75:enable='lt(t,{ro + 0.05:.2f})'[ro]")
    tail = "[ro]"
```

### 3.5 Dissolve between footage shots, with no change to `render.py`
`make_bg` already cross-fades chained pieces (`XF = 0.5`). To dissolve into shot B, start B's `clips` with 0.5 s of the
previous clip, continuing from where it ended:
`clips=[(prev_clip, prev_end, 0.5), (clip, in, None)]`. The fade runs over B's first 0.5 s, starting from the exact frame
the previous shot ended on. `resolve` can build this from a flag such as `xin=0.5`.

### 3.6 Hand-off between two graphics (`make_still_bg`)
Let a `bg` piece carry its own length, as `clips` pieces do: `bg=[(prev_bg_clip, prev_end, 0.6), (clip, t)]`.
Also set `rack=False`, so B's background starts soft and dissolves from A's soft background without a second rack.

### 3.7 Carry (the same graphic across a cut)
The best fix is **one shot, not two**: merge #22 and #23 into one Split with `costs` cues and a chained `bg`. The engine
supports that already, and what the owner has seen doesn't change. If they must stay two shots, mark the second `carry=True`.
`setup()` then starts every entrance tween at or before 0.05 s already finished:

```js
if (scene.carry) TWEENS.forEach(tw => { if (!tw.live && tw.node !== CAM && cue(tw.at) <= 0.05) tw.at = -100; });
```

Also: the first shot gets `exit: false`; the second gets `bg="prev"` and `rack=False`, and starts its camera where the first
ended. Have `render_gfx.js` save the last camera offset to `g{n}/cam.json`, and read it in `startCamera` as the starting offset.

### 3.8 Ledger wipe at chapter changes (`render.py`)
This needs overlap. Render the outgoing shot 0.7 s longer (its background continues, and its graphic has already exited), then
join the pair with an eased custom `xfade` plus a hairline that rides the wipe edge. Verified on ffmpeg 6.1: in a
custom `xfade`, **`P` runs from 1 to 0**, and this expression reveals B from the left with `sine` easing. `drawbox` does
*not* re-evaluate `t` on each frame, so the hairline is an `overlay` of a 6 px colour strip.

```python
WIPE = 0.7
EXPR = "if(lt(X, W*(0.5-0.5*cos(PI*(1-P)))), B, A)"
def ledger_wipe(a_with_handle, b, dur_a, out):        # B starts exactly at dur_a: timing is unchanged
    edge = f"W*(0.5-0.5*cos(PI*min(1,max(0,(t-{dur_a:.3f})/{WIPE}))))-3"
    fc = (f"[0:v][1:v]xfade=transition=custom:duration={WIPE}:offset={dur_a:.3f}:expr='{EXPR}'[w];"
          f"color=c=white:s=6x1080:r={FPS}:d={dur_a + WIPE + 1:.3f}[line];"
          f"[w][line]overlay=x='{edge}':y=0:enable='between(t,{dur_a:.3f},{dur_a + WIPE:.3f})'[v]")
    run(["ffmpeg", "-v", "error", "-y", "-i", str(a_with_handle), "-i", str(b), "-filter_complex", fc, "-map", "[v]",
         "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", str(out)])
```
Replace the two segments in `list.txt` with the joined file. Its length is `dur_a + dur_b`, so the audio stays in sync.

### 3.9 The HTML side of every transition
The graphic's half of each transition is just its entrance (section 2) and its exit (2.12). `resolve` should tell each scene
what comes next, so the exit can be chosen: `scene.next = next_shot.kind` and `scene.exit = not next_shot.get("carry")`.

---

## 4. Template motion specs

For each template: what it does now (from the code, with the share of frozen frames measured on Episode 1), then the spec.
All of them also get the camera (1.4), parallax (1.5), the exit (2.12) and the timing rules (1.3).
Note: `bars`, `versus` and `quote` are defined twice in `scenes.html`. The TEMPLATE LIBRARY versions win (`Object.assign`), so edit those.

**num** (T1): #5, 13, 18, 43, 48, 56, 58, 67, 72, 89; frozen 71–92%
- Now: the number counts (in-out, 1.1 s) or rises 30 px over 0.6 s. The label fades at +0.3 s, the sub at +0.5 s, the source at +0.9 s.
  Several items replace each other with a 0.3 s fade.
- Spec: number per 2.1 (rise 48/64 px, `out` 0.7 s, blur-in, count 1.2 s `out`). Kicker 0.15 s ahead. Label rise at +0.25 s.
  Double underline for net figures (#67 "$20–175", the typical site nets). Items roll (2.10): #48 600,000+ → $4.6B, with the kicker changing alongside.
- Hold: B: drift + 3% push. GF: push only, 1.5%. #89 ("Would you still buy one?"): the two lines rise 0.1 s apart and don't count.

**tag** (T37): #34, 2.8 s
- Now: the 90 px rule grows 0.5 s, the title rises at +0.15 s, the sub fades at +0.4 s.
- Spec: rule (6 px) scaleX 0.5 s `outQuint`; title masked rise 0.6 s at +0.12 s; sub rise 32 px at +0.3 s.
  Exit in reverse over 0.3 s, with the rule retracting to the left (scaleX 1 → 0, `in`). Push 1%.

**routeMap** (T4): #15, 9.9 s; #77, 6.0 s; never frozen, but "barely visible"
- Now: the still zooms 1.14 → 1.0 over 0.9 s, then +5% over the shot. 12 px yellow line over a 22 px navy edge at 0.75,
  drawn over 3–4 s in-out. Pins fade in (a 2% "pop"). Stop labels rise on cue.
- Spec (prototyped; frames checked): the line weights, glow and grade from 2.6. Head marker; the head slows into each
  stop as the voice names it (#15: Restock, Pull cash, Fix what broke). Pins pop and ring (2.7). After the loop closes, a light
  pulse at 600 px/s. Stop labels: 32 px rise plus a 4 px leader tick, 0.3 s. Value (#77 $138,000): number recipe, on
  the near layer, so it parallaxes against the ground.
- Camera: 1.14 → 1.0 over 1.0 s `out`, then +6% and 30 px toward the route. Keep the loop above y = 918: #15's points reach y = 1010.
- Later, with the moving aerial: track four ground points (OpenCV optical flow plus `findHomography`) and apply the result
  each frame as a CSS `matrix3d`, so the route rides real drone footage.

**receipt** (T11): #21, 26, 61, 64; frozen 71–87%
- Now: the paper rises 30 px over 0.6 s. Lines fade in on cue and their values count. The total fades in, then the highlighter (0.7 s). The note fades.
- Spec: the paper lands (2.8). It **prints**: the paper's `height` (with `overflow:hidden`; the box-shadow follows) grows
  to show each new line, 0.45 s `outQuint`, so the receipt gets longer as the voice adds lines. Each line rises 16 px
  and fades, 0.4 s; values count 0.9 s `out` (ranges don't). Dashed rules draw left to right in 0.4 s. Total: rise, then
  the highlighter at +0.3 s (900 px/s), then the double underline at +0.9 s.
- Hold: the camera reframes to each new line (20% of the way, +1%) and to the total (35%, +4%). The paper turns 0.04°/s.

**bars** (T12): #19, 28, 55, 59; frozen 49–81%
- Now: the label fades on cue. The pale part grows 0.6 s, the bar grows 0.9 s in-out, and the value fades in at the end (+0.35 s).
- Spec (prototyped): 2.5. Label rise on cue; the bar grows 1.0 s `outQuint` at +0.1 s; the value rides the tip and counts.
  Spotlight (2.11): the earlier bars step back when the next one arrives, and come back at the summary (#59 "@But the
  fastest growth"). The camera reframes to each new bar (12%, +0.6%).
- #19 (first bar at 6.1 s): draw the three rows' 2 px tracks (white at 0.35, far layer, 0.12 s stagger) at 0.4 s, or
  start the shot at "@a typical site". #28: the locked bar becomes the dashed bar running off frame on "@bigger still".
  #59: the $6M bar is 8 px wide; keep the 8 px minimum, and the value still rides it.

**versus** (T14/T35): #30, 16.3 s; frozen 86%
- Now: the divider grows 0.6 s on A's cue. Columns A and B rise on their cues, and their values count.
- Spec: the divider (4 px, white at 0.6, far layer) draws from the top, 0.6 s `outQuint`, at A − 0.3 s. Each column: label rise
  on its cue, value rise 64 px plus a 1.2 s count at +0.1 s, sub at +0.35 s. On "@spend more", a 6 px rule in the
  winning side's colour grows under its value (0.6 s): the comparison, shown. Column A sits at depth 0.9 and B at 1.1, so they shear slightly
  as the camera drifts. The camera reframes to A, then to B (12%).

**strike** (T15): #7, on footage; frozen 78%
- Now: each line fades in over 0.4 s. It is struck (0.45 s) only if it has `strikeAt` or `strikeDelay`. Lines replace each other with a 0.3 s fade.
- Spec: masked rise of the line, 0.6 s. The strike lands at the end of the phrase + 0.2 s: the bar (size ÷ 12, at least 10 px) does
  scaleX 0 → 1 from the left, 0.45 s `outCubic`. **Every pitch line gets a strike.** Lines roll (2.10). Push 1%, no drift (it's on footage).

**company** (T16): #14, 8.3 s; #42, 5.2 s; frozen 74–78%
- Now: a 520×4 px rule grows 0.6 s, the names rise on cue, the lines fade in on cue, and then nothing.
- Spec (masked rise and tracking prototyped): rule 0.6 s `outQuint` at the cue − 0.15 s. Each name: masked rise 0.7 s plus
  tracking settle +6 → −1 px over 1.2 s (2.3). Line: rise 32 px on cue.
- Showing what's said: in #14, on "@small, local businesses", 200 white dots (10 px, far layer) pop across the right 55% of the
  frame in random order over 2.0 s. The map fills with small operators while the two giants stay. In #42, on
  "@Compass Group", a 4 px line draws down from "Canteen" (0.5 s) just before "Owned by Compass Group" rises: ownership, shown.
- Hold: the rule on the far layer, the names on mid; the drift goes right, into the empty space.

**columns** (T17): #16, 17.7 s; #32; #87; frozen 74–79%
- Now: the rule grows 0.5 s and the block rises at +0.12 s on cue. Values count.
- Spec: rule 6 px, 0.5 s `outQuint`. Label rise at +0.1 s. Value rise 64 px with a 1.2 s count at +0.1 s. Sub at +0.3 s.
  Active column: its rule thickens 6 → 12 px (0.4 s) while the previous one returns to 6 px. Depths 0.9, 1.0, 1.1 from left to right.
  The camera reframes to each column (10%).
- #16's tail is 6 s: give the elevator machine its own event on "@gently lowers each item" (its rule thickens), or end the shot earlier.

**density** (T18): #40, 10.9 s; frozen 76%
- Now: the label fades in. The square frame fades in over 0.4 s. 100 dots pop 0.008 s apart; the 10 scattered dots pop 0.08 s apart.
- Spec: the frame *draws* (stroke-dashoffset around the square, 0.8 s `sine`) on its cue. Dense dots ripple out from the centre over
  1.0 s. Scattered dots 0.12 s apart. **Then show the driving**: on "@beats", a route through each frame's dots draws at the
  same 750 px/s in both frames. The dense one takes about 0.8 s and the scattered one about 3.5 s, so the viewer watches one van
  finish while the other is still driving. Use the head marker from 2.6, and a ring pulse on each route's last dot.

**ranked** (T19): #36, 6.2 s; frozen 47%
- Now: rows rise on cue, each with a 2 px top border at 40%.
- Spec (marker prototyped): the row rule (4 px) does scaleX 0.5 s; the numeral and name rise at +0.08 s; the value counts 1.0 s at +0.1 s.
  The active marker goes to the row the voice is talking about. In #36 that is row 2 on "@Canteen"; Gilly appears without the marker.
  The camera reframes to the row (12%).

**growth** (T20): #57, 6.2 s; frozen 45%
- Now: the start dot pops on A. The path draws 1.4 s in-out on B. The end dot pops at +1.3 s. The labels rise.
- Spec: the axis draws 0.6 s at 0.3 s. A: dot pop plus value rise. On B the curve draws 1.6 s `sine`, with the head dot
  riding the tip and **the value label riding above the head, counting 71 → 572 on the same curve**. The area under
  the curve (ochre, 25% fading to 0% top to bottom) fades in over 0.6 s after the line completes. End dot: a ring pulse every 2.4 s.

**equation** (T21): #76, 15.6 s; #78, 6.7 s; frozen 49–85%
- Now: terms rise on cue and operators fade in. The highlighted term is yellow.
- Spec: the camera reveals the equation. It starts at 1.10, centred on term 1. As each term arrives, it eases (1.2 s `sine`) to
  centre the terms shown so far, ending at 1.0. Operators: scale 0.6 → 1 plus a fade, 0.35 s `outQuint`, at the cue − 0.1 s.
  Terms: rise 64 px plus a 1.2 s count. Result: counts in yellow, then the double underline at +1.0 s.

**ring** (T22): #31, 4.1 s; frozen 62%
- Now: the SVG fades in over 0.3 s. The arc and the number run together over 1.2 s, in-out. The label rises at +0.4 s.
- Spec: the track circle (white at 20%) draws 0.5 s `sine` from the top. The arc grows 1.4 s `outQuint`, and the number counts on
  the *same* curve. An 18 px white head dot sits at the arc's tip. The label rises when the arc reaches 70% (+0.6 s). Hold: a ring
  pulse on the head dot. Never rotate the ring itself.

**clipping** (T23): #45, 51, 82; frozen 85–86%
- Now: the paper rises 30 px over 0.6 s. Highlights sweep for 0.8 s on cue.
- Spec: the paper lands (2.8; final turn +1.2°, starting 3° further round). The camera starts at 1.06 on the headline, then
  read-pushes to each highlight (50%, +8%, 1.4 s, 0.3 s before the sweep). Sweeps at 900 px/s. After the last highlight,
  pull back to 1.03 over 1.5 s. The paper exits downward.

**quote** (T24): #44, 66, 73; frozen 77–90%
- Now: the big quote mark fades in, the whole text rises 30 px, and the name fades in at +0.5 s. #44 is frozen from 1.3 s.
- Spec (word reveal prototyped): the quote mark (far layer) goes opacity 0 → 0.55 and scale 0.9 → 1, 0.6 s `out`, at the cue − 0.2 s. The text
  is revealed **word by word as it is read** (2.3), using the quote's spoken span. The name comes 0.4 s after the last word:
  a 4 px rule (0.5 s), then the name rises (0.6 s). Today the name lands at +0.8 s, before the quote is read; move it.
  Hold: 3% push.

**papers** (T8b): #8, 6.6 s; frozen 73%
- Now: three cards rise 30 px over 0.55 s on their cues, at fixed angles.
- Spec: **dealt in**. Each card lands from +200 px below, turned 6° further, 0.8 s `out`, and its shadow tightens. When a new card
  lands, the earlier ones settle back: scale 1 → 0.97 and +12 px down, over 0.4 s (no greying). Depths 1.0, 1.1, 1.2. Each turns 0.04°/s.

**months** (T41): #68, 11.7 s; frozen 84%
- Now: 20 squares fill 0.035 s apart on A. The outlined squares fade in row by row on B. The values rise.
- Spec: all 168 outlines (3 px teal, far layer) fade in row by row from 0.3 s (0.04 s per row). On "@20 months" the first 20
  fill white, 0.05 s apart (1.0 s), while "20 months" counts 0 → 20 in step. On "@14 years" the filling continues in teal
  from 21 to 168 over 2.4 s, slow to fast (`in`), and "14+ years" counts the years in step, landing as the last square fills.
  The slow fill makes the wait felt.

**split** (T9 + T7 tally): #3, 22, 23, 86; frozen 28–93%
- Now: the whole bar wipes in 0.7 s, then the slices wipe in 0.45 s each, 0.09 s apart. Slices are greyed until named, then brighten in
  0.35 s. Leader lines grow in 0.35 s; labels rise. The tally counts down 0.6 s per step. In #86 everything happens at 0 s.
- Spec: whole bar wipe 0.8 s `outQuint` on "$2". Slices as now. **A named slice gets a beat**: brighten 0.35 s (as now), plus a lift
  of 16 px and a settle (up 0.35 s `out`, back 0.55 s `inOut`). Its leader line grows 0.35 s, its label rises 32 px, and its amount counts.
  The tally ticks down on the same cue and curve (0.7 s `out`). The camera reframes toward the slice (12%, +0.5%).
- Fuller version for #22 (the deep dive), "pay-out": the named slice detaches 150 px down into a paid-out row (0.7 s `inOut`),
  leaving a 2 px outline in its colour. The owner's white slice is left alone in the bar: what's left, shown.
- #23: carry from #22 (3.7). Don't re-wipe the bar, and don't jump the background back to the start of the clip.
- #86 recap: give the slices cues from the narration ("@The supplier takes", "@The building takes", "@best buildings",
  "@payment companies", "@operator keeps"). Each gets the lift beat. "Operator keeps 62¢" gets the double underline. That turns a
  15 s freeze into 5 events.

**doc** (T8 Deal File): #27, 35, 83, 85; frozen 69–87%
- Now: a flat navy desk with static noise. The paper rises 30 px over 0.6 s. Highlights sweep for 0.9 s. #27 is frozen for 9.5 s, with the whole frame still.
- Spec (landing and highlight camera prototyped): background = the previous footage continuing, racked deeper
  (σ 22, dim 0.32), instead of the flat desk. Paper landing at 0.15 s (2.8). **Read-pan**: the camera starts at 1.08 on the header
  and moves down the text at reading pace, about 40 px/s, arriving at each highlight 0.3 s before its sweep (50%, +12%). Sweep at 900 px/s.
  After the last highlight: hold at least 1.5 s, pull back to 1.04 over 1.2 s, then the paper exits downward.
- #27: Riverside is named about 7 s into the shot. Either start the doc at "@One California" or let the read-pan carry the wait.
  #85 (3.0 s): landing, then the sweep at 0.5 s.

---

## 5. Ten implementation changes, ranked

Ranked by how much of "it's stuck" and "nothing is happening" each one fixes across the whole episode. The camera rig
and group exit (1, 3), easing and entrances (2), cue camera on bars and docs (4), `spot`/`marker` (5), bar-riding values (6),
the route drawing (7), paper landing and highlight camera (8), `wordsIn`/`maskRise` (9) and `motionReport` (10) were
**prototyped in a scratch copy of `scenes.html` and run against all 51 graphic shots of Episode 1**: no page errors,
51 of 51 shots never frozen (down from 76% frozen), content within the 96 px margins, and frames checked by eye
(bars, doc, Split, route, ranked, quote, company). Not yet run: rolls, carry, receipt printing, and the other templates'
reframes. `scenes.html` itself is unchanged.

### 1. A camera rig with parallax layers (fixes "stuck" in every shot)
`setup()` builds `#stage > #cam > far | mid | near`, plus a `GLASS` layer outside the camera. `S` (the default parent)
becomes the mid layer, so every template keeps working unchanged. The camera always drifts and pushes, limited to the safe area,
and the same code does the group exit.

```js
const ROOT = document.getElementById('stage');
let S = ROOT, CAM = null, LAYERS = {}, GLASS = ROOT, CAMKEYS = [], SC = {};

function camTo(at, dx = 0, dy = 0, ds = 0, dur = 1.4) { CAMKEYS.push({ at, dx, dy, ds, dur }); }
function focusOn(node, at, k = 0.35, ds = 0.04, dur = 1.4) {   // move the camera part of the way toward a node
  const r = node.getBoundingClientRect(); camTo(at, (960 - (r.left + r.width / 2)) * k, (540 - (r.top + r.height / 2)) * k * 0.6, ds, dur); }

function startCamera(sc, p) {
  const D = sc.dur || 8, SAFE = 96;
  const rs = [...S.children].map(c => c.getBoundingClientRect()).filter(r => r.width && r.height);
  const L = rs.length ? Math.min(...rs.map(r => r.left)) : 760, R = rs.length ? Math.max(...rs.map(r => r.right)) : 1160;
  const T = rs.length ? Math.min(...rs.map(r => r.top)) : 440, B = rs.length ? Math.max(...rs.map(r => r.bottom)) : 640;
  const ox = (L + R) / 2, oy = (T + B) / 2;                       // push from the content's centre: it grows in place
  let push = p.push ?? Math.min(0.03, 0.0035 * D);                // 0.35%/s, at most 3%, never past the safe margins
  push = Math.max(0, Math.min(push, (ox - SAFE) / (ox - L || 1) - 1, (1920 - SAFE - ox) / (R - ox || 1) - 1, (918 - oy) / (B - oy || 1) - 1));
  const roomL = ox - (ox - L) * (1 + push) - SAFE, roomR = 1920 - SAFE - (ox + (R - ox) * (1 + push));
  const want = p.drift ?? Math.min(48, 6 * D);                    // 6 px/s, at most 48 px, toward the emptier side
  const drift = roomR >= roomL ? -Math.min(want, Math.max(0, roomR)) : Math.min(want, Math.max(0, roomL));
  const exitAt = sc.exit === false ? Infinity : D - (sc.exitDur ?? 0.45);
  anim(CAM, { anim: 'fn', at: 0, dur: D, ease: false, fn: (pp, q, t) => {
    let x = -drift * pp, y = 0, s = 1 + push * pp;
    CAMKEYS.forEach(k => { const e = E.sine(clamp((t - cue(k.at)) / k.dur)); x += k.dx * e; y += k.dy * e; s += k.ds * e; });
    Object.values(LAYERS).forEach((Ly, i) => {                    // far, mid, near; near exits first
      const d = Ly.depth, xo = E.in(clamp((t - exitAt - (2 - i) * 0.05) / 0.35));
      Ly.style.transformOrigin = `${ox}px ${oy}px`;
      Ly.style.transform = `translate(${(x * d).toFixed(2)}px, ${(y * d - 20 * xo).toFixed(2)}px) scale(${(1 + (s - 1) * d).toFixed(5)})`;
      Ly.style.opacity = 1 - xo; Ly.style.filter = xo > 0.01 ? `blur(${(6 * xo).toFixed(2)}px)` : ''; });
    GLASS.style.opacity = 1 - E.in(clamp((t - exitAt) / 0.35));
  } });
}

window.setup = (scene) => {
  CUES = scene.cues || {}; TWEENS = []; CAMKEYS = []; ROOT.innerHTML = ''; SC = scene;
  if (scene.opaque) document.body.style.background = 'var(--bg)';
  CAM = el('<div id="cam" class="abs" style="left:0;top:0;width:1920px;height:1080px"></div>', ROOT);
  LAYERS = {};
  [['far', 0.7], ['mid', 1], ['near', 1.25]].forEach(([k, d]) => {
    LAYERS[k] = el('<div class="abs" style="left:0;top:0;width:1920px;height:1080px"></div>', CAM); LAYERS[k].depth = d; });
  GLASS = el('<div class="abs" style="left:0;top:0;width:1920px;height:1080px"></div>', ROOT);
  S = LAYERS.mid;
  SCENES[scene.type](scene.params || {}, scene); countUps();
  if (scene.camera !== false) startCamera(scene, scene.params || {});
  draw(0);
};
```
Then: `srcLine()` and `source()` append to `GLASS`. Give `blk()` an optional last argument `layer` ('far', 'mid' or 'near') and
place rules, tracks, outlines and quote marks on `far`, and paper and route values on `near`. GF shots pass `params.drift: 0`
and `push: 0.015`. Cost: every frame now changes, so the renderer screenshots all of them instead of copying about 76%.
Measured here at 45 ms a frame, that is about 16,000 graphic frames, roughly 4 extra minutes with the 3 existing workers.

### 2. An easing table and stronger entrances (every element)
Replace the single `ease` with a table, give each animation type its own default curve and duration, and make `up` a
real rise: a fast fade, a 48 px `out` settle, and blur-in. The same tween also does the exit roll (−24 px, blur) when `out` is set.

```js
const E = {
  linear: p => p,
  inOut: p => p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2,
  out: p => p >= 1 ? 1 : 1 - Math.pow(2, -10 * p),
  outQuint: p => 1 - Math.pow(1 - p, 5),
  outCubic: p => 1 - Math.pow(1 - p, 3),
  in: p => p * p * p,
  sine: p => -(Math.cos(Math.PI * p) - 1) / 2,
};
const ease = E.inOut;   // kept for old callers
const DEF = { fade: 'outCubic', up: 'out', rise: 'out', land: 'out', slide: 'out', pop: 'outQuint', wipe: 'outQuint',
              grow: 'outQuint', growY: 'outQuint', hl: 'sine', count: 'out', dim: 'outCubic', fn: 'inOut' };
const DUR = { fade: 0.5, up: 0.7, rise: 0.7, land: 0.9, pop: 0.5, wipe: 0.8, grow: 0.8, growY: 0.6, hl: 0.7, count: 1.2 };
function anim(node, opts) { const a = (opts && opts.anim) || 'fade';
  TWEENS.push(Object.assign({ node, anim: a, dur: DUR[a] ?? 0.5, at: 0, base: node.style.transform || '' }, opts)); return node; }

function apply(tw, t) {
  const a = cue(tw.at), raw = clamp((t - a) / tw.dur);
  const p = tw.ease === false ? raw : (E[tw.ease] || E[DEF[tw.anim]] || E.inOut)(raw);
  let q = 1; if (tw.out !== undefined) q = 1 - E.in(clamp((t - cue(tw.out)) / (tw.outDur || 0.35)));
  const n = tw.node, o = E.outCubic(clamp((t - a) / Math.min(tw.dur, 0.35))) * q;   // opacity lands fast, position keeps settling
  switch (tw.anim) {
    case 'up': case 'rise': { const b = Math.max(6 * (1 - clamp((t - a) / 0.45)), 6 * (1 - q));
      n.style.opacity = o; n.style.transform = `${tw.base} translateY(${(1 - p) * (tw.dist ?? 48) - (1 - q) * 24}px)`;
      n.style.filter = b > 0.05 && o > 0 ? `blur(${b.toFixed(2)}px)` : ''; break; }
    case 'land': { const r = tw.rot ?? 0, hold = Math.max(0, t - a - tw.dur);           // paper: 2.8
      n.style.opacity = o;
      n.style.transform = `translateY(${(1 - p) * (tw.dist ?? 140)}px) rotate(${(r + (1 - p) * (tw.turn ?? -3) + (tw.sway ?? 0.04) * hold).toFixed(3)}deg)`;
      n.style.boxShadow = `0 ${(50 - 20 * p).toFixed(1)}px ${(120 - 40 * p).toFixed(1)}px rgba(0,0,0,${(0.35 + 0.2 * p).toFixed(3)})`; break; }
    case 'pop': n.style.opacity = o; n.style.transform = `${tw.base} scale(${(tw.from ?? 0.6) + (1 - (tw.from ?? 0.6)) * p})`; break;
    // fade, slide, wipe, grow, growY, hl, count, dim, fn: unchanged
  }
  /* return key unchanged */
}
```
In `countUps()`, give the added tween `ease: false` and compute `num * E.out(pp)` inside it, with `dur` 1.2 s (0.9 s below 10).
Today it applies a cubic on top of the in-out ease. Use `pop` only for dots and pins. Never use it on text (1.7).

### 3. Exits, rolls and carry (fixes "where is some transition" on the graphic side)
- Group exit at the end of the shot: done inside `startCamera` (change 1). The scene skips it when `scene.exit === false`.
- In `stills.resolve`: set `scene.next`, `scene.exit` and `scene.carry` from the neighbouring shots (3.9), and accept
  `bg="prev"`, `rack_open` and `xin` (3.3–3.5).
- Rolls: in `num` (items) and `strike`, set `out: cue(next.at) - 0.15, outDur: 0.35` and start the next item at
  `cue(next.at) - 0.05`. The `rise` case above already moves the outgoing item up and blurs it.
- Carry: the one line in 3.7. Merge #22 and #23 into one shot.

### 4. A directed camera on cues (makes the camera follow the voice)
`camTo()` and `focusOn()` from change 1. Call `focusOn(node, cue)` wherever a new element arrives far from the current framing:
- bars: `if (i) focusOn(bar, t0, 0.12, 0.006, 1.2)` (prototyped)
- doc and clipping: for each `.hl`, call `focusOn(h, cue(h.dataset.cue) - 0.3, 0.5, 0.08, 1.4)` (prototyped). For the read-pan, set a
  starting framing on the header with a key that is already complete at frame 0 (`camTo(-1, dx, dy, 0.08, 0.1)`), then add a slow
  `camTo(0.3, 0, -40, 0, 6)` that travels down the text until the first highlight move takes over
- receipt lines and total, ranked rows, columns, versus, Split slices, equation terms: amounts as in section 4.
Keep reframes at least 2 s apart. If two arrive closer, drop the second.

### 5. Spotlight and marker (show which item is being spoken, without grey text)
Prototyped; the frames show the marker sliding to the spoken row and earlier bars stepping back with their hue kept.

```js
// Runs every frame for the whole shot (hold motion, markers). It reports motion, so frames aren't wrongly reused.
function live(fn, node = ROOT) { return anim(node, { anim: 'fn', at: 0, dur: SC.dur || 8, ease: false, live: true, fn: (pp, q, t) => fn(t) }); }

// Shapes only. When a later item is spoken, earlier ones step back to 40%; `restore` brings them all back.
function spot(items, restore) {               // items: [{node, at}] in spoken order
  const back = restore === undefined ? Infinity : cue(restore);
  items.forEach((it, i) => { const next = items[i + 1]; if (!next) return; const off = cue(next.at);
    live(t => { const d = E.sine(clamp((t - off) / 0.4)) * (1 - E.sine(clamp((t - back) / 0.5)));
      it.node.style.filter = d > 0.001 ? `opacity(${(1 - 0.6 * d).toFixed(3)})` : ''; }); });
}

// Text lists: a 6 px bar in the item's colour slides to the row being spoken. Text stays white.
function marker(rows, x = 112) {              // rows: [{node, at, key}]
  const m = el(`<div class="abs" style="left:${x}px;top:0;width:6px;height:0;opacity:0"></div>`);
  const box = rows.map(r => { const b = r.node.getBoundingClientRect(); return [b.top + 6, b.height - 12]; });
  live(t => { let i = -1; rows.forEach((r, k) => { if (t >= cue(r.at)) i = k; });
    if (i < 0) { m.style.opacity = 0; return; }
    const e = E.out(clamp((t - cue(rows[i].at)) / 0.6)), [y0, h0] = box[Math.max(0, i - 1)], [y1, h1] = box[i];
    m.style.opacity = i ? 1 : e; m.style.top = (i ? y0 + (y1 - y0) * e : y1) + 'px';
    m.style.height = (i ? h0 + (h1 - h0) * e : h1 * e) + 'px'; m.style.background = `var(--${rows[i].key || 'own'})`; });
}
```
Use `spot` in bars, Split slices (merge it into the Split's existing per-slice `filter` tween: one property, one tween per node),
the density dots and the columns' rules. Use `marker` in ranked (with an optional `spoken` cue per row), receipt lines and the Split costs.

### 6. Values that travel with the data
The number belongs to the shape it describes and moves with it.
- Bars (prototyped): the value is positioned at the start of the bar and moved by `translateX(barWidth × E.outQuint(p))`. Its text counts
  on that same `E.outQuint(p)`, with opacity `clamp(p / 0.12)`, in one `fn` tween with `ease: false`, dur 1.0 s, at cue + 0.1 s.
  Ranges (`–`) move but don't count.
- Growth: label at `path.getPointAtLength(L)`, counting a → b on the same curve as the line.
- Ring: number and head dot on the arc's curve (`outQuint`, 1.4 s).
- Split tally: each step on its slice's cue, 0.7 s `out`, the same curve as the slice's lift.

### 7. One path-drawing helper for routes and lines (fixes "barely visible")
Pull the prototyped `routeMap` code out into `drawPath(svg, d, { at, speed, stops, closed, head, pulse })` and use it in `routeMap`,
`growth`, `density` and `ring`. What it does (2.6):
- builds the 16 px core, 34 px edge and glow, plus a head circle and an optional pulse path (`stroke-dasharray: 160 <len>`)
- turns the timing into knots: `[at, 0]`, then `[cue - 0.3, length to stop i]` for each spoken stop, then the end at `speed`.
  The length drawn at time t is `L0 + (L1 - L0) * E.sine((t - t0) / (t1 - t0))` between knots, so the head slows into each stop
- each frame sets both strokes' `stroke-dashoffset = len - L(t)` and puts the head at `getPointAtLength(L)`.
  Once complete, the pulse moves with `stroke-dashoffset = -(t - tEnd - 0.4) * 600 % len`
- works out each pin's time by sampling `L(t)` at 1/30 s, and gives each pin a `pop` (from 0.6) and a ring pulse
- the tween is one `fn` running the whole shot (`dur: sc.dur`, `ease: false`) so the frame key keeps changing.

### 8. Paper physics and the read-pan (doc, receipt, clipping, papers)
- `anim: 'land'` (change 2) on every paper: `doc`, `receipt`, `clipping`, `papers` (prototyped on doc and receipt).
- Highlighter: `dur = clamp(width / 900, 0.5, 1.2)` instead of a fixed 0.9 s (prototyped).
- Read-pan: `focusOn` each highlight 0.3 s early (prototyped), plus a slow `camTo` from the header.
- Receipt printing: animate the paper box's `height` from header-only to each line's bottom on its cue (0.45 s `outQuint`, `overflow:hidden`).
- doc: a `desk: false` parameter that skips the navy SVG when the shot has a `bg` (render.py already composites over a background when one exists).

### 9. Text that arrives with the voice
Prototyped; frames show the quote building word by word and the name rising from behind its baseline.

```js
// span = [start, end] of the spoken phrase. Each word rises 14 px as it's said; times are spread by characters.
function wordsIn(node, span) {
  node.innerHTML = node.innerHTML.split(/(<br\s*\/?>)/).map(part => /^<br/.test(part) ? part :
    part.split(/(\s+)/).map(w => /^\s*$/.test(w) ? w : `<span class="w" style="display:inline-block">${w}</span>`).join('')).join('');
  const ws = [...node.querySelectorAll('.w')], total = ws.reduce((a, w) => a + w.textContent.length, 0); let acc = 0;
  ws.forEach(w => { anim(w, { anim: 'rise', at: span[0] + (span[1] - span[0]) * acc / total + 0.05, dur: 0.45, dist: 14 }); acc += w.textContent.length; });
}
// Names rise from behind their baseline while the letter-spacing settles from +6 px to -1 px.
function maskRise(node, at, dur = 0.7) {
  const wrap = document.createElement('div'); wrap.style.clipPath = 'inset(-60px -80px -0.12em -80px)';
  node.parentNode.insertBefore(wrap, node); wrap.appendChild(node);
  return anim(node, { anim: 'fn', at, dur: 1.2, ease: false, fn: pp => { const e = E.out(clamp(pp * 1.2 / dur)), e2 = E.out(pp);
    node.style.opacity = pp > 0 ? 1 : 0; node.style.transform = `translateY(${((1 - e) * 120).toFixed(2)}%)`;
    node.style.letterSpacing = `${(6 - 7 * e2).toFixed(2)}px`; } });
}
```
In `stills.resolve` `fix()`, accept `"@@phrase"` and return `[start, end]` (relative to the shot, plus `CUE_DELAY`) from
`tl.at(...)` and `tl.end(...)`. In the quote template: `if (p.span) wordsIn(textNode, p.span)`, and the name goes to `span[1] + 0.4`.
In edit.py: `span="@@the largest unattended retail provider in the United States"` for #44.

### 10. A motion check before rendering
Add a check that fails loudly, so "nothing is happening" is caught before the owner sees it:

```js
window.motionReport = (dur, kind) => {     // call after setup(scene); kind = the shot's kind (F, GF, B, G, D)
  const ev = [...TWEENS.filter(tw => !tw.live && tw.node !== CAM && !(cue(tw.at) <= 0 && tw.dur >= dur - 0.05)).map(tw => cue(tw.at)),
              ...CAMKEYS.map(k => cue(k.at))].filter(t => t >= 0 && t < dur).sort((a, b) => a - b), out = [];
  if (kind !== 'GF' && (!ev.length || ev[0] > 1.5)) out.push('lead-in ' + (ev[0] ?? dur).toFixed(1) + 's');   // on GF the footage leads
  ev.forEach((t, i) => { if (i && t - ev[i - 1] > 2.5) out.push('gap ' + ev[i - 1].toFixed(1) + '-' + t.toFixed(1) + 's'); });
  if (ev.length && dur - ev[ev.length - 1] > 3.0) out.push('tail ' + (dur - ev[ev.length - 1]).toFixed(1) + 's');
  return out;   // [] = fine
};
```
Run it from `render.py` (and the stills build) for every graphic shot except the end screen, and print a warning list.
I tested this version against all 51 shots with the prototype engine (no errors). On the current Episode 1 edit it flags
most shots, which makes it the to-do list for the per-template events in section 4. For example: `#22 split: gap 1.8-10.2s,
gap 10.2-16.2s`, `#27 doc: gap 0.0-9.8s`, `#45 clipping: gap 0.0-8.3s`, `#76 equation: lead-in 7.0s`, `#86 split: tail 15.8s`,
`#59 bars: tail 9.2s`. The camera alone stops the picture from freezing; these events are what make it "show what the video is saying".
The safe area belongs in the same check: after `draw(dur - 0.5)`, every visible element's rectangle must lie within
96 px of the sides and above y = 918.

### Changes outside `scenes.html` that go with these
- `proxies.py`: a real rack with `sendcmd`, constant-speed drift in the same direction as the graphic, `rack=False` for hand-offs,
  `rack_open` for rack-outs, and per-piece lengths in `bg` (3.2, 3.4, 3.6).
- `stills.resolve`: `bg="prev"`, `next`/`exit`/`carry` on scenes, and `"@@phrase"` spans (3.3, 3.9, change 9).
- `render.py`: the ledger wipe at chapter changes (3.8). Optionally, 4 render workers on this 4-core machine.
- `edit.py`: merge #22 and #23; give #86 its narration cues; give every #7 line a `strikeDelay`; move #19 and #27 closer to their first spoken data, or use scaffolding.

---

## 6. Checklist for every graphic shot
1. Is something new happening at least every 2.5 s, and is each event tied to a word?
2. Does the first data element land within 1.5 s of the cut, and is the tail after the last event 3 s or less?
3. Is the camera on, inside the safe area, and moving toward the open side? On footage, push only.
4. Do entrances use `out`, exits use `in`, and moves between resting places use `inOut`/`sine`? Is anything linear except drift?
5. Are numbers counted on the word, values riding their shapes, and net figures double-underlined?
6. Is any text dimmed or below 46 px during its animation? (It must not be.)
7. Which transition goes in and which goes out (3.1)? Does the background continue the previous clip?
8. Run `motionReport`, then watch the shot at 1× on a large screen from about 3 m. If it looks like a slide, it isn't finished.
