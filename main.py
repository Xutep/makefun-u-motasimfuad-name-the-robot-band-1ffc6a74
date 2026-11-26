#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry.

Writes one funny name for a band made of robots, plus a few words on
the band's hit song, to /output/entry.txt. Deterministic, stdlib only:
the text is fixed, so every run produces the exact same entry.
"""

import os
import sys

# The entry: band name + hit song line. Must be 1-200 UTF-8 characters.
ENTRY_TEXT = (
    "THE BLUE SCREENS OF DEATH METAL"
    " \u2014 hit single \u2018Have You Tried Turning Me Off and On Again\u2019"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY_TEXT.strip()
    if not text:
        print("error: entry text is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: entry is {len(text)} chars, over the 200 limit",
              file=sys.stderr)
        return 1
    data = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Read back and verify the file holds exactly the entry text.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(data)} bytes ({len(text)} chars) to {OUTPUT_PATH}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
