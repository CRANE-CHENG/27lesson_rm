#!/usr/bin/env python3
"""mk_p5.py — 生成 P5(slide_id=pfd) 的修订版 XML。

输入: <server slide xml>  输出: <new slide xml>

改动:
  FIX-1  角标 bMO: "05" -> "01"（模板约定角标=章节号；slide-05/06/07=01, slide-16..28=04 可证）
  FIX-2  页眉文字 bMT: 几何还原模板 beG（705.6155118110237, 54.487716535433066,
         548.2546456692913 x 21.560551181102362），去掉 wrap="false"
         —— 原 (y=48, w=160, h=32) 触发 text_may_overflow_shape(估算175.4px > 可用145.6px)
  REFINE-1 左栏三条改为编号条目：新增 3 个 20x20 深蓝编号方块(1./2./3.，新元素不写 id)，
           左栏文本右移到 x=90.42/宽 402（右边缘仍 492.42），标题字号 18 -> 20
"""
from __future__ import annotations

import sys
import xml.etree.ElementTree as ET

NS = "https://www.larkoffice.com/sml/2.0"
ET.register_namespace("", NS)


def q(t):
    return f"{{{NS}}}{t}"


def find_data(root):
    for e in root:
        if e.tag == q("data"):
            return e
    raise SystemExit("no data")


def by_id(data, eid):
    for e in data.iter():
        if e.get("id") == eid:
            return e
    raise SystemExit(f"missing id {eid}")


def set_span_text(shape, txt):
    n = 0
    for sp in shape.iter():
        if sp.tag == q("span"):
            sp.text = txt
            n += 1
    for p in shape.iter():
        if p.tag == q("p") and len(p) == 0:
            p.text = txt
    return n


def mk_square(num, y):
    sh = ET.Element(q("shape"))
    sh.set("width", "20")
    sh.set("height", "20")
    sh.set("topLeftX", "62.42")
    sh.set("topLeftY", str(y))
    sh.set("presetHandlers", "0")
    sh.set("type", "rect")
    fill = ET.SubElement(sh, q("fill"))
    fc = ET.SubElement(fill, q("fillColor"))
    fc.set("color", "rgba(3, 72, 149, 1)")
    c = ET.SubElement(sh, q("content"))
    for k, v in (("paddingTop", "0"), ("paddingBottom", "0"), ("paddingLeft", "0"),
                 ("paddingRight", "0"), ("fontSize", "12"), ("fontFamily", "思源黑体"),
                 ("color", "rgba(255, 255, 255, 1)"), ("bold", "true"),
                 ("lineSpacing", "multiple:1.2"), ("textAlign", "center"),
                 ("verticalAlign", "middle")):
        c.set(k, v)
    p = ET.SubElement(c, q("p"))
    p.set("textAlign", "center")
    sp = ET.SubElement(p, q("span"))
    sp.set("color", "rgba(255, 255, 255, 1)")
    sp.set("fontSize", "12")
    sp.set("fontFamily", "思源黑体")
    sp.set("bold", "true")
    sp.text = f"{num}."
    return sh


def main(argv):
    src, dst = argv[1], argv[2]
    tree = ET.parse(src)
    root = tree.getroot()
    data = find_data(root)

    # FIX-1 角标 = 章节号
    badge = by_id(data, "bMO")
    set_span_text(badge, "01")

    # FIX-2 页眉文字几何还原模板 beG
    hdr = by_id(data, "bMT")
    hdr.set("width", "548.2546456692913")
    hdr.set("height", "21.560551181102362")
    hdr.set("topLeftY", "54.487716535433066")
    for e in hdr.iter():
        if e.tag == q("content"):
            e.attrib.pop("wrap", None)

    # REFINE-1 左栏编号化
    blocks = [("bMY", 1, 128), ("bMw", 2, 198), ("bMz", 3, 268)]
    for bid, num, sq_y in blocks:
        blk = by_id(data, bid)
        blk.set("topLeftX", "90.42")
        blk.set("width", "402")
        for sp in blk.iter():
            if sp.tag == q("span") and (sp.get("color") == "rgba(3, 72, 149, 1)"):
                sp.set("fontSize", "20")
                break
        idx = list(data).index(blk)
        data.insert(idx, mk_square(num, sq_y))

    tree.write(dst, encoding="utf-8", xml_declaration=False)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
