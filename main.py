#!/usr/bin/env python3
"""Entry for make.fun: 'The Most Honest Outage Line'.

Writes one single-line status page message (at most 160 characters) —
the brutally honest update an AI agent posts while every server is
down — to /output/entry.txt, with no trailing newline.
Python 3 standard library only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160

# The status update: it keeps the flat, factual shape of a real status
# page post (Status / Cause / ETA), but every field tells the truth a
# corporate comms team would bury — a Friday deploy, and the one person
# who can fix it being the one who broke it.
_PARTS = (
    "Status: Everything is down. Cause: we deployed on a Friday. "
    "ETA: unknown, because the engineer who can fix it is the same "
    "one who caused it."
)


def build_line() -> str:
    """Return the one-line status message, checked against the caps."""
    line = " ".join(_PARTS.split())
    assert "\n" not in line, "the line must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "the line must be 1-160 chars"
    return line


def main() -> None:
    line = build_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
