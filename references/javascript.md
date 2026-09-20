# JavaScript

检索分组：值与作用域、函数与对象、数据结构、异步、DOM 与模块。
页面性能见 [frontend.md](frontend.md)，静态类型见 [typescript.md](typescript.md)，运行/构建见 [tooling.md](tooling.md)。来源 S23、S01，见 [sources.md](sources.md)。区分 ECMAScript 语言和浏览器/Node 等宿主 API。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| JS001 | ECMAScript; ES; JavaScript; JS | ES 版本、语言标准 | ECMAScript 定义核心语言，宿主提供额外能力 | JavaScript 不是 Java；DOM 也不是语言本体 |
| JS002 | Primitive; Object; typeof | 基本类型、对象类型判断 | 区分不可变基本值与对象身份 | typeof null 的结果不能用于判定普通对象 |
| JS003 | Coercion; ==; ===; Object.is | 隐式转换、真假相等 | 不同相等算法和类型转换影响比较 | NaN、负零及对象身份需按具体算法判断 |
| JS004 | Truthy/Falsy; Nullish; ?? | 默认值吃掉 0、空串被替换 | 区分假值与仅 null/undefined 的缺失 | 逻辑或兜底不等同空值合并 |
| JS005 | Optional chaining; ?. | 深层属性可能不存在 | 对 nullish 接收者短路访问或调用 | 不吞掉任意异常，也不使未声明变量安全 |
| JS006 | let; const; var; Lexical scope; TDZ | 声明提升、初始化前访问 | 不同声明有不同作用域及初始化规则 | const 约束绑定，不冻结对象内容 |
| JS007 | Closure; 闭包 | 回调记住旧值、函数保存环境 | 函数可持续访问其词法环境 | 闭包捕获不自动生成每次调用的深拷贝 |
| JS008 | this; call/apply/bind | this 丢失、方法作为回调 | 调用方式或绑定决定普通函数 this | 从对象取出方法后不自动保留对象接收者 |
| JS009 | Arrow function; 箭头函数 | 箭头函数绑定、不能 new | 箭头函数使用词法 this 等绑定 | 不适合需要独立 this 或构造行为的场景 |
| JS010 | Prototype; Prototype chain; class | 原型继承、类的方法在哪 | 对象可通过原型链查找属性 | class 语法不意味着脱离原型对象模型 |
| JS011 | Own property; Descriptor; Getter/Setter | 枚举漏字段、属性不可改 | 属性有归属及可写/可枚举/可配置等描述 | 读取属性可能执行 getter 而非纯取值 |
| JS012 | Destructuring; Spread; Rest | 解构、展开、剩余参数 | 提取或组合数据和参数 | 对象展开通常是浅复制，不保留全部描述符/原型语义 |
| JS013 | Shallow/Deep copy; structuredClone | 复制后改到原对象 | 区分共享嵌套引用与独立结构复制 | JSON 往返不是通用深拷贝；可克隆类型有限 |
| JS014 | Array; map/filter/reduce; Mutating methods | 列表转换、原数组被改 | 区分产生新结果与就地变更操作 | sort 等变异行为易影响共享状态 |
| JS015 | Map; Set; WeakMap; WeakSet | 键值表、去重、对象缓存 | 选择键集合及弱引用关联结构 | WeakMap 不提供任意枚举，并非一般缓存的万能替代 |
| JS016 | Iterable; Iterator; Generator; yield | 自定义 for-of、惰性生成 | 以迭代协议逐项产出值 | for-in 枚举键，与 for-of 消费值不同 |
| JS017 | Async iterable; Async generator; for-await-of | 异步逐条消费 | 用异步迭代协议衔接生产与消费 | 仍需设计取消及资源释放 |
| JS018 | Promise; then/catch/finally | 异步结果、未处理拒绝 | 表达未来完成或失败并链接后续处理 | Promise 执行器同步运行，不会自动开线程 |
| JS019 | async/await | 异步写成顺序代码 | 在异步函数中等待 Promise 结果 | await 不让 CPU 密集计算自动脱离主线程 |
| JS020 | Promise.all/allSettled/race/any | 多请求并发、一个失败怎么办 | 按不同完成/失败条件组合任务结果 | 组合提前结束不自动取消其他底层操作 |
| JS021 | Task; Microtask; Event loop | setTimeout 与 Promise 顺序 | 运行时按调度机制执行任务及微任务 | 具体宿主阶段不同，不把 Node 规则直接套到浏览器 |
| JS022 | setTimeout; setInterval; Timer drift | 定时不准、倒计时漂移 | 调度可执行时机而非承诺精确时钟 | 后台节流、长任务会延迟执行 |
| JS023 | requestAnimationFrame; RAF | 跟屏幕刷新做动画 | 在合适绘制时机前更新动画状态 | 需使用时间差，不能假定固定帧率 |
| JS024 | Fetch; Response; AbortController | 请求 404 为何没进 catch | Fetch 提供响应对象，调用者检查状态并消费正文 | HTTP 错误状态通常不等于网络 Promise 拒绝 |
| JS025 | try/catch; Error cause; Unhandled rejection | 异步报错抓不到 | 在正确异步边界观察失败并保留根因 | 外层同步 try 不会自动捕获日后回调错误 |
| JS026 | EventTarget; Event listener; Cleanup | 重复绑定、组件卸载后触发 | 订阅事件并在生命周期结束时解除 | 需匹配回调身份及相关捕获选项 |
| JS027 | Capture/Bubble; Delegation; Event propagation | 点击子元素触发父级、事件委托 | 利用事件传播路径组织处理 | stopPropagation 与 preventDefault 职责不同 |
| JS028 | Event target/currentTarget; composedPath | 点到图标取错元素 | 区分事件目标和当前监听对象 | Shadow DOM 会影响跨边界传播与重定向 |
| JS029 | DOM query; Node; Element; Live collection | 元素集合自己变了 | 通过 DOM API 操作文档节点 | 不同查询返回静态或动态集合，需按 API 区分 |
| JS030 | MutationObserver; ResizeObserver; IntersectionObserver | 监听尺寸、进入视口、DOM 变化 | 针对不同变化来源获取通知 | 避免回调中引发无限反馈循环 |
| JS031 | ESM; import/export; Live binding | 模块导入、循环依赖 | 使用标准模块链接及导出绑定 | 命名导出与默认导出不同，循环初始化有风险 |
| JS032 | Dynamic import; Top-level await | 按需加载模块、模块先等数据 | 按需取得模块或在模块评估中等待 | 支持程度与构建配置/宿主相关 |
| JS033 | CommonJS; require; module.exports | require 和 import 混用 | 使用另一种模块装载/导出约定 | ESM 互操作随运行时和打包器核对 |
| JS034 | JSON; parse/stringify; Serialization | 序列化丢字段、循环引用报错 | 在 JSON 可表达数据范围内转换 | undefined、BigInt、日期和特殊数值需明确处理 |
| JS035 | Number; IEEE 754; BigInt; Safe integer | 大整数精度丢、0.1 加 0.2 | 区分浮点数值与任意精度整数 | BigInt 不用于小数，不能任意与 Number 混算 |
| JS036 | Date; Timestamp; Intl | 日期错一天、国际化格式 | 区分时间数值、解析和地区格式化 | 不依赖含糊日期字符串或默认时区 |
| JS037 | RegExp; Unicode; Code point; Grapheme | 正则匹配、emoji 长度不对 | 文本处理需区分码元、码点与可见字符簇 | 字符串 length 不是人眼字符数 |
| JS038 | Proxy; Reflect | 拦截对象读写、代理行为 | 以陷阱和对应底层操作定制对象行为 | 代理不是网络代理，也不天然安全或高性能 |
