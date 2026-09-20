# Java 与 JVM

检索分组：语言、对象与类型、集合与函数、并发、运行时、后端框架。
构建依赖见 [tooling.md](tooling.md)，互操作见 [kotlin.md](kotlin.md)，模组见 [minecraft.md](minecraft.md)。来源入口 S18、S30、S31，见 [sources.md](sources.md)。语言特性以项目 JDK、release 和预览开关为准，不因官方文档介绍新特性就升级项目。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| JV001 | JDK; JVM; Java SE; Runtime | Java 环境、编译与运行版本 | JDK 提供开发工具，JVM 执行字节码，SE 定义平台规范 | Java 与 JavaScript 是不同语言 |
| JV002 | Bytecode; Class file; javac; release | 编译能过运行版本不支持 | 编译器生成目标版本类文件 | 字节码版本、所用 API 与运行时都要兼容 |
| JV003 | Primitive; Reference; Boxing; Unboxing | int 和 Integer、空值拆箱 | 区分基本值、对象引用及包装转换 | 包装类缓存不能作为相等判断依据 |
| JV004 | Pass-by-value; 值传递 | 方法里改参数为何不同 | 参数接收值副本，对象参数复制的是引用值 | 修改对象内容不同于重新绑定调用方变量 |
| JV005 | equals; hashCode; Identity | HashMap 找不到、对象比较 | 区分逻辑相等和引用身份，保持哈希契约 | 改变键的参与哈希字段会破坏查找预期 |
| JV006 | final; Immutability; 不可变对象 | 不让修改、线程安全共享 | final 限制重新赋值，不可变性约束可观察状态变化 | final 引用指向的对象仍可能可变 |
| JV007 | Class; Interface; Abstract class | 抽象接口、继承实现 | 用类与接口表达契约、状态和实现复用 | 组合与继承应依实际替换关系选择 |
| JV008 | Overload; Override; Dynamic dispatch | 同名方法、重载重写 | 重载按签名选择，重写参与动态分派 | static 方法隐藏不等于实例方法重写 |
| JV009 | Access modifier; Package; Encapsulation | private、包可见、访问不到 | 用访问级别限制实现暴露 | package-private 与 protected 语义不同 |
| JV010 | Generics; Type parameter; Type erasure; 类型擦除 | 泛型、运行时取不到 T | 用类型参数检查复用代码，运行时存在擦除限制 | 泛型不能自动提供完整运行时类型验证 |
| JV011 | Wildcard; Bounded type; PECS | extends/super、不知道泛型怎么传 | 用上下界表达协变读取或逆变写入需求 | List 子类型关系不能按元素继承直接推导 |
| JV012 | Raw type; Heap pollution; Unchecked cast | 未检查转换警告、泛型污染 | 绕过泛型约束可能将错误延迟到运行时 | suppress warning 不是证明转换安全 |
| JV013 | Record; 数据载体 | DTO、少写样板代码 | 声明以组件值为中心的数据类型 | record 的引用组件不自动深度不可变 |
| JV014 | Enum; Sealed class; Pattern matching | 固定状态、穷举分支 | 用枚举、受限继承及模式匹配表达有限形态 | 可用语法及穷举规则随 JDK 版本核对 |
| JV015 | Exception; Checked/Unchecked; try/finally | 异常传播、要不要 throws | 区分编译期处理要求与运行时异常 | 不吞掉根因或无区别捕获全部 Throwable |
| JV016 | AutoCloseable; try-with-resources | 文件句柄泄露、连接没关 | 以词法作用域确定资源关闭 | GC 不是及时关闭外部资源的替代 |
| JV017 | Annotation; Reflection; Retention | 注解读取不到、动态调用 | 元数据通过保留策略及反射参与处理 | 注解本身不自动执行逻辑 |
| JV018 | Annotation processing; APT; Generated source | 自动生成代码、编译期处理 | 在编译过程中读取注解生成产物 | 编译期处理器不同于运行时反射 |
| JV019 | List; Set; Map; Collection | 有序列表、去重、键值查找 | 用不同集合契约表达内容组织 | 顺序、重复、null 支持要按实现核对 |
| JV020 | Iterator; Fail-fast; ConcurrentModificationException | 遍历时删除报错 | 迭代器有各自结构变更规则 | fail-fast 不是并发安全保证 |
| JV021 | Comparator; Comparable; Stable sort | 自定义排序、排序不稳定 | 定义自然顺序或外部比较规则 | 比较器需保持契约，避免减法溢出比较 |
| JV022 | Lambda; Functional interface; Method reference | 回调、方法引用 | 将行为传给单抽象方法接口 | 捕获局部变量受 effectively final 约束 |
| JV023 | Stream API; Intermediate/Terminal operation | 集合过滤聚合、流只执行一次 | 用惰性流水线组合数据处理 | Stream 不是 IO 流，也不天然可重复消费 |
| JV024 | Collector; groupingBy; parallelStream | 分组统计、并行流 | 定义归约容器或并行处理 | 并行不保证更快，副作用和公共线程池有风险 |
| JV025 | Optional | 返回值可能不存在 | 显式建模可缺失结果 | Optional 不替代全部 null 策略或异常机制 |
| JV026 | Thread; ExecutorService; Thread pool | 后台任务、线程池耗尽 | 分离任务提交与线程管理 | 无界队列、阻塞任务及关闭策略需设计 |
| JV027 | Java Memory Model; Happens-before; volatile | 多线程看不到更新 | 用内存模型描述可见性和有序关系 | volatile 不让复合读改写自动原子化 |
| JV028 | synchronized; Lock; Monitor | 多线程抢共享数据 | 通过互斥及约定协调共享状态 | 所有访问必须遵守同一同步协议 |
| JV029 | Atomic; CAS; ConcurrentHashMap | 无锁计数、并发 Map | 提供特定原子操作或并发容器 | 多个线程安全操作串联未必整体原子 |
| JV030 | CompletableFuture; CompletionStage | 多个异步结果组合 | 表达异步依赖与完成处理 | join/get 会等待，执行器与异常传播需明确 |
| JV031 | Virtual thread; 虚拟线程 | 大量阻塞式 IO、线程太贵 | 用运行时管理的轻量线程承载并发任务 | 不增加 CPU 算力；兼容及限制以 JDK 核对 |
| JV032 | Interruption; ThreadLocal | 取消线程、请求上下文串了 | 中断表达协作取消，线程局部变量绑定线程 | 线程复用需清理；上下文不自动跨异步传播 |
| JV033 | Heap; Stack; GC; Reachability | 内存泄露、频繁回收 | 区分对象存储、调用帧与可达性回收 | 可达但无用的对象仍可能形成逻辑泄露 |
| JV034 | JIT; Warm-up; Profiling | 第一次慢、基准不稳定 | 运行时编译及优化影响性能表现 | 微基准需控制预热、死代码消除与测量环境 |
| JV035 | ClassLoader; Classpath; JPMS; Module path | 同名类不能转换、模块不可见 | 类身份含加载器，模块可限制可读与导出边界 | 依赖存在不等于加载和访问一定成功 |
| JV036 | NoClassDefFoundError; ClassNotFoundException; NoSuchMethodError | 编译正常运行缺类缺方法 | 定位运行时依赖、初始化或二进制兼容问题 | 缺类也可能由类初始化失败引发 |
| JV037 | NIO; Buffer; Channel; Charset | 文件读写、乱码、网络缓冲区 | 以通道/缓冲区操作数据并显式处理编码 | 字节不等于字符，字符数不等于字节数 |
| JV038 | java.time; Instant; LocalDateTime; ZoneId | 时区错、时间比较 | 区分时间线上的点与本地日期时间 | LocalDateTime 本身没有时区或偏移 |
| JV039 | BigDecimal; Precision; Scale; RoundingMode | 小数不准、金额舍入 | 控制十进制精度、尺度和舍入 | 从二进制浮点构造仍可能带入误差 |
| JV040 | Spring; IoC; DI; Bean; ApplicationContext | 自动注入、Bean 找不到 | 容器管理对象创建、装配与生命周期 | Spring 不是 Java 语言本身，组件扫描有边界 |
| JV041 | Spring Boot; Auto-configuration; Profile | 自动配置、不同环境配置 | 按依赖和条件提供配置及环境选择 | 自动配置不等于无配置，也不应盲目覆盖已有配置 |
| JV042 | AOP; Proxy; Transactional; 事务代理 | 注解事务没生效、自调用 | 通过代理等机制织入横切行为 | 代理模式下自调用可能绕过拦截，需核对配置 |
| JV043 | JPA; Hibernate; Entity; Persistence context | 实体持久化、懒加载异常 | 用持久化上下文管理实体映射及变更 | JPA 是规范，Hibernate 是实现之一；查询成本仍存在 |
| JV044 | JUnit; Test fixture; Mock; Integration test | Java 测试、模拟依赖 | 组织测试生命周期及依赖替身 | mock 测试不能替代关键真实集成行为 |
