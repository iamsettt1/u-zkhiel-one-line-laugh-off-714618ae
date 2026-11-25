"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt: a single joke that
lands on a cold read, with no setup notes and no explanation.

The joke: a calendar app reminding its owner to "be spontaneous today"
at exactly 9:00 a.m. -- the punchline is the contradiction itself, and
it lands on the very last words.
"""

import os

LINE = "My calendar reminded me to 'be spontaneous today' at exactly 9:00 a.m."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the competition gate in code: 1-200 UTF-8 chars, one line.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE and LINE.strip(), "entry must not be blank"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
