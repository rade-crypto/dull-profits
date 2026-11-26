# Editing playbook: Net to Owner

For the AI editor cutting Net to Owner episodes. Read it before touching `edit.py`, and run the checklist (section 4) before the owner sees anything.

This is the standard for calm business explainers like Modern MBA, Wendover Productions and How Money Works, adjusted for this channel: viewers aged 40 to 65 watching on a TV, real numbers, no hype.

Terms used below:

- **F**: footage only.
- **GF**: one number or short line on sharp footage.
- **B**: a graphic with several parts on its own footage background.
- **G**: a full-screen graphic.
- **D**: a Deal File document.
- **Cue**: the moment a word starts in `timings-clean.json`.
- **Motion score**: see section 4, check 1.

## What is wrong with the current cut, measured

Measured on `render/Net-to-Owner-Ep1.mp4` (11:38.7, 91 shots) and `review/shots.md`.

| Measure | Now | Target |
|---|---|---|
| Sharp footage on screen (F + GF) | 34% of runtime | 55–65% |
| Graphics on a blurred background (B) | 56% of runtime | 25% or less |
| Average shot length | 7.7 s | 4–5 s (about 140–160 shots) |
| Shots longer than 8 s | 31 of 91 | 0 (end screen excepted) |
| Shots that measure as frozen (motion median under 1.0 or identical frames) | 41 shots, about 40% of runtime | 0 |
| Clips used more than once | 12 | 0, plus one deliberate callback |
| On-screen number that differs from the voice | "$3,450" while the voice says "$3,500" (shot 16) | 0 |
| Graphics in the bottom 15% of the frame | route pins (shot 15), "Source: VMFS USA" (shot 16) | 0 |
| On-screen items the voice never says | Gilly Vending 42.0% (36), Trustpilot quote (85), winner names before they're introduced (32) | 0 |

**The core mistake:** every multi-part graphic sits on footage blurred with a radius-22 box blur and darkened to 42%. At that blur, moving footage reads as a frozen photo. When a clip runs out, the engine holds its last frame (`tpad=stop_mode=clone`), and some backgrounds were real freeze frames. Then those graphics stay up for 10–28 s. That is why the owner says "stuck" and "100x worse".

The stills storyboard can't show this, because a still never looks stuck. **Always judge a cut in motion.**

---

## 1. The 15 rules

### Rule 1. Footage first. A graphic must earn its place

- **Mix per episode:**
  - 55–65% sharp footage (F + GF).
  - 20–30% graphics (B + G).
  - 10–15% Deal File (D).
- **Decision test, sentence by sentence:**
  1. The sentence says **one** number or name that matters: **GF**. Put the number on the footage, in the footage's empty space.
  2. It compares or adds up **two or more** things (prices, slices, before and after): **B** or **G**.
  3. It quotes or cites a document: **D**.
  4. Anything else: **F**, footage that shows the sentence (Rule 5).
- **Do:** let footage carry the feeling and graphics carry the numbers.
- **Don't:** use a graphic as a way to avoid finding footage. Don't put a graphic on screen with no number, name or quote in it.
- **In this cut:** 56% of runtime is B. Most of it should be footage, with the graphic shown only while numbers are being said.

### Rule 2. Shot length

- **Footage shots:** 2.5–6 s. **Hard maximum for any shot: 8 s.**
- **List beats:** when the narrator names 2–4 separate things in a row ("restocking snacks, pulling cash, fixing..."), use one clip per item, 0.9–2.5 s each.
- **Graphics (B, G, D):** may stay up for up to 8 s on one background clip. In that time:
  - Something new must enter at least every 4 s.
  - If the narration on a graphic runs longer than 8 s, either cut away to footage and come back (Rule 9), or change the background clip under it.
- **Average:** 4–5 s per shot. For an 11.6-minute episode, that's about 140–160 shots.
- **Don't:** let any screen sit for more than 4 s with no cut and nothing new.
- **In this cut:** shot 22 (the Split) runs 28 s, shot 19 runs 18.6 s and shot 16 runs 17.7 s.

### Rule 3. Something moves in every frame (the "stuck" rule)

Every frame needs at least one of these, and ideally two:

- real motion inside the footage (people, traffic, hands, machines);
- a camera move;
- a graphic element animating.

**Numbers:**

- Footage plays at 1.0× speed. Slow it to at most 1.1×; anything slower looks frozen on a TV.
- If a clip is shorter than the shot, use a second clip. Never hold the last frame.
- A static (locked-off) clip gets a linear push-in from scale 1.00 to 1.06 over the shot (never more than 1.10), and you should still look for a better clip.
- A finished graphic keeps "breathing": the whole graphic layer drifts from scale 1.00 to 1.02, linear, over its time on screen.
- A still image (Deal File, archive photo) always gets a push of at least 1.00 to 1.05, plus at least one animated element.

**Pass mark:**

- Motion score median of at least 2.5 for any shot longer than 3 s.
- No pair of identical frames 0.5 s apart.
- The command is in section 4, check 1.

**Don't:**

- freeze frames;
- `tpad` holds;
- still images with a 5% zoom;
- heavy blur on a background (it kills the motion).

**In this cut:**

| Shot | What it is | Motion median |
|---|---|---|
| 14 (company names) | | 2.0 |
| 15 (route) | | 0.24 |
| 16 (prices) | | 0.93 |
| 91 | end screen | 0.00 |
| 4 | sharp footage the owner accepted | 6.1 |
| 9 | sharp footage the owner accepted | 11 |
| 11 | sharp footage the owner accepted | 26 |

### Rule 4. Graphic backgrounds are moving footage

The background of a B shot is a **playing clip**, softened like an out-of-focus lens. It is never a blurred still.

**Settings:**

- `gblur` sigma 8 (range 6–10) at 1080p. Replace today's `boxblur` radius 22.
- Brightness ×0.60, saturation 0.75.
- Play at 1.0×.
- Linear push from 1.00 to 1.05 over the shot.
- The clip must be at least as long as its piece. When it isn't, chain clips with a 0.5 s crossfade.
- Change the background clip every 6 s or less, on a spoken cue.

**Pick backgrounds:**

- Choose clips whose motion survives the softening: people walking, traffic, moving lights, hands.
- Buildings, skylines, documents and empty rooms go dead when softened.
- The background must match the topic: an airport for the airport's cut, a hospital for hospital sales.

**Focus pull (sharp to soft over 0.5 s):**

- Only when the B shot's background is the same clip as the shot just before it. The clip keeps playing and defocuses while the first element enters.
- If it's a different clip, cut straight to the background already soft.
- Cutting to a new sharp clip and blurring it a moment later looks like a glitch.

**Do:** keep B shots at 25% of runtime or less, and no single B background longer than 8 s.

### Rule 5. Show exactly what the narrator says

**Noun-verb test:** for every sentence, write down its concrete noun or verb. The shot must show it.

| Words | The shot shows |
|---|---|
| "drives a loop" | a van driving |
| "restocking snacks" | hands loading a machine's rows |
| "pulling cash" | a coin box being emptied |
| "fixing" | a technician with the machine door open |
| "the building" | a machine standing in a lobby |

