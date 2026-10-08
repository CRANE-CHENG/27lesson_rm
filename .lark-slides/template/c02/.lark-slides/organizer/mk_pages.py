#!/usr/bin/env python3
"""mk_pages.py — 批量生成内容页修订版 XML。

统一修复：
  FIX-1 角标 = 章节号（模板约定：内容页角标写本章节号，非页码）
  FIX-2 页眉文字几何还原（705.6155118110237, 54.487716535433066,
        548.2546456692913 x 21.560551181102362）并去掉 wrap="false"
        —— 原 (y=48, w=160, h=32) 触发 text_may_overflow_shape
按页 refine：
  l1    左栏三条要点编号化：3 个 20x20 深蓝编号方块(1./2./3.)，文本右移 x=90.42/宽 402，
        标题字号 18 -> 20
  l3    整行浅灰底块承载每一条编号步骤（page-plan L3 定义「整行 rect 承载行文字」未落地）
        + 代码框左右边距对齐内容边距（x 74.42/宽 793 -> x 62.42/宽 817.58）
  chap4 章节页标题与 P3 目录条目统一为「04数组·字符串·结构体·指针」
  e23   P23 第 04 条补回 page-plan 要求的「指定邮箱 / 附件形式」
  l2syn P10 表格下方补「语法」对照行
  l2tab P11 列宽重排 + 表体字号 16->15，消除单元格拦腰断字

命名空间说明：服务端单页 XML 有的带 xmlns、有的不带；本脚本按输入文档自身的
命名空间状态统一处理（T()），保证写回时与输入同形。

用法: python mk_pages.py <src_dir> <out_dir> [sid ...]
"""
from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = "https://www.larkoffice.com/sml/2.0"
ET.register_namespace("", NS)

JOBS = [
    ("pfA", "03", "l1", None, "p15"),
    ("pfm", None, "none", "orig-p16.xml", "p16"),
    ("pfX", "04", "l3", None, "p17"),
    ("pfl", "04", "l3", None, "p18"),
    ("pfr", "04", "l3", None, "p19"),
    ("pfs", "04", "l3", "slide-p20.xml", "p20"),
    ("pfo", "04", "l1g", None, "p21"),
    ("pfv", "04", "l3", None, "p22"),
    ("pfS", "04", "l3e23", "orig-p23.xml", "p23"),
]
HDR_W, HDR_H, HDR_Y = "548.2546456692913", "21.560551181102362", "54.487716535433066"
EDGE_L, EDGE_W = "62.42", "817.58"

NSP = True  # 输入文档是否带命名空间，main() 里设定


def T(name):
    return f"{{{NS}}}{name}" if NSP else name


def local(e):
    return e.tag.split("}")[-1]


def nocol(s):
    return (s or "").replace(" ", "")


def data_of(root):
    for e in root.iter():
        if local(e) == "data":
            return e
    raise SystemExit("no data")


def txt_of(e, n=40):
    return " ".join("".join(e.itertext()).split())[:n]


def mk_square(num, y):
    sh = ET.Element(T("shape"))
    for k, v in (("width", "20"), ("height", "20"), ("topLeftX", "62.42"),
                 ("topLeftY", str(y)), ("presetHandlers", "0"), ("type", "rect")):
        sh.set(k, v)
    fill = ET.SubElement(sh, T("fill"))
    ET.SubElement(fill, T("fillColor")).set("color", "rgba(3, 72, 149, 1)")
    c = ET.SubElement(sh, T("content"))
    for k, v in (("paddingTop", "0"), ("paddingBottom", "0"), ("paddingLeft", "0"),
                 ("paddingRight", "0"), ("fontSize", "12"), ("fontFamily", "思源黑体"),
                 ("color", "rgba(255, 255, 255, 1)"), ("bold", "true"),
                 ("lineSpacing", "multiple:1.2"), ("textAlign", "center"),
                 ("verticalAlign", "middle")):
        c.set(k, v)
    p = ET.SubElement(c, T("p"))
    p.set("textAlign", "center")
    sp = ET.SubElement(p, T("span"))
    for k, v in (("color", "rgba(255, 255, 255, 1)"), ("fontSize", "12"),
                 ("fontFamily", "思源黑体"), ("bold", "true")):
        sp.set(k, v)
    sp.text = f"{num}."
    return sh


def mk_bar(y, h=40):
    """步骤条左侧 signature 竖装饰条 4x40 主色（不承载文字，不与文字框相邻，不会触发 container/overlap 检查）。"""
    sh = ET.Element(T("shape"))
    for k, v in (("width", "4"), ("height", str(h)), ("topLeftX", "56.42"),
                 ("topLeftY", str(y)), ("presetHandlers", "0"), ("type", "rect")):
        sh.set(k, v)
    fill = ET.SubElement(sh, T("fill"))
    ET.SubElement(fill, T("fillColor")).set("color", "rgba(3, 72, 149, 1)")
    ET.SubElement(sh, T("content"))
    return sh


