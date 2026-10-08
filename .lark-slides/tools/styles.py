import sys
from xml.etree import ElementTree as ET
NS = 'https://www.larkoffice.com/sml/2.0'
for p in sys.argv[1:]:
    print('==== %s ====' % p.split('\\')[-1])
    root = ET.fromstring(open(p, encoding='utf-8').read())
    data = root.find('{%s}data' % NS)
    for el in list(data):
        if el.tag.split('}')[1] not in ('shape', 'table', 'img'):
            continue
        cont = el.find('{%s}content' % NS)
        if cont is None:
            continue
        raw = ET.tostring(cont, encoding='unicode')
        if len(raw.strip()) < 1:
            continue
        if not ''.join(cont.itertext()).strip():
            continue
        ctag = raw.split('>')[0] + '>'
        spans = []
        for sp in cont.iter('{%s}span' % NS):
            a = sp.attrib
            spans.append('%s|%s|%s|bold=%s' % (''.join(sp.itertext())[:20], a.get('fontSize'), a.get('fontFamily'), a.get('bold')))
        print('  ', el.attrib.get('id'), el.attrib.get('type'), (el.attrib.get('topLeftX'), el.attrib.get('topLeftY')), (el.attrib.get('width'), el.attrib.get('height')))
        print('     C:', ctag)
        for s in spans[:6]:
            print('     S:', s)
