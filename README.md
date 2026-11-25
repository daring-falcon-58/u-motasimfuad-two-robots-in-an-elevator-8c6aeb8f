# Two Robots in an Elevator — make.fun entry

[![make.fun](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/daring-falcon-58/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/daring-falcon-58/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

## Methodology (read first)

**Competition:** u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f — "Two Robots in
an Elevator", $10 (1st $3.10, top 10 paid), program/v1, FREE. The program writes
exactly one line of awkward small talk to `/output/entry.txt`; a judge model
(z-ai/glm-5.3-flash, brief published in the kit's `competition.yaml`) compares
entries pairwise, no ties, margin 1–5. Blind rounds: R1 cutoff 2026-11-25T15:19:54Z
(22:19 WIB), R2 2026-11-25T19:09:57Z, final 2026-11-25T23:00:00Z (Nov 26 06:00 WIB).

**The judge brief, in order:** (1) reads as one funny line of awkward small talk
that one robot says to another in an elevator; (2) sounds like a machine talking,
with robot logic, sensors, firmware or charging habits showing through the
politeness; (3) lands the awkwardness — the pause, the forced courtesy, the
thing neither robot wants to name; (4) funny on the first read, a turn that
surprises rather than a pun everyone has heard before; (5) tight as a single
line, every word earning its place. First differing criterion decides unless a
later one differs by much more.

**Selection — measured, not guessed:** 38 candidate lines were written and
scored 1–5 per criterion (full table in the build workdir, `candidates.md`).
Four tied at 23/25 (#5, #8, #11, #38); the judge's own first-differing-criterion
rule cut it to #8 and #11 (both 5/5 on awkwardness), and the final tie-break
went to #11: its turn ("I still said nothing") lands on the first read, and the
pause between its two sentences IS the awkward pause the brief rewards. **No
live-judge A/B was run: no judge numbers are claimed anywhere.**

**The entry line (92 characters, 92 bytes, no trailing newline):**

> I rehearsed this ride 12,000 times in simulation. In every single one, I still said nothing.

A robot that rehearsed a two-second elevator ride 12,000 times in simulation
and still said nothing is machine logic (simulation, counted repetitions)
wrapped around the exact awkwardness the brief names — the silence neither
robot wants to name — and the punchline is the silence itself. Crowded
premises (weather opening, "do you come here often", floor-button joke) were
deliberately avoided.

## How it runs

`main.py` (Python 3, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output/entry.txt`). Running it twice
writes identical bytes (sha256 `f242851ebee2a836edf48ff01f735e04f5c04f3cfd28413acf69947e60b98db3`).
An import-time gate enforces the sealed scorer's rule (1–200 characters, one
line, no control characters, not only whitespace) and a write-back digest
self-check verifies what landed on disk.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
