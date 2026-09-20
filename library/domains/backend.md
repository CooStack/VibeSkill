# 后端

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [BE001 · 接口契约 API contract; Schema](../concepts/BE001.md) | 前后端字段对不上、返回格式 |
| [BE002 · REST; 资源 Resource](../concepts/BE002.md) | 增删改查接口、资源地址 |
| [BE003 · RPC; gRPC](../concepts/BE003.md) | 服务间调用、强类型契约 |
| [BE004 · GraphQL; 查询语言](../concepts/BE004.md) | 客户端按需取字段 |
| [BE005 · Webhook; 回调通知](../concepts/BE005.md) | 外部系统通知我、支付通知 |
| [BE006 · 分页 Pagination; 游标 Cursor; Offset](../concepts/BE006.md) | 列表翻页、滚动加载 |
| [BE007 · 版本化 Versioning; 向后兼容](../concepts/BE007.md) | 老客户端不能坏 |
| [BE008 · 幂等 Idempotency; 幂等键](../concepts/BE008.md) | 重复提交、重试重复下单 |
| [BE009 · 认证 Authentication; AuthN](../concepts/BE009.md) | 你是谁、登录 |
| [BE010 · 授权 Authorization; AuthZ; RBAC; ABAC](../concepts/BE010.md) | 角色权限、只能看自己的 |
| [BE011 · Session; Cookie; JWT](../concepts/BE011.md) | 登录态、令牌、退出登录 |
| [BE012 · OAuth 2.0; OIDC; SSO](../concepts/BE012.md) | 第三方登录、统一登录 |
| [BE013 · 输入验证 Validation; 参数化查询](../concepts/BE013.md) | 非法输入、SQL 注入 |
| [BE014 · 密码哈希 Password hashing; Salt](../concepts/BE014.md) | 保存密码、密码泄露 |
| [BE015 · 密钥管理 Secrets; 最小权限](../concepts/BE015.md) | API key、配置泄露 |
| [BE016 · 限流 Rate limiting; Quota](../concepts/BE016.md) | 刷接口、防滥用、配额 |
| [BE017 · 关系模型 Relational model; 主外键](../concepts/BE017.md) | 表关联、数据一致 |
| [BE018 · 规范化 Normalization; 反规范化](../concepts/BE018.md) | 重复字段、联表太多 |
| [BE019 · 索引 Index; B-tree; 复合索引](../concepts/BE019.md) | 查询慢、筛选排序 |
| [BE020 · 查询计划 Query plan; EXPLAIN](../concepts/BE020.md) | SQL 为什么慢 |
| [BE021 · 事务 Transaction; ACID](../concepts/BE021.md) | 转账、同时成功或失败 |
| [BE022 · 隔离级别 Isolation; MVCC](../concepts/BE022.md) | 脏读、幻读、并发读取 |
| [BE023 · 乐观锁 Optimistic locking; CAS](../concepts/BE023.md) | 防覆盖别人修改、版本号 |
| [BE024 · 悲观锁 Pessimistic locking; 死锁 Deadlock](../concepts/BE024.md) | 抢库存、锁住数据 |
| [BE025 · ORM; N+1; 批量加载](../concepts/BE025.md) | 循环查数据库、实体映射 |
| [BE026 · 迁移 Migration; 回填 Backfill](../concepts/BE026.md) | 修改表结构、补历史数据 |
| [BE027 · 缓存 Cache; TTL; Invalidation](../concepts/BE027.md) | 重复查询、加速、旧数据 |
| [BE028 · Cache-aside; 缓存穿透/击穿/雪崩](../concepts/BE028.md) | 热点过期、缓存失效打爆库 |
| [BE029 · 消息队列 Queue; Pub/Sub](../concepts/BE029.md) | 异步排队、事件广播 |
| [BE030 · 投递语义 At-least-once; At-most-once; Exactly-once](../concepts/BE030.md) | 消息不能丢也不能重复 |
| [BE031 · 重试 Retry; 退避 Backoff; Jitter](../concepts/BE031.md) | 网络失败再试 |
| [BE032 · 超时 Timeout; Deadline; 取消 Cancellation](../concepts/BE032.md) | 一直等待、请求卡死 |
| [BE033 · 熔断 Circuit breaker; 隔舱 Bulkhead](../concepts/BE033.md) | 下游故障拖垮全部 |
| [BE034 · 背压 Backpressure; 负载削减 Load shedding](../concepts/BE034.md) | 消费跟不上、内存涨 |
| [BE035 · 一致性 Consistency; 最终一致 Eventual consistency](../concepts/BE035.md) | 写完读不到、跨节点同步 |
| [BE036 · CAP; 网络分区 Partition](../concepts/BE036.md) | 分布式可用与一致如何选 |
| [BE037 · Saga; 补偿事务 Compensation](../concepts/BE037.md) | 跨服务订单流程 |
| [BE038 · Outbox; CDC](../concepts/BE038.md) | 数据提交了但消息没发 |
| [BE039 · CQRS; 读写模型分离](../concepts/BE039.md) | 读写结构差异很大 |
| [BE040 · 事件溯源 Event sourcing](../concepts/BE040.md) | 历史状态重放、事件账本 |
| [BE041 · 单体 Monolith; 模块化单体; 微服务](../concepts/BE041.md) | 拆服务、独立发布 |
| [BE042 · 负载均衡 Load balancing; 水平扩展](../concepts/BE042.md) | 多台机器、扩容 |
| [BE043 · 分片 Sharding; 复制 Replication](../concepts/BE043.md) | 数据太大、读副本 |
| [BE044 · 可观测性 Observability; Logs; Metrics; Traces](../concepts/BE044.md) | 找故障、链路慢 |
| [BE045 · SLI; SLO; 错误预算 Error budget](../concepts/BE045.md) | 可用率目标、延迟目标 |
| [BE046 · 健康检查 Liveness; Readiness](../concepts/BE046.md) | 启动未好就接流量 |
| [BE047 · CI/CD; 蓝绿 Blue-green; 金丝雀 Canary](../concepts/BE047.md) | 自动发布、逐步上线 |
| [BE048 · 容器 Container; 编排 Orchestration; IaC](../concepts/BE048.md) | 环境一致、自动部署 |
| [BE049 · 备份 Backup; RPO; RTO; 灾备](../concepts/BE049.md) | 丢数据怎么办、多久恢复 |
| [BE050 · 单元/集成/契约/端到端测试](../concepts/BE050.md) | 接口改动不敢上线 |
| [BE051 · 多租户 Multi-tenancy; 租户隔离](../concepts/BE051.md) | 多家公司共用系统 |
| [BE052 · 后台任务 Job; Scheduler; 工作流 Workflow](../concepts/BE052.md) | 定时处理、长任务进度 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为后端领域基线，将已选概念落实为请求、业务状态和外部副作用的可验证约定；按任务选用，不替代概念专用教程。

