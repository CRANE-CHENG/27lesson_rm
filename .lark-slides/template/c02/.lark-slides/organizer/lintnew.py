#!/usr/bin/env python3
"""lintnew.py — 对修订版 new-p<NN>.xml 快速跑 template_lint_all，只打印错误码集合与关键计数。

用法: python lintnew.py <new_dir> <page_num> [<page_num> ...]
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
    for p in argv[2:]:
        num = int(p)
        f = nd / f"new-p{num:02d}.xml"
        if not f.exists():
            print(f"p{num}: MISSING {f.name}")
            continue
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
        try:
            res = json.loads(q.stdout or "")
        except Exception:
            print(f"p{num}: LINT FAIL {(q.stdout or '')[:200]} {(q.stderr or '')[:200]}")
            continue
        s = res.get("summary") or {}
        raw = ((res.get("checks") or {}).get("xml_lint") or {}).get("raw") or {}
        codes = {}
        for sl in raw.get("slides") or []:
            for e in sl.get("errors") or []:
                codes[e.get("code")] = codes.get(e.get("code"), 0) + 1
        rt = s.get("refine_triggers") or {}
        extra = ""
        if role == "active_rebuild":
            extra = (f" total={s.get('total_elements')} visual={s.get('visual_elements')}"
                     f" should_refine={rt.get('should_refine')} hit={rt.get('hit_count')}")
        print(f"p{num}: status={res.get('status')} errs={s.get('xml_lint_errors')} codes={codes}"
              f" wrap_warn={s.get('unexpected_wrapping_warn_count')}"
              f" ovf_below={s.get('overflow_covers_below_fail_count')}{extra}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
