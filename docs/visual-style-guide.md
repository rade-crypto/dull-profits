# Visual style guide

Based on `research/channel-strategy-and-visuals.md`, which covers 11 comparable channels, TV-viewing data and license checks.

## The approach in one line
**Documents and diagrams, not cinematic B-roll.** Most of the screen is graphics you build and real source documents.
Stock footage gives the eye a rest. This costs nothing, avoids copyright claims, builds trust with skeptical older viewers, and is
the best defense against YouTube's "inauthentic / template content" demonetization, because every graphic is unique to its episode.

Closest models: **Wall Street Millennial** (filings on screen, cheap to make, high revenue per video) and **Modern MBA**
(slide-style diagrams that build piece by piece). Tone model: **ColdFusion** (calm, restrained). Avoid the MagnatesMedia
style (dramatic music, founder faces). It's the wrong tone for this audience.

## Screen-time mix (per 10–14 min episode)
| Share | What | Examples in Ep 1 |
|---|---|---|
| 40–50% | **Your own data graphics** | The Split, price tags, bars, P&L table, route maps |
| 20–25% | **"Deal File" source documents** | LAX board report, Riverside contract, FTC 1998 release, Cantaloupe report |
| 25–35% | **Stock or archive B-roll** (unbranded) | Card tap, route van, break room, 1950s vending footage |
| 0–5% | AI images | Abstract only. Never fake "real" places, people or documents |

## The two signature devices (the brand)
**1. The Split.** Every episode follows one real transaction: a $2 soda, a $15 car wash, a $4.75 laundromat load.
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
| Location / landlord | `#E8913A` orange | |
| Supplier / product | `#4C8DD6` blue | |
| Payments / tech | `#9B7BD4` violet | |
| Tax / government | `#6B7280` grey | |
| Operating costs | `#C9A227` mustard | gas, labor, repairs |
| Highlighter | `#F5D547` | Deal File sweeps only |

Always label slices with text as well as color, since 1 in 12 men is colorblind. Never pair red with green.

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
| Stock video | Pexels, Pixabay, Coverr | Unbranded clips only. Blur any visible soda or candy logos |
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
