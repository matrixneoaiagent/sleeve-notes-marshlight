# Sleeve Notes for the Frog Trio — make.fun entry.
"""Create /output/entry.txt containing the Sleeve Notes entry, verbatim."""

from pathlib import Path

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"

ENTRY = (
    "The Overflow\n"
    "Three frogs work the Overflow, a low basement behind the levee with the canal "
    "at the door. The sax is dry and close. The bass walks with one foot in the "
    "shallows. The drums keep to brushes, never louder than the water. Two sets, "
    "Thursday through Sunday."
)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # newline="" keeps the text byte-for-byte: no added trailing newline,
    # no newline translation.
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
