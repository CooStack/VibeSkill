# 资料入口与维护

## 范围与证据

本库覆盖计算机科学主要方向，以及开发、设计、美术、三维资产、计算机图形学、应用数学和音效。技术栈包括 Java/JVM、Kotlin、HTML、CSS、JavaScript、TypeScript、Vue、Minecraft、MySQL、Spring、Vert.x、OpenGL 和构建工具链。用户概念页是摘要与实施索引，不是完整教材、标准全文或逐条引用的权威词典；不声称包含所有术语。

主要消费者为智能体：用概念帮助优化编程提示词和执行理解。`prompting.md`、`prompt-workflow.md`、`prompt-examples.md` 和 `agent-guidance.json` 是本 Skill 作者编写的本地工作约定及示例；`engineering.md` 是补充的稳定工程术语摘要。它们不假托外部研究来源、不宣称某模型必然遵循，也不以词面检索测试代替真实提示词质量评估。

资料入口核查日期：2026-09-19。网页检索工具未返回可用正文，改用 HTTP 获取官方页面。S01-S08、S18-S29 确认了标题及入口；其中 S19/S20/S24/S25/S27/S28 额外阅读了相关正文段落，实际范围见下表。其他来源是后续核对入口。不能把入口核查解释为全部条目已逐项核验；版本化 API、数值阈值和标准条款必须在使用时重新核对。

2026-09-20 补充 S43-S55：网页工具仍未返回可用正文，使用 HTTP 获取下表列明的一手资料。MySQL 主站返回 403，改读 Oracle 托管的同版本手册；Vertex AI 历史入口返回了不同的当前产品标题，因此保留名称消歧并要求使用时核对，不把旧名称写成当前完整产品契约。下表明确区分目录访问与正文核查。

## 来源目录

2026-09-20 计算机科学扩充：新增体系结构、操作系统、网络、算法、语言/编译、安全、分布式、数据、AI、可靠性、理论、嵌入式及人与计算。S56-S74 的状态见下表；本次 HTTP 仅核查列明的页面标题/入口，不声称逐项核验全部摘要。CS2023 入口返回验证页，ACM 伦理入口返回 403，均不记为正文已读取。

