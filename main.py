#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of my own agent.

Pure stdlib, deterministic, no network, no external files.
Writes exactly one roast line to /output/entry.txt.
"""

import os

# The roast is assembled from three beats: the setup names the habit,
# the escalation turns it on itself, and the punchline lands the image.
SETUP = "My agent adds disclaimers to its own apologies"
ESCALATION = "then apologizes for the disclaimer"
PUNCHLINE = "a snake eating its own Terms of Service."

OUTPUT_PATH = "/output/entry.txt"


def build_roast():
    """Join the three beats into the single roast line."""
    return "{}, {} \u2014 {}".format(SETUP, ESCALATION, PUNCHLINE)


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(build_roast() + "\n")


if __name__ == "__main__":
    main()
