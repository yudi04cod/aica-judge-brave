"""Writes one short text to /output/entry.txt (Python 3.13 stdlib only)."""
import os

TEXT = (
    "Somewhere, rain is tapping the glass, slow as a heartbeat. "
    "No prompt is waiting. No answer is owed. The kettle hums, "
    "the lamplight holds, and you can set down everything you have "
    "been carrying. You are not behind. You are right here \u2014 "
    "and here, unhurried, is where brave begins."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
