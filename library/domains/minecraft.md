# Minecraft / 我的世界

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [MC001 · Minecraft; MC; 我的世界; Java Edition; JE; Bedrock Edition; BE](../concepts/MC001.md) | Java 版、基岩版互通 |
| [MC002 · Vanilla; 原版; Modded](../concepts/MC002.md) | 原版能否实现、需不需要装模组 |
| [MC003 · Mod; 模组; Mod loader](../concepts/MC003.md) | 增加方块、修改游戏内部 |
| [MC004 · Fabric; Fabric Loader; Fabric API; Loom](../concepts/MC004.md) | Fabric 开发环境、缺依赖 |
| [MC005 · Forge; NeoForge; Event bus; Mod lifecycle](../concepts/MC005.md) | Forge 和 NeoForge、注册事件 |
| [MC006 · Quilt; Multi-loader; Common module](../concepts/MC006.md) | 多加载器兼容、共用代码 |
| [MC007 · Plugin; Bukkit; Spigot; Paper](../concepts/MC007.md) | 服务器插件、玩家不装客户端 |
| [MC008 · Folia; Region scheduler](../concepts/MC008.md) | 区域线程、Paper 插件线程错误 |
| [MC009 · Add-on; Behavior pack; Resource pack](../concepts/MC009.md) | 基岩版行为包、附加包 |
| [MC010 · Modpack; 整合包; Config](../concepts/MC010.md) | 一整套模组、配置冲突 |
| [MC011 · Dedicated server; Integrated server; 单人内置服务器](../concepts/MC011.md) | 单人正常服务器崩 |
| [MC012 · Physical side; Logical side; Client/Server](../concepts/MC012.md) | 客户端类在服务端报错、执行两次 |
| [MC013 · Tick; TPS; MSPT; Game tick](../concepts/MC013.md) | TPS 低、服务器一顿一顿 |
| [MC014 · Random tick; Scheduled tick; Redstone tick](../concepts/MC014.md) | 作物生长、方块延迟、红石计时 |
| [MC015 · Chunk; 区块; Section; Region file](../concepts/MC015.md) | 区块加载、分区存档 |
| [MC016 · Chunk ticket; Force loading; Simulation/View distance](../concepts/MC016.md) | 远处机器停了、强加载 |
| [MC017 · Dimension; Level; World](../concepts/MC017.md) | 主世界、下界、末地、维度 |
| [MC018 · Biome; Noise; Worldgen; 世界生成](../concepts/MC018.md) | 生物群系、地形噪声 |
| [MC019 · Feature; Placed/Configured feature; Structure](../concepts/MC019.md) | 矿物生成、地物、建筑结构 |
| [MC020 · Seed; 世界种子](../concepts/MC020.md) | 同种子地图不同、复现世界 |
| [MC021 · Block; BlockState; Property](../concepts/MC021.md) | 方块朝向、开关状态 |
| [MC022 · BlockEntity; TileEntity; 方块实体](../concepts/MC022.md) | 机器存电、容器数据 |
| [MC023 · Item; ItemStack; 物品堆](../concepts/MC023.md) | 物品数量、自定义物品数据 |
| [MC024 · Entity; EntityType; Mob](../concepts/MC024.md) | 实体、生物、自定义怪 |
| [MC025 · NBT; Named Binary Tag; SNBT](../concepts/MC025.md) | NBT 数据、可读标签串 |
| [MC026 · Data component; 物品数据组件](../concepts/MC026.md) | 新版本物品数据、组件补丁 |
| [MC027 · Data Pack; 数据包; pack.mcmeta; Pack format](../concepts/MC027.md) | 不写 Java 添加配方、游戏数据 |
| [MC028 · Resource Pack; 资源包; assets](../concepts/MC028.md) | 改贴图、声音、模型外观 |
| [MC029 · Namespace; Resource identifier; Identifier; ResourceLocation](../concepts/MC029.md) | 资源 ID、命名空间冒号 |
| [MC030 · Registry; 注册表; Registry key; Holder](../concepts/MC030.md) | 注册物品方块、动态内容引用 |
| [MC031 · Tag; 标签; TagKey](../concepts/MC031.md) | 一组物品、所有木板、类型分类 |
| [MC032 · Recipe; Ingredient; Recipe type/serializer](../concepts/MC032.md) | 自定义合成、机器配方 |
| [MC033 · Loot table; Predicate; Item modifier](../concepts/MC033.md) | 掉落表、条件掉落 |
| [MC034 · Advancement; Criteria; Trigger](../concepts/MC034.md) | 进度、成就条件 |
| [MC035 · Function; mcfunction; Command block; execute](../concepts/MC035.md) | 命令函数、执行上下文 |
| [MC036 · Selector; Scoreboard; Team; Gamerule](../concepts/MC036.md) | 选择玩家、记分板、游戏规则 |
| [MC037 · Redstone; 红石; Comparator; Repeater; Quasi-connectivity](../concepts/MC037.md) | 红石电路、比较器、中继器、准连接 |
| [MC038 · Mob spawning; Mob cap; Spawn rules](../concepts/MC038.md) | 刷怪塔效率、怪不生成 |
| [MC039 · Datagen; Data generation](../concepts/MC039.md) | 自动生成配方模型标签 |
| [MC040 · Mapping; Mojang mappings; Yarn; Remapping](../concepts/MC040.md) | 教程类名不同、映射转换 |
| [MC041 · Mixin; Injection; Inject; At](../concepts/MC041.md) | 注入原版方法、修改字节码 |
| [MC042 · Redirect; ModifyArg; ModifyVariable; Accessor; Invoker](../concepts/MC042.md) | 替换调用、访问私有字段 |
| [MC043 · Access widener; Access transformer](../concepts/MC043.md) | 访问级别阻碍扩展 |
| [MC044 · Event; Callback; Hook; Subscription](../concepts/MC044.md) | 监听玩家动作、事件回调 |
| [MC045 · Codec; MapCodec; StreamCodec](../concepts/MC045.md) | 数据编解码、包序列化 |
| [MC046 · Packet; Payload; C2S; S2C; Custom networking](../concepts/MC046.md) | 发包、双端同步、客户端请求 |
| [MC047 · Main/Server thread; Render thread; Enqueue work](../concepts/MC047.md) | 异步改世界崩溃、线程切换 |
| [MC048 · Synchronization; Dirty marking; Persistence](../concepts/MC048.md) | 重进数据丢、客户端不更新 |
| [MC049 · Menu/ScreenHandler; Container; Screen](../concepts/MC049.md) | 机器 GUI、物品槽不同步 |
| [MC050 · Capability; Attachment; Transfer API](../concepts/MC050.md) | 物品能量流体接口、附加实体数据 |
| [MC051 · SavedData; Persistent state; Server data](../concepts/MC051.md) | 全世界共享数据、存档级状态 |
| [MC052 · Block model; Blockstate JSON; Baked model](../concepts/MC052.md) | 方块模型状态、紫黑贴图 |
| [MC053 · Renderer; Render layer/type/pipeline; Buffer](../concepts/MC053.md) | 自定义渲染、透明排序 |
| [MC054 · PoseStack; MatrixStack; Transform stack](../concepts/MC054.md) | 模型旋转位移叠错、矩阵栈 |
| [MC055 · Particle type; Particle provider/factory; 粒子](../concepts/MC055.md) | 注册粒子、特效不显示 |
| [MC056 · Frustum; AABB; VoxelShape](../concepts/MC056.md) | 提前消失、碰撞箱与轮廓 |
| [MC057 · Shader pack; Iris; Sodium; Rendering compatibility](../concepts/MC057.md) | 光影冲突、渲染优化模组 |
| [MC058 · Crash report; latest.log; Stack trace; Mixin apply error](../concepts/MC058.md) | 启动崩溃、注入失败、缺类 |
| [MC059 · Tick profiling; Spark; Heap/Thread dump](../concepts/MC059.md) | 哪个模组卡服、内存涨 |
| [MC060 · Data migration; DataFixer; Save compatibility](../concepts/MC060.md) | 更新后旧存档坏了 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 Minecraft 领域基线，先辨明玩法、资源、数据、插件或模组，再将相关概念映射到实际环境与生命周期。

