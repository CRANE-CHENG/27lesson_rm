#!/usr/bin/env python3
"""vfy.py — 结构核对：角标文字 / 步骤竖条数 / 代码框几何 / 元素总数。

用法: python vfy.py <file.xml> [<file.xml> ...]
"""
from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def local(e):
    return e.tag.split("}")[-1]


def main(argv):
    for p in argv[1:]:
        f = Path(p)
        if not f.exists():
            print(f"{f.name}: MISSING")
            continue
        root = ET.parse(str(f)).getroot()
        data = None
        for e in root.iter():
            if local(e) == "data":
                data = e
        n = len(list(data)) if data is not None else 0
        badge, bars, code = None, 0, ""
        for e in data:
            if local(e) != "shape":
                continue
            y = float(e.get("topLeftY", 0) or 0)
            x = float(e.get("topLeftX", 0) or 0)
            w = float(e.get("width", 0) or 0)
            if e.get("type") == "text" and abs(y - 15.7691) < 1:
                badge = "".join(e.itertext()).strip()
            if (e.get("type") == "rect" and abs(x - 56.42) < 0.1
                    and abs(float(e.get("width", 0) or 0) - 4) < 0.1):
                bars += 1
            if e.get("type") == "text" and abs(x - 62.42) < 0.2:
                t = "".join(e.itertext())
                if "int " in t or "char " in t or "Date " in t or "void " in t:
                    code = f"code({x},{y},{w})"
        print(f"{f.name}: sid={root.get('id')} elements={n} badge={badge!r} bars={bars} {code}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
