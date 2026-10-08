import sys, re
from xml.etree import ElementTree as ET
NS = 'https://www.larkoffice.com/sml/2.0'
p = sys.argv[1]
src = open(p, encoding='utf-8').read()
root = ET.fromstring(src)
data = root.find('{%s}data' % NS)
print('ROOT id=', root.get('id'))
def txt(el):
    out = []
    for pa in el.iter('{%s}p' % NS):
        out.append(''.join(pa.itertext()))
    return ' ⏎ '.join(out)
i = 0
for el in list(data):
    tag = el.tag.split('}')[1]
    a = el.attrib
    key = {k: a.get(k) for k in ('type', 'topLeftX', 'topLeftY', 'width', 'height', 'rotation', 'path', 'src', 'presetHandlers', 'flipY', 'flipX', 'id') if a.get(k) is not None}
    print(f'[{i}] {tag} {key}')
    t = txt(el).strip()
    if t:
        print('     TEXT:', t[:400])
    i += 1
