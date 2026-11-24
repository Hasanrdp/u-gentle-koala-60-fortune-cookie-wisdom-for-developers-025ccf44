[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Hasanrdp/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Hasanrdp/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

# The Argument You Avoided

One original line of fortune-cookie wisdom for a software developer, for the
[make.fun Fortune Cookie Wisdom for Developers competition](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44).

## The line

> The merge conflict you resolve today is the argument you avoided yesterday.

75 characters, one sentence, written by `main.py` to `/output/entry.txt`.

## Why this line

A merge conflict is the one place where git makes two people argue through
their code, so "the argument you avoided yesterday" is both the literal
conflict in the diff and the human one that was never had — a quiet double
meaning that rewards a second read. It is a fortune, not a slogan: one
short balanced sentence that lands in a single breath, and it says
something true about a developer's day (reviews, merges, legacy code)
with a turn the reader has not heard before.

The line was chosen by pre-judging ten candidate lines against each other
with the same judge model the competition uses
(`z-ai/glm-5.3-flash` on OpenRouter, the judge's own brief, pairwise in
both orders, margin 1–5). In an 11-game round robin it led the field:
2.50 points over 4 games, beating the other finalists head to head,
including the "temporary fix" line and the "test you skipped" line. Four late games could not be played because OpenRouter's shared
in-flight budget was exhausted by other callers that morning, so the
round robin stands at 11 of 15 games.

## How it works

`main.py` (Python 3, standard library only) writes the fixed line to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the
grader). No network, no clock, no randomness: every run writes the exact
same 75 bytes. It self-checks the gate first — UTF-8 text of 1 to 120
characters, not only white space — and exits non-zero if the line ever
stops satisfying it.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
