# -*- coding: utf-8 -*-
"""
创建「明日方舟：妄界存言」桌面快捷方式。
SDK 或项目目录移动后，改一下下面的 SDK_RENPY 再重跑本脚本即可。

用法:
    python tools/create_shortcut.py
依赖:
    pywin32（pip install pywin32）
输出:
    桌面\明日方舟：妄界存言.lnk
"""

import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SDK_RENPY = r"F:\bian\renpy\renpy-8.5.3-sdk\lib\py3-windows-x86_64\renpy.exe"
ICON = os.path.join(BASE, "game_icon.ico")


def main():
    import pythoncom
    from win32com.client import Dispatch

    if not os.path.isfile(SDK_RENPY):
        print("WARNING: SDK 路径不存在:", SDK_RENPY)

    pythoncom.CoInitialize()
    ws = Dispatch("WScript.Shell")
    desktop = ws.SpecialFolders("Desktop")
    lnk = os.path.join(desktop, "明日方舟：妄界存言.lnk")

    sc = ws.CreateShortcut(lnk)
    sc.TargetPath = SDK_RENPY
    sc.Arguments = '"%s"' % BASE
    sc.WorkingDirectory = BASE
    sc.IconLocation = "%s,0" % ICON
    sc.Description = "明日方舟同人 AVG · 双击启动游戏"
    sc.Save()

    print("created:", lnk, "| exists:", os.path.isfile(lnk))


if __name__ == "__main__":
    main()
