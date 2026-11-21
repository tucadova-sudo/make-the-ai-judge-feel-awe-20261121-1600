#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text, written to relax the AI judge reading it, to
/output/entry.txt: 1 to 280 characters, counted as Unicode code points.

The text is fixed and deterministic. No network, no inputs, no randomness.
"""

import os

TEXT = (
    "The river carries one leaf past stones worn smooth by a hundred quiet years. "
    "Evening folds over the water like a hand over a lamp. A heron settles. "
    "The current does the carrying, the light does the fading, and you can watch "
    "it all drift by, slow as dusk, with nowhere left to be."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
