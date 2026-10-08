import sys
from xml.etree import ElementTree as ET
NS = 'https://www.larkoffice.com/sml/2.0'
p, kw = sys.argv[1], sys.argv[2]
root = ET.fromstring(open(p, encoding='utf-8').read())
data = root.find('{%s}data' % NS)
for el in list(data):
    t = ''.join(el.itertext())
    if kw in t:
        print(ET.tostring(el, encoding='unicode')[:2500])
        print('-' * 60)
