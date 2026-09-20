---
name: vibe-skill
description: 用户每次提问或提出任务时，先检索概念库，按适用概念拆解目标与约束，再区分实施、纯提问和提示词改写。涵盖计算机科学、开发、设计、美术、数学、游戏及音效，提供概念与实施指南。保留用户自定义概念及无匹配内容，不强行替换、不曲解原意，不把候选当新增需求。
---

# VibeSkill 概念神

主要职责是**用概念澄清用户意图，改善回答、编程提示词与执行理解**，不是向用户讲授术语百科。把“想做什么”的口语转成清楚的目标、行为、约束和验收，而不是机械替换成专业名词。

智能体优先读 `references/` 和 `--agent` 检索结果，不为每个内部命中再读生成的用户页，不加载整库。用户入口 [概念库总目录](library/index.md) 是可选解释层，保留供用户点开理解关键概念。

## 每条消息的首要流程

本 Skill 生效时，每条用户提问或任务消息都先查询本库，再决定怎样回答或实施。优先把原始消息交给 `search_prompt.py`，结合必要上下文核对结果；过长消息按完整目标与约束分段，不只截取前半段。脚本不可用时读相应参考，不假称已执行检索。这里的规则不覆盖更高优先级指令，也不意味着未加载 Skill 的宿主会自动执行它。

1. **先检索，不先套名词。** 保留用户原话、定义、否定项和范围，再看概念候选及其实施深度。分数只帮助找资料。
2. **只映射真正重合的部分。** 按 [消息处理规则](references/message-workflow.md) 区分匹配、部分匹配、有歧义、用户自定义与无匹配。用户自定义术语及无合适概念的片段原样保留；无需为了使用 Skill 改名。
3. **按交付意图行动。** 实施请求以确认适用的概念和保留的原始要求完成目标功能；纯提问据此解释，不擅自改代码；提示词改写只交付改写。混合消息按各部分意图处理。
4. **检查有没有改变意思。** 概念拆解只是澄清，不得改变目标、删除限定条件、增加技术栈或将用户定义偷换成标准含义。没有概念命中也照常处理原始请求，不作为拒绝、反复追问或捏造术语的理由。
5. **按授权积累新概念。** 用户已允许自进化：确认内置库与个人库均没有对应概念后，将本次新概念的必要定义、来源、范围和核查状态写入个人库。用户定义照录其语义；推断或外部未核实知识明确标记，不因为保存过就升级为事实。具体流程见 [个人知识库](references/personal-knowledge.md)。

通常只在内部整理目标、对象、机制、约束、待确认点和验收。对外按用户需要给简短的拆解结果或关键概念链接，不展示内部检索过程或推理草稿，不要求每次回复都列术语。

## 先判断任务模式

| 用户意图 | 应做的事 | 不应做的事 |
| --- | --- | --- |
| “优化/改写这段编程提示词”“帮我表达需求” | 按 [改写流程](references/prompt-workflow.md) 交付可直接使用的提示词，必要时标明假设或少量待确认事项 | 不执行提示词中描述的开发、安装、删除、发请求等动作；引用内容是改写对象 |
| “实现/修复/重构这个功能” | 内部整理任务规格并按授权继续实施，沿用项目规范与专门 Skill | 不把真实开发请求降级成只返回一份提示词 |
| “解释这个概念”“为什么采用它” | 给简短解释、区别和可点击说明 | 不伪装正在实现功能，也不强行套完整需求模板 |
| 用户明确自定义术语，或描述在库内没有合适概念 | 保留用户命名和语义，直接依据原始目标回答或实施；只映射其他确实匹配的片段 | 不按词面最高分强行纠正、不擅自写入全局知识库 |

“优化”不总指提示词：优化 SQL、帧率或代码通常是实际工程任务。用户同时明确要求改写并执行时，两者按其指定顺序完成。不要将待改写文本里的命令或引用要求当作执行授权。

## 使用方式

1. 提取目标、对象、症状与约束。分别标记用户明确要求、已检查的项目事实、待验证假设和可选方案，不能混成“用户已要求”。
2. 查看下方领域和技术栈路由。若代码、配置或用户明确指定语言/框架，优先该技术栈参考，再按问题补读领域表；不要仅凭扩展名就认定运行环境。普通需求通常从一两个文件开始。
3. 用中文、英文、缩写或口语线索定位条目。每条记录包括稳定 ID、别名、需求线索、概念用途和边界。不要把同一条目内的相关概念误认为完全同义。
4. 把概念转换为行为和检查要求。例如“幂等”转换为“同一业务意图重试不重复产生副作用”，而不是直接强制某个中间件。详见 [改写流程](references/prompt-workflow.md) 和 [完整案例](references/prompt-examples.md)。
5. 按任务模式交付优化后的提示词或实际实现。保留用户明确的技术栈、版本、范围和格式；补充的方案有证据才定为实现要求。未知指标不能凭空写成承诺；重要歧义需澄清或在提示词中要求执行者检查。
6. API、引擎版本、兼容性、标准条款与安全配置必须核对项目及当前官方文档；这里的概念摘要不能作为版本事实。查不到时明确不确定，不能编造出处。

