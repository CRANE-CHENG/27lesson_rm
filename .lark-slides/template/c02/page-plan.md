# page-plan · 电控组第二讲（C语言②）

Style: learning-and-training
模板: 电控组c语言培训第一讲.pptx（29 页）
WORD_DIR: D:\桌面\培训\.lark-slides\template\c02
deck: F0JnsLJyVl4EyOdihVacpfKEnYd  https://my.feishu.cn/slides/F0JnsLJyVl4EyOdihVacpfKEnYd
first_page_slide_id: pff

## 视觉基线（照搬模板，禁止新色族）
- 主色 深蓝 rgba(3,72,149,1) / 亮蓝 rgba(0,0,238,1) / rgba(0,0,171,249,1) 即 rgba(0,171,249,1)
- 正文 rgba(31,35,41,1) / 黑 rgba(0,0,0,1) / 浅灰 rgba(240,240,240,1) / 白
- 字体：正文与标题 思源黑体；代码 Consolas；角标数字 锐字真言体免费商用
- 内容页通用 chrome（全部内容页固定）：bUs/bUg/bUr/bUx/bUM/bee/bsN 装饰组 + bes 页眉 logo
  - 角标 `<shape type="text" topLeftX="33.255" topLeftY="15.769" width="66.95" height="50.8">` 白 36 锐字真言体免费商用 = 章节号
  - 标题 `<shape type="text" topLeftX="110.89" topLeftY="33.10" width="700" height="36.25">` 思源黑体 24 bold 深蓝
  - 页眉文字 `705.6155, 54.4877, 548.2546×21.5606` 思源黑体 14 黑 = "哈理工A.I.R.创新实验室"
  - 内容安全区：x 62~898，y 100~478
- 代码块：深灰字色分色 Consolas，示例
  - 关键字/函数符号 rgba(86,156,214,1)、函数名 rgba(210,168,255,1)、字符串引号与内容 rgba(165,214,255,1)、格式符 rgba(255,123,114,1)、转义 rgba(215,186,125,1)、符号灰 rgba(187,190,191,1)

## 版式基线
- **L1 要点+代码**（基线 P5）：左栏要点（rect 色块标题 + text 列表，x 62 / 宽 430），右栏代码框（shape type=text + border，x 510 / 宽 388）
- **L2 表格对比**（基线 P10）：table 宽 828，表头深蓝底白字 + 正文行；底部一条结论 text
- **L3 编号步骤条**（基线 P17）：整行 rect 承载行文字（y 111.75 起，行高 36 / 间隔 46）

## 页面清单

| 目标页 | 页形 | 页型策略 | 来源模板页 | 来源 XML | skeleton_ref | 使用的 style 内容 | 要填的新内容 |
|---|---|---|---|---|---|---|---|
| P1 | cover | fixed_template | slide-01 | source-slides/slide-01.xml | - | - | 主标题=电控组第二讲；副标语=『生无所息，斗无所止』；底部条=培训时间：第7周 10.17　主讲人：＿＿＿＿（留占位） |
| P2 | chapter(00) | fixed_template | slide-02 | source-slides/slide-02.xml | - | - | 标题=关于时间安排:（保留模板自带计划表图片 VjCYbiiDSo9uCKxsOiscYNuJnye） |
| P3 | toc | fixed_template | slide-03 | source-slides/slide-03.xml | - | - | 01 程序流程与分支 / 02 循环语句 / 03 函数 / 04 数组·字符串·结构体·指针 |
| P4 | chapter | fixed_template | slide-04 | source-slides/slide-04.xml | - | - | 01 程序流程与分支 |
| P5 | content | active_rebuild | slide-16 | - | - | L1 要点+代码（本页为 L1 基线） | 三种基本结构：顺序/选择/循环；为什么需要分支与循环；代码块演示顺序执行 |
| P6 | content | active_rebuild | slide-16 | - | P5 | L1 同 P5 | if / if-else / else-if 梯；条件表达式真假；单行省略大括号的坑 |
| P7 | content | active_rebuild | slide-16 | - | P5 | L1 同 P5 | switch-case：break 作用、default；什么时候用 switch 而不是 if |
| P8 | chapter | fixed_template | slide-04 | source-slides/slide-04.xml | - | - | 02 循环语句 |
| P9 | content | active_rebuild | slide-16 | - | P5 | L1 同 P5 | for 循环：三段式 init;cond;step、执行顺序、for 遍历数组 |
| P10 | content | active_rebuild | slide-16 | - | - | L2 表格对比（本页为 L2 基线） | while / do-while / for 三者对比表：语法、执行条件、最少执行次数、适用场景 |
| P11 | content | active_rebuild | slide-16 | - | P10 | L2 同 P10 | break / continue 对比表 + 死循环的三种成因 |
| P12 | chapter | fixed_template | slide-04 | source-slides/slide-04.xml | - | - | 03 函数 |
| P13 | content | active_rebuild | slide-16 | - | P5 | L1 同 P5 | 函数定义与调用：返回类型 函数名(形参){}、先声明后使用、main 的返回值 |
| P14 | content | active_rebuild | slide-16 | - | P5 | L1 同 P5 | 参数传递：值传递（形参是副本）vs 指针传递（改到实参）；返回值只能带回一个值 |
| P15 | content | active_rebuild | slide-16 | - | P5 | L1 同 P5 | 作用域与生命周期：局部/全局/静态；变量重名与初始化陷阱 |
| P16 | chapter | fixed_template | slide-04 | source-slides/slide-04.xml | - | - | 04 数组、字符串、结构体与指针 |
| P17 | content | active_rebuild | slide-16 | - | - | L3 编号步骤条（本页为 L3 基线） | 数组：下标从 0 开始、下标与元素个数差 1、越界不会报错但很危险、遍历写法 |
| P18 | content | active_rebuild | slide-16 | - | P17 | L3 同 P17 | 字符串：char 数组 + '\0' 结尾；strlen 与 sizeof 的区别；常见库函数 |
| P19 | content | active_rebuild | slide-16 | - | P17 | L3 同 P17 | 结构体：把不同类型的数据打包；定义 / 声明变量 / 成员访问 . 与 -> |
| P20 | content | active_rebuild | slide-16 | - | P17 | L3 同 P17 | 指针：变量有地址；& 取地址、* 取值；指针变量存的是地址；NULL 指针 |
| P21 | content | active_rebuild | slide-16 | - | P5 | L1 同 P5 | 指针传参：swap(int*,int*) 为什么必须用指针（配讲课级代码） |
| P22 | content | active_rebuild | slide-16 | - | P17 | L3 同 P17 | 作业2 四道题（Date 结构体求第几天 / swap 指针交换 / n 个整数求平均 / 函数指针调用 add） |
| P23 | content | active_rebuild | slide-16 | - | P17 | L3 同 P17 | 提交要求与完成标准（单次压缩包、班级+姓名+第几次任务、UTF-8 注释、指定邮箱） |
| P24 | ending | fixed_template | slide-29 | source-slides/slide-29.xml | - | - | 下课啦！ |

页数：24。章节页 4 张（01/02/03/04），两两之间均有内容页；引题页与小结页按学习闭环落在各章首末页。
