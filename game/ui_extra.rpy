# ============================================================
# 演出层 UI：对话框、姓名条、选项按钮、快捷工具栏
# ============================================================

################################################################################
# 点击继续指示器（对话框右下角呼吸的 ▼）
################################################################################

transform ctc_pulse:
    alpha 0.35
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.35
    repeat

image ctc_arrow = At(Text("▼", size=16, color="#E3B457"), ctc_pulse)


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
    ysize 260
    background Frame("gui_gen/window_bg.png", 8, 8)
    padding (64, 60, 64, 50)

style namebox:
    xpos 0
    ypos -38
    background Frame("gui_gen/nameplate.png", 8, 8)
    padding (24, 8)

style say_label:
    color "#EAEAEA"
    size 28
    bold False
    outlines [ (2, "#000000A0", 0, 0) ]

style say_dialogue:
    xpos 4
    size 27
    color "#EAEAEA"
    outlines [ (2, "#000000B0", 0, 0) ]
    line_spacing 12
    kerning 0.4


################################################################################
# 选项按钮（剧中分支）
################################################################################

style choice_button:
    xsize 840
    xalign 0.5
    background Frame("gui_gen/btn.png", 8, 8)
    hover_background Frame("gui_gen/btn_hover.png", 8, 8)
    padding (40, 20)

style choice_button_text:
    size 26
    color "#C3C9D1"
    hover_color "#FFFFFF"
    xalign 0.0

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing 16


################################################################################
# 快捷工具栏（游戏中常驻，鼠标移到屏幕底部出现）
################################################################################

screen quick_menu():
    zorder 100
    style_prefix "quick"

    frame:
        xalign 0.5
        yalign 1.0
        yoffset -4
        background Frame("gui_gen/quickbar.png", 8, 8)
        padding (14, 8)

        hbox:
            spacing 2

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
    padding (14, 6)
    background None

style quick_button_text:
    size 18
    color "#6E747C"
    hover_color "#FFFFFF"
    selected_color "#7FB3D5"
