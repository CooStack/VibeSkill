# 前端工程概念

检索分组：组件与数据流、渲染、CSS、异步与性能、工程与测试。
相邻领域：[网页](web.md)、[设计](design.md)、[后端](backend.md)。来源入口：S01、S11、S12，见 [sources.md](sources.md)。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| FE001 | 组件 Component; 组合 Composition | 重复 UI、可复用部件 | 按职责组织可组合界面 | 不为一次性小片段过度抽象 |
| FE002 | Props; Events; 单向数据流 | 父子传值、点击通知 | 通过明确输入与事件传递信息 | 隐式共享可变状态增加耦合 |
| FE003 | 状态 State; 派生状态 Derived state | 勾选联动、数值不一致 | 保留最小事实源，计算其派生值 | 可计算值不必重复存储 |
| FE004 | 受控/非受控 Controlled/Uncontrolled | 表单值由谁管理 | 由应用状态或元素自身持有输入值 | 切换控制模式可能造成不同步 |
| FE005 | 状态提升 Lifting state; Store; Context | 多处共享筛选、跨组件同步 | 将状态移到共同拥有者或共享容器 | Context 不是所有状态的默认归宿 |
| FE006 | 服务端状态 Server state; Query cache | 请求数据缓存、刷新列表 | 管理远端数据的新鲜度、同步与失效 | 与纯 UI 状态的生命周期不同 |
| FE007 | 状态机 State machine; Reducer | 流程很多、不能同时成功失败 | 用有限状态和事件描述转换 | Reducer 与完整状态机不是同义 |
| FE008 | 生命周期 Lifecycle; Effect; Cleanup | 卸载后还请求、监听重复 | 将外部订阅与组件存续对齐 | 纯计算不必塞进副作用 |
| FE009 | 响应式 Reactivity; Signal; Observable | 值变了界面更新 | 跟踪依赖并通知更新 | 与“响应式布局”不是同一概念 |
| FE010 | DOM; Virtual DOM; Reconciliation | 为什么重渲染、节点更新 | 区分真实文档、描述表示与更新比较 | 虚拟 DOM 不保证永远更快 |
| FE011 | Key; 稳定标识 Identity | 列表重排后输入串行 | 为动态集合成员保留正确身份 | 可重排列表不宜使用位置充当身份 |
| FE012 | CSR; Client-side rendering | 浏览器生成页面 | 客户端脚本负责主要 UI 生成 | 首屏、索引及弱设备成本需权衡 |
| FE013 | SSR; Server-side rendering | 服务器直出 HTML | 服务端生成初始页面内容 | 与静态生成及游戏屏幕空间反射不同 |
| FE014 | SSG; Static generation; ISR | 内容预生成、定期更新 | 在构建或受控再生成时产出页面 | ISR 的具体语义取决于框架 |
| FE015 | Hydration; 水合 | HTML 有了但不能点、首屏不一致 | 给服务端输出连接客户端交互 | 首次渲染不一致会造成 mismatch |
| FE016 | Islands; 岛屿架构; Partial hydration | 静态页只有少量交互 | 局部激活需要交互的区域 | 与完整 SPA 的状态组织不同 |
| FE017 | 路由 Router; 嵌套路由; Route guard | 页面切换、子页面 | 映射地址到界面及加载边界 | 路由守卫不是服务端授权 |
| FE018 | CSS 盒模型 Box model; box-sizing | 宽度多出来、间距不对 | 区分内容、内边距、边框与外边距 | margin 折叠只在特定布局条件发生 |
| FE019 | 层叠 Cascade; Specificity; Inheritance | 样式覆盖不了 | 确定声明优先级及继承 | 不用不断添加 important 掩盖结构问题 |
| FE020 | Flexbox | 一行排列、等分、对齐 | 主要组织一维流与空间分配 | 内容最小尺寸可能阻碍收缩 |
| FE021 | CSS Grid | 二维网格、列行对齐 | 用轨道控制二维布局 | 与单纯卡片外观无关 |
| FE022 | Position; Containing block; Sticky | 固定导航、吸顶、绝对定位 | 定义定位参照和滚动关系 | Sticky 受滚动祖先及范围约束 |
| FE023 | Stacking context; z-index | 弹窗被盖住、层级无效 | 在局部堆叠上下文中排序 | 大 z-index 不能任意跨越上下文 |
| FE024 | Overflow; Intrinsic sizing; min-content | 长文本撑破、横向溢出 | 处理内容固有尺寸及越界 | 直接隐藏溢出可能掩盖不可访问内容 |
| FE025 | Media query; Container query | 根据屏幕或容器改变布局 | 分别依据环境及容器条件应用样式 | 容器查询不等同于全页断点 |
| FE026 | CSS variables; Design token | 全站换主题、统一间距 | 变量实现复用，token 表达设计语义 | token 是设计契约，不只是一堆颜色值 |
| FE027 | Transition; Animation; Easing | 平滑展开、缓动 | 描述属性随时间变化的轨迹 | 需关注动效偏好、布局成本及可中断性 |
| FE028 | FLIP; Layout animation | 列表重排动画 | 测量前后布局并以变换衔接 | 测量成本及异步布局变化要控制 |
| FE029 | 防抖 Debounce; 节流 Throttle | 输入搜索、滚动事件太多 | 防抖等待安静窗口；节流限制执行频率 | 保留首尾触发行为需明确 |
| FE030 | 虚拟列表 Virtualization; Windowing | 一万行滚动卡 | 只渲染视窗附近内容 | 需处理动态高度、焦点、搜索与读屏 |
| FE031 | Memoization; 缓存计算 | 同样计算重复、重渲染慢 | 用输入关联复用计算结果 | 测量后使用，错误依赖会产生陈旧结果 |
| FE032 | 代码分割 Code splitting; Tree shaking | 首包太大 | 按需加载及剔除可证明未使用代码 | 动态加载也有网络往返和错误状态 |
| FE033 | Event loop; Microtask; Main thread | JS 卡住、异步顺序 | 理解任务调度及 UI 主线程占用 | Promise 不会自动把计算移到后台 |
| FE034 | Web Worker | 大计算阻塞页面 | 在独立执行上下文处理工作 | 不能直接操作 DOM，通信也有成本 |
| FE035 | Reflow/Layout; Paint; Composite | 动画掉帧、页面抖 | 区分布局计算、绘制和合成阶段 | transform 不保证任何场景都零成本 |
| FE036 | 乐观更新 Optimistic UI; Rollback | 点赞立即变化 | 先反馈预期结果，失败时协调或回退 | 与数据库乐观锁不同 |
| FE037 | 竞态 Race condition; AbortController | 旧搜索结果覆盖新结果 | 取消无用工作或拒绝陈旧响应 | 取消请求不保证服务端工作取消 |
| FE038 | Loading; Empty; Error; Skeleton | 加载空白、失败没提示 | 明确定义异步界面的各类状态 | 无数据、无权限与加载失败不要混为一谈 |
| FE039 | Error boundary; 异常边界 | 一处组件错误整页崩 | 在框架支持边界隔离部分渲染错误 | 不自动捕获全部异步或事件错误 |
| FE040 | Portal; Teleport | 弹层逃离裁剪容器 | 将 UI 渲染到另一个 DOM 位置 | 仍需设计焦点、滚动锁及堆叠策略 |
| FE041 | TypeScript; 类型收窄; 泛型 | 字段类型、代码提示 | 用静态类型表达约束及复用 | 静态类型不能验证未受信任的运行时输入 |
| FE042 | Bundler; ESM; Transpilation; Source map | 构建报错、定位压缩代码 | 模块解析、转换、打包及源码映射 | 源码映射发布策略需考虑信息暴露 |
| FE043 | 单元测试; Component test; E2E; Visual regression | UI 改坏、截图对比 | 按逻辑、组件、流程和外观验证 | 截图通过不证明交互和无障碍正确 |
| FE044 | BFF; Backend for Frontend | 多接口聚合、不同端数据 | 为特定客户端提供适配接口层 | 不应复制所有后端业务规则 |
