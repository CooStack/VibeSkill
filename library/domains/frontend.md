# 前端工程

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [FE001 · 组件 Component; 组合 Composition](../concepts/FE001.md) | 重复 UI、可复用部件 |
| [FE002 · Props; Events; 单向数据流](../concepts/FE002.md) | 父子传值、点击通知 |
| [FE003 · 状态 State; 派生状态 Derived state](../concepts/FE003.md) | 勾选联动、数值不一致 |
| [FE004 · 受控/非受控 Controlled/Uncontrolled](../concepts/FE004.md) | 表单值由谁管理 |
| [FE005 · 状态提升 Lifting state; Store; Context](../concepts/FE005.md) | 多处共享筛选、跨组件同步 |
| [FE006 · 服务端状态 Server state; Query cache](../concepts/FE006.md) | 请求数据缓存、刷新列表 |
| [FE007 · 状态机 State machine; Reducer](../concepts/FE007.md) | 流程很多、不能同时成功失败 |
| [FE008 · 生命周期 Lifecycle; Effect; Cleanup](../concepts/FE008.md) | 卸载后还请求、监听重复 |
| [FE009 · 响应式 Reactivity; Signal; Observable](../concepts/FE009.md) | 值变了界面更新 |
| [FE010 · DOM; Virtual DOM; Reconciliation](../concepts/FE010.md) | 为什么重渲染、节点更新 |
| [FE011 · Key; 稳定标识 Identity](../concepts/FE011.md) | 列表重排后输入串行 |
| [FE012 · CSR; Client-side rendering](../concepts/FE012.md) | 浏览器生成页面 |
| [FE013 · SSR; Server-side rendering](../concepts/FE013.md) | 服务器直出 HTML |
| [FE014 · SSG; Static generation; ISR](../concepts/FE014.md) | 内容预生成、定期更新 |
| [FE015 · Hydration; 水合](../concepts/FE015.md) | HTML 有了但不能点、首屏不一致 |
| [FE016 · Islands; 岛屿架构; Partial hydration](../concepts/FE016.md) | 静态页只有少量交互 |
| [FE017 · 路由 Router; 嵌套路由; Route guard](../concepts/FE017.md) | 页面切换、子页面 |
| [FE018 · CSS 盒模型 Box model; box-sizing](../concepts/FE018.md) | 宽度多出来、间距不对 |
| [FE019 · 层叠 Cascade; Specificity; Inheritance](../concepts/FE019.md) | 样式覆盖不了 |
| [FE020 · Flexbox](../concepts/FE020.md) | 一行排列、等分、对齐 |
| [FE021 · CSS Grid](../concepts/FE021.md) | 二维网格、列行对齐 |
| [FE022 · Position; Containing block; Sticky](../concepts/FE022.md) | 固定导航、吸顶、绝对定位 |
| [FE023 · Stacking context; z-index](../concepts/FE023.md) | 弹窗被盖住、层级无效 |
| [FE024 · Overflow; Intrinsic sizing; min-content](../concepts/FE024.md) | 长文本撑破、横向溢出 |
| [FE025 · Media query; Container query](../concepts/FE025.md) | 根据屏幕或容器改变布局 |
| [FE026 · CSS variables; Design token](../concepts/FE026.md) | 全站换主题、统一间距 |
| [FE027 · Transition; Animation; Easing](../concepts/FE027.md) | 平滑展开、缓动 |
| [FE028 · FLIP; Layout animation](../concepts/FE028.md) | 列表重排动画 |
| [FE029 · 防抖 Debounce; 节流 Throttle](../concepts/FE029.md) | 输入搜索、滚动事件太多 |
| [FE030 · 虚拟列表 Virtualization; Windowing](../concepts/FE030.md) | 一万行滚动卡 |
| [FE031 · Memoization; 缓存计算](../concepts/FE031.md) | 同样计算重复、重渲染慢 |
| [FE032 · 代码分割 Code splitting; Tree shaking](../concepts/FE032.md) | 首包太大 |
| [FE033 · Event loop; Microtask; Main thread](../concepts/FE033.md) | JS 卡住、异步顺序 |
| [FE034 · Web Worker](../concepts/FE034.md) | 大计算阻塞页面 |
| [FE035 · Reflow/Layout; Paint; Composite](../concepts/FE035.md) | 动画掉帧、页面抖 |
| [FE036 · 乐观更新 Optimistic UI; Rollback](../concepts/FE036.md) | 点赞立即变化 |
| [FE037 · 竞态 Race condition; AbortController](../concepts/FE037.md) | 旧搜索结果覆盖新结果 |
| [FE038 · Loading; Empty; Error; Skeleton](../concepts/FE038.md) | 加载空白、失败没提示 |
| [FE039 · Error boundary; 异常边界](../concepts/FE039.md) | 一处组件错误整页崩 |
| [FE040 · Portal; Teleport](../concepts/FE040.md) | 弹层逃离裁剪容器 |
| [FE041 · TypeScript; 类型收窄; 泛型](../concepts/FE041.md) | 字段类型、代码提示 |
| [FE042 · Bundler; ESM; Transpilation; Source map](../concepts/FE042.md) | 构建报错、定位压缩代码 |
| [FE043 · 单元测试; Component test; E2E; Visual regression](../concepts/FE043.md) | UI 改坏、截图对比 |
| [FE044 · BFF; Backend for Frontend](../concepts/FE044.md) | 多接口聚合、不同端数据 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为前端领域基线，将交互概念落实为状态来源、事件流和可见界面状态，不限定框架或状态库。

### 关键特征

- 每项可变状态应有明确所有者，派生值与独立存储值分开处理。
- 以用户操作引发的状态转换组织实现，覆盖等待、成功、失败与恢复。
- 组件边界服务于现有交互和复用，不以拆分数量或抽象层数衡量质量。

### 如何落实

- 列出本次交互的事件、状态及转换条件，区分本地编辑态、服务端数据和暂存输入。
- 沿现有组件边界传递数据与操作，避免多个组件各自维护同一权威值。
- 为异步操作确定取消、过期响应和重复触发的处理，保留用户尚未提交的输入。
- 按实际布局约束实现各状态，安排焦点恢复、错误定位和组件卸载时的订阅清理。

### 如何验收

- 连续执行编辑、提交、失败、重试，核对输入保留及界面状态转换。
- 快速切换对象或路由并打乱响应顺序，确认旧结果不会覆盖当前选择。
- 在目标尺寸与键盘操作下核对内容、控件和焦点，不因加载或错误状态产生遮挡。

### 常见误用

- 以多个布尔值拼出互相矛盾的界面状态而没有转换约束。
- 仅验证首次成功渲染，遗漏再次进入、卸载和异步竞态。
