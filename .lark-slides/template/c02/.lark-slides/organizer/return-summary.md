# Organizer 影子审查 · 收尾回报（27赛季培训计划 · 电控组第二讲）

- deck: `F0JnsLJyVl4EyOdihVacpfKEnYd`（https://my.feishu.cn/slides/F0JnsLJyVl4EyOdihVacpfKEnYd）
- 最终状态：rev=83、slides=24、errs=266、warns=1
- 本轮（round 12）覆盖页：P15~P24；此前轮次已闭环：P1~P14
- 审查方法：A `template_lint_all.py`（必带 `--page-role`）+ B 逐页 `+screenshot` 亲自 Read + C fixed_template 对 `source-slides/`、active_rebuild 对 `content-skeletons/` 的 brand_assets 清单 + D 目录/章节/角标一致性 + E 不适用（`is_manuscript_apply=false`）

## 一、全稿两个系统性 P0（已全部修完并写入服务端）

1. **角标 = 章节号，不是页码**。`tpl_index.py` 扫模板 29 页证明：slide-05/06/07 全为 `01`、slide-09/10=`02`、slide-12/13/14=`03`、slide-16~28=`04`，章节页不带角标。修正后的角标分布：P5/6/7=`01`，P9/10/11=`02`，P13/14/15=`03`，P17~P23=`04`。
2. **页眉『哈理工A.I.R.创新实验室』几何被写坏**：原写 `(705.6155, 48, 160×32)` + `wrap="false"`（可用宽仅 145.6px，文字估算 175.44px → 每页必然 `text_may_overflow_shape`），已还原为模板原生 `(705.6155118110237, 54.487716535433066, 548.2546456692913×21.560551181102362)` + `letterSpacing 1.1` + 斜体。

## 二、本轮 refine 清单（active_rebuild 页 · shape 数 before → after）

| 页 | slide_id | before → after | refine 动作 |
|---|---|---|---|
| P15 | pfA | 18 → 21 | L1：左栏三条要点编号化（20×20 深蓝方块 1./2./3.，文本 x62.42→90.42、宽 430→402，标题 18→20px） |
| P17 | pfX | 21 → 24 | L3：步骤条 3×竖装饰条 4×40 主色 @x56.42 + 代码框边距对齐内容边距（x74.42/793 → x62.42/817.58） |
| P18 | pfl | 21 → 24 | L3（同 P17） |
| P19 | pfr | 21 → 24 | L3（同 P17） |
| P20 | pfs | 21 → 24 | L3（同 P17） |
| P21 | pfo | 18 → 21 | L1 变体：编号方块放左栏外侧 x40.42（文本容量实测需 ≥409.6px，压缩到 387.6 会触发 unexpected_wrapping×2，故不动文本） |
| P22 | pfv | 21 → 25 | L3：步骤竖条 ×4 |
| P23 | pfS | 23 → 28 | L3：步骤竖条 ×5 + 第 04 条正文补回 page-plan 要求的『以附件形式发送到指定邮箱』（内容取自培训计划 md，未编造） |

（P5 18→23、P6 18→21、P7 18→21、P9 18→21、P10 14→15、P11 16→16（列宽重排+字号 16→15）、P13 18→21、P14 18→21 为前几轮已完成，见 audit-r10.jsonl 与 current-round-11/。）

**未 refine 的 active_rebuild 页：无。** 19 个 active_rebuild 页（P5~P7、P9~P11、P13~P15、P17~P23）全部至少完成 1 次 refine；多数页 `refine_triggers` 由 1~2 项命中变为 5/5 全过（如 P15 hit=2→0、P17/18/19/20 hit=1→0、P21 hit=2→0）。
fixed_template 页（P1/P2/P3/P4/P8/P12/P16/P24）按规程只修 bug、不做 refine。

## 三、本轮修过的 bug（非 refine）

- P15/P17~P23：角标改章节号 + 页眉几何还原（见上）。
- P16（章节页）：曾尝试把标题改为与 P3 目录一致的『04数组·字符串·结构体·指针』，渲染出现「行首分隔符 / 拆段后截断」→ 判定为对固定模板页的过度修改，**已回滚为原稿文本**，专注修 bug 原则。
- P23：第 1 次写入时把步骤行整段替换（该页 L3 行的标题段与正文段同在一个 text shape），导致标题被正文覆盖 → 已从 `full.xml` 原始切片重做，仅改含「例如」的正文段（spans=1）。
- P22：作业 2 四道题与 `27赛季培训计划.md` 第 63–74 行逐字比对一致；P23 的五条提交要求与第 42–49 行比对一致（UTF-8 注释、一个压缩包、班级+姓名+第几次任务、指定邮箱/附件、考核前交齐）。

## 四、已知豁免项（模板固有 / 启发式误报，均经截图确认）

- 模板装饰组固有的 `shape_out_of_canvas`（含页眉文本框本身按模板原生几何就出画布 293.87px——这是模板缺陷，但还原几何后渲染位置正确，比原来 160px 宽的错误几何更对）。
- `text_overflows_container`（页眉/标题/步骤编号 vs 模板的全画布 custom 形状）、`bbox_overlap`（模板右下角装饰 vs 「本页判断」色带，intersection 832.896px²，与本次改动无关）。
- 各页 `overflow_covers_below`（文本框高 40px 而 36px 字形估算需 63px 的启发式误报，可见字形并不重叠）。
- P8/P12/P16/P24 的 `黑体` 字体（模板原生，见 source-slides/slide-04.xml）。
- P3 的 `text_may_overflow_shape[bRq]`、`text_color_contrast` WARN；P4 的 `unexpected_wrapping[bMu]`；P16 改写前的 `unexpected_wrapping`（现渲染为 2 行、落在蓝色斜带内可读）。

## 五、诚实标注的局限

1. **P18/P19/P20/P22 的服务端渲染缓存未刷新**：这 4 页在写入后连续 4 次 `+screenshot` 返回的 jpeg 字节数与修复前完全一致（177473/187563/168214/196345），而 `+xml-get` 证实服务端已是新版本（element_count 24/24/24/25 = 修复前 +3/+3/+3/+4 竖条，revision 81→83）。因此这 4 页的**最终视觉**改用结构核对（`vfy.py`：角标文字、竖条数量、元素总数）+ 同版式族页面（P17/P23）的新截图验证，未取得这 4 页自身的新截图。
2. 本轮未使用 enrich subagent（`is_manuscript_apply=false`，且用户已提供完整培训计划），enrich 素材全部来自 `27赛季培训计划.md` 与模板 source，无编造。
3. 工具链均留在 `D:\桌面\培训\.lark-slides\template\c02\.lark-slides\organizer\`：`mk_pages.py`（批量生成修订版，JOBS 含 mode=l1/l1g/l2syn/l2tab/l3/l3e23）、`lintnew.py`、`det.py`、`vfy.py`、`poll.py`、`slice.py`、`geo.py`、`tab.py`、`crop.py`、`batch.py`、`check_content.py`、`dump.py`、`cmp.py`、`tpl_index.py`。
4. 审查记录：`audit-r1/r3/r5/r6/r10/r12.jsonl`（`audit-r12.jsonl` 覆盖 P15~P24）。
