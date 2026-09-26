# -*- coding: utf-8 -*-
"""Check that all expected gui_gen assets exist with expected sizes."""
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "game", "gui_gen")

expected = {
    "bg_main.png": (1280, 720), "bg_menu.png": (1280, 720),
    "panel.png": (128, 128), "panel_hover.png": (128, 128),
    "card.png": (128, 128), "card_hover.png": (128, 128),
    "btn.png": (96, 96), "btn_hover.png": (96, 96),
    "nameplate.png": (96, 96), "window_bg.png": (128, 128),
    "slot.png": (96, 96), "slot_hover.png": (96, 96),
    "quickbar.png": (96, 96), "rule.png": (420, 2),
    "ctc.png": (20, 12), "placeholder.png": (32, 32),
    "deco_line.png": (640, 16), "bar_fill.png": (16, 16), "bar_track.png": (16, 16),
}

lines = []
ok = True
for name, (w, h) in sorted(expected.items()):
    p = os.path.join(OUT, name)
    if not os.path.exists(p):
        lines.append("MISSING " + name)
        ok = False
        continue
    from PIL import Image
    im = Image.open(p)
    status = "OK" if im.size == (w, h) else "BAD size %s want %s" % (im.size, (w, h))
    if im.size != (w, h):
        ok = False
    lines.append("%-18s %sx%s  %6d bytes  %s" % (name, im.size[0], im.size[1], os.path.getsize(p), status))

extra = [f for f in os.listdir(OUT) if f.endswith(".png") and f not in expected]
if extra:
    lines.append("EXTRA: " + ", ".join(sorted(extra)))

lines.append("RESULT: " + ("ALL PASS" if ok else "FAIL"))
report = os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_report.txt")
with open(report, "w", encoding="ascii", errors="replace") as f:
    f.write("\n".join(lines))
print("\n".join(lines))
