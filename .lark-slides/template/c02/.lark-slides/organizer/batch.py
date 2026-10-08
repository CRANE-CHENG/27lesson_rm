#!/usr/bin/env python3
"""batch.py — 一次审多页：切页 + 抽关键字段（角标/标题/页眉几何/字体/色/安全区）+ 跑 template_lint_all 紧凑摘要。

用法: python batch.py <round_tag>
页表写在 JOBS 里，按 page-plan.md 的「页型策略」列填。
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SKILL = r"C:\Users\访鹤愚者\AppData\Local\Doubao\User Data\Default\.doubao\agent_mode\workspace\.skills\ppt"
SRC = Path(r"D:\桌面\培训\.lark-slides\template\c02")
BASE = Path(__file__).resolve().parent

# (page_num, slide_id, page_role, source_kind, source_file, expected_badge, fname_override)
JOBS = [
    (15, "pfA", "active_rebuild", "skeleton", "slide-16", "03", None),
    (16, "pfm", "fixed_template", "source",   "slide-04", None, None),
    (17, "pfX", "active_rebuild", "skeleton", "slide-16", "04", None),
    (18, "pfl", "active_rebuild", "skeleton", "slide-16", "04", None),
    (19, "pfr", "active_rebuild", "skeleton", "slide-16", "04", None),
    (20, "pfs", "active_rebuild", "skeleton", "slide-16", "04", "slide-p20.xml"),
    (21, "pfo", "active_rebuild", "skeleton", "slide-16", "04", None),
    (22, "pfv", "active_rebuild", "skeleton", "slide-16", "04", None),
    (23, "pfS", "active_rebuild", "skeleton", "slide-16", "04", "slide-p23.xml"),
    (24, "pfJ", "fixed_template", "source",   "slide-29", None, None),
]
ALLOWED_FONTS = {"思源黑体", "Consolas", "锐字真言体免费商用", "思源宋体"}
SAFE_L, SAFE_T, SAFE_R, SAFE_B = 62.0, 100.0, 898.0, 478.0


def tag(e):
    return e.tag.split("}")[-1]


def src_path(kind, f):
    if kind == "skeleton":
        return SRC / "manifest" / "content-skeletons" / f"{f}.content-skeleton.xml"
    return SRC / "source-slides" / f"{f}.xml"


def brief(e, n=34):
    return " ".join("".join(e.itertext()).split())[:n]


def run_job(round_dir: Path, job):
    num, sid, role, kind, sf, exp, fname = job
    full = round_dir / "full.xml"
    out = round_dir / (fname or f"slide-{sid}.xml")
    subprocess.run([sys.executable, str(BASE / "slice.py"), str(full), sid, str(out)],
                   capture_output=True, text=True, encoding="utf-8")
    if not out.exists():
        print(f"=== P{num} {sid}: SLICE FAILED")
        return
    root = ET.parse(str(out)).getroot()
    data = [c for c in root if tag(c) == "data"][0]
    kids = list(data)

    badge = bgeo = title = tgeo = hdr = hgeo = ""
    fonts, colors, safe_bad, imgs, embeds = set(), set(), [], 0, 0
    for e in data.iter():
        t = tag(e)
        if t == "img":
            imgs += 1
        elif t == "embed":
            embeds += 1
        elif t in ("content", "span"):
            if e.get("fontFamily"):
                fonts.add(e.get("fontFamily"))
            if e.get("color"):
                colors.add(e.get("color"))
        if t == "shape" and e.get("type") == "text":
            txt = brief(e, 30)
            x, y = float(e.get("topLeftX", 0)), float(e.get("topLeftY", 0))
            w, h = float(e.get("width", 0)), float(e.get("height", 0))
            fs = 0.0
            for sp in e.iter():
                if tag(sp) == "span" and sp.get("fontSize"):
                    fs = max(fs, float(sp.get("fontSize")))
            geo = f"({x:.1f},{y:.1f},{w:.1f}x{h:.1f})"
            if re.fullmatch(r"\d{1,2}", txt) and fs >= 30:
                badge, bgeo = txt, geo
            elif abs(y - 33.1025) < 1 and w > 100:
                title, tgeo = txt, geo
            elif y < 100 and y > 40 and x > 600:
                hdr, hgeo = txt, geo
            if y >= SAFE_T and (x < SAFE_L - 1 or x + w > SAFE_R + 1 or y + h > SAFE_B + 1):
                safe_bad.append(f"{txt}|{geo}")

    p = subprocess.run([sys.executable, SKILL + r"\scripts\template_lint_all.py",
                        "--authored", str(out), "--source", str(src_path(kind, sf)),
                        "--skill-root", SKILL, "--page-role", role],
                       capture_output=True, text=True, encoding="utf-8")
    try:
        res = json.loads(p.stdout or "")
    except Exception:
        print(f"=== P{num} {sid} {role}: lint parse FAIL")
        print((p.stdout or "")[:400], (p.stderr or "")[:300])
        return
    s = res.get("summary") or {}
    print(f"=== P{num} {sid} {role} elems={len(kids)}")
    flag = ""
    if exp and badge != exp:
        flag = f"   <<< 角标应为 {exp}（本章节号）"
    print(f"  badge={badge!r}{bgeo}  {flag}")
    print(f"  title={title[:30]!r} {tgeo}")
    print(f"  header={hdr!r} {hgeo}")
    print(f"  fonts={sorted(fonts)}  bad_fonts={sorted(fonts - ALLOWED_FONTS)}")
    print(f"  colors({len(colors)})={sorted(colors)}")
    print(f"  imgs={imgs} embeds={embeds} safe_violations={len(safe_bad)} {safe_bad[:3]}")
    print(f"  lint errors={s.get('xml_lint_errors')} contrast_blocking={s.get('contrast_blocking')} "
          f"placeholder_warn={s.get('placeholder_warn_count')} "
          f"ovf_covers_below={s.get('overflow_covers_below_fail_count')} "
          f"wrap_warn={s.get('unexpected_wrapping_warn_count')} sparsity_fail={s.get('sparsity_fail_count')}")
    rt = s.get("refine_triggers") or {}
    if role == "active_rebuild":
        print(f"  refine: should_refine={rt.get('should_refine')} hit={rt.get('hit_count')} {rt.get('summary')}")
    xl = (res.get("checks") or {}).get("xml_lint") or {}
    raw = xl.get("raw") or {}
    for sl in raw.get("slides") or []:
        for e in sl.get("errors") or []:
            print(f"    ERR {e.get('code')} {e.get('elements') or e.get('element_ids')} :: {str(e.get('message'))[:120]}")
        for e in sl.get("warnings") or []:
            print(f"    WARN {e.get('code')} {e.get('elements') or e.get('element_ids')} :: {str(e.get('message'))[:120]}")
    for nm in ("overflow_covers_below", "unexpected_wrapping", "color_contrast", "placeholder_diff"):
        c = (res.get("checks") or {}).get(nm) or {}
        iss = c.get("issues") or []
        if iss:
            print(f"    {nm}: {json.dumps(iss, ensure_ascii=False)[:400]}")


def main(argv):
    rd = BASE / f"current-round-{argv[1]}"
    for job in JOBS:
        run_job(rd, job)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
