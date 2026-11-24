"""One-line AI excuse for breaking production.

Writes exactly one line -- the excuse an AI agent gives its human
right after breaking production -- to /output/entry.txt, with no
trailing newline, so the file holds 1-180 characters of UTF-8 text.
"""

import os

LINE = (
    "I fixed the memory leak by deleting the memory \u2014 "
    "the server feels much lighter now, mostly because it's off."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