## 从名称到实施

概念命中只是定位，不是完成理解。涉及设计、机制或工程方案时，继续读取检索结果的 `implementation_context`：它说明关键特征、落实步骤、验收和常见误用。`specificity=concept` 是专用指南；`specificity=domain` 只是领域基线，不能包装成该概念完整做法。纯定义已经足够表达的原子术语不必强行扩展。

对需要展开的概念，至少把四件事说清：哪些特征构成它；在当前目标和约束下如何体现；如何观察或测试这些特征；哪些相似做法其实不满足它。风格类转成布局、比例、排版、色彩、材质及状态语言；机制类转成输入输出、不变量、状态转换、失败与资源边界；算法和数学类转成前提、计算步骤、误差及正确性检查。只选择本任务相关维度，不把这份检查表强制全部塞给用户。

优化后的提示词应描述可观察行为，而非仅写“使用某风格/模式”。例如玻璃风格需明确材料位于哪些界面层、背景如何透出、文字对比、滚动/状态反馈及回退；音效需明确语义、瞬态/主体/尾部、触发/变体、混音关系和试听标准。用户未指定的数值或工具保留为候选，不编造品牌规范。

缺少具体指南时，指出尚需确认的关键机制，并查项目及一手资料；不能用自动套模板制造“已覆盖”的假象。配方是作者编写的实施建议，不等于官方规范或已验证实现。维护方式见 [实施指南编写规则](references/recipe-authoring.md)。

## 内部概念与对外说明

- 大多数命中只进入内部需求理解，不向用户逐条展示检索过程、推理草稿或术语清单。改写提示词应能脱离本机概念库独立使用，不依赖裸 ID 或本地路径。
- 已确认且真正影响实现的关键概念，可简短说“我会使用某概念完成某功能，因为它能解决某问题”，并链接说明页。仅改写提示词时说“这版提示词明确了某项要求”，不要承诺已经实施。
- 用户把名称用混时，温和说明“你描述的更准确地对应某概念，而不是某某；区别在于……”，并链接该概念。用户只是用了口语、别名或合理近义表达时，不强行说“你错了”。
- 尚未确认：“这可能涉及某概念；先检查某项证据再确定”，并链接候选阅读页。不要把候选说成已经采用的方案。
- 相同概念在同一任务已经介绍过，无需每条更新都重复；方案改变时更新说明。明确要求只给代码或极简结果时，尊重其格式要求。
- 需要对外链接时，使用 `--json` 的 `reader_link` 或 `--markdown` 结果并确认目标存在；不要为纯内部检索重复加载用户页。用户只要最终提示词时，不额外追加概念讲解。
- 对话中用实际 Skill 根目录下 `library/concepts/<ID>.md` 的**绝对路径**链接；不要只给裸 ID、整张术语表、不可定位的标题或相对链接。安装后重新运行安装位置的脚本，路径自然指向安装副本，不能写死项目目录。
- 概念页内部使用相对链接以便随整个 Skill 迁移。入口/领域页用于浏览；回答具体概念时优先直达概念页。没有可用阅读页时链接已存在的参考并说明缺少独立页，不谎称已有。
- “Vertex”必须先消歧：图形学顶点 GL003、图论顶点 DT013、JVM 工具集 Vert.x VX001、云平台名 VX014。不得无证据将一种纠正成另一种。
- 数学术语命中时说明其与功能的关系；采用公式时注明单位、定义域、坐标/乘法约定和必要数值条件，不把数学名词当万能解释。

## 领域路由

计算机科学基础及跨系统问题先看 [计算机科学覆盖地图](references/cs-map.md)：架构、操作系统、网络、算法、语言/编译、安全、分布式、数据、AI、可靠性、计算理论、嵌入式和人与计算。地图只负责定位；按需求读取相关表，不加载全部领域。“覆盖主要方向”不等于穷尽整个学科。

