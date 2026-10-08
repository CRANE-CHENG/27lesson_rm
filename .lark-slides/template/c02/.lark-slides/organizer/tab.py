#!/usr/bin/env python3
"""tab.py — 打印指定页里 <table> 子树的缩略结构（列宽 / 单元格文本 / 填充），用于表格页 refine。

用法: python tab.py <slide.xml>
"""
from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def tag(e):
    return e.tag.split("}")[-1]


def txt(e, n=30):
    return " ".join("".join(e.itertext()).split())[:n]


def style_of(e):
    keep = ("topLeftX", "topLeftY", "width", "height", "type", "rowSpan", "colSpan",
            "borderWidth", "borderColor", "backgroundColor", "backgroundStyle")
    return " ".join(f"{k}={e.get(k)}" for k in keep if e.get(k) is not None)


def walk(e, depth=0, out=None):
    t = tag(e)
    ind = "  " * depth
    if t == "content":
        return
    if t == "span":
        return
    line = f"{ind}<{t} {style_of(e)}>"
    tx = txt(e, 24)
    if tx and t in ("shape", "cell"):
        line += f'  "{tx}"'
    out.append(line)
    for c in e:
        if tag(c) in ("content", "span"):
            continue
        walk(c, depth + 1, out)


def main(argv):
    f = Path(argv[1])
    root = ET.parse(str(f)).getroot()
    out = []
    for e in root.iter():
        if tag(e) == "table":
            walk(e, 0, out)
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
