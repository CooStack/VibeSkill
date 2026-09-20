# 设计语言与风格实现

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [DL001 · Apple Liquid Glass; 苹果液态玻璃; 原生材料](../concepts/DL001.md) | 像苹果新系统、液态玻璃控件 |
| [DL002 · Liquid Glass-inspired Web; 苹果玻璃 Web 近似; 网页液态玻璃](../concepts/DL002.md) | 苹果的玻璃风格用于网页，保留可读性；用 HTML/CSS 做苹果玻璃感；苹果风网页文字清晰 |
| [DL003 · Glassmorphism; 毛玻璃 UI; 传统玻璃拟态](../concepts/DL003.md) | 磨砂卡片、透出背景、玻璃面板 |
| [DL004 · Regular / Clear Liquid Glass; 材料变体](../concepts/DL004.md) | 玻璃更通透、照片上有控件、文字多 |
| [DL005 · Functional layer; Content layer; Scroll edge](../concepts/DL005.md) | 浮动导航、内容滑到工具栏下、层次不清 |
| [DL006 · Optical cues; Edge highlight; Vibrancy / Refraction](../concepts/DL006.md) | 边缘发亮、折射感、玻璃有厚度 |
| [DL007 · Material motion; Morphing; 交互状态连续性](../concepts/DL007.md) | 点击弹性、按钮展开菜单、控件融合 |
| [DL008 · Material accessibility; 降低透明度; 高对比](../concepts/DL008.md) | 玻璃字看不清、关动画、无障碍模式 |
| [DL009 · Material rendering budget; 玻璃性能](../concepts/DL009.md) | 滚动掉帧、手机发热、滤镜耗电 |
| [DL010 · Material Design; Material 3; 语义色角色](../concepts/DL010.md) | Material 风格、状态统一、主题色 |
| [DL011 · Fluent 2; Fluent design language](../concepts/DL011.md) | 微软风格、工作台、清晰分层 |
| [DL012 · Mica; Mica Alt; 云母材料](../concepts/DL012.md) | 微软窗口底色、桌面壁纸微染色 |
| [DL013 · Acrylic; 亚克力材料; Smoke](../concepts/DL013.md) | 半透明菜单、临时浮层、遮罩 |
| [DL014 · Minimalism; 极简; 克制界面](../concepts/DL014.md) | 干净、少装饰、留白、内容优先 |
| [DL015 · Swiss / International Typographic Style; 瑞士排版](../concepts/DL015.md) | 严谨网格、大字排版、非对称平衡 |
| [DL016 · Bauhaus-inspired; 包豪斯启发; 几何构成](../concepts/DL016.md) | 几何、基本形、色块、功能性 |
| [DL017 · Web brutalism; 网页粗野主义](../concepts/DL017.md) | 原始、直接、粗线、非精修感 |
| [DL018 · Neo-brutalism; 新粗野主义](../concepts/DL018.md) | 粗描边、硬阴影、高彩度、块面按钮 |
| [DL019 · Skeuomorphism; 拟物; 实体隐喻](../concepts/DL019.md) | 旋钮、纸张、仪表、像真实设备 |
| [DL020 · Neumorphism; Soft UI; 新拟态](../concepts/DL020.md) | 浮雕、柔软凹凸、同色阴影 |
| [DL021 · Flat design; 扁平设计](../concepts/DL021.md) | 去质感、少阴影、简单图标 |
| [DL022 · Editorial UI; 编辑式排版](../concepts/DL022.md) | 杂志感、长文、图文节奏 |
| [DL023 · Utility-first visual language; Dense workbench; 工具型界面](../concepts/DL023.md) | 后台、数据密、专业、操作效率 |
| [DL024 · Bento layout; 模块化拼板](../concepts/DL024.md) | 大小模块、仪表盘拼块、便当布局 |
| [DL025 · Style tokens; Semantic theme; 风格契约](../concepts/DL025.md) | 保持风格、换主题、避免拼贴 |
| [DL026 · Responsive style continuity; 响应式风格连续性](../concepts/DL026.md) | 手机不像桌面、缩放溢出、长文案 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为设计语言领域基线，将材料、风格和布局名称转成有限视觉特征与状态契约，明确平台原生行为和 Web 近似的区别。

### 关键特征

- 先确认原生采用、网页近似或静态风格目标，不从风格名称推导框架、动画或全站改造。
- 以内容和操作层级选择材料与布局，风格不能牺牲语义、可读性与完整状态。
- 采用有限且一致的表面、文字、边界和状态规则，不把多个风格随意拼接或声称数值等同官方规范。

### 如何落实

- 从参考中列出需要保留和明确排除的特征，区分材料机制、视觉线索与布局方式。
- 映射到项目已有的语义主题变量和组件状态，为前景背景成对指定表达并保护正文层。
- 只在承担相应职责的区域应用透明、阴影或运动；涉及增强材料时设计实色或减少动态的可用表现。
- 用真实内容接入页面，在长文案、小屏和状态切换下重排；涉及滤镜时对比增强与基础模式的实际渲染成本。

### 如何验收

- 对照参考及任务目标检查层级和风格连续性，确认没有依赖装饰隐藏核心能力。
- 检查变化背景、主题切换、文字缩放和键盘焦点，必要边界与状态在基础模式下仍可辨认。
- 在目标设备滚动、展开和重排界面，核对内容遮挡、交互连续性及任务已有的性能预算。

### 常见误用

- 把模糊、圆角或双阴影视为完整设计系统，混淆视觉近似与原生材料能力。
- 为保持截图外观隐藏操作或缩小整页，忽略长内容、可访问性与渲染成本。
