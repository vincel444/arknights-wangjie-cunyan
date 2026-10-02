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

# ---------- 图标系统 v1 ----------
# 素材：gui_gen/icons/*.png（Ardot 导出，源 64 栅格 / 线稿 4px / 琥珀 #E3B457，导出于 2x = 128px）
define ICON_ZOOM = 48.0 / 128.0


################################################################################
# 标题画面
################################################################################

screen main_menu_title():
    style_prefix "title"

    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.25
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

        hbox:
            xalign 0.5
            spacing 10
            add Solid("#3E464F") xysize (24, 1) yalign 0.5
            text "非官方同人作品" size 13 color "#5A6068" yalign 0.5
            add Solid("#3E464F") xysize (24, 1) yalign 0.5

    hbox:
        xalign 0.5
        yalign 0.73
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

    # 左下角制作信息
    vbox:
        xalign 0.015
        yalign 0.965
        spacing 2
        text "WANGJIE CUNYAN" size 11 kerning 4 color "#3A424B"
        text "v[config.version]" size 11 color "#3A424B"


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

screen mode_card(idx, mtitle, mdesc, act, icon=None):
    button:
        style "mode_card"
        action act

        if icon:
            add icon:
                xpos 26
                yalign 0.5
                zoom ICON_ZOOM

        vbox:
            xpos 88
            yalign 0.5
            spacing 8

            text mtitle style "mode_card_title"
            text mdesc style "mode_card_desc"

        text idx style "mode_card_idx" xalign 0.90 yalign 0.06


screen mode_select_menu():
    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.11
        spacing 12

        hbox:
            xalign 0.5
            spacing 12
            add Solid(C_ACCENT) xysize (4, 30) yalign 0.5
            text "选择模式":
                size 36
                kerning 5
                color C_TEXT
                yalign 0.5

        add "gui_gen/deco_line.png" xalign 0.5

        text "MAIN MODE SELECT" :
            xalign 0.5
            size 12
            kerning 8
            color "#3E464F"

    grid 3 2:
        xalign 0.5
        yalign 0.53
        spacing 24

        use mode_card("01", "主线模式", "罗德岛本舰 · 章节式主线", Return("main"), "gui_gen/icons/icon_main.png")
        use mode_card("02", "角色剧情", "干员个人线 · 深入其人", Return("chara"), "gui_gen/icons/icon_chara.png")
        use mode_card("03", "干员档案", "干员资料库 · 建设中", Return("archive"), "gui_gen/icons/icon_archive.png")
        use mode_card("04", "故事集", "短篇与外传 · 建设中", Return("collection"), "gui_gen/icons/icon_collection.png")
        use mode_card("05", "时间线", "泰拉大事记 · 建设中", Return("timeline"), "gui_gen/icons/icon_timeline.png")
        use mode_card("06", "正在开发", "版本路线图 · 敬请期待", Return("dev"), "gui_gen/icons/icon_dev.png")

    textbutton "← 返回标题":
        style "mode_back"
        xalign 0.5
        yalign 0.94
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

# 主行动按钮（开始阅读）：琥珀实底 + 深色字，页面上唯一的高亮元素
style story_cta:
    padding (40, 12)
    background Frame("gui_gen/btn_cta.png", 12, 12)
    hover_background Frame("gui_gen/btn_cta_hover.png", 12, 12)

style story_cta_text:
    size 21
    kerning 6
    color "#0C1015"
    hover_color "#0C1015"

# 逐句阅读页的透明全屏点击层（点击推进，不产生任何视觉）
style story_click:
    background None
    hover_background None


################################################################################
# 章节选择（主线模式入口，替代引擎默认 menu）
################################################################################

screen chapter_row(num, ctitle, csub, act, locked=False):
    button:
        style ("chapter_locked" if locked else "chapter_row")
        action (None if locked else act)

        hbox:
            yalign 0.5
            spacing 0

            # 左侧大号章节数字
            text num:
                style "chapter_num"
                yalign 0.5

            vbox:
                xpos 0
                yalign 0.5
                spacing 6

                text ctitle style "chapter_title"
                text csub style ("chapter_sub_locked" if locked else "chapter_sub")

        # 右侧状态标记
        text ("未解锁" if locked else "▶") style "chapter_flag" xalign 0.95 yalign 0.5


