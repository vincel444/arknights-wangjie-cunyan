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

    add "gui_gen/bg_menu.png"

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 44

        vbox:
            xsize 250
            spacing 8

            text title style "gm_title"
            add Solid("#E3B457") xysize (120, 2)

            null height 18

            textbutton "继续游戏" action Return()
            textbutton "存档" action ShowMenu("save")
            textbutton "读档" action ShowMenu("load")
            textbutton "历史" action ShowMenu("history")
            textbutton "设置" action ShowMenu("preferences")

            null height 18

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
    size 32
    color "#EAEAEA"
    kerning 3

style gm_content:
    background Frame("gui_gen/panel.png", 16, 16)
    padding (36, 28)
    xsize 840
    ysize 520

style gm_button is title_button:
    xsize 240
    xalign 0.0
    selected_background Frame("gui_gen/btn_hover.png", 12, 12)

style gm_button_text is title_button_text:
    selected_color "#E3B457"


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
            spacing 20

            grid 3 2:
                spacing 16

                for i in range(1, 7):

                    button:
                        action (FileSave(i) if save_mode else FileLoad(i))
                        style "slot_button"
                        has vbox
                        spacing 8

                        # 缩略图：外包一层科技细框
                        frame:
                            style "thumb_box"
                            xalign 0.5
                            add FileScreenshot(i) xsize 210 ysize 116

                        text FileTime(i, format="%m-%d %H:%M", empty="— 空档位 —") style "slot_time_text"

            # 页码指示：当前页实心琥珀，共 5 页
            hbox:
                xalign 0.5
                spacing 8
                for p in range(1, 6):
                    if FileCurrentPage() == str(p):
                        add "gui_gen/page_dot_on.png" yalign 0.5
                    else:
                        add "gui_gen/page_dot_off.png" yalign 0.5

            hbox:
                xalign 0.5
                spacing 16

                textbutton "上一页" style "page_button" action FilePagePrevious()
                textbutton "自动存档" style "page_button" action FilePage("auto")
                textbutton "下一页" style "page_button" action FilePageNext()


style slot_button:
    xsize 244
    ysize 176
    background Frame("gui_gen/slot.png", 14, 14)
    hover_background Frame("gui_gen/slot_hover.png", 14, 14)
    padding (12, 12)

style thumb_box:
    background Frame("gui_gen/thumb_frame.png", 8, 8)
    padding (3, 3)

style slot_time_text:
    size 15
    color "#8A9099"
    xalign 0.5

style page_button is title_button:
    xsize 150
    padding (16, 10)

style page_button_text is title_button_text:
    size 18


################################################################################
# 设置
################################################################################

screen preferences():
    tag menu
    use game_menu("设置"):
        vbox:
            spacing 22

            # ---- 文本 ----
            hbox:
                spacing 10
                add Solid("#E3B457") xysize (4, 22)
                text "文本" style "pref_section_text"

            vbox:
                spacing 8
                text "文字速度" style "pref_label"
                bar value Preference("text speed") xsize 460 style "pref_bar"

            vbox:
                spacing 8
                text "自动前进间隔" style "pref_label"
                bar value Preference("auto-forward time") xsize 460 style "pref_bar"

            # ---- 音量 ----
            hbox:
                spacing 10
                add Solid("#E3B457") xysize (4, 22)
                text "音量" style "pref_section_text"

            hbox:
                spacing 20
                vbox:
                    spacing 12
                    hbox:
                        spacing 16
                        text "音乐" style "pref_label_sub" yalign 0.5
                        bar value Preference("music volume") xsize 280 style "pref_bar"
                    hbox:
                        spacing 16
                        text "音效" style "pref_label_sub" yalign 0.5
                        bar value Preference("sound volume") xsize 280 style "pref_bar"
                    hbox:
                        spacing 16
                        text "语音" style "pref_label_sub" yalign 0.5
                        bar value Preference("voice volume") xsize 280 style "pref_bar"

            # ---- 显示 ----
            hbox:
                spacing 10
                add Solid("#E3B457") xysize (4, 22)
                text "显示" style "pref_section_text"

            hbox:
                spacing 20
                textbutton "窗口 / 全屏" action Preference("display", "toggle") style "pref_tog"
                textbutton "跳过未读文本" action Preference("skip", "toggle") style "pref_tog"


style pref_section_text:
    size 22
    color "#EAEAEA"
    yalign 0.5

style pref_label:
    size 18
    color "#8A9099"

style pref_label_sub:
    size 17
    color "#8A9099"
    xsize 50

style pref_tog is title_button:
    xsize 230

style pref_tog_text is title_button_text:
    xalign 0.5

style pref_bar:
    xsize 460
    ysize 16
    left_bar Frame("gui_gen/bar_fill.png", 5, 5)
    right_bar Frame("gui_gen/bar_track.png", 5, 5)
    thumb Solid("#00000000")


################################################################################
# 历史记录
################################################################################

screen history():
    tag menu
    use game_menu("历史", scroll="viewport"):
        vbox:
            spacing 14

            if not _history_list:
                vbox:
                    xalign 0.5
                    spacing 12
                    text "暂无历史记录。" style "history_empty" xalign 0.5
                    text "开始阅读后，对话将在此按序留档。" xalign 0.5 size 15 color "#4E555E"

            for h in _history_list:
                frame:
                    style "history_item"
                    xfill True

                    vbox:
                        spacing 6

                        if h.who:
                            hbox:
                                spacing 10
                                add Solid("#7FB3D5") xysize (3, 16) yalign 0.5
                                text h.who style "history_name_text" yalign 0.5

                        text h.what style "history_text"


style history_item:
    background Frame("gui_gen/hist_item.png", 12, 12)
    padding (20, 14)
    xsize 760

style history_text:
    size 21
    color "#C3C9D1"
    line_spacing 6
    xsize 712

style history_name_text:
    size 20
    color "#7FB3D5"

style history_empty:
    size 20
    color "#8A9099"
