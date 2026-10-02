# -*- coding: utf-8 -*-
"""git 状态/提交/推送辅助：PowerShell 下 git 常静默失败，改走 Python subprocess。

用法：
  <venv python> tools/git_helper.py status
  <venv python> tools/git_helper.py commit <message.txt>
  <venv python> tools/git_helper.py push
输出统一落 tools/_git.txt（UTF-8）。
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tools", "_git.txt")

CANDIDATES = [
    r"C:\Program Files\Git\cmd\git.exe",
    r"C:\Program Files\Volta\tools\image\git\cmd\git.exe",
    r"C:\Users\54780\.workbuddy\binaries\PortableGit\versions\1.2.0\bin\git.exe",
    r"C:\Users\54780\.workbuddy\binaries\PortableGit\versions\1.2.0\cmd\git.exe",
    "git",
]


def git_exe():
    for c in CANDIDATES:
        if os.path.isfile(c) or c == "git":
            return c
    return "git"


def run(args):
    exe = git_exe()
    r = subprocess.run([exe, "-C", ROOT] + args, capture_output=True, timeout=120)
    return r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")


lines = []
mode = sys.argv[1] if len(sys.argv) > 1 else "status"
if mode == "status":
    rc, out, err = run(["status", "--porcelain=v1", "-b"])
elif mode == "commit":
    msg_file = os.path.abspath(sys.argv[2])
    rc, out, err = run(["commit", "-F", msg_file])
elif mode == "push":
    rc, out, err = run(["push", "origin", "main"])
elif mode == "add":
    rc, out, err = run(["add"] + sys.argv[2:])
elif mode == "raw":
    rc, out, err = run(sys.argv[2:])
else:
    rc, out, err = 2, "", "unknown mode"

lines.append("mode=" + mode + " rc=" + str(rc))
if out.strip():
    lines.append("--- stdout ---")
    lines.append(out)
if err.strip():
    lines.append("--- stderr ---")
    lines.append(err)

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines) + "\n")
