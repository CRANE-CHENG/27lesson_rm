#!/usr/bin/env python3
"""dump.py — 按页打印每个元素的 id / 类型 / 几何 / 关键样式 / 文本，供审查定位。

用法: python dump.py <slide.xml>
"""
from __future__ import annotations

import sys
import xml.etree.ElementTree as ET


def tag(e):
    return e.tag.split("}")[-1]


def g(e, k, d=None):
    return e.get(k, d)


def preview(s, n=48):
    s = " / ".join(x.strip() for x in s.split("\n") if x.strip())
    return s[:n]


def main(argv):
    root = ET.parse(argv[1]).getroot()
    for e in root.iter():
        if tag(e) != "data":
            continue
        kids = list(e)
        print(f"-- data: {len(kids)} children")
        for i, k in enumerate(kids):
            t = tag(k)
            line = f"[{i}] {t} id={k.get('id')}"
            if t in ("shape", "img", "icon", "embed", "line", "polyline"):
                line += f" type={k.get('type')}"
            line += f" x={g(k,'topLeftX')} y={g(k,'topLeftY')} w={g(k,'width')} h={g(k,'height')}"
            for a in ("rotation", "presetHandlers", "alpha"):
                if k.get(a) is not None:
                    line += f" {a}={k.get(a)}"
            if t == "img":
                line += f" src={(k.get('src') or '')[:34]}"
            print(line)
            for sub in k.iter():
                st = tag(sub)
                if st == "content":
                    attrs = dict(sub.attrib)
                    keep = {kk: vv for kk, vv in attrs.items() if kk in
                            ("fontFamily", "fontSize", "color", "bold", "italic", "wrap",
                             "textAlign", "verticalAlign", "lineSpacing", "autoFit", "textType")}
                    print(f"     content {keep} :: {preview(''.join(sub.itertext()), 60)!r}")
                elif st == "span" and (sub.get("fontFamily") or sub.get("color")):
                    keep = {kk: vv for kk, vv in sub.attrib.items() if kk in
                            ("fontFamily", "fontSize", "color", "bold", "italic")}
                    print(f"       span  {keep} :: {preview(''.join(sub.itertext()), 40)!r}")
                elif st in ("fillColor",):
                    print(f"     fill  {sub.get('color')}")
                elif st == "border":
                    print(f"     border {dict(sub.attrib)}")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
