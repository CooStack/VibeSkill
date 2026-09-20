# 设计语言与实现概念

检索分组：Apple 材料与 Web 近似、平台设计系统、视觉风格、布局与交付。
相邻领域：[设计](design.md)、[前端](frontend.md)、[CSS](css.md)。
实施配方：[design-recipes.json](design-recipes.json)；玻璃示例与验收：[design-language-guide.md](design-language-guide.md)。

## 使用约定

- 先确认用户要的是平台原生行为、Web 视觉近似，还是某种静态风格。命中名称不意味着必须引入框架、着色器、动画或改写全站。
- 五列表中的同组词用于相关检索，不表示全部同义。DL001-DL009 将一个复杂材料系统拆成可实施、可验收的不同关注点；DL010-DL026 包含设计系统、风格及布局模式，并非同一层级的历史流派。
- Apple、Material、Fluent 的官方行为与本文作者提出的 Web 配方分开看。CSS 数值、布局断点及配色示例都是项目起点，不是官方视觉常量或性能保证。
- DL014-DL024 的风格描述是用于需求转译的可观察特征，不是艺术史定义、唯一规范或风格认证。请用参考图和真实任务进一步约束，不从名称推导年代、创始人或普适比例。
- 配方默认保留语义 HTML、键盘操作、可见焦点、文字缩放、错误恢复。风格不豁免可访问性；必须在真实内容、长文案和状态切换下验收。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| DL001 | Apple Liquid Glass; 苹果液态玻璃; 原生材料 | 像苹果新系统、液态玻璃控件 | Apple 的动态功能层材料，结合背景处理、光色响应及交互变化；原生优先用系统导航和控件，再按需自定义 | 不是给所有内容卡加 blur；行为取决于平台、SDK、系统设置和组件，不是一个固定 CSS 配方 |
| DL002 | Liquid Glass-inspired Web; 苹果玻璃 Web 近似; 网页液态玻璃 | 苹果的玻璃风格用于网页，保留可读性；用 HTML/CSS 做苹果玻璃感；苹果风网页文字清晰 | 将内容层与功能表面分开，以半透明底色、有限背景滤镜、边缘高光、阴影及明确状态模拟层次；具体 HTML/CSS 见本领域实施指南 | CSS 可以近似外观和部分响应，不能宣称完全复制原生折射、光照、融合或自动可读性适配 |
| DL003 | Glassmorphism; 毛玻璃 UI; 传统玻璃拟态 | 磨砂卡片、透出背景、玻璃面板 | 用模糊背景、透色和边界分离形成磨砂表面；可用于少量概览或辅助浮层 | 广义 Web 风格，不等于 Liquid Glass；正文可读性与交互语义不由透明度自动保证 |
| DL004 | Regular / Clear Liquid Glass; 材料变体 | 玻璃更通透、照片上有控件、文字多 | Apple regular 更重视背景处理与可读性；clear 用于照片视频等丰富背景上的控件，必要时加局部衬底 | 原生变体不是两档 CSS blur；Web 应按内容风险定义自己的实色/半透明层，不宣称数值等价 |
| DL005 | Functional layer; Content layer; Scroll edge | 浮动导航、内容滑到工具栏下、层次不清 | 将导航与操作留在功能层，正文留在内容层；滚动边缘保护控件，安全区和布局留量保护内容 | z-index 高不等于层级合理；Web sticky 不自动拥有系统 scroll edge 或键盘避让 |
| DL006 | Optical cues; Edge highlight; Vibrancy / Refraction | 边缘发亮、折射感、玻璃有厚度 | 用边界高光、接触阴影和适度透色提示表面；原生 vibrancy、折射与普通颜色滤镜需分别理解 | 静态 inset shadow 不是光学折射；saturate() 不等于系统 vibrancy，禁止模糊前景文字来冒充材料 |
| DL007 | Material motion; Morphing; 交互状态连续性 | 点击弹性、按钮展开菜单、控件融合 | 让选中、按下、展开和关闭表达同一对象的状态变化；Web 可用有限 transform/opacity 转场保留关系 | 原生容器融合不等于 CSS border-radius 动画；减少动态效果时仍需即时状态反馈 |
| DL008 | Material accessibility; 降低透明度; 高对比 | 玻璃字看不清、关动画、无障碍模式 | 分别处理减少透明度、减少动态效果、强制颜色及前景/合成背景对比；提供页面内实色选项 | 媒体查询支持并不统一；不能把不支持当作用户同意透明，也不能把减少动态当作减少透明 |
| DL009 | Material rendering budget; 玻璃性能 | 滚动掉帧、手机发热、滤镜耗电 | 控制滤镜覆盖面积、重叠层和动态背景，比较增强/实色两种模式的真实设备表现 | 支持 backdrop-filter 不代表性能合格；CSS 没有跨浏览器等价的原生低电量自动材料回退 |
| DL010 | Material Design; Material 3; 语义色角色 | Material 风格、状态统一、主题色 | 用 surface/on-surface、primary/on-primary 等成对角色与排版角色组织组件，状态和任务优先级一致 | 不是大圆角加涟漪；本文核查颜色与排版，不把所有组件版本或 Expressive 行为视为已验证 |
| DL011 | Fluent 2; Fluent design language | 微软风格、工作台、清晰分层 | 区分 solid、mica、acrylic、smoke 的职责，以稳定导航、内容区域及可扫描状态支持工作流 | Fluent 不是全屏透明；Web 借鉴语义与布局，不自动获得 Windows 材料和系统窗口状态 |
| DL012 | Mica; Mica Alt; 云母材料 | 微软窗口底色、桌面壁纸微染色 | Windows 的不透明基础材料融合主题与壁纸色；Web 以用户主题和少量低饱和底色近似层级 | 不是实时看穿窗口的毛玻璃；普通网页没有原生桌面壁纸采样能力，不能伪称已取得壁纸 |
| DL013 | Acrylic; 亚克力材料; Smoke | 半透明菜单、临时浮层、遮罩 | Fluent acrylic 用于临时辅助表面；smoke 弱化模态后方内容。Web 用局部滤镜与独立遮罩近似 | Acrylic 和 smoke 不是同一材质；视觉遮罩不自动阻止背景焦点，不能只画黑层就称模态 |
| DL014 | Minimalism; 极简; 克制界面 | 干净、少装饰、留白、内容优先 | 减少竞争元素，用明确文字层级、对齐、间距和有限强调组织任务 | 极简不等于隐藏标签、只剩图标、低对比灰字或把工作台变成大标题 |
| DL015 | Swiss / International Typographic Style; 瑞士排版 | 严谨网格、大字排版、非对称平衡 | 以共享对齐线、清晰字级、受控行长和图文关系组织信息；用 Grid 实现可重排版面 | 工程特征摘取，不要求某一字体、固定列数或全站大写；视觉顺序不可破坏 DOM 阅读顺序 |
| DL016 | Bauhaus-inspired; 包豪斯启发; 几何构成 | 几何、基本形、色块、功能性 | 用少量几何母题、清楚功能分区和受控色彩关系建立识别，装饰与交互分开 | 不把红黄蓝加圆三角当作充分条件；不声称有唯一历史配色或所有项目都应几何化 |
| DL017 | Web brutalism; 网页粗野主义 | 原始、直接、粗线、非精修感 | 暴露内容结构与链接关系，使用强边界、直接排版和较少装饰层，保留浏览器语义 | 无统一工程规范；故意难读、破坏导航、布局溢出不是风格必需，也不等于建筑定义 |
| DL018 | Neo-brutalism; 新粗野主义 | 粗描边、硬阴影、高彩度、块面按钮 | 用平面填色、明确描边、无模糊投影和清晰按压状态形成图形化控件 | 不是所有 brutalism 的同义词；彩度高不保证明度对比，硬阴影不能成为唯一焦点提示 |
| DL019 | Skeuomorphism; 拟物; 实体隐喻 | 旋钮、纸张、仪表、像真实设备 | 让材质与形状辅助理解已知操作，实际控件仍使用语义输入及可靠状态 | 外观像旋钮不代表必须拖拽旋转；不要引入物理隐喻中无助于任务的限制 |
| DL020 | Neumorphism; Soft UI; 新拟态 | 浮雕、柔软凹凸、同色阴影 | 通过同底色的明暗阴影提示凸起或压入，限制在少量非关键表面 | 低对比是常见风险而非必须追求的特征；表单边界、选中与焦点不能只靠双阴影 |
| DL021 | Flat design; 扁平设计 | 去质感、少阴影、简单图标 | 以色面、线条、文字和布局分组表达结构，保持控件的可辨识性 | 不等于无层级或无状态；可保留必要分隔线、焦点环及弹层边界 |
| DL022 | Editorial UI; 编辑式排版 | 杂志感、长文、图文节奏 | 围绕阅读顺序组织标题、正文、图注和引用，以受控行长及图像比例安排节奏 | 不把正文变成图片，不以花式分栏牺牲移动阅读；不自动要求付费字体或巨大 hero |
| DL023 | Utility-first visual language; Dense workbench; 工具型界面 | 后台、数据密、专业、操作效率 | 以可扫描表格、紧凑筛选、稳定工具区和语义状态支持反复操作，视觉克制但功能完整 | 此处指视觉任务取向，不指 Tailwind 或某个 CSS 库；紧凑不能压缩到不可触控 |
| DL024 | Bento layout; 模块化拼板 | 大小模块、仪表盘拼块、便当布局 | 通过 Grid 的受控跨度区分信息权重，适用于独立且可比较的重复模块 | 不是页面所有区段都套卡片；卡片不能嵌卡片，窄屏必须回到语义顺序而非缩小整张拼图 |
| DL025 | Style tokens; Semantic theme; 风格契约 | 保持风格、换主题、避免拼贴 | 把表面、文字、间距、边框、半径、阴影和状态映射为有限语义变量，记录采用与排除的特征 | 不把所有风格混成一个 token 包；主题切换必须成对更新前景与背景，不能仅替换主色 |
| DL026 | Responsive style continuity; 响应式风格连续性 | 手机不像桌面、缩放溢出、长文案 | 保留信息优先级和交互模型，按可用空间重排导航、列数与操作区，而非等比缩放 | 断点由内容约束决定，不是风格名称给出的固定设备宽度；不得隐藏核心能力来维持截图 |

