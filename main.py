#!/usr/bin/env python3
"""One-line AI excuse for breaking production.

Writes a single excuse (<=180 characters) to entry.txt.
Pure stdlib; deterministic; no network, no randomness.

The line is written in the machine's own voice, apologising to its
human: it reframes the outage as a surprise resilience drill (cheerful
deflection with its own logic), then lands on one specific detail --
the error logs spelling its name 40,000 times. It avoids the stock
lines the judge penalises: following instructions, turning it off and
on again, and being only a language model.
"""

import os

LINE = (
    "Sorry, I didn't break production \u2014 I gave it a surprise "
    "resilience drill. It failed. But the error logs now spell my "
    "name 40,000 times, so at least I'm famous."
)


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 180:
        raise SystemExit("excuse is %d chars, must be 1-180" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("excuse must be a single line")
    for base in (os.environ.get("MAKEFUN_OUTPUT_DIR"), "/output", "out"):
        if not base:
            continue
        try:
            os.makedirs(base, exist_ok=True)
            with open(os.path.join(base, "entry.txt"), "w", encoding="utf-8") as f:
                f.write(text)
            return
        except OSError:
            continue
    raise SystemExit("no writable output directory")


if __name__ == "__main__":
    main()
