"""In-place page update with reliable JSON reading.

usage: python apply_update.py <workdir> <deck> <nn>:<slide_id> [<nn>:<slide_id> ...]
Prints one compact line per page: ok=..., or the lint error codes when blocked.
"""
import json
import os
import subprocess
import sys
import time

work = sys.argv[1]
deck = sys.argv[2]
no_lint = "--no-lint" in sys.argv
os.chdir(work)

for arg in [a for a in sys.argv[3:] if a != "--no-lint"]:
    nn, sid = arg.split(":")
    cmd = ["lark-cli", "slides", "+update-slide",
           "--presentation", deck, "--slide-id", sid,
           "--content", "@authoring/slide-%s.xml" % nn]
    if no_lint:
        cmd.append("--no-lint")
    for attempt in (1, 2):
        p = subprocess.run(cmd, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        d = None
        for raw in (p.stdout, p.stderr):
            if not raw or not raw.strip():
                continue
            try:
                d = json.loads(raw)
                break
            except Exception:
                continue
        if d is None:
            print("%s %s UNPARSED rc=%s out=%r err=%r" % (nn, sid, p.returncode,
                                                          p.stdout[:200], p.stderr[:300]))
            break
        if d.get("ok"):
            print("%s %s ok=true" % (nn, sid))
            break
        err = d.get("error") or {}
        msg = err.get("message") or ""
        codes = {}
        summary = {}
        try:
            rep = json.loads(msg)
            summary = rep.get("summary", {})
            for sl in rep.get("slides", []):
                for e in sl.get("errors", []):
                    codes[e["code"]] = codes.get(e["code"], 0) + 1
        except Exception:
            pass
        print("%s %s ok=false code=%s errors=%s attempt=%s %s"
              % (nn, sid, err.get("code"), summary.get("error_count"), attempt, codes))
        if err.get("code") != 4000153:
            break
        time.sleep(1.5)
