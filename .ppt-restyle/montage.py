"""Build contact sheets (grids of page thumbnails) for quick whole-deck review."""
import sys, os, glob
from PIL import Image, ImageDraw

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

COLS = 6
TW = 400
PAD = 6
LABEL = 18


def sheet(folder, out):
    files = sorted(glob.glob(os.path.join(folder, '*.png')))
    if not files:
        print('no images in', folder)
        return
    im0 = Image.open(files[0])
    th = int(TW * im0.height / im0.width)
    rows = (len(files) + COLS - 1) // COLS
    W = COLS * (TW + PAD) + PAD
    H = rows * (th + LABEL + PAD) + PAD
    canvas = Image.new('RGB', (W, H), (230, 232, 236))
    d = ImageDraw.Draw(canvas)
    for i, f in enumerate(files):
        r, c = divmod(i, COLS)
        im = Image.open(f).convert('RGB').resize((TW, th), Image.LANCZOS)
        x = PAD + c * (TW + PAD)
        y = PAD + r * (th + LABEL + PAD)
        canvas.paste(im, (x, y))
        d.rectangle([x - 1, y - 1, x + TW, y + th], outline=(120, 120, 120))
        d.text((x + 3, y + th + 3), os.path.basename(f).replace('page-', 'p').replace('.png', ''),
               fill=(30, 30, 30))
    canvas.save(out)
    print('%s -> %s  (%dx%d, %d pages)' % (folder, out, W, H, len(files)))


if __name__ == '__main__':
    for folder, out in zip(sys.argv[1::2], sys.argv[2::2]):
        sheet(folder, out)
