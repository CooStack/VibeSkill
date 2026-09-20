# HTML

检索分组：文档与元素、原生交互、表单、媒体与组件边界。
平台安全/SEO/无障碍见 [web.md](web.md)，样式见 [css.md](css.md)，DOM 行为见 [javascript.md](javascript.md)。来源 S21、S01，见 [sources.md](sources.md)。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| HT001 | HTML; Element; Tag; Attribute | 标签属性、网页骨架 | 标记描述文档结构，元素与源代码标签相关但不完全等同 | HTML 不是通用编程语言；解析可修复不合法嵌套 |
| HT002 | DOCTYPE; Standards/Quirks mode | 老页面布局异常 | 文档模式影响浏览器兼容行为 | 不是声明应用使用哪种 JS 框架 |
| HT003 | head; body; lang; charset | 文档语言、中文乱码 | 分离元信息与正文，声明语言及字符编码 | HTTP 与文件编码也要一致 |
| HT004 | Content category; Nesting; Void element | 标签嵌套错、自闭合 | 元素有内容模型，空元素不承载子内容 | HTML 与 XML 自闭合解析不能混用 |
| HT005 | Boolean attribute; Property reflection | disabled=false 仍禁用 | 布尔属性通常以是否出现表达真值 | 字符串 false 不等于布尔 false |
| HT006 | id; class; data-*; dataset | 定位元素、自定义数据 | 分别提供标识、分类与元素附加字符串数据 | data-* 不替代业务状态库或隐藏敏感数据 |
| HT007 | Heading; section; article; nav; main | 标题层级、正文结构 | 用语义组织内容和导航区域 | 按内容结构选标题等级，不只按字体大小 |
| HT008 | a; href; button | 链接还是按钮、点击跳转 | 链接用于导航，按钮用于动作 | 不用无 href 的伪链接替代原生动作控件 |
| HT009 | form; action; method; submit | 表单提交、回车触发 | 定义数据收集与提交行为 | form 内 button 需明确 type 以避免意外提交 |
| HT010 | input type; name; value; FormData | 取表单值、字段没提交 | 类型决定输入语义，name 参与提交数据键 | DOM id 不等于提交字段名 |
| HT011 | label; for; fieldset; legend | 点文字选中、字段分组 | 建立输入名称和关联分组 | placeholder 不代替标签 |
| HT012 | disabled; readonly; hidden input | 不可编辑但要提交 | 禁用、只读和隐藏字段具有不同交互/提交行为 | 禁用控件通常不参与表单提交；隐藏不等于安全 |
| HT013 | Constraint validation; required; pattern; validity | 浏览器自动校验、显示错误 | 利用原生约束与验证 API 表达输入要求 | 前端校验不能替代服务端验证 |
| HT014 | select; option; datalist | 下拉选项、可输入建议 | select 约束选择，datalist 提供建议 | datalist 不是强制枚举校验 |
| HT015 | textarea; Text content; value | 多行输入默认值不同步 | 区分源文档默认内容与运行时当前值 | 不用 innerHTML 设置用户输入文本 |
| HT016 | table; caption; th; scope | 数据表头、读屏关联 | 表达二维数据及标题关系 | 不用 table 搭建整页装饰布局 |
| HT017 | img; alt; width/height; picture | 图片加载后页面跳 | 提供替代信息和固有布局尺寸 | 适配来源及懒加载另见 WB039/WB038 |
| HT018 | audio; video; source; track | 视频字幕、多格式媒体 | 组合媒体源及定时文本轨道 | 自动播放受浏览器与用户设置约束 |
| HT019 | iframe; sandbox; allow | 嵌入外部页面、限制能力 | 嵌入独立文档并限制其权限边界 | sandbox 组合与同源设置需审慎核对 |
| HT020 | script; defer; async; type=module | 脚本加载顺序、阻塞解析 | 定义脚本获取和执行方式 | async 不保证依声明顺序执行，模块语义另有规则 |
| HT021 | template; DocumentFragment | 模板片段、克隆内容 | 保存暂不作为普通活动文档内容的结构 | 模板内容需实例化，不自动绑定业务数据 |
| HT022 | dialog; showModal; popover; Top layer | 原生弹窗、顶层弹出 | 使用平台提供的模态或弹出行为 | 非模态 popover 与模态 dialog 焦点/遮罩语义不同 |
| HT023 | details; summary | 原生折叠展开 | 无需自造完整控件即可表达披露内容 | 不等同复杂树状导航或任意手风琴规则 |
| HT024 | Web Components; Custom elements; Shadow DOM; slot | 自定义标签、样式封装 | 使用平台组件及封装/内容分发机制 | 不等同 Vue 组件、scoped CSS 或 Vue slot |
