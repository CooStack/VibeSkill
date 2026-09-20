# 程序语言与编译系统

用于定位语言语义、编译阶段、类型、链接与内存管理问题。S60 为 LLVM IR 资料入口而非所有语言的共同规范，见 [sources.md](sources.md)。Java/Kotlin/JS/TS 特有规则仍回到各自参考。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| LC001 | Lexer; Tokenization; 词法分析 | 把源代码切成 token | 将字符序列识别为词法单元 | 编程语言 token 与 LLM token 不同 |
| LC002 | Parser; Grammar; 语法分析 | 表达式解析、优先级 | 按文法组织 token，处理结合性和语法错误 | 任意嵌套语法一般不应靠单条正则替代解析器 |
| LC003 | AST; Abstract syntax tree; 抽象语法树 | 代码变换、语法结构 | 保留表达程序含义所需的树结构 | AST 通常不保留全部排版；格式保真需要 token/CST 等信息 |
| LC004 | CST; Concrete syntax tree; 具体语法树 | 格式化不能丢注释 | 更完整保留语法层次以支持源代码工具 | 是否保留空白和注释取决于工具，不凭名称保证 |
| LC005 | Name resolution; Scope; 名称解析与作用域 | 同名变量、找不到符号 | 按作用域和绑定规则确定名字指向 | 词法作用域、动态作用域与对象生命周期不同 |
| LC006 | Type checking; Type inference; 类型检查与推导 | 不写类型也能检查 | 检查表达式的类型关系，或从约束推导类型 | 静态/动态类型与强/弱类型不是同一轴 |
| LC007 | Nominal/Structural typing; 名义与结构类型 | 字段相同却不兼容 | 区分按声明身份还是结构判定类型关系 | 具体语言常混合机制，需核对兼容和可见性规则 |
| LC008 | Subtyping; Variance; 型变 | 泛型协变逆变 | 分析类型替代关系及泛型参数的方向 | 可变容器尤其不能随意协变；继承不等于所有替代都安全 |
| LC009 | Operational/Denotational semantics; 程序语义 | 语法合法但行为不清楚 | 分别用执行步骤或数学对象描述程序含义 | 规范语义与某次实现的偶然行为不同 |
| LC010 | IR; Intermediate representation; 中间表示 | 编译器中间代码、优化通道 | 在源语言和目标机器间表达可分析的程序结构 | IR 有多个层次，不都与机器指令一一对应 |
| LC011 | SSA; Static single assignment | 变量只赋值一次、phi 节点 | 用每个值一次定义的形式简化数据流分析 | SSA 是表示约定，不代表源语言禁止变量更新 |
| LC012 | CFG; Control-flow graph; 控制流图 | 基本块、分支流向 | 以基本块及可能跳转表示执行路径 | 此处 CFG 不是 context-free grammar，需消歧 |
| LC013 | Data-flow analysis; 数据流分析 | 活跃变量、到达定义 | 在控制流上推导程序点的抽象事实 | 静态分析常作保守近似，不等于实际执行轨迹 |
| LC014 | Optimization pass; Constant folding; DCE | 常量折叠、死代码消除 | 在语义约束下改写程序以改善成本 | 浮点、异常、可观察副作用约束优化合法性 |
| LC015 | Code generation; Register allocation | 汇编生成、寄存器溢出 | 将中间表示降低到目标指令并分配寄存器 | 寄存器不够的 spill 是内存暂存，不是整数溢出 |
| LC016 | ABI; Calling convention; 二进制接口 | 库能编译但调用崩溃 | 约定参数、返回值、布局及二进制互操作 | API 源码兼容不保证 ABI 兼容 |
| LC017 | Linker; Symbol; Relocation; 链接 | undefined reference、重复符号 | 组合目标文件、解析符号并修正地址引用 | 链接错误与运行时类/模块加载错误需区分 |
| LC018 | Static/Dynamic linking; 静态与动态链接 | 动态库找不到、部署缺库 | 区分构建时纳入代码和运行时依赖共享库 | 动态链接不自动保证可热替换或版本兼容 |
| LC019 | Interpreter; JIT; AOT; 执行策略 | 解释执行、运行时编译 | 区分解释、即时编译与提前编译及混合实现 | 不能仅凭语言名称认定其唯一执行方式 |
| LC020 | Ownership; Borrowing; Lifetime | 悬空指针、借用冲突 | 跟踪资源拥有者、访问权限及有效期 | 所有权不只是引用计数；规则依语言和类型而异 |
| LC021 | Undefined behavior; UB; 未定义行为 | 某编译器正常换一个出错 | 规范未对某执行施加要求的情形 | 不同于未指定行为或实现定义行为，也不保证必然崩溃 |
| LC022 | Functional programming; FP; 纯函数 | 副作用难测、函数组合 | 以函数、不可变数据等组织计算并控制副作用 | 函数式不是完全没有副作用，也不是只用 lambda |
| LC023 | Closure conversion; 闭包转换 | 捕获变量如何存储 | 将自由变量和可调用代码组合为运行时表示 | 捕获按值/引用及逃逸影响生命周期，不能跨语言套用 |
| LC024 | FFI; Foreign function interface | Java 调原生库、跨语言互调 | 在不同语言/运行时之间桥接调用与数据 | 需明确 ABI、所有权、异常边界和线程约束 |