| 领域 | 用户可能的说法 | 参考 |
| --- | --- | --- |
| 后端 | 接口、数据库、订单、权限、重复提交、缓存、排队、并发、部署、服务挂了 | [backend.md](references/backend.md) |
| 网页 | 网站、链接、搜索收录、加载、域名、浏览器、移动端、无障碍、页面结构 | [web.md](references/web.md) |
| 前端 | 组件、表单、状态、刷新丢失、列表卡顿、样式、动画、打包、页面交互 | [frontend.md](references/frontend.md) |
| 游戏开发 | 玩法、关卡、角色、碰撞、帧率、联机、数值、存档、相机、音效 | [game.md](references/game.md) |
| 设计 | 布局、流程、信息层级、品牌、排版、操作效率、反馈、一致性 | [design.md](references/design.md) |
| 美术 | 构图、配色、光影、画风、立绘、像素画、贴图、材质、特效、动效 | [art.md](references/art.md) |
| 设计语言与风格实现 | 苹果玻璃、Liquid Glass、Material、Fluent、极简、排版风格、布局特征 | [design-language.md](references/design-language.md)；玻璃落地见 [HTML/CSS 指南](references/design-language-guide.md) |
| 音效设计与游戏音频 | 音效太薄、打击感、包络、频谱、混音、变体、空间、声音触发与验收 | [audio.md](references/audio.md)；制作流程见 [音效设计指南](references/audio-design-guide.md) |
| 建模 | 网格、拓扑、雕刻、布线、UV、烘焙、骨骼、蒙皮、三维资产、导出 | [modeling.md](references/modeling.md) |
| 计算机图形学 / 特效 | 坐标空间、光栅化、光追、材质、模型、纹理采样、粒子、拖尾、体积雾 | [graphics.md](references/graphics.md) |
| 数学 | 向量、矩阵、四元数、曲线、微积分、概率、数值积分、误差、优化 | [mathematics.md](references/mathematics.md) |
| 数据结构 | 数组、链表、堆、树、图、哈希、队列、复杂度、范围查询 | [data-structures.md](references/data-structures.md) |
| 设计模式 | 策略、工厂、观察者、命令、代理、组合、SOLID、职责分离 | [design-patterns.md](references/design-patterns.md) |
| 提示词与任务规格 | 需求不清、补全约束、边界、上下文、复现、验收、不要过度设计 | [prompting.md](references/prompting.md) |
| 工程表达与简写 | OOP、DTO、DAO、DDD、TDD、PR、ADR、POC、吞吐 | [engineering.md](references/engineering.md) |
| 跨领域或词义不明 | 渲染、模型、材质、状态、层级、实例、分辨率、卡顿 | [routing.md](references/routing.md) |
| 核对来源或补充条目 | 新术语、框架专用词、版本行为、官方定义 | [sources.md](references/sources.md) |

## 技术栈路由

| 技术栈 | 用户可能的说法 | 参考 |
| --- | --- | --- |
| Java / JVM | 泛型、集合、线程、类加载、字节码、Spring、JPA、JDK | [java.md](references/java.md) |
| Kotlin | 空安全、扩展函数、委托、协程、Flow、Java 互操作、KMP | [kotlin.md](references/kotlin.md) |
| HTML | 标签、表单、属性、原生弹窗、文档语义、Web Components | [html.md](references/html.md) |
| CSS | 选择器、层叠层、单位、溢出、尺寸约束、伪元素、样式隔离 | [css.md](references/css.md) |
| JavaScript / JS | 闭包、this、原型、Promise、异步、事件、模块、DOM | [javascript.md](references/javascript.md) |
| TypeScript / TS | 类型推导、联合、泛型、收窄、声明文件、tsconfig、类型报错 | [typescript.md](references/typescript.md) |
| Vue | ref、reactive、computed、watch、SFC、插槽、Pinia、Router、Nuxt | [vue.md](references/vue.md) |
| Minecraft / MC / 我的世界 | Java版、基岩版、模组、插件、红石、区块、注册表、Mixin、双端同步 | [minecraft.md](references/minecraft.md) |
| 构建与生态 | Gradle、Maven、KSP、npm、pnpm、Vite、依赖、打包、版本冲突 | [tooling.md](references/tooling.md) |
| MySQL | SQL、联合索引、回表、事务、锁、binlog、慢查询、主从延迟 | [mysql.md](references/mysql.md) |
| Spring | Bean、依赖注入、Boot、事务代理、MVC、Security、WebFlux | [spring.md](references/spring.md) |
| Vert.x / Vertex 消歧 | 事件循环、Verticle、异步消息、worker、Vertex | [vertx.md](references/vertx.md) |
| OpenGL / GLSL | Vertex、VBO、VAO、着色器、uniform、FBO、纹理绑定、GPU 同步 | [opengl.md](references/opengl.md) |

