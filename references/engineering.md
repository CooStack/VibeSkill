# 工程表达与常见简写

面向编程提示词的稳定术语摘要，用于理解团队惯用简写，不限定某个框架版本。与 [设计模式](design-patterns.md)、[后端](backend.md)、[工具链](tooling.md) 互补。领域专用 API 仍需核对项目资料。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| EN001 | OOP; Object-oriented programming; 面向对象 | 封装继承多态、对象协作 | 用对象职责和交互组织程序 | 不要求把所有数据或函数强制变成类 |
| EN002 | FP; Functional programming; 函数式编程 | 纯函数、不可变、函数组合 | 用函数和值转换表达计算并控制副作用 | 支持 lambda 不等于整个设计已经是函数式 |
| EN003 | DTO; Data transfer object; 数据传输对象 | 接口字段、传输模型 | 按边界契约组织用于传输的数据 | 不必与数据库实体一一对应 |
| EN004 | DAO; Data access object; 数据访问对象 | 封装数据库读写 | 用对象隔离数据访问操作 | 与领域仓储可能分工不同，不要求重复套层 |
| EN005 | POJO; Plain old Java object; Java 普通对象 | 简单 Java 对象、不绑框架 | 指不依赖特定容器继承要求的普通 Java 对象 | 不保证对象一定是 DTO、实体或不可变 |
| EN006 | DRY; KISS; YAGNI | 避免重复、保持简单、别过度设计 | 分别提醒避免知识重复、控制复杂度和不预建未需能力 | 三者是不同原则，不是拒绝一切抽象或测试 |
| EN007 | VO; Value object; View object; 值对象/视图对象 | VO 到底是哪种对象 | 领域语境常指按值表达的对象，部分团队将 VO 用作展示模型名 | 必须看项目约定，不能固定映射到一种含义 |
| EN008 | DDD; Domain-driven design; 领域驱动设计 | 领域模型、限界上下文 | 用业务语言与边界组织复杂业务建模和协作 | 不等于多建 Entity/Service/Repository 文件夹 |
| EN009 | MVP; Minimum viable product; 最小可行产品 | 先做核心验证版本 | 用最小可交付范围验证关键产品假设 | 与展示架构 Model-View-Presenter 或图形矩阵 MVP 不同 |
| EN010 | TDD; Test-driven development; 测试驱动开发 | 先写失败测试再实现 | 通过测试、实现和重构的循环推进开发 | 不等同“项目有单元测试”或只追求覆盖率 |
| EN011 | BDD; Behavior-driven development; 行为驱动开发 | 用业务场景讨论验收 | 用共享行为描述连接业务理解与验证 | Given/When/Then 语法本身不保证团队已践行 BDD |
| EN012 | SDK; API; ABI | 开发包、接口、二进制兼容 | SDK 是开发工具资源集合，API 是编程契约，ABI 是二进制调用/布局契约 | API 源码兼容不一定意味着 ABI 兼容 |
| EN013 | CRUD; Create/Read/Update/Delete; 增删改查 | 基础数据管理、CRUD 接口 | 描述创建读取更新删除这一组数据操作 | 不自动包含权限、审计、事务及完整业务流程 |
| EN014 | PR; MR; Pull request; Merge request | 提交合并申请、代码评审 | 围绕候选变更进行审查和合并的协作对象 | 写提示词时提及 PR 不等于已授权推送或创建远程请求 |
| EN015 | RFC; ADR; 技术提案/架构决策记录 | 讨论方案、记录为什么这样选 | RFC 可用于征求讨论，ADR 保存具体决策及取舍 | 语境也可能是标准文档，不要求小改动都写正式提案 |
| EN016 | POC; Proof of concept; 概念验证 | 先试可不可行 | 用受限实验验证某个技术假设 | 可行性演示不等于生产就绪或完整产品 |
| EN017 | SLA; Service-level agreement | 对外服务承诺 | 用协议表达服务承诺及相应约定 | 与内部 SLO 目标、SLI 指标不同，不能擅自承诺可用率 |
| EN018 | RPS; QPS; Throughput; 请求/查询吞吐 | 每秒多少请求、压测容量 | 在明确计数范围和时间窗内描述吞吐 | 高吞吐不意味着低尾延迟，RPS 和 QPS 计数口径可能不同 |
