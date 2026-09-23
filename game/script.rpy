# ============================================================
# 明日方舟同人剧情 AVG - 主脚本
# 结构：init 配置 → 角色定义 → 章节调度 → 第一章（垂直切片）
# ============================================================

# ---------- 基础配置 ----------
define config.name = _("明日方舟：妄界存言")
define gui.show_name = True
define config.version = "0.1.0"
define gui.about = _("\n非官方同人作品。《明日方舟》版权归鹰角网络所有。\n本作品为非商业同人创作，仅供学习交流。")
define build.name = "WangjieCunyan"

# 窗口图标暂缺，接入美术素材后再配置：define config.window_icon = "gui/window_icon.png"
define config.has_autosave = True
define config.autosave_slots = 3
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

# 1280x720 起步，方舟剧情界面是 16:9
define config.screen_width = 1280
define config.screen_height = 720

# ---------- 字体：默认 DejaVuSans 无中文字形，全局替换为微软雅黑 ----------
# 手搓骨架不走 gui.init 模板构建，gui.* 变量不生效，改用样式层直接覆盖：
style default:
    font "fonts/msyh.ttc"

# 替换映射：兜底所有引用 DejaVuSans 的内置样式（界面按钮/输入框/菜单等）
# 注意：值必须是 (字体, 粗体, 斜体) 三元组，不能只写字符串
define config.font_replacement_map = {
    ("DejaVuSans.ttf", False, False): ("fonts/msyh.ttc", False, False),
    ("DejaVuSans.ttf", True, False): ("fonts/msyh.ttc", True, False),
    ("DejaVuSans.ttf", False, True): ("fonts/msyh.ttc", False, True),
    ("DejaVuSans.ttf", True, True): ("fonts/msyh.ttc", True, True),
}

# ---------- 角色定义（占位，后续按正式剧本补全） ----------
# who=None 是旁白；颜色后续与干员主题色对齐
define a = Character(_("阿米娅"), color="#64C1E8", who_outlines=[(1, "#00000080")])
define k = Character(_("凯尔希"), color="#5DBB6B", who_outlines=[(1, "#00000080")])
define d = Character(_("博士"), color="#E0E0E0", who_outlines=[(1, "#00000080")])
define n = Character(None, what_color="#DDDDDD", what_outlines=[(1, "#00000080")])

# ---------- 游戏状态（章节/好感等全局变量） ----------
default chapter = 1
default trust_akamiya = 0   # 占位：角色信赖值，供分支使用

# ---------- 入口 ----------
label splashscreen:
    scene black
    with Pause(0.5)
    show text _("非官方同人作品\n《明日方舟》版权归 上海鹰角网络 所有") with dissolve
    with Pause(2.0)
    hide text with dissolve
    return

label start:
    jump ch1_opening

# ---------- 标题主菜单（引擎 return 后回到这里） ----------
label main_menu:
    call screen main_menu_title

# ---------- 模式选择（开始游戏后进入） ----------
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
# 第一章 · 垂直切片（占位剧本，验证流程与演出）
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
    call ch1_end
    jump mode_select

# 第一章结束卡：强制停留，点击后才返回
label ch1_end:
    call end_card("第一章 · 完")
    return

# 通用结束卡（章节 / 角色剧情共用）
label end_card(card_text):
    show screen chapter_end_card(card_text) with dissolve
    $ renpy.pause(1.5)
    pause
    hide screen chapter_end_card with dissolve
    return
