#!/usr/bin/env python3
"""Copy the front-page image to /output/entry.png."""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
