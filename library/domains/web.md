# 网页与 Web 平台

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [WB001 · URL; URI; 路径 Path; 查询 Query; Fragment](../concepts/WB001.md) | 链接参数、锚点 |
| [WB002 · DNS; 域名 Domain](../concepts/WB002.md) | 域名打不开、解析 |
| [WB003 · HTTP; Method; Status code](../concepts/WB003.md) | 404、请求返回错误 |
| [WB004 · HTTPS; TLS; 证书 Certificate](../concepts/WB004.md) | 安全连接、证书错误 |
| [WB005 · Origin; 同源策略 SOP](../concepts/WB005.md) | 不同域名访问 |
| [WB006 · CORS; 预检 Preflight](../concepts/WB006.md) | 跨域报错、OPTIONS |
| [WB007 · CSP; Content Security Policy](../concepts/WB007.md) | 限制脚本来源 |
| [WB008 · XSS; 上下文编码; Sanitization](../concepts/WB008.md) | 用户内容执行脚本 |
| [WB009 · CSRF; SameSite; 防伪令牌](../concepts/WB009.md) | 被诱导发请求、跨站提交 |
| [WB010 · Cookie; Secure; HttpOnly](../concepts/WB010.md) | 浏览器自动带登录凭据 |
| [WB011 · HTTP 缓存; Cache-Control; ETag; 304](../concepts/WB011.md) | 页面资源老不更新 |
| [WB012 · CDN; 边缘缓存 Edge cache](../concepts/WB012.md) | 全球访问慢、静态资源 |
| [WB013 · 重定向 Redirect; 301; 302; 307; 308](../concepts/WB013.md) | 换地址、登录跳转 |
| [WB014 · 语义 HTML; Landmark](../concepts/WB014.md) | 页面结构、读屏理解 |
| [WB015 · 元信息 Metadata; title; meta description](../concepts/WB015.md) | 标签页标题、搜索摘要 |
| [WB016 · SEO; Crawling; Indexing](../concepts/WB016.md) | 搜不到、搜索收录 |
| [WB017 · robots.txt; Sitemap; noindex](../concepts/WB017.md) | 不让搜索收录、站点地图 |
| [WB018 · Canonical; 规范网址](../concepts/WB018.md) | 重复页面、带参数同内容 |
| [WB019 · Structured data; 结构化数据](../concepts/WB019.md) | 富媒体搜索结果 |
| [WB020 · Open Graph; 社交卡片](../concepts/WB020.md) | 分享链接预览 |
| [WB021 · 响应式 Responsive; Viewport; Breakpoint](../concepts/WB021.md) | 手机适配、宽屏 |
| [WB022 · 渐进增强 Progressive enhancement](../concepts/WB022.md) | 老浏览器也能用 |
| [WB023 · 无障碍 Accessibility; a11y](../concepts/WB023.md) | 键盘操作、读屏、可访问 |
| [WB024 · WCAG; 可感知/可操作/可理解/健壮](../concepts/WB024.md) | 无障碍验收 |
| [WB025 · ARIA; 可访问名称 Accessible name](../concepts/WB025.md) | 图标按钮读什么 |
| [WB026 · 焦点 Focus; Tab 顺序; 焦点陷阱](../concepts/WB026.md) | 弹窗键盘乱跳 |
| [WB027 · 替代文本 Alt text; 字幕 Captions](../concepts/WB027.md) | 图片说明、视频听不见 |
| [WB028 · 对比度 Contrast; Reduced motion](../concepts/WB028.md) | 看不清、动画眩晕 |
| [WB029 · 表单语义 Label; Autocomplete; Validation](../concepts/WB029.md) | 输入提示、自动填充 |
| [WB030 · History API; 深链接 Deep link](../concepts/WB030.md) | 刷新 404、返回上一页 |
| [WB031 · localStorage; sessionStorage](../concepts/WB031.md) | 刷新后保留、当前标签页 |
| [WB032 · IndexedDB](../concepts/WB032.md) | 本地大量结构化数据 |
| [WB033 · Service Worker; PWA; 离线 Offline](../concepts/WB033.md) | 断网还能用、安装网页 |
| [WB034 · WebSocket; SSE; Polling](../concepts/WB034.md) | 实时聊天、进度推送 |
| [WB035 · WebRTC](../concepts/WB035.md) | 音视频通话、点对点 |
| [WB036 · Core Web Vitals; LCP; INP; CLS](../concepts/WB036.md) | 首屏慢、点击迟钝、页面跳 |
| [WB037 · TTFB; 关键渲染路径](../concepts/WB037.md) | 第一字节慢、白屏 |
| [WB038 · Lazy loading; 预加载 Preload; Prefetch](../concepts/WB038.md) | 图片按需、提前加载 |
| [WB039 · 响应式图片 srcset; sizes; picture](../concepts/WB039.md) | 手机图片太大、不同裁切 |
| [WB040 · 国际化 i18n; 本地化 l10n; RTL](../concepts/WB040.md) | 多语言、日期货币 |
| [WB041 · Canvas; SVG; WebGL; WebGPU](../concepts/WB041.md) | 网页画图、交互三维 |
| [WB042 · 浏览器权限 Permissions; 安全上下文](../concepts/WB042.md) | 摄像头、定位、剪贴板 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为网页领域基线，将概念落实到文档、URL、浏览器加载与导航行为；只检查本次页面适用的访问场景。

### 关键特征

- 把 URL 对应的资源、页面状态和导航结果作为可独立验证的契约。
- 区分服务器响应、浏览器解析与脚本增强各阶段的问题，避免把所有故障归因于页面组件。
- 公开可访问性、搜索收录与离线能力分别按需求确认，不从网站类型推导额外功能。

### 如何落实

- 明确目标 URL、路径参数、查询参数和刷新后的状态恢复规则，区分页面不存在与数据为空。
- 梳理文档及关键资源的获取顺序，为任务涉及的加载、失败和导航中断安排可见结果。
- 核对实际部署路径、相对资源地址和跳转目标，使站内导航与直接访问指向同一页面语义。
- 按目标浏览器和访问方式安排文档语义与渐进增强；仅在有收录要求时定义可索引内容及元数据。

### 如何验收

- 直接打开深层链接、刷新并使用前进后退，核对页面与 URL 表达的状态一致。
- 模拟关键资源缺失或网络变慢，核对错误反馈和剩余可用内容，不出现无法解释的空白。
- 在约定的屏幕尺寸和输入方式下完成核心导航，核对链接目标、焦点与内容顺序。

### 常见误用

- 只验证开发服务器内的点击跳转，遗漏部署后的深层路径和资源地址。
- 把可交互、可收录、可离线视为同一验收目标并全部强加给任务。
