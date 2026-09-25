# ============================================================
# 游戏内菜单层：游戏菜单 / 存档 / 读档 / 设置 / 历史
# 这些界面由 Esc、鼠标右键或快捷工具栏唤起
# ============================================================

################################################################################
# 游戏菜单外壳（左导航 + 右内容）
################################################################################

screen game_menu(title, scroll=None):
    tag menu
    style_prefix "gm"

    add Solid("#0B0D10")

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 48

        vbox:
            xsize 240
            spacing 10

            text title style "gm_title"

            null height 14

            textbutton "继续游戏" action Return()
            textbutton "存档" action ShowMenu("save")
            textbutton "读档" action ShowMenu("load")
            textbutton "历史" action ShowMenu("history")
            textbutton "设置" action ShowMenu("preferences")

            null height 14

            textbutton "返回标题" action MainMenu()
            textbutton "退出游戏" action Quit(confirm=True)

        frame:
            style "gm_content"

            if scroll == "viewport":
                viewport:
                    mousewheel True
                    draggable True
                    ysize 460
                    transclude
            else:
                transclude


style gm_title:
    size 30
    color "#E8E8E8"

style gm_content:
    background Solid("#12151A")
    padding (36, 28)
    xsize 820
    ysize 520

style gm_button is confirm_button
style gm_button_text is confirm_button_text
style gm_button:
    xfill True

################################################################################
# 存档 / 读档
################################################################################

screen save():
    tag menu
    use file_slots("存档", True)

screen load():
    tag menu
    use file_slots("读档", False)

screen file_slots(title, save_mode):
    use game_menu(title):
        vbox:
            spacing 18

            grid 3 2:
                spacing 16

                for i in range(1, 7):

                    button:
                        action (FileSave(i) if save_mode else FileLoad(i))
                        style "slot_button"
                        has vbox
                        spacing 6

                        add FileScreenshot(i)

                        text FileTime(i, format="%m-%d %H:%M", empty="— 空档位 —") style "slot_time_text"

            hbox:
                xalign 0.5
                spacing 16

                textbutton "上一页" action FilePagePrevious()
                textbutton "自动存档" action FilePage("auto")
                textbutton "下一页" action FilePageNext()


style slot_button:
    padding (6, 6)
    background Solid("#1A1E24")
    hover_background Solid("#28323E")

style slot_time_text:
    size 16
    color "#9AA0A8"
    xalign 0.5

################################################################################
# 设置
################################################################################

screen preferences():
    tag menu
    use game_menu("设置"):
        vbox:
            spacing 26

            vbox:
                spacing 6
                text "文字速度" style "pref_label"
                bar value Preference("text speed") xsize 460

            vbox:
                spacing 6
                text "自动前进间隔" style "pref_label"
                bar value Preference("auto-forward time") xsize 460

            vbox:
                spacing 10
                text "音量" style "pref_label"

                hbox:
                    spacing 16
                    text "音乐" style "pref_label_sub" yalign 0.5
                    bar value Preference("music volume") xsize 320
                hbox:
                    spacing 16
                    text "音效" style "pref_label_sub" yalign 0.5
                    bar value Preference("sound volume") xsize 320
                hbox:
                    spacing 16
                    text "语音" style "pref_label_sub" yalign 0.5
                    bar value Preference("voice volume") xsize 320

            hbox:
                spacing 20
                textbutton "窗口 / 全屏" action Preference("display", "toggle")
                textbutton "跳过未读文本" action Preference("skip", "toggle")


style pref_label:
    size 20
    color "#C3C9D1"

style pref_label_sub:
    size 18
    color "#8A9099"
    xsize 60

style pref_button is confirm_button
style pref_button_text is confirm_button_text

################################################################################
# 历史记录
################################################################################

screen history():
    tag menu
    use game_menu("历史", scroll="viewport"):
        vbox:
            spacing 18

            if not _history_list:
                text "暂无历史记录。" style "history_empty"

            for h in _history_list:
                vbox:
                    spacing 4

                    if h.who:
                        text h.who style "history_name_text"

                    text h.what style "history_text"
                    # 去掉文本标签，按纯文本显示


style history_text:
    size 22
    color "#C3C9D1"
    line_spacing 6
    xsize 700

style history_name_text:
    size 20
    color "#7FB3D5"

style history_empty:
    size 20
    color "#6E747C"
