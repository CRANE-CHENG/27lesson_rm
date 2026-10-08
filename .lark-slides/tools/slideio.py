"""Compact wrapper for lark-cli slides write commands.

usage:
  python slideio.py add <nn> [--lint]        append authoring/slide-<nn>.xml
  python slideio.py update <slide_id> <nn> [--lint]
  python slideio.py shot <slide_id> [tag]
Prints a one-block compact result.
"""
import json
import os
import re
import subprocess
import sys

WORK = os.environ.get("LARK_WORK") or r"D:\桌面\培训\.lark-slides\template\c02"
DECK = os.environ.get("LARK_DECK") or "F0JnsLJyVl4EyOdihVacpfKEnYd"
CLI = "lark-cli"


def run(args):
    p = subprocess.run([CLI] + args, cwd=WORK, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p


def summarize(text):
    """Return compact string from lark-cli stdout json, or short error digest."""
    try:
        d = json.loads(text)
    except Exception:
        return "RAW:" + text[:400]
    if d.get("ok"):
        data = d.get("data") or {}
        issues = data.get("issues")
        out = "ok=true slide_id=%s" % data.get("slide_id")
        if issues:
            out += " issues=" + json.dumps(issues, ensure_ascii=False)[:600]
        return out
    err = d.get("error") or {}
    msg = err.get("message") or ""
    out = "ok=false code=%s" % err.get("code")
    try:
        report = json.loads(msg)
        codes = {}
        for sl in report.get("slides", []):
            for e in sl.get("errors", []):
                codes.setdefault(e["code"], []).extend(e.get("element_ids", [])[:5])
        out += " err_count=%s" % report.get("summary", {}).get("error_count")
        for k, v in codes.items():
            out += "\n    ERR %s %s" % (k, v)
    except Exception:
        out += " msg=" + msg[:500]
    out += "\n    hint=" + (err.get("hint") or "")[:160]
    return out


def main():
    mode = sys.argv[1]
    if mode == "add":
        nn = sys.argv[2]
        args = ["slides", "+add-slide", "--presentation", DECK,
                "--slide", "@authoring/slide-%s.xml" % nn]
        if "--lint" not in sys.argv:
            args.append("--no-lint")
        p = run(args)
        res = summarize(p.stdout)
        if res.startswith("ok=false"):
            print("   (first-write lint guard hit, retrying)")
            p = run(args)
            res = summarize(p.stdout)
        print("add-slide %s ->" % nn, res)
    elif mode == "update":
        sid, nn = sys.argv[2], sys.argv[3]
        args = ["slides", "+update-slide", "--presentation", DECK,
                "--slide-id", sid, "--content", "@authoring/slide-%s.xml" % nn]
        if "--lint" not in sys.argv:
            args.append("--no-lint")
        p = run(args)
        res = summarize(p.stdout)
        if res.startswith("ok=false"):
            print("   (first-write lint guard hit, retrying)")
            p = run(args)
            res = summarize(p.stdout)
        print("update-slide %s ->" % sid, res)
    elif mode == "shot":
        sid = sys.argv[2]
        tag = sys.argv[3] if len(sys.argv) > 3 else sid
        p = run(["slides", "+screenshot", "--presentation", DECK,
                 "--slide-id", sid, "--output-dir", "lint/screenshots"])
        try:
            d = json.loads(p.stdout)
            for s in d["data"]["screenshots"]:
                print("shot:", s["path"])
        except Exception:
            print("shot FAIL", p.stdout[:300], p.stderr[:300])
    elif mode == "pages":
        p = run(["slides", "+xml-get", "--presentation", DECK, "--output", "final.xml"])
        print("xml-get:", p.stdout[:200])


main()
