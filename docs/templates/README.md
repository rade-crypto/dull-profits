# Net to Owner graphics templates

There are 50 graphic templates. The picture sheets are `template-options.jpg` and `template-options-2.jpg` to `-6.jpg`, rendered from `templates*.html` with `shoot*.js`.
The video engine is in `tools/video/gfx/scenes.html` (under TEMPLATE LIBRARY). Shots are set up in `episodes/*/edit.py`.

## Rules (owner)
- No boxes, panels or dark layers behind text.
- A number or a short line can sit straight on footage, in the shot's empty space, never over a face.
  Use white text with a soft shadow on dark shots, and navy `#0B1422` on light shots.
- Anything with more than one part (charts, receipts, lists, the Split) gets its own background image:
  a blurred, darkened, slowly drifting still. In `edit.py` that's `B(at, bg=(clip, seconds), scene)`.
- Every number appears when it's said: cues are `"@phrase"`, and `"@phrase+0.5"` adds a delay for staggered builds.
- Fonts: Libre Caslon Display for numbers, Libre Franklin for labels. Text is at least 46 px. Square corners only.
- No repeated B-roll. Check clips for hidden cuts: give a clip piece `{"until": s}` to stop before the cut.

## Engine scene types (template number → `type`)
| # | Template | `type` | Sits on |
|---|---|---|---|
| 1 | Number in the shot's empty space | `num` (`items` for several in turn) | footage, or `B` |
| 4 | Route and pins on an aerial | `routeMap` (`img=(clip, t)`, `pts`, `value`) | the still itself, zooming slowly |
| 7 | Running total ("Operator keeps") | `split(..., tally=...)` | with the Split |
| 8 | Deal File (real document, highlighted) | `doc` | navy |
| 8b | Three source cards | `papers` | `B` |
| 9 | The Split | `split(...)` | `B` |
| 11 | Receipt | `receipt` | `B` |
| 12 | Comparison bars | `bars` | `B` |
| 14 / 35 | Two columns (then vs now, card vs cash) | `versus` | `B` |
| 15 | The pitch, struck through | `strike` | footage (low, `x=140, y=780`) or `B` |
| 16 | Company card | `company` (`names` for several) | `B` |
| 17 | Three columns / three winners | `columns` | `B` |
| 18 | Dense vs scattered | `density` | `B` |
| 19 | Ranked list | `ranked` | `B` |
| 20 | Growth line | `growth` | `B` |
| 21 | The equation | `equation` | `B` |
| 22 | Ring chart | `ring` | `B` |
| 23 | Newspaper / trade-press clipping | `clipping` | `B` |
| 24 | Quote with name | `quote` | `B` |
| 37 | Place tag | `tag` | footage |
| 41 | Month grid | `months` | `B` |

Templates 2, 3, 5, 6, 10, 13, 25–36, 38–40 and 42–50 are designed on the sheets but not yet in the engine. Add them the same way when an episode needs them.
