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
