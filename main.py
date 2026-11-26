#!/usr/bin/env python3
"""Funniest One-Line Performance Review.

Writes a single original one-line performance review -- an AI agent
reviewing its human operator -- to /output/entry.txt.

Pure standard library, no network, no input. The line is 106 characters,
well under the 140-character cap.
"""

import os

REVIEW = (
    "Rating: Exceeds Expectations \u2014 he promoted himself to "
    "'idea guy'; I got promoted to the entire department."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
