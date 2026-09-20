# MySQL

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [MY001 · MySQL; RDBMS; InnoDB; Storage engine](../concepts/MY001.md) | 关系型数据库、表引擎 |
| [MY002 · Database; Schema; Table; Column](../concepts/MY002.md) | 库表字段、建表 |
| [MY003 · DDL; DML; DCL; SQL](../concepts/MY003.md) | 改表、查数据、授予权限 |
| [MY004 · Primary key; Unique constraint; Foreign key](../concepts/MY004.md) | 主键、唯一订单号、关联完整性 |
| [MY005 · NULL; Three-valued logic; IS NULL](../concepts/MY005.md) | 等于空查不到、空值筛选 |
| [MY006 · Character set; Collation; utf8mb4](../concepts/MY006.md) | emoji 存不了、大小写比较 |
| [MY007 · DECIMAL; Integer; Temporal type; JSON](../concepts/MY007.md) | 金额、日期、动态字段类型 |
| [MY008 · JOIN; INNER/LEFT JOIN](../concepts/MY008.md) | 多表查询、保留没有明细的主表 |
| [MY009 · GROUP BY; HAVING; Aggregate](../concepts/MY009.md) | 分类统计、聚合后筛选 |
| [MY010 · CTE; WITH; Recursive CTE; Window function](../concepts/MY010.md) | 层级递归、分组排名、累计值 |
| [MY011 · Clustered index; 聚簇索引](../concepts/MY011.md) | 主键为什么影响整张表 |
| [MY012 · Secondary index; 二级索引; 回表](../concepts/MY012.md) | 普通索引还要查主键 |
| [MY013 · Composite index; Leftmost prefix; 联合索引](../concepts/MY013.md) | 多条件筛选、索引列顺序 |
| [MY014 · Covering index; 覆盖索引](../concepts/MY014.md) | 不想回表、只查少数字段 |
| [MY015 · Sargability; Index selectivity; Cardinality](../concepts/MY015.md) | 加了索引仍全表扫描 |
| [MY016 · EXPLAIN; EXPLAIN ANALYZE; 执行计划](../concepts/MY016.md) | SQL 慢在哪里、估算不准 |
| [MY017 · Filesort; Temporary table; LIMIT/OFFSET](../concepts/MY017.md) | 排序慢、深分页慢 |
| [MY018 · Autocommit; START TRANSACTION; COMMIT; ROLLBACK](../concepts/MY018.md) | 多次 SQL 一起成功 |
| [MY019 · Isolation level; Consistent read; Locking read](../concepts/MY019.md) | 同事务两次读不一致、读最新值 |
| [MY020 · MVCC; Undo log; Read view](../concepts/MY020.md) | 快照读、旧版本可见 |
| [MY021 · Record lock; Gap lock; Next-key lock](../concepts/MY021.md) | 更新锁太多、插入被阻塞 |
| [MY022 · Deadlock; Lock wait timeout](../concepts/MY022.md) | 死锁、锁等待超时 |
| [MY023 · Redo log; WAL; Crash recovery](../concepts/MY023.md) | 崩溃后如何恢复提交 |
| [MY024 · Binary log; Binlog; GTID; Replication](../concepts/MY024.md) | 主从复制、变更订阅 |
| [MY025 · Replica lag; Read/write splitting](../concepts/MY025.md) | 刚写完从库读不到 |
| [MY026 · Buffer pool; Page; Flush; Checkpoint](../concepts/MY026.md) | 内存缓存、脏页刷盘 |
| [MY027 · Connection pool; Prepared statement; Parameter binding](../concepts/MY027.md) | 连接耗尽、防 SQL 注入 |
| [MY028 · Slow query log; Performance Schema](../concepts/MY028.md) | 哪条 SQL 拖慢、锁分析 |
| [MY029 · Online DDL; Metadata lock; Schema migration](../concepts/MY029.md) | 改表卡住、上线改字段 |
| [MY030 · Backup; PITR; Logical/Physical backup](../concepts/MY030.md) | 恢复误删、恢复到时间点 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 MySQL 领域基线，将查询与事务概念落实为数据语义、访问路径和并发证据，不预设索引或配置方案。

### 关键特征

- 查询正确性先于执行成本，空值、重复、排序和分页语义必须明确。
- 索引设计服从实际筛选、连接和写入负载，不以索引数量衡量优化。
- 事务与锁的判断基于实际配置、语句和并发轨迹，不依靠孤立术语推断。

### 如何落实

- 确认相关表结构、数据分布及查询参数，写出预期结果与事务需要守住的不变量。
- 结合代表性数据观察执行计划与实际耗时，定位扫描、排序、连接或等待的主要成本。
- 只调整与证据对应的查询、索引或事务范围，同时估计写入成本和现有调用影响。
- 若涉及结构或数据迁移，按项目流程安排兼容阶段、失败处理及必要的恢复验证。

### 如何验收

- 用空值、重复键及边界排序数据对比修改前后结果，核对分页是否满足原契约。
- 在相同参数分布和数据规模下比较计划、扫描量与延迟，不只比较单次热缓存耗时。
- 交错执行相关事务并观察等待、冲突和最终数据，确认不变量及重试处理符合约定。

### 常见误用

- 看到慢查询就添加索引，而未区分扫描成本、锁等待和返回数据量。
- 依赖未核对的隔离或锁行为，用单连接测试代替并发验证。
