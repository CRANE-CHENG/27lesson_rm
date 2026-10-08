import sys
from xml.etree import ElementTree as ET
NS = 'https://www.larkoffice.com/sml/2.0'
DECO = {'bUs', 'bUg', 'bUG', 'bUr', 'bUx', 'bUM', 'bUS'}
for p in sys.argv[1:]:
    print('======== %s ========' % p.split('\\')[-1])
    root = ET.fromstring(open(p, encoding='utf-8').read())
    data = root.find('{%s}data' % NS)
    def txt(el):
        return ' ⏎ '.join(''.join(pa.itertext()) for pa in el.iter('{%s}p' % NS))
    for el in list(data):
        a = el.attrib
        if a.get('id') in DECO:
            continue
        tag = el.tag.split('}')[1]
        key = {k: a.get(k) for k in ('type', 'topLeftX', 'topLeftY', 'width', 'height', 'rotation', 'src', 'presetHandlers', 'flipY') if a.get(k) is not None}
        print('%s %s' % (tag, key))
        t = txt(el).strip()
        if t:
            print('    T:', t[:500])
