#!/usr/bin/env python3
"""slice.py — 从 full.xml 里切出指定 slide_id 的单页 XML，保留 SML 命名空间与画布尺寸。

用法:
    python slice.py <full.xml> <slide_id> <out.xml>
    python slice.py <full.xml> --list          # 列出所有 slide_id 与 element 数
"""
import sys
import xml.etree.ElementTree as ET

NS = "https://www.larkoffice.com/sml/2.0"
ET.register_namespace("", NS)


def main(argv):
    full = argv[1]
    tree = ET.parse(full)
    root = tree.getroot()
    tag_slide = "{%s}slide" % NS
    slides = [e for e in root if e.tag == tag_slide]

    if argv[2] == "--list":
        for i, s in enumerate(slides, 1):
            data = s.find("{%s}data" % NS)
            n = len(list(data)) if data is not None else 0
            print(i, s.get("id"), n)
        return 0

    sid = argv[2]
    out = argv[3]
    target = None
    for s in slides:
        if s.get("id") == sid:
            target = s
            break
    if target is None:
        print("NOT FOUND", sid)
        return 1
    new_root = ET.Element("{%s}slide" % NS)
    for k, v in target.attrib.items():
        new_root.set(k, v)
    for child in list(target):
        new_root.append(child)
    ET.ElementTree(new_root).write(out, encoding="utf-8", xml_declaration=False)
    print("OK", out, "shapes=", len(list(target.find("{%s}data" % NS))))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
