# -*- coding: utf-8 -*-
"""
《明日方舟：妄界存言》UI 素材生成器
生成深色 + 琥珀强调的方舟风界面素材（全部自绘，无版权素材依赖）。

用法：
    python tools/gen_ui.py
输出：
    game/gui_gen/*.png
"""

import os
from PIL import Image, ImageDraw, ImageFilter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "game", "gui_gen")

W, H = 1280, 720

# ---------- 调色板 ----------
BG_TOP = (10, 12, 16)
BG_BOTTOM = (23, 28, 35)
PANEL_FILL = (15, 19, 24, 242)
PANEL_BORDER = (38, 45, 53, 255)
PANEL_HOVER_FILL = (24, 32, 40, 246)
PANEL_HOVER_BORDER = (62, 76, 89, 255)
BTN_FILL = (20, 26, 32, 240)
BTN_HOVER_FILL = (30, 40, 49, 248)
ACCENT = (227, 180, 87)
COOL = (127, 179, 213)
HAIRLINE = (255, 255, 255, 10)


def ensure_dir():
    os.makedirs(OUT, exist_ok=True)


def vgradient(w, h, top, bottom):
    img = Image.new("RGB", (1, h))
    px = img.load()
    for y in range(h):
        t = y / max(1, h - 1)
        px[0, y] = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
    return img.resize((w, h), Image.BILINEAR).convert("RGBA")


def add_hairlines(img, step=90, inset=110, alpha=8):
    """极淡的水平细线，营造科技面板感"""
    draw = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    for y in range(step, h - 20, step):
        draw.line([(inset, y), (w - inset, y)], fill=(255, 255, 255, alpha), width=1)
    return img


def add_corner_brackets(img, margin=44, size=210, alpha=26):
    """四角斜向科技括号"""
    draw = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    a = (255, 255, 255, alpha)
    # 左上
    draw.polygon([(margin, margin), (margin + size, margin), (margin + size, margin + 3), (margin + 3, margin + 3), (margin + 3, margin + size), (margin, margin + size)], fill=a)
    # 右下
    draw.polygon([(w - margin, h - margin), (w - margin - size, h - margin), (w - margin - size, h - margin - 3), (w - margin - 3, h - margin - 3), (w - margin - 3, h - margin - size), (w - margin, h - margin - size)], fill=a)
    return img


def add_accent_block(img, xy, wh, alpha=40):
    draw = ImageDraw.Draw(img, "RGBA")
    x, y = xy
    w, h = wh
    draw.rectangle([x, y, x + w, y + h], fill=ACCENT + (alpha,))
    return img


def add_vignette(img, strength=90):
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(mask)
    inset = 120
    d.rectangle([inset, inset, w - inset, h - inset], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(150))
    dark = Image.new("RGBA", (w, h), (0, 0, 0, strength))
    img = Image.composite(img, Image.alpha_composite(img, dark), mask)
    return img


def make_bg(name, left_band=False):
    img = vgradient(W, H, BG_TOP, BG_BOTTOM)
    add_hairlines(img)
    add_corner_brackets(img)
    add_accent_block(img, (44, 44), (3, 96), 90)
    add_accent_block(img, (44, 44), (96, 3), 90)
    if left_band:
        draw = ImageDraw.Draw(img, "RGBA")
        draw.rectangle([0, 0, 292, H], fill=(0, 0, 0, 90))
        draw.line([(292, 0), (292, H)], fill=(255, 255, 255, 18), width=1)
        add_accent_block(img, (292, 0), (2, 120), 70)
    img = add_vignette(img)
    img.convert("RGB").save(os.path.join(OUT, name), optimize=True)


def rounded_panel(w, h, fill, border, radius=3, accent_bar=None, top_line=None, bottom_line=None):
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=fill, outline=border, width=1)
    # 顶部内高光
    d.line([(radius, 1), (w - radius - 1, 1)], fill=(255, 255, 255, 14), width=1)
    if accent_bar:
        color, width_px = accent_bar
        d.rectangle([0, 0, width_px - 1, h - 1], fill=color)
    if top_line:
        d.line([(0, 0), (w - 1, 0)], fill=top_line, width=1)
    if bottom_line:
        d.line([(0, h - 1), (w - 1, h - 1)], fill=bottom_line, width=1)
    return img


def make_frames():
    # 面板（9 补丁：border 12）
    rounded_panel(64, 64, PANEL_FILL, PANEL_BORDER).save(os.path.join(OUT, "panel.png"))
    rounded_panel(64, 64, PANEL_HOVER_FILL, PANEL_HOVER_BORDER).save(os.path.join(OUT, "panel_hover.png"))

    # 按钮（9 补丁：border 8，左侧琥珀色条）
    rounded_panel(48, 48, BTN_FILL, PANEL_BORDER, accent_bar=(ACCENT + (190,), 3)).save(
        os.path.join(OUT, "btn.png"))
    rounded_panel(48, 48, BTN_HOVER_FILL, PANEL_HOVER_BORDER, accent_bar=(ACCENT + (255,), 3)).save(
        os.path.join(OUT, "btn_hover.png"))

    # 姓名条（左侧琥珀色条更粗）
    rounded_panel(48, 48, (18, 22, 27, 240), PANEL_BORDER, accent_bar=(ACCENT + (255,), 4)).save(
        os.path.join(OUT, "nameplate.png"))

    # 对话框（顶部琥珀色发丝 + 深色底）
    rounded_panel(64, 64, (5, 7, 10, 226), (24, 29, 35, 255), top_line=ACCENT + (150,)).save(
        os.path.join(OUT, "window_bg.png"))

    # 存档槽
    rounded_panel(64, 64, (16, 20, 25, 246), PANEL_BORDER).save(os.path.join(OUT, "slot.png"))
    rounded_panel(64, 64, (26, 34, 43, 250), PANEL_HOVER_BORDER, accent_bar=(ACCENT + (200,), 3)).save(
        os.path.join(OUT, "slot_hover.png"))

    # 快捷栏底条
    rounded_panel(64, 64, (8, 10, 13, 200), (28, 34, 41, 220), top_line=(255, 255, 255, 16)).save(
        os.path.join(OUT, "quickbar.png"))


def make_title_rule():
    """标题下划线：左侧实心琥珀 + 右侧渐隐"""
    w, h = 420, 2
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for x in range(w):
        t = x / (w - 1)
        alpha = int(230 * (1 - t) + 20)
        d.line([(x, 0), (x, h - 1)], fill=ACCENT + (alpha,))
    img.save(os.path.join(OUT, "rule.png"))


def make_ctc_arrow():
    """点击继续指示器：细琥珀三角"""
    w, h = 14, 9
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.polygon([(0, 0), (w - 1, 0), (w // 2, h - 1)], fill=ACCENT + (255,))
    img.save(os.path.join(OUT, "ctc.png"))


def make_checker():
    """缩略图失败时的占位块"""
    img = Image.new("RGBA", (32, 32), (18, 22, 27, 255))
    d = ImageDraw.Draw(img)
    d.line([(0, 0), (31, 31)], fill=(40, 47, 55, 255))
    img.save(os.path.join(OUT, "placeholder.png"))


def main():
    ensure_dir()
    make_bg("bg_main.png")
    make_bg("bg_menu.png", left_band=True)
    make_frames()
    make_title_rule()
    make_ctc_arrow()
    make_checker()
    files = sorted(os.listdir(OUT))
    print("生成完成 ->", OUT)
    for f in files:
        print("  ", f, os.path.getsize(os.path.join(OUT, f)), "bytes")


if __name__ == "__main__":
    main()
