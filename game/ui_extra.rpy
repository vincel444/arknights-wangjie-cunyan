# ============================================================
# 演出层 UI：对话框、姓名条、选项按钮、快捷工具栏
# ============================================================

################################################################################
# 点击继续指示器（对话框内呼吸的琥珀三角）
################################################################################

transform ctc_pulse:
    alpha 0.45
    linear 0.7 alpha 1.0
    linear 0.7 alpha 0.45
    repeat

image ctc_arrow = At("gui_gen/ctc.png", ctc_pulse)


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
    background Frame("gui_gen/window_bg.png", 16, 16)
    padding (64, 58, 64, 48)

style namebox:
    xpos 0
    ypos -42
    background Frame("gui_gen/nameplate.png", 12, 12)
    padding (28, 10)

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
    line_spacing 14
    kerning 0.4


################################################################################
# 选项按钮（剧中分支）
################################################################################

style choice_button:
    xsize 840
    xalign 0.5
    background Frame("gui_gen/btn.png", 12, 12)
    hover_background Frame("gui_gen/btn_hover.png", 12, 12)
    padding (40, 20)

style choice_button_text:
    size 26
    color "#C9CFD7"
    hover_color "#FFFFFF"
    xalign 0.5

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing 16


################################################################################
# 快捷工具栏（游戏中常驻，右上角，不遮挡对话框与立绘区文字）
################################################################################

screen quick_menu():
    zorder 100
    style_prefix "quick"

    frame:
        xalign 0.99
        yalign 0.02
        background Frame("gui_gen/quickbar.png", 12, 12)
        padding (18, 9)

        hbox:
            spacing 6

            textbutton "回退" action Rollback()
            textbutton "隐藏" action HideInterface()
            textbutton "自动" action Preference("auto-forward", "toggle")
            textbutton "快进" action Skip() alternate Skip(fast=True, confirm=True)
            textbutton "存档" action ShowMenu("save")
            textbutton "读档" action ShowMenu("load")
            textbutton "历史" action ShowMenu("history")
            textbutton "设置" action ShowMenu("preferences")
            textbutton "标题" action MainMenu()


################################################################################
# 状态提示（快进 / 自动播放），左上角，中文
################################################################################

screen play_state_indicator():
    zorder 99

    if config.skipping:
        frame:
            xalign 0.015
            yalign 0.02
            background Frame("gui_gen/quickbar.png", 12, 12)
            padding (18, 9)
            text "快进中 ▶▶" size 19 color "#E3B457"

    elif preferences.afm_enable:
        frame:
            xalign 0.015
            yalign 0.02
            background Frame("gui_gen/quickbar.png", 12, 12)
            padding (18, 9)
            text "自动播放中" size 19 color "#7FB3D5"


style quick_button:
    padding (15, 7)
    background None

style quick_button_text:
    size 19
    color "#7A828C"
    hover_color "#FFFFFF"
    selected_color "#7FB3D5"
