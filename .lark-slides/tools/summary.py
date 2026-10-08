import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "final.xml"
x = open(path, encoding="utf-8").read()
ids = re.findall(r'<slide[^>]*\bid="([^"]+)"', x)
print("slides:", len(re.findall(r"<slide[ >]", x)))
print("ids:", ids)
for i, m in enumerate(re.finditer(r"<slide\b[^>]*>(.*?)</slide>", x, re.S), 1):
    body = m.group(1)
    texts = re.findall(r">([^<>]{2,40})</span>", body)
    texts = [t for t in texts if t.strip() and t.strip() != " "]
    print(i, "|", " / ".join(texts[:6])[:170])
