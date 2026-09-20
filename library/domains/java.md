# Java 与 JVM

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [JV001 · JDK; JVM; Java SE; Runtime](../concepts/JV001.md) | Java 环境、编译与运行版本 |
| [JV002 · Bytecode; Class file; javac; release](../concepts/JV002.md) | 编译能过运行版本不支持 |
| [JV003 · Primitive; Reference; Boxing; Unboxing](../concepts/JV003.md) | int 和 Integer、空值拆箱 |
| [JV004 · Pass-by-value; 值传递](../concepts/JV004.md) | 方法里改参数为何不同 |
| [JV005 · equals; hashCode; Identity](../concepts/JV005.md) | HashMap 找不到、对象比较 |
| [JV006 · final; Immutability; 不可变对象](../concepts/JV006.md) | 不让修改、线程安全共享 |
| [JV007 · Class; Interface; Abstract class](../concepts/JV007.md) | 抽象接口、继承实现 |
| [JV008 · Overload; Override; Dynamic dispatch](../concepts/JV008.md) | 同名方法、重载重写 |
| [JV009 · Access modifier; Package; Encapsulation](../concepts/JV009.md) | private、包可见、访问不到 |
| [JV010 · Generics; Type parameter; Type erasure; 类型擦除](../concepts/JV010.md) | 泛型、运行时取不到 T |
| [JV011 · Wildcard; Bounded type; PECS](../concepts/JV011.md) | extends/super、不知道泛型怎么传 |
| [JV012 · Raw type; Heap pollution; Unchecked cast](../concepts/JV012.md) | 未检查转换警告、泛型污染 |
| [JV013 · Record; 数据载体](../concepts/JV013.md) | DTO、少写样板代码 |
| [JV014 · Enum; Sealed class; Pattern matching](../concepts/JV014.md) | 固定状态、穷举分支 |
| [JV015 · Exception; Checked/Unchecked; try/finally](../concepts/JV015.md) | 异常传播、要不要 throws |
| [JV016 · AutoCloseable; try-with-resources](../concepts/JV016.md) | 文件句柄泄露、连接没关 |
| [JV017 · Annotation; Reflection; Retention](../concepts/JV017.md) | 注解读取不到、动态调用 |
| [JV018 · Annotation processing; APT; Generated source](../concepts/JV018.md) | 自动生成代码、编译期处理 |
| [JV019 · List; Set; Map; Collection](../concepts/JV019.md) | 有序列表、去重、键值查找 |
| [JV020 · Iterator; Fail-fast; ConcurrentModificationException](../concepts/JV020.md) | 遍历时删除报错 |
| [JV021 · Comparator; Comparable; Stable sort](../concepts/JV021.md) | 自定义排序、排序不稳定 |
| [JV022 · Lambda; Functional interface; Method reference](../concepts/JV022.md) | 回调、方法引用 |
| [JV023 · Stream API; Intermediate/Terminal operation](../concepts/JV023.md) | 集合过滤聚合、流只执行一次 |
| [JV024 · Collector; groupingBy; parallelStream](../concepts/JV024.md) | 分组统计、并行流 |
| [JV025 · Optional](../concepts/JV025.md) | 返回值可能不存在 |
| [JV026 · Thread; ExecutorService; Thread pool](../concepts/JV026.md) | 后台任务、线程池耗尽 |
| [JV027 · Java Memory Model; Happens-before; volatile](../concepts/JV027.md) | 多线程看不到更新 |
| [JV028 · synchronized; Lock; Monitor](../concepts/JV028.md) | 多线程抢共享数据 |
| [JV029 · Atomic; CAS; ConcurrentHashMap](../concepts/JV029.md) | 无锁计数、并发 Map |
| [JV030 · CompletableFuture; CompletionStage](../concepts/JV030.md) | 多个异步结果组合 |
| [JV031 · Virtual thread; 虚拟线程](../concepts/JV031.md) | 大量阻塞式 IO、线程太贵 |
| [JV032 · Interruption; ThreadLocal](../concepts/JV032.md) | 取消线程、请求上下文串了 |
| [JV033 · Heap; Stack; GC; Reachability](../concepts/JV033.md) | 内存泄露、频繁回收 |
| [JV034 · JIT; Warm-up; Profiling](../concepts/JV034.md) | 第一次慢、基准不稳定 |
| [JV035 · ClassLoader; Classpath; JPMS; Module path](../concepts/JV035.md) | 同名类不能转换、模块不可见 |
| [JV036 · NoClassDefFoundError; ClassNotFoundException; NoSuchMethodError](../concepts/JV036.md) | 编译正常运行缺类缺方法 |
| [JV037 · NIO; Buffer; Channel; Charset](../concepts/JV037.md) | 文件读写、乱码、网络缓冲区 |
| [JV038 · java.time; Instant; LocalDateTime; ZoneId](../concepts/JV038.md) | 时区错、时间比较 |
| [JV039 · BigDecimal; Precision; Scale; RoundingMode](../concepts/JV039.md) | 小数不准、金额舍入 |
| [JV040 · Spring; IoC; DI; Bean; ApplicationContext](../concepts/JV040.md) | 自动注入、Bean 找不到 |
| [JV041 · Spring Boot; Auto-configuration; Profile](../concepts/JV041.md) | 自动配置、不同环境配置 |
| [JV042 · AOP; Proxy; Transactional; 事务代理](../concepts/JV042.md) | 注解事务没生效、自调用 |
| [JV043 · JPA; Hibernate; Entity; Persistence context](../concepts/JV043.md) | 实体持久化、懒加载异常 |
| [JV044 · JUnit; Test fixture; Mock; Integration test](../concepts/JV044.md) | Java 测试、模拟依赖 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 Java 领域基线，将语言与 JVM 概念落实为对象契约、资源生命周期及运行证据，具体行为以项目环境核对。

### 关键特征

- 区分语言语义、库契约和运行时表现，不从一次运行结果推断通用保证。
- 对象的可变性、相等性及共享范围需要一致设计，尤其关注集合键与并发访问。
- 资源释放和异常传播属于行为契约，不能只验收正常返回值。

### 如何落实

- 从构建配置确定编译与运行环境，明确本次方法的输入、空值、异常和线程使用约定。
- 按实际调用关系确定对象所有者、共享方式及集合语义，必要时约束可变字段的修改时机。
- 为文件、连接、线程任务等涉及的资源安排关闭或取消路径，保留有诊断价值的异常上下文。
- 若任务是性能或内存问题，采集与症状对应的分配、线程或堆证据，再限定修改点。

### 如何验收

- 用边界输入与异常路径核对方法契约，确认调用者能够区分预期失败和程序错误。
- 对涉及相等性或排序的对象检查集合行为；对共享可变对象检查并发读写结果。
- 在重复运行与失败退出后核对相关资源数量，性能变更用相同负载及运行阶段作对照。

### 常见误用

- 只根据关键字名称推断线程安全、可见性或跨版本库行为。
- 通过吞掉异常或盲目增大堆空间掩盖所有权与资源泄漏问题。
