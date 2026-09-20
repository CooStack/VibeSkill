# HTML

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [HT001 · HTML; Element; Tag; Attribute](../concepts/HT001.md) | 标签属性、网页骨架 |
| [HT002 · DOCTYPE; Standards/Quirks mode](../concepts/HT002.md) | 老页面布局异常 |
| [HT003 · head; body; lang; charset](../concepts/HT003.md) | 文档语言、中文乱码 |
| [HT004 · Content category; Nesting; Void element](../concepts/HT004.md) | 标签嵌套错、自闭合 |
| [HT005 · Boolean attribute; Property reflection](../concepts/HT005.md) | disabled=false 仍禁用 |
| [HT006 · id; class; data-*; dataset](../concepts/HT006.md) | 定位元素、自定义数据 |
| [HT007 · Heading; section; article; nav; main](../concepts/HT007.md) | 标题层级、正文结构 |
| [HT008 · a; href; button](../concepts/HT008.md) | 链接还是按钮、点击跳转 |
| [HT009 · form; action; method; submit](../concepts/HT009.md) | 表单提交、回车触发 |
| [HT010 · input type; name; value; FormData](../concepts/HT010.md) | 取表单值、字段没提交 |
| [HT011 · label; for; fieldset; legend](../concepts/HT011.md) | 点文字选中、字段分组 |
| [HT012 · disabled; readonly; hidden input](../concepts/HT012.md) | 不可编辑但要提交 |
| [HT013 · Constraint validation; required; pattern; validity](../concepts/HT013.md) | 浏览器自动校验、显示错误 |
| [HT014 · select; option; datalist](../concepts/HT014.md) | 下拉选项、可输入建议 |
| [HT015 · textarea; Text content; value](../concepts/HT015.md) | 多行输入默认值不同步 |
| [HT016 · table; caption; th; scope](../concepts/HT016.md) | 数据表头、读屏关联 |
| [HT017 · img; alt; width/height; picture](../concepts/HT017.md) | 图片加载后页面跳 |
| [HT018 · audio; video; source; track](../concepts/HT018.md) | 视频字幕、多格式媒体 |
| [HT019 · iframe; sandbox; allow](../concepts/HT019.md) | 嵌入外部页面、限制能力 |
| [HT020 · script; defer; async; type=module](../concepts/HT020.md) | 脚本加载顺序、阻塞解析 |
| [HT021 · template; DocumentFragment](../concepts/HT021.md) | 模板片段、克隆内容 |
| [HT022 · dialog; showModal; popover; Top layer](../concepts/HT022.md) | 原生弹窗、顶层弹出 |
| [HT023 · details; summary](../concepts/HT023.md) | 原生折叠展开 |
| [HT024 · Web Components; Custom elements; Shadow DOM; slot](../concepts/HT024.md) | 自定义标签、样式封装 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 HTML 领域基线，将文档和控件概念落实为语义结构、原生交互与表单行为。

### 关键特征

- 元素选择先表达内容或操作语义，再决定视觉呈现。
- 文档顺序、可访问名称与表单关联应可独立理解，不只依赖样式或占位文本。
- 原生行为与脚本增强的责任明确，具体元素能力按项目目标环境核对。

### 如何落实

- 按内容关系组织标题、区域、列表和表格，避免用视觉字号代替文档层级。
- 为操作选择链接或按钮等合适元素，明确导航目标、提交类型和禁用语义。
- 为表单控件安排标签、名称、值与错误关联，定义提交数据及重复提交时的界面状态。
- 在需要脚本增强的部位协调焦点、展开状态与原生事件，保留一致的键盘路径。

### 如何验收

- 检查文档结构与可访问名称，核对阅读顺序和视觉含义一致。
- 只用键盘完成相关操作，确认焦点顺序、提交与关闭行为符合约定。
- 核对实际提交数据以及空值、禁用控件和校验失败时的行为。

### 常见误用

- 用可点击容器代替语义控件，却未承担键盘与状态表达责任。
- 把占位提示当作持久标签，或用样式隐藏结构错误。
