# 设计概念

检索分组：产品与体验、结构与交互、视觉系统、排版、验证。
相邻领域：[前端](frontend.md)、[美术](art.md)、[网页无障碍](web.md)。来源入口：S03、S07、S15，见 [sources.md](sources.md)。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| DS001 | UX; User experience | 用起来别扭、体验 | 用户完成目标的整体经历 | 不只视觉美观或 UI |
| DS002 | UI; User interface | 控件、界面样式 | 用户感知和操纵系统的接触层 | 与整体产品价值不同 |
| DS003 | 用户研究 User research; 访谈; 观察 | 不知道用户真正需要什么 | 收集任务、情境和行为证据 | 用户说法与实际行为需交叉验证 |
| DS004 | Persona; 用户画像; JTBD | 为谁做、什么情况下用 | 用角色或待完成任务约束设计 | 不虚构调研事实或刻板标签 |
| DS005 | Problem statement; 成功指标 | 需求模糊、怎么验收 | 把问题、目标群体与可验证结果联系起来 | 解决方案不能冒充问题定义 |
| DS006 | 信息架构 IA; Taxonomy | 栏目怎么分、内容找不到 | 组织内容分类、层级及命名 | 内部组织结构未必适合用户导航 |
| DS007 | Card sorting; Tree testing | 菜单分类验证 | 分别探索分类与验证信息查找路径 | 不是视觉稿满意度调查 |
| DS008 | User flow; Task flow | 操作流程太绕 | 描述任务经过的状态、分支与动作 | 不只绘制理想成功路径 |
| DS009 | Journey map; Service blueprint | 跨渠道体验、后台配合 | 连接用户旅程与服务前后台活动 | 不把想象的旅程当真实调研结论 |
| DS010 | Wireframe; Mockup; Prototype | 线框、高保真、可点击样稿 | 分别探索结构、外观或交互假设 | 保真度应匹配待验证的问题 |
| DS011 | Design system; Component library | 全站一致、多人协作 | 统一原则、语义、组件与使用规则 | 组件库只是设计系统的一部分 |
| DS012 | Design tokens; Semantic tokens | 主题、颜色规范、间距规范 | 用具名值连接设计意图与实现 | 避免把“危险色”硬绑定某个唯一色值 |
| DS013 | Affordance; Signifier; 可供性/指示符 | 看不出能点击、怎么拖 | 区分可采取行动与行动提示 | 视觉像按钮不代表真的可操作 |
| DS014 | Mapping; Mental model | 操作方向反直觉 | 使控制与结果符合用户理解 | 用户模型不必等同实现模型 |
| DS015 | Feedback; 状态可见性 | 点了没反应、不知道完成没 | 及时表达行动结果与系统进度 | 动画反馈不能掩盖真实失败 |
| DS016 | Progressive disclosure; 渐进披露 | 设置太多、界面复杂 | 按当前任务逐步呈现细节 | 高频必要操作不应被深藏 |
| DS017 | Cognitive load; Recognition vs recall | 记不住、信息太多 | 减少工作记忆负担，优先可识别线索 | 简化外观不一定降低认知负担 |
| DS018 | Fitts's law; 目标获取 | 按钮难点、触控误触 | 考虑目标尺寸与距离对操作的影响 | 不机械推导所有按钮都最大 |
| DS019 | Hick-Hyman law; 选择成本 | 选项太多、不知道选哪个 | 关注选择数量及可预测性对决策的影响 | 分类、熟练度和语义也会改变难度 |
| DS020 | Gestalt; 接近/相似/连续/闭合 | 分组混乱、看不出关联 | 利用视觉组织倾向表达关系 | 不用视觉相似暗示错误业务关系 |
| DS021 | Visual hierarchy; 视觉层级 | 主次不清、重点不突出 | 用尺寸、位置、对比与留白引导注意 | 不只把所有标题放大 |
| DS022 | Grid; Alignment; Rhythm | 排版乱、不整齐 | 通过网格、对齐和重复间隔建立秩序 | 设计网格与 CSS Grid 不是同一层概念 |
| DS023 | Whitespace; Density | 太挤、太空、后台低效 | 调整内容密度与分组间距 | 留白不是越多越好，按任务取舍 |
| DS024 | Typography; 字体层级 | 字体乱、阅读累 | 用字体、字号、字重及节奏组织阅读 | 不以增加字体种类解决层级问题 |
| DS025 | Leading; Tracking; Kerning | 行距、字距、字偶距 | 分别调整行间、整体字距和特定字偶 | 三者不可互换；实现遵循项目限制 |
| DS026 | Measure; 行长; Baseline | 长段难读、文字对不齐 | 控制阅读行长与基线关系 | 不用固定高度裁掉可变内容 |
| DS027 | 色彩语义 Semantic color; Contrast | 警告成功颜色、颜色看不清 | 为状态分配可区分的视觉表达 | 同时使用文字或符号，不只依赖颜色 |
| DS028 | Brand identity; Visual identity | 品牌感、统一识别 | 用名称、标识、色彩和图像语汇建立识别 | 不等于给每个界面加大 logo |
| DS029 | Iconography; 图标系统 | 工具按钮、图标不统一 | 统一隐喻、线宽、视觉尺寸与识别方式 | 陌生图标应有名称或可访问标签 |
| DS030 | Microcopy; Content design | 按钮怎么写、错误提示 | 用贴合任务的文字帮助理解与行动 | 不用内部术语或指责用户 |
| DS031 | Microinteraction; 微交互 | 收藏反馈、开关反馈 | 设计触发、规则、反馈与持续状态 | 装饰动画不能代替功能 |
| DS032 | Navigation; Breadcrumb; Tabs | 找不到位置、返回上层 | 表达位置和可选路径或同级视图 | 标签页切换与页面跳转语义要一致 |
| DS033 | Modal; Drawer; Popover; Tooltip | 弹窗还是侧栏、悬浮提示 | 按打断程度、内容和操作类型选容器 | Tooltip 不承载必须操作的复杂内容 |
| DS034 | Empty state; Error recovery | 没数据、失败之后怎么办 | 表达现状并提供合理下一步 | 不把失败伪装为空列表 |
| DS035 | Prevention; Confirmation; Undo | 误删、防后悔 | 用限制、确认或撤销控制操作风险 | 所有动作都确认会形成习惯性跳过 |
| DS036 | Optimistic/Pessimistic feedback | 操作马上生效还是等确认 | 协调响应速度与结果可信度 | 高风险不可逆动作不宜假装成功 |
| DS037 | Usability testing; Think aloud | 用户能不能完成任务 | 观察实际任务完成与障碍 | 引导式提问会污染结果 |
| DS038 | Heuristic evaluation; 启发式评估 | 专家检查界面问题 | 按原则系统发现可用性风险 | 不能完全替代真实用户测试 |
| DS039 | A/B test; 实验分流 | 哪个方案更有效 | 随机对照评估定义好的结果指标 | 样本量、护栏指标及实验偏差需考虑 |
| DS040 | Inclusive design; Universal design | 特殊人群、边缘场景 | 从多样能力及情境设计可参与体验 | 不以“普通用户”排除关键人群 |
| DS041 | Responsive design; Adaptive design | 手机与桌面不同交互 | 连续适配空间或为类别提供专门布局 | 不只缩放视觉，需保留任务能力 |
| DS042 | Design handoff; Acceptance criteria | 设计交付开发、验收 | 明确状态、尺寸、资产、行为与判据 | 单张静态截图不是完整交付 |
