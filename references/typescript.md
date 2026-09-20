# TypeScript

检索分组：类型建模、控制流、泛型与类型操作、模块、检查配置。
运行时语义见 [javascript.md](javascript.md)，Vue 类型见 [vue.md](vue.md)，构建见 [tooling.md](tooling.md)。来源 S24，见 [sources.md](sources.md)。类型层面的通过不能代替外部数据验证。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| TS001 | TypeScript; TS; Type erasure | TS 类型运行时去哪了 | 在 JavaScript 上进行静态检查，类型信息大多被擦除 | 某些 TS 语法有运行时输出，不能概括为全都无输出 |
| TS002 | Annotation; Inference; Contextual typing | 要不要手写类型、自动推导 | 显式声明与上下文推导共同确定类型 | 避免无益重复注解，但公开边界应清晰 |
| TS003 | Structural typing; Excess property check | 结构一样为什么能赋值 | 根据结构兼容性检查赋值 | 新鲜对象字面量的多余属性检查有特定规则 |
| TS004 | any; unknown | 不知道类型、接口返回任意数据 | any 放宽检查，unknown 要先收窄后使用 | unknown 更适合未验证输入，但本身不验证内容（S24） |
| TS005 | never; void | 不可能出现、函数没返回值 | 分别表达无可能值和忽略返回值的特定契约 | void 回调的赋值规则不等同禁止任何返回值 |
| TS006 | Union; 联合类型 | 两种类型都可能、状态分支 | 值属于候选类型之一 | 使用成员前需证明对应类型可用 |
| TS007 | Intersection; 交叉类型 | 合并多个约束 | 值同时满足多组类型约束 | 冲突字段可能推导为 never，不是运行时合并对象 |
| TS008 | Literal type; Widening; as const | 字符串变宽、保留字面值 | 精确描述常量值并控制推导宽化 | as const 的只读类型约束不是运行时深冻结 |
| TS009 | interface; type alias; Declaration merging | 接口还是类型别名 | 声明对象契约或命名任意类型表达式 | 并非所有类型别名都能由 interface 替代 |
| TS010 | Optional property; readonly; ReadonlyArray | 字段可选、只读集合 | 限制类型检查下的可用字段与写入 | readonly 不保证对象在运行时绝对不可变 |
| TS011 | Tuple; Variadic tuple | 固定位置参数、不同类型数组 | 按位置表达长度和元素类型约束 | 普通数组元素联合不能完整替代元组结构 |
| TS012 | Narrowing; Control-flow analysis | 判断后类型变精确 | 使用分支、赋值和可达性收窄类型 | 类型断言绕过的是证明，不会改造值 |
| TS013 | Discriminated union; Exhaustiveness | 多状态数据、漏处理状态 | 用共同判别字段区分数据变体并检查穷举 | 判别字段需保持字面量精度及关联关系 |
| TS014 | Type predicate; Assertion function | 自定义 isX 判断、验证函数 | 向编译器表达收窄结论 | 声明的结论必须由实现保障，否则会产生虚假安全 |
| TS015 | Type assertion; 类型断言; as; Non-null assertion | 强制转类型、感叹号消报错 | 告知编译器按开发者断言解释类型（S24） | 不执行运行时转换或空值检查 |
| TS016 | satisfies | 校验结构但保留推导 | 检查表达式满足约束，同时保留较具体的推导信息 | 不取代运行时 schema 验证 |
| TS017 | Generic; Constraint; extends | 泛型函数、约束字段存在 | 将输入输出间类型关系参数化 | 无真实关系时多余类型参数增加复杂度 |
| TS018 | keyof; Type query typeof; Indexed access | 根据对象生成键类型 | 从已有值/类型提取键和属性类型 | 类型上下文 typeof 与 JS 运行时 typeof 不同 |
| TS019 | Mapped type; Key remapping | 批量改可选、重命名类型键 | 按键集合生成新的属性约束 | 不实际遍历或转换运行时对象 |
| TS020 | Conditional type; infer; Distributivity | 提取 Promise 内类型、条件类型 | 按类型条件推导分支或捕获子类型 | 对联合的分配行为有条件，需避免错误预期 |
| TS021 | Template literal type | 拼接类型字符串、事件名约束 | 在类型层组合有限字符串模式 | 大规模组合可能增加类型检查成本 |
| TS022 | Utility types; Partial/Required/Pick/Omit/Record | 复用 DTO、选字段、字典类型 | 用标准工具类型变换契约 | 默认多为浅层；Record 不是实际 Map 实例 |
| TS023 | ReturnType; Parameters; Awaited | 复用函数输入输出类型 | 从函数或异步结果提取关联类型 | 不保证外部返回的数据真的满足声明 |
| TS024 | Overload signature; Function variance | 函数多种调用方式、回调不兼容 | 描述调用签名并检查函数可赋值关系 | 实现签名与公开重载可见性不同 |
| TS025 | enum; const enum | 枚举值与编译产物 | 使用命名常量集，部分形式会生成运行时代码 | 跨包发布及编译工具对 const enum 支持需核对 |
| TS026 | Declaration file; .d.ts; Ambient declaration | 第三方库没类型、declare | 描述外部运行时已存在的 API 形状 | 声明文件不会生成缺失实现 |
| TS027 | Module augmentation; Global augmentation | 给库扩展类型 | 在规定范围补充已有模块或全局声明 | 类型扩展必须与实际运行时能力一致 |
| TS028 | import type; export type | 仅类型导入、运行时找不到导出 | 表达只在类型层使用的模块依赖 | 不可据此访问不存在的运行时值 |
| TS029 | strict; strictNullChecks; noImplicitAny | 开严格检查、漏空值 | 用编译选项控制检查强度 | 启用 strict 不表示所有额外严格选项都已启用 |
| TS030 | tsconfig; target; lib; moduleResolution | 有类型但浏览器运行不了 | 分别控制输出语法、可用声明和模块解析 | lib 声明不会安装 polyfill，paths 也不自动改写运行时路径 |
| TS031 | Project references; Incremental build | 多包 TS 构建很慢 | 划分类型构建边界并复用结果 | 构建图需要与包依赖和产物路径一致 |
| TS032 | Runtime validation; Schema; Type guard | 接口 JSON 类型撒谎 | 在运行时验证外部数据并连接静态类型 | 写一个类型别名不等于已经做了验证 |