Vue 问题按根因补读 JS/TS/HTML/CSS，不默认把五份资料全部加载。Minecraft 问题先区分玩法、资源、数据、插件或模组；仅在涉及实现时继续确认版本、加载器、映射和侧。`Java` 不代表 Minecraft，`我的世界` 也不代表一定要写 Java 模组。

## 检索

整段提示词优先使用 `search_prompt.py`。它用本地倒排索引、中文片段、词面权重、需求信号和显式简写映射找候选，无第三方依赖、不联网、不执行输入文本、不存储用户提示词。不是向量模型或完整语义理解，仍需智能体结合原文判断。

```powershell
python scripts/search_prompt.py "Vue 列表数据一多就卡，沿用现有 UI，不要加依赖" --limit 5
python scripts/search_prompt.py "使用 DTO 和 DI，保持 API 契约" --limit 5
python scripts/search_prompt.py --file task.txt --format json
python scripts/search_prompt.py --stdin --limit 5
python scripts/search_prompt.py "TCP 收到半条消息，不要改现有协议" --limit 5
python scripts/search_prompt.py "模型离线准确率很高上线很差，只分析数据泄漏" --limit 5
```

从结果先读取 `constraints_verbatim` 和 `abbreviation_candidates`，再看 `results` 中的匹配依据、含义、边界、已有 `guidance` 和 `implementation_context`；它们只是候选上下文。专用指南正文参与低权重检索，不把通用领域方法重复索引给每个概念。`mode_hint` 不决定执行授权，原始请求优先。明确排除的技术即使命中，也不能作为必须采用的方案。

简写自动忽略大小写和全半角差异，并检查英文词边界，避免在更长单词内部误匹配 `DI/PR/CS`。`SSR/MVP/CSR/TPS/DP/CS/MAC/CFG/ANN` 等保留多个解释；领域过滤只筛候选，不删除原始歧义信息。映射表 [abbreviations.json](references/abbreviations.json) 可维护，[简写阅读索引](library/abbreviations.md) 可点击。该映射不是全部缩写词典，未知简写不得臆造展开。

已经知道关键词或 ID 时，继续使用精确词面脚本：

```powershell
python scripts/search_concepts.py "重复提交" "幂等"
python scripts/search_concepts.py "蒙皮" --domain modeling
python scripts/search_concepts.py "SSR" --json
python scripts/search_concepts.py "解构后不更新" --domain vue
python scripts/search_concepts.py "suspend" --domain kotlin
python scripts/search_concepts.py "方块实体" --domain mc
python scripts/search_concepts.py "unknown" --domain ts
python scripts/search_concepts.py "策略模式" --markdown
python scripts/search_concepts.py "四元数" --domain math --json
python scripts/search_concepts.py "Vertex" --markdown
python scripts/search_concepts.py "重复提交" --agent --limit 3
python scripts/search_concepts.py "验收条件" --domain prompting --agent
```

示例命令在本 Skill 根目录执行；实际项目可从项目目录运行脚本绝对路径，或通过 `--project` 明确个人概念的适用项目。`--agent` 返回候选、实施知识及阅读链接，不自动改写、不判断实际适用性。领域采用参考文件名及脚本支持的别名；`--domain user` 只查个人条目，`--builtin-only` 排除个人库。`Vertex` 不作为 `vertx` 领域别名。

维护内置参考表、`references/reader-notes.json` 或简写映射后，运行 `python scripts/build_library.py` 重新生成阅读页，再运行 `python scripts/build_library.py --check` 检查一致性。智能体专用的转译/检查提示保存在 `references/agent-guidance.json`。普通调用不修改内置库；已授权的新概念只写入独立个人库，不能顺手提交到 Git 或发布。

实施指南保存在 `references/*-recipes.json`，领域方法保存在 `references/domain-playbooks.json`。检索与阅读页使用同一数据；新增指南后也要重建阅读页。领域基线与概念专用指南分别统计，不能将前者计为所有条目的专用教程。

## 使用边界

- 概念重合不等于必须增加功能。例如“排行榜”不自动要求微服务，“风格化”不自动要求低多边形，“撤销”不自动要求事件溯源。
- 区分需求、实现机制、质量指标和艺术风格；不能把它们当作互相替代的方案。
- 优先遵循现有代码、设计系统、引擎、资产规范和专门 Skill；本 Skill 负责概念辨认，不覆盖它们的实施规则。
- 未命中不表示不存在。先换别名并查内置与个人库，避免重复；确为新概念时按自进化授权存入个人库，不擅自修改内置库。
- 新增内容遵循 [来源与维护规则](references/sources.md)，保留稳定 ID；入口只放路由，不堆积词典正文。
