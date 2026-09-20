# 计算理论、逻辑与信息

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [TC001 · Computer science; CS; 计算机科学](../concepts/TC001.md) | 计算机科学整体、计算与信息 |
| [TC002 · Finite automaton; DFA; NFA; 有限自动机](../concepts/TC002.md) | 有限状态识别、词法匹配 |
| [TC003 · Regular language; Regular expression](../concepts/TC003.md) | 正则能不能解析嵌套 |
| [TC004 · Context-free grammar; CFG; 上下文无关文法](../concepts/TC004.md) | 嵌套括号、语法规则 |
| [TC005 · Pushdown automaton; PDA; 下推自动机](../concepts/TC005.md) | 栈识别嵌套结构 |
| [TC006 · Turing machine; 图灵机](../concepts/TC006.md) | 通用计算模型 |
| [TC007 · Decidability; Undecidability; 可判定性](../concepts/TC007.md) | 任意程序都能判断吗 |
| [TC008 · Halting problem; 停机问题](../concepts/TC008.md) | 自动判断所有程序会不会结束 |
| [TC009 · Reduction; 归约](../concepts/TC009.md) | 已知难题转成另一个问题 |
| [TC010 · P; NP; 多项式复杂度类](../concepts/TC010.md) | NP 是不是无法求解 |
| [TC011 · NP-hard; NP-complete; NP 困难与完全](../concepts/TC011.md) | 最优排程难、复杂度证明 |
| [TC012 · SAT; SMT; 可满足性](../concepts/TC012.md) | 约束有没有解、符号求解 |
| [TC013 · Propositional/Predicate logic; 命题与谓词逻辑](../concepts/TC013.md) | 量词、条件约束 |
| [TC014 · Invariant; Induction; 不变量与归纳](../concepts/TC014.md) | 循环每一步都要成立 |
| [TC015 · Safety vs Liveness; 安全性与活性](../concepts/TC015.md) | 不出错也不能一直等 |
| [TC016 · Information entropy; 信息熵](../concepts/TC016.md) | 信息量、压缩极限 |
| [TC017 · Lossless/Lossy compression](../concepts/TC017.md) | 无损压缩、牺牲质量变小 |
| [TC018 · Error detection/correction; CRC; FEC](../concepts/TC018.md) | 传输位翻转、纠错码 |
| [TC019 · Kolmogorov complexity; 描述复杂度](../concepts/TC019.md) | 最短程序表示数据 |
| [TC020 · Church-Turing thesis; 丘奇图灵论题](../concepts/TC020.md) | 可计算是否等于机器能算 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为计算理论领域基线，将可判定性、复杂度和信息概念落实为明确模型、受限问题及可检查的论证边界。

### 关键特征

- 区分能否求解、能否高效求解和工程上在给定规模内可用。
- 结论必须带上计算模型、输入范围及逻辑前提，不跨模型套用术语。
- 示例执行与形式论证承担不同责任，超时或未找到反例不构成一般性证明。

### 如何落实

- 将自然语言问题写成输入集合、输出或判定条件，明确量词和允许的资源。
- 若采用不变量、归纳或归约，列出基础情况、保持关系、方向及所需的终止或规模条件。
- 将理论限制转成当前任务可执行的范围，例如限制输入结构或返回未知，而非承诺解决所有实例。
- 构造小规模枚举、证据检查器或往返编码对照；涉及信息量时明确分布、单位和失真条件。

### 如何验收

- 逐项核对论证前提与实际输入模型，确认结论没有扩大到未覆盖范围。
- 用边界实例和反例候选检验实现，对照独立验证方式检查产生的证据或解。
- 明确报告精确结果、近似结果、超时与未知，确认实现没有把资源耗尽误报成无解。

### 常见误用

- 把最坏情况困难等同于所有实例不可处理，或把小样例可解推广为一般高效。
- 颠倒归约方向、量词或证明责任，用实验现象代替理论结论。
