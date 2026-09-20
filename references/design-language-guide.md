# 玻璃设计语言实施指南

本文件是局部工程示例与验收说明，不是生产网站、完整组件库或原生材料复刻。对应 DL001-DL009；其中 **DL002 专门承接“苹果的玻璃风格用于网页，保留可读性”**。实现路径：[HTML 结构](#局部-html) → [CSS 材料与回退](#局部-css) → [实色开关绑定](#实色开关的最小绑定) → [可读性验收](#对比度与辅助验收) → [真机性能](#真机性能与验收记录)。其他风格的实施步骤见 [design-recipes.json](design-recipes.json)。来源 URL 与实际核查范围统一放在 [design-language.md 尾部](design-language.md#资料与实际核查范围)。

## 先确认要实现什么

| 目标 | 能采用的机制 | 不应作出的承诺 |
| --- | --- | --- |
| Apple 原生 Liquid Glass | 在目标 SDK/OS 上采用系统控件、材料及官方容器/过渡能力；验证自定义背景和辅助设置 | 不承诺所有平台、旧版本或自定义控件行为完全相同 |
| Liquid Glass-inspired Web | 内容/功能分层、局部透色、背景模糊、边缘提示、状态反馈和显式回退 | 不称为原生光学折射、系统 vibrancy、自动背景亮度补偿或原生形态融合 |
| 传统 glassmorphism | 少量磨砂表面、背景透色、边界与阴影 | 不因有 blur 就称为 Apple 官方设计语言 |

Apple HIG 把 Liquid Glass 主要用于导航和控制的功能层，而不是让全部内容都透明。原生 regular 和 clear 有各自语境；Web 不以两个 blur 半径冒充这些变体。下面选择偏可读的操作层近似，不尝试 clear 媒体控件或实时折射。

## 结构先于材质

**只改视觉、不改布局的任务**：下面是独立示例，不可整段覆盖已有组件。保留现有字体、尺寸、间距、排列、定位、断点、导航与滚动行为，只提取适用的材料 token、表面与前景样式、状态和回退规则。不要因示例包含设置开关就新增产品功能；优先复用已有设置，额外入口须符合任务范围。

1. 保持正文连续，用 `main` 和语义章节承载任务内容。导航是 `nav`，跳转是 `a`，命令才是 `button`，不要把 `div` 画成所有控件。
2. 一个关联操作组共用一个材料面，避免每个按钮各自滤镜。示例中的链接有不透明前景承载面，牺牲部分通透来稳定文字对比。
3. 使用文档流和可换行布局。`sticky` 保留初始占位，但仍可能遮住滚动锚点或焦点；`fixed` 更需要额外的内容留位。
4. 材质由背景 alpha、有限滤镜、边界和阴影协作表达。整个父元素的 `opacity` 会连文字一起变淡，也可能改变后代背景滤镜的采样边界。
5. 圆角是功能表面轮廓，不是给所有内容加卡片的许可。下面的胶囊只用于紧凑导航项，正文不套卡片。

## 局部 HTML

以下片段可嵌入已有页面评估。没有外部图片、字体或库依赖，不创建网站文件；接入项目时沿用现有语义、路由和设计 token。若已有同名 ID，应改为项目唯一值。

```html
<div class="dl-demo" data-effects="solid">
  <label class="dl-setting" hidden>
    <input id="dl-solid" type="checkbox">
    使用不透明界面
  </label>

  <nav class="dl-glass" aria-label="本页章节">
    <a href="#dl-overview">概览</a>
    <a href="#dl-details">详细信息</a>
    <a href="#dl-history">历史记录</a>
  </nav>

  <main class="dl-content">
    <section id="dl-overview" aria-labelledby="dl-overview-title">
      <h2 id="dl-overview-title">概览</h2>
      <p>这里放项目的真实内容，而不是为了透色添加的装饰背景。</p>
    </section>
    <section id="dl-details" aria-labelledby="dl-details-title">
      <h2 id="dl-details-title">详细信息</h2>
      <p>长正文保持稳定背景；用实际长度的数据验证布局。</p>
    </section>
    <section id="dl-history" aria-labelledby="dl-history-title">
      <h2 id="dl-history-title">历史记录</h2>
      <p>滚动、锚点跳转和键盘操作都要检查最后一项是否可见。</p>
    </section>
  </main>
</div>
```

此处是章节导航，不是 ARIA tabs，不添加 `role="tab"`。也没有假装实现当前位置高亮；若项目要 scrollspy，另按真实当前章节设置 `aria-current="location"`。页面已有 `main` 时，嵌入片段的 `main` 应改为合适的普通容器，避免多个未区分的主地标。

## 局部 CSS

数值是作者给出的调试起点，不是 Apple 参数。所有规则限定在 `.dl-demo`；不要把示例中的局部重置扩散到整个产品。

```css
.dl-demo {
  --dl-page: #f4f5f6;
  --dl-surface: #ffffff;
  --dl-glass-fill: rgb(255 255 255 / 86%);
  --dl-text: #17191c;
  --dl-border: #737982;
  --dl-focus: #0755b5;
  --dl-highlight: rgb(255 255 255 / 80%);
  --dl-shadow: 0 5px 16px rgb(0 0 0 / 12%);
  --dl-sticky-offset: 0.5rem;
  color-scheme: light;
  color: var(--dl-text);
  background: var(--dl-page);
  font: 1rem/1.5 system-ui, sans-serif;
  letter-spacing: 0;
  padding: 1rem;
}

.dl-demo,
.dl-demo *,
.dl-demo *::before,
.dl-demo *::after {
  box-sizing: border-box;
}

.dl-demo .dl-setting {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-block-end: 1rem;
}

.dl-demo .dl-setting[hidden] {
  display: none;
}

.dl-demo .dl-setting input {
  flex: none;
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.dl-demo .dl-glass {
  position: sticky;
  inset-block-start: var(--dl-sticky-offset);
  z-index: 2;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  inline-size: fit-content;
  max-inline-size: 100%;
  padding: 0.5rem;
  border: 1px solid var(--dl-border);
  border-radius: 1.5rem;
  background: var(--dl-surface);
  box-shadow: var(--dl-shadow),
    inset 0 1px 0 var(--dl-highlight);
}

.dl-demo .dl-glass a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 0;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.875rem;
  border: 1px solid var(--dl-border);
  border-radius: 999px;
  color: var(--dl-text);
  background: var(--dl-surface);
  text-decoration: underline;
  text-underline-offset: 0.2em;
  overflow-wrap: anywhere;
  transition: transform 120ms ease-out;
}

.dl-demo .dl-glass a:active {
  transform: translateY(1px);
}

.dl-demo :where(a, input):focus-visible {
  outline: 3px solid var(--dl-focus);
  outline-offset: 3px;
}

.dl-demo .dl-content {
  max-inline-size: 68ch;
  padding-block-start: 1.5rem;
  margin-inline: auto;
}

.dl-demo .dl-content section {
  padding-block: 1rem;
  scroll-margin-block-start: 6rem;
  overflow-wrap: anywhere;
}

@media (prefers-color-scheme: dark) {
  .dl-demo {
    --dl-page: #181a1e;
    --dl-surface: #25282e;
    --dl-glass-fill: rgb(37 40 46 / 90%);
    --dl-text: #f4f5f7;
    --dl-border: #a6adb8;
    --dl-focus: #9ccaff;
    --dl-highlight: rgb(255 255 255 / 16%);
    --dl-shadow: 0 5px 16px rgb(0 0 0 / 28%);
    color-scheme: dark;
  }
}

@supports ((backdrop-filter: blur(1px)) or
           (-webkit-backdrop-filter: blur(1px))) {
  .dl-demo .dl-glass {
    background: var(--dl-glass-fill);
    -webkit-backdrop-filter: blur(12px) saturate(115%);
    backdrop-filter: blur(12px) saturate(115%);
  }
}

.dl-demo[data-effects="solid"] .dl-glass {
  background: var(--dl-surface);
  -webkit-backdrop-filter: none;
  backdrop-filter: none;
}

@media (prefers-reduced-transparency: reduce), (prefers-contrast: more) {
  .dl-demo .dl-glass {
    background: var(--dl-surface);
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    box-shadow: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .dl-demo .dl-glass a {
    transition: none;
  }

  .dl-demo .dl-glass a:active {
    transform: none;
  }
}

@media (max-width: 40rem) {
  .dl-demo .dl-glass {
    position: static;
    inline-size: 100%;
  }

  .dl-demo .dl-content section {
    scroll-margin-block-start: 1rem;
  }
}

@media (forced-colors: active) {
  .dl-demo {
    --dl-page: Canvas;
    --dl-surface: Canvas;
    --dl-glass-fill: Canvas;
    --dl-text: CanvasText;
    --dl-border: ButtonText;
    --dl-focus: Highlight;
  }

  .dl-demo .dl-glass {
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    box-shadow: none;
  }

  .dl-demo .dl-glass a {
    color: LinkText;
    border-color: LinkText;
  }
}
```

示例不设置 `overflow: hidden`，避免剪掉焦点环；阴影只是辅助线索。`prefers-contrast: more` 是额外增强策略，本次未单独核查其兼容矩阵，不能代替强制颜色或实色开关。较旧环境忽略不认识的媒体特性时，基础实色样式和显式开关仍必须可用。

示例的 `6rem` 锚点留量只适合当前短标签，不是任意语言、缩放和工具栏高度的通用保证。接入后若宽屏也会多行，应按真实高度同步留量，或像窄屏一样恢复普通流；同时核查页面其他 sticky 栏，并将其偏移纳入 `--dl-sticky-offset`。不要为保留玻璃外观剪掉长标签。

## 实色开关的最小绑定

此绑定只更改当前片段，不存储偏好、不发送请求。生产接入应使用项目已有设置状态；需要跨页记忆时再接入现有持久化逻辑，并处理存储失败。系统减少透明度/强制颜色规则仍然优先，不允许用“增强”选项抵消它们。

```js
const root = document.querySelector(".dl-demo");
const solid = root?.querySelector("#dl-solid");

if (root && solid) {
  const applyPreference = () => {
    root.dataset.effects = solid.checked ? "solid" : "auto";
  };
  solid.addEventListener("change", applyPreference);
  applyPreference();
  solid.closest(".dl-setting").hidden = false;
}
```

集成时脚本应在元素存在之后运行。HTML 默认 `data-effects="solid"` 并隐藏设置；只有绑定完成才显示开关并允许增强，因此无 JS 时保留实色，不留下无作用的设置。也可接入项目已有的 CSS/服务端偏好路径；此处不实现跨页持久化。

## 两种进一步场景

### 媒体上的通透控制

照片/视频上的暂停、音量、返回等控件，需要先保证随帧变化的可读性。优先给控件一个稳定实色或足够强的局部衬底，再按实际素材尝试提高通透。若用暗色局部遮罩，必须测试高亮画面、字幕和控件下方明暗交界，不能只取视频首帧。

不要承诺 CSS 会像原生 clear 材料自动处理所有背景。不默认加入 canvas 逐帧取色：它增加性能、跨源和实现边界问题。用户明确需要时，另行规定适用媒体、取样频率、失效回退及性能预算。

### 按钮展开浮层

优先复用已有 popover/dialog 组件，先决定是否模态。模态弹窗要有可访问名称、适当初始焦点、背景交互约束和关闭后的焦点归还；非模态浮层不应无故锁住全页。视觉上可以让浮层靠近触发点、用短暂 opacity/transform 维持关系，但不能把这种普通转场称为 Liquid Glass 原生融合。

不要让关闭流程依赖动画结束事件；在减少动态、后台标签页或中途取消时，交互状态也必须正确结束。

## 对比度与辅助验收

- WCAG 2.2 的 1.4.3：适用普通文本至少 4.5:1；大文本至少 3:1，大文本通常按至少 18pt，或至少 14pt 粗体判断，并注意字体与规范定义。不要把任意标题标签都当成大文本。例外需按原规范判断。
- 1.4.11：识别控件、状态或理解图形所必需的非文本信息，与相邻色至少 3:1；不是每条装饰边框都必须达到该值。焦点必须可辨认，不能只靠会被强制颜色移除的阴影。
- 在玻璃场景，评价的是文字背后实际合成结果，而不是仅拿 `background: rgba(...)` 的 RGB 部分计算。对预定背景、滚动位置和视频最不利帧建立覆盖；背景不可控时改用不透明文字衬底。
- 评估颜色时不要以抗锯齿后的字缘像素替代文字本身颜色。自动检测不能证明所有动态合成状态合格，人工检查也不能替代完整可访问性审计。
- 分别测试减少透明度、减少动态、增加对比、强制颜色和页面实色开关。减少动态不必然减少透明，系统关闭透明也不保证所有浏览器都能通过媒体查询获知。
- 使用键盘和目标屏幕阅读器验证名称、顺序、当前状态、错误和焦点归还；使用 200% 文本放大及窄视区做回流检查。这里是测试集合，不是完整 WCAG 合规声明。

## 真机性能与验收记录

不要只以“看起来流畅”结案，也不要把浏览器模拟节流当成真实 GPU、电量和温升测试。按项目支持范围选中低端手机、桌面和代表性浏览器，记录型号、OS、浏览器版本、DPR、刷新率与测试内容。

| 场景 | 比较内容 | 未通过时优先处理 |
| --- | --- | --- |
| 静态正文滚过工具栏 | 相同数据的增强/实色轨迹、帧间隔、绘制与合成活动 | 减小滤镜面积，取消嵌套滤镜，检查祖先效果 |
| 视频或高频背景经过材料 | 持续滚动/播放下的掉帧、可读性和设备温升现象 | 局部实色衬底，停止无必要背景动画 |
| 菜单快速开关与输入 | 操作到反馈延迟、焦点和布局是否稳定 | 简化转场，分离业务更新与装饰，排查长任务 |
| 实色/辅助模式切换 | 布局、焦点、状态和功能是否保持 | 移除只靠材质表达的交互，修正覆盖顺序 |
| 不支持滤镜或媒体特性 | 默认表面与页面设置是否可用 | 让实色成为完整路径，而不是空白回退 |

先由项目确定目标设备及可接受帧间隔、延迟与功耗目标，再记录实测；本文不设伪精确的通用毫秒或层数上限。`will-change` 不是免费加速开关，不默认放在每个组件上。浏览器工具未暴露的 GPU/电量信息应注明未测，不从主线程耗时推算。

交付记录至少包含：场景、设备与版本、增强/实色两组结果、异常复现步骤、采用的回退和仍未覆盖项。本次只核查资料并编写参考文本，未在浏览器、原生应用或真实设备运行这些片段；代码与验收步骤需要集成后验证。
