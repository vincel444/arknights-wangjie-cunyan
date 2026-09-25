# ============================================================
# 对话演出层：对话框、姓名条、选项按钮、快捷工具栏
# 视觉基调：深色半透明 + 冷灰文字 + 左侧强调色姓名条
# ============================================================

################################################################################
# 对话屏幕
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


style say_window:
    xfill True
    yalign 1.0
    ysize 250
    background Solid("#05070AD9")
    padding (64, 56, 64, 44)

style namebox:
    xpos 0
    ypos -34
    background Solid("#12151AF0")
    padding (24, 8)

style say_label:
    color "#E8E8E8"
    size 28
    bold False

style say_dialogue:
    xpos 4
    size 27
    color "#E8E8E8"
    outlines [ (2, "#000000B0", 0, 0) ]
    line_spacing 12
    kerning 0.4

################################################################################
# 选项按钮（剧中分支）
################################################################################

style choice_button:
    xsize 860
    xalign 0.5
    background Solid("#12151AD8")
    hover_background Solid("#2C3E52E8")
    padding (40, 18)

style choice_button_text:
    size 26
    color "#C3C9D1"
    hover_color "#FFFFFF"
    xalign 0.5

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing 14

################################################################################
# 快捷工具栏（游戏中常驻，鼠标移到屏幕底部出现）
################################################################################

screen quick_menu():
    zorder 100
    style_prefix "quick"

    hbox:
        xalign 0.5
        yalign 1.0
        yoffset -8
        spacing 4

        textbutton "回退" action Rollback()
        textbutton "隐藏" action HideInterface()
        textbutton "自动" action Preference("auto-forward", "toggle")
        textbutton "快进" action Skip() alternate Skip(fast=True, confirm=True)
        textbutton "存档" action ShowMenu("save")
        textbutton "读档" action ShowMenu("load")
        textbutton "历史" action ShowMenu("history")
        textbutton "设置" action ShowMenu("preferences")
        textbutton "标题" action MainMenu()


style quick_button:
    padding (16, 6)
    background None

style quick_button_text:
    size 18
    color "#6E747C"
    hover_color "#FFFFFF"
    selected_color "#7FB3D5"
