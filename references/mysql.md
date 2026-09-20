# MySQL

检索分组：SQL 与数据建模、索引与计划、事务与锁、运维与一致性。
共通数据库概念见 [backend.md](backend.md)，结构原理见 [data-structures.md](data-structures.md)。来源 S43，见 [sources.md](sources.md)。以项目 MySQL 版本、存储引擎和会话设置为准；不把其他数据库的同名机制直接套入。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| MY001 | MySQL; RDBMS; InnoDB; Storage engine | 关系型数据库、表引擎 | MySQL 管理关系数据；InnoDB 是支持事务等能力的存储引擎 | 数据库产品、SQL 语言和存储引擎不是同一层 |
| MY002 | Database; Schema; Table; Column | 库表字段、建表 | 以表和列组织数据并定义结构约束 | MySQL 中 schema 的用法不应泛化到所有数据库 |
| MY003 | DDL; DML; DCL; SQL | 改表、查数据、授予权限 | 区分结构定义、数据操作与权限管理语句 | 部分 DDL 的提交语义不同于普通 DML |
| MY004 | Primary key; Unique constraint; Foreign key | 主键、唯一订单号、关联完整性 | 表达记录身份、业务唯一性与引用约束 | 外键不代替应用授权，唯一性中的 NULL 规则需核对 |
| MY005 | NULL; Three-valued logic; IS NULL | 等于空查不到、空值筛选 | SQL 条件需处理真、假和未知 | NULL 不等于空字符串或数字零 |
| MY006 | Character set; Collation; utf8mb4 | emoji 存不了、大小写比较 | 字符集描述编码，排序规则影响比较与排序 | 客户端、连接、库表列配置均可能影响结果 |
| MY007 | DECIMAL; Integer; Temporal type; JSON | 金额、日期、动态字段类型 | 按数据语义与查询需求选存储类型 | JSON 灵活性不能替代必要关系约束和索引设计 |
| MY008 | JOIN; INNER/LEFT JOIN | 多表查询、保留没有明细的主表 | 按关系匹配组合行或保留无匹配行 | WHERE 中右表过滤可能改变外连接的保留效果 |
| MY009 | GROUP BY; HAVING; Aggregate | 分类统计、聚合后筛选 | 按组计算并筛选聚合结果 | WHERE 与 HAVING 作用阶段不同 |
| MY010 | CTE; WITH; Recursive CTE; Window function | 层级递归、分组排名、累计值 | 分解查询或在保留行明细时计算窗口结果 | 不是保证提速的语法，支持与限制依版本 |
| MY011 | Clustered index; 聚簇索引 | 主键为什么影响整张表 | InnoDB 用聚簇结构组织行数据，通常以主键作为键 | 不等于多台服务器的数据库集群 |
| MY012 | Secondary index; 二级索引; 回表 | 普通索引还要查主键 | InnoDB 二级索引记录包含主键值，可用它定位完整行（S43） | 二级索引不必包含查询需要的所有列 |
| MY013 | Composite index; Leftmost prefix; 联合索引 | 多条件筛选、索引列顺序 | 按有序键前缀及条件形态组织可用访问路径 | 范围条件后列是否用于过滤/覆盖需看计划，不背绝对口诀 |
| MY014 | Covering index; 覆盖索引 | 不想回表、只查少数字段 | 若所需数据均可由索引满足，可减少额外行访问 | 过宽索引增加存储和写入成本 |
| MY015 | Sargability; Index selectivity; Cardinality | 加了索引仍全表扫描 | 查询可搜索性、区分度和估算成本影响路径选择 | 使用函数或类型转换的影响应结合表达式索引及版本判断 |
| MY016 | EXPLAIN; EXPLAIN ANALYZE; 执行计划 | SQL 慢在哪里、估算不准 | 观察访问路径、行数及执行阶段成本 | ANALYZE 类操作可能实际执行，先确认安全与环境 |
| MY017 | Filesort; Temporary table; LIMIT/OFFSET | 排序慢、深分页慢 | 定位排序、中间结果和跳过大量行的成本 | filesort 名称不意味着必定全部落磁盘 |
| MY018 | Autocommit; START TRANSACTION; COMMIT; ROLLBACK | 多次 SQL 一起成功 | 显式约束一组操作的事务边界 | 连接池归还时需处理残留事务状态 |
| MY019 | Isolation level; Consistent read; Locking read | 同事务两次读不一致、读最新值 | 区分快照读取与带锁读取等可见性规则 | 不同隔离级别、语句及事务时序影响行为 |
| MY020 | MVCC; Undo log; Read view | 快照读、旧版本可见 | 用版本与可见性机制支持并发读取 | 长事务可能阻碍历史版本清理 |
| MY021 | Record lock; Gap lock; Next-key lock | 更新锁太多、插入被阻塞 | 区分索引记录锁、间隙锁及组合范围锁 | 实际锁范围受索引、隔离级别与执行路径影响 |
| MY022 | Deadlock; Lock wait timeout | 死锁、锁等待超时 | 区分相互依赖环与等待超时，事务需正确回退或重试 | 不在未确认事务结果时盲目重放非幂等副作用 |
| MY023 | Redo log; WAL; Crash recovery | 崩溃后如何恢复提交 | 日志机制支撑故障恢复及持久性策略 | redo 与撤销版本的 undo 不是同一种日志 |
| MY024 | Binary log; Binlog; GTID; Replication | 主从复制、变更订阅 | 记录可用于复制/恢复的变更并标识事务进度 | binlog 与 InnoDB redo 职责不同 |
| MY025 | Replica lag; Read/write splitting | 刚写完从库读不到 | 将读流量分配副本时处理同步延迟 | 副本不能被假定立即一致，也不能替代备份 |
| MY026 | Buffer pool; Page; Flush; Checkpoint | 内存缓存、脏页刷盘 | 用页缓存与刷盘机制协调内存和存储 | 缓存命中率高不证明不存在锁或 CPU 瓶颈 |
| MY027 | Connection pool; Prepared statement; Parameter binding | 连接耗尽、防 SQL 注入 | 复用连接并把值参数与 SQL 结构分离 | 标识符和排序方向通常不能直接当值参数绑定 |
| MY028 | Slow query log; Performance Schema | 哪条 SQL 拖慢、锁分析 | 通过日志与运行指标定位负载和等待 | 采集开销及日志敏感信息需要控制 |
| MY029 | Online DDL; Metadata lock; Schema migration | 改表卡住、上线改字段 | 评估结构变更算法、元数据锁和应用兼容窗口 | online 不代表完全无锁或任意版本都同样支持 |
| MY030 | Backup; PITR; Logical/Physical backup | 恢复误删、恢复到时间点 | 区分逻辑导出、物理备份与日志重放恢复 | 需要验证恢复链及一致性，不只确认导出成功 |
