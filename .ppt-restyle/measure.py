"""Measure key landmarks in a rendered slide and compare with XML geometry."""
import sys
from PIL import Image

path = sys.argv[1]
im = Image.open(path).convert('RGB')
W, H = im.size
px = im.load()
PPI = W / (12192000 / 914400)
print('image %dx%d  ppi=%.3f' % (W, H, PPI))


def blue(c):
    r, g, b = c
    return b > 90 and b - r > 45 and b - g > 25


def white(c):
    return min(c) > 225


# white glyph pixels that sit inside the blue ribbon area (top-left 3.5in x 3in)
whites = [(x, y) for y in range(0, int(3.0 * PPI)) for x in range(0, int(3.5 * PPI))
          if white(px[x, y]) and any(blue(px[x + dx, y + dy])
                                     for dx in (-14, 14) for dy in (-14, 14)
                                     if 0 <= x + dx < W and 0 <= y + dy < H)]
if whites:
    xs = [p[0] for p in whites]
    ys = [p[1] for p in whites]
    print('ribbon "01" white glyphs: x %d..%d (%.2f..%.2f in)  y %d..%d (%.2f..%.2f in)' % (
        min(xs), max(xs), min(xs) / PPI, max(xs) / PPI,
        min(ys), max(ys), min(ys) / PPI, max(ys) / PPI))
else:
    print('no ribbon glyphs found')

# blue title text in the band just right of the ribbon
band = [(x, y) for y in range(0, int(1.6 * PPI)) for x in range(int(2.2 * PPI), W) if blue(px[x, y])]
if band:
    xs = [p[0] for p in band]
    ys = [p[1] for p in band]
    print('title text            : x %d..%d (%.2f..%.2f in)  y %d..%d (%.2f..%.2f in)' % (
        min(xs), max(xs), min(xs) / PPI, max(xs) / PPI,
        min(ys), max(ys), min(ys) / PPI, max(ys) / PPI))

# bottom-most non-white content row (to see whether the whole slide is used)
lastrow = 0
for y in range(H - 1, -1, -1):
    if any(not white(px[x, y]) and not blue(px[x, y]) or blue(px[x, y]) for x in range(0, W, 3)):
        if any(min(px[x, y]) < 235 for x in range(0, W, 3)):
            lastrow = y
            break
print('lowest non-white row  : %d (%.2f in of %.2f in)' % (lastrow, lastrow / PPI, H / PPI))
