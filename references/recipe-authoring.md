# 概念落地指南编写约定

## 定位与范围

`*-recipes.json` 是现有概念表的实施补充，不替代定义、领域路由或 `agent-guidance.json` 的需求识别。它回答：真正实现这个概念时，什么性质成立；如何把它落实；用什么动作区分实现与表面模仿。以下编写规则适用于所有实施指南文件。

其中 `core-recipes.json` 覆盖 160 个已存在 ID，限定在以下 11 个领域。前端、图形、数学、Minecraft、系统、设计语言和音效由独立配方文件覆盖，整体范围见 [深度统计](../library/coverage.md)。技术选型是条件性方案，不因命中某个 recipe 就自动获得实施授权。

| 领域 | 前缀 | 条数 | 主要深度 |
| --- | --- | --- | --- |
| 后端 | BE | 30 | 契约、授权、幂等、事务、恢复、容量与观测 |
| Java | JV | 18 | 类型契约、资源、集合、并发及数值时间边界 |
| Kotlin | KT | 15 | 可空性、复制、型变、协程与流生命周期 |
| MySQL | MY | 18 | SQL 结果语义、索引、计划、并发、迁移与恢复 |
| Spring | SP | 15 | 装配、作用域、代理、事务、安全与事件 |
| Vert.x | VX | 8 | 事件循环、上下文、工作池、异步链及背压 |
| 数据结构 | DT | 12 | 操作契约、结构不变量、参考实现对照及成本 |
| 设计模式 | DP | 12 | 真实变化点、协作契约、失败与生命周期 |
| 工具链 | TL | 12 | 构建图、目标兼容、依赖解析、缓存及交付 |
| 工程表达 | EN | 8 | 数据边界、建模、测试、实验与容量口径 |
| 任务规格 | PR | 12 | 意图保真、可观察要求、范围、证据与完成条件 |

这不是“所有非定义概念已穷尽”的声明。优先选取误用后果明显、经常需要实施推导的概念；工具品牌、角色名称、简单语法以及单靠定义即可理解的条目不为凑数展开。`scripts/practices.py` 汇总各配方文件，供搜索和阅读页生成使用；不要重复定义同一 ID。

## 五字段契约

JSON 顶层直接以稳定 ID 为键，无 `recipes` 包装层、注释或额外元数据。每项严格只有五个字段：

| 字段 | 类型 | 应回答的问题 |
| --- | --- | --- |
| `intent` | 非空字符串 | 用户真正得到什么可观察性质，而不只是“用了什么”？ |
| `principles` | 非空字符串数组 | 哪些不变量、适用前提或职责区别不可破坏？ |
| `implementation` | 非空字符串数组 | 应检查、选择、修改和协调哪些具体对象，先后关系是什么？ |
| `checks` | 非空字符串数组 | 在什么输入、时序或故障下观察什么，怎样识别错误实现？ |
| `pitfalls` | 非空字符串数组 | 哪种常见替代做法看似实现了它，实际缺了什么？ |

本批通常使用一个核心原则、三个实施动作、两个检查动作和一个误用提醒；这只是紧凑写法，不是机械配额。后续遇到真正需要更多约束的条目应按内容调整。来源范围记录在本文件，不向 JSON 塞入第六字段。

中文是内容语言。标识符、API 名称和命令保留原始拼写；不把英文名相似当成语义一致。

## 怎样判断足够具体

一个概念说明应通过以下检查，而不是看篇幅是否足够长：

1. **有判别性质。** 将“采用幂等”“使用响应式”替换为状态或时序性质。例如同意图并发重试只产生一份业务提交，不能仅写增加幂等键。
2. **有明确对象。** 指明谁拥有状态、哪个事务覆盖哪些写入、哪一段队列受到容量约束。没有对象的“合理管理资源”仍是方向。
3. **有实现闭环。** 不只说创建，还覆盖何时使用、失效、取消或恢复；并非每项都要涉及全部阶段，按概念风险选择。
4. **有可失败的检查。** 一种常见错误实现应能被检查击穿。例如提交后确认前崩溃，可以区分消息去重与只防按钮连点。
5. **有边界而非绝对承诺。** 说明需要的隔离级别、生命周期或输入条件；未知数值目标留待项目确定，不发明吞吐或可靠性指标。
6. **不能随意换标题复用。** 如果把 ID 换成任意概念，正文仍像通用“检查需求、完善测试”，就需要继续细化。
7. **能停止细分。** 已能据此选择局部实现并写出观察动作时，不继续展开成整门课程或堆砌底层术语。

