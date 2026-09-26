# -*- coding: utf-8 -*-
"""
《明日方舟：妄界存言》UI 素材生成器 v2
生成深色 + 琥珀强调的方舟风界面素材（全部自绘，无版权素材依赖）。

用法:
    python tools/gen_ui.py
输出:
    game/gui_gen/*.png

v2 变更:
  - 9-patch 素材升到 96/128px（DPI 缩放下更锐利），圆角与描边同步放大
  - 背景新增 45° 细网格与噪点，避免纯渐变发平
  - 新增 card / card_hover（模式卡片）、bar_fill / bar_track（设置滑条）、deco_line（标题装饰线）
  - ctc 三角重绘并加柔光
"""

import os
import random
from PIL import Image, ImageDraw, ImageFilter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "game", "gui_gen")

W, H = 1280, 720

# ---------- 调色板 ----------
BG_TOP = (10, 12, 16)
BG_BOTTOM = (23, 28, 35)
PANEL_FILL = (15, 19, 24, 242)
PANEL_BORDER = (40, 48, 57, 255)
PANEL_HOVER_FILL = (24, 32, 40, 248)
PANEL_HOVER_BORDER = (66, 80, 94, 255)
BTN_FILL = (20, 26, 32, 240)
BTN_HOVER_FILL = (32, 42, 52, 250)
ACCENT = (227, 180, 87)
COOL = (127, 179, 213)


def ensure_dir():
    os.makedirs(OUT, exist_ok=True)


def vgradient(w, h, top, bottom):
    img = Image.new("RGB", (1, h))
    px = img.load()
    for y in range(h):
        t = y / max(1, h - 1)
        px[0, y] = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
    return img.resize((w, h), Image.BILINEAR).convert("RGBA")


def add_hairlines(img, step=96, inset=110, alpha=7):
    """极淡的水平细线，营造科技面板感"""
    draw = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    for y in range(step, h - 20, step):
        draw.line([(inset, y), (w - inset, y)], fill=(255, 255, 255, alpha), width=1)
    return img


def add_diag_grid(img, step=170, alpha=6):
    """45° 双向细网格，极低透明度，工程图纸感"""
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    w, h = img.size
    for offset in range(-h, w, step):
        d.line([(offset, 0), (offset + h, h)], fill=(255, 255, 255, alpha), width=1)
        d.line([(offset + h, 0), (offset, h)], fill=(255, 255, 255, alpha), width=1)
    return Image.alpha_composite(img, overlay)


def add_noise(img, count=2200, alpha_max=12):
    """极淡噪点，打破渐变色带"""
    random.seed(20260927)
    draw = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    for _ in range(count):
        x = random.randrange(w)
        y = random.randrange(h)
        a = random.randrange(3, alpha_max)
        draw.point((x, y), fill=(255, 255, 255, a))
    return img


def add_corner_brackets(img, margin=44, size=210, alpha=30):
    """四角斜向科技括号（左上/右下长臂，右上/左下短臂呼应）"""
    draw = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    a = (255, 255, 255, alpha)
    # 左上（长）
    draw.polygon([(margin, margin), (margin + size, margin), (margin + size, margin + 3),
                  (margin + 3, margin + 3), (margin + 3, margin + size), (margin, margin + size)], fill=a)
    # 右下（长）
    draw.polygon([(w - margin, h - margin), (w - margin - size, h - margin),
                  (w - margin - size, h - margin - 3), (w - margin - 3, h - margin - 3),
                  (w - margin - 3, h - margin - size), (w - margin, h - margin - size)], fill=a)
    # 右上（短）
    s2 = 90
    draw.polygon([(w - margin - s2, margin), (w - margin, margin), (w - margin, margin + s2),
                  (w - margin - 3, margin + s2), (w - margin - 3, margin + 3),
                  (w - margin - s2, margin + 3)], fill=a)
    # 左下（短）
    draw.polygon([(margin, h - margin - s2), (margin + 3, h - margin - s2), (margin + 3, h - margin - 3),
                  (margin + s2, h - margin - 3), (margin + s2, h - margin),
                  (margin, h - margin)], fill=a)
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
    img = add_diag_grid(img)
    img = add_hairlines(img)
    img = add_noise(img)
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


def rounded_panel(w, h, fill, border, radius=6, accent_bar=None, top_line=None, glow=False):
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=fill, outline=border, width=1)
    # 顶部内高光
    d.line([(radius, 1), (w - radius - 1, 1)], fill=(255, 255, 255, 16), width=1)
    if glow:
        # hover 态：上缘再叠一条更亮的高光
        d.line([(radius + 2, 2), (w - radius - 3, 2)], fill=(255, 255, 255, 26), width=1)
    if accent_bar:
        color, width_px = accent_bar
        d.rectangle([0, 0, width_px - 1, h - 1], fill=color)
    if top_line:
        d.line([(radius, 0), (w - radius - 1, 0)], fill=top_line, width=2)
    return img