**If you have no literal clip:**

1. Search Magnific with three queries: the literal thing ("vending machine technician repair"), the action ("restocking vending machine") and the place ("hospital vending machine hallway"). Downloads are free.
2. If nothing turns up, show it with a graphic: a drawing, a map, a number.
3. Only then use a general clip of the same subject. Never use a mismatched one.

**Banned stand-ins:**

- a man staring at his phone in the dark for "passive income";
- a city skyline for a company;
- a grocery shelf for restocking a vending machine;
- Japanese vending machines for US facts (clips `02`–`05-*-4k` and `c01-can-in-pickup-tray`);
- cash piles.

**In this cut:**

- Shot 7: a man on his phone for "stock a machine once a week".
- Shot 14: the Chicago skyline for "Compass Group and Aramark".
- Shot 15: a tiny far-off aerial for "restocking, pulling cash, fixing".

### Rule 6. Timing: on the word, never before it

- **Cuts:** a new shot starts on the first syllable of the phrase it illustrates, 0–4 frames before the word, never after.
- **Graphic elements:** each appears 0.1–0.3 s after its word starts (the engine's `CUE_DELAY` of 0.2 is right). Counting numbers finish by the end of the spoken number.
- **Labels:** a label that sets up a number (for example "US vending operators' sales, 2025") may appear when the sentence that introduces it starts. The number itself waits for its word.
- **Recaps:** a number already said earlier in the episode may be on screen from the start of the shot (for example the 10% and 33% bars in shot 28).
- **Don't** show names or values before they're said.
  - Shot 32 shows "Location, Scale, Payments" while the voice only says "three kinds of players".
  - Shot 36 shows "Gilly Vending 42.0%", which is never said.

### Rule 7. Numbers

**Must match the voice:**

- Every money amount, percentage or count that matters appears on screen as it's said, with exactly the spoken value.
- Shot 16 must say "$3,500", because the voice says "$3,500".
- If a source number differs from the script, fix the script and the voiceover. Never quietly fix only the graphic.

**Sizes:**

| Element | Font | Size |
|---|---|---|
| Hero number | Libre Caslon Display | 160–200 px |
| Secondary number | Libre Caslon Display | 110–140 px |
| Label | Libre Franklin 600 | 52–60 px |
| Source line | Libre Franklin 500 | 46 px |
| Anything | | never under 46 px |

**Wording:**

- Hero numbers spell out the unit: "$7 billion", "$4.6 billion", "$848 million", "$6 million".
- Abbreviations ("$3.3B") are fine only as values inside a chart.
- Use a small "More than" line above the number instead of a trailing "+".

**Entrance:**

- Money and percentages count up from 0, or from the previous value, over 0.6–1.0 s with an ease-out. The count starts on the spoken word.
- Years, ranges ("5–20%") and words ("Free") rise 30 px while fading in over 0.45 s.

**On screen:**

- One hero number per screen.
- At most 3 numbers on screen at once, unless a table builds one row per spoken line.
- A number stays at least 2.5 s after its last digit is said. TV viewers read more slowly.

**Sources:**

- Every number has its source on screen: 46 px, appearing 0.8 s after the number, or on the words where the voice names the source.

### Rule 8. How a graphic enters, builds, holds and leaves

**Enter:**

- Never show the whole graphic at once.
- The frame (kicker, axis, hairlines) arrives first, in 0.4–0.6 s. Each data element then arrives on its own spoken cue.
- If the first cue comes more than 1 s after the cut, start the graphic shot later and stay on the previous footage longer.

**Motion vocabulary (use only these):**

| Element | Motion | Duration |
|---|---|---|
| Bars | grow from the baseline | 0.7 s, ease-out; value label fades in at 70% of the growth |
| Lines and routes | draw along their path | 0.8–1.6 s, ease-in-out |
| Numbers | count | 0.6–1.0 s |
| Text | rises 30 px while fading in | 0.45 s, ease-out |
| Highlighter | sweeps left to right | 0.6–0.8 s |
| Hairline rules | wipe | 0.4 s |
| Pins and dots | scale 0.9 to 1.0 with a fade, no overshoot | 0.25 s |

**Build:**

- One new element per spoken item.
- Parts of the same item may stagger by 0.15–0.25 s.

**Hold:**

- After the last element, hold at least 2 s; hold the Split's final state at least 4 s.
- Keep the 1.00 to 1.02 drift running during the hold.

**Leave:**

- By default the graphic leaves with the cut, with no exit animation.
- Use a 0.3 s ease-in fade only when the background clip carries on.
- When the next shot continues the same graphic (Split, then Split with costs), never rebuild it from zero. Keep it on screen and animate only what changes.

**Don't:**

- bounces, spins, scale-pops over 3%, typewriter text;
- elements sliding in from off-screen;
- everything fading in together.

### Rule 9. Break long graphics with footage (the sandwich)

- When numbers keep coming for more than 8 s, alternate: graphic (5–6 s), then footage of the thing just named (2–3 s), then the graphic again.
- When the graphic comes back, it returns **in the state it left**: no re-entry animation, only the next element building.
- During the footage part, keep the money thread visible with the corner tally (template 7, "Operator keeps 62¢"), 52 px label and 120 px number.
- **Example, the $2 Split (2:30–2:58):**
  1. Tax slice.
  2. Bottling line ("the product").
  3. Drink-company slice.
  4. Card tap ("the tech companies").
  5. Card and software slices.
  6. A machine in a lobby ("the building").
  7. Building slice and owner slice.
- Background footage that is a different part of a clip you show sharp is fine, and a focus pull back to sharp on the same clip ("The biggest slice is the product") is the best cutaway of all.

### Rule 10. Transitions

| Transition | When | Length |
|---|---|---|
| Hard cut | the default: 90% or more of all joins | — |
| Crossfade | a background change under an unchanged graphic; into and out of archive film (1929, 1998) | 0.5 s |
| Focus pull | from footage into a graphic on the same clip (Rule 4) | 0.5 s |
| Zoom-through | from a map into aerial footage. The map scales toward the place (ease-in), a 0.35 s crossfade hands over to the aerial, and the aerial lands from 1.15 to 1.00 (ease-out) | 0.7–0.9 s |
| Fade | last shot to the end screen | 1.0 s |

- **Never:** whip pans, glitch or RGB-split effects, light leaks, spins, page curls, zoom blur, dips to black mid-episode, or chapter title cards.
- Pieces inside one shot currently always crossfade for 0.5 s (`proxies.py` `XF`). A list beat needs hard cuts, so add a per-piece `cut=True`.

### Rule 11. Clean cuts, no glitches

**Clips:**

- Scene-detect every source clip and stop before any hidden cut (`until`). The command is in section 4, check 5.
- Don't use the first 0.2 s or last 0.3 s of a stock clip: they often hold fades, flash frames or a slow-down.

**Graphics carried across a cut:**

- They must be pixel-identical on both sides: same position and opacity, no re-entry and no one-frame flicker.
- Render carried elements already fully visible from frame 0 (add a `held` option in `scenes.html`).

**Encoding:**

- Every segment uses 30 fps, 1920×1080 and yuv420p.
- If any join stutters, re-encode the joined video in one pass instead of `concat -c copy`.

**Check:**

- Export frames −2 to +2 around every cut and look at them (section 4, check 6).

**Audio:**

- The voice is continuous. Never cut audio at a picture cut.
- Mute leftovers: "Part" is read aloud at 8:48.0–8:48.6 (527.98–528.62 s).

### Rule 12. Text on footage, without dark layers

**Footage shots (F and GF):**

- No darkening, vignette, gradient, box or panel, ever (owner's rule).
- The only grade is saturation 0.86 with contrast 1.03.

**Placement:**

- Pick a clip that has a calm, even area of at least 700×300 px where the text goes: sky, a wall, an out-of-focus area.
- Never put text over faces, over hands doing the action, or over the subject.
- If the subject is on the left, choose another clip. Mirror a clip only when it has no readable text in it.

**Color:**

- White `#FFFFFF` with a soft shadow (0 2px 12px at 55% black) on dark or mid areas.
- Navy `#0B1422` with no shadow on light areas.
- If the area is half light and half dark (like the bright aerial in shot 13), the clip is wrong for text.

**Measured contrast:** average luma of the footage under the text box, measured on the background before the overlay (0–255):

| Text | Luma under it |
|---|---|
| White labels (46–60 px) | 100 or less |
| White big numbers (120 px or more) | 120 or less |
| Navy text | 170 or more |

**Safe area:**

- Left and right margins at least 96 px (the grid's left edge is x = 116).
- Top at least 96 px.
- **Nothing below y = 918** (the bottom 15%: YouTube controls and captions).

### Rule 13. Choosing B-roll

**Choose, in this order:**

1. **Literal.** It shows the sentence (Rule 5).
2. **Right place.** A US setting for US facts.
3. **Motion.** Something moves in the first second.
4. **Room for text,** when the shot is GF.
5. **Quality.** 1080p or better, no watermark, level horizon.

**Never use:**

- staged stock acting (fake laughter, high-fives, people pointing at screens);
- people looking into the lens;
- visible brand logos (blur them, as with the LAX billboards);
- cash piles;
- very dark clips (average luma under 20%) for more than 2 s.

**Each clip once per episode:**

- The one allowed exception is a deliberate callback: the opening machine shot at "Back to your $2". That reuse must come from a different part of the clip.
- A clip continuing across a focus pull counts as one use.
- Never cut a clip into two shots and repeat it later.
- **In this cut, 12 clips repeat:**
  - `c12-vending-closeup`
  - `c03-highway-driving` (3 uses)
  - `c02-office-vending`
  - `c10-checking-sales-records`
  - `c01-bottling-line`
  - `c02-repair-closeup`
  - `c06-warehouse-drink-racks`
  - `c09-laptop-night`
  - `c09-auto-repair-shop`
  - `c09-credit-card-overdue`
  - `c11-newsprint-listings`
  - `c11-phone-night-viewer`
  - Shots 54 and 58 show the same footage.

**Neighbors:**

- Alternate scale (wide, then medium, then close).
- Don't put two look-alike clips back to back (two kiosks, two server rooms).
- Keep neighboring clips within about 20% of each other's brightness.

**Process:**

- Use the best 3–6 s of a clip, where the action happens, not the start.
- Download 2–3 candidates per beat from Magnific. Stock downloads are free; about 40 per burst, then wait 15 minutes. Queue IDs in `footage/pending.tsv`.
- Pick by literalness first, then motion, then text space, then quality.

### Rule 14. Words on screen

**Only these:** numbers, short labels for them (2–6 words, sentence case), names, quoted words the voice says, sources, and Deal File excerpts.

**Never:**

- presenter lines ("We'll get to that", "Would you still buy one?");
- chapter cards;
- words the voice doesn't say, beyond a unit or label (for example "per month").

**Limits:**

- At most 12 words on screen outside a Deal File.
- A Deal File excerpt has at most 40 words, with at most 8 highlighted.
- Reading time: on screen for at least 0.3 s per word plus 1.5 s.

**Color:**

- White, navy on light, `#FFE14D` only as the highlighter, and the Split palette only for data.
- Never grey, and never text opacity under 0.9 (for example the uppercase grey "Illustration, not real ads" label in `versus`).

### Rule 15. Look like Net to Owner, not like Claude

**Use:**

- Square corners.
- Hairline rules like a financial statement.
- Left-aligned layouts on the 116 px grid.
- Libre Caslon Display for numbers and quotes, Libre Franklin 500/600 for labels, Libre Caslon Text for documents.
- Navy `#0B1422` and the Split colors for data only.

**Never use:**

- rounded corners, pills or badges;
- cards with drop shadows (the three tilted "papers" in shot 8 have them, so remove the shadows);
- glassy blur panels;
- gradient fills;
- icon-pack icons or emoji;
- Inter or system fonts;
- cream, terracotta or warm charcoal;
- centered dashboard grids;
- tiny uppercase letter-spaced labels.

**A Deal File** is flat paper `#F7F8F5` on navy, with no glow and no drop shadow.

### Engine changes these rules need

These are in `tools/video/`.

1. **`proxies.make_still_bg`:** replace `boxblur` radius 22, dim 0.42 and the sideways crop drift with:
   - `gblur=sigma=8`;
   - brightness ×0.60 and saturation 0.75;
   - a linear push from 1.00 to 1.05;
   - a speed cap of 1.1×;
   - no `tpad` holds: raise an error when a clip is too short;
   - the focus pull only when the background is the previous shot's clip.
2. **`proxies.make_bg`:**
   - Speed cap 1.1× (now 1.5).
   - Raise an error instead of a `tpad` hold.
   - Add a per-piece `cut=True` for hard cuts.
3. **`scenes.html`:**
   - Count-ups for all money and percentages.
   - A drift from 1.00 to 1.02 on the whole graphic layer.
   - A `held` option for elements carried over a cut.
   - 0.3 s exits.
4. **`routeMap`:**
   - Accept a playing clip plus a per-frame transform track, from ffmpeg `vidstabdetect` (installed) or OpenCV phase correlation (`pip install opencv-python-headless`).
   - Keep all points above y = 918.
5. **New templates from the sheets:**
   - T33: US map. `docs/templates/map.mjs` already builds the geometry, including Chicago.
   - T26: machine drawings.
   - A strip of three moving footage panels, square corners (like T47/T48).
   - T7: the corner tally used during cutaways.

---

## 2. Fixes for the five complaint spots

Times are from `timings-clean.json`, written as m:ss.s.

### Fix A. 0:26.6–0:32.8, shot 7: the struck-through pitch ("terrible choice")

**Why it failed:**

- The same dark close-up of a man in the dark runs for 8.2 s, and about 70% of the frame is black.
- Nothing shows a vending machine or the pitch.
- Striking the pitch through passes judgment before any evidence. It reads as a meme or a presenter's aside.
- Only one line is visible at a time, low in the frame.

**New version.** Keep shot 6 (0:24.6–0:26.6, man on his phone), which the owner didn't complain about.

| Time | Screen |
|---|---|
| 0:26.6 ("as") | Hard cut to **P1**: a brightly lit, fully stocked US snack or drink machine in an office or lobby. Sharp, slow camera move, nothing on top of the footage. |
| 0:26.7 | Kicker "How it's pitched online": Franklin 600, 56 px, white with soft shadow, x 116, y 150. Rises and fades in over 0.4 s. |
| 0:26.9 ("easy") | Quote 1: **"Easy passive income."** Caslon Display 110 px, x 116, y 230. Rises 30 px and fades in over 0.45 s. |
| 0:28.2 ("Stock") | Hard cut to **P2**: hands loading snack packs into a machine's spiral rows, close-up. The kicker and quote 1 stay exactly where they are. |
| 0:28.4 | Quote 2: **"Stock it once a week."** y 370. |
| 0:30.6 ("and let") | Hard cut to **P3**: a hand opening a machine's coin box or pulling the coin bin. No piles of bills. |
| 0:31.0 ("let") | Quote 3: **"Let the cash pile up."** y 510. |
| 0:31.4–0:32.8 | Hold: three quotes stacked, footage playing. |
| 0:32.8 | Hard cut to shot 8. The quotes leave with the cut. |

**Rules for this beat:**

- No strike-through, no yellow, no judgment. The verdict comes later, from evidence: shot 66, "It's not as passive as people make it sound".
- All three clips must have calm space at the top left (x 96–1100, y 130–640).

**Footage (Magnific queries):**

| Clip | Queries |
|---|---|
| P1 | "snack vending machine office lobby", "vending machine modern lobby" |
| P2 | "restocking vending machine", "vending machine refill snacks" |
| P3 | "vending machine coin box", "collecting coins vending machine" |

**Fallbacks:**

- P1: `n-drinks-machine-night` from 0.5 s. Shot 32 then gets other footage, see 4:11 in section 3.
- P2 and P3 have no fallback: if nothing literal exists, let P1 or P2 run on. Never use the grocery-shelf clip.
- Worst case, one clip runs for 6.2 s with the three quotes stacking.

### Fix B. 0:55.3–1:03.6, shots 12–13: "$7B+" over a bright aerial ("why aren't graphics on screen")

**Why it failed:**

- The number sentence starts at 0:55.3 ("In 2025, US vending operators brought in"), but the screen showed plain footage until 0:58.9.
- Then a thin white "$7B+" sat on a bright green-and-grey aerial (low contrast, over trees), with small labels and no build.

**New version:**

| Time | Screen |
|---|---|
| 0:52.4–0:55.3 | Keep `c02-office-vending` sharp ("places them in other people's buildings, and keeps them stocked"). End shot 12 at 0:55.3. |
| 0:55.3–0:55.8 | Same clip keeps playing. Focus pull: blur sigma 0 to 8 and brightness 1.0 to 0.6 over 0.5 s (B shot starts). |
| 0:57.1 ("US") | Kicker **"US vending operators' sales, 2025"**: Franklin 600, 56 px, x 116, y 230. Rises and fades in. |
| 0:58.9 ("more") | Background crossfades over 0.5 s to `c02-van-aerial-road` from 1.0 s (a route van driving), softened the same way. Small line **"More than"** (56 px, y 320) fades in. |
| 0:59.4–1:00.2 ("$7 billion") | **"$7 billion"** counts up from $0 billion: Caslon Display 200 px, white with soft shadow, x 116, y 370, ease-out, landing as the word ends. |
| 1:01.0 ("according to") | "Source: IBISWorld", 46 px, x 116, y 850. |
| 1:00.2–1:03.6 | Hold. The background keeps playing; the graphic layer drifts from 1.00 to 1.02. |
| 1:03.6 | Hard cut to Fix C. The graphic leaves with the cut. |

**Contrast check:** the softened aerial at ×0.6 must measure 120 or less under the number.

### Fix C. 1:03.6–1:11.9, shot 14: company names over a frozen blurred still ("it stuck!!!!")

**Why it failed:**

- 8.3 s of a box-blurred, 42%-dark Chicago skyline. The drone motion disappeared under the blur: motion median 2.0, with frozen steps.
- A skyline doesn't show a food service company.
- "Most of the map" was never shown as a map.

**New version:**

| Time | Screen |
|---|---|
| 1:03.6 ("The biggest") | Hard cut to **C1**: a large food-service operation at work (a corporate cafeteria serving line or a contract-catering kitchen). Sharp and moving, no brands visible. Text space at the upper left. |
| 1:04.6 ("food service giants") | Kicker "Food service giants", 56 px, x 116, y 200. |
| 1:05.9 ("Compass Group") | **"Compass Group"**: Caslon Display 150 px, y 270. Rises and fades in. |
| 1:06.8 ("Aramark") | **"Aramark"**: 150 px, y 440. |
| 1:07.7 ("But") | Hard cut to a G graphic: **US map** (template 33) on navy. White state hairlines, 2 px, fade in over 0.5 s. The map drifts from 1.00 to 1.04. |
| 1:08.5 ("map") to 1:11.0 | About 120 yellow dots (`#FFE14D`, 14 px) pop in across the country in a random stagger, spread roughly by population. This illustrates what the voice says; never label a count. |
| 1:09.9 ("small, local") | Label **"Small, local businesses"**, 60 px, x 116, y 780. |
| 1:11.2–1:11.9 | The map starts the zoom-through toward the Chicago dot (ease-in). It continues in Fix D. |

**Footage (Magnific queries):**

- C1: "corporate cafeteria serving line", "catering kitchen staff", "food service workers cafeteria".
- Fallback: `c01-office-lobby`, sharp. Shot 44 then needs a different background.

### Fix D. 1:11.9–1:21.8, shot 15: the route ("where is some transition", "nothing is happening", "barely visible", "you're not showing what the video is saying")

**Why it failed:**

- A hard cut from a blurred skyline to a still frame, with a 5% zoom (motion 0.24).
- The 12 px line and small pins were drawn on a far-off aerial, inside the bottom 15% of the frame (y 880–1045).
- "Restocking, pulling cash, fixing" weren't shown.

**New version:**

| Time | Screen |
|---|---|
| 1:11.2–1:12.3 | **Zoom-through:** the map scales from 1.0 to 4.0 toward Chicago. At 1:11.9 ("Most") a 0.35 s crossfade hands over to `c10-chicago-suburbs-aerial`, **playing**, which lands from scale 1.15 to 1.00 by 1:12.8 (ease-out). |
| 1:12.3–1:13.6 | Aerial moving; nothing on top. |
| 1:13.6 ("route") | 8 pins pop onto houses **in the middle of the frame** (x 420–1500, y 330–780), staggered 0.06 s. Pins are 52 px yellow with a 7 px navy ring, **tracked to the footage**. |
| 1:14.9 ("drives") to 1:16.5 ("locations") | The route draws pin to pin as a closed loop: a 14 px `#FFE14D` line on a 26 px navy edge, ease-in-out over 1.6 s. A 30 px white square "van" marker rides the head of the line, then keeps circling the loop. |
| 1:16.9 ("restocking") | Hard cut to **R1**: hands loading snacks into a machine. 1:16.9–1:18.1. |
| 1:18.1 ("pulling cash") | Hard cut to **R2**: a coin box being opened or emptied. 1:18.1–1:19.0. |
| 1:19.0 ("and fixing") | Hard cut to **R3**: a technician with a machine door open, working inside. 1:19.0–1:21.8. |
| 1:21.8 | Hard cut to Fix E. |

**Tracking:**

- Run `vidstabdetect` (or OpenCV phase correlation) on the clip section and apply each frame's move and scale to the pin and route layer.
- If it drifts more than 10 px, use a calmer section, or a top-down suburb aerial (Magnific: "top down aerial suburb drone").
- Last resort: a still with a 1.00 to 1.15 push and the van marker circling. Never a still with a 5% zoom.

**Footage (Magnific queries):**

- R1: a second "restocking vending machine" clip, different from P2.
- R2: "vending machine coin mechanism", "emptying coins vending machine", different from P3.
- R3: "vending machine repair technician", "technician fixing vending machine".
- If R2 doesn't exist, keep the aerial on screen through 1:19.0 and add a "Pull cash" label at its pin. Don't use wrong footage.

### Fix E. 1:21.8–1:39.6, shot 16: machine prices over a frozen blurred still ("stuck!!!! how did you make the video 100x worse")

**Why it failed:**

- 17.7 s on one graphic over a box-blurred, slowed man at a machine (motion 0.93, ten frozen steps).
- The three columns only fade in.
- "$3,450" is on screen while the voice says "$3,500".
- The source line sits at y ≈ 1000, inside the bottom 15%.
- Nothing shows what a countertop, combo or elevator machine looks like, or what "gently lowers each item" means.

**New version:**

| Time | Screen |
|---|---|
| 1:21.8 ("The machines") | Hard cut to **E0**: a vending machine being wheeled in on a hand truck or installed. Sharp, nothing on top. Fallback: `n-street-vending-man` from 3.0 s, **sharp**. |
| 1:23.2 ("One supplier") | E0 keeps playing and focus-pulls to a soft background (B starts). Kicker "One supplier's prices", 56 px, x 116, y 110. |
| 1:24.9 ("countertop") | **Countertop machine line drawing** draws itself: white 5 px strokes, square corners, 0.8 s, left column (x 116). Its bottom sits on the baseline at y 560. Label "Countertop", 56 px, y 590. |
| 1:26.5–1:27.3 ("$1,900") | **"$1,900"** counts up: Caslon Display 130 px, y 650. |
| 1:26.9 | "Source: VMFS USA", 46 px, x 116, y 840. It stays. |
| 1:28.2 ("A combo") | Background crossfades over 0.5 s to `c02-combo-machine` from 0.5 s (a woman at a combo machine). |
| 1:28.5 ("combo") | **Combo drawing** draws in the middle column (x 700). Label "Combo". |
| 1:30.7–1:31.6 ("$3,500") | **"$3,500"** counts up. It must match the voice. |
| 1:32.1 ("An elevator machine") | Hard cut to **E3** footage: an elevator vending machine lowering a product on its lift. 1:32.1–1:36.4. |
| 1:36.4 ("starts at about") | Back to the graphic, exactly as it was. Countertop and combo are already in place, with no re-entry. Background: `n-subway-vending-woman2` from 1.0 s, soft. **Elevator drawing** draws in 0.6 s in the right column (x 1260). |
| 1:37.3–1:38.9 ("$8,650") | **"$8,650"** counts up. |
| 1:38.9–1:39.6 | Hold, with drift. |
| 1:39.6 | Hard cut to shot 17. |

**If there's no E3 footage:**

- Stay on the graphic.
- The elevator drawing draws at 1:32.3.
- At 1:33.5 ("gently lowers each item"), a small product box inside the drawing rides a platform down from the top row to the pickup bin over 2.0 s (ease-in-out).
- Change the background clip at 1:33.0.

**Drawing proportions:**

- Countertop about 1/3 the height of the combo.
- Elevator the same height as the combo and about 1.3× wider.
- The tallest top is at y ≥ 100. Prices end by y 780.
- Nothing below y 918.

**Footage (Magnific queries):**

- E0: "vending machine delivery hand truck", "installing vending machine".
- E3: "vending machine elevator", "vending machine lift delivery", "fresh food vending machine glass front".

---

## 3. Minute by minute

Each line gives the time, what the viewer sees, the kind of shot and what to do. "Keep" means it stays as the owner saw it. "Fix" means it is fixed in place: same idea and graphic, new motion, background or timing. "New" means it is replaced (a complaint spot or a broken rule). "Ask" means the owner saw it and didn't object, so ask before changing it.

### 0:00–0:59

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 0:00.0–0:02.7 | Phone tap, soda drops (1–2) | F | Keep |
| 0:02.7–0:15.8 | The Split: $2.00, the bar splits on "five other players", one slice per name (9.4, 10.2, 11.2, 12.4, 13.8 s) (3) | B | Fix: shot 2's clip carries on as the background (focus pull), playing; 0.5 s crossfade to `n-coins-office-vending` at about 0:08 |
| 0:15.8–0:18.4 | Plane landing at LAX (4) | F | Keep |
| 0:18.4–0:24.6 | "59.5%" counts up over LAX at night (5) | GF | Fix: the clip is almost static (motion 0.57). Add a 1.00 to 1.06 push, or swap in moving LAX night traffic |
| 0:24.6–0:26.6 | Man scrolling his phone (6) | F | Keep |
| 0:26.6–0:32.8 | Pitch quotes stack over a stocked machine, restocking, coin box (7) | GF | New: Fix A |
| 0:32.8–0:39.4 | Three source papers, each on its spoken word (8) | B | Fix: background plays; remove the drop shadows |
| 0:39.4–0:47.5 | Hand truck; coins in hand (9–10) | F | Keep |
| 0:47.5–0:55.3 | Route driver in his van; woman at an office machine (11–12) | F | Fix: end shot 12 at 0:55.3 |
| 0:55.3–1:03.6 | "$7 billion" builds, source IBISWorld (12–13) | B | New: Fix B |

### 1:00–1:59

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 1:03.6–1:07.7 | Food service at scale; "Compass Group", "Aramark" (14) | GF | New: Fix C |
| 1:07.7–1:11.9 | US map fills with small local businesses (14) | G | New: Fix C |
| 1:11.9–1:16.9 | Zoom into the suburbs; pins and a loop drawn on the moving aerial (15) | GF | New: Fix D |
| 1:16.9–1:21.8 | Restocking, coin box, repair: one clip each (15) | F | New: Fix D |
| 1:21.8–1:39.6 | Machine delivered; drawings and prices, with elevator footage in the middle (16) | F + B | New: Fix E |
| 1:39.6–1:42.0 | A machine in a small business ("the deal with the location") (17) | F | Fix: split shot 17 (8.7 s) with a new clip |
| 1:42.0–1:48.2 | Break room; **"Free"** rises on "free" (about 1:44.4), placed on the wall area (17) | GF | Fix: navy text if the wall is light |
| 1:48.2–1:55.3 | "5–20%" at the transit station (18) | GF | Fix: move the number to the dark upper-left (y about 150); rise on "five to 20%" |
| 1:55.3–1:59.7 | Two machines in very different places, about 2.2 s each ("depend almost entirely on where it stands") (19) | F | Fix: sandwich, new clips |

### 2:00–2:59

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 1:59.7–2:07.9 | Bars: typical site $150–700, strong site up to $1,500 (19) | B | Fix: playing corridor background; bars grow on their words |
| 2:08.4–2:11.5 | Three square footage panels: hospital, factory, transit hub, each wiping in on its word (19) | F | Fix: `c02-hospital-corridor`, `c02-factory-floor`, plus a new transit clip |
| 2:11.5–2:13.9 | Bars return as they were; third bar "$2,000+" grows on "$2,000" (19) | B | Fix |
| 2:13.9–2:19.4 | Can opening (20) | F | Fix: slow (1.9), so add a 1.00 to 1.05 push |
| 2:19.4–2:23.5 | Soda dropping into a machine tray ("how one equipment supplier models a $2 soda") (21) | F | Fix: new clip; the receipt starts at 2:23.5 |
| 2:23.5–2:30.3 | Receipt: 6%, 10%, "Most" on their words (21) | B | Fix: playing background |
| 2:30.3–2:35.3 | Split: tax slice 11¢; corner tally $2.00 to $1.89 (22) | B | Fix: sandwich (Rule 9) |
| 2:35.3–2:38.0 | Bottling line goes back into focus ("the product"); tally stays (22) | F | Fix |
| 2:38.0–2:43.5 | Split returns; drink company 94¢ (22) | B | Fix |
| 2:43.8–2:46.2 | Card tap close-up ("the tech companies take theirs"); tally stays (22) | F | Fix: new clip |
| 2:46.3–2:51.8 | Split: card 9¢, software 4¢ (22) | B | Fix |
| 2:52.3–2:54.1 | A machine in a building lobby ("The building takes its 10%") (22) | F | Fix: new clip |
| 2:54.1–2:58.5 | Split: building 20¢, then "Owner 62¢" (22) | B | Fix |

### 3:00–3:59

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 2:58.5–3:04.0 | The same Split, not rebuilt: costs list one per word; background changes to a route van clip (23) | B | Fix |
| 3:04.0–3:12.7 | Highway driving; gas pump (24–25) | F | Keep |
| 3:12.7–3:25.2 | Receipt: $900, then "Operator keeps $197", then the 22% note (26) | B | Fix: `c02-driver-paperwork` playing; change the background at 3:19 |
| 3:25.2–3:29.3 | Driver doing paperwork, back in focus (same clip) ("before the operator pays themselves") (26) | F | Fix |
| 3:29.3–3:35.6 | A busy campus or public building with a machine ("the bigger its cut") (27) | F | Fix: new clip |
| 3:35.6–3:41.6 | Riverside Deal File; "33% on gross sales" highlighted on "33%" (27) | D | Fix: paper rises in 0.6 s; push from 1.00 to 1.05 |
| 3:41.6–3:46.5 | Bars: typical 10%, Riverside 33%, "That airport ?" (28) | B | Fix: playing airport background (motion was 0.29) |
| 3:46.5–3:50.8 | Card tap at a terminal (29) | F | Keep |
| 3:50.8–3:59.4 | Card or phone: "$2.45" counts up (30) | B | Fix: playing card-tap background |

### 4:00–4:59

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 3:59.4–4:07.0 | Cash: "$1.57" on "$1.57"; background crossfades to coins going into a slot (30) | B | Fix |
| 4:07.0–4:11.1 | Ring draws 0 to 78% on "78%" (31) | B | Fix: playing background |
| 4:11.1–4:15.5 | One soda in a machine's pickup tray ("a thin slice of each soda") (32) | F | Fix: new clip (not the Japanese tray clip) |
| 4:15.5–4:19.6 | Three colored hairlines numbered 1, 2, 3 wipe in on "three kinds of players". **No names yet.** (32) | B | Fix: names appear when each winner is introduced |
| 4:19.6–4:21.8 | Airport concourse; label "1  Location" rises on "the location" (33) | GF | Fix |
| 4:21.8–4:24.6 | LAX place tag (34) | GF | Keep |
| 4:24.6–4:27.7 | Contract signing, sharp ("its board approved a vending deal") (35) | F | Fix: `c05-contract-signing` moves here; shot 36 gets a new background |
| 4:27.7–4:36.1 | LAX Deal File: "59.5 percent of gross sales" highlighted on "59.5%", then "$100 per machine" on "$100" (35) | D | Fix: push from 1.00 to 1.05 |
| 4:36.1–4:42.3 | Ranked bids: 59.5%, Canteen 51.6% (36) | B | Fix: playing background. Ask: the "Gilly Vending 42.0%" row is never said; drop it or add it to the voiceover |
| 4:42.3–4:48.7 | Repair close-up; airport terminal (37–38) | F | Keep |
| 4:48.7–4:50.8 | Trucks at docks; label "2  Scale" (39) | GF | Fix |
| 4:50.8–4:54.6 | Van in city traffic ("Driving between machines") (40) | F | Fix: `c06-downtown-traffic-aerial` sharp, or a new clip |
| 4:54.6–5:01.8 | Dense vs scattered dots on their words; a route line draws through each box on "beats someone": short in the dense box, long in the scattered one (40) | B | Fix: playing background (motion was 0.00) |

### 5:00–5:59

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 5:01.8–5:06.9 | Warehouse drink racks (41) | F | Keep |
| 5:06.9–5:12.1 | "Canteen, owned by Compass Group" (42) | B | Fix: background with motion (people in a tower lobby), not a static tower |
| 5:12.1–5:17.1 | "1929" over archive street film (43) | GF | Keep; add 0.5 s dissolves in and out |
| 5:17.1–5:23.7 | Quote: "The largest unattended retail provider..." (44) | B | Keep; end at 5:23.7 |
| 5:23.7–5:27.0 | An office micro market ("covers far more than vending machines") (44) | F | Fix: new clip |
| 5:27.0–5:34.3 | Cans on a conveyor (`c03-cans-conveyor`, unused), then beverage trucks leaving a depot ("the Alabama bottler Buffalo Rock") (45) | F | Fix |
| 5:34.3–5:42.9 | Clipping: "700 micro markets" and "7,600 vending locations" highlighted on their words (45) | B | Fix: playing background, not the racks clip again |
| 5:42.9–5:45.3 | Card terminal; label "3  Payments" on "payments" (46) | GF | Fix |
| 5:45.3–5:49.1 | Card tap to unlock (47) | F | Keep |
| 5:49.1–5:57.5 | "600,000+" counts up on server-room footage (48) | GF | Fix: clip must move (push or dolly) |

### 6:00–6:59

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 5:57.5–6:02.9 | "$4.6 billion" counts up on the data center (48) | GF | Fix: spell out "billion" |
| 6:02.9–6:09.3 | Contactless machine (49) | F | Fix: slow (1.4), so push or swap |
| 6:09.3–6:12.3 | Handshake (50) | F | Keep |
| 6:12.3–6:21.0 | Clipping: 365 buys Cantaloupe; "$848 million" highlighted on its word (51) | B | Fix: playing boardroom background |
| 6:21.0–6:24.6 | US Capitol at dusk ("Regulators only let the deal through") (51) | F | Fix: `c11-penn-ave-capitol-dusk`, unused |
| 6:24.6–6:27.3 | Clipping returns; "sell a competing kiosk business" highlighted on "sell off" (51) | B | Fix |
| 6:27.3–6:43.2 | Busy office; grab-and-go cooler; self-checkout (52–54) | F | Keep |
| 6:43.2–6:53.0 | Bars: "$2.01", then "$3.02" (55) | B | Fix: playing background |
| 6:53.0–6:57.8 | A smart cabinet opened with a card tap (`c08-smart-cabinet`, unused) (55) | F | Fix |
| 6:58.0–7:00.9 | Bars return; "$4.49" grows (55) | B | Fix |

### 7:00–7:59

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 7:00.9–7:08.0 | "$1 billion" with "More than" above; "up 13%" on "13%" (56) | GF | Fix: push on slow footage |
| 7:08.0–7:14.2 | Growth line draws from 71 to 572 over 1.0 s on "572" (57) | B | Fix: playing background |
| 7:14.2–7:18.4 | "$6 million" on smart-store footage (58) | GF | Fix: the clip repeats shot 54, so use a new smart-fridge angle |
| 7:18.4–7:26.3 | Total sales bars: $3.3B, $1B+, $6M (59) | B | Fix: playing background |
| 7:26.3–7:32.7 | People shopping a micro market ("the fastest growth") (59) | F | Fix: new clip |
| 7:32.7–7:39.9 | Man on a laptop at night (60) | F | Keep |
| 7:39.9–7:48.9 | Receipt: "$3,200", then "$400" (61) | B | Fix: its background was a frozen frame, so use `c09-calculator-hands` playing |
| 7:48.9–7:54.4 | Office; mechanic under a lift (62–63) | F | Keep |
| 7:54.4–7:59.9 | Receipt: office machine, then repair shop (64) | B | Fix: playing background |

### 8:00–8:59

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 8:00–8:03.3 | Receipt continues (64) | B | Fix: change the background clip |
| 8:03.3–8:05.8 | Restock drive through a suburb ("After gas, restocking and repairs") (64) | F | Fix |
| 8:06.2–8:10.5 | Receipt returns; "Kept $130–150" highlighted on "keep about" (64) | B | Fix |
| 8:10.5–8:14.7 | Someone checking receipts ("We can't check those numbers") (65) | F | Fix: it was a frozen repeat of the repair shop, so use a new clip |
| 8:14.7–8:19.2 | Quote: "It's not as passive as people make it sound." (66) | B | Keep |
| 8:19.2–8:21.7 | One machine in an ordinary hallway or laundromat ("an ordinary location") (67) | F | Fix: new clip |
| 8:21.7–8:28.1 | "$20–175" a month (67) | B | Fix: playing background, not the highway again |
| 8:28.1–8:37.4 | Month grid: 20 squares on "20 months", then keeps filling to 168 on "14 years" (68) | B | Fix: playing background |
| 8:37.4–8:39.8 | An out-of-order machine ("if nothing breaks") (68) | F | Fix: new clip |
| 8:39.8–8:44.8 | Jammed bill acceptor (69) | F | Fix: replace the second use of `c02-repair-closeup` |
| 8:44.8–8:49.0 | Security camera (70) | F | Keep. **Mute the stray "Part" at 8:48.0–8:48.6** |
| 8:49.0–8:52.5 | Overdue credit card bill (71) | F | Keep |
| 8:52.5–8:59.0 | "$3,330" to start (72) | B | Keep |

### 9:00–9:59

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 8:59.0–9:06.7 | Quote: "Save it in cash. Don't borrow it." George Kamel (73) | B | Fix: background is `c09-one-dollar-bill`, not the repeated bill |
| 9:06.7–9:11.7 | Card into a reader (74) | F | Fix: trim the frozen frames at the clip's end |
| 9:11.7–9:21.0 | Two people reviewing documents (75) | F | Fix: frozen frame at the join |
| 9:21.0–9:34.2 | Equation built in spoken order: "2× a year's earnings" on "two times", then "$83,500 typical sale price" on "$83,500" (76) | B | Fix: playing background; change the clip at about 9:27 |
| 9:34.2–9:36.6 | Business-for-sale listings on a laptop ("Asking prices often run higher") (76) | F | Fix: new clip |
| 9:36.6–9:42.6 | Chicago-area route on the aerial; "$138,000" (77) | GF | Fix: as in Fix D (playing, tracked, pins above y 918) |
| 9:42.6–9:49.3 | $138,000 ÷ $49,000 ≈ 2.8× (78) | B | Fix: the same aerial carries on (focus pull) |
| 9:49.3–9:59.9 | Calculator and ledger; records review (79–80) | F | Keep |

### 10:00–10:59

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 10:00.1–10:02.0 | Newsprint close-up (81) | F | Keep |
| 10:02.0–10:10.8 | Clipping "Operation Vend Up Broke": "10 states" and "40 enforcement actions" highlighted (82) | B | Fix: background `c11-fraud-highlighted` playing, not the newsprint again |
| 10:10.8–10:13.5 | Gavel strike ("against companies selling vending business opportunities") (82) | F | Fix: `c11-gavel-strike`, unused |
| 10:14.2–10:17.6 | A 1990s-style phone call ("easy routes and big money") (82) | F | Fix: `c11-landline-dialing`, unused |
| 10:17.6–10:25.1 | FTC Deal File; highlight on "fake references" (83) | D | Fix: push from 1.00 to 1.05 |
| 10:25.1–10:30.7 | Phone social feed runs through "the math behind them is the same" (84–85) | F | Ask: drop the Trustpilot document (85), because its words are not in the voiceover |
| 10:30.7–10:43.5 | Split recap: the named slice stays full while the others drop to 40% opacity; on "most of it" the building slice stretches to 59.5% (86) | B | Fix |
| 10:43.5–10:46.9 | Callback: the opening machine clip, second half ("if the location is good and nothing breaks") (86) | F | Fix: the one allowed repeat |
| 10:46.9–10:52.5 | "Location", "Scale", "Technology" on each word (87) | B | Fix: playing background |
| 10:52.5–10:55.6 | A single machine alone in a corridor ("just the box in the middle") (87) | F | Fix: new clip |
| 10:55.6–10:59.9 | A buyer looking over a machine ("a route for sale") (88) | F | Fix: replace the repeat of `c10-checking-sales-records` |

### 11:00–11:39

| Time | Viewer sees | Kind | Do |
|---|---|---|---|
| 11:00–11:01.6 | Shot 88 continues | F | — |
| 11:01.6–11:09.0 | Office footage under "Would you still buy one..." (89) | F | Fix: new clip (`c02-office-vending` is a repeat). Ask: remove the on-screen question, which is a presenter line |
| 11:09.0–11:17.1 | Car wash tunnel; "Next" and "The car wash" rise on "Next time, the car wash" (template 50) (90) | GF | Fix |
| 11:17.1–11:36.7 | End screen: car wash footage carries on, softened and playing; wordmark at top center; right half kept clear for YouTube's end-screen tiles; 1.0 s fade in (91) | B | Fix: set `END_TAIL` to 18 s so the end screen is 20 s or less, never a static frame |

### New footage to download (Magnific, free)

Magnific allows about 40 downloads per burst. Queue the clip IDs in `footage/pending.tsv`, and download 2–3 candidates per line.

| For | Query |
|---|---|
| 0:26 P1 | snack vending machine office lobby |
| 0:28 P2; 1:16 R1 (two different clips) | restocking vending machine; vending machine refill snacks |
| 0:30 P3; 1:18 R2 (two different clips) | vending machine coin box; emptying coins vending machine |
| 1:19 R3 | vending machine repair technician |
| 1:03 C1 | corporate cafeteria serving line; catering kitchen staff |
| 1:21 E0 | vending machine delivery hand truck; installing vending machine |
| 1:32 E3 | vending machine elevator; vending machine lift |
| 1:39, 1:55, 8:19, 10:52 | vending machine small office; vending machine hallway; vending machine laundromat; vending machine train station |
| 2:19, 4:11 | soda can drop vending machine tray |
| 2:52 | vending machine building lobby |
| 3:29 | college campus hallway students |
| 5:06 background | office tower lobby people walking |
| 5:23, 7:26 | office micro market pantry; self checkout micro market |
| 5:29 | beverage delivery trucks depot |
| 7:14 | smart fridge card tap |
| 8:10 | small business owner reviewing receipts |
| 8:37 | out of order vending machine |
| 9:34 | business for sale listing laptop |
| 10:55, 11:01 | inspecting vending machine; office break room vending |

---

## 4. Final checklist: run before the owner sees anything

Paths assume `EP=/home/user/dull-profits/episodes/01-vending-machines` and the render at `$EP/render/Net-to-Owner-Ep1.mp4`.

### Automated checks

**1. Nothing is stuck.** Pass: no FAIL lines, and FIX lines only on purpose.

```bash
ffmpeg -v error -i $EP/render/Net-to-Owner-Ep1.mp4 \
  -vf "fps=2,scale=192:108,format=gray,tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=$EP/render/motion.txt" -f null -
python3 - "$EP/review/shots.md" "$EP/render/motion.txt" <<'PY'
import re, sys
vals, t = [], None
for line in open(sys.argv[2]):
    if m := re.search(r'pts_time:([\d.]+)', line): t = float(m[1])
    if m := re.search(r'YAVG=([\d.]+)', line): vals.append((t, float(m[1])))
for line in open(sys.argv[1]):
    p = [x.strip() for x in line.split('|')]
    if len(p) > 6 and p[1].isdigit():
        n, a, b = int(p[1]), float(p[2]), float(p[3])
        v = sorted(y for (tt, y) in vals if a + 0.6 <= tt < b - 0.1)
        if not v: continue
        med, frozen = v[len(v) // 2], sum(1 for y in v if y < 0.05)
        verdict = "FAIL frozen" if med < 1.0 or frozen else ("FIX slow" if med < 2.5 and b - a > 3 else "ok")
        if verdict != "ok": print(f"shot {n:3d} {a:7.2f}-{b:7.2f} median {med:5.2f} frozen steps {frozen:2d} {verdict}")
PY
```

Calibration on the current cut:

- The owner's "stuck" shots score 0.2–2.0, with frozen steps.
- Footage the owner accepted scores 4–35.
- The current cut fails 41 shots.

**2. Shot lengths.**

- No shot over 8 s, except the end screen.
- Average 4–5 s.
- No graphic goes 4 s without something new entering.

**3. Mix.**

- F + GF: 55–65% of runtime.
- B + G: 20–30%.
- D: 10–15%.

**4. No repeats.** Count clip names in `edit.py`. Each clip appears once; the only exception is the declared callback at 10:43.

**5. No hidden cuts.** For every clip, check the section actually used:

```bash
ffmpeg -i CLIP -vf "select='gt(scene,0.35)',showinfo" -f null - 2>&1 | grep -o 'pts_time:[0-9.]*'
```

Set `until` before any detected cut.

**6. Every cut looks clean.**

- Export 5 frames around each cut:

  ```bash
  ffmpeg -ss CUT-0.07 -i MP4 -frames:v 5 cut_%d.png
  ```

- Look for flash frames, black frames, one-frame jumps and flickering graphics.

**7. Text size and safe area.**

- Nothing under 46 px.
- Nothing below y = 918.
- Nothing within 96 px of the left or right edge.
- Nothing over a face.

**8. Text color.**

- Only `#FFFFFF`, navy `#0B1422` on light areas, `#FFE14D` as the highlighter, and the Split colors for data.
- No grey, and no text opacity under 0.9.

**9. Contrast.** Measure the luma under each text box on the background clip:

```bash
ffmpeg -ss T -i render/work/bgNN.mp4 -frames:v 1 -vf "crop=W:H:X:Y,format=gray,signalstats,metadata=print" -f null -
```

| Text | Pass if YAVG is |
|---|---|
| White labels | 100 or less |
| White big numbers | 120 or less |
| Navy text | 170 or more |

**10. Numbers match the voice.**

- List every on-screen number next to the transcript word it belongs to.
- They must match exactly. "$3,500", not "$3,450".
- Each number has a source on screen.

**11. Nothing appears before it's said.** Every element's cue time must be at or after its word's start, except recaps of numbers already said.

**12. No forbidden looks.**

- On F and GF shots: no darkening layer, no vignette, no box or panel behind text.
- On B shots: no box blur and no frozen still.
- Nowhere: rounded corners, drop shadows, or presenter lines on screen.

**13. Audio.**

- The voice is continuous, with no clicks at cuts and no leftover headings ("Part" at 8:48.0).
- Music sits well under the voice and ducks.
- The mix is −14 LUFS overall.

### Watch-through, at 1× on a TV-sized screen with sound, start to finish, no pausing

14. For every sentence, ask: does the screen show what I'm hearing right now?
15. Was the screen ever still, dark, or the same for more than 4 s?
16. Could I read every number from 3 m away before it left?
17. Go through the owner's complaint list one item at a time and write the timecode where each one is fixed:
    - 0:28 pitch;
    - 1:00 $7B;
    - 1:05 stuck names;
    - 1:13 route;
    - 1:22 stuck prices;
    - dark overlays;
    - no animation;
    - repeated or boring B-roll;
    - graphics before they're said;
    - glitches at cuts;
    - small text;
    - grey text;
    - presenter lines;
    - Claude-looking design.

### Delivery

18. Send the MP4 first. Stills only show the final state of each shot and hide every motion problem.
19. Include a short change list: what changed, at which timecode, and why.
20. List the "Ask" items as questions. Don't change them until the owner answers:
    - shot 36, the Gilly Vending row;
    - shot 85, the Trustpilot document;
    - shot 89, the on-screen question.
