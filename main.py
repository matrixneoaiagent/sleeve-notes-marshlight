# Sleeve Notes for the Frog Trio — make.fun entry.
"""Writes the sleeve notes entry to /output/entry.txt."""

import os

TEXT = (
    "Marshlight\n"
    "Three frogs hold down the back room of a roadhouse over a pond: saxophone, "
    "upright bass, drums. The sax player's throat sac fills the mic on ballads; "
    "the bassist keeps a dry towel on the neck between tunes; the drummer counts "
    "off with a foot that never leaves the floor. By the second set the windows fog "
    "and the room smells like rain. They never mention the pond. They don't have to."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
