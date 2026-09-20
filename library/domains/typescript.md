# TypeScript

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [TS001 · TypeScript; TS; Type erasure](../concepts/TS001.md) | TS 类型运行时去哪了 |
| [TS002 · Annotation; Inference; Contextual typing](../concepts/TS002.md) | 要不要手写类型、自动推导 |
| [TS003 · Structural typing; Excess property check](../concepts/TS003.md) | 结构一样为什么能赋值 |
| [TS004 · any; unknown](../concepts/TS004.md) | 不知道类型、接口返回任意数据 |
| [TS005 · never; void](../concepts/TS005.md) | 不可能出现、函数没返回值 |
| [TS006 · Union; 联合类型](../concepts/TS006.md) | 两种类型都可能、状态分支 |
| [TS007 · Intersection; 交叉类型](../concepts/TS007.md) | 合并多个约束 |
| [TS008 · Literal type; Widening; as const](../concepts/TS008.md) | 字符串变宽、保留字面值 |
| [TS009 · interface; type alias; Declaration merging](../concepts/TS009.md) | 接口还是类型别名 |
| [TS010 · Optional property; readonly; ReadonlyArray](../concepts/TS010.md) | 字段可选、只读集合 |
| [TS011 · Tuple; Variadic tuple](../concepts/TS011.md) | 固定位置参数、不同类型数组 |
| [TS012 · Narrowing; Control-flow analysis](../concepts/TS012.md) | 判断后类型变精确 |
| [TS013 · Discriminated union; Exhaustiveness](../concepts/TS013.md) | 多状态数据、漏处理状态 |
| [TS014 · Type predicate; Assertion function](../concepts/TS014.md) | 自定义 isX 判断、验证函数 |
| [TS015 · Type assertion; 类型断言; as; Non-null assertion](../concepts/TS015.md) | 强制转类型、感叹号消报错 |
| [TS016 · satisfies](../concepts/TS016.md) | 校验结构但保留推导 |
| [TS017 · Generic; Constraint; extends](../concepts/TS017.md) | 泛型函数、约束字段存在 |
| [TS018 · keyof; Type query typeof; Indexed access](../concepts/TS018.md) | 根据对象生成键类型 |
| [TS019 · Mapped type; Key remapping](../concepts/TS019.md) | 批量改可选、重命名类型键 |
| [TS020 · Conditional type; infer; Distributivity](../concepts/TS020.md) | 提取 Promise 内类型、条件类型 |
| [TS021 · Template literal type](../concepts/TS021.md) | 拼接类型字符串、事件名约束 |
| [TS022 · Utility types; Partial/Required/Pick/Omit/Record](../concepts/TS022.md) | 复用 DTO、选字段、字典类型 |
| [TS023 · ReturnType; Parameters; Awaited](../concepts/TS023.md) | 复用函数输入输出类型 |
| [TS024 · Overload signature; Function variance](../concepts/TS024.md) | 函数多种调用方式、回调不兼容 |
| [TS025 · enum; const enum](../concepts/TS025.md) | 枚举值与编译产物 |
| [TS026 · Declaration file; .d.ts; Ambient declaration](../concepts/TS026.md) | 第三方库没类型、declare |
| [TS027 · Module augmentation; Global augmentation](../concepts/TS027.md) | 给库扩展类型 |
| [TS028 · import type; export type](../concepts/TS028.md) | 仅类型导入、运行时找不到导出 |
| [TS029 · strict; strictNullChecks; noImplicitAny](../concepts/TS029.md) | 开严格检查、漏空值 |
| [TS030 · tsconfig; target; lib; moduleResolution](../concepts/TS030.md) | 有类型但浏览器运行不了 |
| [TS031 · Project references; Incremental build](../concepts/TS031.md) | 多包 TS 构建很慢 |
| [TS032 · Runtime validation; Schema; Type guard](../concepts/TS032.md) | 接口 JSON 类型撒谎 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 TypeScript 领域基线，将类型概念落实为可表达的状态与调用约束，同时保留运行时数据边界。

### 关键特征

- 类型应描述真实可出现的值与状态，而不是为了消除报错伪造保证。
- 静态类型检查与运行时输入验证分别承担责任。
- 泛型和类型工具只服务于真实的输入输出关系，避免不必要的类型复杂度。

### 如何落实

- 从实际生产者和消费者提取数据形状，区分缺失、空值、失败和成功状态。
- 在外部输入处验证或解析未知数据，再通过可辨别的状态和收窄传递已确认的信息。
- 用最小类型关系约束 API，核对可变数据、回调和泛型参数的使用方向。
- 沿项目编译配置检查声明与实际实现，并保留调用端的类型推导和错误提示质量。

### 如何验收

- 确认合法调用能够通过检查，代表性的非法状态组合或参数确实被拒绝。
- 输入不符合声明的外部数据，确认运行时边界能识别错误而非继续使用。
- 核对生成或维护的公开声明与实现一致，类型修改未迫使调用方添加无依据断言。

### 常见误用

- 使用断言或宽泛类型绕过错误，把未验证数据包装为可信数据。
- 把编译通过当作序列化数据、网络响应和业务规则已经验证。
