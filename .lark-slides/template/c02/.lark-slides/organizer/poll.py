#!/usr/bin/env python3
"""poll.py — 一轮 poll：拉全稿 XML 到 current-round-<tag>/，打印 rev / 页数 / error 数 / 各页 slide_id+元素数。

用法（在 organizer 目录下）: python poll.py <tag>
"""
from __future__ import annotations

import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

PRES = "F0JnsLJyVl4EyOdihVacpfKEnYd"


def main(argv):
    tag = argv[1]
    base = Path.cwd()
    d = base / f"current-round-{tag}"
    d.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ["lark-cli", "slides", "+xml-get", "--presentation", PRES,
         "--output", "./full.xml", "--json"],
        cwd=str(d), capture_output=True, text=True,
        encoding="utf-8", errors="replace", timeout=180,
    )
    try:
        j = json.loads(r.stdout)
    except Exception:
        print("PARSE_FAIL rc=", r.returncode)
        print("STDOUT:", (r.stdout or "")[:800])
        print("STDERR:", (r.stderr or "")[:400])
        return 1
    data = j.get("data", {}) or {}
    sm = ((data.get("issues") or {}).get("summary") or {})
    print(f"rev={data.get('revision_id')} slides={sm.get('slide_count')} errs={sm.get('error_count')} warns={sm.get('warning_count')}")
    root = ET.parse(str(d / "full.xml")).getroot()
    slides = [e for e in root if e.tag.split("}")[-1] == "slide"]
    for i, s in enumerate(slides, 1):
        sid = s.get("id") or ""
        datael = [c for c in s if c.tag.split("}")[-1] == "data"]
        cnt = len(list(datael[0])) if datael else 0
        print(i, sid, cnt)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
