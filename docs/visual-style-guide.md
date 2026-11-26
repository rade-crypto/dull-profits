# Visual style guide

Based on `research/channel-strategy-and-visuals.md`, which covers 11 comparable channels, TV-viewing data and license checks.

## The approach in one line
**Stock footage + custom motion graphics.** Real footage on screen most of the time, with motion graphics on top whenever a number matters.
The channels this one is modeled on keep real footage on screen. (Corrected after the owner watched them: the first
version of this guide said graphics-first, based on written descriptions rather than the videos themselves.)
Graphics carry the numbers. Footage carries the feeling that this is a real business in the real world.

## Screen-time mix (per 10–14 min episode)
| Share | What | Examples in Ep 1 |
|---|---|---|
| 55–65% | **Real footage**: mostly free stock, plus archive film, Google Earth flyovers and (optional) your own phone clips | Card tap, route van, break room, airport concourse |
| 20–30% | **Graphics**, mostly *on top of* darkened footage | The Split over a shot of a real machine; full-screen only for the 3–4 biggest numbers |
| 10–15% | **"Deal File" source documents** | LAX board report, Riverside contract, FTC 1998 release |
| 0% | AI images | None. Real footage is the point |

**Why custom graphics matter:** stock footage alone looks like the generic "template" channels YouTube now demonetizes, and anyone can download the same clips.
The graphics built from each episode's own numbers make the video original. Never use pre-made graphics templates unchanged.

**Combining them:** when a graphic sits on footage, darken the footage 40–60% and add a slight blur, so text stays readable on a TV.

## Getting real footage for $0
1. **Free stock (your main source):** Pexels, Pixabay, Coverr, Mixkit. Search "vending machine", "break room", "delivery van",
   "airport terminal". Free for monetized use; blur any visible brand logos. Download a few extra clips per scene so
   shots don't repeat across episodes.
2. **Optional: a few of your own phone clips.** Even 5–10% of runtime helps. Vending machines, laundromats and car washes are everywhere.
   - Film in 4K, 5–10 second clips, slow pans, phone held steady or on a cheap tripod.
   - No faces, and don't linger on brand logos.
   - Ask before filming inside a private business. Airports and hospitals often restrict filming, so check first.
   - Your own footage is the strongest proof of original content under YouTube's "inauthentic content" policy.
   - **Ep 1 shot list:** card tap on a machine · a soda dropping · a spiral coil turning · restocking a machine ·
     a van pulling up · an office break room · micro-market shelves and self-checkout · a public airport concourse.
3. **Archive film:** the Prelinger Archives on the Internet Archive (many items are public domain). Use 1950s vending and
   automat footage for the Canteen 1929 history beat, and check each item's rights.
4. **Google Earth Studio (free):** real aerial flyovers of LAX, a car-wash strip, an industrial park. It requires an on-screen
   "Google Earth" credit; check its current terms before publishing.
5. **Company press kits:** some companies publish footage for press use, but terms are often editorial-only. Skip unless the terms clearly allow it.
6. **Never** rip clips from news broadcasts or other YouTubers. That's the fastest route to copyright claims and "reused content" demonetization.

## The two signature devices (the brand)
**1. The Split.** Ideally overlaid on real footage of the machine or business. Every episode follows one real transaction: a $2 soda, a $15 car wash, a $4.75 laundromat load.
A horizontal money bar slices into labeled segments, and each slice drops into a labeled bin.
A small **Owner's Tally** in the top-right corner counts down as each slice leaves.
Ep 1: `$2.00 → $1.89 (tax) → $0.95 (supplier) → $0.86 (card) → $0.82 (software) → $0.62 (location)`. Hold the final frame 4+ seconds.

**2. The Deal File.** A real source document on a dark desk texture. A yellow highlighter sweeps across the key line
("59.5 percent of gross sales") in sync with the narration. A fixed **SOURCE:** tag sits in the lower-left (e.g. `SOURCE: LA Board of Airport Commissioners, Feb 16 2023`).

