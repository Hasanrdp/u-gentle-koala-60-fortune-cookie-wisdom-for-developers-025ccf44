#!/usr/bin/env python3
# Fortune Cookie Wisdom for Developers — make.fun entry.
#
# One original line of fortune-cookie wisdom for a software developer,
# written to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt locally).
#
# The line is a fixed string: no network, no clock, no randomness, no
# input of any kind, so every run writes the exact same bytes.
#
# Why this line: a merge conflict is the one place where git makes two
# people argue through their code, so "the argument you avoided
# yesterday" is both the literal conflict and the human one — a quiet
# double meaning that rewards a second read, in a single short sentence
# that lands in one breath, about a truth of a developer's day.

import os
import sys

LINE = "The merge conflict you resolve today is the argument you avoided yesterday."


def main() -> int:
    text = LINE
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 120
    # characters, not only white space.
    if not (1 <= len(text) <= 120):
        print(f"line is {len(text)} characters, outside 1..120", file=sys.stderr)
        return 1
    if not text.strip():
        print("line is only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
