# Free male narrator TTS: options as of 2026-11-26

Goal: a calm, mature, credible male documentary narrator for a monetized YouTube channel.
Constraints: free; weights AND voice licensed for commercial use; runs on 4 CPU cores / 15 GB RAM / no GPU;
13 min of audio in under 40 min; no unconsented cloning of a real person.

## Verdict

1. **Phonon 31M (Gradium, Oct 2026). Voice `Preston`.** Alternates: `Miles` and `Trevor` (US), `Edwin` (UK).
   It meets every constraint. It ranks clearly above Kokoro on Artificial Analysis, and I measured it on this container at 3–5x realtime.
2. **Kyutai Pocket TTS, voice `javert` or `marius`.** These are CC0 donated voices. The VCTK voices `charles`, `george`, `paul` and `michael` (CC-BY 4.0) are a fallback.
3. **Kokoro-82M (already installed).** `am_michael`, `am_fenrir`, `am_puck`, `bm_george`, `bm_fable`. Use it as the fallback. It is no longer the best free male option.

Kokoro's male voices are no longer the best that meets the constraints. Phonon 31M is a later model from the Kyutai and Pocket-TTS lineage, and its English model and voices are Apache-2.0.

Nobody listened to these samples. Audition `Preston`, `Miles`, `Trevor` and `Edwin` by ear against `am_michael` (see "How to audition" below).

---

## 1. Phonon 31M English (Gradium): top pick

- **Weights:** `gradium/phonon-31m-en`, **Apache-2.0**. The model card says "weights, tokenizer, and voices in this repo: Apache 2.0".
  The runtime `ptts` is MIT OR Apache-2.0.
  - **Warning:** the **Phonon 40m** models (per-language and multilingual) are **CC BY-NC 4.0**. Do not use them.
    The default `ptts.TTS(lang="en")` downloads `phonon-31m-en`, which I confirmed in the HF cache. Pin it explicitly anyway (code below).
- **Voices:** `gradium/phonon-voices`, tagged **Apache-2.0**. These are preset voice embeddings used "with no cloning". The 12 character voices are labelled "made with Gradium Voice Design". The model card says nothing about where the 25 named voices came from. They are vendor stock voices, not voices cloned from a named real person.
- **Quality evidence:**
  - Artificial Analysis Speech Arena, open-weights board, Nov 2026: **Phonon 31M (English) Elo 1108, rank 5–7.**
    On the same board: Kokoro 82M 1060 (rank 9–11), Higgs Audio V3 1035, Chatterbox 1021, VibeVoice 1.5B 955, XTTS v2 917, StyleTTS 2 888.
    Every model ranked above Phonon is non-commercial or impractical on CPU (see the table below).
  - Gradium's own blind test: Phonon 31m 2098 vs Kokoro 2043.
    Gradium's own hard-sentence WER test: Phonon 31m 1.7% vs Kokoro 3.5% vs Kitten 7.4% vs NeuTTS Nano 8.7%.
  - The checkpoint's default voice, `Easton`, is male.
- **Measured on this container** (4 vCPU x86, `ptts` 0.7.1, q8 default, 117-word paragraph):

  | Voice | Accent | Wall time | Audio | Speed | Median F0 | Pitch spread (IQR) | Pace (default) |
  |---|---|---|---|---|---|---|---|
  | **Preston** | US | 11.5 s | 42.7 s | 3.7x RT | **108 Hz** (deepest) | 6.0 st | 164 wpm |
  | Russell | US | 12.2 s | 38.9 s | 3.2x | 119 Hz | 5.6 st | 181 wpm (too hyped per description) |
  | Trevor | US | 12.5 s | 44.2 s | 3.5x | 130 Hz | 5.7 st | 159 wpm |
  | Miles | US | 10.7 s | 41.0 s | 3.8x | 135 Hz | 4.7 st | 171 wpm |
  | Master Aldric | UK char. | 10.7 s | 52.8 s | 4.9x | 144 Hz | 4.4 st | 133 wpm ("wise old wizard, ~80", too theatrical) |
  | Edwin | UK | 10.3 s | 42.8 s | 4.2x | 151 Hz | 4.8 st | 164 wpm |

  - With `-c duration_delta=0.3`, Preston slows to **144 wpm** at 12.4 s wall time, which is a good documentary pace for a 40–65+ audience. With `duration_delta=0.6` he reads at 140 wpm.
  - **Throughput:** about 1,900 words / 13 min of audio renders in **about 3–4 min** on this box, well under the 40-min budget. Load time is 2.4 s. It needs no PyTorch.
