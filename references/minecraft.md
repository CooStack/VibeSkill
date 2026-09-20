# Minecraft / 我的世界

检索分组：版本生态、世界与玩法、资源数据、模组 API、联机与生命周期、渲染性能。
语言与构建见 [java.md](java.md)、[kotlin.md](kotlin.md)、[tooling.md](tooling.md)；图形学见 [game.md](game.md)、[modeling.md](modeling.md)。来源 S26-S29、S35-S38，见 [sources.md](sources.md)。

## 先确认语境

- 先辨别 Java Edition / Bedrock Edition，再辨别 Mod / Plugin / Data Pack / Resource Pack / Add-on。
- 开发问题需要游戏版本、加载器及版本、映射命名、JDK 和物理/逻辑侧。只讨论玩法术语时，不必额外盘问完整技术栈。
- 类名如 Level/World、Identifier/ResourceLocation、BlockEntity/TileEntity 可能来自不同版本或映射；这里只帮助识别概念，不能据此拼凑跨版本可运行代码。
- 正式修改模组代码时，使用目标项目的开发规范及可用的 Minecraft 专门 Skill；本表不替代实现规约。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| MC001 | Minecraft; MC; 我的世界; Java Edition; JE; Bedrock Edition; BE | Java 版、基岩版互通 | 区分不同游戏实现、协议与内容生态 | 不将 Java 模组 API 套到基岩版附加包 |
| MC002 | Vanilla; 原版; Modded | 原版能否实现、需不需要装模组 | 区分基础游戏能力与扩展运行环境 | 服务端扩展与客户端是否需安装要分别判断 |
| MC003 | Mod; 模组; Mod loader | 增加方块、修改游戏内部 | 通过加载器及相关 API 扩展游戏 | 模组不同于服务端插件或资源包 |
| MC004 | Fabric; Fabric Loader; Fabric API; Loom | Fabric 开发环境、缺依赖 | 分别识别生态、加载器、API 集与开发构建插件 | Fabric API 不是 Loader 自带的同一个组件 |
| MC005 | Forge; NeoForge; Event bus; Mod lifecycle | Forge 和 NeoForge、注册事件 | 加载器及其 API 提供扩展和生命周期机制 | 二者不能假定二进制或源码无差别兼容 |
| MC006 | Quilt; Multi-loader; Common module | 多加载器兼容、共用代码 | 识别另一加载器生态或跨加载器组织方式 | 兼容矩阵依具体版本，不保证一次编写随处运行 |
| MC007 | Plugin; Bukkit; Spigot; Paper | 服务器插件、玩家不装客户端 | 在对应服务器 API 上扩展服务端功能 | 不能据此保证新增任意客户端代码/注册内容 |
| MC008 | Folia; Region scheduler | 区域线程、Paper 插件线程错误 | 区分区域调度与传统主线程模型（S28） | 不将普通 Bukkit 同步任务规则直接套用 |
| MC009 | Add-on; Behavior pack; Resource pack | 基岩版行为包、附加包 | 在基岩版内容体系中组合行为与资源扩展 | 不等同 Java Edition 的 Mod JAR |
| MC010 | Modpack; 整合包; Config | 一整套模组、配置冲突 | 组合依赖、配置、资源与游戏体验 | 包能启动不代表全部模组相互兼容 |
| MC011 | Dedicated server; Integrated server; 单人内置服务器 | 单人正常服务器崩 | 区分独立服务器进程与客户端内运行的服务器 | 单人也有逻辑服务端，需独立服务端测试 |
| MC012 | Physical side; Logical side; Client/Server | 客户端类在服务端报错、执行两次 | 物理侧描述程序环境，逻辑侧描述职责（S27） | 判断逻辑侧不等于确认客户端类可加载 |
| MC013 | Tick; TPS; MSPT; Game tick | TPS 低、服务器一顿一顿 | 区分模拟步进率与每步处理耗时 | 与显示 FPS、网络延迟分开；时间换算要考虑实际 Tick 速率 |
| MC014 | Random tick; Scheduled tick; Redstone tick | 作物生长、方块延迟、红石计时 | 随机更新、预约更新与红石时间表达解决不同问题 | 不将它们都当任意对象每 Tick 执行 |
| MC015 | Chunk; 区块; Section; Region file | 区块加载、分区存档 | 区分世界空间分块、垂直分段和磁盘组织 | 渲染、加载、保存与模拟不是同一状态 |
| MC016 | Chunk ticket; Force loading; Simulation/View distance | 远处机器停了、强加载 | 控制区块保持加载或模拟的条件与范围 | 加载并不总表示实体和所有逻辑都在 Tick |
| MC017 | Dimension; Level; World | 主世界、下界、末地、维度 | 区分游戏维度及管理世界状态的上下文 | 类名受映射影响；World 也可能指整套存档 |
| MC018 | Biome; Noise; Worldgen; 世界生成 | 生物群系、地形噪声 | 通过环境分类及生成算法组织世界 | 地形规则、群系分布和装饰生成不是同一层 |
| MC019 | Feature; Placed/Configured feature; Structure | 矿物生成、地物、建筑结构 | 定义可配置生成内容及其放置约束 | 注册方式及数据格式高度依赖版本 |
| MC020 | Seed; 世界种子 | 同种子地图不同、复现世界 | 作为生成随机过程的输入 | 游戏版本、配置、模组和生成次序都可能影响结果 |
| MC021 | Block; BlockState; Property | 方块朝向、开关状态 | Block 表达类型，BlockState 表达有限属性组合 | 不为任意大数据或无限数值制造状态组合 |
| MC022 | BlockEntity; TileEntity; 方块实体 | 机器存电、容器数据 | 给特定方块位置附加实例数据和可选逻辑 | 不是可移动 Entity；静态方块不都需要方块实体 |
| MC023 | Item; ItemStack; 物品堆 | 物品数量、自定义物品数据 | 区分物品类型与具体数量/数据实例 | 修改共享类型字段不等于修改某个堆 |
| MC024 | Entity; EntityType; Mob | 实体、生物、自定义怪 | 区分世界中实例及注册类型 | BlockEntity 与 Entity 不属于同一种实例系统 |
| MC025 | NBT; Named Binary Tag; SNBT | NBT 数据、可读标签串 | 用树状带类型数据及其文本表达保存/表达内容 | 命令和物品持久化接口会随版本变化 |
| MC026 | Data component; 物品数据组件 | 新版本物品数据、组件补丁 | 用类型化组件描述物品堆附加信息 | 不将所有新旧 NBT 写法混用；版本范围必须确认 |
| MC027 | Data Pack; 数据包; pack.mcmeta; Pack format | 不写 Java 添加配方、游戏数据 | 以目标版本支持的数据资源扩展服务器逻辑/内容 | 不是可以执行任意 JVM 代码的模组 |
| MC028 | Resource Pack; 资源包; assets | 改贴图、声音、模型外观 | 在客户端资源体系中覆盖或增加可解析资产 | 改外观不自动改变碰撞、注册或服务器规则 |
| MC029 | Namespace; Resource identifier; Identifier; ResourceLocation | 资源 ID、命名空间冒号 | 使用限定标识区分不同来源的资源 | 标识符语法及类名按版本映射确认 |
| MC030 | Registry; 注册表; Registry key; Holder | 注册物品方块、动态内容引用 | 将稳定标识关联到类型或数据条目 | 静态/动态注册表生命周期和访问方式不同 |
| MC031 | Tag; 标签; TagKey | 一组物品、所有木板、类型分类 | 以数据驱动的标识集合表达成员关系 | 不是 HTML 标签、NBT tag 或 Git 标签 |
| MC032 | Recipe; Ingredient; Recipe type/serializer | 自定义合成、机器配方 | 区分输入匹配、配方行为及数据编解码 | 客户端配方展示不等于服务端执行校验 |
| MC033 | Loot table; Predicate; Item modifier | 掉落表、条件掉落 | 数据化组合生成物品和条件/修改操作 | 不把战利品随机当成无条件或固定结果 |
| MC034 | Advancement; Criteria; Trigger | 进度、成就条件 | 表达按条件完成的游戏进度逻辑 | Java/基岩成就体系和命名不能任意互换 |
| MC035 | Function; mcfunction; Command block; execute | 命令函数、执行上下文 | 组合命令并控制执行者、位置和维度等上下文 | function 不是 JVM 或 JS 函数，权限语义独立 |
| MC036 | Selector; Scoreboard; Team; Gamerule | 选择玩家、记分板、游戏规则 | 分别筛选对象、记录分值、组织队伍或调整规则 | 同名规则和命令支持范围依版本/版本生态核对 |
| MC037 | Redstone; 红石; Comparator; Repeater; Quasi-connectivity | 红石电路、比较器、中继器、准连接 | 区分信号传递、比较/延迟和特定更新行为 | Java 与基岩机制不必一致，不能只凭外观推断 |
| MC038 | Mob spawning; Mob cap; Spawn rules | 刷怪塔效率、怪不生成 | 由生成条件、数量约束与加载情境共同决定 | 不把全局/局部限制简化成单一常数 |
| MC039 | Datagen; Data generation | 自动生成配方模型标签 | 以开发期工具产生资源/数据文件 | 生成产物不等于运行时注册已完成 |
| MC040 | Mapping; Mojang mappings; Yarn; Remapping | 教程类名不同、映射转换 | 在命名空间间关联类、字段和方法 | 映射转换不自动修复游戏版本的行为/API 变化 |
| MC041 | Mixin; Injection; Inject; At | 注入原版方法、修改字节码 | 对目标类按选择器和注入点应用变换 | 优先现有事件/扩展 API，注入点需验证版本及冲突 |
| MC042 | Redirect; ModifyArg; ModifyVariable; Accessor; Invoker | 替换调用、访问私有字段 | 不同注入/桥接机制各有作用边界 | 不随意以侵入性替换覆盖其他模组行为 |
| MC043 | Access widener; Access transformer | 访问级别阻碍扩展 | 在目标工具链支持下调整访问约束 | 机制及配置格式因加载器不同，不等同 Mixin |
| MC044 | Event; Callback; Hook; Subscription | 监听玩家动作、事件回调 | 在公开扩展点添加行为 | 事件派发侧、线程、取消及生命周期必须核对 |
| MC045 | Codec; MapCodec; StreamCodec | 数据编解码、包序列化 | 区分数据结构编解码和网络流编解码职责 | 类名及可用 API 依版本；Codec 不只是视频编码器 |
| MC046 | Packet; Payload; C2S; S2C; Custom networking | 发包、双端同步、客户端请求 | 按方向与协议把意图或状态传至另一端 | 不信任客户端声明，验证权限、距离及数据规模 |
| MC047 | Main/Server thread; Render thread; Enqueue work | 异步改世界崩溃、线程切换 | 按运行环境将状态操作交给拥有者线程/调度器 | 包回调线程不是普遍固定规则；Folia 需独立判定 |
| MC048 | Synchronization; Dirty marking; Persistence | 重进数据丢、客户端不更新 | 区分保存变更、网络同步及客户端展示更新 | 标记脏数据不等同立即发包或重绘 |
| MC049 | Menu/ScreenHandler; Container; Screen | 机器 GUI、物品槽不同步 | 区分容器交互逻辑与客户端绘制界面 | 屏幕输入需服务端验证，类名随映射不同 |
| MC050 | Capability; Attachment; Transfer API | 物品能量流体接口、附加实体数据 | 识别生态特定扩展与数据能力机制 | 不是跨加载器通用的一套名称/API |
| MC051 | SavedData; Persistent state; Server data | 全世界共享数据、存档级状态 | 按世界/服务器生命周期保存自定义内容 | 不直接依赖静态全局变量跨世界持久化 |
| MC052 | Block model; Blockstate JSON; Baked model | 方块模型状态、紫黑贴图 | 将模型资源与状态选择、纹理引用联系起来 | 数据格式、模型加载和烘焙机制可能随版本调整 |
| MC053 | Renderer; Render layer/type/pipeline; Buffer | 自定义渲染、透明排序 | 组织目标版本的绘制入口、管线状态和顶点数据 | 不将旧教程渲染 API 与新版本直接混用 |
| MC054 | PoseStack; MatrixStack; Transform stack | 模型旋转位移叠错、矩阵栈 | 用嵌套变换隔离局部坐标操作 | push/pop 配对，坐标空间和版本命名要一致 |
| MC055 | Particle type; Particle provider/factory; 粒子 | 注册粒子、特效不显示 | 区分类型/参数与客户端实例构造及绘制 | 粒子展示通常不应承担权威伤害判定 |
| MC056 | Frustum; AABB; VoxelShape | 提前消失、碰撞箱与轮廓 | 分别关注可见性测试、包围盒和体素形状 | 绘制范围、碰撞形状与交互选框用途不同 |
| MC057 | Shader pack; Iris; Sodium; Rendering compatibility | 光影冲突、渲染优化模组 | 识别生态渲染扩展和兼容环境 | 不把它们看作原版统一 API，核对具体版本与桥接 |
| MC058 | Crash report; latest.log; Stack trace; Mixin apply error | 启动崩溃、注入失败、缺类 | 从根因、依赖环境及加载阶段定位问题 | 最后一个提到的模组不一定是根因 |
| MC059 | Tick profiling; Spark; Heap/Thread dump | 哪个模组卡服、内存涨 | 结合采样、Tick 归因和运行时快照诊断 | 工具结果需结合场景，不用总内存大小直接判泄露 |
| MC060 | Data migration; DataFixer; Save compatibility | 更新后旧存档坏了 | 管理持久化结构及资源 ID 的演进 | 备份后验证迁移；移除模组或改 ID 可损害已有世界 |
