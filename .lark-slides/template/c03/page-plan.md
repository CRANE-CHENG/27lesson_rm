# 电控组第三讲 · STM32①（GPIO、按键与外部中断）施工清单

Style: learning-and-training
Deck: MRoTswOBPlNnMYdGxFdc7xJTnZc
URL: https://my.feishu.cn/slides/MRoTswOBPlNnMYdGxFdc7xJTnZc
WORK_DIR: D:\桌面\培训\.lark-slides\template\c03
模板：电控组c语言培训第一讲.pptx（29 页，第二讲同款视觉）——沿用深蓝 rgba(3,72,149,1) / 亮蓝 / 浅灰几何风、思源黑体正文、Consolas 代码、锐字真言体编号。

课程事实来源：《27赛季培训计划.md》第 8 周（10月24日）STM32①。
- 本节重点：工程建立、GPIO 输入输出、LED、上下拉、EXTI、按键消抖
- 课后成果：完成按键控制 LED 并能处理按键抖动

## 版式基线（沿用第二讲已定稿三型）
- **L1「要点+代码」**：左栏 3 个要点块 width=430 height=60，topLeftY = 124/194/264；右栏代码底板 width=378 height=230~240 @ (510,112)（fill rgba(240,240,240,1) + border 深蓝 1），代码文本 width=354 height=224 @ (522,120)（Consolas 16，lineSpacing 1.35）；底部结论条 rect+text 817.58×32 @ (62.42,372)，深蓝底白字。
- **L2「表格对比」**：table width=828 @ topLeftX=62.42，表头深蓝底白字粗体，td borderTop 深蓝 width=1，底部结论条同 L1。
- **L3「编号步骤条」**：编号块 56×40 @ x=62.42（y = 100/156/212 三条版；118/186/254/322/366 五条版），编号 28px 锐字真言体 深蓝；正文块 width=752~758 height=44~64 @ x=124，首行 17~18px 深蓝粗体 + 次行 15px 正文；底部结论条 @ y=396（五条版 428）。

## 硬性技术规则（第二讲踩坑所得，本讲沿用）
1. 标题一律深蓝 rgba(3,72,149,1)（模板原白字在白底不可见，是有意修复）。
2. 代码块内函数名用 rgba(140,70,190,1)（模板原 210,168,255 在浅灰底会被对比度检查阻断）。
3. 编号块 y ≥ 118 且不与左上深蓝三角 bUs(0,0,141.14×116.86) 区域重叠，否则报 text_color_contrast。
4. 文字拆成多个小 shape，代码底板与代码文本框不重合，避免 dominated_by_paragraphs / text_overflow_covers_below。
5. 每页 `本页判断：…` 结论条；每页 note 写 3–5 句中文讲稿。

## 页面清单（共 24 页）

| 目标页 | 页形 | 策略 | 来源模板页 | 本页判断 / 内容要点 |
|---|---|---|---|---|
| P1 | cover | fixed_template | 01 | 电控组第三讲 / 培训时间：第8周 10.24　主讲人：＿＿＿＿＿ / 『生无所息，斗无所止』 |
| P2 | 计划表 | fixed_template | 02 | 保留模板 raster 计划表截图，标题改深蓝+思源黑体，note 换讲稿 |
| P3 | toc | fixed_template | 03 | 01 工程建立与 GPIO 输出 / 02 GPIO 输入与按键 / 03 按键消抖 / 04 外部中断 EXTI |
| P4 | chapter01 | fixed_template | 04 | 01 工程建立与 GPIO 输出 |
| P5 | content | active_rebuild | 16 | L1 从写 C 到点灯，中间多了什么（工具链/寄存器/HAL 库） |
| P6 | content | active_rebuild | 16 | L1 用 CubeMX 建一个能跑的工程：五步走完 |
| P7 | content | active_rebuild | 16 | L1 第一次点灯：HAL_GPIO_WritePin / TogglePin |
| P8 | chapter02 | fixed_template | 04 | 02 GPIO 输入与按键 |
| P9 | content | active_rebuild | 16 | L1 按键接到哪：上拉、下拉与「按下读到 0」 |
| P10 | content | active_rebuild | 16 | L2 表格 GPIO 四种输入模式对比（浮空/上拉/下拉/模拟） |
| P11 | content | active_rebuild | 16 | L1 HAL_GPIO_ReadPin 读按键，以及为什么不能直接信它 |
| P12 | chapter03 | fixed_template | 04 | 03 按键消抖 |
| P13 | content | active_rebuild | 16 | L1 抖动从哪来：一次按下被读成十几次 |
| P14 | content | active_rebuild | 16 | L2 表格 消抖方案对比（裸延时 / 状态机 / 定时器） |
| P15 | content | active_rebuild | 16 | L1 延时消抖与状态机消抖代码 |
| P16 | chapter04 | fixed_template | 04 | 04 外部中断 EXTI |
| P17 | content | active_rebuild | 16 | L3 中断是什么：CPU 被打断的五个步骤 |
| P18 | content | active_rebuild | 16 | L1 CubeMX 配 EXTI 与回调函数 HAL_GPIO_EXTI_Callback |
| P19 | content | active_rebuild | 16 | L1 中断里能做与不能做的事 |
| P20 | content | active_rebuild | 16 | L2 表格 轮询 vs 中断 |
| P21 | content | active_rebuild | 16 | L3 本节易错清单（五条版） |
| P22 | content | active_rebuild | 16 | L3 课后作业 3（四题，原文逐字） |
| P23 | content | active_rebuild | 16 | L3 交作业之前先过一遍这五条（提交要求，原文口径） |
| P24 | ending | fixed_template | 29 | 下课啦！ |
