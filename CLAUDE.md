# Dull Profits: project context for Claude

Faceless YouTube channel about **buying, owning and selling unglamorous small businesses, with real numbers**
(vending routes, laundromats, car washes, self-storage, HVAC/plumbing roll-ups, funeral homes).
Audience: roughly 40–65+, has capital, might actually buy or sell one; many watch on a TV. Tone: calm, sourced, no hype, not financial advice.

## What the owner wants from Claude
- **Claude makes the videos end to end**: script → voiceover → stock footage + custom motion graphics → captions → final MP4.
  Don't hand the owner editing instructions instead.
- Keep replies short and direct. The owner often can't see text written between tool calls, so put answers in
  the final message, and send images/audio/video with SendUserFile.
- The owner uses a **Magnific** account (Freepik rebranded as Magnific, Apr 2026) through the official MCP connector
  `https://mcp.magnific.com` (OAuth). They declined to paste an API key; use the connector, not a key.

## Decisions so far
- Name: **Dull Profits**. YouTube @dullprofits, dullprofits.com, X **@dull_profits** (@dullprofits is taken on X).
- Logo: `brand/`. Recommended profile picture: `profile-coin.png`. Wordmark and banner are there too.
- Visual approach (`docs/visual-style-guide.md`): **stock footage + custom motion graphics**, about 60% footage,
  25% graphics mostly overlaid on darkened footage, and 15% "Deal File" source documents.
  Signature devices: **The Split** (a money bar sliced into tax/supplier/payments/location/owner) and **The Deal File** (a real document with a highlighter sweep).
  Locked palette: bg `#1C1F24`, text/owner `#F2EFE8`, supplier `#4C8DD6`, payments `#D1679E`, location `#DB8230`,
  tax `#6B7280`, costs `#C9A227`, highlighter `#F5D547`. Font: Inter / Inter Display. Example frames: `docs/visual-examples/`.
  TV rules: key numbers 120–200 px, nothing under 36 px, bottom 15% clear, 4–8 s shots.
- **No realistic AI-generated footage** of real places or people. It would need YouTube's synthetic-content label and
  undermines credibility. AI images only for abstract or illustrative use. Never rip news or other creators' clips.
- Footage sources: Magnific (via MCP), Mixkit (free, no key, reachable, but no vending-machine clips),
  Pexels (free key, not set up), archive.org Prelinger (public-domain archive film).

## Episode 1: vending machines (`episodes/01-vending-machines/`)
- `script-v2.md` / `narration-v2.md` is the current, fact-checked script (~12.5 min). `fact-check.md` lists every change and source.
  **Four facts still need a browser check before publishing** (listed in fact-check.md).
- **Voiceover is NOT approved.** The owner rejected the Phonon "Trevor" sample ("vo is bad") and said don't generate
  the full VO yet. They haven't said what was wrong, so ask before rendering a full VO and offer short samples.
  Tools: `tools/voiceover/` (Kokoro-82M and Phonon 31M, both Apache-2.0, CPU). Run `setup.sh` first, since a fresh container has no venv.
  `render.py` makes the VO plus captions.srt, chapters.txt and timings.json. `qa_asr.py` proofreads it with Whisper.
  Don't use Phonon 40M models (non-commercial), Coqui XTTS, F5-TTS, Fish, or ElevenLabs' free tier (no commercial rights).

## Next steps
1. Confirm the Magnific MCP tools work. Find out what they offer (stock video? images? AI video?) and their credit cost.
2. Resolve the voice with the owner (short samples first).
3. Build the video pipeline: timings.json → shot list → fetch footage (Magnific/Mixkit/Pexels) → render motion graphics
   (HTML/SVG → frames via headless Chromium, as in `docs/visual-examples/src`) → compose with ffmpeg
   (darken/blur footage under graphics) → music bed at about −26 LUFS (YouTube Audio Library / CC-BY) → captions → MP4.
   Start with a 60-second sample (the hook) for approval before rendering the full episode.
