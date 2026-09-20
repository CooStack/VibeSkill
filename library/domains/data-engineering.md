# 数据工程、存储与检索

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [DE001 · OLTP; Online transaction processing](../concepts/DE001.md) | 订单写入、短事务 |
| [DE002 · OLAP; Online analytical processing](../concepts/DE002.md) | 报表聚合、历史趋势 |
| [DE003 · Data warehouse; Data lake; Lakehouse](../concepts/DE003.md) | 数据仓库、数据湖、湖仓 |
| [DE004 · ETL; ELT; 数据集成](../concepts/DE004.md) | 抽取清洗入库 |
| [DE005 · CDC; Change data capture; 变更数据捕获](../concepts/DE005.md) | 增量同步、不全量扫表 |
| [DE006 · Schema evolution; 模式演进](../concepts/DE006.md) | 加字段旧消费者报错 |
| [DE007 · Data lineage; 数据血缘](../concepts/DE007.md) | 报表数字从哪来 |
| [DE008 · Data quality; Data contract](../concepts/DE008.md) | 空值暴涨、口径不一致 |
| [DE009 · Event time; Processing time; 事件时间](../concepts/DE009.md) | 迟到日志算在哪天 |
| [DE010 · Watermark; Allowed lateness; 水位线](../concepts/DE010.md) | 乱序数据、窗口何时关闭 |
| [DE011 · Tumbling/Sliding/Session window](../concepts/DE011.md) | 五分钟统计、会话聚合 |
| [DE012 · Batch vs Stream processing](../concepts/DE012.md) | 批处理、持续处理 |
| [DE013 · Row/Column storage; 行存列存](../concepts/DE013.md) | 只读少量列却扫全表 |
| [DE014 · LSM tree; SSTable; Compaction](../concepts/DE014.md) | 写多读少、后台合并 |
| [DE015 · Inverted index; 倒排索引](../concepts/DE015.md) | 按词找文档、全文搜索 |
| [DE016 · BM25; Lexical retrieval; 词面检索](../concepts/DE016.md) | 关键词相关性排序 |
| [DE017 · Vector search; ANN; 向量近邻](../concepts/DE017.md) | 语义相似搜索、召回 |
| [DE018 · Hybrid retrieval; Reranking](../concepts/DE018.md) | 关键词与语义搜索结合 |
| [DE019 · Object/Block/File storage](../concepts/DE019.md) | 对象存储、块设备、文件共享 |
| [DE020 · Erasure coding; 纠删码](../concepts/DE020.md) | 冗余存储节省空间 |
| [DE021 · Normalization; Denormalization](../concepts/DE021.md) | 重复字段、分析宽表 |
| [DE022 · Data retention; Deletion propagation](../concepts/DE022.md) | 删除后副本还有、保留期限 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为数据工程领域基线，将管道与数据模型概念落实为数据契约、时间语义和可重复处理结果。

### 关键特征

- 先定义记录粒度、主键和字段意义，再安排转换与存储。
- 区分事件发生时间、到达时间和处理时间，迟到与重复规则需明确。
- 数据质量、完整性和时效性分别验收，不把任务运行成功等同于数据正确。

### 如何落实

- 记录来源、目标、字段类型、单位和空值语义，明确过滤或聚合会改变的记录粒度。
- 将转换组织为可定位阶段，为无效记录、重复记录和模式变化安排与现有流程一致的处理。
- 若涉及增量处理，定义进度标记、重跑范围及迟到数据策略，避免仅用处理时间猜测完整性。
- 对本次输出建立行数、键集合或聚合量的对账方式，按需求保留来源与转换版本线索。

### 如何验收

- 使用缺失、重复、迟到和字段变更样本核对输出及被拒记录的归属。
- 对同一范围重跑并在中途失败后恢复，确认不会遗漏或额外累加数据。
- 比较源与目标的约定对账量，分别核对完整性、质量和时效指标。

### 常见误用

- 仅以管道退出码或输出行数判断正确，忽略字段语义与聚合粒度。
- 用简单去重掩盖来源冲突，或默认所有数据都按事件时间顺序到达。
