#!/usr/bin/env python3
"""cmp.py — 对比 source 页与 authored 页的元素结构（按位置对齐，因为服务端会重分配 id）。

用法:
    python cmp.py <source.xml> <authored.xml> [--text-ok]

输出:
    - 元素计数
    - 逐位置的几何 / 样式 / 子结构差异（MUTATED-*）
    - 文本差异（TEXTDIFF，允许，仅列出）
"""
import sys
import xml.etree.ElementTree as ET

NS = "https://www.larkoffice.com/sml/2.0"
TAGS = ("shape", "line", "polyline", "img", "icon", "table", "chart", "embed")


def elements(path):
    root = ET.parse(path).getroot()
    data = root.find("{%s}data" % NS)
    out = []
    if data is None:
        return out
    for el in list(data):
        tag = el.tag.rsplit("}", 1)[-1]
        if tag not in TAGS:
            continue
        out.append(el)
    return out


def texts(el):
    res = []
    for c in el.iter():
        if c.tag.rsplit("}", 1)[-1] == "content":
            s = "".join(c.itertext()).strip()
            res.append(s)
    return res


def content_sig(el):
    """content 子树里每个节点的 (tag, 排序属性, 文本)，能捕捉 span 上的 color/fontSize 变化。"""
    out = []
    for c in el.iter():
        tag = c.tag.rsplit("}", 1)[-1]
        if tag in ("content", "p", "span", "strong", "em", "u", "del", "br", "li", "ul", "ol"):
            attrs = tuple(sorted(c.attrib.items()))
            txt = (c.text or "").strip()
            out.append((tag, attrs, txt))
    return out


def geom(el):
    keys = ("type", "topLeftX", "topLeftY", "width", "height", "rotation", "flipX", "flipY",
            "presetHandlers", "path", "src", "startX", "startY", "endX", "endY")
    return {k: el.get(k) for k in keys if el.get(k) is not None}


def style(el):
    res = []
    for f in el.iter():
        tag = f.tag.rsplit("}", 1)[-1]
        if tag in ("fillColor", "border"):
            res.append((tag, {k: v for k, v in f.attrib.items()}))
    return res


def children(el):
    return [c.tag.rsplit("}", 1)[-1] for c in el]


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def main(argv):
    src, auth = argv[1], argv[2]
    s, a = elements(src), elements(auth)
    print(f"source elements: {len(s)}   authored elements: {len(a)}")
    if len(s) != len(a):
        print("!! 元素数量不同 —— 需要人工判断")
    for i in range(min(len(s), len(a))):
        se, ae = s[i], a[i]
        sid, aid = se.get("id"), ae.get("id")
        gs, ga = geom(se), geom(ae)
        diffs = []
        for k in set(gs) | set(ga):
            vs, va = gs.get(k), ga.get(k)
            if vs == va:
                continue
            ns, na = num(vs), num(va)
            if ns is not None and na is not None and abs(ns - na) < 0.01:
                continue
            diffs.append(f"{k}: {vs} -> {va}")
        if diffs:
            print(f"\n[{i}] MUTATED-GEOM {sid}->{aid}: " + "; ".join(diffs))
        ss, sa = style(se), style(ae)
        if ss != sa:
            print(f"\n[{i}] MUTATED-STYLE {sid}->{aid}:\n  source  ={ss}\n  authored={sa}")
        cs, ca = children(se), children(ae)
        if cs != ca:
            print(f"\n[{i}] CHILD-TAGS {sid}->{aid}: source={cs} authored={ca}")
        ts, ta = texts(se), texts(ae)
        if ts != ta:
            print(f"\n[{i}] TEXTDIFF {sid}->{aid}:\n  source  ={ts}\n  authored={ta}")
        cs, ca = content_sig(se), content_sig(ae)
        if cs != ca:
            print(f"\n[{i}] CONTENT-STYLE {sid}->{aid}:")
            for x, y in zip(cs, ca):
                if x != y:
                    print(f"     source  ={x}\n     authored={y}")
            if len(cs) != len(ca):
                print(f"     !! node count source={len(cs)} authored={len(ca)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
