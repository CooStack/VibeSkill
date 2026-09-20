# Vue

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [VU001 · Vue; Options API; Composition API](../concepts/VU001.md) | 选项式、组合式 |
| [VU002 · SFC; Single-file component; .vue](../concepts/VU002.md) | 单文件组件、三块结构 |
| [VU003 · setup; script setup; Compiler macro](../concepts/VU003.md) | setup 语法糖、宏不用导入 |
| [VU004 · ref; .value; Unwrapping](../concepts/VU004.md) | ref 为什么要 value |
| [VU005 · reactive; Proxy; Reactive identity](../concepts/VU005.md) | 对象响应式、替换后不更新 |
| [VU006 · toRef; toRefs; Reactive destructuring](../concepts/VU006.md) | 解构后不更新 |
| [VU007 · computed; Writable computed](../concepts/VU007.md) | 派生值、缓存计算 |
| [VU008 · watch; watchEffect; Watch source](../concepts/VU008.md) | 监听变化、自动依赖收集 |
| [VU009 · Watch cleanup; Invalidation; Race](../concepts/VU009.md) | 旧请求覆盖新值、停止旧订阅 |
| [VU010 · nextTick; Flush timing; DOM update batching](../concepts/VU010.md) | 改值后量不到新高度 |
| [VU011 · shallowRef; shallowReactive; triggerRef](../concepts/VU011.md) | 大型外部对象代理成本 |
| [VU012 · readonly; markRaw; toRaw](../concepts/VU012.md) | 第三方实例不要代理 |
| [VU013 · Props; defineProps; Default props](../concepts/VU013.md) | 父传子、默认值 |
| [VU014 · Emits; defineEmits; Component event](../concepts/VU014.md) | 子通知父、事件参数 |
| [VU015 · v-model; modelValue; defineModel](../concepts/VU015.md) | 双向绑定、自定义输入组件 |
| [VU016 · v-bind; v-on; Modifier](../concepts/VU016.md) | 动态属性、事件修饰符 |
| [VU017 · v-if; v-show; Conditional rendering](../concepts/VU017.md) | 显隐切换、状态总重置 |
| [VU018 · v-for; key; List rendering](../concepts/VU018.md) | 列表复用错位、输入串行 |
| [VU019 · Slot; Scoped slot; 插槽](../concepts/VU019.md) | 父组件自定义子组件区域 |
| [VU020 · Template ref; defineExpose](../concepts/VU020.md) | 父调用子方法、拿 DOM |
| [VU021 · provide/inject](../concepts/VU021.md) | 深层组件传值、依赖注入 |
| [VU022 · Composable; useX; Effect scope](../concepts/VU022.md) | 抽出复用逻辑、订阅泄露 |
| [VU023 · onMounted; onUnmounted; Lifecycle hook](../concepts/VU023.md) | 初始化插件、销毁监听 |
| [VU024 · KeepAlive; Activated/Deactivated](../concepts/VU024.md) | 切页保留状态、不想重复加载 |
| [VU025 · Teleport; Transition; TransitionGroup](../concepts/VU025.md) | 弹层挂到 body、列表过渡 |
| [VU026 · Async component; Suspense](../concepts/VU026.md) | 按需组件、异步加载回退 |
| [VU027 · style scoped; :deep(); :slotted(); :global()](../concepts/VU027.md) | scoped 穿透、插槽样式 |
| [VU028 · Custom directive; v-html](../concepts/VU028.md) | 低层 DOM 行为、显示 HTML |
| [VU029 · Vue Router; Route record; Nested route](../concepts/VU029.md) | 页面地址、嵌套路由 |
| [VU030 · Route params/query; Navigation guard](../concepts/VU030.md) | 路由参数、登录拦截 |
| [VU031 · RouterView; RouterLink; History mode](../concepts/VU031.md) | 返回键、hash 与 history |
| [VU032 · Pinia; defineStore; State/Getters/Actions](../concepts/VU032.md) | 跨页面共享状态 |
| [VU033 · storeToRefs; Store hydration; Persistence](../concepts/VU033.md) | Pinia 解构不更新、刷新丢数据 |
| [VU034 · Nuxt; SSR; Hydration; useAsyncData](../concepts/VU034.md) | Vue 全栈、服务端取数 |
| [VU035 · vue-tsc; Template type checking](../concepts/VU035.md) | 模板类型没检查、构建通过仍报类型 |
| [VU036 · Vue Test Utils; Mount; Stub; flushPromises](../concepts/VU036.md) | 测组件、异步状态测试 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 Vue 领域基线，将组件概念落实为响应式依赖、数据归属和生命周期内的副作用。

### 关键特征

- 明确响应式源与派生值的依赖关系，不以多份可写副本维持同一状态。
- 组件输入、输出与共享状态各有边界，修改责任应与状态所有者一致。
- 订阅、监听和异步任务随其拥有者的生命周期建立与清理，具体机制按项目版本核对。

### 如何落实

- 从模板读取与交互写入两端追踪状态，标明响应式源、派生计算及可能失去关联的传值位置。
- 将无副作用的派生关系与需要执行动作的监听分开，明确监听触发条件与写回路径。
- 沿既有组件协议传递输入和事件；列表中确定稳定身份，避免局部编辑态跟随位置错配。
- 在组件或现有共享作用域内管理请求和订阅，处理快速切换、卸载以及任务涉及的缓存或服务端渲染路径。

### 如何验收

- 修改每个关键依赖并观察派生值与模板，确认更新既不丢失也不形成反馈循环。
- 重排列表、切换属性和重复进入页面，核对组件身份及本地编辑状态归属。
- 卸载或切换对象后完成旧请求，确认不会污染当前状态，相关订阅能按约定释放。

### 常见误用

- 用监听器复制所有派生状态，制造循环更新和多个权威来源。
- 把页面可见性等同于组件销毁，忽略实际生命周期与副作用存续。
