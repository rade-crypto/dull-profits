# Net to Owner: project context for Claude

(Renamed from "Dull Profits" on Nov 26, 2026. The repo is still called `dull-profits`.)

Faceless YouTube channel about **buying, owning and selling unglamorous small businesses, with real numbers**
(vending routes, laundromats, car washes, self-storage, HVAC/plumbing roll-ups, funeral homes).
Audience: roughly 40–65+, has capital, might actually buy or sell one; many watch on a TV. Tone: calm, sourced, no hype, not financial advice.

## What the owner wants from Claude
- **Claude makes the videos end to end**: script → voiceover → stock footage + custom motion graphics → captions → final MP4.
  Don't hand the owner editing instructions instead.
- **Replies: one or two lines max. No explanations, research summaries or reasoning unless the owner asks.**
  Put explanations in a .md file instead (and only if useful). Never send a wall of text.
- Keep replies short and direct. The owner often can't see text written between tool calls, so put answers in
  the final message, and send images/audio/video with SendUserFile.
- **Send scripts/documents so they open in the side panel, not as a download:** write them as `.md` and send with
  SendUserFile `display: "render"`. Never use `display: "attach"` for things the owner should read.
- **Never send drafts before the research they depend on is finished.** Finish the research first, then send the finished
  piece. "Storyboard" means **stills** (one rendered frame per shot, real clips plus our graphics), not a text table.
- **Never remove or replace something the owner has already seen and not asked to change** (a shot, a line, a graphic).
  Fix it in place, or ask first.
- **Order of work, one step at a time:** research → decision report → owner's OK → style → B-roll → stills storyboard →
  video. Don't start a later step (B-roll, graphics, storyboard) before the step it depends on is finished.
- The owner wants **reports that explain the decision making**: what was researched, the sources, the competitors, and why
  each choice was made.
- **The channel always uses AI voices.** Never suggest the owner record their own voice, hire a voice actor, or
  anything like that. More generally, don't recommend things the owner didn't ask for; just do the task.
- The owner uses a **Magnific** account (Freepik rebranded as Magnific, Apr 2026) through the official MCP connector
  `https://mcp.magnific.com` (OAuth). They declined to paste an API key; use the connector, not a key.

