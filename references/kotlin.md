# Kotlin

检索分组：类型与空安全、表达式与对象、函数与集合、协程、互操作与多平台。
JVM 共通概念见 [java.md](java.md)，构建与 KSP 见 [tooling.md](tooling.md)。来源 S19、S20，见 [sources.md](sources.md)。协程框架能力与 suspend 语言机制分开理解。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| KT001 | val; var; Read-only property | 只读属性、变量不能重新赋值 | val 禁止通过该属性重新赋值，var 允许 | val 不意味着指向的集合或对象深度不可变 |
| KT002 | Null safety; Nullable; Safe call; Elvis; !! | 空安全、问号、空值兜底 | 类型和操作符显式处理可能缺失的值 | 非空断言可能抛异常；Java 平台类型仍有风险 |
| KT003 | Smart cast; as?; Type check | 判断类型后直接用、智能转换 | 由控制流信息推导更具体的可用类型 | 可变属性、自定义 getter 等可能阻止智能转换 |
| KT004 | Any; Unit; Nothing | 无返回值、永不返回、所有类型 | 区分非空顶层类型、正常完成值与无正常结果的底类型 | Unit 不是 Java void 在所有场景的直接同义 |
| KT005 | Expression; when; if; Exhaustiveness | 分支返回值、漏分支 | 将条件选择作为表达式并利用穷举检查 | 开放类型不能假定枚举所有子类型 |
| KT006 | Data class; copy; Destructuring | 数据对象复制、解构 | 自动提供基于主构造属性的常见操作 | copy 是浅复制，类体属性不都参与自动操作 |
| KT007 | Sealed class/interface; enum class | 有多种数据形态的状态 | 受限类型层级或固定实例集表达变体 | 子类允许范围和穷举行为依平台/版本核对 |
| KT008 | object; Companion object; Object expression | 单例、伴生对象、匿名对象 | 分别定义单例声明、类关联对象或临时实现 | companion 成员不都直接等同 Java static |
| KT009 | Primary/Secondary constructor; init | 初始化顺序、构造函数 | 定义构造入口及初始化逻辑 | 初始化时访问开放成员可能触及未就绪状态 |
| KT010 | open; override; final; internal | Kotlin 类不能继承、模块可见 | 声明继承可扩展性与模块内可见范围 | internal 的模块边界不是 Java package |
| KT011 | Extension function/property; 扩展函数 | 给现有类补方法 | 在调用语法上扩展可用函数或属性 | 按接收者静态类型解析，不真正修改目标类 |
| KT012 | Receiver; Function type with receiver; DSL | this 不知道是谁、类型安全 DSL | 用接收者作用域组织声明式调用 | 隐式接收者多层嵌套时需明确归属 |
| KT013 | Higher-order function; Lambda; Trailing lambda | 函数作参数、尾随 lambda | 用函数值抽象行为 | 留意捕获可变状态和返回目标 |
| KT014 | Scope functions; let/run/with/apply/also | 链式处理、初始化对象 | 按接收者名称和返回值选择作用域函数 | 不堆叠作用域函数制造隐式上下文 |
| KT015 | Inline; noinline; crossinline; Non-local return | lambda 里 return 跳出哪里 | 控制内联和函数参数返回行为 | inline 不是所有函数都更快，可能增加代码体积 |
| KT016 | Reified type parameter | 运行时用 T 判断类型 | 在可内联位置保留具体类型操作的机会 | 不会自动保留嵌套泛型的所有类型信息 |
| KT017 | Variance; in/out; Star projection | 泛型型变、星投影 | 定义参数的消费/产出关系与未知类型投影 | 型变不代表容器可随意写入任意类型 |
| KT018 | Delegation; by; Delegated property; lazy | 属性委托、延迟初始化 | 将接口或属性访问行为委托给其他对象 | lazy 的线程安全模式与重入需要按环境选择 |
| KT019 | lateinit; Backing field; Custom accessor | 属性稍后赋值、getter/setter | 支持受约束的延迟初始化或自定义访问 | lateinit 未初始化访问会失败，不替代完整生命周期设计 |
| KT020 | Read-only/Mutable collections | List 为什么还能被别人改 | 区分只读接口和可变接口 | 只读视图不保证底层不可变或线程安全 |
| KT021 | Sequence; Collection pipeline | 链式集合处理分配多 | 用惰性序列组合处理避免部分中间集合 | 小集合可能更慢，副作用执行时机不同 |
| KT022 | Equality; ==; === | Kotlin 相等和同一对象 | 分别表达结构相等和引用身份 | 自定义 equals 契约仍需与 hashCode 一致 |
| KT023 | Operator overloading; Infix | 自定义操作符、中缀调用 | 用约定函数承载特定语法 | 语法简洁不能牺牲语义可预测性 |
| KT024 | Suspend function; suspend; 挂起函数 | suspend 会自动开线程吗 | 声明函数可参与挂起/恢复；不自行指定执行线程（S20） | 调用阻塞代码仍会阻塞承载线程 |
| KT025 | CoroutineScope; Structured concurrency; Job | 页面关了任务还跑 | 用作用域与父子任务管理生命周期和完成 | 脱离归属的全局任务需明确必要性 |
| KT026 | launch; async; Deferred; await | 协程并发取结果 | launch 返回 Job，async 提供可等待结果 | async 后立即 await 不等于多个工作已并行启动 |
| KT027 | Dispatcher; CoroutineContext; withContext | 切 IO 线程、回主线程 | 将调度与上下文传入协程执行 | 调度器不自动让共享状态线程安全 |
| KT028 | Cancellation; CancellationException; ensureActive | 取消没反应、任务停不下 | 协作式取消依赖挂起点或主动检查 | 不无意吞掉取消异常；CPU 循环也需响应取消 |
| KT029 | SupervisorJob; supervisorScope; Exception propagation | 一个任务失败全部取消 | 定义子任务失败的隔离及处理关系 | 监督不等于异常会自动被忽略或恢复 |
| KT030 | runBlocking | 在同步入口等协程完成 | 阻塞当前线程直到内部工作结束 | 不把它当 UI 或服务器 Tick 线程的异步方案 |
| KT031 | Flow; Cold flow; collect | 异步连续数据、订阅才执行 | 用可挂起流表达逐项产生和消费 | 冷流通常按收集者启动，不能等同共享热流 |
| KT032 | StateFlow; SharedFlow; Hot flow | 当前状态、多订阅广播 | StateFlow 表达当前值，SharedFlow 配置共享事件流 | 重放、缓冲、相等合并及事件丢失策略要明确 |
| KT033 | Channel; Mutex; Coroutine synchronization | 协程通信、共享计数 | 用通道传值或可挂起互斥协调状态 | 通道不是任意场景下的广播流 |
| KT034 | Platform type; Java interop; SAM conversion | Java 返回值能为空吗 | 处理 Java 空注解缺失、接口和类型边界 | 平台类型削弱空安全，不能当确定非空（S19） |
| KT035 | JvmStatic; JvmField; JvmOverloads; JvmName | Java 调不到 Kotlin API | 控制生成的 JVM 接口形态 | 默认参数和扩展函数不会自动成为 Java 同形语法 |
| KT036 | Value class; JvmInline | 轻量 ID 包装、避免混类型 | 用受约束的包装类型表达语义并允许部分内联表示 | 泛型、可空或接口使用时可能装箱 |
| KT037 | Kotlin Multiplatform; KMP; expect/actual | 多平台共享逻辑 | 共享代码并声明平台相关实现边界 | JVM 库不能直接用于所有平台 source set |
| KT038 | kotlinx.serialization; Serializer; SerialName | Kotlin 对象转 JSON | 通过序列化规则和生成支持处理数据 | 是库/插件能力，不等同语言自带任意对象序列化 |
