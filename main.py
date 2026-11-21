#!/usr/bin/env python3
"""news-image-20261121: the world's news of Saturday 21 November 2026,
summed up in one image.

The entry point copies the front page shipped in this repository to
/output/entry.png. The copy is exact, so running the program twice
writes byte-identical output both times. Python 3.13, standard
library only, no network access.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET = "/output/entry.png"


def main() -> int:
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    print("wrote %s (%d bytes)" % (TARGET, os.path.getsize(TARGET)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
