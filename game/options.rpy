# ============================================================
# 项目配置 / 全局字体
# 说明：本文件只放引擎级配置，剧情内容见 script.rpy / chara_story.rpy
# ============================================================

# ---------- 基本信息 ----------
define config.name = _("明日方舟：妄界存言")
define config.version = "0.1.0"
define gui.about = _("\n非官方同人作品。《明日方舟》版权归鹰角网络所有。\n本作品为非商业同人创作，仅供学习交流。")
define build.name = "WangjieCunyan"

# ---------- 画面 ----------
define config.screen_width = 1280
define config.screen_height = 720
define config.thumbnail_width = 320
define config.thumbnail_height = 180
define config.check_conflicting_properties = True

# ---------- 存档 ----------
define config.has_autosave = True
define config.autosave_slots = 3
define config.has_quicksave = True

# ---------- 图层 ----------
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

# 窗口图标暂缺，接入美术素材后再配置：define config.window_icon = "gui/window_icon.png"

# 按 Esc/右键直接打开保存界面（左侧导航可切换到读档/设置/历史）
define config.game_menu_action = ShowMenu("save")

# 游戏中常驻的状态提示层（快进中 / 自动播放中）
init python:
    if "play_state_indicator" not in config.overlay_screens:
        config.overlay_screens.append("play_state_indicator")

    # 引擎内置提示语汉化（退出确认、覆盖存档、读档提示等）
    layout.ARE_YOU_SURE = "确定吗？"
    layout.DELETE_SAVE = "确定要删除这个存档吗？"
    layout.OVERWRITE_SAVE = "确定要覆盖这个存档吗？"
    layout.LOADING = "读取存档将丢失未保存的进度。\n确定要继续吗？"
    layout.QUIT = "确定要退出游戏吗？"
    layout.MAIN_MENU = "确定要返回标题画面吗？\n未保存的进度将丢失。"
    layout.CONTINUE = "确定要从上次离开的地方继续吗？"
    layout.END_REPLAY = "确定要结束回放吗？"
    layout.SLOW_SKIP = "确定要开始快进阅读吗？"
    layout.FAST_SKIP_SEEN = "确定要快进到下一个选项吗？"
    layout.FAST_SKIP_UNSEEN = "确定要跳过未读文本，直达下一个选项吗？"

# ---------- 默认偏好（新玩家首次进游戏的初值） ----------
define config.default_text_cps = 45
define config.default_afm_time = 12

# ============================================================
# 全局字体：默认 DejaVuSans 无中文字形，替换为微软雅黑
# 手搓骨架不走 gui.init 模板构建，因此用样式层直接覆盖
# ============================================================
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
