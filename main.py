#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message -- make.fun entry (program/v1).

Writes the entrant's single commit message, exactly, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line (64 characters, one line):

    fix: tests pass now. the app does not. unclear which one matters

Why this one, after drafting 17 candidates and judging them pairwise
against the judge's brief (reads as a real commit message for a fix that
backfired first, then laugh-out-loud funny, then the specific irony of a
repair that broke more than it mended, then a tired engineer's voice, then
a fresh angle -- see candidates.md):

- Three beats, each one a sentence: the fix worked, the app broke, and the
  author no longer knows which of those two facts counts. The joke is the
  shrug, not the damage.
- The specific irony is exact: the repair optimised the metric (green
  tests) while destroying the thing the metric was supposed to measure.
  The fix did not fail — it succeeded at the wrong thing.
- It reads like a real commit subject line: lowercase "fix:", plain words,
  the kind of thing typed at the end of a bad day when the author has
  stopped pretending the suite and the product agree.
- No worn angle: no revert, no testing in production, no "broke
  everything" -- the damage is implied, never stated, and the line lands
  on its own without an explanation.
- Pairwise final: it beat the runner-up -- "fix: the database is now
  consistent. consistently empty" -- on the bigger laugh and on the more
  specific fix-vs-app irony.
"""

import os

LINE = "fix: tests pass now. the app does not. unclear which one matters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 100 characters,
    # not only white space. One line, 64 characters, no trailing newline.
    assert len(LINE) == 64, "gate: exactly the 64-character line"
    assert 1 <= len(LINE) <= 100, "gate: 1-100 characters"
    assert LINE.strip() == LINE, "gate: no surrounding whitespace"
    assert "\n" not in LINE, "one line"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: what lands on disk must be exactly the line.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt must hold exactly the line"


if __name__ == "__main__":
    main()