def make_frames():
    # 面板（9-patch border 16）
    rounded_panel(128, 128, PANEL_FILL, PANEL_BORDER, radius=6).save(os.path.join(OUT, "panel.png"))
    rounded_panel(128, 128, PANEL_HOVER_FILL, PANEL_HOVER_BORDER, radius=6, glow=True).save(
        os.path.join(OUT, "panel_hover.png"))

    # 模式卡片（border 16，左侧琥珀条；hover 边框转琥珀）
    rounded_panel(128, 128, (16, 20, 26, 244), PANEL_BORDER, radius=6,
                  accent_bar=(ACCENT + (170,), 5)).save(os.path.join(OUT, "card.png"))
    rounded_panel(128, 128, (27, 35, 44, 250), ACCENT + (190,), radius=6,
                  accent_bar=(ACCENT + (255,), 5), glow=True).save(os.path.join(OUT, "card_hover.png"))

    # 按钮（border 12，左侧琥珀条）
    rounded_panel(96, 96, BTN_FILL, PANEL_BORDER, radius=5,
                  accent_bar=(ACCENT + (190,), 4)).save(os.path.join(OUT, "btn.png"))
    rounded_panel(96, 96, BTN_HOVER_FILL, PANEL_HOVER_BORDER, radius=5,
                  accent_bar=(ACCENT + (255,), 4), glow=True).save(os.path.join(OUT, "btn_hover.png"))

    # 姓名条（border 12，左侧琥珀条更粗）
    rounded_panel(96, 96, (18, 22, 27, 240), PANEL_BORDER, radius=5,
                  accent_bar=(ACCENT + (255,), 5)).save(os.path.join(OUT, "nameplate.png"))

    # 对话框（border 16，顶部琥珀发丝）
    rounded_panel(128, 128, (5, 7, 10, 228), (26, 31, 38, 255), radius=6,
                  top_line=ACCENT + (150,)).save(os.path.join(OUT, "window_bg.png"))

    # 存档槽（border 14）
    rounded_panel(96, 96, (16, 20, 25, 246), PANEL_BORDER, radius=6).save(os.path.join(OUT, "slot.png"))
    rounded_panel(96, 96, (27, 35, 44, 250), PANEL_HOVER_BORDER, radius=6,
                  accent_bar=(ACCENT + (210,), 4), glow=True).save(os.path.join(OUT, "slot_hover.png"))

    # 快捷栏（border 12）
    rounded_panel(96, 96, (8, 10, 13, 205), (30, 36, 44, 225), radius=5,
                  top_line=(255, 255, 255, 20)).save(os.path.join(OUT, "quickbar.png"))

    # 设置滑条（border 5）
    rounded_panel(16, 16, ACCENT + (235,), (250, 220, 160, 255), radius=6).save(
        os.path.join(OUT, "bar_fill.png"))
    rounded_panel(16, 16, (32, 39, 47, 255), (48, 57, 68, 255), radius=6).save(
        os.path.join(OUT, "bar_track.png"))


def make_title_rule():
    """旧版标题下划线（保留兼容）：左侧实心琥珀 + 右侧渐隐"""
    w, h = 420, 2
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for x in range(w):
        t = x / (w - 1)
        alpha = int(230 * (1 - t) + 20)
        d.line([(x, 0), (x, h - 1)], fill=ACCENT + (alpha,))
    img.save(os.path.join(OUT, "rule.png"))


def make_deco_line():
    """标题装饰线：左右渐隐细线 + 中央菱形"""
    w, h = 640, 16
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cy = h // 2
    # 中央菱形（旋转 45° 的小方块）+ 深色内芯
    d.polygon([(w // 2, cy - 5), (w // 2 + 5, cy), (w // 2, cy + 5), (w // 2 - 5, cy)],
              fill=ACCENT + (255,))
    d.polygon([(w // 2, cy - 2), (w // 2 + 2, cy), (w // 2, cy + 2), (w // 2 - 2, cy)],
              fill=(10, 12, 16, 255))
    # 两侧渐隐线（靠近菱形最亮，向外消失）
    half = w // 2 - 14
    for x in range(half):
        t = (half - x) / max(1, half)
        alpha = int(220 * (1 - t))
        d.line([(x, cy - 1), (x, cy)], fill=ACCENT + (alpha,))
        d.line([(w - 1 - x, cy - 1), (w - 1 - x, cy)], fill=ACCENT + (alpha,))
    img.save(os.path.join(OUT, "deco_line.png"))


def make_ctc_arrow():
    """点击继续指示器：琥珀三角 + 柔光（4x 超采样保证边缘锐利）"""
    w, h = 20, 12
    img = Image.new("RGBA", (w * 4, h * 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.polygon([(0, 0), (w * 4 - 1, 0), (w * 2, h * 4 - 1)], fill=ACCENT + (255,))
    img = img.resize((w, h), Image.LANCZOS)
    glow = img.filter(ImageFilter.GaussianBlur(1.5))
    out = Image.alpha_composite(glow, img)
    out.save(os.path.join(OUT, "ctc.png"))


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
    make_deco_line()
    make_ctc_arrow()
    make_checker()
    files = sorted(os.listdir(OUT))
    print("生成完成 ->", OUT)
    for f in files:
        print("  ", f, os.path.getsize(os.path.join(OUT, f)), "bytes")


if __name__ == "__main__":
    main()
