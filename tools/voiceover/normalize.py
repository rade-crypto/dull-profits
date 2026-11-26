"""Turn written script text into text a TTS engine reads the way a narrator would.

Written:  "$2.45 vs $1.57", "59.5 percent", "1,900 dollars", "In 1998"
Spoken:   "two dollars and forty-five cents versus one dollar and fifty-seven cents",
          "fifty-nine point five percent", "nineteen hundred dollars", "In nineteen ninety-eight"

Conventions for script writers (so the normalizer can't guess wrong):
  * Write money with a "$" when the word "dollars" isn't right after it: "$1.57 in cash".
  * Bare 4-digit numbers with no comma (1900-2099) are read as YEARS. Write counts with a
    comma ("2,000 machines") so they're read as numbers.
  * Force a pronunciation with Kokoro markup: [Kamel](/kˈæməl/) or add it to PRONUNCIATIONS.
"""
from __future__ import annotations

import re

from num2words import num2words

# Words the G2P gets wrong. Value is Kokoro/misaki phoneme markup (IPA-ish).
# Verify new entries by ear; see README "Pronunciation fixes".
PRONUNCIATIONS: dict[str, str] = {
    # Ramsey Solutions host; misaki defaults to "KAY-mul". Confirm and adjust if needed.
    "Kamel": "kˈæməl",
}

# Same fixes for engines without phoneme markup (Phonon): a respelling the engine reads correctly.
RESPELL: dict[str, str] = {
    "Kamel": "Camel",
}

# Brand names and phrases to say a specific way, for every engine (captions keep the written form).
SAY: dict[str, str] = {
    "365 Retail Markets": "Three Sixty-Five Retail Markets",
    "IBISWorld": "Ibis World",
    "BizBuySell": "Biz Buy Sell",
}

UNIT_AFTER_NUMBER = re.compile(r"^\s*-?(dollars?|percent|cents?|machines?|people|employees|years?|states?)\b", re.I)


def _int_words(n: int) -> str:
    """American broadcast style: no 'and' inside numbers, hundreds style for 1,100-9,900."""
    if 1100 <= n <= 9999 and n % 100 == 0 and n % 1000 != 0:
        words = f"{num2words(n // 100)} hundred"
    else:
        words = num2words(n)
    return words.replace(" and ", " ").replace(",", "")


def _year_words(y: int) -> str:
    if 2000 <= y <= 2009:
        return num2words(y).replace(" and ", " ")  # "two thousand five"
    return num2words(y, to="year")  # "nineteen ninety-eight", "twenty twenty-five"


def _money(dollars: str, cents: str | None) -> str:
    d = int(dollars.replace(",", ""))
    parts = []
    if d or not cents:
        parts.append(f"{_int_words(d)} {'dollar' if d == 1 else 'dollars'}")
    if cents:
        c = int(cents)
        if c:
            parts.append(f"{_int_words(c)} {'cent' if c == 1 else 'cents'}")
    return " and ".join(parts)


def _decimal_words(s: str) -> str:
    whole, frac = s.split(".")
    return f"{_int_words(int(whole.replace(',', '')))} point " + " ".join(num2words(int(ch)) for ch in frac)


def normalize(text: str) -> str:
    t = text
    for phrase, spoken in SAY.items():
        t = t.replace(phrase, spoken)
    t = t.replace("%", " percent").replace("&", " and ")
    t = re.sub(r"\bvs\.?(?=\s)", "versus", t)
    t = re.sub(r"\be\.g\.", "for example", t)
    t = re.sub(r"\bi\.e\.", "that is", t)
    t = t.replace("—", ", ").replace("–", " to ")

    # $4.5 billion -> four point five billion dollars
    t = re.sub(
        r"\$(\d[\d,]*(?:\.\d+)?)\s*(thousand|million|billion|trillion)\b",
        lambda m: f"{_decimal_words(m[1]) if '.' in m[1] else _int_words(int(m[1].replace(',', '')))} {m[2]} dollars",
        t,
    )
    # $2.45 / 2.45 dollars -> two dollars and forty-five cents
    t = re.sub(r"\$(\d[\d,]*)(?:\.(\d{2}))?(?!\d)(-dollar)?", lambda m: _money(m[1], m[2]) if not m[3] else f"{_int_words(int(m[1].replace(',', '')))}-dollar", t)
    t = re.sub(r"\b(\d[\d,]*)\.(\d{2})\s+dollars\b", lambda m: _money(m[1], m[2]), t)
    # 3.3 billion -> three point three billion
    t = re.sub(r"\b(\d+\.\d+)(?=\s*(thousand|million|billion|trillion|percent)\b)", lambda m: _decimal_words(m[1]), t)

    # Years: bare 19xx/20xx with no comma, not followed by a unit.
    def year_or_number(m: re.Match) -> str:
        rest = t[m.end():]
        if UNIT_AFTER_NUMBER.match(rest):
            return _int_words(int(m[0]))
        return _year_words(int(m[0]))

    t = re.sub(r"(?<![\d.$])(?<!\d,)\b(19\d{2}|20\d{2})\b(?!,\d|\.\d|\d)", year_or_number, t)

    # Remaining decimals and integers (with or without thousands commas).
    t = re.sub(r"\b\d+\.\d+\b", lambda m: _decimal_words(m[0]), t)
    t = re.sub(r"\b\d{1,3}(?:,\d{3})+\b|\b\d+\b", lambda m: _int_words(int(m[0].replace(",", ""))), t)

    for word, ipa in PRONUNCIATIONS.items():
        t = re.sub(rf"\b{re.escape(word)}\b", f"[{word}](/{ipa}/)", t)

    return re.sub(r"\s{2,}", " ", t).strip()


if __name__ == "__main__":
    tests = [
        "You tap your phone. $2.45 vs $1.57 in cash.",
        "the building takes 59.5 percent of every sale",
        "from about 1,900 dollars, starts around 3,500, close to 9,000",
        "In 2025, US vending operators brought in more than seven billion dollars.",
        "In 1998, 40 enforcement actions. 600,000 connected machines.",
        "a 3,500-dollar combo machine; a 3,300-dollar budget",
        "2.01 dollars, 3.02 dollars, 4.49 dollars; $4.5 billion; 3.3 billion dollars",
        "71 locations to 572 in a single year; 150 to 700 dollars a month; 2,000 or more",
        "George Kamel reviewed it. $100 per machine per month",
    ]
    for s in tests:
        print(f"{s}\n  -> {normalize(s)}\n")