screen chapter_select_menu():
    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.11
        spacing 12

        hbox:
            xalign 0.5
            spacing 12
            add Solid(C_ACCENT) xysize (4, 30) yalign 0.5
            text "主线模式":
                size 36
                kerning 5
                color C_TEXT
                yalign 0.5

        add "gui_gen/deco_line.png" xalign 0.5

        text "MAIN STORY" xalign 0.5 size 12 kerning 8 color "#3E464F"

    vbox:
        xalign 0.5
        yalign 0.53
        spacing 16

        use chapter_row("01", "第一章", "罗德岛本舰 · 深夜的走廊", Return(1))
        use chapter_row("02", "第二章", "待续 · 敬请期待", Return(2), locked=True)
        use chapter_row("03", "第三章", "待续 · 敬请期待", Return(3), locked=True)

    textbutton "← 返回模式选择":
        style "mode_back"
        xalign 0.5
        yalign 0.94
        action Return("back")


style chapter_row:
    xsize 720
    ysize 96
    padding (0, 0)
    background Frame("gui_gen/chapter_card.png", 16, 16)
    hover_background Frame("gui_gen/chapter_card_hover.png", 16, 16)

style chapter_locked is chapter_row:
    background Frame("gui_gen/chapter_card_locked.png", 16, 16)
    hover_background Frame("gui_gen/chapter_card_locked.png", 16, 16)

style chapter_num:
    size 40
    color "#3E464F"
    xsize 92
    xalign 0.5
    kerning 2

style chapter_title:
    size 24
    color "#EAEAEA"
    kerning 2

style chapter_sub:
    size 15
    color "#8A9099"

style chapter_sub_locked:
    size 15
    color "#4E555E"

style chapter_flag:
    size 20
    color "#E3B457"


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
# 故事集 · 故事列表
################################################################################

screen story_card(idx, stitle, sdesc, act):
    button:
        style "story_card"
        action act

        vbox:
            xpos 34
            yalign 0.5
            spacing 9

            text stitle style "story_card_title"
            text sdesc style "story_card_desc"

        text idx style "mode_card_idx" xalign 0.92 yalign 0.08


screen story_collection_list():
    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.11
        spacing 12

        hbox:
            xalign 0.5
            spacing 12
            add Solid(C_ACCENT) xysize (4, 30) yalign 0.5
            text "故事集":
                size 36
                kerning 5
                color C_TEXT
                yalign 0.5

        add "gui_gen/deco_line.png" xalign 0.5

        text "STORY COLLECTION" xalign 0.5 size 12 kerning 8 color "#3E464F"

    # 故事卡片（每行 2 张以内；超过 3 篇时改为 grid 2 N）
    vbox:
        xalign 0.5
        yalign 0.48
        spacing 24

        hbox:
            xalign 0.5
            spacing 24

            use story_card("01", "如您亲启", "一场从未谋划的骗局，一次再向未来的道别", Return("rnqq"))

    textbutton "← 返回模式选择":
        style "mode_back"
        xalign 0.5
        yalign 0.94
        action Return("back")


style story_card:
    xsize 460
    ysize 152
    padding (0, 0)
    background Frame("gui_gen/card.png", 16, 16)
    hover_background Frame("gui_gen/card_hover.png", 16, 16)

style story_card_title:
    size 26
    color "#EAEAEA"
    kerning 2

style story_card_desc:
    size 15
    color "#8A9099"
    line_spacing 4


################################################################################
# 通用提示页（占位模式用）
################################################################################

screen notice_screen(notice_title, notice_body, notice_tag="", notice_items=None):
    add "gui_gen/bg_main.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 720
        background Frame("gui_gen/panel.png", 16, 16)
        padding (52, 46)

        vbox:
            spacing 24
            xalign 0.5

            # 标题区：琥珀竖条 + 标题 + 英文角标
            vbox:
                xalign 0.5
                spacing 10

                hbox:
                    xalign 0.5
                    spacing 12
                    add Solid(C_ACCENT) xysize (4, 30) yalign 0.5
                    text notice_title:
                        size 34
                        color C_TEXT
                        kerning 3
                        yalign 0.5

                add "gui_gen/deco_line.png" xalign 0.5 xysize (480, 12)

                if notice_tag:
                    text notice_tag:
                        xalign 0.5
                        size 12
                        kerning 8
                        color "#3E464F"

            # 状态胶囊
            frame:
                xalign 0.5
                background Frame("gui_gen/hist_item.png", 12, 12)
                padding (20, 8)
                text "◈ 建设中" size 15 color C_COOL

            # 规划条目（若提供则渲染为列表）
            if notice_items:
                vbox:
                    xalign 0.5
                    spacing 10
                    for it in notice_items:
                        hbox:
                            xalign 0.5
                            spacing 10
                            add Solid(C_ACCENT) xysize (3, 16) yalign 0.5
                            text it size 18 color "#A8AFB8" yalign 0.5
            else:
                text notice_body:
                    xalign 0.5
                    text_align 0.5
                    size 19
                    color C_MUTED
                    line_spacing 12

            null height 6

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
