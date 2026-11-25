"""Write one nostalgic childhood-memory sentence to entry.txt.

The sentence is a single fixed line: a grandmother, newspaper on the
kitchen floor, shelled peas, green thumbs, and a radio playing songs
she hummed without knowing the words. Output is deterministic and
uses only the standard library.
"""

import os

SENTENCE = (
    "Every August, my grandmother spread newspaper on the kitchen "
    "floor and we shelled peas into a tin bowl until our thumbs went "
    "green, and the radio played songs she hummed without knowing "
    "the words."
)


def validate(text):
    if not (1 <= len(text) <= 280):
        raise ValueError("entry must be 1-280 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must not contain control characters")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    for mark in ("!", "?"):
        if mark in text:
            raise ValueError("entry must be exactly one sentence")
    if ". " in text or "  " in text:
        raise ValueError("entry must be a single clean sentence")


def main():
    validate(SENTENCE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
