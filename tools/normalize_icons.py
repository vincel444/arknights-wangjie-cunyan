"""把 Ardot 导出的图标 PNG 规范化为带 alpha 的 RGBA 素材。

Ardot 导出的是 128x128 调色板 PNG（colortype=3），透明信息靠 tRNS 承载，
在 Ren'Py 里缩放显示容易出现硬边锯齿。此脚本统一转为 RGBA 并写入原路径，
同时输出探测报告 icon_probe.txt（模式 / 尺寸 / 透明像素包围盒）。

运行：<venv python> tools/normalize_icons.py
"""
import glob
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "game", "gui_gen", "icons")
OUT = os.path.join(ROOT, "icon_probe.txt")

lines = []
for path in sorted(glob.glob(os.path.join(BASE, "*.png"))):
    with Image.open(path) as img:
        src_mode = img.mode
        src_size = img.size
        rgba = img.convert("RGBA")
    bbox = rgba.getchannel("A").getbbox()
    corner_alpha = rgba.getpixel((0, 0))[3]
    rgba.save(path, "PNG", optimize=True)
    lines.append(
        os.path.basename(path)
        + " src=" + src_mode + " " + str(src_size[0]) + "x" + str(src_size[1])
        + " -> RGBA  corner_alpha=" + str(corner_alpha)
        + " ink_bbox=" + str(bbox)
    )

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines) + "\n")
