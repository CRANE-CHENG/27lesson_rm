#!/usr/bin/env python3
"""tla.py — 跑 template_lint_all.py 并只打印紧凑摘要（避免超大 stdout 污染上下文）。

用法:
    python tla.py <authored.xml> <source.xml> <page-role>
"""
import json
import subprocess
import sys

SKILL = r"C:\Users\访鹤愚者\AppData\Local\Doubao\User Data\Default\.doubao\agent_mode\workspace\.skills\ppt"


def main(argv):
    authored, source, role = argv[1], argv[2], argv[3]
    cmd = [
        sys.executable, SKILL + r"\scripts\template_lint_all.py",
        "--authored", authored,
        "--source", source,
        "--skill-root", SKILL,
        "--page-role", role,
    ]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    out = p.stdout or ""
    try:
        res = json.loads(out)
    except Exception:
        print("STDOUT(non-json):", out[:3000])
        print("STDERR:", (p.stderr or "")[:2000])
        return 1

    print("status:", res.get("status"))
    print("block_reasons:", res.get("block_reasons"))
    s = res.get("summary") or {}
    for k in ("xml_lint_errors", "contrast_blocking", "placeholder_warn_count",
              "overflow_covers_below_fail_count", "unexpected_wrapping_warn_count",
              "sparsity_fail_count", "page_role", "total_elements", "text_elements",
              "visual_elements", "total_text_chars", "max_font_size"):
        print(f"  {k}: {s.get(k)}")
    print("  refine_triggers:", json.dumps(s.get("refine_triggers"), ensure_ascii=False))

    checks = res.get("checks") or {}
    for name, c in checks.items():
        if name == "xml_lint":
            raw = c.get("raw") or {}
            codes = {}
            for sl in raw.get("slides") or []:
                for e in sl.get("errors") or []:
                    codes[e.get("code")] = codes.get(e.get("code"), 0) + 1
                for e in sl.get("warnings") or []:
                    codes["warn:" + str(e.get("code"))] = codes.get("warn:" + str(e.get("code")), 0) + 1
            print(f"  xml_lint: status={c.get('status')} errors={c.get('error_count')} codes={codes}")
            for sl in raw.get("slides") or []:
                for e in sl.get("errors") or []:
                    print(f"      ERR {e.get('code')} {e.get('elements') or e.get('element_ids')} :: {e.get('message')}")
                for e in sl.get("warnings") or []:
                    print(f"      WARN {e.get('code')} {e.get('elements') or e.get('element_ids')} :: {e.get('message')}")
            continue
        print(f"  {name}: {json.dumps({k: v for k, v in c.items() if k not in ('raw',)}, ensure_ascii=False)[:1500]}")

    pw = res.get("placeholder_details") or res.get("placeholders") or []
    if pw:
        print("placeholder_details:", json.dumps(pw, ensure_ascii=False)[:1500])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
