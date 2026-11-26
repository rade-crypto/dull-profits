# Dull Profits

YouTube **@dullprofits** · dullprofits.com · X **@dull_profits** (plain @dullprofits is taken on X)

A faceless YouTube channel about **buying, owning and selling unglamorous small businesses, using real numbers**:
vending routes, laundromats, car washes, self-storage, HVAC and plumbing roll-ups, funeral homes.

**Audience:** viewers aged roughly 40 to 65+ with capital, who might actually buy or sell one of these businesses.
**Tone:** calm, sourced and specific. No hype, no "get rich" framing, no financial advice.

## Repo layout

```
episodes/
  01-vending-machines/
    script-v1-original.md     first draft, as written
    script-v2.md              fact-checked + adjusted for the owner/buyer audience  ← current script
    narration-v2.md           TTS source (chapters, $ conventions)
    fact-check.md             every claim → verdict + source (paste sources into the description)
    voiceover/                created by the renderer: voiceover.wav/.mp3, captions.srt, chapters.txt, timings.json
research/                     raw research reports (TTS options, channel strategy & visuals, fact-checks)
docs/
  visual-style-guide.md       the channel's look: palette, type, motion rules, the two signature devices, free tools
  channel-names.md            name/handle availability check
tools/voiceover/              free, local voiceover pipeline (Kokoro-82M, Apache-2.0, runs on CPU)
```

## Make a voiceover (free, offline, unlimited)

> **Voice not final yet.** Two free, commercially licensed engines are wired in (both Apache-2.0, CPU only):
> **Phonon 31M** (`--engine phonon`, male voices Trevor, Preston, Miles, Russell, Easton, Micah, Edwin) and
> **Kokoro-82M** (`--engine kokoro`, e.g. `am_michael`, or blends like `am_michael,am_fenrir`).
> Don't use Phonon's 40M models: they are non-commercial. Research: `research/voiceover-tts-options.md`.

```bash
tools/voiceover/setup.sh && pip install ptts     # one time
source ~/.venvs/kokoro/bin/activate
python tools/voiceover/render.py episodes/01-vending-machines/narration-v2.md --engine phonon --voice Preston --duration-delta 0.3
python tools/voiceover/qa_asr.py episodes/01-vending-machines/voiceover   # auto-proofread by Whisper
```

That writes, into `episodes/<ep>/voiceover/`:
- `voiceover.wav` and `voiceover.mp3`: 48 kHz, mastered to −14 LUFS (YouTube's playback loudness)
- `captions.srt`: subtitles timed to the narration (upload to YouTube Studio → Subtitles)
- `chapters.txt`: paste into the description, and YouTube adds chapter markers
- `timings.json`: start and end of every chapter, paragraph and sentence (used for the shot list)

Writing tips for the narration file:
- `## Chapter name` starts a chapter and adds a longer pause
- `[[pause 1.5]]` adds a pause in seconds
- Write money as `$1.57` when "dollars" doesn't follow the number. Write counts with commas (`2,000`). Bare `1998` / `2025` are read as years.
- Fix a mispronounced word in `tools/voiceover/normalize.py` → `PRONUNCIATIONS`.

Compare voices: render auditions with `--paragraphs 6` into separate folders, then `python tools/voiceover/score_voices.py <dir>`
scores clarity (Whisper), pitch and pace for each.