def mk_syntax_line():
    """P10：表格下方补语法对照行。"""
    sh = ET.Element(T("shape"))
    for k, v in (("type", "text"), ("topLeftX", "62.42"), ("topLeftY", "360"),
                 ("width", "620"), ("height", "22"), ("presetHandlers", "0")):
        sh.set(k, v)
    c = ET.SubElement(sh, T("content"))
    for k, v in (("paddingTop", "0"), ("paddingBottom", "0"), ("paddingLeft", "0"),
                 ("paddingRight", "0"), ("fontSize", "14"), ("fontFamily", "思源黑体"),
                 ("color", "rgba(31, 35, 41, 1)"), ("lineSpacing", "multiple:1.2"),
                 ("verticalAlign", "middle"), ("wrap", "false")):
        c.set(k, v)
    p = ET.SubElement(c, T("p"))
    sp1 = ET.SubElement(p, T("span"))
    for k, v in (("color", "rgba(3, 72, 149, 1)"), ("fontSize", "14"),
                 ("fontFamily", "思源黑体"), ("bold", "true")):
        sp1.set(k, v)
    sp1.text = "语法"
    sp2 = ET.SubElement(p, T("span"))
    for k, v in (("color", "rgba(86, 156, 214, 1)"), ("fontSize", "14"),
                 ("fontFamily", "Consolas")):
        sp2.set(k, v)
    sp2.text = "  for (初始化; 判断; 更新)　｜　while (判断)　｜　do { 循环体 } while (判断)"
    return sh


def fix_badge(data, badge):
    if badge is None:
        return "n/a"
    for e in data.iter():
        if local(e) == "shape" and e.get("type") == "text" and abs(float(e.get("topLeftY", 0)) - 15.769) < 1:
            old = txt_of(e)
            for sp in e.iter():
                if local(sp) == "span":
                    sp.text = badge
            return old
    return None


def fix_header(data):
    for e in data.iter():
        if local(e) == "shape" and "哈理工" in txt_of(e, 60):
            old = f"({e.get('topLeftX')},{e.get('topLeftY')},{e.get('width')}x{e.get('height')})"
            e.set("width", HDR_W)
            e.set("height", HDR_H)
            e.set("topLeftY", HDR_Y)
            for c in e.iter():
                if local(c) == "content":
                    c.attrib.pop("wrap", None)
            return old
    return None


def set_text(shape, txt):
    n = 0
    for sp in shape.iter():
        if local(sp) == "span":
            sp.text = txt
            n += 1
    return n


def refine_l1(data, gutter=False):
    blocks = []
    for e in data.iter():
        if local(e) != "shape" or e.get("type") != "text":
            continue
        if (abs(float(e.get("topLeftX", 0)) - 62.42) < 1.5
                and float(e.get("width", 0)) >= 250
                and 110 < float(e.get("topLeftY", 0)) < 300):
            blocks.append(e)
    blocks.sort(key=lambda e: float(e.get("topLeftY", 0)))
    if len(blocks) != 3:
        return f"SKIP(找到 {len(blocks)} 条左栏，期望 3)"
    for i, blk in enumerate(blocks, 1):
        if not gutter:
            blk.set("topLeftX", "90.42")
            blk.set("width", "402")
            for sp in blk.iter():
                if local(sp) == "span" and nocol(sp.get("color")) == "rgba(3,72,149,1)" and sp.get("fontSize") == "18":
                    sp.set("fontSize", "20")
                    break
        sq = mk_square(i, float(blk.get("topLeftY", 0)) + 4)
        if gutter:
            sq.set("topLeftX", "40.42")
        data.insert(list(data).index(blk), sq)
    return f"编号方块 x3 @y={[round(float(b.get('topLeftY', 0)), 1) for b in blocks]}{' (gutter x40.42)' if gutter else ''}"


def refine_l3(data):
    """步骤条左侧 signature 竖装饰条（4x40 主色）+ 代码框边距对齐内容边距。"""
    nums, bodies = [], []
    for e in data.iter():
        if local(e) != "shape" or e.get("type") != "text":
            continue
        x, y = float(e.get("topLeftX", 0)), float(e.get("topLeftY", 0))
        w = float(e.get("width", 0))
        t = txt_of(e, 8)
        if abs(x - 62.42) < 1.5 and 40 <= w <= 80 and t.isdigit():
            nums.append(e)
        elif abs(x - 128.0) < 6 and w > 600:
            bodies.append(e)
    nums.sort(key=lambda e: float(e.get("topLeftY", 0)))
    if len(nums) < 2:
        return f"SKIP(找到 {len(nums)} 个步骤编号)"
    for e in nums:
        y = float(e.get("topLeftY", 0))
        pos = list(data).index(e)
        for b in bodies:
            if abs(float(b.get("topLeftY", 0)) - y) < 2:
                pos = min(pos, list(data).index(b))
        data.insert(pos, mk_bar(y))
    fixed = ""
    for e in data.iter():
        if (local(e) == "shape" and e.get("type") == "text"
                and abs(float(e.get("topLeftX", 0)) - 74.42) < 2 and float(e.get("width", 0)) > 700):
            e.set("topLeftX", EDGE_L)
            e.set("width", EDGE_W)
            fixed = "；代码框 x74.42/w793 -> x62.42/w817.58"
    return f"步骤竖条 x{len(nums)} (4x40 @x56.42){fixed}"


