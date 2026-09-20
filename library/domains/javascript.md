# JavaScript

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [JS001 · ECMAScript; ES; JavaScript; JS](../concepts/JS001.md) | ES 版本、语言标准 |
| [JS002 · Primitive; Object; typeof](../concepts/JS002.md) | 基本类型、对象类型判断 |
| [JS003 · Coercion; ==; ===; Object.is](../concepts/JS003.md) | 隐式转换、真假相等 |
| [JS004 · Truthy/Falsy; Nullish; ??](../concepts/JS004.md) | 默认值吃掉 0、空串被替换 |
| [JS005 · Optional chaining; ?.](../concepts/JS005.md) | 深层属性可能不存在 |
| [JS006 · let; const; var; Lexical scope; TDZ](../concepts/JS006.md) | 声明提升、初始化前访问 |
| [JS007 · Closure; 闭包](../concepts/JS007.md) | 回调记住旧值、函数保存环境 |
| [JS008 · this; call/apply/bind](../concepts/JS008.md) | this 丢失、方法作为回调 |
| [JS009 · Arrow function; 箭头函数](../concepts/JS009.md) | 箭头函数绑定、不能 new |
| [JS010 · Prototype; Prototype chain; class](../concepts/JS010.md) | 原型继承、类的方法在哪 |
| [JS011 · Own property; Descriptor; Getter/Setter](../concepts/JS011.md) | 枚举漏字段、属性不可改 |
| [JS012 · Destructuring; Spread; Rest](../concepts/JS012.md) | 解构、展开、剩余参数 |
| [JS013 · Shallow/Deep copy; structuredClone](../concepts/JS013.md) | 复制后改到原对象 |
| [JS014 · Array; map/filter/reduce; Mutating methods](../concepts/JS014.md) | 列表转换、原数组被改 |
| [JS015 · Map; Set; WeakMap; WeakSet](../concepts/JS015.md) | 键值表、去重、对象缓存 |
| [JS016 · Iterable; Iterator; Generator; yield](../concepts/JS016.md) | 自定义 for-of、惰性生成 |
| [JS017 · Async iterable; Async generator; for-await-of](../concepts/JS017.md) | 异步逐条消费 |
| [JS018 · Promise; then/catch/finally](../concepts/JS018.md) | 异步结果、未处理拒绝 |
| [JS019 · async/await](../concepts/JS019.md) | 异步写成顺序代码 |
| [JS020 · Promise.all/allSettled/race/any](../concepts/JS020.md) | 多请求并发、一个失败怎么办 |
| [JS021 · Task; Microtask; Event loop](../concepts/JS021.md) | setTimeout 与 Promise 顺序 |
| [JS022 · setTimeout; setInterval; Timer drift](../concepts/JS022.md) | 定时不准、倒计时漂移 |
| [JS023 · requestAnimationFrame; RAF](../concepts/JS023.md) | 跟屏幕刷新做动画 |
| [JS024 · Fetch; Response; AbortController](../concepts/JS024.md) | 请求 404 为何没进 catch |
| [JS025 · try/catch; Error cause; Unhandled rejection](../concepts/JS025.md) | 异步报错抓不到 |
| [JS026 · EventTarget; Event listener; Cleanup](../concepts/JS026.md) | 重复绑定、组件卸载后触发 |
| [JS027 · Capture/Bubble; Delegation; Event propagation](../concepts/JS027.md) | 点击子元素触发父级、事件委托 |
| [JS028 · Event target/currentTarget; composedPath](../concepts/JS028.md) | 点到图标取错元素 |
| [JS029 · DOM query; Node; Element; Live collection](../concepts/JS029.md) | 元素集合自己变了 |
| [JS030 · MutationObserver; ResizeObserver; IntersectionObserver](../concepts/JS030.md) | 监听尺寸、进入视口、DOM 变化 |
| [JS031 · ESM; import/export; Live binding](../concepts/JS031.md) | 模块导入、循环依赖 |
| [JS032 · Dynamic import; Top-level await](../concepts/JS032.md) | 按需加载模块、模块先等数据 |
| [JS033 · CommonJS; require; module.exports](../concepts/JS033.md) | require 和 import 混用 |
| [JS034 · JSON; parse/stringify; Serialization](../concepts/JS034.md) | 序列化丢字段、循环引用报错 |
| [JS035 · Number; IEEE 754; BigInt; Safe integer](../concepts/JS035.md) | 大整数精度丢、0.1 加 0.2 |
| [JS036 · Date; Timestamp; Intl](../concepts/JS036.md) | 日期错一天、国际化格式 |
| [JS037 · RegExp; Unicode; Code point; Grapheme](../concepts/JS037.md) | 正则匹配、emoji 长度不对 |
| [JS038 · Proxy; Reflect](../concepts/JS038.md) | 拦截对象读写、代理行为 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 JavaScript 领域基线，将语言和异步概念落实为值、引用、事件顺序与宿主资源的明确行为。

### 关键特征

- 分清值转换、对象引用和可变共享状态，避免依赖隐式转换表达关键业务条件。
- 异步操作的完成、失败和过期是不同状态，需要明确接收结果的责任。
- 语言能力与浏览器或其他宿主能力分开核对，不假定运行环境相同。

### 如何落实

- 确定运行宿主和模块入口，列出外部输入的数据形状及需要转换的边界。
- 对涉及的对象明确复制、共享和修改策略，对回调明确捕获值与调用上下文。
- 按真实事件顺序安排异步链，处理拒绝、取消及旧响应，不以固定等待时间替代完成信号。
- 为监听器、计时器和外部连接安排注册与释放，使重复初始化和退出都有明确结果。

### 如何验收

- 用空值、缺失字段、特殊数值及不同输入类型核对转换和判断结果。
- 改变异步完成顺序并注入失败，确认结果归属正确且错误不会悄然丢失。
- 重复初始化与销毁，核对回调次数和相关资源数量没有累积。

### 常见误用

- 把浅层复制当作嵌套对象完全隔离，或依赖偶然的回调执行顺序。
- 用任意延时修复竞态，让正确性依赖机器速度。