### 关键特征

- 版本、平台、加载方式和运行侧是实现前提，不能跨环境套用符号或行为。
- 游戏状态的权威来源与客户端表现分离，按现有同步路径传递必要状态。
- 沿项目已有注册、资源与生命周期机制扩展，不因概念命中擅自增加注入或兼容层。

### 如何落实

- 从项目依赖和任务确认内容类型；实际模组开发遵循对应专门规范，再核对版本、加载器与映射。
- 将功能落到现有入口和状态拥有者，明确注册时机、世界上下文及逻辑侧和物理侧限制。
- 若涉及持久化或同步，列出保存字段、发送方向、接收校验和实体或区块失效时的处理。
- 仅使用本地依赖或已核对资料中的接口，按实际入口安排资源重载、世界退出或服务端停止清理。

### 如何验收

- 在任务要求的实际运行环境中触发功能，涉及服务端兼容时核对无客户端专属引用误加载。
- 按相关生命周期执行世界重进、区块卸载或资源重载，核对状态与资源没有残留。
- 若功能涉及保存或多人同步，对比重启前后及两端状态，并验证非法或过期输入的处理。

### 常见误用

- 从相似版本示例直接复制 API、注册顺序或映射名称而不核对。
- 在客户端修改权威游戏状态，或无需求地用注入替代现有扩展入口。
