#!/usr/bin/env python3
"""Render a narration script to a finished voiceover with Kokoro-82M (free, Apache-2.0, CPU).

    python render.py ../../episodes/01-vending-machines/narration.md --voice af_heart

Outputs (in --out, default: <episode>/voiceover/):
    voiceover.wav      48 kHz / 24-bit, loudness-normalized to -14 LUFS (YouTube's playback target)
    voiceover.mp3      same, 192 kbps, for quick listening / sharing
    captions.srt       subtitles timed from the model's own word timings (upload to YouTube)
    chapters.txt       YouTube chapter list, paste into the description
    timings.json       start/end of every chapter, paragraph, sentence (drives the edit / shot list)

Narration file format (Markdown-ish):
    # Title                -> ignored
    ## Chapter name        -> YouTube chapter + longer pause
    blank line             -> paragraph break
    [[pause 1.5]]          -> explicit pause, seconds
    <!-- comment -->       -> ignored
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import soundfile as sf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize import normalize  # noqa: E402

SR = 24_000
GAP_CHUNK = 0.30      # between chunks inside a paragraph
GAP_PARAGRAPH = 0.62  # between paragraphs
GAP_CHAPTER = 1.05    # at a chapter boundary
LEAD_IN, TAIL_OUT = 0.35, 1.2
MAX_CHUNK_CHARS = 300  # Kokoro sounds best around 100-250 phonemes per call
MAX_CUE_CHARS = 84     # two subtitle lines of ~42


# ---------------------------------------------------------------- parsing
@dataclass
class Piece:            # one subtitle cue
    text: str
    spoken: str
    start: float = 0.0
    end: float = 0.0


@dataclass
class Sentence:
    text: str
    pieces: list[Piece] = field(default_factory=list)
    start: float = 0.0
    end: float = 0.0


@dataclass
class Paragraph:
    chapter: str
    sentences: list[Sentence]
    pause_before: float | None = None
    start: float = 0.0
    end: float = 0.0

    @property
    def text(self) -> str:
        return " ".join(s.text for s in self.sentences)


SENT_SPLIT = re.compile(r"(?<=[.!?])[\"”’)]?\s+(?=[\"“(]?[A-Z0-9$])")


def split_cues(sentence: str) -> list[str]:
    if len(sentence) <= MAX_CUE_CHARS:
        return [sentence]
    mid = len(sentence) / 2
    # Prefer clause punctuation, then conjunctions, then any space, nearest the middle.
    for pattern in (r"[,;:]\s", r"\s(?=(?:and|but|or|so|because|where|which|while|before|after|versus)\b)", r"\s"):
        cands = [m.end() if pattern.startswith("[") else m.start() for m in re.finditer(pattern, sentence)]
        cands = [c for c in cands if 12 < c < len(sentence) - 12]
        if cands:
            cut = min(cands, key=lambda c: abs(c - mid))
            return split_cues(sentence[:cut].strip()) + split_cues(sentence[cut:].strip())
    return [sentence]


def parse(path: Path) -> list[Paragraph]:
    raw = re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S)
    paras: list[Paragraph] = []
    chapter, buf, pending_pause = "Intro", [], None

    def flush():
        nonlocal buf, pending_pause
        text = " ".join(buf).strip()
        buf = []
        if not text:
            return
        sents = []
        for s in SENT_SPLIT.split(text):
            s = s.strip()
            if s:
                sents.append(Sentence(s, [Piece(c, normalize(c)) for c in split_cues(s)]))
        paras.append(Paragraph(chapter, sents, pending_pause))
        pending_pause = None

    for line in raw.splitlines():
        st = line.strip()
        if st.startswith("## "):
            flush()
            chapter = st[3:].strip()
            pending_pause = GAP_CHAPTER if paras else None
        elif st.startswith("# "):
            continue
        elif m := re.fullmatch(r"\[\[pause\s+([\d.]+)\]\]", st):
            flush()
            pending_pause = float(m[1])
        elif not st:
            flush()
        else:
            buf.append(st)
    flush()
    return paras


def chunk_sentences(sents: list[Sentence]) -> list[list[Sentence]]:
    chunks, cur = [], []
    for s in sents:
        if cur and sum(len(x.text) + 1 for x in cur) + len(s.text) > MAX_CHUNK_CHARS:
            chunks.append(cur)
            cur = []
        cur.append(s)
    if cur:
        chunks.append(cur)
    # Kokoro is weak on very short utterances: fold a tiny trailing chunk into the previous one.
    if len(chunks) > 1 and sum(len(x.text) for x in chunks[-1]) < 40:
        chunks[-2].extend(chunks.pop())
    return chunks


# ---------------------------------------------------------------- synthesis
ALNUM = re.compile(r"[A-Za-z0-9]")
MARKUP = re.compile(r"\[([^\]]+)\]\(/[^)]*/\)")


def synth_chunk(pipe, chunk: list[Sentence], voice: str, speed: float):
    pieces = [p for s in chunk for p in s.pieces]
    text = " ".join(p.spoken for p in pieces)
    audio, toks, offset = [], [], 0.0
    for r in pipe(text, voice=voice, speed=speed, split_pattern=None):
        a = r.audio.numpy() if hasattr(r.audio, "numpy") else np.asarray(r.audio)
        for t in r.tokens or []:
            if t.start_ts is not None and t.end_ts is not None:
                toks.append((t.text, t.start_ts + offset, t.end_ts + offset))
        audio.append(a)
        offset += len(a) / SR
    audio = np.concatenate(audio)

    # Trim leading/trailing silence to make pauses consistent.
    env = np.abs(audio)
    thr = max(env.max() * 0.012, 1e-4)
    loud = np.where(env > thr)[0]
    s0 = max(0, loud[0] - int(0.05 * SR))
    s1 = min(len(audio), loud[-1] + int(0.14 * SR))
    audio = audio[s0:s1]
    shift = s0 / SR
    toks = [(w, max(0.0, a - shift), max(0.0, b - shift)) for w, a, b in toks]

    # Assign word timings to subtitle pieces by counting letters/digits (robust to punctuation).
    budgets = [len(ALNUM.findall(MARKUP.sub(r"\1", p.spoken))) for p in pieces]
    i, used = 0, 0
    spans: list[list[float]] = [[] for _ in pieces]
    for w, a, b in toks:
        n = len(ALNUM.findall(w))
        if n == 0:
            continue
        while i < len(pieces) - 1 and used >= budgets[i]:
            i, used = i + 1, 0
        spans[i] += [a, b]
        used += n
    dur = len(audio) / SR
    for p, sp in zip(pieces, spans):
        p.start, p.end = (min(sp), max(sp)) if sp else (0.0, dur)
    return audio, dur


def trim(audio: np.ndarray) -> tuple[np.ndarray, float]:
    env = np.abs(audio)
    loud = np.where(env > max(env.max() * 0.012, 1e-4))[0]
    s0 = max(0, loud[0] - int(0.05 * SR))
    s1 = min(len(audio), loud[-1] + int(0.14 * SR))
    return audio[s0:s1], s0 / SR


# Phonon has no phoneme markup: say respelled words instead (see normalize.RESPELL).
def plain(spoken: str) -> str:
    from normalize import RESPELL
    return MARKUP.sub(lambda m: RESPELL.get(m[1], m[1]), spoken)


def synth_sentence_phonon(tts, sent: Sentence, voice: str, seed: int):
    """Phonon splits text into sentences internally, so one call per sentence loses no prosody
    and gives exact sentence timings. Subtitle pieces inside a sentence are timed by length."""
    audio = np.asarray(tts.synth(" ".join(plain(p.spoken) for p in sent.pieces), voice=voice, seed=seed), dtype=np.float32)
    audio, _ = trim(audio)
    dur = len(audio) / SR
    budgets = [max(1, len(ALNUM.findall(plain(p.spoken)))) for p in sent.pieces]
    a, b, tot, acc = 0.05, max(0.06, dur - 0.14), sum(budgets), 0
    for p, n in zip(sent.pieces, budgets):
        p.start = a + (b - a) * acc / tot
        acc += n
        p.end = a + (b - a) * acc / tot
    return audio, dur


# ---------------------------------------------------------------- outputs
def fmt_srt(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def fmt_chapter(t: float) -> str:
    t = int(t)
    return f"{t // 3600}:{t % 3600 // 60:02}:{t % 60:02}" if t >= 3600 else f"{t // 60}:{t % 60:02}"


def wrap2(text: str, width: int = 42) -> str:
    if len(text) <= width:
        return text
    mid = len(text) // 2
    spaces = [m.start() for m in re.finditer(" ", text)]
    cut = min(spaces, key=lambda c: abs(c - mid))
    return text[:cut] + "\n" + text[cut + 1:]


def master(raw_wav: Path, out_wav: Path, out_mp3: Path, lufs: float):
    pre = "highpass=f=70,lowpass=f=15500,acompressor=threshold=-21dB:ratio=2.2:attack=8:release=120:makeup=1.5"
    probe = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(raw_wav), "-af",
         f"{pre},loudnorm=I={lufs}:TP=-1.0:LRA=9:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True, check=True).stderr
    m = json.loads(probe[probe.rindex("{"):probe.rindex("}") + 1])
    ln = (f"loudnorm=I={lufs}:TP=-1.0:LRA=9:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    chain = f"{pre},{ln},aresample=48000"
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(raw_wav), "-af", chain,
                    "-ar", "48000", "-c:a", "pcm_s24le", str(out_wav)], check=True)
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(out_wav),
                    "-c:a", "libmp3lame", "-b:a", "192k", str(out_mp3)], check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("narration", type=Path)
    ap.add_argument("--voice", default="af_heart", help="Kokoro voice id, or a blend like 'am_michael,am_fenrir'")
    ap.add_argument("--engine", choices=["kokoro", "phonon"], default="kokoro")
    ap.add_argument("--speed", type=float, default=1.0, help="Kokoro speaking speed (0.95 = calmer)")
    ap.add_argument("--duration-delta", type=float, default=0.3, help="Phonon pacing; higher = slower (0.3 ~ 144 wpm)")
    ap.add_argument("--seed", type=int, default=7, help="Phonon sampling seed, for repeatable renders")
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--paragraphs", type=int, default=0, help="only render the first N paragraphs (auditions)")
    ap.add_argument("--start", type=int, default=1, help="first paragraph to render, 1-based (auditions)")
    ap.add_argument("--lufs", type=float, default=-14.0)
    ap.add_argument("--name", default="voiceover")
    args = ap.parse_args()

    out = args.out or args.narration.parent / "voiceover"
    out.mkdir(parents=True, exist_ok=True)
    paras = parse(args.narration)
    paras = paras[args.start - 1:]
    if args.paragraphs:
        paras = paras[: args.paragraphs]

    if args.engine == "kokoro":
        from kokoro import KPipeline  # imported late so --help is fast
        # British voices (bf_/bm_) need British G2P; everything else American.
        lang = "b" if args.voice.split(",")[0].startswith(("bf_", "bm_")) else "a"
        pipe = KPipeline(lang_code=lang, repo_id="hexgrad/Kokoro-82M")
    else:
        import ptts
        # Pin the Apache-2.0 31M model (the 40M Phonon models are non-commercial).
        pipe = ptts.TTS("hf://gradium/phonon-31m-en", lang="en", conditions={"duration_delta": args.duration_delta})

    t0 = time.time()
    parts = [np.zeros(int(LEAD_IN * SR), dtype=np.float32)]
    cursor = LEAD_IN
    for pi, para in enumerate(paras):
        if pi:
            gap = para.pause_before if para.pause_before is not None else GAP_PARAGRAPH
            parts.append(np.zeros(int(gap * SR), dtype=np.float32))
            cursor += int(gap * SR) / SR
        para.start = cursor
        units = chunk_sentences(para.sentences) if args.engine == "kokoro" else [[s] for s in para.sentences]
        for ci, chunk in enumerate(units):
            if ci:
                parts.append(np.zeros(int(GAP_CHUNK * SR), dtype=np.float32))
                cursor += int(GAP_CHUNK * SR) / SR
            if args.engine == "kokoro":
                audio, dur = synth_chunk(pipe, chunk, args.voice, args.speed)
            else:
                audio, dur = synth_sentence_phonon(pipe, chunk[0], args.voice, args.seed)
            for s in chunk:
                for p in s.pieces:
                    p.start += cursor
                    p.end += cursor
                s.start, s.end = s.pieces[0].start, s.pieces[-1].end
            parts.append(audio.astype(np.float32))
            cursor += dur
        para.end = cursor
        print(f"  [{pi + 1}/{len(paras)}] {fmt_chapter(para.start)}  {para.text[:70]}…", flush=True)
    parts.append(np.zeros(int(TAIL_OUT * SR), dtype=np.float32))
    total = cursor + TAIL_OUT
    full = np.concatenate(parts)

    with tempfile.TemporaryDirectory() as td:
        raw = Path(td) / "raw.wav"
        sf.write(raw, full, SR, subtype="PCM_16")
        master(raw, out / f"{args.name}.wav", out / f"{args.name}.mp3", args.lufs)

    # Subtitles: hold each cue until just before the next one (max +0.8 s) so text doesn't flicker.
    cues = [p for para in paras for s in para.sentences for p in s.pieces]
    srt = []
    for i, c in enumerate(cues):
        nxt = cues[i + 1].start if i + 1 < len(cues) else total
        end = min(max(c.end + 0.25, c.start + 1.0), nxt - 0.04, c.end + 0.8)
        srt.append(f"{i + 1}\n{fmt_srt(c.start)} --> {fmt_srt(max(end, c.end))}\n{wrap2(c.text)}\n")
    (out / "captions.srt").write_text("\n".join(srt), encoding="utf-8")

    chapters, seen = [], set()
    for para in paras:
        if para.chapter not in seen:
            seen.add(para.chapter)
            chapters.append((0.0 if not chapters else para.start - 0.3, para.chapter))
    (out / "chapters.txt").write_text("\n".join(f"{fmt_chapter(t)} {name}" for t, name in chapters) + "\n", encoding="utf-8")

    words = sum(len(p.text.split()) for p in paras)
    timing = {
        "engine": args.engine, "voice": args.voice,
        "speed": args.speed if args.engine == "kokoro" else None,
        "duration_delta": args.duration_delta if args.engine == "phonon" else None, "duration_s": round(total, 2),
        "words": words, "wpm": round(words / (total / 60), 1),
        "chapters": [{"start": round(t, 2), "title": n} for t, n in chapters],
        "paragraphs": [{"i": i + 1, "chapter": p.chapter, "start": round(p.start, 2), "end": round(p.end, 2),
                        "text": p.text,
                        "sentences": [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text} for s in p.sentences]}
                       for i, p in enumerate(paras)],
    }
    (out / "timings.json").write_text(json.dumps(timing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"done: {fmt_chapter(total)} of audio ({timing['wpm']} wpm) in {time.time() - t0:.0f}s -> {out}")


if __name__ == "__main__":
    main()
