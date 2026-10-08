#!/usr/bin/env python3
"""check_content.py — active_rebuild 内容页专项体检（Organizer 审查用）。

用法: python check_content.py <slide.xml> [iconpark-index.json]

检查项：
  1. icon 类型合法性（iconType 必须来自 IconPark 索引）与 emoji 混入
  2. 字体族清单（只允许 思源黑体 / Consolas / 锐字真言体免费商用）
  3. 文字色清单（便于与模板主色比对，禁止新色族）
  4. 正文安全区（x 62~898, y 100~478）越界文字
  5. <embed> 存在性与底缘 y<=476 约束
  6. <img> src token 清单
  7. 字号分布
"""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET

NS = {"s": "https://www.larkoffice.com/sml/2.0"}
ALLOWED_FONTS = {"思源黑体", "Consolas", "锐字真言体免费商用", "思源宋体"}
EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF"
    "\U00002190-\U000021FF\U00002B00-\U00002BFF\uFE0F]"
)
SAFE_L, SAFE_T, SAFE_R, SAFE_B = 62.0, 100.0, 898.0, 478.0


def tag(e):
    return e.tag.split("}")[-1]


def load_icon_names(path):
    names = set()
    try:
        raw = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        return names, f"iconpark index load failed: {e}"

    def walk(o):
        if isinstance(o, str):
            names.add(o)
        elif isinstance(o, dict):
            for k, v in o.items():
                names.add(k)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(raw)
    return names, "ok"


def main(argv):
    src = argv[1]
    idx = argv[2] if len(argv) > 2 else None
    root = ET.parse(src).getroot()

    icons, icon_types = [], []
    imgs, embeds = [], []
    fonts, colors, sizes = set(), set(), {}
    emoji_hits = []
    over_safe = []
    texts = []

    for e in root.iter():
        t = tag(e)
        if t == "icon":
            v = e.get("iconType") or ""
            icon_types.append(v)
        elif t == "img":
            imgs.append(e.get("src") or "")
        elif t == "embed":
            x, y = float(e.get("topLeftX", 0)), float(e.get("topLeftY", 0))
            w, h = float(e.get("width", 0)), float(e.get("height", 0))
            embeds.append((x, y, w, h, y + h))
        elif t == "content":
            ff = e.get("fontFamily")
            if ff:
                fonts.add(ff)
            c = e.get("color")
            if c:
                colors.add(c)
            fs = e.get("fontSize")
            if fs:
                sizes[fs] = sizes.get(fs, 0) + 1
            txt = "".join(e.itertext())
            if EMOJI_RE.search(txt):
                emoji_hits.append(txt[:40])
        elif t == "span":
            ff = e.get("fontFamily")
            if ff:
                fonts.add(ff)
            c = e.get("color")
            if c:
                colors.add(c)
            fs = e.get("fontSize")
            if fs:
                sizes[fs] = sizes.get(fs, 0) + 1
        elif t == "shape" and e.get("type") == "text":
            x, y = float(e.get("topLeftX", 0)), float(e.get("topLeftY", 0))
            w, h = float(e.get("width", 0)), float(e.get("height", 0))
            txt = "".join(e.itertext()).strip()
            texts.append((round(x, 1), round(y, 1), round(w, 1), round(h, 1), txt[:28]))
            if y >= SAFE_T and (x < SAFE_L - 1 or x + w > SAFE_R + 1 or y + h > SAFE_B + 1):
                over_safe.append((round(x, 1), round(y, 1), round(w, 1), round(h, 1), txt[:28]))

    print("== icons ==", len(icon_types))
    if idx:
        names, note = load_icon_names(idx)
        print("  iconpark index:", note, "names:", len(names))
        if names:
            bad = [v for v in icon_types if v not in names]
            leaf = {n.rsplit("/", 1)[-1] for n in names}
            bad2 = [v for v in bad if v.rsplit("/", 1)[-1] not in leaf]
            print("  unknown iconType:", bad2 if bad2 else "none")
    print("== emoji hits ==", emoji_hits if emoji_hits else "none")
    print("== fonts ==", sorted(fonts), "| not in allowlist:", sorted(fonts - ALLOWED_FONTS))
    print("== colors ==", len(colors))
    for c in sorted(colors):
        print("   ", c)
    print("== font sizes ==", dict(sorted(sizes.items(), key=lambda kv: -kv[1])))
    print("== imgs ==", len(imgs))
    for s in imgs:
        print("   ", s[:60])
    print("== embeds ==", len(embeds))
    for x, y, w, h, bot in embeds:
        flag = "  <<< 底缘越过 y=476" if bot > 476 else ""
        print(f"    x={x} y={y} w={w} h={h} bottom={bot}{flag}")
    print("== text shapes ==", len(texts))
    for r in texts:
        print("   ", r)
    print("== text outside safe area ==", len(over_safe))
    for r in over_safe:
        print("   ", r)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
