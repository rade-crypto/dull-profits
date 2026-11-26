"""Find when phrases are spoken in a voiceover, from timings.json word timings.

    from timing import Timeline
    tl = Timeline("episodes/01-vending-machines/voiceover/timings-clean.json")
    tl.at("five other players")          # start time (s) of the first match
    tl.at("the building", after=15.0)    # first match after 15 s
    tl.end("let the cash pile up")       # end time of the match

Matching ignores case and punctuation; digits and words are both fine as long as they match
how Whisper wrote them (it writes numbers as digits: "$2", "59.5%", "2025").
"""
import json
import re


def _clean(s: str) -> str:
    s = s.lower().replace("’", "'").replace(",", "")
    s = re.sub(r"[^a-z0-9'$%.]+", "", s)
    return s.rstrip(".") if not re.search(r"\d\.$", s) else s[:-1]


class Timeline:
    def __init__(self, path):
        d = json.load(open(path))
        self.duration = d["duration"]
        self.words = d["words"]
        # Whisper splits numbers ("59", ".5", "%"), so match on the joined characters, at word boundaries.
        self.text, self.owner, self.starts, self.ends = "", [], set(), set()
        for i, w in enumerate(self.words):
            c = _clean(w["w"])
            if not c:
                continue
            self.starts.add(len(self.text))
            self.text += c
            self.owner += [i] * len(c)
            self.ends.add(len(self.text))

    def _find(self, phrase, after=0.0):
        want = "".join(_clean(t) for t in phrase.split())
        k = self.text.find(want)
        while k != -1:
            e = k + len(want)
            if k in self.starts and e in self.ends and self.words[self.owner[k]]["start"] >= after - 1e-6:
                return self.owner[k], self.owner[e - 1]
            k = self.text.find(want, k + 1)
        raise KeyError(f"phrase not found after {after:.2f}s: {phrase!r}")

    def at(self, phrase, after=0.0):
        return self.words[self._find(phrase, after)[0]]["start"]

    def end(self, phrase, after=0.0):
        return self.words[self._find(phrase, after)[1]]["end"]
