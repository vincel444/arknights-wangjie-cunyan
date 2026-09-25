# ============================================================
# 基础 UI 屏幕层（对照官方 gui 模板精简）
# 后续方舟化视觉改造在此文件上进行
# ============================================================

define config.confirm_screen = True

################################################################################
# 主菜单（标题画面）
################################################################################

screen main_menu_title():
    style_prefix "title"

    add Solid("#0B0D10")

    vbox:
        xalign 0.5
        yalign 0.38
        spacing 20

        text "明日方舟：妄界存言":
            xalign 0.5
            size 46
            color "#E8E8E8"

        text "非官方同人作品 · 仅供学习交流":
            xalign 0.5
            size 16
            color "#8A8F98"

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
        color "#4A4F56"


style title_button is confirm_button
style title_button_text is confirm_button_text

# 章节结束卡
screen chapter_end_card(chapter_text):
    add Solid("#000000")

    vbox:
        xalign 0.5
        yalign 0.45
        spacing 28

        text chapter_text:
            xalign 0.5
            size 40
            color "#E8E8E8"

        text "未完待续":
            xalign 0.5
            size 22
            color "#8A8F98"

    text "点击继续":
        xalign 0.5
        yalign 0.92
        size 14
        color "#5A5F66"

################################################################################
# 角色剧情 · 角色列表
################################################################################

screen chara_story_list():
    style_prefix "title"

    add Solid("#0B0D10")

    vbox:
        xalign 0.5
        yalign 0.18
        spacing 12

        text "角色剧情":
            xalign 0.5
            size 34
            color "#E8E8E8"

        text "选择干员，阅读其个人剧情":
            xalign 0.5
            size 15
            color "#6E747C"

    vbox:
        xalign 0.5
        yalign 0.48
        spacing 16

        textbutton "仕衣":
            action Return("shiyi")

    vbox:
        xalign 0.5
        yalign 0.87

        textbutton "返回":
            action Return("back")


################################################################################
# 模式选择（开始游戏后进入）
################################################################################

screen mode_select_menu():
    style_prefix "title"

    add Solid("#0B0D10")

    vbox:
        xalign 0.5
        yalign 0.2
        spacing 12

        text "选择模式":
            xalign 0.5
            size 34
            color "#E8E8E8"

        text "主线模式 / 角色剧情 / 开发中内容":
            xalign 0.5
            size 15
            color "#6E747C"

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 120

        vbox:
            spacing 16

            textbutton "主线模式":
                action Return("main")
            textbutton "角色剧情":
                action Return("chara")
            textbutton "干员档案":
                action Return("archive")

        vbox:
            spacing 16

            textbutton "故事集":
                action Return("collection")
            textbutton "时间线":
                action Return("timeline")
            textbutton "正在开发":
                action Return("dev")

    vbox:
        xalign 0.5
        yalign 0.87

        textbutton "返回标题":
            action Return("back")


# 通用提示页（占位模式用）
screen notice_screen(notice_title, notice_body):
    style_prefix "title"

    add Solid("#0B0D10")

    vbox:
        xalign 0.5
        yalign 0.32
        spacing 24

        text notice_title:
            xalign 0.5
            size 34
            color "#E8E8E8"

        text notice_body:
            xalign 0.5
            text_align 0.5
            size 18
            color "#9AA0A8"
            line_spacing 10

    vbox:
        xalign 0.5
        yalign 0.82

        textbutton "返回":
            action Return()

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
        background Solid("#1C1E22")
        padding (48, 36)

        vbox:
            spacing 28
            xalign 0.5

            text message:
                xalign 0.5
                text_align 0.5
                color "#E8E8E8"
                size 24

            hbox:
                xalign 0.5
                spacing 48

                textbutton _("确定"):
                    action yes_action
                textbutton _("取消"):
                    action no_action


style confirm_frame is default

style confirm_button is default:
    xminimum 160
    background Solid("#2E3138")
    padding (20, 10)

style confirm_button_text is default:
    xalign 0.5
    color "#E8E8E8"
    size 22

style confirm_button_hover is confirm_button:
    background Solid("#3D5A73")

style confirm_button_text_hover is confirm_button_text:
    color "#FFFFFF"