- **Male voice IDs:**
  - US: `Easton`, `Micah`, `Trevor`, `Russell`, `Preston`, `Miles`.
  - UK: `Alfie`, `Hugh`, `Edwin`, `Spencer`, `Toby`, `Teddy`.
  - Characters: `Master Aldric`, `Sir Bramwell`, `Old Mortlake`, `Captain Silas Blackwater`, and others.
- **Catalog descriptions of the best narrator candidates:**
  - Preston: "Trim, focused delivery… steady, low-set core."
  - Miles: "Resonant and decisive, with genuine dynamic range."
  - Trevor: "Resonant mid-low core, phrases landing softly."
  - Edwin: "Efficient and firm, sincere… tidy articulation."
- **Quirks:**
  - The voices were designed for ads and customer support, so they are energetic by default. Slow them with `duration_delta` and keep the low default temperature of 0.3 for steady reads.
  - Long text is split into sentences, so prosody does not carry across sentences. Feed it one paragraph at a time, as `render.py` already does with its chunking.
  - English only. Text normalization (numbers, $, dates) depends on `lang="en"`. Keep using our `normalize.py` first.
  - Output is 24 kHz mono, the same as Kokoro, so `render.py`'s post-processing applies unchanged.
  - The model card's responsible-use section says: do not impersonate real people, and disclose synthetic speech. YouTube's "altered or synthetic content" label is for realistic content, so a plain narrator voice generally does not need it. A note in the video description is harmless.
- **Install and usage (Linux, CPU):**
  ```bash
  python -m pip install ptts            # pure CPU runtime, no torch; Python 3.9+
  ptts --lang en --list-voices          # catalog with descriptions
  ptts --lang en --threads 4 --voice Preston -c duration_delta=0.3 -o out.wav "Text here."
  ```
  ```python
  import ptts
  tts = ptts.TTS("hf://gradium/phonon-31m-en", lang="en", conditions={"duration_delta": 0.3})  # pin the Apache-2.0 model
  tts.save("out.wav", "Every year, thousands of profitable small businesses change hands.", voice="Preston")
  # tts.synth(...) / tts.stream(...) return audio for in-memory use; tts.sample_rate == 24000
  ```
  - The `conditions=` keyword appears in `ptts.TTS`'s signature (along with `set_conditions`), but I only exercised it through the CLI `-c` flag. If the keyword errors, call `tts.set_conditions(...)`.
- **Attribution:** Apache-2.0 does not require credit in the video. Keep the LICENSE/NOTICE if you redistribute the weights.
- Sources:
  - https://huggingface.co/gradium/phonon-31m-en
  - https://huggingface.co/gradium/phonon-voices
  - https://gradium.ai/blog/release-phonon-open-weight
  - https://github.com/gradium-ai/xn-ptts
  - https://artificialanalysis.ai/text-to-speech/leaderboard/open-weights

## 2. Kyutai Pocket TTS (100M): runner-up

- **Weights:** `kyutai/pocket-tts`, **CC-BY-4.0**. The repo is gated, so you accept the terms on HF. Credit Kyutai in the video description.
  The terms prohibit voice impersonation without consent and deceptive use.
- **Voice licences:** the preset names map to files in `kyutai/tts-voices` (`pocket_tts/utils/utils.py`).

  | Preset | Sex | Source | Licence | OK? |
  |---|---|---|---|---|
  | `javert`, `marius` | M | `voice-donations/` (donated for TTS use) | CC0 | **Yes, cleanest** |
  | `charles` (p254), `george` (p315), `paul` (p259), `michael` (p360) | M | VCTK | CC-BY 4.0 | Yes, with attribution (consented research corpus) |
  | `peter_yearsley`, `stuart_bell`, `bill_boerst` | M | voice-zero (LibriVox) | CC0 recordings | Licence OK. The readers never agreed to synthetic voice use, so avoid them under the no-cloning rule. |
  | `jean` | M | EARS | **CC-BY-NC** | **No** |
  | `cosette` | F | Expresso | **CC-BY-NC** | **No** |

- **Speed:** Kyutai says about 6x realtime on an M4 using 2 cores. On a 4 vCPU x86 VM they report about 2.3–2.5x. 13 min of audio therefore takes about 6 min.
- **Quality:** I found no Artificial Analysis entry. Gradium says Phonon (distilled from the same Pocket-TTS/Mimi stack) beats it.
- **Install and usage:**
  ```bash
  pip install pocket-tts --extra-index-url https://download.pytorch.org/whl/cpu
  ```
  ```python
  from pocket_tts import TTSModel; import scipy.io.wavfile
  m = TTSModel.load_model(); st = m.get_state_for_audio_prompt("javert")
  scipy.io.wavfile.write("out.wav", m.sample_rate, m.generate_audio(st, "Hello.").numpy())
  ```
