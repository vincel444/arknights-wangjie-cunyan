# -*- coding: utf-8 -*-
"""
《明日方舟：妄界存言》应用图标生成器
深色圆角底 + 琥珀菱形（与标题装饰线 deco_line 呼应）→ game_icon.ico

用法:
    python tools/gen_icon.py
输出:
    game_icon.ico（项目根目录，供桌面快捷方式引用）
"""

import os
from PIL import Image, ImageDraw

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = 256  # 母版尺寸

ACCENT = (227, 180, 87)
BG_TOP = (10, 12, 16)
BG_BOTTOM = (23, 28, 35)


def build():
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))

    # 深色垂直渐变底 + 圆角裁切
    grad = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    dg = ImageDraw.Draw(grad)
    for y in range(S):
        t = y / (S - 1)
        c = tuple(int(BG_TOP[i] + (BG_BOTTOM[i] - BG_TOP[i]) * t) for i in range(3)) + (255,)
        dg.line([(0, y), (S, y)], fill=c)
    mask = Image.new("L", (S, S), 0)
    dm = ImageDraw.Draw(mask)
    dm.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.18), fill=255)
    img.paste(grad, (0, 0), mask)

    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.18),
                        outline=(64, 76, 90, 255), width=max(2, S // 64))

    # 中央琥珀菱形 + 深色内芯 + 两侧渐隐短线（呼应 deco_line）
    cx = cy = S // 2
    r = int(S * 0.30)
    d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=ACCENT + (255,))
    r2 = int(S * 0.12)
    d.polygon([(cx, cy - r2), (cx + r2, cy), (cx, cy + r2), (cx - r2, cy)],
              fill=(10, 12, 16, 255))
    lw = max(2, S // 42)
    pad = int(S * 0.08)
    d.line([(pad, cy), (cx - r - pad // 2, cy)], fill=ACCENT + (230,), width=lw)
    d.line([(cx + r + pad // 2, cy), (S - pad, cy)], fill=ACCENT + (230,), width=lw)
    return img


def main():
    img = build()
    out = os.path.join(BASE, "game_icon.ico")
    img.save(out, format="ICO",
             sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
    print("saved:", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
