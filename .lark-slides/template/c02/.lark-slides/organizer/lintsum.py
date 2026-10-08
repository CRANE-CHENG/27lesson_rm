#!/usr/bin/env python3
"""lintsum.py — 对单个 slide XML 跑 xml_lint，并紧凑列出各条 issue。

用法: python lintsum.py <slide.xml> [source.xml]
"""
import sys
import collections

SKILL = r"C:\Users\访鹤愚者\AppData\Local\Doubao\User Data\Default\.doubao\agent_mode\workspace\.skills\ppt\scripts"
sys.path.insert(0, SKILL)

from xml_lint import lint_xml  # noqa: E402


def main(argv):
    path = argv[1]
    src = argv[2] if len(argv) > 2 else None
    xml = open(path, encoding="utf-8").read()
    res = lint_xml(xml, source_path=src)
    slides = res.get("slides") or []
    for s in slides:
        print(f"slide {s.get('slide_number')} status={s.get('status')} elements={s.get('element_count')}")
        for level in ("errors", "warnings", "infos"):
            items = s.get(level) or []
            if not items:
                continue
            print(f"  -- {level}: {len(items)}")
            counter = collections.Counter()
            for it in items:
                code = it.get("code")
                counter[code] += 1
                els = it.get("elements") or it.get("element_ids") or []
                print(f"    [{level[:-1]}] {code} {els} :: {it.get('message')}")
            print("  summary:", dict(counter))
    print("document:", {k: len(v) for k, v in (res.get("document") or {}).items()})
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
