#!/usr/bin/env python3
"""crop.py — 按 960x540 画布坐标裁切截图并放大，便于细看局部渲染。

用法: python crop.py <shot.jpg> <x0> <y0> <x1> <y1> <out.jpg> [scale]
"""
import sys
from PIL import Image


def main(argv):
    src, x0, y0, x1, y1, out = argv[1], float(argv[2]), float(argv[3]), float(argv[4]), float(argv[5]), argv[6]
    scale = float(argv[7]) if len(argv) > 7 else 2.0
    im = Image.open(src)
    W, H = im.size
    sx, sy = W / 960.0, H / 540.0
    box = (int(x0 * sx), int(y0 * sy), int(x1 * sx), int(y1 * sy))
    crop = im.crop(box)
    crop = crop.resize((int(crop.width * scale), int(crop.height * scale)), Image.LANCZOS)
    crop.save(out, quality=95)
    print("saved", out, "src_size=", (W, H), "box=", box, "crop=", crop.size)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
