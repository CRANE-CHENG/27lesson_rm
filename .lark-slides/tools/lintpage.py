"""Compact wrapper around template_lint_all.py.

usage: python lintpage.py <nn> <fixed_template|active_rebuild> [srcdir]
Writes lint/slide-<nn>.json and prints a compact summary.
"""
import json
import os
import subprocess
import sys

SKILL = r"C:\Users\访鹤愚者\AppData\Local\Doubao\User Data\Default\.doubao\agent_mode\workspace\.skills\ppt"
WORK = os.environ.get("LARK_WORK") or r"D:\桌面\培训\.lark-slides\template\c02"

nn = sys.argv[1]
role = sys.argv[2]
src = sys.argv[3] if len(sys.argv) > 3 else "source-slides/slide-%s.xml" % nn

authored = os.path.join(WORK, "authoring", "slide-%s.xml" % nn)
out = os.path.join(WORK, "lint", "slide-%s.json" % nn)
cmd = [sys.executable, os.path.join(SKILL, "scripts", "template_lint_all.py"),
       "--authored", authored,
       "--source", os.path.join(WORK, src.replace("/", os.sep)),
       "--skill-root", SKILL,
       "--page-role", role]
p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
raw = p.stdout or ""
try:
    data = json.loads(raw)
except Exception:
    print("PARSE FAIL", raw[:800], p.stderr[:800])
    sys.exit(1)
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

s = data.get("summary", {})
print("LINT-ONLY %s %s status=%s block=%s" % (nn, role, data.get("status"), data.get("block_reasons")))
print("  counts xml_err=%s contrast=%s placeholder=%s overflow=%s wrap=%s sparsity=%s" % (
    s.get("xml_lint_errors"), s.get("contrast_blocking"), s.get("placeholder_warn_count"),
    s.get("overflow_covers_below_fail_count"), s.get("unexpected_wrapping_warn_count"),
    s.get("sparsity_fail_count")))
checks = data.get("checks", {})
raw_lint = checks.get("xml_lint", {}).get("raw", {})
GEO = {"shape_out_of_canvas", "bbox_overlap", "image_covers_text", "img_out_of_canvas",
       "text_overflows_container", "shape_overlaps_text"}
other = []
for sl in raw_lint.get("slides", []):
    for e in sl.get("errors", []):
        if e["code"] not in GEO:
            other.append((e["code"], e.get("element_ids")))
if other:
    print("  NON-GEO:", other[:8])
for name in ("color_contrast", "placeholder", "text_overflow_covers_below", "sparsity", "template_copy_overfit"):
    c = checks.get(name) or {}
    for i in c.get("issues", [])[:3]:
        print("  CHK %s %s" % (name, i.get("elements")))
