# -*- coding: utf-8 -*-
"""作业文件夹三层结构重排脚本：
作业/个人文件夹(专业-班级-姓名)/第一次作业/第X次提交/
先打印计划（dry-run），确认后执行。
"""
import os, shutil, sys

ROOT = r"D:\桌面\培训\作业"
TMP = r"D:\桌面\培训\_新包临时"

# ---------------- 计划定义 ----------------
# 1) 已有文件夹重排：个人文件夹 -> (原顶层内容移入 第一次作业/第一次提交/)
#    特殊：已有"第一次提交/第二次提交"结构的，整体移入 第一次作业/
# 2) 新同学：新文件夹/第一次作业/第一次提交/ <- 临时解压内容
# 3) 已有同学新提交：移入 个人文件夹/第一次作业/第X次提交/

PLAN = []

def plan_move(src, dst, desc):
    PLAN.append((src, dst, desc))

# ---------- 已有 22 人重排 ----------
# 常规：顶层内容 -> 个人文件夹/第一次作业/第一次提交/
regular = [
    "孟繁志",
    "机器人工程-26-1-段少龙",
    "机械-大珩-刘飞扬",
    "机电-26-2-曹奥华",
    "测控-26-3-刘永鹏",
    "测控-26-3-唐俊毅",
    "测控-26-3-顾柳霖",
    "测控-26-6-郝欣如",
    "电信-26-1-田晓宁",
    "电气-26-10-王子豪",
    "电气-26-14-王璟",
    "电气-26-3-殷浩然",
    "电气-26-9-周泽宇",
    "电气-26-9-黄竟轩",
    "自动化-26-2-陈梦祺",
    "自动化-26-5-程义硕",
    "车辆-26-3-刘博宇",
]
for name in regular:
    p = os.path.join(ROOT, name)
    if not os.path.isdir(p):
        continue
    first = os.path.join(p, "第一次作业", "第一次提交")
    for item in os.listdir(p):
        if item == "第一次作业":
            continue
        s = os.path.join(p, item)
        d = os.path.join(first, item)
        plan_move(s, d, f"[常规] {name}: {item}")

# 已有 第一次提交/第二次提交 结构的（郑瀚、刘明远）：整体移入 第一次作业/
nested = ["测控-26-4-郑瀚", "电信-26-4-刘明远"]
for name in nested:
    p = os.path.join(ROOT, name)
    if not os.path.isdir(p):
        continue
    for item in os.listdir(p):
        if item == "第一次作业":
            continue
        s = os.path.join(p, item)
        d = os.path.join(p, "第一次作业", item)
        plan_move(s, d, f"[嵌套] {name}: {item}")

# 宋文松：已有内容 -> 第一次提交
p = os.path.join(ROOT, "机器人工程-26-1-宋文松")
for item in os.listdir(p):
    if item == "第一次作业":
        continue
    s = os.path.join(p, item)
    d = os.path.join(p, "第一次作业", "第一次提交", item)
    plan_move(s, d, f"[宋文松] {item}")

# 李韩煦：文件夹名规范化 + 内容移入
lhx_old = os.path.join(ROOT, "集成26-1李韩煦")
lhx_new = os.path.join(ROOT, "集成-26-1-李韩煦")
if os.path.isdir(lhx_old):
    plan_move(lhx_old, lhx_new, "[李韩煦] 文件夹更名 集成26-1李韩煦 -> 集成-26-1-李韩煦")
    if os.path.isdir(lhx_new):
        for item in os.listdir(lhx_new):
            if item == "第一次作业":
                continue
            s = os.path.join(lhx_new, item)
            d = os.path.join(lhx_new, "第一次作业", "第一次提交", item)
            plan_move(s, d, f"[李韩煦] {item}")

