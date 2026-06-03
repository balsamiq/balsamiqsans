#!/usr/bin/env python3
"""Post-build script: adds STAT and meta tables to all compiled fonts."""

import glob
import os
import sys
from fontTools.ttLib import TTFont, newTable
from fontTools.otlLib.builder import buildStatTable

FONTS_DIR = "fonts/ttf"

# Per-font STAT axis configurations using Format 1 axis values (no Format 4).
# Each font gets only its own axis values so the STAT table correctly describes
# where each static instance sits in the design space.
# Elidable flag (0x2) marks the "normal" value on each axis; linkedValue wires
# Roman→Italic so style linking works correctly.
FONT_STAT = {
    "BalsamiqSans-Regular.ttf": [
        {
            "tag": "wght", "name": "Weight",
            "values": [{"value": 400, "name": "Regular", "flags": 0x2, "linkedValue": 700}],
        },
        {
            "tag": "ital", "name": "Italic",
            "values": [{"value": 0, "name": "Roman", "flags": 0x2, "linkedValue": 1}],
        },
    ],
    "BalsamiqSans-Bold.ttf": [
        {
            "tag": "wght", "name": "Weight",
            "values": [{"value": 700, "name": "Bold"}],
        },
        {
            "tag": "ital", "name": "Italic",
            "values": [{"value": 0, "name": "Roman", "flags": 0x2, "linkedValue": 1}],
        },
    ],
    "BalsamiqSans-Italic.ttf": [
        {
            "tag": "wght", "name": "Weight",
            "values": [{"value": 400, "name": "Regular", "flags": 0x2, "linkedValue": 700}],
        },
        {
            "tag": "ital", "name": "Italic",
            "values": [{"value": 1, "name": "Italic"}],
        },
    ],
    "BalsamiqSans-BoldItalic.ttf": [
        {
            "tag": "wght", "name": "Weight",
            "values": [{"value": 700, "name": "Bold"}],
        },
        {
            "tag": "ital", "name": "Italic",
            "values": [{"value": 1, "name": "Italic"}],
        },
    ],
}

# Latin-script language tags for the meta table.
META_DLNG = "Latn"
META_SLNG = "Latn"


def add_stat(font, filename):
    axes = FONT_STAT.get(filename)
    if axes is None:
        print(f"  WARNING: no STAT config for {filename}, skipping STAT")
        return
    buildStatTable(font, axes)
    print(f"  Added STAT table ({filename})")


def add_meta(font, filename):
    meta = newTable("meta")
    meta.data = {"dlng": META_DLNG, "slng": META_SLNG}
    font["meta"] = meta
    print(f"  Added meta table ({filename})")


def process_font(path):
    filename = os.path.basename(path)
    print(f"Processing {filename}")
    font = TTFont(path)
    add_stat(font, filename)
    add_meta(font, filename)
    font.save(path)


if __name__ == "__main__":
    paths = sorted(glob.glob(os.path.join(FONTS_DIR, "*.ttf")))
    if not paths:
        print(f"No TTF files found in {FONTS_DIR}", file=sys.stderr)
        sys.exit(1)
    for path in paths:
        process_font(path)
    print("Done.")
