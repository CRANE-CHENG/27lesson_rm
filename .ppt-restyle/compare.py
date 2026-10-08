"""Build before/after comparison sheets from rendered page images."""
import sys, os
from PIL import Image, ImageDraw

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

PAIRS = [
    ('第二讲 p5  三栏讲解页', r'.ppt-restyle\view-l2\page-0005.png', r'.ppt-restyle\view-new-l2\page-0005.png'),
    ('第二讲 p10  表格页', r'.ppt-restyle\view-l2\page-0010.png', r'.ppt-restyle\view-new-l2\page-0010.png'),
    ('第三讲 p14  消抖方案表', r'.ppt-restyle\view-l3\page-0014.png', r'.ppt-restyle\view-new-l3\page-0014.png'),
    ('第四讲 p18  作业页', r'.ppt-restyle\view-l4\page-0018.png', r'.ppt-restyle\view-new-l4\page-0018.png'),
]

TW = 640
PAD, HDR, LBL = 10, 34, 22
out = sys.argv[1]
W = 2 * TW + 3 * PAD
H = HDR + len(PAIRS) * (int(TW * 720 / 1280) + LBL + PAD) + PAD
canvas = Image.new('RGB', (W, H), (245, 246, 248))
d = ImageDraw.Draw(canvas)
d.text((PAD, 10), 'BEFORE  (原始 2-5 讲)', fill=(140, 30, 30))
d.text((PAD * 2 + TW, 10), 'AFTER  (改成第一讲单栏风格)', fill=(20, 100, 50))
y = HDR
th = int(TW * 720 / 1280)
for label, a, b in PAIRS:
    for i, p in enumerate((a, b)):
        im = Image.open(p).convert('RGB').resize((TW, th), Image.LANCZOS)
        x = PAD + i * (TW + PAD)
        canvas.paste(im, (x, y))
        d.rectangle([x - 1, y - 1, x + TW, y + th], outline=(150, 150, 150))
    d.text((PAD + 2, y + th + 4), label, fill=(30, 30, 30))
    y += th + LBL + PAD
canvas.save(out)
print('-> %s (%dx%d)' % (out, W, H))
