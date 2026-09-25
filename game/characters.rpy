# ============================================================
# 角色定义 / 全局状态变量
# 新增角色：在下方加 define，并在 script.rpy 或 chara_story.rpy 中使用
# ============================================================

# ---------- 主要角色 ----------
# ctc 与动效见 ui_extra.rpy
# who=None 表示旁白；color 为角色名颜色，后续与干员主题色对齐
define a = Character(_("阿米娅"), color="#64C1E8", who_outlines=[(1, "#00000080")],
                     ctc="ctc_arrow", ctc_position="nestled")
define k = Character(_("凯尔希"), color="#5DBB6B", who_outlines=[(1, "#00000080")],
                     ctc="ctc_arrow", ctc_position="nestled")
define d = Character(_("博士"), color="#E0E0E0", who_outlines=[(1, "#00000080")],
                     ctc="ctc_arrow", ctc_position="nestled")
define n = Character(None, what_color="#DDDDDD", what_outlines=[(1, "#00000080")],
                     ctc="ctc_arrow", ctc_position="nestled")

# ---------- 全局状态 ----------
default chapter = 1
default trust_akamiya = 0   # 阿米娅信赖值（分支用）
