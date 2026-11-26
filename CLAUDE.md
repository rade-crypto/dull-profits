# Dull Profits: project context for Claude

Faceless YouTube channel about **buying, owning and selling unglamorous small businesses, with real numbers**
(vending routes, laundromats, car washes, self-storage, HVAC/plumbing roll-ups, funeral homes).
Audience: roughly 40–65+, has capital, might actually buy or sell one; many watch on a TV. Tone: calm, sourced, no hype, not financial advice.

## What the owner wants from Claude
- **Claude makes the videos end to end**: script → voiceover → stock footage + custom motion graphics → captions → final MP4.
  Don't hand the owner editing instructions instead.
- Keep replies short and direct. The owner often can't see text written between tool calls, so put answers in
  the final message, and send images/audio/video with SendUserFile.
- **The channel always uses AI voices.** Never suggest the owner record their own voice, hire a voice actor, or
  anything like that. More generally, don't recommend things the owner didn't ask for; just do the task.
- The owner uses a **Magnific** account (Freepik rebranded as Magnific, Apr 2026) through the official MCP connector
  `https://mcp.magnific.com` (OAuth). They declined to paste an API key; use the connector, not a key.

## Magnific is for B-ROLL ONLY (owner's standing rule)
**Use Magnific only to search and download stock footage/photos for B-roll.** Never use it for voiceover, music,
images, video generation or anything else. **The voiceover is made by Claude locally with free open-source models.**
(Samples 1–4 in `voice-samples/` were wrongly made on Magnific for 144 credits. Don't repeat that.)

## ⛔ NEVER spend Magnific credits (owner's standing rule)
Every generation or processing job through the Magnific MCP costs credits, even ones the owner's plan treats as
"unlimited" on the website. **Do not run any Magnific tool that costs credits. No exceptions, not even small samples.**
- Allowed (free, read-only): `magnific_start`, `account_balance`, `simulate_cost`, `stock_search`, `stock_get`,
  `creations_search` / `creations_get` / `creations_list`, `folders_list`, `audio_voices_list`, guides.
- Anything else (`audio_tts`, `images_*`, `video_*`, `audio_music_generate`, `stock_download`, `stock_to_creation`, …):
  first call `simulate_cost` (it never charges). Proceed **only if it returns 0 credits**. If it costs anything, don't run it.
- When something needs credits, ask the owner to make it themselves on the Magnific **website** (where their plan may
  be unlimited), then pick up the result from their library with `creations_search` / `creations_get` and download it.
- History: 144 credits were spent on 4 voice samples (Nov 26, 2026) before this rule existed. Don't repeat that.

### Stock footage
- **The owner says Magnific stock footage never costs anything:** they're on a paid plan (Plus) where stock is free and unlimited.
- **✅ CONFIRMED FREE through the MCP (Nov 26, 2026):** balance was 35,324 before and after a premium video
  `stock_download`, even though `stock_search` shows `creditCost: 600`. Ignore that label: **`stock_download`
  (photos, videos, icons, vectors) is free to use as much as needed.** Download URLs may come from
  delivery.gettyimages.com, which is normal.
- Still never call generation tools (`audio_tts`, `images_generate`, `video_generate`, music, upscales, …) without the
  `simulate_cost` = 0 check above. Only *downloads of existing stock* are free.

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
- Footage sources: **Magnific stock via MCP (downloads confirmed free)**; raw files go in `episodes/*/footage/`, which is
  gitignored (stock licenses forbid redistributing raw files, and the repo is public). Also Mixkit (free, no key, reachable, but no vending-machine clips),
  Pexels (free key, not set up), archive.org Prelinger (public-domain archive film).

## Episode 1: vending machines (`episodes/01-vending-machines/`)
- `script-v2.md` / `narration-v2.md` is the current, fact-checked script (~12.5 min). `fact-check.md` lists every change and source.
  **Four facts still need a browser check before publishing** (listed in fact-check.md).
- **Voiceover is NOT approved.** The owner rejected the local Phonon "Trevor" sample ("vo is bad") and said don't generate
  the full VO yet. Four Magnific (ElevenLabs v4) narrator samples are in `episodes/01-vending-machines/voice-samples/`:
  Jake Miller (id 438), Owen Combs Huff (993), Callum Thornbury (1006), Nico Cochran House (1090). Samples 1 and 4 have
  identical size and length, so check they aren't the same file before sending. The owner hasn't heard them yet.
  **Voice must be made locally (free).** Samples 5–6 (Qwen3-TTS VoiceDesign) were rejected as "AI sounding".
  Priority is the most human-sounding free local model. Samples 7–9 = Chatterbox (MIT, `/opt/tts/cb-env`, CPU ~3x slower
  than real time; Turbo ~1.5x): 7 = Chatterbox with sample 6 as voice reference, 8 = Turbo with the same reference,
  9 = Chatterbox default voice. Owner: 7–9 "not good".
  Samples 10–13 = **VoxCPM2** (openbmb/VoxCPM2, Apache-2.0, 2B, 48 kHz, voice design from a text description in
  parentheses before the line; `/opt/tts/vox-env`, CPU ~3x slower than real time). Awaiting the owner's pick. Keep Chatterbox's built-in Perth watermark on (needs `setuptools<81`).
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
