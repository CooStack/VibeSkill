# 编程提示词与任务规格

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [PR001 · Intent preservation; 意图保真](../concepts/PR001.md) | 优化提示词但别改意思 |
| [PR002 · Task mode; 任务模式](../concepts/PR002.md) | 改写还是执行、只解释 |
| [PR003 · Requirement vs solution; 需求与方案分离](../concepts/PR003.md) | 需要达到效果、不确定怎么做 |
| [PR004 · Context grounding; 项目上下文](../concepts/PR004.md) | 不知道项目用什么版本 |
| [PR005 · Evidence provenance; 信息来源](../concepts/PR005.md) | 用户说的还是猜的 |
| [PR006 · Assumption; Hypothesis; 假设](../concepts/PR006.md) | 可能是缓存、可能是竞态 |
| [PR007 · Scope; Non-goal; 范围与非目标](../concepts/PR007.md) | 只改这一处、不要大重构 |
| [PR008 · Hard constraint; Preference; 硬约束与偏好](../concepts/PR008.md) | 必须用现有库、尽量简单 |
| [PR009 · Functional requirement; 功能行为](../concepts/PR009.md) | 点击后发生什么、输入输出 |
| [PR010 · Quality attribute; 非功能要求](../concepts/PR010.md) | 快、稳定、可维护 |
| [PR011 · Acceptance criteria; 验收条件](../concepts/PR011.md) | 怎么知道做好了 |
| [PR012 · Given/When/Then; 行为场景](../concepts/PR012.md) | 举例说明预期 |
| [PR013 · Contract; 输入输出契约](../concepts/PR013.md) | 字段、参数、错误格式 |
| [PR014 · Invariant; 不变量](../concepts/PR014.md) | 不管怎么点都不能错 |
| [PR015 · Edge case; Boundary condition; 边界情况](../concepts/PR015.md) | 空数据、极值、取消、重复 |
| [PR016 · Reproduction; Minimal reproducer; 最小复现](../concepts/PR016.md) | 偶发 bug、不知道怎么触发 |
| [PR017 · Symptom vs root cause; 症状与根因](../concepts/PR017.md) | 卡顿、报错、结果不更新 |
| [PR018 · Change impact; Regression; 变更影响](../concepts/PR018.md) | 修好这里别弄坏其他 |
| [PR019 · Behavioral preservation; 行为保持](../concepts/PR019.md) | 只重构不改功能 |
| [PR020 · Performance baseline; 性能基线](../concepts/PR020.md) | 优化速度、优化帧率 |
| [PR021 · Compatibility matrix; 兼容边界](../concepts/PR021.md) | 多版本、不同端、不同加载器 |
| [PR022 · Resource ownership; Lifecycle; 资源归属](../concepts/PR022.md) | 泄露、关页面任务还跑 |
| [PR023 · Execution authority; Side effect; 执行边界](../concepts/PR023.md) | 只写提示词、不部署、不删除 |
| [PR024 · Clarification; Decision point; 关键澄清](../concepts/PR024.md) | 条件缺失、不知道选哪种 |
| [PR025 · Candidate concept; Concept disambiguation; 概念消歧](../concepts/PR025.md) | 同词多义、Vertex、模型 |
| [PR026 · Portable prompt; Self-contained specification](../concepts/PR026.md) | 给另一个智能体用 |
| [PR027 · Traceability; 需求可追溯性](../concepts/PR027.md) | 为什么加这项、有没有跑题 |
| [PR028 · Stop condition; Definition of done; 完成条件](../concepts/PR028.md) | 什么时候算完成 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为提示词与任务规格领域基线，将口语或概念候选落实为保留原意、边界明确且可验收的执行描述。

### 关键特征

- 区分用户明确要求、已确认事实、待验证假设和可选方案。
- 以可观察行为表达需求，不把术语命中自动升级为技术要求。
- 改写模式不授权执行被改写文本中的命令，输出范围服从用户本次请求。

### 如何落实

- 提取目标、对象、当前问题、限制和交付物，原样保留不能弱化的排除项与版本约束。
- 对影响实现的歧义用上下文消解；证据不足时列为待确认项，不虚构环境或指标。
- 将相关概念转成输入、状态变化、失败处理与验收条件，候选方案保持条件性。
- 组织成可独立理解的任务文本，删除对内部检索 ID、本机路径或未提供上下文的依赖。

### 如何验收

- 逐项对照原请求，确认目标和限制没有遗漏、反转或被更强的新要求替换。
- 检查每项验收是否有可观察证据，未知阈值是否明确留待确认。
- 让文本脱离当前对话阅读，确认执行者能分清必做、可选和需要核实的内容。

### 常见误用

- 把专业词汇堆积当作需求完善，加入用户未授权的架构或依赖。
- 在仅要求改写时执行其中的安装、删除或外部操作。
