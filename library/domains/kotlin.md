# Kotlin

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [KT001 · val; var; Read-only property](../concepts/KT001.md) | 只读属性、变量不能重新赋值 |
| [KT002 · Null safety; Nullable; Safe call; Elvis; !!](../concepts/KT002.md) | 空安全、问号、空值兜底 |
| [KT003 · Smart cast; as?; Type check](../concepts/KT003.md) | 判断类型后直接用、智能转换 |
| [KT004 · Any; Unit; Nothing](../concepts/KT004.md) | 无返回值、永不返回、所有类型 |
| [KT005 · Expression; when; if; Exhaustiveness](../concepts/KT005.md) | 分支返回值、漏分支 |
| [KT006 · Data class; copy; Destructuring](../concepts/KT006.md) | 数据对象复制、解构 |
| [KT007 · Sealed class/interface; enum class](../concepts/KT007.md) | 有多种数据形态的状态 |
| [KT008 · object; Companion object; Object expression](../concepts/KT008.md) | 单例、伴生对象、匿名对象 |
| [KT009 · Primary/Secondary constructor; init](../concepts/KT009.md) | 初始化顺序、构造函数 |
| [KT010 · open; override; final; internal](../concepts/KT010.md) | Kotlin 类不能继承、模块可见 |
| [KT011 · Extension function/property; 扩展函数](../concepts/KT011.md) | 给现有类补方法 |
| [KT012 · Receiver; Function type with receiver; DSL](../concepts/KT012.md) | this 不知道是谁、类型安全 DSL |
| [KT013 · Higher-order function; Lambda; Trailing lambda](../concepts/KT013.md) | 函数作参数、尾随 lambda |
| [KT014 · Scope functions; let/run/with/apply/also](../concepts/KT014.md) | 链式处理、初始化对象 |
| [KT015 · Inline; noinline; crossinline; Non-local return](../concepts/KT015.md) | lambda 里 return 跳出哪里 |
| [KT016 · Reified type parameter](../concepts/KT016.md) | 运行时用 T 判断类型 |
| [KT017 · Variance; in/out; Star projection](../concepts/KT017.md) | 泛型型变、星投影 |
| [KT018 · Delegation; by; Delegated property; lazy](../concepts/KT018.md) | 属性委托、延迟初始化 |
| [KT019 · lateinit; Backing field; Custom accessor](../concepts/KT019.md) | 属性稍后赋值、getter/setter |
| [KT020 · Read-only/Mutable collections](../concepts/KT020.md) | List 为什么还能被别人改 |
| [KT021 · Sequence; Collection pipeline](../concepts/KT021.md) | 链式集合处理分配多 |
| [KT022 · Equality; ==; ===](../concepts/KT022.md) | Kotlin 相等和同一对象 |
| [KT023 · Operator overloading; Infix](../concepts/KT023.md) | 自定义操作符、中缀调用 |
| [KT024 · Suspend function; suspend; 挂起函数](../concepts/KT024.md) | suspend 会自动开线程吗 |
| [KT025 · CoroutineScope; Structured concurrency; Job](../concepts/KT025.md) | 页面关了任务还跑 |
| [KT026 · launch; async; Deferred; await](../concepts/KT026.md) | 协程并发取结果 |
| [KT027 · Dispatcher; CoroutineContext; withContext](../concepts/KT027.md) | 切 IO 线程、回主线程 |
| [KT028 · Cancellation; CancellationException; ensureActive](../concepts/KT028.md) | 取消没反应、任务停不下 |
| [KT029 · SupervisorJob; supervisorScope; Exception propagation](../concepts/KT029.md) | 一个任务失败全部取消 |
| [KT030 · runBlocking](../concepts/KT030.md) | 在同步入口等协程完成 |
| [KT031 · Flow; Cold flow; collect](../concepts/KT031.md) | 异步连续数据、订阅才执行 |
| [KT032 · StateFlow; SharedFlow; Hot flow](../concepts/KT032.md) | 当前状态、多订阅广播 |
| [KT033 · Channel; Mutex; Coroutine synchronization](../concepts/KT033.md) | 协程通信、共享计数 |
| [KT034 · Platform type; Java interop; SAM conversion](../concepts/KT034.md) | Java 返回值能为空吗 |
| [KT035 · JvmStatic; JvmField; JvmOverloads; JvmName](../concepts/KT035.md) | Java 调不到 Kotlin API |
| [KT036 · Value class; JvmInline](../concepts/KT036.md) | 轻量 ID 包装、避免混类型 |
| [KT037 · Kotlin Multiplatform; KMP; expect/actual](../concepts/KT037.md) | 多平台共享逻辑 |
| [KT038 · kotlinx.serialization; Serializer; SerialName](../concepts/KT038.md) | Kotlin 对象转 JSON |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 Kotlin 领域基线，将空安全、扩展和异步概念落实为调用契约、作用域与生命周期，沿用现有 Kotlin 写法。

### 关键特征

- 空值含义应来自业务与互操作边界，不用强制断言替代输入契约。
- 异步任务的所有者、取消时机和错误传播需要与业务生命周期对应。
- 扩展函数与泛型设计依据真实调用方，不为语法简短增加隐藏状态或宽泛抽象。

### 如何落实

- 定位现有类型、扩展及调用方，确认接收者语义、可空值来源和 Java 互操作边界。
- 用项目已有的类型表达合法状态，在边界处理外部空值和错误，不把不确定性传播为随处断言。
- 若涉及协程或数据流，明确作用域所有者、执行上下文、收集生命周期和取消后的资源处理。
- 沿现有 API 风格实现最小修改，核对重载、扩展解析及调用端类型推导是否仍表达原意。

### 如何验收

- 覆盖空值、缺失值和互操作输入，确认错误发生在可解释的边界。
- 在任务取消、收集者离开和上游失败时核对副作用、资源与错误传播。
- 编译实际 Kotlin 及相关 Java 调用端，核对 API 可用性与预期分派行为。

### 常见误用

- 把挂起标记理解为自动切换线程或自动免除阻塞成本。
- 创建无明确所有者的异步作用域，或用扩展函数隐藏跨对象可变状态。
