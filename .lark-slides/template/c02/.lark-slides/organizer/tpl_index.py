#!/usr/bin/env python3
"""tpl_index.py — 扫描模板 source-slides，解出「角标数字 / 标题 / 视觉形态」三列，用于判定角标约定。

用法: python tpl_index.py <source-slides-dir>
"""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def tag(e):
    return e.tag.split("}")[-1]


def txt_of(e):
    return " ".join("".join(e.itertext()).split())


def main(argv):
    d = Path(argv[1])
    files = sorted(d.glob("slide-*.xml"))
    print(f"{'file':<14} {'badge':<6} {'badge_geo':<28} {'title/text(60)'}")
    for f in files:
        try:
            root = ET.parse(str(f)).getroot()
        except Exception as e:
            print(f.name, "parse fail", e)
            continue
        badge, bgeo, best, bestsize = "", "", "", 0.0
        for e in root.iter():
            if tag(e) != "shape" or e.get("type") != "text":
                continue
            t = txt_of(e)
            if not t:
                continue
            span_fs = 0.0
            for sp in e.iter():
                if tag(sp) == "span" and sp.get("fontSize"):
                    try:
                        span_fs = max(span_fs, float(sp.get("fontSize")))
                    except Exception:
                        pass
            if re.fullmatch(r"\d{1,2}", t) and span_fs >= 30:
                badge = t
                bgeo = f"{float(e.get('topLeftX',0)):.1f},{float(e.get('topLeftY',0)):.1f},{float(e.get('width',0)):.1f}x{float(e.get('height',0)):.1f}"
            elif span_fs > bestsize and len(t) > 1:
                bestsize, best = span_fs, t
        print(f"{f.name:<14} {badge:<6} {bgeo:<28} {best[:60]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
