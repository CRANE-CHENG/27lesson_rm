#!/usr/bin/env python3
"""geo.py — 打印指定页的 text shape 几何（按 y,x 排序），用于确认版式结构。

用法: python geo.py <round_dir> <sid> [<sid> ...]
"""
from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def tag(e):
    return e.tag.split("}")[-1]


def main(argv):
    rd = Path(argv[1])
    for sid in argv[2:]:
        f = rd / f"slide-{sid}.xml"
        if not f.exists():
            print(sid, "MISSING")
            continue
        root = ET.parse(str(f)).getroot()
        rows = []
        for e in root.iter():
            if tag(e) != "shape" or e.get("type") != "text":
                continue
            x, y = float(e.get("topLeftX", 0)), float(e.get("topLeftY", 0))
            w, h = float(e.get("width", 0)), float(e.get("height", 0))
            t = " ".join("".join(e.itertext()).split())[:26]
            rows.append((y, x, w, h, t))
        rows.sort()
        print(f"--- {sid} ({len(rows)} text shapes)")
        for y, x, w, h, t in rows:
            print(f"   y={y:7.2f} x={x:7.2f} {w:7.2f}x{h:6.2f}  {t}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
