# 设计

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [DS001 · UX; User experience](../concepts/DS001.md) | 用起来别扭、体验 |
| [DS002 · UI; User interface](../concepts/DS002.md) | 控件、界面样式 |
| [DS003 · 用户研究 User research; 访谈; 观察](../concepts/DS003.md) | 不知道用户真正需要什么 |
| [DS004 · Persona; 用户画像; JTBD](../concepts/DS004.md) | 为谁做、什么情况下用 |
| [DS005 · Problem statement; 成功指标](../concepts/DS005.md) | 需求模糊、怎么验收 |
| [DS006 · 信息架构 IA; Taxonomy](../concepts/DS006.md) | 栏目怎么分、内容找不到 |
| [DS007 · Card sorting; Tree testing](../concepts/DS007.md) | 菜单分类验证 |
| [DS008 · User flow; Task flow](../concepts/DS008.md) | 操作流程太绕 |
| [DS009 · Journey map; Service blueprint](../concepts/DS009.md) | 跨渠道体验、后台配合 |
| [DS010 · Wireframe; Mockup; Prototype](../concepts/DS010.md) | 线框、高保真、可点击样稿 |
| [DS011 · Design system; Component library](../concepts/DS011.md) | 全站一致、多人协作 |
| [DS012 · Design tokens; Semantic tokens](../concepts/DS012.md) | 主题、颜色规范、间距规范 |
| [DS013 · Affordance; Signifier; 可供性/指示符](../concepts/DS013.md) | 看不出能点击、怎么拖 |
| [DS014 · Mapping; Mental model](../concepts/DS014.md) | 操作方向反直觉 |
| [DS015 · Feedback; 状态可见性](../concepts/DS015.md) | 点了没反应、不知道完成没 |
| [DS016 · Progressive disclosure; 渐进披露](../concepts/DS016.md) | 设置太多、界面复杂 |
| [DS017 · Cognitive load; Recognition vs recall](../concepts/DS017.md) | 记不住、信息太多 |
| [DS018 · Fitts's law; 目标获取](../concepts/DS018.md) | 按钮难点、触控误触 |
| [DS019 · Hick-Hyman law; 选择成本](../concepts/DS019.md) | 选项太多、不知道选哪个 |
| [DS020 · Gestalt; 接近/相似/连续/闭合](../concepts/DS020.md) | 分组混乱、看不出关联 |
| [DS021 · Visual hierarchy; 视觉层级](../concepts/DS021.md) | 主次不清、重点不突出 |
| [DS022 · Grid; Alignment; Rhythm](../concepts/DS022.md) | 排版乱、不整齐 |
| [DS023 · Whitespace; Density](../concepts/DS023.md) | 太挤、太空、后台低效 |
| [DS024 · Typography; 字体层级](../concepts/DS024.md) | 字体乱、阅读累 |
| [DS025 · Leading; Tracking; Kerning](../concepts/DS025.md) | 行距、字距、字偶距 |
| [DS026 · Measure; 行长; Baseline](../concepts/DS026.md) | 长段难读、文字对不齐 |
| [DS027 · 色彩语义 Semantic color; Contrast](../concepts/DS027.md) | 警告成功颜色、颜色看不清 |
| [DS028 · Brand identity; Visual identity](../concepts/DS028.md) | 品牌感、统一识别 |
| [DS029 · Iconography; 图标系统](../concepts/DS029.md) | 工具按钮、图标不统一 |
| [DS030 · Microcopy; Content design](../concepts/DS030.md) | 按钮怎么写、错误提示 |
| [DS031 · Microinteraction; 微交互](../concepts/DS031.md) | 收藏反馈、开关反馈 |
| [DS032 · Navigation; Breadcrumb; Tabs](../concepts/DS032.md) | 找不到位置、返回上层 |
| [DS033 · Modal; Drawer; Popover; Tooltip](../concepts/DS033.md) | 弹窗还是侧栏、悬浮提示 |
| [DS034 · Empty state; Error recovery](../concepts/DS034.md) | 没数据、失败之后怎么办 |
| [DS035 · Prevention; Confirmation; Undo](../concepts/DS035.md) | 误删、防后悔 |
| [DS036 · Optimistic/Pessimistic feedback](../concepts/DS036.md) | 操作马上生效还是等确认 |
| [DS037 · Usability testing; Think aloud](../concepts/DS037.md) | 用户能不能完成任务 |
| [DS038 · Heuristic evaluation; 启发式评估](../concepts/DS038.md) | 专家检查界面问题 |
| [DS039 · A/B test; 实验分流](../concepts/DS039.md) | 哪个方案更有效 |
| [DS040 · Inclusive design; Universal design](../concepts/DS040.md) | 特殊人群、边缘场景 |
| [DS041 · Responsive design; Adaptive design](../concepts/DS041.md) | 手机与桌面不同交互 |
| [DS042 · Design handoff; Acceptance criteria](../concepts/DS042.md) | 设计交付开发、验收 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为设计领域基线，将布局与交互概念落实为具体任务路径、信息层级和可比较的界面方案。

### 关键特征

- 从目标用户要完成的任务确定主次，而非从流行样式推导页面内容。
- 以现有设计系统和内容结构约束布局，保持同类操作的一致表达。
- 美观判断与任务完成效果分别验收，不用装饰代替必要状态和控制。

### 如何落实

- 列出当前任务中的主要决策、输入和结果，给内容及操作排序，保留用户需要比较的信息。
- 用真实或具有代表性的长短内容设计布局，明确密度、对齐、分组和小屏重排方式。
- 为关键操作补齐默认、选中、禁用、等待和错误表达，危险操作的确认强度按后果安排。
- 沿目标任务制作可走通的界面流程，将取舍记录为任务收益与成本，而非只有视觉形容词。

### 如何验收

- 让代表性使用者从入口完成任务，记录误选、回退和停顿位置并与设计目标比较。
- 使用长标题、空数据及高密度内容核对层级、截断和操作可达性。
- 对照已有页面核对术语、间距和同类操作位置，确认差异有任务依据。

### 常见误用

- 为了简洁隐藏关键状态或常用操作，让用户依赖记忆完成任务。
- 把设计偏好写成业务需求，未经确认改动品牌、功能或信息范围。
