# 人与计算、隐私及专业责任

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [HC001 · HCI; Human-computer interaction](../concepts/HC001.md) | 人机交互、用户行为 |
| [HC002 · Usability; User research](../concepts/HC002.md) | 用户找不到入口、可用性测试 |
| [HC003 · Accessibility; Assistive technology](../concepts/HC003.md) | 键盘可用、读屏兼容 |
| [HC004 · Cognitive load; Mental model](../concepts/HC004.md) | 操作难记、理解错功能 |
| [HC005 · Privacy by design; Data minimization](../concepts/HC005.md) | 不想收集多余信息 |
| [HC006 · PII; Personal data; 个人信息](../concepts/HC006.md) | 日志里有身份信息 |
| [HC007 · Anonymization; Pseudonymization](../concepts/HC007.md) | 用户 ID 替换后算匿名吗 |
| [HC008 · Differential privacy; DP; 差分隐私](../concepts/HC008.md) | 发布统计但保护个体 |
| [HC009 · Fairness; Bias; 公平性与偏差](../concepts/HC009.md) | 不同人群效果差很大 |
| [HC010 · Explainability; Accountability](../concepts/HC010.md) | 决策能解释、谁负责 |
| [HC011 · Consent; Purpose limitation](../concepts/HC011.md) | 数据能不能换用途 |
| [HC012 · Dark pattern; Deceptive design](../concepts/HC012.md) | 取消难、默认勾选误导 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为人与计算领域基线，将可用性、隐私及责任概念落实为真实任务、数据处理边界和受影响人群的验证。

### 关键特征

- 目标人群、使用环境和辅助方式决定验证范围，内部人员意见不能代替用户证据。
- 数据收集、使用、保留和撤回分别说明，不以模糊的匿名或同意标签替代具体行为。
- 效果、可理解性与责任归属分别评价，不从一个指标推出公平、合规或无障碍的全面结论。

### 如何落实

- 定义受影响用户、核心任务及可能被排除的场景，把概念转成可观察的操作或决策结果。
- 沿任务路径识别理解负担、辅助技术障碍和误导选择，保留必要控制并明确反馈。
- 若涉及个人数据，梳理字段、用途、访问方和保存期限，只按已确认需求安排减少收集及撤回处理。
- 若涉及自动决策或群体差异，明确解释对象、评价口径和人工审查责任，法律或规范结论另行核对。

### 如何验收

- 由具有代表性的使用者或辅助方式完成任务，记录理解偏差、阻断点及实际完成结果。
- 跟踪相关数据从收集到删除或撤回的路径，核对实际行为与向用户表达的约定一致。
- 对适用群体分别检查错误与后果，确认说明、申诉或人工处理入口能承担已约定的责任。

### 常见误用

- 以默认勾选、隐藏取消或含糊文案制造表面同意和任务转化。
- 把去标识、单一公平指标或一次内部体验评审当作全面隐私与责任保证。