### 关键特征

- 以业务不变量界定成功，例如余额或订单状态的合法变化，而非只以接口返回成功界定完成。
- 分清请求边界、事务边界与外部副作用边界，明确每份状态的权威来源。
- 并发、重试和缓存策略由已有调用方式与一致性要求决定，不默认增加队列或服务拆分。

### 如何落实

- 列出本次入口的输入约束、身份来源、返回契约和可观察副作用，标注拒绝请求时不能发生的写入。
- 把业务条件放入负责该状态的现有模块，划定校验、读写与提交顺序，明确中途失败后的状态。
- 若入口可能并发或重试，定义同一业务意图的识别方式，并安排冲突处理与重复响应语义。
- 沿实际依赖链安排超时、错误映射和资源释放；只有任务涉及跨边界副作用时才确定补偿或恢复路径。

### 如何验收

- 用合法、非法和越权输入核对返回结果与持久化状态，失败请求不留下未约定副作用。
- 对适用的重复和并发请求核对业务不变量，而不只比较响应码。
- 在依赖失败及提交前后失败点核对可恢复状态，确认错误能定位到具体阶段。

### 常见误用

- 把一次数据库提交成功等同于整个跨系统业务已经完成。
- 为简单入口默认引入微服务、消息队列或缓存，扩大需求与失效面。
