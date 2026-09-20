# Vue 与相关生态

检索分组：组件与模板、响应式、通信与生命周期、内置组件、路由与状态、工程。
默认将条目视作 Vue 3 语境的概念索引；实际项目先确认主版本及次版本。通用前端概念见 [frontend.md](frontend.md)，语言见 [javascript.md](javascript.md) / [typescript.md](typescript.md)。来源 S12、S25、S32-S34，见 [sources.md](sources.md)。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| VU001 | Vue; Options API; Composition API | 选项式、组合式 | 两种组织组件逻辑的 API 风格 | 不等于 Vue 2 与 Vue 3 的简单一一对应 |
| VU002 | SFC; Single-file component; .vue | 单文件组件、三块结构 | 以 template/script/style 组织可编译组件文件 | 浏览器不能直接按原生 HTML 执行整个 SFC |
| VU003 | setup; script setup; Compiler macro | setup 语法糖、宏不用导入 | 用编译阶段支持简化组件声明和模板暴露 | 编译宏不等同普通运行时函数，版本须核对 |
| VU004 | ref; .value; Unwrapping | ref 为什么要 value | 以容器跟踪一个可替换的响应式值 | 模板、对象属性和集合的自动解包规则不同 |
| VU005 | reactive; Proxy; Reactive identity | 对象响应式、替换后不更新 | 对对象访问进行依赖跟踪 | 原始对象与代理不同，整体替换引用可能断开跟踪 |
| VU006 | toRef; toRefs; Reactive destructuring | 解构后不更新 | 将响应式属性连接到独立 ref（普通 reactive 解构限制见 S25） | 普通 reactive 解构与编译器支持的 props 解构需区分版本 |
| VU007 | computed; Writable computed | 派生值、缓存计算 | 按响应式依赖计算并缓存值 | getter 应避免副作用，不用来执行请求 |
| VU008 | watch; watchEffect; Watch source | 监听变化、自动依赖收集 | watch 显式选源；watchEffect 跟踪执行中读取的依赖 | 异步边界会影响自动收集范围 |
| VU009 | Watch cleanup; Invalidation; Race | 旧请求覆盖新值、停止旧订阅 | 在侦听任务失效时清理过期工作 | onWatcherCleanup 等 API 的可用性及调用时机需核对 |
| VU010 | nextTick; Flush timing; DOM update batching | 改值后量不到新高度 | 等待一轮响应式引起的 DOM 更新完成 | 不保证所有图片、网络和未来布局已完成 |
| VU011 | shallowRef; shallowReactive; triggerRef | 大型外部对象代理成本 | 只跟踪浅层变化或显式通知 ref 更新 | 不假定嵌套对象会自动深度触发 |
| VU012 | readonly; markRaw; toRaw | 第三方实例不要代理 | 控制只读包装或绕过/取得原始对象 | 混用代理和原始对象需留意身份比较 |
| VU013 | Props; defineProps; Default props | 父传子、默认值 | 声明组件输入契约 | 子组件不应直接篡改父级拥有的输入状态 |
| VU014 | Emits; defineEmits; Component event | 子通知父、事件参数 | 声明并发出组件自定义事件 | 组件事件不等同 DOM 冒泡事件 |
| VU015 | v-model; modelValue; defineModel | 双向绑定、自定义输入组件 | 将值与更新事件组合为受约定的数据接口 | defineModel 依 Vue 版本；默认值需防父子不同步 |
| VU016 | v-bind; v-on; Modifier | 动态属性、事件修饰符 | 绑定表达式或事件并附加声明式行为 | 修饰符顺序可能影响语义 |
| VU017 | v-if; v-show; Conditional rendering | 显隐切换、状态总重置 | 分别控制条件实例化或 CSS 显示 | 高频切换成本与保留状态需求不同 |
| VU018 | v-for; key; List rendering | 列表复用错位、输入串行 | 用稳定 key 连接数据身份与组件实例 | 不默认用索引表示可重排业务实体 |
| VU019 | Slot; Scoped slot; 插槽 | 父组件自定义子组件区域 | 用模板内容及子组件提供的数据扩展呈现 | 插槽内容的词法作用域不等同 DOM 所在层级 |
| VU020 | Template ref; defineExpose | 父调用子方法、拿 DOM | 在挂载后引用元素或显式暴露的组件接口 | ref 可能尚未存在或因条件渲染变为 null |
| VU021 | provide/inject | 深层组件传值、依赖注入 | 在组件祖先链传递约定依赖 | 不自动替代全局状态管理，需定义更新责任 |
| VU022 | Composable; useX; Effect scope | 抽出复用逻辑、订阅泄露 | 用组合函数封装状态和副作用生命周期 | 不只是给普通工具函数加 use 前缀 |
| VU023 | onMounted; onUnmounted; Lifecycle hook | 初始化插件、销毁监听 | 在组件生命周期边界管理外部工作 | SSR 中可用钩子和 DOM 环境不同 |
| VU024 | KeepAlive; Activated/Deactivated | 切页保留状态、不想重复加载 | 缓存动态组件实例并区分激活状态 | 停用不等同卸载，订阅与资源仍需管理 |
| VU025 | Teleport; Transition; TransitionGroup | 弹层挂到 body、列表过渡 | 分别改变 DOM 挂载位置或组织进入离开动画 | Teleport 不自动解决模态焦点与滚动锁 |
| VU026 | Async component; Suspense | 按需组件、异步加载回退 | 协调异步组件及等待状态 | Suspense 的稳定性/支持边界应核对项目版本 |
| VU027 | style scoped; :deep(); :slotted(); :global() | scoped 穿透、插槽样式 | 用编译后的作用域规则限定样式目标 | 不是 Shadow DOM 隔离，不任意穿透第三方内部实现 |
| VU028 | Custom directive; v-html | 低层 DOM 行为、显示 HTML | 指令封装元素行为，v-html 写入原始 HTML | 不可信 HTML 需正确清洗，插值文本与其风险不同 |
| VU029 | Vue Router; Route record; Nested route | 页面地址、嵌套路由 | 组织路径匹配与路由组件层级 | 直接访问路径需配合服务端部署规则 |
| VU030 | Route params/query; Navigation guard | 路由参数、登录拦截 | 管理 URL 数据及导航过程 | 守卫不代替后端授权；参数变化不必重建组件 |
| VU031 | RouterView; RouterLink; History mode | 返回键、hash 与 history | 提供路由出口和导航，选择历史实现 | HTML5 history 通常需服务端正确回退 |
| VU032 | Pinia; defineStore; State/Getters/Actions | 跨页面共享状态 | 用 store 组织共享事实、派生值和操作 | 不把所有局部 UI 状态默认移入全局 |
| VU033 | storeToRefs; Store hydration; Persistence | Pinia 解构不更新、刷新丢数据 | 提取响应式属性并区分状态恢复和持久化 | Pinia 状态不因创建 store 就自动永久保存 |
| VU034 | Nuxt; SSR; Hydration; useAsyncData | Vue 全栈、服务端取数 | 在框架路由及服务端/客户端生命周期组织页面 | 属于 Nuxt 生态，不是所有 Vue 项目都具备 |
| VU035 | vue-tsc; Template type checking | 模板类型没检查、构建通过仍报类型 | 检查 Vue 文件的脚本和模板类型 | Vite 转译成功不代表完成了完整类型检查 |
| VU036 | Vue Test Utils; Mount; Stub; flushPromises | 测组件、异步状态测试 | 挂载组件并控制依赖/异步观测边界 | nextTick 与等待 Promise 完成不是同一件事 |