## Colors (locked for the whole series)
| Role | Hex | Use |
|---|---|---|
| Background | `#1C1F24` charcoal | Every graphic. Avoid full-screen white, which looks harsh on TVs |
| Text | `#F2EFE8` off-white | At least 7:1 contrast |
| **Owner (what's left)** | `#F2EFE8` cream, bold outline | Always the same. It's the "you" slice |
| Location / landlord | `#DB8230` orange | |
| Supplier / product | `#4C8DD6` blue | |
| Payments / tech | `#D1679E` pink | was violet; changed because violet next to blue failed the colorblind check |
| Tax / government | `#6B7280` grey | |
| Operating costs | `#C9A227` mustard | gas, labor, repairs |
| Highlighter | `#F5D547` | Deal File sweeps only |

Blue, pink and orange pass a colorblind-separation check (`dataviz` validator, dark mode, on `#1C1F24`). Gray (tax) and cream (owner)
are deliberately neutral and highlight colors. Always label slices with text as well as color, since 1 in 12 men is colorblind. Never pair red with green.

**Example frames** at real 1920×1080 size: `docs/visual-examples/` (sources in `docs/visual-examples/src`).

## Type
- **Inter** (Google Fonts, free for commercial use) with **tabular numbers** turned on, so counters don't jiggle.
  Use IBM Plex Mono for SOURCE tags.
- On a 1920×1080 canvas: key numbers **120–200 px**, labels **48–56 px**, nothing below **36 px**.
  If you can't read it on a phone at arm's length, a viewer on a TV across the room can't either.
- Keep text inside a 6% margin and keep the **bottom 15% clear** (YouTube's progress bar, captions, end screens).

## Motion and pacing
- Shots of **4–8 seconds**, one idea per screen. Hold text for 1 s + 0.3 s per word.
- **Show each number as it's spoken, not before.** The voiceover's `timings.json` gives the second each sentence starts.
- Simple cuts and slides. No whoosh on every transition, no zoom-punches, no shaking.
- Audio: voice at −14 LUFS. Music (YouTube Audio Library) at about −26 LUFS, and **no music under the number-dense parts**.

## Free tool stack
| Job | Tool | Notes |
|---|---|---|
| Edit | **DaVinci Resolve** (free) on Win/Mac, or **Kdenlive** | The free Linux build of Resolve can't use H.264/AAC media, so use Kdenlive on Linux |
| Graphics | **Canva Free**, Inkscape | Don't use Canva's "Popular Music" in monetized videos |
| Animated charts | **Motion Canvas** or Manim (both MIT, free) | Or ask me to generate The Split programmatically from this repo |
| Footage | Your phone first, then Pexels, Pixabay, Coverr, Mixkit | Unbranded clips only. Blur any visible soda or candy logos |
| Archive | Prelinger / Internet Archive, US federal works | Check each item's rights. City and state documents (LAX) aren't automatically public domain, but showing an excerpt with a highlight to report on it is standard |
| Maps | QGIS + Natural Earth (public domain) | OpenStreetMap needs "© OpenStreetMap contributors" on screen |
| Music / SFX | YouTube Audio Library, Freesound **CC0 only** | Pixabay music can trigger Content ID claims, so keep the license PDFs |
| Thumbnails | Canva Free or GIMP | |
| **Avoid** | CapCut as main editor | Its 2025 terms grant broad rights to your content |

## Rules that keep the channel safe
- **Never screenshot** Reddit posts or other creators' videos. Retype the numbers as your own graphic with a source line
  (`Source: operator post on r/passive_income, via Benzinga, Jan 2026`).
- Don't show George Kamel's face or footage. Use a text quote card with attribution.
- Company logos: brief, factual use when naming the company is fine. Don't put them in thumbnails.
- Put a source tag on every number, and a date on every statistic ("in 2025").
- Description footer: "Narration uses a synthetic voice. Researched and written by [channel]. Not financial advice."
  (A generic TTS narrator doesn't need YouTube's altered-content label, but being upfront builds trust.)

## Thumbnails (3 concepts for Ep 1)
1. **The Split:** a $2.00 bar with a small cream slice labeled "YOU: 62¢". Nothing else.
2. **"59.5%"**, huge, next to an unbranded airport vending machine.
3. A paper receipt with "OPERATOR: $0.62" circled in highlighter.

Big number, 1–3 words, lots of empty space. No shocked faces or red arrows (they look like hype to this audience).
Use YouTube's **Test & Compare** to A/B test them.