纯定义型条目可以不写 recipe。某项技术名只有在存在需要处理的生命周期、契约或操作边界时才值得展开。概念组包含不同机制时必须保留区别，例如缓存与配置缓存、线程可见性与原子性、注入与依赖倒置。

## 编写流程

1. 先读取领域表中的完整行及相邻概念，确认 ID、含义和已有边界；再查 `agent-guidance.json`，保持对误用和方案扩张的限制一致。
2. 从真实需求反推一个核心性质，写入 `intent`。框架名可保留在明确框架语境里，但不要将具体供应商工具写成通用问题的唯一答案。
3. 找出维护该性质的最小机制，写入 `principles`。将经验建议、API 事实与项目特定选择分开。
4. 沿现有项目可执行的顺序写实施动作：确认前提，选择局部机制，处理关键失败或收尾。优先复用已有库和模式，不默认安装或重构。
5. 设计正常样例和一个最能暴露误用的反例；并发问题安排交错，持久化问题安排崩溃点，数据结构使用朴素参考结果，性能问题控制负载和环境。
6. 用一条高价值误用提醒解释机制不能替代什么，避免每项都复述“不要过度设计”。
7. 核对外部技术的目标版本文档，记录实际读到的段落及未核查范围；然后检查 JSON 结构、ID 存在性、范围和重复键。

## 从指南生成具体要求

recipe 提供的是可选的实施知识，不是用户授权或现成项目诊断。转换时保留用户明确约束，将不确定环境写成待检查条件，并只选择与本次行为有关的动作。

例如 BE008 可转换为：“沿用现有数据库事务与约束，明确订单意图键的账户范围。同键不同内容应拒绝；并发重复提交只产生一份订单。在提交后返回前模拟连接断开，重试仍取得原结果。”这里数据库机制仅在项目确实已有并适用时采用，不能凭示例强制换存储。

DT016 的检查应针对依赖边，不要求某一个固定输出顺序；PR020 的检查应产生可比较记录，不把测量建议改写成未经用户同意的性能承诺。它们不能共用一段“运行测试确保正确”的验收模板。

## 资料与核查范围

核查日期：2026-09-20。以下为本批实际通过 HTTP 获取的一手文档及读取范围。读取采用正文相关段落抽取，不等同整页所有细节已经审阅，更不等同 160 项逐条或逐版本认证。页面 `current`、`stable` 或无版本地址会变化，实施时仍须对照目标依赖版本。

