# 工程表达与常见简写

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [EN001 · OOP; Object-oriented programming; 面向对象](../concepts/EN001.md) | 封装继承多态、对象协作 |
| [EN002 · FP; Functional programming; 函数式编程](../concepts/EN002.md) | 纯函数、不可变、函数组合 |
| [EN003 · DTO; Data transfer object; 数据传输对象](../concepts/EN003.md) | 接口字段、传输模型 |
| [EN004 · DAO; Data access object; 数据访问对象](../concepts/EN004.md) | 封装数据库读写 |
| [EN005 · POJO; Plain old Java object; Java 普通对象](../concepts/EN005.md) | 简单 Java 对象、不绑框架 |
| [EN006 · DRY; KISS; YAGNI](../concepts/EN006.md) | 避免重复、保持简单、别过度设计 |
| [EN007 · VO; Value object; View object; 值对象/视图对象](../concepts/EN007.md) | VO 到底是哪种对象 |
| [EN008 · DDD; Domain-driven design; 领域驱动设计](../concepts/EN008.md) | 领域模型、限界上下文 |
| [EN009 · MVP; Minimum viable product; 最小可行产品](../concepts/EN009.md) | 先做核心验证版本 |
| [EN010 · TDD; Test-driven development; 测试驱动开发](../concepts/EN010.md) | 先写失败测试再实现 |
| [EN011 · BDD; Behavior-driven development; 行为驱动开发](../concepts/EN011.md) | 用业务场景讨论验收 |
| [EN012 · SDK; API; ABI](../concepts/EN012.md) | 开发包、接口、二进制兼容 |
| [EN013 · CRUD; Create/Read/Update/Delete; 增删改查](../concepts/EN013.md) | 基础数据管理、CRUD 接口 |
| [EN014 · PR; MR; Pull request; Merge request](../concepts/EN014.md) | 提交合并申请、代码评审 |
| [EN015 · RFC; ADR; 技术提案/架构决策记录](../concepts/EN015.md) | 讨论方案、记录为什么这样选 |
| [EN016 · POC; Proof of concept; 概念验证](../concepts/EN016.md) | 先试可不可行 |
| [EN017 · SLA; Service-level agreement](../concepts/EN017.md) | 对外服务承诺 |
| [EN018 · RPS; QPS; Throughput; 请求/查询吞吐](../concepts/EN018.md) | 每秒多少请求、压测容量 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为工程实践领域基线，将职责、流程和质量概念落实为有限变更范围、接口契约与可追踪交付证据。

### 关键特征

- 先消歧工程简写并定位实际责任，不能仅凭名称决定组织结构。
- 变更规模与风险相称，复用既有流程而不为局部需求增加制度或基础设施。
- 区分行为保证、实施过程与交付证据，完成某个流程不等于目标已经达成。

### 如何落实

- 明确本次变更的入口、拥有者、调用方和不能改变的契约，列出直接影响面。
- 在既有模块边界内安排实现，只有真实重复或协作关系支持时才提取抽象。
- 按失败后果选择验证层级，若涉及兼容或迁移则明确过渡行为和恢复路径。
- 记录实际变更、验证结果与未验证部分，使交付说明能够对应具体产物和行为。

### 如何验收

- 核对受影响调用方的输入输出与错误契约，确认没有隐藏的行为扩张。
- 用本次风险对应的代表场景验证结果，确认检查不仅覆盖新代码也覆盖连接处。
- 对照请求与产物清单，确认没有无关重构、配置漂移或未披露的验证缺口。

### 常见误用

- 把 DTO、DDD 或 TDD 等标签当作必须采用的整套架构或流程。
- 以代码量、覆盖率数字或流程完成数代替行为正确性的证据。
