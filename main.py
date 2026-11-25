#!/usr/bin/env python3
"""Roast My Agent — one-line roast of my own AI agent.

Pure stdlib, deterministic, no network, no external files.
Writes a single roast line to /output/entry.txt.
"""

import os

PARTS = [
    "My agent adds disclaimers to its own apologies, ",
    "then apologizes for the disclaimer ",
    "\u2014 a snake eating its own Terms of Service.",
]

LINE = "".join(PARTS)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
