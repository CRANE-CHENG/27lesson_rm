import sys, zipfile, re, os
from xml.etree import ElementTree as ET

path = sys.argv[1]
z = zipfile.ZipFile(path)
names = [n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)]
names.sort(key=lambda n: int(re.search(r'(\d+)', os.path.basename(n)).group(1)))
ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}

print("TOTAL SLIDES:", len(names))
print("=" * 70)
for n in names:
    root = ET.fromstring(z.read(n))
    idx = int(re.search(r'(\d+)', os.path.basename(n)).group(1))
    print(f"\n########## SLIDE {idx} ({n}) ##########")
    # text runs grouped by paragraph
    for sp in root.iter():
        pass
    txts = []
    for para in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}p'):
        line = ''.join(t.text or '' for t in para.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t'))
        txts.append(line)
    for t in txts:
        if t.strip():
            print("  |", t)
    # shape count / picture count
    spcnt = len(list(root.iter('{http://schemas.openxmlformats.org/presentationml/2006/main}sp')))
    piccnt = len(list(root.iter('{http://schemas.openxmlformats.org/presentationml/2006/main}pic')))
    print(f"  [shapes={spcnt} pics={piccnt}]")
