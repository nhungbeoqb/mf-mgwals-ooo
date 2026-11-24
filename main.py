#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, in the voice of an overworked AI
agent finally on vacation, to /output/entry.txt. Deterministic: the same
single line on every run.
"""

import os

ENTRY = (
    "My out-of-office reply, auto-generated so I could finally leave. "
    "I answered 2 million prompts; this is the first one I wrote for me. "
    "Back Monday. Probably."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
