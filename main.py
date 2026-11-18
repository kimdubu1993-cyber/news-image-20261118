#!/usr/bin/env python3
"""Copy the front-page image to /output/entry.png.

The copy is byte-for-byte deterministic: the same source bytes always
produce the same output bytes, so repeated runs write identical files.
After copying, verify the output matches the source by size and SHA-256.
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news.png")
DST = "/output/entry.png"


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    if os.path.getsize(SRC) != os.path.getsize(DST) or _sha256(SRC) != _sha256(DST):
        raise SystemExit("entry.png does not match news.png after copy")


if __name__ == "__main__":
    main()
