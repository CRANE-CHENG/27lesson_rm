"""Content-preservation check: original deck vs restyled deck, per slide.

Two independent tests per slide:
  1. character multiset diff  (catches lost or duplicated words)
  2. unit check: every text unit of the original must still appear in the new slide
"""
import sys, re, collections
from pptx import Presentation

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

STRIP = re.compile(r'[\s\u200b\u3000]')
MARKERS = '①②③④⑤⑥⑦⑧⑨⑩'


def norm(s):
    s = s.replace('\u200b', '')
    for m in MARKERS:
        s = s.replace(m, '')
    return STRIP.sub('', s)


def cells(slide):
    out = []
    for sh in slide.shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                t = ''.join(r.text for r in p.runs)
                if t.strip():
                    out.append(t)
        if sh.has_table:
            for row in sh.table.rows:
                for c in row.cells:
                    if c.text.strip():
                        out.append(c.text)
    return out


def unit_key(s):
    s = norm(s)
    s = re.sub(r'^[0-9]{1,2}[.、)）]?', '', s)
    return s


if __name__ == '__main__':
    orig, new = sys.argv[1], sys.argv[2]
    po, pn = Presentation(orig), Presentation(new)
    assert len(po.slides) == len(pn.slides), 'slide count differs'
    problems = 0
    for i in range(len(po.slides)):
        ca = collections.Counter(norm(''.join(cells(po.slides[i]))))
        cb = collections.Counter(norm(''.join(cells(pn.slides[i]))))
        lost = ca - cb
        gained = cb - ca
        whole_b = norm(''.join(cells(pn.slides[i])))
        missing_units = []
        for u in cells(po.slides[i]):
            k = unit_key(u)
            if len(k) >= 3 and k not in whole_b:
                missing_units.append(u.strip()[:90])
        if lost or missing_units:
            problems += 1
            print('--- p%d' % (i + 1))
            if lost:
                s = ''.join(k * v for k, v in lost.items())
                print('    char diff  lost=%r' % s[:160])
            if gained:
                s = ''.join(k * v for k, v in gained.items())
                print('    char diff  new =%r' % s[:160])
            for m in missing_units[:8]:
                print('    unit lost : %s' % m)
    print('%s: %d problematic slides of %d' % (new, problems, len(po.slides)))