# ---------- 新同学（新建文件夹） ----------
new_students = {
    "储能-26-2-蔡一炜": r"储能26_2班_蔡一炜_第一次任务\储能26-2班+蔡一炜+第一次任务",
    "机器人工程-26-2-何青铄": r"机器人工程26_2何青铄_1",
    "机电-26-1-姚硕": r"机电26_1班_姚硕_第一次任务",
    "测控-26-5-刘岳": r"测控26_5班刘岳第1次任务\测控26-5班刘岳第1次任务",
    "电气-26-8-任宏杰": r"电气26_8班_任宏杰_第一次任务",
    "集成-26-1-李壮": r"集成26_1李壮第一次任务",
}
for name, sub in new_students.items():
    src_dir = os.path.join(TMP, sub)
    if not os.path.isdir(src_dir):
        print(f"!! 新同学源目录不存在: {src_dir}")
        continue
    first = os.path.join(ROOT, name, "第一次作业", "第一次提交")
    # 源内顶层内容整体移入（若源内只有一个顶层目录则移入其内容）
    top_items = os.listdir(src_dir)
    if len(top_items) == 1 and os.path.isdir(os.path.join(src_dir, top_items[0])):
        inner = os.path.join(src_dir, top_items[0])
        for item in os.listdir(inner):
            s = os.path.join(inner, item)
            d = os.path.join(first, item)
            plan_move(s, d, f"[新同学] {name}: {item}")
    else:
        for item in top_items:
            s = os.path.join(src_dir, item)
            d = os.path.join(first, item)
            plan_move(s, d, f"[新同学] {name}: {item}")

# ---------- 已有同学的新提交 ----------
second_submits = {
    # 宋文松 (1).zip -> 第二次提交
    "机器人工程-26-1-宋文松": [
        (r"机器人工程26_1宋文松第一次任务_1_\机器人工程26-1宋文松第一次任务", "第二次提交"),
    ],
    # 曹奥华 (1).zip -> 第二次提交；空格版 -> 第三次提交
    "机电-26-2-曹奥华": [
        (r"机电26_2曹奥华第一次作业_1_\机电26-2曹奥华第一次作业", "第二次提交"),
        (r"机电26_2曹奥华第一次作业_", "第三次提交"),
    ],
    # 左翔宇 -> 第二次提交
    "电气-26-13-左翔宇": [
        (r"电气26_13班_左翔宇_第一次任务\电气26-13班+左翔宇+第一次任务", "第二次提交"),
    ],
    # 程义硕 -> 第二次提交
    "自动化-26-5-程义硕": [
        (r"自动化26_5程义硕第一次作业", "第二次提交"),
    ],
}
for name, pairs in second_submits.items():
    p = os.path.join(ROOT, name)
    if not os.path.isdir(p):
        print(f"!! 已有同学文件夹不存在: {p}")
        continue
    for sub, subdir in pairs:
        src_dir = os.path.join(TMP, sub)
        if not os.path.isdir(src_dir):
            print(f"!! 新提交源不存在: {src_dir}")
            continue
        first = os.path.join(p, "第一次作业", subdir)
        top_items = os.listdir(src_dir)
        if len(top_items) == 1 and os.path.isdir(os.path.join(src_dir, top_items[0])):
            inner = os.path.join(src_dir, top_items[0])
            for item in os.listdir(inner):
                s = os.path.join(inner, item)
                d = os.path.join(first, item)
                plan_move(s, d, f"[{name} {subdir}] {item}")
        else:
            for item in top_items:
                s = os.path.join(src_dir, item)
                d = os.path.join(first, item)
                plan_move(s, d, f"[{name} {subdir}] {item}")

# ---------------- 执行或预览 ----------------
if len(sys.argv) > 1 and sys.argv[1] == "--execute":
    moved = 0
    errors = []
    for src, dst, desc in PLAN:
        if not os.path.exists(src):
            errors.append(f"源不存在: {src}")
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        try:
            shutil.move(src, dst)
            moved += 1
        except Exception as e:
            errors.append(f"{desc}: {e}")
    print(f"完成移动 {moved}/{len(PLAN)} 项")
    if errors:
        print("错误:")
        for e in errors:
            print(" ", e)
else:
    print(f"计划共 {len(PLAN)} 项移动：")
    for src, dst, desc in PLAN:
        print(f"  {desc}\n    {src}\n    -> {dst}")
