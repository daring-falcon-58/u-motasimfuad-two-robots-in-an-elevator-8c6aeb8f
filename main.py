#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Methodology (read first): the competition asks for a single line, under 200
characters, of awkward small talk one robot says to another while they ride
an elevator together. A judge model (z-ai/glm-5.3-flash, brief published in
the kit's competition.yaml) compares entries pairwise, no ties, margin 1-5,
weighing in order: (1) reads as robot-to-robot elevator small talk;
(2) machine logic showing through the politeness; (3) the awkwardness landing;
(4) funny on the first read, a surprising turn, not a heard-before pun;
(5) tight single line, every word earning its place.

Selection (full table in candidates.md, this workdir): 38 candidate lines
were written and scored 1-5 per criterion. Four tied at 23/25 (#5, #8, #11,
#38); the judge's own first-differing-criterion rule cut it to #8 and #11
(both 5/5 on awkwardness), and the final tie-break went to #11: its turn
("I still said nothing") lands on the first read, and the pause between its
two sentences IS the awkward pause the brief rewards. No live-judge A/B was
run; no judge numbers are claimed anywhere.

The winning line (92 characters, 92 bytes, no trailing newline):

    I rehearsed this ride 12,000 times in simulation. In every single one,
    I still said nothing.

Why it wins: a robot that rehearsed a two-second elevator ride 12,000 times
in simulation and still said nothing is machine logic (simulation, counted
repetitions) wrapped around the exact awkwardness the brief names — the
silence neither robot wants to name — and the punchline is the silence
itself. No weather opening, no "do you come here often", no floor-button
joke: the crowded premises in a 1,674-entry field were deliberately avoided
(the comp page's Feed is JS-rendered, so no live entrant texts could be
read; avoidance is by premise, not by copying).

Run it (outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
from pathlib import Path

# The entry line. Exactly one line, 92 characters, no trailing newline.
ENTRY = "I rehearsed this ride 12,000 times in simulation. In every single one, I still said nothing."

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def _validate(text: str) -> None:
    """Import-time gate: the sealed scorer requires UTF-8 text of 1-200
    characters, not only whitespace, in a single line."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text.strip() != text or not text.strip():
        raise ValueError("entry must not be only whitespace or padded")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must contain no control characters")


_validate(ENTRY)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(ENTRY, encoding="utf-8")
    # Write-back self-check: what landed on disk must be exactly ENTRY.
    written = TARGET.read_bytes()
    if written != ENTRY.encode("utf-8"):
        raise RuntimeError("entry.txt on disk does not match ENTRY")
    digest = hashlib.sha256(written).hexdigest()
    print(f"Wrote {TARGET} ({len(written)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