def fix_chap4(data):
    """章节页大标题：改为两段，断行落在「·」处，避免自动换行把分隔符甩到行首。"""
    for e in data.iter():
        if local(e) != "shape" or "04数组" not in txt_of(e, 40):
            continue
        cont = None
        for c in e:
            if local(c) == "content":
                cont = c
        if cont is None:
            continue
        p = None
        for c in cont:
            if local(c) == "p":
                p = c
                break
        if p is None:
            continue
        spans = [s for s in p.iter() if local(s) == "span"]
        if not spans:
            continue
        tpl = spans[0]
        idx = list(cont).index(p)
        cont.remove(p)
        for k, txt in enumerate(("04 数组·字符串", "结构体·指针")):
            np = ET.Element(T("p"))
            for kk, vv in p.attrib.items():
                np.set(kk, vv)
            sp = ET.SubElement(np, T("span"))
            for kk, vv in tpl.attrib.items():
                sp.set(kk, vv)
            sp.text = txt
            cont.insert(idx + k, np)
        return "章节标题拆两段『04 数组·字符串』/『结构体·指针』"
    return "SKIP(未找到章节标题)"


def enrich_23(data):
    """P23 第 04 条正文补回 page-plan 要求的「指定邮箱 / 附件形式」。

    注意：L3 步骤行的标题段与正文段同在一个 text shape 里，只能改正文段（含「例如」），
    否则标题会被正文覆盖。来源：培训计划 md「每周考核任务 · 任务要求」。
    """
    for e in data.iter():
        if local(e) == "shape" and "第一次任务.zip" in txt_of(e, 200):
            n = 0
            for sp in e.iter():
                if local(sp) == "span" and sp.text and "例如" in sp.text:
                    sp.text = "例如：电气26-5班+李华+第一次任务.zip；以附件形式发送到指定邮箱，邮件主题同名。"
                    n += 1
            return f"第 04 条正文补『以附件形式发送到指定邮箱』(spans={n})"
    return "SKIP(未找到命名示例行)"


def refine_l2syn(data):
    tbl = None
    for e in data.iter():
        if local(e) == "table" and abs(float(e.get("height", 0)) - 244) < 2:
            tbl = e
    if tbl is None:
        return "SKIP(未找到 height=244 的对比表)"
    data.insert(list(data).index(tbl) + 1, mk_syntax_line())
    return "语法对照行 @(62.42,360,620x22)"


def refine_l2tab(data):
    tbl = None
    for e in data.iter():
        if local(e) == "table" and abs(float(e.get("height", 0)) - 188) < 2:
            tbl = e
    if tbl is None:
        return "SKIP(未找到 height=188 的对比表)"
    cols = [c for c in tbl.iter() if local(c) == "col"]
    old = [c.get("width") for c in cols]
    for c, w in zip(cols, ("100", "272", "296", "160")):
        c.set("width", w)
    n = 0
    for e in tbl.iter():
        if local(e) in ("span", "content") and e.get("fontSize") == "16":
            e.set("fontSize", "15")
            n += 1
    return f"列宽 {old} -> ['100','272','296','160']；{n} 处字号 16->15"


def main(argv):
    global NSP
    rd, od = Path(argv[1]), Path(argv[2])
    only = set(argv[3:])
    od.mkdir(exist_ok=True)
    for sid, badge, mode, fname, outname in JOBS:
        if only and sid not in only:
            continue
        src = rd / (fname or f"slide-{sid}.xml")
        tree = ET.parse(str(src))
        root = tree.getroot()
        NSP = root.tag.startswith("{")
        data = data_of(root)
        old_badge = fix_badge(data, badge)
        old_hdr = fix_header(data)
        if mode == "none":
            note = "revert to original（不做改动）"
        elif mode == "l1":
            note = refine_l1(data)
        elif mode == "l1g":
            note = refine_l1(data, gutter=True)
        elif mode == "l3":
            note = refine_l3(data)
        elif mode == "l3e23":
            note = refine_l3(data) + "；" + enrich_23(data)
        elif mode == "chap4":
            note = fix_chap4(data)
        elif mode == "l2syn":
            note = refine_l2syn(data)
        else:
            note = refine_l2tab(data)
        out = od / f"new-{outname}.xml"
        tree.write(str(out), encoding="utf-8", xml_declaration=False)
        print(f"{out.name} [{sid}] ns={NSP} badge {old_badge}->{badge} | header {old_hdr} | {mode}: {note}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
