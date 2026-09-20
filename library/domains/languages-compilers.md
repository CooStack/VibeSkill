# 程序语言与编译系统

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [LC001 · Lexer; Tokenization; 词法分析](../concepts/LC001.md) | 把源代码切成 token |
| [LC002 · Parser; Grammar; 语法分析](../concepts/LC002.md) | 表达式解析、优先级 |
| [LC003 · AST; Abstract syntax tree; 抽象语法树](../concepts/LC003.md) | 代码变换、语法结构 |
| [LC004 · CST; Concrete syntax tree; 具体语法树](../concepts/LC004.md) | 格式化不能丢注释 |
| [LC005 · Name resolution; Scope; 名称解析与作用域](../concepts/LC005.md) | 同名变量、找不到符号 |
| [LC006 · Type checking; Type inference; 类型检查与推导](../concepts/LC006.md) | 不写类型也能检查 |
| [LC007 · Nominal/Structural typing; 名义与结构类型](../concepts/LC007.md) | 字段相同却不兼容 |
| [LC008 · Subtyping; Variance; 型变](../concepts/LC008.md) | 泛型协变逆变 |
| [LC009 · Operational/Denotational semantics; 程序语义](../concepts/LC009.md) | 语法合法但行为不清楚 |
| [LC010 · IR; Intermediate representation; 中间表示](../concepts/LC010.md) | 编译器中间代码、优化通道 |
| [LC011 · SSA; Static single assignment](../concepts/LC011.md) | 变量只赋值一次、phi 节点 |
| [LC012 · CFG; Control-flow graph; 控制流图](../concepts/LC012.md) | 基本块、分支流向 |
| [LC013 · Data-flow analysis; 数据流分析](../concepts/LC013.md) | 活跃变量、到达定义 |
| [LC014 · Optimization pass; Constant folding; DCE](../concepts/LC014.md) | 常量折叠、死代码消除 |
| [LC015 · Code generation; Register allocation](../concepts/LC015.md) | 汇编生成、寄存器溢出 |
| [LC016 · ABI; Calling convention; 二进制接口](../concepts/LC016.md) | 库能编译但调用崩溃 |
| [LC017 · Linker; Symbol; Relocation; 链接](../concepts/LC017.md) | undefined reference、重复符号 |
| [LC018 · Static/Dynamic linking; 静态与动态链接](../concepts/LC018.md) | 动态库找不到、部署缺库 |
| [LC019 · Interpreter; JIT; AOT; 执行策略](../concepts/LC019.md) | 解释执行、运行时编译 |
| [LC020 · Ownership; Borrowing; Lifetime](../concepts/LC020.md) | 悬空指针、借用冲突 |
| [LC021 · Undefined behavior; UB; 未定义行为](../concepts/LC021.md) | 某编译器正常换一个出错 |
| [LC022 · Functional programming; FP; 纯函数](../concepts/LC022.md) | 副作用难测、函数组合 |
| [LC023 · Closure conversion; 闭包转换](../concepts/LC023.md) | 捕获变量如何存储 |
| [LC024 · FFI; Foreign function interface](../concepts/LC024.md) | Java 调原生库、跨语言互调 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为程序语言与编译系统领域基线，将语法、类型和转换概念落实为分阶段契约与可观察语义保持。

### 关键特征

- 词法、语法、绑定、类型、链接和执行错误分阶段定位。
- 表示转换应保持任务要求的语义；格式保真与行为保真是不同目标。
- 规范保证、实现约定和偶然运行结果分别记录，优化不能越过副作用与错误语义。

### 如何落实

- 明确输入语言子集、目标表示及需要保留的行为或源码信息，列出不支持的构造。
- 为受影响阶段定义输入输出不变量，保留必要的源位置以便诊断。
- 沿已有解析或转换设施实现修改，处理作用域、类型及控制流中与该变更相关的约束。
- 对生成代码或互操作边界核对布局、调用和资源所有权，用参考执行或阶段产物对照结果。

### 如何验收

- 用优先级、嵌套、遮蔽和非法输入样例核对受影响阶段及错误位置。
- 比较转换前后的结果、异常和可观察副作用，不能只比较最终数值。
- 对任务涉及的链接或跨语言调用验证参数、返回值及资源释放，区分源码兼容与二进制契约。

### 常见误用

- 用文本替换承担需要语法或绑定信息的变换，误改注释、字符串或同名符号。
- 把未定义或未核对的行为作为优化依据，再以某次执行正常证明合法。
