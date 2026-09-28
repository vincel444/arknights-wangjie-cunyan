# ============================================================
# 故事集模块
# 结构：故事列表（screens.rpy 的 story_collection_list）→ 详情页 → 逐句阅读
# 新增故事：① 在 screens.rpy 的 story_collection_list 里加一张 story_card
#           ② 在此文件加正文数据与对应 label，命名规范 story_<拼音>
# 说明：故事文案由作者提供，AI 不代写；排版只做呈现，不改动原文
# ============================================================

init python:
    def story_quote(s):
        """呈现层加中文引号：正文数据保持原文，一字不改"""
        return u"\u201c%s\u201d" % s


# 逐句阅读的游标（显式声明，便于存档 / 回滚）
default story_play_i = 0


# ---------- 阅读页进入动效 ----------
transform story_fade:
    alpha 0.0
    linear 0.7 alpha 1.0


# ---------- 逐句阅读：每句淡入上浮 ----------
transform story_line_in:
    alpha 0.0
    yoffset 12
    linear 0.40 alpha 1.0 yoffset 0.0


################################################################################
# 如您亲启 · 正文（作者原文，逐行居中对齐）
################################################################################

define rnqq_lines = [
    "我已经不记得你了",
    "可我的手却用无比熟悉的方式写出这封信",
    "就好像曾无数次如此将我寄向你",
    "记忆就像是飞鸟",
    "我已经看不清他们在何处飞翔",
    "或许现下正吃的饭却是前天的事",
    "我像一个幽灵在生活中游荡",
    "可我却无数次梦到",
    "我梦到了什么呢？",
    "我看不清你",
    "我听不清你",
    "我触碰不到你",
    "可我的身体却写下这些",
    "这封回念会寄向何方",
    "我甚至不记得我在什么时候写下了地址",
    "你是谁？",
    "我……又是谁？",
]


################################################################################
# 详情页（居中排版 + 滚动预览 + 开始阅读）
################################################################################

screen story_reader(stitle, lines, stitle_en=""):
    add "gui_gen/bg_main.png"

    # 整页作为一块纵向居中排版，避免各元素绝对定位互相压盖
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        at story_fade

        # ---- 标题区 ----
        vbox:
            xalign 0.5
            spacing 12

            text stitle:
                xalign 0.5
                size 34
                kerning 6
                color C_TEXT

            add "gui_gen/deco_line.png" xalign 0.5 xysize (420, 11)

            if stitle_en:
                text stitle_en:
                    xalign 0.5
                    size 11
                    kerning 7
                    color "#3E464F"

        # ---- 主行动：开始阅读 ----
        textbutton "开始阅读":
            style "story_cta"
            xalign 0.5
            action Return("read")

        # ---- 正文预览（超出时滚动；高度取整行数，避免末行被裁一半）----
        viewport:
            xalign 0.5
            xsize 820
            ysize min(298, len(lines) * 52 - 14)
            mousewheel True
            draggable True

            vbox:
                xsize 820
                spacing 14

                # 每行放进定宽容器再居中——Text 默认收缩宽度，直接 text_align 不生效
                for ln in lines:
                    fixed:
                        xsize 820
                        ysize 38

                        text story_quote(ln):
                            xalign 0.5
                            yalign 0.5
                            size 25
                            color "#C9CFD7"

        text "滚轮 / 拖动浏览全文":
            xalign 0.5
            size 12
            color "#414A54"

    textbutton "← 返回故事集":
        style "mode_back"
        xalign 0.5
        yalign 0.955
        action Return("back")


################################################################################
# 逐句阅读页（沉浸模式：单击推进）
################################################################################

screen story_play(stitle, lines, idx):
    # 注意：不加 modal——call screen 场景下无下层交互，加了反而会吞掉
    # 事件层（曾导致自动化 pause 卡死）。返回详情按钮即为唯一出口。
    add "gui_gen/bg_main.png"

    # 透明全屏点击区：单击 / 空格 进入下一句；文字不可聚焦，点击会落到这层
    button:
        style "story_click"
        xfill True
        yfill True
        action Return("next")

    # ---- 左上：返回详情页 ----
    textbutton "← 返回详情":
        style "mode_back"
        xpos 26
        ypos 18
        action Return("exit")

    # ---- 顶部居中：篇名 · 进度 ----
    hbox:
        xalign 0.5
        ypos 40
        spacing 14

        text stitle:
            yalign 0.5
            size 14
            kerning 5
            color "#525C68"

        add Solid("#2C343E") xysize (1, 12) yalign 0.5

        text "%02d / %02d" % (idx + 1, len(lines)):
            yalign 0.5
            size 14
            kerning 3
            color C_ACCENT

    add "gui_gen/deco_line.png" xalign 0.5 ypos 72 xysize (300, 11) alpha 0.55

    # ---- 中央：当前句 ----
    fixed:
        xalign 0.5
        yalign 0.48
        xsize 1080
        ysize 220

        text story_quote(lines[idx]):
            xalign 0.5
            yalign 0.5
            xmaximum 1080
            xminimum 1080
            text_align 0.5
            line_spacing 16
            size 40
            color "#EDEFF2"
            at story_line_in

    # ---- 底部：进度条 + 操作提示 ----
    vbox:
        xalign 0.5
        yalign 0.90
        spacing 12

        fixed:
            xalign 0.5
            xsize 420
            ysize 2

            add Solid("#232A33") xysize (420, 2)
            add Solid(C_ACCENT) xysize (int(420 * (idx + 1) / len(lines)), 2)

        text ("单击继续  ·  空格 / 回车同样有效" if idx < len(lines) - 1 else "单击结束本篇"):
            xalign 0.5
            size 12
            kerning 2
            color "#3B434D"


################################################################################
# 阅读完毕
################################################################################

screen story_end(stitle):
    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.42
        spacing 16
        at story_fade

        text "— 完 —":
            xalign 0.5
            size 24
            kerning 10
            color "#8A9099"

        add "gui_gen/deco_line.png" xalign 0.5 xysize (280, 11)

        text stitle:
            xalign 0.5
            size 14
            kerning 5
            color "#454E58"

    textbutton "← 返回故事集":
        style "mode_back"
        xalign 0.5
        yalign 0.60
        action Return("back")


################################################################################
# 故事集入口
################################################################################

label story_collection_menu:
    call screen story_collection_list

    if _return == "rnqq":
        jump story_rnqq
    else:
        jump mode_select


# ---------- 如您亲启 ----------
label story_rnqq:
    call screen story_reader("如您亲启", rnqq_lines, "A LETTER FOR YOU TO OPEN")

    if _return == "read":
        jump story_play_rnqq

    jump story_collection_menu


label story_play_rnqq:
    $ story_play_i = 0

    while story_play_i < len(rnqq_lines):
        call screen story_play("如您亲启", rnqq_lines, story_play_i)

        if _return == "exit":
            jump story_collection_menu

        $ story_play_i += 1

    call screen story_end("如您亲启")
    jump story_collection_menu