- Sources:
  - https://github.com/kyutai-labs/pocket-tts
  - https://huggingface.co/kyutai/pocket-tts
  - https://huggingface.co/kyutai/tts-voices

## 3. Kokoro-82M (current): fallback

- Weights and voices are Apache-2.0. Artificial Analysis Elo is 1060.
- The author grades its male voices only C+ (`am_michael`, `am_fenrir`, `am_puck`). They remain a solid, legally clean fallback, and the pipeline is already built around them.

## Rejected or not better

| Option | Why not |
|---|---|
| Fish Audio Drama 3 / S2 Pro, OpenAudio S1 | Top of the arena (Elo 1278 / 1104), but Fish licences are CC-BY-NC(-SA). Not commercial. |
| Breeze TTS 2 (1229), Voxtral TTS (1094) | Non-commercial (Voxtral is CC BY-NC). |
| Ming-3.0-tts-0.5B (inclusionAI, Oct 2026) | MIT, with about 5 English preset voices, and very strong (Elo 1181). But it is a 0.5B LLM plus DiT (about 3 GB), was only tested on H800/H20 GPUs, and has no CPU numbers. 13 min on 4 cores is unlikely to fit in 40 min. Worth a test only if a GPU appears. |
| Phonon 40m (any) | CC BY-NC 4.0. |
| Chatterbox / Turbo (MIT) | Elo 1021, below Kokoro. The default voice is a "neutral" stock voice, not a male narrator; getting a male narrator means cloning from reference audio. On CPU it is 5–10x slower than GPU, which is marginal for 13 min. |
| Higgs Audio V3 (1035), VibeVoice 1.5B (955), StyleTTS 2 (888), XTTS v2 (917, CPML non-commercial) | Ranked below Kokoro and/or licence problems. They are also heavy on CPU. |
| Orpheus 3B (`leo`/`dan`/`zac`) | Llama 3.2 community licence (commercial OK under 700M MAU), but 3B plus SNAC on 4 CPU cores is far below realtime even as a GGUF. 13 min would blow the 40-min budget. |
| Supertonic 3 (M1–M5 male presets) | OpenRAIL-M (commercial with use restrictions and attribution). Upstream announced the open project's discontinuation (Voice Builder ended 2026-08-31). Lower community standing than Kokoro or Phonon. |
| Kitten TTS (`expr-voice-*-m`), NeuTTS Air/Nano | Apache-2.0, but clearly weaker (Gradium hard-set WER 7.4% / 8.7%). NeuTTS has cloning only, no preset voices with clear consent. |
| MeloTTS (MIT) | Older, flat prosody. Below Kokoro in community comparisons. |
| Piper `en_US-ryan-*` | Trained on RyanSpeech, which is **CC BY-NC-SA 4.0**: not commercial. `en_GB-alan` comes from the Mycroft mimic3 `apope` voice and its licence is unstated ("see URL"), so avoid it. Piper LibriTTS-based voices are CC-BY but lower quality. |
| edge-tts (`en-US-AndrewNeural`, `ChristopherNeural`, `en-GB-RyanNeural`) | An unofficial wrapper around Edge's Read Aloud endpoint. Microsoft Q&A says commercial use of Edge's services without an Azure subscription "could be a violation of our terms". Commercial output rights come from paid Azure Speech. Not free and safe. |
| Gemini TTS free tier (Charon, Orus, etc.) | Cloud, not local. Google declines to confirm monetized-YouTube use of free-tier output (forum, Oct 30 2026: "can't provide specific legal guidance"). Free-tier prompts and outputs are used to improve Google products. Output carries a SynthID watermark. Use the paid tier if you go this way. |
| ElevenLabs free | Its terms forbid commercial use. |

## How to audition by ear (5 min)

```bash
python -m pip install ptts
for v in Preston Miles Trevor Edwin; do
  ptts --lang en --threads 4 --voice "$v" -c duration_delta=0.3 -o "audition_$v.wav" "$(cat hook.txt)"
done
```

Compare these against the Kokoro `am_michael` hook. `tools/voiceover/score_voices.py` can score WER, F0 and pace on them once a `timings.json` exists.

To add Phonon to `render.py`, swap the Kokoro `KPipeline` call for `tts.synth(chunk, voice=...)`. Both output 24 kHz, so the chunking, pauses, loudness and SRT steps stay. Kokoro's word timings would be lost, so time captions with faster-whisper, which is already in `setup.sh`.
