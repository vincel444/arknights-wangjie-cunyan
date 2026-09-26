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
        yalign 0.26
        spacing 14

        text "明日方舟：妄界存言":
            size 62
            kerning 6
            color C_TEXT
            outlines [ (2, "#000000A0", 0, 0) ]

        add "gui_gen/deco_line.png" xalign 0.5

        text "泰拉纪年 · 剧情向文字冒险":
            size 17
            kerning 7
            color C_COOL

        text "非官方同人作品 · 仅供学习交流":
            size 14
            color "#5A6068"

    hbox:
        xalign 0.5
        yalign 0.74
        spacing 32

        vbox:
            spacing 14

            textbutton "开始游戏":
                action Start("mode_select")
            textbutton "读取存档":
                action ShowMenu("load")

        vbox:
            spacing 14

            textbutton "设置":
                action ShowMenu("preferences")
            textbutton "退出游戏":
                action Quit(confirm=False)

    text "v[config.version]":
        xalign 0.985
        yalign 0.965
        size 14
        color "#565E68"


style title_button:
    xsize 300
    xalign 0.5
    background Frame("gui_gen/btn.png", 12, 12)
    hover_background Frame("gui_gen/btn_hover.png", 12, 12)
    padding (34, 16)

style title_button_text:
    size 24
    color "#EAEAEA"
    hover_color "#FFFFFF"
    xalign 0.5


################################################################################
# 模式选择（3×2 卡片网格）
################################################################################

screen mode_card(idx, mtitle, mdesc, act):
    button:
        style "mode_card"
        action act

        vbox:
            xpos 34
            yalign 0.5
            spacing 8

            text mtitle style "mode_card_title"
            text mdesc style "mode_card_desc"

        text idx style "mode_card_idx" xalign 0.90 yalign 0.06


screen mode_select_menu():
    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.13
        spacing 12

        text "选择模式":
            size 36
            kerning 5
            color C_TEXT

        add "gui_gen/deco_line.png" xalign 0.5

    grid 3 2:
        xalign 0.5
        yalign 0.52
        spacing 24

        use mode_card("01", "主线模式", "罗德岛本舰 · 章节式主线", Return("main"))
        use mode_card("02", "角色剧情", "干员个人线 · 深入其人", Return("chara"))
        use mode_card("03", "干员档案", "干员资料库 · 建设中", Return("archive"))
        use mode_card("04", "故事集", "短篇与外传 · 建设中", Return("collection"))
        use mode_card("05", "时间线", "泰拉大事记 · 建设中", Return("timeline"))
        use mode_card("06", "正在开发", "版本路线图 · 敬请期待", Return("dev"))

    textbutton "← 返回标题":
        style "mode_back"
        xalign 0.5
        yalign 0.92
        action Return("back")


style mode_card:
    xsize 300
    ysize 148
    padding (0, 0)
    background Frame("gui_gen/card.png", 16, 16)
    hover_background Frame("gui_gen/card_hover.png", 16, 16)

style mode_card_title:
    size 25
    color "#EAEAEA"
    kerning 2

style mode_card_desc:
    size 15
    color "#8A9099"
    line_spacing 4

style mode_card_idx:
    size 15
    color "#454E58"

style mode_back:
    background None
    hover_background None
    padding (24, 10)

style mode_back_text:
    size 17
    color "#8A9099"
    hover_color "#EAEAEA"


################################################################################
# 角色剧情 · 角色列表
################################################################################

screen chara_story_list():
    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.15
        spacing 12

        text "角色剧情":
            size 36
            kerning 5
            color C_TEXT

        add "gui_gen/deco_line.png" xalign 0.5

        text "选择干员，阅读其个人剧情":
            size 15
            color C_MUTED

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 24

        use mode_card("01", "仕衣", "第一章 · 等待剧本接入", Return("shiyi"))

    textbutton "← 返回":
        style "mode_back"
        xalign 0.5
        yalign 0.9
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
        background Frame("gui_gen/panel.png", 16, 16)
        padding (52, 48)

        vbox:
            spacing 26
            xalign 0.5

            vbox:
                xalign 0.5
                spacing 12

                text notice_title:
                    size 34
                    color C_TEXT
                    kerning 3
                    xalign 0.5

                add "gui_gen/deco_line.png" xalign 0.5 xysize (460, 12)

            text notice_body:
                xalign 0.5
                text_align 0.5
                size 19
                color C_MUTED
                line_spacing 12

            null height 12

            textbutton "返回":
                style "notice_button"
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
        spacing 30
        xsize 640

        add "gui_gen/deco_line.png" xalign 0.5

        text chapter_text:
            xalign 0.5
            size 42
            kerning 5
            color C_TEXT

        text "未完待续":
            xalign 0.5
            size 20
            kerning 6
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
        background Frame("gui_gen/panel.png", 16, 16)
        padding (52, 40)

        vbox:
            spacing 28
            xalign 0.5

            hbox:
                xalign 0.5
                spacing 12
                add Solid(C_ACCENT) xysize (4, 24)
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
