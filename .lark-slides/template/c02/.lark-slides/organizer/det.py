#!/usr/bin/env python3
"""det.py — 打印某页 lint 错误/警告明细（元素 id + 度量值）。

用法: python det.py <new_dir> <page_num> [code_keyword]
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SKILL = r"C:\Users\访鹤愚者\AppData\Local\Doubao\User Data\Default\.doubao\agent_mode\workspace\.skills\ppt"
SRC = Path(r"D:\桌面\培训\.lark-slides\template\c02")
FIXED = {1, 2, 3, 4, 8, 12, 16, 24}


def main(argv):
    nd = Path(argv[1])
    num = int(argv[2])
    kw = argv[3] if len(argv) > 3 else ""
    fn = argv[4] if len(argv) > 4 else f"new-p{num:02d}.xml"
    f = nd / fn
    role = "fixed_template" if num in FIXED else "active_rebuild"
    if role == "active_rebuild":
        src = SRC / "manifest" / "content-skeletons" / "slide-16.content-skeleton.xml"
    elif num == 24:
        src = SRC / "source-slides" / "slide-29.xml"
    else:
        src = SRC / "source-slides" / "slide-04.xml"
    q = subprocess.run([sys.executable, SKILL + r"\scripts\template_lint_all.py",
                        "--authored", str(f), "--source", str(src),
                        "--skill-root", SKILL, "--page-role", role],
                       capture_output=True, text=True, encoding="utf-8")
    res = json.loads(q.stdout or "")
    raw = ((res.get("checks") or {}).get("xml_lint") or {}).get("raw") or {}
    n = 0
    for sl in raw.get("slides") or []:
        for lvl in ("errors", "warnings", "infos"):
            for it in sl.get(lvl) or []:
                code = it.get("code", "")
                if kw and kw not in code:
                    continue
                n += 1
                keep = {k: v for k, v in it.items()
                        if k in ("code", "severity", "message", "element_ids", "elements",
                                 "measurement", "target", "related_objects", "path", "attrs")}
                print(f"  [{lvl}] " + json.dumps(keep, ensure_ascii=False)[:500])
    print(f"total matched {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
