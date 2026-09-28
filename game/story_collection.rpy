# ============================================================
# 故事集模块
# 结构：故事列表（screens.rpy 的 story_collection_list）→ 各故事阅读页
# 新增故事：① 在 screens.rpy 的 story_collection_list 里加一张 story_card
#           ② 在此文件加正文数据与对应 label，命名规范 story_<拼音>
# 说明：故事文案由作者提供，AI 不代写；排版只做呈现，不改动原文
# ============================================================

# ---------- 阅读页进入动效 ----------
transform story_fade:
    alpha 0.0
    linear 0.7 alpha 1.0


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
# 通用故事阅读页（居中排版 + 滚动浏览）
################################################################################

screen story_reader(stitle, lines, stitle_en=""):
    add "gui_gen/bg_main.png"

    vbox:
        xalign 0.5
        yalign 0.055
        spacing 15
        at story_fade

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

    viewport:
        xalign 0.5
        yalign 0.55
        xsize 800
        ysize 450
        mousewheel True
        draggable True
        at story_fade

        vbox:
            xsize 800
            spacing 14

            # 每行放进定宽容器再居中——Text 默认收缩宽度，直接 text_align 不生效
            for ln in lines:
                fixed:
                    xsize 800
                    ysize 38

                    text ln:
                        xalign 0.5
                        yalign 0.5
                        size 25
                        color "#C9CFD7"

    # 滚动提示（内容超出视口时可见）
    text "滚轮 / 拖动浏览全文":
        xalign 0.5
        yalign 0.905
        size 12
        color "#414A54"

    textbutton "← 返回故事集":
        style "mode_back"
        xalign 0.5
        yalign 0.955
        action Return()


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
    jump story_collection_menu