## Magnific is for B-ROLL ONLY (owner's standing rule)
**Use Magnific only to search and download stock footage/photos for B-roll.** Never use it for voiceover, music,
images, video generation or anything else. **The owner makes the voiceover in ElevenLabs.**
(144 credits were once wrongly spent on Magnific voice samples. Don't repeat that.)

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
- **Download rate limit:** after roughly 40 downloads in a short burst, `stock_download` returns `rate_limit_exceeded`
  (account-wide, resets after ~15 min). Its error text suggests `images_generate` instead: never do that (costs credits).
  Queue the IDs (`footage/pending.tsv`, `manifest-*.json` with `status: pending_download`) and download them after the reset.
- Still never call generation tools (`audio_tts`, `images_generate`, `video_generate`, music, upscales, …) without the
  `simulate_cost` = 0 check above. Only *downloads of existing stock* are free.

## Decisions so far
- Name: **Net to Owner** (chosen Nov 26, 2026, replacing Dull Profits). YouTube **@nettoowner** and **nettoowner.com** were free
  on Nov 26, 2026 (not yet claimed; X and Instagram not checked from here). "Net to owner" is the line in business-for-sale
  listings for what the owner keeps, so it hints at buying/selling without saying it and matches The Split's last slice.
- Logo (direction A, chosen Nov 26, 2026): "Net to Owner" in **Libre Caslon Display**, white on ink navy `#0E1726`,
  with an accountant's **double underline** (the mark for a final net figure). Files in
  `brand/`: `profile-picture.png` (serif N, double underline), `wordmark.png`, `youtube-banner.png`; source `brand/src/brand.html`.
  The colored Split palette is for data inside videos only, not for the brand marks. Owner felt the first bold-caps +
  rainbow-bar logo looked unserious.
- Visual approach (`docs/visual-style-guide.md`): **stock footage + custom motion graphics**, about 60% footage,
  25% graphics mostly overlaid on darkened footage, and 15% "Deal File" source documents.
  **Graphics templates: `docs/templates/README.md`** (50 designs, rules, which ones the engine has). Use them for every episode.
  Signature devices: **The Split** (a money bar sliced into tax/supplier/payments/location/owner) and **The Deal File** (a real document with a highlighter sweep).
  **Look (changed Nov 26, 2026; owner: the old cream/orange/charcoal + serif/Inter look was Claude's own and over-used, rounded
  boxes looked like Claude too, and it should feel premium but readable):** deep navy bg `#0B1422`, white text (never grey),
  slices: tax rose `#B65A86`, supplier blue `#4F7EC2`, payments ochre `#B88E30`, location teal `#16998A`, **owner = white**
  (navy text on it), highlighter `#FFE14D`, document paper `#F7F8F5` (passes the dataviz validator on #0B1422).
  **Square corners only** (no rounded boxes, no pills, no card panels or drop shadows): thin colored rules, hairlines
  like a financial statement. Footage darkened with a left-to-right gradient (text side dark, footage visible on the
  right) and graded slightly (saturation 0.86). Fonts: **Libre Caslon Display** for hero numbers, quotes and the logo,
  **Libre Caslon Text** for documents, **Libre Franklin** 500/600 for labels and chart values (sentence case).
  **Nothing smaller than 46 px on a 1920x1080 frame** (owner: no small text). Files in `tools/video/gfx/fonts/`. Never use Inter, cream/terracotta, warm charcoal or rounded UI shapes.
  TV rules: key numbers 120–200 px, nothing under 36 px, bottom 15% clear, 4–8 s shots.
- **No realistic AI-generated footage** of real places or people. It would need YouTube's synthetic-content label and
  undermines credibility. AI images only for abstract or illustrative use. Never rip news or other creators' clips.
- **Owner (Nov 26, 2026): use Pexels when Magnific hits its download limit, and in general whenever Pexels has footage
  that fits better or looks better.** Pexels API key is a network secret on the environment (host api.pexels.com).
- **Pexels downloads work without a key:** `https://www.pexels.com/download/video/<id>/` redirects to the file on videos.pexels.com. Find ids by web search (site pages are behind a bot check). Files are named `px-*.mp4`.
- Footage sources: **Magnific stock via MCP (downloads confirmed free)**; raw files go in `episodes/*/footage/`, which is
  gitignored (stock licenses forbid redistributing raw files, and the repo is public). Also Mixkit (free, no key, reachable, but no vending-machine clips),
  Pexels (free key, not set up), archive.org Prelinger (public-domain archive film).

## Episode 1: vending machines (`episodes/01-vending-machines/`)
- `script-v2.md` / `narration-v2.md` is the current, fact-checked script (~12.5 min). `fact-check.md` lists every change and source.
  **Four facts still need a browser check before publishing** (listed in fact-check.md).
- **Voiceover: the owner generates it themselves in ElevenLabs** from `voiceover-script.md` (numbers spelled out,
  3 parts under 4,500 characters each). Claude does NOT make voiceovers anymore. After 20 rejected samples from
  Magnific, Qwen3-TTS, Chatterbox, VoxCPM2 and VibeVoice, all local voice tools and samples were deleted.
  When the owner provides the audio file, get word timings from it (`tools/video/transcribe.py`) and build the video around it.
  **QA the transcript first:** the first ElevenLabs file had the "PART n of 3 (… characters)" headings read aloud; they were
  cut out (`voiceover-clean.wav`, `timings-clean.json`). Phrase lookup for timing: `tools/video/timing.py`.
  Recommended ElevenLabs Voice Library voices (library voices persist; the old built-in defaults Brian/Eric/Bill
  expire Dec 31, 2026 and aren't available to accounts made after Mar 2026):
  "David - American Narrator" (https://elevenlabs.io/app/voice-library?voiceId=v9LgF91V36LGgbLX3iHW),
  "David Castlemore - Newsreader" (…voiceId=XjLkpWUlnhS8i7gGz3lZ), "Bill - Informative, Clean and Natural" (…voiceId=lnUnPeUhSI5EcqtFBux7).

## Next steps
1. Confirm the Magnific MCP tools work. Find out what they offer (stock video? images? AI video?) and their credit cost.
2. Wait for the owner's ElevenLabs voiceover file, then time everything to it.
3. Build the video pipeline: timings.json → shot list → fetch footage (Magnific/Mixkit/Pexels) → render motion graphics
   (HTML/SVG → frames via headless Chromium, as in `docs/visual-examples/src`) → compose with ffmpeg
   (darken/blur footage under graphics) → music bed at about −26 LUFS (YouTube Audio Library / CC-BY) → captions → MP4.
   Start with a 60-second sample (the hook) for approval before rendering the full episode.
