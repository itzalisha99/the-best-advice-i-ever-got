#!/usr/bin/env python3
"""The Best Advice I Ever Got — one sentence, up to 200 characters.

Writes the entry to /output/entry.txt.
"""

import os

ENTRY = "My grandmother said, 'Don't marry a man who is rude to waiters,' and I have never once regretted listening."


def validate(text):
    """Mirror the bounty gate: 1-200 chars, not only whitespace, one sentence."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text.strip().count(".") > 1 or text.strip().count("!") > 0 or text.strip().count("?") > 0:
        raise ValueError("entry must be a single sentence")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the file is byte-identical to the entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the entry")
    print(ENTRY)


if __name__ == "__main__":
    main()
