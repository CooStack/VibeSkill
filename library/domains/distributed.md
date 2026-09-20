# 分布式系统

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [DC001 · Partial failure; 局部失败](../concepts/DC001.md) | 对方没响应但可能已执行 |
| [DC002 · Network partition; 网络分区](../concepts/DC002.md) | 集群分裂、节点互相看不到 |
| [DC003 · Replication; Leader/follower; 复制](../concepts/DC003.md) | 多副本、主从切换 |
| [DC004 · Sharding; 数据分片](../concepts/DC004.md) | 单机装不下、按键拆数据 |
| [DC005 · Consistent hashing; 一致性哈希](../concepts/DC005.md) | 扩容迁移太多键 |
| [DC006 · Linearizability; 线性一致性](../concepts/DC006.md) | 写完所有后续读取都看见 |
| [DC007 · Sequential consistency; 顺序一致性](../concepts/DC007.md) | 多线程观察顺序 |
| [DC008 · Causal consistency; 因果一致性](../concepts/DC008.md) | 回复不能先于原消息出现 |
| [DC009 · Eventual consistency; 最终一致性](../concepts/DC009.md) | 副本过一会才追上 |
| [DC010 · CAP; 分区下的一致性与可用性](../concepts/DC010.md) | CAP 三选二 |
| [DC011 · Quorum; 法定人数](../concepts/DC011.md) | 多数派读写、票数 |
| [DC012 · Consensus; Raft; Paxos; 共识](../concepts/DC012.md) | 多节点决定同一日志顺序 |
| [DC013 · Leader election; Split brain; 选主与脑裂](../concepts/DC013.md) | 两个主节点同时写 |
| [DC014 · Lease; Fencing token; 租约与隔离令牌](../concepts/DC014.md) | 锁过期旧任务还在写 |
| [DC015 · Logical clock; Lamport clock; 逻辑时钟](../concepts/DC015.md) | 跨机器事件排序 |
| [DC016 · Vector clock; 向量时钟](../concepts/DC016.md) | 判断并发更新还是先后修改 |
| [DC017 · Clock skew; Monotonic clock; 时钟偏差](../concepts/DC017.md) | 机器时间倒退、超时不准 |
| [DC018 · CRDT; 无冲突复制数据类型](../concepts/DC018.md) | 离线多端合并 |
| [DC019 · Two-phase commit; 2PC; 两阶段提交](../concepts/DC019.md) | 跨资源原子提交 |
| [DC020 · Saga; Compensation; 补偿事务](../concepts/DC020.md) | 长流程失败撤销前面步骤 |
| [DC021 · Delivery semantics; At-least-once; Exactly-once](../concepts/DC021.md) | 消息重复、一次且仅一次 |
| [DC022 · Transactional outbox; Inbox](../concepts/DC022.md) | 数据保存成功但消息没发 |
| [DC023 · Anti-entropy; Read repair; 副本修复](../concepts/DC023.md) | 副本长期不一致 |
| [DC024 · Failure detector; Heartbeat; 故障检测](../concepts/DC024.md) | 心跳超时就踢节点 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为分布式系统领域基线，将一致性与协调概念落实为故障模型、状态权威和跨节点副作用的可验证边界。

### 关键特征

- 先定义允许的延迟、重复和不一致表现，再选择协调机制。
- 节点超时不等于远端没有执行，消息确认也不自动等于外部副作用完成。
- 保持已有部署与协调方式，除非任务约束证明需要新增分布式组件。

### 如何落实

- 列出节点角色、状态权威、复制或消息路径，明确业务不变量与实际故障假设。
- 为跨节点操作定义唯一业务意图、提交判定及重试或去重责任，区分可重做和不可重做动作。
- 若涉及副本读取或并发写入，明确可观察一致性、冲突处理和恢复后的状态收敛规则。
- 为相关失败点安排恢复过程与诊断关联，只有协议确实涉及任期或租约时才核对旧拥有者的拒绝机制。

### 如何验收

- 注入消息重复、延迟及乱序，核对业务不变量和允许的中间状态。
- 在提交前后中断节点或连接，确认重试与恢复不会产生未约定的重复副作用。
- 恢复通信后比较各节点状态与操作历史，按约定验证收敛或一致性而非只观察服务存活。

### 常见误用

- 把重试成功或消息交付保证扩大为全业务链路只执行一次。
- 用墙上时钟先后直接判断分布式因果，或把超时当作远端失败的确定证据。