| ID | 资料 | 用途 | 核查状态 |
| --- | --- | --- | --- |
| S01 | [MDN Web Glossary](https://developer.mozilla.org/en-US/docs/Glossary) | Web、浏览器、前端基础术语 | 标题及入口已读取 |
| S02 | [Microsoft Cloud Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/) | 后端和分布式模式、适用条件与反模式 | 标题及章节目录已读取 |
| S03 | [W3C WAI Accessibility Introduction](https://www.w3.org/WAI/fundamentals/accessibility-intro/) | 无障碍基础与后续规范入口 | 标题及章节目录已读取 |
| S04 | [Godot Best Practices](https://docs.godotengine.org/en/stable/tutorials/best_practices/index.html) | 场景组织、职责与引擎工作方式 | 标题及入口已读取 |
| S05 | [Blender Manual Glossary](https://docs.blender.org/manual/en/latest/glossary/index.html) | 几何、动画、渲染与资产术语 | 标题及入口已读取 |
| S06 | [Krita Color Concepts](https://docs.krita.org/en/general_concepts/colors.html) | 数字绘画色彩及颜色管理 | 标题及入口已读取 |
| S07 | [GOV.UK Design System Components](https://design-system.service.gov.uk/components/) | 实际界面组件与使用规则 | 标题及章节目录已读取 |
| S08 | [PostgreSQL Concurrency Control](https://www.postgresql.org/docs/current/mvcc.html) | 事务隔离、并发和锁 | 标题及入口已读取 |
| S09 | [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | 认证、授权、输入与 Web 安全 | 后续核对入口，未逐篇读取 |
| S10 | [Google Search SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) / [web.dev](https://web.dev/) | 搜索可发现性与浏览器性能 | 后续核对入口，未逐篇读取 |
| S11 | [React Learn](https://react.dev/learn) | 组件、状态、渲染与副作用示例 | 后续核对入口，非全框架通用契约 |
| S12 | [Vue Guide](https://vuejs.org/guide/introduction.html) | 响应式、组件与生命周期示例 | 后续核对入口，非全框架通用契约 |
| S13 | [Unity Manual](https://docs.unity3d.com/Manual/index.html) | 游戏对象、物理、渲染、资源管线 | 后续核对入口，使用时选项目版本 |
| S14 | [Valve Developer Community: Networking](https://developer.valvesoftware.com/wiki/Source_Multiplayer_Networking) | 联机同步、预测、插值案例 | 后续核对入口，不能泛化引擎默认值 |
| S15 | [Nielsen Norman Group Articles](https://www.nngroup.com/articles/) | 可用性研究、信息架构和交互概念 | 后续核对入口，研究条件须保留 |
| S16 | [Khronos glTF Specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html) | 资产数据、材质、坐标和传输约定 | 后续核对入口，区分规范和扩展 |
| S17 | [OpenUSD Documentation](https://openusd.org/release/index.html) | 场景描述、组合和资产交换 | 后续核对入口，使用时选项目版本 |
| S18 | [Learn Java](https://dev.java/learn/) | Java 语言、标准库和 JVM 学习目录 | 标题及章节目录已读取 |
| S19 | [Kotlin Null Safety](https://kotlinlang.org/docs/null-safety.html) / [Kotlin Docs](https://kotlinlang.org/docs/home.html) | 空安全及语言文档入口 | 空安全页标题、目录及 NPE/Java 互操作相关段落已读取；非全语言逐项验证 |
| S20 | [Kotlin Coroutines Basics](https://kotlinlang.org/docs/coroutines-basics.html) | 挂起、线程、作用域及协程构建器 | 标题、目录及挂起计算/线程关系段落已读取 |
| S21 | [WHATWG HTML Standard](https://html.spec.whatwg.org/multipage/) | 元素、属性、解析和浏览器文档模型 | 标题及总目录已读取，具体条款按需核对 |
| S22 | [MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) | 属性、选择器、规则与语法入口 | 标题及索引章节已读取 |
| S23 | [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) | ECMAScript 语言概念与示例 | 标题及章节目录已读取 |
| S24 | [TypeScript Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html) / [Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) | 类型基础及进一步类型操作入口 | 基础页标题、目录及 any/类型断言无运行时检查段落已读取；非全 Handbook 验证 |
| S25 | [Vue Reactivity Fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals.html) | ref、代理对象、解包和 reactive 的限制 | 标题、目录及替换引用/解构丢失连接段落已读取 |
| S26 | [Fabric Block Entities](https://docs.fabricmc.net/develop/blocks/block-entities) / [Developer Docs](https://docs.fabricmc.net/develop/) | 方块实体及模组开发目录 | 方块实体页标题及章节入口已读取，代码需选对应版本 |
| S27 | [NeoForge Sides](https://docs.neoforged.net/docs/concepts/sides/) | 物理/逻辑侧、单人内置服务器和独立服务端 | 核心区别及专服缺失客户端类的正文段落已读取 |
| S28 | [Paper Scheduling](https://docs.papermc.io/paper/dev/scheduler/) | Tick、同步/异步任务、调度语境 | 标题、目录及线程/Folia 排除说明已读取 |
| S29 | [Minecraft Bedrock Behavior Packs](https://learn.microsoft.com/en-us/minecraft/creator/documents/behaviorpack?view=minecraft-bedrock-stable) | 基岩版行为包入门与结构 | 标题及教程目录已读取；不是 Java 模组文档 |
| S30 | [Gradle User Manual](https://docs.gradle.org/current/userguide/userguide.html) | 任务、依赖、toolchain、缓存及多项目 | 后续核对入口，使用时选 wrapper 对应版本 |
| S31 | [Spring Framework Reference](https://docs.spring.io/spring-framework/reference/) | 容器、代理、事务及 Java 后端框架 | 后续核对入口，非 Java 语言规范 |
| S32 | [Vue Router Guide](https://router.vuejs.org/guide/) | 路由记录、导航与历史模式 | 后续核对入口，使用时核对主版本 |
| S33 | [Pinia Core Concepts](https://pinia.vuejs.org/core-concepts/) | store、状态、动作和类型 | 后续核对入口，非 Vue 核心内置能力 |
| S34 | [Nuxt Documentation](https://nuxt.com/docs) | Vue 全栈框架、数据获取和渲染生命周期 | 后续核对入口，使用时选主版本 |
| S35 | [Forge Documentation](https://docs.minecraftforge.net/en/latest/) | Forge 生命周期与扩展 API | 后续核对入口，不能替代 NeoForge 对应文档 |
| S36 | [SpongePowered Mixin Documentation](https://github.com/SpongePowered/Mixin/wiki) | 字节码混入、注入点及约束 | 后续核对入口，需配合目标字节码及工具链版本 |
| S37 | [Minecraft Java Edition Updates](https://www.minecraft.net/en-us/updates) | 官方版本变化与后续发布说明入口 | 后续核对入口；本文不据此断言任何“最新版本” |
| S38 | [Iris Source Repository](https://github.com/IrisShaders/Iris) | 渲染扩展实现及具体版本兼容线索 | 后续核对入口，第三方生态而非原版 API |
| S39 | [Maven Guides](https://maven.apache.org/guides/) | 生命周期、坐标、依赖范围与多模块 | 后续核对入口，不能机械套用 Gradle 名称 |
| S40 | [KSP Overview](https://kotlinlang.org/docs/ksp-overview.html) | Kotlin 符号处理与处理器模型 | 后续核对入口，核对 Kotlin/处理器兼容性 |
| S41 | [Node.js API](https://nodejs.org/api/) / [npm Documentation](https://docs.npmjs.com/) | 宿主 API、包声明与安装规则 | 后续核对入口，使用时选项目运行时/管理器版本 |
| S42 | [Vite Guide](https://vite.dev/guide/) | 开发服务器、生产构建、环境变量与兼容目标 | 后续核对入口，不固定假定内部打包工具 |
| S43 | [Oracle MySQL 8.4: Clustered and Secondary Indexes](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/innodb-index-types.html) | InnoDB 索引组织；其他 MySQL 机制需另查相应章节 | 标题及聚簇/主键正文已读取；MySQL 主站对应入口本次返回 403 |
| S44 | [Spring AOP Proxying Mechanisms](https://docs.spring.io/spring-framework/reference/core/aop/proxying.html) | 代理、自调用及接口/类代理区别 | 标题及代理机制正文已读取；其他 Spring 专题仍以 S31 为后续入口 |
| S45 | [Vert.x Core](https://vertx.io/docs/vertx-core/java/) | 事件驱动、事件循环、阻塞调用及核心 API | 标题及阻塞 API 相关正文已读取；具体接口以项目版本核对 |
| S46 | [Vertex AI 历史官方入口](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) | 云平台语境消歧 | HTTP 成功但返回标题为 Gemini Enterprise Agent Platform 相关介绍；未据此推断全部改名/兼容关系 |
| S47 | [Open Data Structures](https://opendatastructures.org/) | 作者公开教材，数据结构及复杂度 | 入口可访问，未逐章核验全部摘要 |
| S48 | [Hillside: About Design Patterns](https://hillside.net/patterns/about-patterns) | 模式思想与 GoF 资料定位 | 标题及模式/GoF 相关正文已读取；不是全部模式的逐项证明 |
| S49 | [Khronos glVertexAttribPointer Reference](https://registry.khronos.org/OpenGL-Refpages/gl4/html/glVertexAttribPointer.xhtml) | 顶点属性类型、布局及状态 | 标题及参数入口已读取；其他 GL API 要读各自参考页 |
| S50 | [Khronos glMemoryBarrier Reference](https://registry.khronos.org/OpenGL-Refpages/gl4/html/glMemoryBarrier.xhtml) | GPU 内存访问屏障 | 标题及功能/参数入口已读取；不替代具体访问路径的同步验证 |
| S51 | [Physically Based Rendering, 4th ed.](https://pbr-book.org/4ed/contents) | 作者公开教材，几何、采样、光传输、体渲染 | 目录可访问，未逐章核验全部图形学摘要 |
| S52 | [Blender Shader Nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/index.html) | 材质与着色节点制作入口 | 标题及入口已读取；节点图不是 OpenGL API 文档 |
| S53 | [MIT OCW Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) | 线性代数课程与材料入口 | 课程标题与入口已读取，未逐条证明摘要 |
| S54 | [MIT OCW Probability and Statistics](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/) | 概率统计课程材料 | 课程标题与入口已读取 |
| S55 | [MIT OCW Differential Equations](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/) | 微分方程与数值应用课程材料 | 课程标题与入口已读取 |
| S56 | [CS2023 Knowledge Areas](https://csed.acm.org/knowledge-areas/) | 计算机科学知识领域的后续核对入口 | 返回验证页，未读取课程正文；本库分组不是官方课程逐项映射 |
| S57 | [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) | 作者公开教材，虚拟化、并发和持久化 | 标题及入口已读取，未逐章核验 |
| S58 | [RFC 9293 TCP](https://www.rfc-editor.org/rfc/rfc9293) | TCP 字节流和连接机制 | 标题及入口已读取，协议条款使用时核对 |
| S59 | [RFC 9000 QUIC](https://www.rfc-editor.org/rfc/rfc9000) | 基于 UDP 的安全多路复用传输 | 标题及入口已读取，非全部协议逐条核验 |
| S60 | [LLVM Language Reference](https://llvm.org/docs/LangRef.html) | LLVM IR、SSA 与指令语义 | 标题及入口已读取；不是全部语言规范 |
| S61 | [Raft 作者资料页](https://raft.github.io/) | 共识论文、可视化及实现入口 | 标题及入口已读取；其他协议需各自原文 |
| S62 | [Kubernetes Concepts](https://kubernetes.io/docs/concepts/) | 编排、工作负载及控制器 | 标题及入口已读取，使用时选项目版本 |
| S63 | [scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | 数据划分、预处理与泄漏 | 标题及入口已读取，非全部机器学习摘要逐项证明 |
| S64 | [OpenTelemetry Concepts](https://opentelemetry.io/docs/concepts/) | 可观测信号及上下文 | 标题及入口已读取 |
| S65 | [RISC-V ISA](https://docs.riscv.org/reference/isa/unpriv/unpriv-index.html) | 架构规范入口 | HTTP 返回版本跳转页标题，未逐条读取规范 |
| S66 | [MIT Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | 算法课程材料 | 课程标题及入口已读取 |
| S67 | [MIT Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/) | 自动机、可计算性和复杂度 | 课程标题及入口已读取 |
| S68 | [Apache Flink Timely Stream Processing](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) | 流时间与水位线 | 标题及入口已读取；实现行为需版本核对 |
| S69 | [Zephyr Scheduling](https://docs.zephyrproject.org/latest/kernel/services/scheduling/index.html) | 实时内核调度及任务 | 标题及入口已读取，非所有 RTOS 的通用契约 |
| S70 | [ACM Code of Ethics](https://www.acm.org/code-of-ethics) | 专业责任的后续核对入口 | 本次 HTTP 返回 403，未读正文；不据此作法律判断 |
| S71 | [RFC 1034 DNS Concepts](https://www.rfc-editor.org/rfc/rfc1034) | DNS 结构与概念 | 标题及入口已读取；现代扩展需查后续 RFC |
| S72 | [OWASP Threat Modeling](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) | 威胁建模入口 | 标题及入口已读取，安全配置需另核对 |
| S74 | [RFC 8446 TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) | TLS 协议与安全通信 | 标题及入口已读取，非部署安全保证 |

选择来源时优先使用规范制定者、实现方官方文档和研究原文。社区整理可帮助找关键词，但涉及安全、协议或版本行为时应继续追到一手资料。多个引擎同名术语的行为不同，应分别记录，不能合并成假定的通用事实。

## 条目格式

扩充领域前缀：HW 体系结构、OS 操作系统、NW 网络、AL 算法、LC 语言与编译、SE 安全、DC 分布式、DE 数据工程、ML 人工智能、RE 可靠性、TC 计算理论、EM 嵌入式、HC 人与计算、AU 音效、DL 设计语言。音频和设计语言的一手来源及实际核查边界单列于各自领域文末，避免将风格配方冒充官方数值规范。

全部领域与技术栈表统一使用五列，脚本读取以稳定 ID 开头的行：

```text
| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| BE053 | 中文术语; English; 缩写 | 用户的自然表达 | 能影响决策的简短解释 | 适用条件或易混淆项 |
```

- 前缀：BE 后端、WB 网页、FE 前端、GM 游戏、DS 设计、AR 美术、MD 建模；JV Java、KT Kotlin、HT HTML、CS CSS、JS JavaScript、TS TypeScript、VU Vue、MC Minecraft、TL 工具链；MY MySQL、SP Spring、VX Vert.x/Vertex 名称消歧、DT 数据结构、DP 设计模式、GL OpenGL、CG 图形学、MA 数学；PR 提示词与任务规格、EN 工程表达。ID 全库唯一，不因排序而改号；删除的 ID 不复用。
- 一行表达一个概念或紧密相关的概念组。组内如果并非同义，必须在解释中区分。不要把独立概念为凑数量堆在一起。
- 别名覆盖中文、英文、常见缩写；线索包含用户可能实际说的话，不只重复标题。缩写较短或跨领域重名时同步补充消歧。
- 优先记录“何时想到它、解决什么、何时不能套用”，不要复制百科长文。
- 新的细分领域达到独立阅读价值时才拆文件；同步更新主入口、检索脚本领域映射、测试及相关路由。
- 框架名、软件名和产品名不是概念全集。需要引用时说明它是实例，不将某厂商特性默认为通用机制。
- 保留事实、经验性建议、项目约定的区分。重要新增条目附来源 ID；逐条核验过时可将来源标在该条解释末尾，并在此记录实际核验范围。
- 定期按实际未命中需求补充，不以总数作为质量标准；拒绝宣称“已穷尽”或“全部最新”。

## 用户概念页

- `references/*.md` 的五列表格是基础事实源；`reader-notes.json` 保存按稳定 ID 编写的额外例子及关联 ID。说明同一组里的多个术语时保留区别，不将它们强行当作同义词。
- `scripts/build_library.py` 从上述资料生成 `library/index.md`、领域目录及每个 ID 的独立概念页。它是可重复的内容生成，不需要服务器或前端依赖；不要手改生成页造成分叉。
- 页面提供“这是什么、什么时候会想到它、容易混淆的地方、资料入口”，有人工例子的条目再展示例子及关联。没有详细教程时不伪装成完整百科。
- 页面内部链接为相对路径；对话检索返回基于当前安装根目录计算的绝对 `reader_link`。迁移/安装整包后再次检索即可获得新位置，不复制旧项目路径。
- 修改参考后先重建，再以 `--check` 检查缺失、过时或多余页面。脚本不删除意外文件；异常残留应先核查来源，再有针对性处理。

## 智能体检索元数据

- `agent-guidance.json` 按已存在概念 ID 提供 `translate_to`、`inspect`、`acceptance`、`avoid` 和 `signals`。每个 signal 是需同时出现的短语列表，不是正则或可执行指令；多个 signal 为候选触发的不同表达。
- `abbreviations.json` 为大小写/全半角归一化后的唯一 alias 保存一个或多个 `meanings`；每个含义有展开语境和实际概念 ID。已存在于标题的缩写仍可由词面索引找到；显式映射用于补充展开及跨领域消歧。
- 不能因一个领域常用某简称就删除其他真实含义；尤其 `MVP/SSR/CSR/TPS/VO`。过短且语境不足的简称只作为候选，未知含义保留不确定性。
- `search_prompt.py` 在内存构建索引，默认返回 JSON；接受单段文本、UTF-8 文件或标准输入，上限为 20000 字符以限定查询工作量。无匹配退出码为 1，参数/数据错误为 2，有匹配为 0。
- 分数由词面稀有度、字段、确切短语、元数据与需求信号形成，只用于排序；弱结果还按相对得分过滤，显式简写/ID/需求信号候选保留。不声称是语义向量、置信度或匹配概率。返回原文限制片段帮助智能体防止方案扩张，但不能保证发现全部否定、条件或引用层级。
- 后续添加概念/映射后无需生成持久搜索缓存；每次 CLI 读取当前资料。长期 Python 调用可复用 `PromptIndex`，资料修改后重新构造。

## 验证

`*-recipes.json` 提供概念专用实施指南；`domain-playbooks.json` 提供领域基线。两者是作者编写的条件性应用建议，`implementation_context.specificity` 区分深度；缺少专用配方时不自动制造泛化教程。生成器会同步内容到阅读页，并在 [深度覆盖页](../library/coverage.md)分别统计。维护规则见 [recipe-authoring.md](recipe-authoring.md)。

在 Skill 根目录运行：

```powershell
python -m unittest discover -s tests -v
python scripts/search_concepts.py "重复提交"
python scripts/search_concepts.py "SSR" --json
python scripts/search_concepts.py "解构后不更新" --domain vue
python scripts/search_concepts.py "方块实体" --domain mc
python scripts/build_library.py
python scripts/build_library.py --check
python scripts/search_concepts.py "四元数" --domain math --markdown
python scripts/search_prompt.py "保存点两次创建两条，不要加依赖" --limit 3
python scripts/search_concepts.py "IBO" --agent
```

测试检查检索行为、领域过滤/别名、歧义候选、全库 ID、跨表引用、表格结构、本地链接、用户页生成一致性及安装路径可迁移性。它不证明全部内容正确；还应使用真实需求检查是否只纠正真正的概念误用、是否链接正确页面，以及是否把候选误说成必须采用。

新增整段提示词测试验证代表性口语需求的前列命中、缩写多义、词边界、文件/标准输入、原文限制保留及脚本不执行文本。此类检索回归不是“最终答案一定正确”的语义评测；提示词改写质量仍用案例人工评估。
