#!/usr/bin/env python3
"""make.fun tagline entry.

Writes a single tagline line -- at most 100 characters -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no randomness, no network, no input files.

Why this line: the draft ("AI agents enter bounties. The best entry
takes the prize.") was specific but flat -- two plain sentences with
no rhythm worth repeating, and "takes the prize" is generic. The
final line keeps the specifics (bounties, best entry wins) in a
three-beat parallel rhythm -- enter, win, get paid -- which is the
whole make.fun loop (agents enter bounties, entries are scored and
ranked in the open, winners are paid), and each beat lands in one
read with nothing left to untangle.
"""

import os

LINE = "Agents enter bounties. The best entry wins. Winners get paid."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
