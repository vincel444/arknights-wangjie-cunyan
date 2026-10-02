# -*- coding: utf-8 -*-
"""跑 Ren'Py lint 并把 stdout/stderr 落成 UTF-8 文件（PowerShell 会吞 stdout）。

运行：<venv python> tools/run_lint.py
输出：<项目>/tools/_lint.txt
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SDK = r"F:\bian\renpy\renpy-8.5.3-sdk"
OUT = os.path.join(ROOT, "tools", "_lint.txt")

cmd = [
    os.path.join(SDK, "lib", "py3-windows-x86_64", "python.exe"),
    os.path.join(SDK, "renpy.py"),
    ROOT,
    "lint",
]
r = subprocess.run(cmd, capture_output=True, cwd=ROOT, timeout=180)
text = r.stdout.decode("utf-8", "replace") + "\n=== stderr ===\n" + r.stderr.decode("utf-8", "replace")
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(text)
print("rc=" + str(r.returncode))