| 资料入口 | 实际读取范围 | 本批用途与限制 |
| --- | --- | --- |
| [Spring AOP Proxying](https://docs.spring.io/spring-framework/reference/core/aop/proxying.html) | HTTP 200；`this` 自调用绕过代理通知及相关解决路径段落 | SP011、SP012 的代理边界；没有验证项目是否采用代理或织入 |
| [Spring Transaction Annotations](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html) | HTTP 200；外部代理调用、默认异常回滚及可配置规则段落 | SP013、SP015；项目全局规则仍需另查，不将默认值写成普遍事实 |
| [Spring Transaction Propagation](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/tx-propagation.html) | HTTP 200；REQUIRES_NEW 独立资源与连接池风险、NESTED 保存点段落 | SP014；具体事务管理器支持范围仍需确认 |
| [Java 21 Concurrent Package](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/package-summary.html) | HTTP 200；ExecutorService 调度关闭与 happens-before 段落 | JV026、JV027 等并发边界；不是其他 JDK 特性或全部 Java 条目的逐项核验 |
| [kotlinx.coroutines ensureActive](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/ensure-active.html) | HTTP 200；协作取消、非挂起计算主动检查、无 Job 时行为段落 | KT028；未将具体示例调度器写成必选 |
| [Kotlin Cancellation and Timeouts](https://kotlinlang.org/docs/cancellation-and-timeouts.html) | HTTP 200，但本次关键词抽取未取得目标正文段落 | 仅记可访问入口，不据此声称读完取消教程；取消机制以以上 API 页为已读依据 |
| [MySQL 8.4 Multiple-Column Indexes](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/multiple-column-indexes.html) | HTTP 200；复合键前缀查询示例及访问路径段落 | MY013；过滤、覆盖及版本特有优化仍要求查看实际计划 |
| [MySQL 8.4 EXPLAIN](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/explain.html) | HTTP 200；计划信息、连接顺序及索引用途段落 | MY016；本页未逐项核对所有 ANALYZE 支持语法，执行前仍检查是否真实执行及权限 |
| [MySQL 8.4 Isolation Levels](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/innodb-transaction-isolation-levels.html) | HTTP 200；一致性读快照及不同隔离级别的读取、锁行为段落 | MY019、MY021；不泛化到其他引擎 |
| [MySQL 8.4 Deadlock Handling](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/innodb-deadlocks-handling.html) | HTTP 200；死锁诊断、事务重试、缩短事务及一致锁顺序段落 | MY022；等待超时的具体回滚配置未在此页核验 |
| [Vert.x Core](https://vertx.io/docs/vertx-core/java/) | HTTP 200；多事件循环与禁止阻塞回调的正文段落 | VX002、VX005；流、SQL 和每个版本线程细节并未在本次全部逐项读取 |
| [Gradle Build Cache Concepts](https://docs.gradle.org/current/userguide/build_cache_concepts.html) | HTTP 200；缓存键、声明输入、可重复输出及时间戳反例段落 | TL012；本次页面显示版本不作为升级项目的依据 |
| [Gradle Dependency Locking](https://docs.gradle.org/current/userguide/dependency_locking.html) | HTTP 200；按配置启用锁定、初始锁状态及解析结果验证段落 | TL010；不将 Gradle 的具体行为泛化成所有包管理器同名命令 |
| [Azure Architecture Retry](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) | HTTP 200；重试与幂等、副作用风险段落 | BE008、BE031；只采用模式约束，不要求 Azure 产品 |
| [Azure Architecture Saga](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) | HTTP 200；局部事务、补偿、不可回退分界及可重试步骤段落 | BE037；检查场景为本批编写，非厂商端到端保证 |
| [Open Data Structures: Hash Tables](https://opendatastructures.org/ods-java/5_Hash_Tables.html) | HTTP 200；作者教材中的哈希表、哈希码及实现类别导言 | DT008 的结构定位；其他结构的所有复杂度与实现细节未据此宣称逐章证明 |

来源没有覆盖的步骤属于依据现有领域表编写的通用工程操作建议，而非特定 API 已通过实测的结论。Spring Security 配置、Flow 缓冲默认值、Vert.x 新旧 API、DDL 算法和包管理命令等实际使用时，应继续查目标版本的专门章节。本批刻意不提供未经目标项目确认的可运行 API 拼接代码。

## 维护与审阅

- 只引用已经存在的稳定 ID；同一主题跨表存在时按本批分工选择 ID，不凭同名创造映射。
- 先用 JSON 解析器验证五字段和字符串数组，再核对领域表 ID。重复键须单独检测，不能依赖会覆盖同名键的解析器。
- 核对检查项与正文性质是否对应，特别检查并发、异常、取消和恢复是否被写成空泛提醒。
- 审阅时抽取不同领域的条目，而不只展示最成熟的后端案例。数据结构可用参考结果，工程概念可用行为对照，任务规格可用约束可追溯性证明。
- 不把本文记录的 HTTP 成功当测试通过；结构验证、资料核查、项目实现验证是三类不同证据。
- 本批不修改已有入口、README、搜索脚本、metadata 或生成页，也不运行会重建这些文件的命令。后续整体集成由维护者决定。
