# CSS

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [CS001 · Selector; Combinator](../concepts/CS001.md) | 选中子元素、相邻兄弟 |
| [CS002 · Pseudo-class; :hover; :focus-visible; :checked](../concepts/CS002.md) | 悬停、键盘焦点、勾选样式 |
| [CS003 · Pseudo-element; ::before; ::after](../concepts/CS003.md) | 装饰内容、伪元素 |
| [CS004 · :is(); :where(); :not(); :has()](../concepts/CS004.md) | 父级按子元素状态变化 |
| [CS005 · Cascade layer; @layer; Origin; important](../concepts/CS005.md) | 第三方样式覆盖冲突 |
| [CS006 · initial; inherit; unset; revert; revert-layer](../concepts/CS006.md) | 重置样式、回到上一层 |
| [CS007 · Custom property; var(); Fallback; @property](../concepts/CS007.md) | CSS 变量、主题值、变量动画 |
| [CS008 · px; em; rem; Percent; vw/vh; dvh](../concepts/CS008.md) | 字号和高度按什么算 |
| [CS009 · calc(); min(); max(); clamp()](../concepts/CS009.md) | 尺寸上下限、混合单位 |
| [CS010 · Logical properties; inline/block; Writing mode](../concepts/CS010.md) | RTL、横竖排适配 |
| [CS011 · Formatting context; BFC; flow-root](../concepts/CS011.md) | 浮动塌陷、外边距影响父级 |
| [CS012 · Margin collapse; Gap](../concepts/CS012.md) | 上下间距合并、列表间距 |
| [CS013 · Flex basis/grow/shrink; min-width: 0](../concepts/CS013.md) | flex 子项挤不下、文本撑破 |
| [CS014 · Grid tracks; fr; minmax(); auto-fit/auto-fill](../concepts/CS014.md) | 自动列数、最后一行拉伸 |
| [CS015 · Subgrid](../concepts/CS015.md) | 子组件列线与父级对齐 |
| [CS016 · aspect-ratio; object-fit; object-position](../concepts/CS016.md) | 图片拉伸、裁切位置 |
| [CS017 · Text overflow; white-space; overflow-wrap; line-clamp](../concepts/CS017.md) | 省略号、长网址撑破 |
| [CS018 · Font face; Fallback font; font-display](../concepts/CS018.md) | 字体加载闪、中文缺字 |
| [CS019 · Transform; Transform origin; Containing block](../concepts/CS019.md) | 缩放旋转、fixed 跟错父级 |
| [CS020 · Filter; Backdrop filter; Blend mode](../concepts/CS020.md) | 背景毛玻璃、颜色混合 |
| [CS021 · Clip-path; Mask; Border radius](../concepts/CS021.md) | 裁成形状、渐隐遮罩 |
| [CS022 · Containment; contain; content-visibility](../concepts/CS022.md) | 长页面渲染成本 |
| [CS023 · Scroll snap; scroll-margin; overscroll-behavior](../concepts/CS023.md) | 滚动对齐、锚点被导航挡住 |
| [CS024 · Media feature; prefers-color-scheme; prefers-reduced-motion](../concepts/CS024.md) | 深色模式、减少动画 |
| [CS025 · @supports; Progressive enhancement](../concepts/CS025.md) | 新 CSS 不支持怎么办 |
| [CS026 · CSS Modules; BEM; Utility CSS](../concepts/CS026.md) | 类名冲突、工具类、命名规范 |
| [CS027 · Sass/SCSS; PostCSS; Preprocessor](../concepts/CS027.md) | 样式变量编译、自动前缀 |
| [CS028 · Scoped style; Deep selector](../concepts/CS028.md) | 样式改不到组件内部 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 CSS 领域基线，将布局与样式概念落实为尺寸约束、层叠关系和可复现的渲染结果。

### 关键特征

- 先定位尺寸与包含关系，再处理对齐、间距和装饰。
- 层叠、继承及选择器影响范围应明确，沿用项目已有样式组织方式。
- 响应式布局围绕内容与容器约束，不凭单个截图假设所有文本长度和屏幕比例。

### 如何落实

- 标出相关元素的包含块、尺寸来源、最小尺寸和溢出方向，确定造成挤压的约束。
- 根据一维或二维排列需求选用现有布局机制，明确可伸缩区域与不能被压缩的控件。
- 把修复放在拥有该布局责任的样式范围，核对状态类、继承与层叠来源。
- 用实际长文本、动态状态及目标宽度安排换行和溢出策略，动画仅处理任务要求的属性。

### 如何验收

- 在最窄、常用和宽屏容器下核对重排、滚动与可点击区域。
- 放入最长内容并改变字体缩放，确认文字没有遮挡相邻内容或越出控件。
- 对照计算样式核对目标规则生效，同时确认相邻组件与其他状态未受选择器污染。

### 常见误用

- 不断提高选择器优先级或追加固定高度，掩盖错误的尺寸责任。
- 只用裁切和隐藏溢出消除表面问题，导致内容或焦点不可达。
