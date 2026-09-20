# CSS

检索分组：选择器与层叠、尺寸与排版、布局上下文、绘制、适配与样式工程。
基础盒模型/Flex/Grid/堆叠概念沿用 [frontend.md](frontend.md) FE018-FE027，不重复定义；视觉选择见 [design.md](design.md)。来源 S22、S01，见 [sources.md](sources.md)。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| CS001 | Selector; Combinator | 选中子元素、相邻兄弟 | 用匹配条件与结构关系指定规则目标 | 后代选择与直接子元素选择不同 |
| CS002 | Pseudo-class; :hover; :focus-visible; :checked | 悬停、键盘焦点、勾选样式 | 根据状态或结构匹配元素 | 不把仅 hover 可见内容作为触摸设备唯一入口 |
| CS003 | Pseudo-element; ::before; ::after | 装饰内容、伪元素 | 对生成的或特定元素部分应用样式 | 不承载必须被理解和操作的唯一业务内容 |
| CS004 | :is(); :where(); :not(); :has() | 父级按子元素状态变化 | 组合、排除或关系匹配选择器 | :where 的零特异性与其他函数规则不同 |
| CS005 | Cascade layer; @layer; Origin; important | 第三方样式覆盖冲突 | 通过来源与层组织层叠优先级 | important 会改变层顺序规则，不能只算特异性 |
| CS006 | initial; inherit; unset; revert; revert-layer | 重置样式、回到上一层 | 按不同基准恢复属性值 | 这些关键字不等价于全部回浏览器默认 |
| CS007 | Custom property; var(); Fallback; @property | CSS 变量、主题值、变量动画 | 自定义属性承载可继承值或注册类型 | var 后备值不处理所有计算值无效情况 |
| CS008 | px; em; rem; Percent; vw/vh; dvh | 字号和高度按什么算 | 单位分别依赖 CSS 像素、字体或参考尺寸 | CSS 像素不等于物理像素，移动视口高度可变化 |
| CS009 | calc(); min(); max(); clamp() | 尺寸上下限、混合单位 | 表达响应式约束和数值计算 | 必须有合理约束，不用来规避项目字体规则 |
| CS010 | Logical properties; inline/block; Writing mode | RTL、横竖排适配 | 依书写方向描述尺寸与间距 | inline-size 不总是物理宽度 |
| CS011 | Formatting context; BFC; flow-root | 浮动塌陷、外边距影响父级 | 独立格式化上下文改变布局相互作用 | 不随意用 overflow hidden 裁掉内容来清理浮动 |
| CS012 | Margin collapse; Gap | 上下间距合并、列表间距 | 区分块外边距折叠与布局容器内间隙 | flex/grid 项目间距不能按普通块折叠推断 |
| CS013 | Flex basis/grow/shrink; min-width: 0 | flex 子项挤不下、文本撑破 | 定义基础尺寸与余量分配并处理固有最小尺寸 | flex: 1 不保证任意内容都自动收缩 |
| CS014 | Grid tracks; fr; minmax(); auto-fit/auto-fill | 自动列数、最后一行拉伸 | 用轨道和重复规则分配二维空间 | fr 不是不受内容最小尺寸限制的百分比 |
| CS015 | Subgrid | 子组件列线与父级对齐 | 让嵌套网格共享父级选定轴轨道 | 适用轴与兼容性需核对 |
| CS016 | aspect-ratio; object-fit; object-position | 图片拉伸、裁切位置 | 分别控制盒子比例及替换内容填充和定位 | cover 会裁切，contain 可能留空 |
| CS017 | Text overflow; white-space; overflow-wrap; line-clamp | 省略号、长网址撑破 | 控制换行、溢出及多行截断 | 截断不替代提供完整关键内容的途径 |
| CS018 | Font face; Fallback font; font-display | 字体加载闪、中文缺字 | 定义字体来源及加载时文本显示策略 | 字体替换仍可能改变排版与行数 |
| CS019 | Transform; Transform origin; Containing block | 缩放旋转、fixed 跟错父级 | 变换影响绘制及部分定位/层叠参照 | 变换不按普通文档流重新分配邻居位置 |
| CS020 | Filter; Backdrop filter; Blend mode | 背景毛玻璃、颜色混合 | 分别处理元素或背后像素并定义混合 | 可能增加合成成本及降低文字可读性 |
| CS021 | Clip-path; Mask; Border radius | 裁成形状、渐隐遮罩 | 几何裁剪和透明度遮罩控制可见区域 | 不是改变原始图片或三维几何 |
| CS022 | Containment; contain; content-visibility | 长页面渲染成本 | 在符合边界条件时限制布局/绘制影响或跳过离屏工作 | 需处理固有尺寸，不能当虚拟列表完全替代 |
| CS023 | Scroll snap; scroll-margin; overscroll-behavior | 滚动对齐、锚点被导航挡住 | 控制滚动停靠、目标偏移和滚动链 | 不应使键盘或触摸滚动陷入不可控状态 |
| CS024 | Media feature; prefers-color-scheme; prefers-reduced-motion | 深色模式、减少动画 | 根据用户偏好及环境调整表现 | 不把系统偏好强制覆盖用户明确选择 |
| CS025 | @supports; Progressive enhancement | 新 CSS 不支持怎么办 | 通过能力查询组织可回退样式 | 语法支持不一定代表所有组合行为符合预期 |
| CS026 | CSS Modules; BEM; Utility CSS | 类名冲突、工具类、命名规范 | 分别通过局部命名、约定或单职责类组织样式 | 三者不是 CSS 标准中的同一种机制 |
| CS027 | Sass/SCSS; PostCSS; Preprocessor | 样式变量编译、自动前缀 | 在构建阶段扩展或转换样式代码 | Sass 变量与运行时 CSS 变量行为不同 |
| CS028 | Scoped style; Deep selector | 样式改不到组件内部 | 框架转换选择器以限制作用范围 | Vue scoped 不是 Shadow DOM；详见 VU027 |
