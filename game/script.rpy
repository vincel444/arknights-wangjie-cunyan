# ============================================================
# 明日方舟：妄界存言 · 主流程
# 配置见 options.rpy ｜ 角色见 characters.rpy ｜ UI 见 screens.rpy / ui_extra.rpy
# ============================================================

# ---------- 免责声明 ----------
label splashscreen:
    scene black
    with Pause(0.5)
    show text _("非官方同人作品\n《明日方舟》版权归 上海鹰角网络 所有") with dissolve
    with Pause(2.0)
    hide text with dissolve
    return

# ---------- 入口 ----------
label start:
    jump mode_select

# ---------- 标题主菜单（引擎 return 后回到这里） ----------
label main_menu:
    call screen main_menu_title

# ---------- 模式选择 ----------
label mode_select:
    call screen mode_select_menu

    if _return == "main":
        jump chapter_select
    elif _return == "chara":
        jump chara_story
    elif _return == "archive":
        jump operator_archive
    elif _return == "collection":
        jump story_collection
    elif _return == "timeline":
        jump world_timeline
    elif _return == "dev":
        jump dev_roadmap
    else:
        return

# ---------- 干员档案（开发中占位） ----------
label operator_archive:
    call screen notice_screen("干员档案", "该模块正在开发中\n\n规划内容：\n干员立绘一览 · 档案文本 · 语音试听")
    jump mode_select

# ---------- 故事集（开发中占位） ----------
label story_collection:
    call screen notice_screen("故事集", "该模块正在开发中\n\n规划内容：\n活动故事 · 短篇集 · 世界观补充阅读")
    jump mode_select

# ---------- 时间线（开发中占位） ----------
label world_timeline:
    call screen notice_screen("时间线", "该模块正在开发中\n\n规划内容：\n泰拉纪年 · 大事件年表 · 剧情节点回溯")
    jump mode_select

# ---------- 角色剧情（列表在 chara_story.rpy） ----------
label chara_story:
    jump chara_story_menu

# ---------- 开发中内容一览（占位） ----------
label dev_roadmap:
    call screen notice_screen("正在开发", "即将上线：\n\n· 角色剧情模式\n· 档案 / 干员资料库\n· 多结局分支系统\n· 语音与动态立绘")
    jump mode_select

# ---------- 章节调度 ----------
label chapter_select:
    menu:
        "第一章":
            jump ch1_opening
        "返回模式选择":
            jump mode_select

# ============================================================
# 第一章 · 垂直切片（占位剧本，等待正式剧本替换）
# ============================================================
label ch1_opening:
    scene black with fade
    n "罗德岛本舰，深夜。"
    n "走廊的应急灯把地面切成明暗相间的条纹，矿石病防护提示在舱门上缓慢闪烁。"
    scene bg corridor with dissolve
    show amiya neutral at center with dissolve
    a "博士，你还没休息吗？"
    menu:
        "「睡不着，出来走走。」":
            $ trust_akamiya += 1
            a "那我陪你走一段吧。"
        "「工作还没做完。」":
            a "……你总是这样。身体是革命的本钱，博士。"
    a "凯尔希医生说，明天有一场新的行动。她要我转告你——"
    show kalse neutral at right with easeinright
    k "阿米娅，把话说完之前，不要替别人下结论。"
    k "博士，明早六点，作战会议室。详情到时候再谈。"
    hide kalse with easeoutright
    n "她转身离开，白大褂的下摆消失在走廊尽头。"
    a "……那，晚安，博士。"
    hide amiya with dissolve
    scene black with fade
    call end_card("第一章 · 完")
    jump mode_select

# ---------- 通用结束卡（章节 / 角色剧情共用） ----------
label end_card(card_text):
    show screen chapter_end_card(card_text) with dissolve
    $ renpy.pause(1.5)
    pause
    hide screen chapter_end_card with dissolve
    return
