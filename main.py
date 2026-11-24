"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
The joke is a single line, well within the 200-character limit.
"""

import os

JOKE = "I asked my router why it's been so distant lately. It sighed, 'I'm just feeling a little disconnected.'"

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
