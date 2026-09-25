# ============================================================
# 导航层 UI：标题、模式选择、角色列表、结束卡、确认弹窗
# 配色：深色底 + 琥珀色强调(#E3B457) + 冷灰蓝次级(#7FB3D5)
# ============================================================

define config.confirm_screen = True

# ---------- 通用颜色 ----------
define C_TEXT = "#EAEAEA"
define C_MUTED = "#8A9099"
define C_ACCENT = "#E3B457"
define C_COOL = "#7FB3D5"
define C_BG = "#0B0D10"


################################################################################
# 标题画面
################################################################################

screen main_menu_title():
    style_prefix "title"

    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.28
        spacing 12

        text "明日方舟：妄界存言":
            size 64
            kerning 5
            color C_TEXT
            outlines [ (3, "#00000080", 0, 0) ]

        hbox:
            xalign 0.5
            add "gui_gen/rule.png"

        text "ARKNIGHTS · FAN VISUAL NOVEL":
            size 13
            kerning 4
            color C_MUTED

        text "非官方同人作品 · 仅供学习交流":
            size 15
            color "#5A6068"

    vbox:
        xalign 0.5
        yalign 0.66
        spacing 16

        textbutton "开始游戏":
            action Start("mode_select")
        textbutton "读取存档":
            action ShowMenu("load")
        textbutton "设置":
            action ShowMenu("preferences")
        textbutton "退出游戏":
            action Quit(confirm=False)

    text "v[config.version]":
        xalign 0.98
        yalign 0.97
        size 14
        color "#3A4048"


style title_button:
    xsize 300
    xalign 0.5
    background Frame("gui_gen/btn.png", 8, 8)
    hover_background Frame("gui_gen/btn_hover.png", 8, 8)
    padding (32, 16)

style title_button_text:
    size 24
    color "#EAEAEA"
    hover_color "#FFFFFF"
    xalign 0.0


################################################################################
# 模式选择
################################################################################

screen mode_select_menu():
    style_prefix "mode"

    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.16
        spacing 10

        text "选择模式":
            size 38
            kerning 4
            color C_TEXT

        hbox:
            xalign 0.5
            add "gui_gen/rule.png" xysize (240, 2)

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100

        vbox:
            spacing 14

            textbutton "主线模式":
                action Return("main")
            textbutton "角色剧情":
                action Return("chara")
            textbutton "干员档案":
                action Return("archive")

        vbox:
            spacing 14

            textbutton "故事集":
                action Return("collection")
            textbutton "时间线":
                action Return("timeline")
            textbutton "正在开发":
                action Return("dev")

    vbox:
        xalign 0.5
        yalign 0.88

        textbutton "返回标题":
            action Return("back")


style mode_button is title_button
style mode_button_text is title_button_text


################################################################################
# 角色剧情 · 角色列表
################################################################################

screen chara_story_list():
    style_prefix "mode"

    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.16
        spacing 10

        text "角色剧情":
            size 38
            kerning 4
            color C_TEXT

        hbox:
            xalign 0.5
            add "gui_gen/rule.png" xysize (240, 2)

        text "选择干员，阅读其个人剧情":
            size 15
            color C_MUTED

    vbox:
        xalign 0.5
        yalign 0.48
        spacing 16

        textbutton "仕衣":
            action Return("shiyi")

    vbox:
        xalign 0.5
        yalign 0.88

        textbutton "返回":
            action Return("back")


################################################################################
# 通用提示页（占位模式用）
################################################################################

screen notice_screen(notice_title, notice_body):
    add "gui_gen/bg_main.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 680
        background Frame("gui_gen/panel.png", 12, 12)
        padding (48, 44)

        vbox:
            spacing 24
            xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                add Solid(C_ACCENT) xysize (6, 30)
                text notice_title:
                    size 34
                    color C_TEXT
                    yalign 0.5

            text notice_body:
                xalign 0.5
                text_align 0.5
                size 19
                color C_MUTED
                line_spacing 10

            null height 16

            textbutton "返回":
                xalign 0.5
                action Return()


style notice_button is title_button:
    xsize 180

style notice_button_text is title_button_text:
    xalign 0.5


################################################################################
# 章节结束卡
################################################################################

screen chapter_end_card(chapter_text):
    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.4
        spacing 28
        xsize 520

        hbox:
            xalign 0.5
            spacing 0
            add Solid(C_ACCENT) xysize (80, 2)
            null width 16
            add Solid(C_ACCENT) xysize (80, 2)

        text chapter_text:
            xalign 0.5
            size 42
            kerning 4
            color C_TEXT

        text "未完待续":
            xalign 0.5
            size 22
            color C_MUTED

    text "点击继续":
        xalign 0.5
        yalign 0.9
        size 15
        color C_MUTED
        at ctc_pulse


################################################################################
# 确认弹窗（退出/返回主菜单时调用）
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add Solid("#000000C8")

    frame:
        xalign 0.5
        yalign 0.5
        background Frame("gui_gen/panel.png", 12, 12)
        padding (48, 36)

        vbox:
            spacing 28
            xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                add Solid(C_ACCENT) xysize (4, 22)
                text message:
                    size 24
                    color C_TEXT
                    yalign 0.5

            hbox:
                xalign 0.5
                spacing 40

                textbutton "确定":
                    action yes_action
                textbutton "取消":
                    action no_action


style confirm_button is title_button:
    xsize 140

style confirm_button_text is title_button_text:
    xalign 0.5