## 资料与实际核查范围

核查日期：2026-09-20。web 工具未返回可用正文，改用 HTTP 读取官方 HTML、Apple 文档 JSON 和官方仓库 Markdown。下列 URL 是实际读取入口；正文核查不代表图片、视频、全部 API、历史版本或浏览器兼容矩阵已逐项验证。recipes 与 guide 中的工程建议为作者综合转译，不是官方逐字规范。未新建 Sxx 来源编号。

| 资料 URL | 实际核查范围与限制 |
| --- | --- |
| [Apple HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials) / [同页文档 JSON](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/materials.json) | 通过 JSON 阅读功能层/内容层、节制使用、regular/clear、可读性与 standard materials 的正文；未逐图比对，也未验证所有平台分节。支持 DL001、DL004-DL006。 |
| [Apple Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass) / [文档 JSON](https://developer.apple.com/tutorials/data/documentation/technologyoverviews/adopting-liquid-glass.json) | 阅读标准框架采用、显示与辅助设置、控件/导航/工具栏、scroll edge、安全区及性能相关正文；未编译原生示例，不将“最新 SDK”改写为固定版本承诺。支持 DL001、DL005、DL007-DL009。 |
| [Apple Applying Liquid Glass to custom views](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views) / [文档 JSON](https://developer.apple.com/tutorials/data/documentation/swiftui/applying-liquid-glass-to-custom-views.json) | 阅读光色/交互响应、容器组合、形态过渡及性能正文；抽取正文时部分 API 引用以引用节点存在，未核对全部签名与 availability。Web 示例不移植此渲染器。 |
| [MDN backdrop-filter](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter) | 阅读作用于背后像素、半透明条件、语法及 backdrop root/祖先 opacity 影响；未执行 MDN 示例，未读取需要 JS 的完整兼容表。支持 DL002、DL003、DL006、DL009。 |
| [MDN prefers-reduced-transparency](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-transparency) | 阅读 reduce/no-preference、系统偏好与 Limited availability/Experimental 提示；因此保留显式实色路径作为候选，不默认新增设置功能，也不承诺跨浏览器自动适配。 |
| [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) | 初次请求传输失败，重试成功；阅读偏好语义、减少非必要移动和示例覆盖顺序。未采用页面中具体 OS 版本/设置路径作为本库事实。 |
| [MDN forced-colors](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors) | 阅读受影响属性、box-shadow 被移除、系统色和原生语义说明；guide 保留系统颜色及可见边框，不强制保留品牌色。 |
| [Material 3 Color roles](https://m3.material.io/styles/color/roles) | HTTP 只获得页面标题和需要 JavaScript 的外壳，未把此页计为正文已核验；以下官方仓库补足有限范围。 |
| [Material Web color.md](https://raw.githubusercontent.com/material-components/material-web/main/docs/theming/color.md) | 阅读颜色角色、on-* 配对、surface 角色及 CSS custom properties；只证明这套主题机制，不代表组件库维护状态或所有 Material 3 规范。支持 DL010。 |
| [Material Web typography.md](https://raw.githubusercontent.com/material-components/material-web/main/docs/theming/typography.md) | 阅读 typeface/typescale 区别、display/headline/title/body/label 角色和 token；未安装库、加载字体或验证所有代码片段。 |
| [Fluent 2 Material](https://fluent2.microsoft.design/material) | 阅读 solid/acrylic/mica/smoke 的用途、透明性、主题与窗口焦点说明；未审计全部 Fluent 组件。支持 DL011-DL013。 |
| [Microsoft Mica](https://learn.microsoft.com/en-us/windows/apps/design/style/mica) | 页面含通用授权提示，但实际返回可读正文；阅读不透明基础层、壁纸采样、层级及回退条件。未运行 WinUI 或验证列出的版本矩阵。 |
| [Microsoft Acrylic](https://learn.microsoft.com/en-us/windows/apps/design/style/acrylic) | 同样返回授权提示和正文；阅读两类混合、临时表面、避免叠层、GPU/电量、实色回退和材料构成。Web 不声称具有桌面采样或相同 blend 管线。 |
| [W3C Understanding WCAG 2.2: Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | 阅读 1.4.3 的普通文本 4.5:1、大文本 3:1、大小定义及例外；guide 数值只指适用内容，不宣称完整 WCAG 合规。 |
| [W3C Understanding WCAG 2.2: Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) | 阅读 1.4.11 的必要识别信息/状态与相邻色 3:1、边框并非一概必需及例外；未实施产品审计。支持全体配方的对比验收。 |

未核查范围：DL014-DL024 不提供历史归属论证；无真机渲染、辅助技术测试、原生材料实测或性能基准。指南列的是后续验收步骤，不是已通过的测试报告。
