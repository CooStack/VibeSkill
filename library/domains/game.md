# 游戏开发

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [GM001 · 核心循环 Core loop; Meta loop](../concepts/GM001.md) | 玩什么、为什么再玩一次 |
| [GM002 · 机制 Mechanics; 动态 Dynamics; 体验 Aesthetics; MDA](../concepts/GM002.md) | 规则怎样形成体验 |
| [GM003 · 游戏感 Game feel; Juice; 打击感](../concepts/GM003.md) | 手感软、打击没力 |
| [GM004 · 输入缓冲 Input buffer; Coyote time](../concepts/GM004.md) | 按跳没反应、离边缘还能跳 |
| [GM005 · 反馈循环 Feedback loop; 正/负反馈](../concepts/GM005.md) | 越赢越强、追赶机制 |
| [GM006 · 资源源汇 Sources/Sinks; 经济平衡](../concepts/GM006.md) | 金币泛滥、材料没用 |
| [GM007 · 成长曲线 Progression; 难度曲线](../concepts/GM007.md) | 后期无聊、前期太难 |
| [GM008 · 随机 RNG; 种子 Seed; 洗牌袋 Shuffle bag](../concepts/GM008.md) | 随机可复现、避免连续不出 |
| [GM009 · 程序化生成 PCG; 约束生成](../concepts/GM009.md) | 随机关卡、无限地图 |
| [GM010 · 关卡节奏 Pacing; 引导 Signposting](../concepts/GM010.md) | 不知道去哪、战斗太密 |
| [GM011 · 灰盒 Graybox; Blockout; 垂直切片 Vertical slice](../concepts/GM011.md) | 先验证玩法、一小段完整体验 |
| [GM012 · 实体组件 ECS; Entity/Component/System](../concepts/GM012.md) | 大量单位、数据驱动 |
| [GM013 · 场景图 Scene graph; Prefab; Resource](../concepts/GM013.md) | 层级对象、可复用实体 |
| [GM014 · 游戏循环 Game loop; Delta time; 固定步长](../concepts/GM014.md) | 帧率变化速度不同 |
| [GM015 · 帧时间 Frame time; FPS; Frame pacing](../concepts/GM015.md) | 卡顿、平均帧率很高仍不顺 |
| [GM016 · 对象池 Object pool; 生命周期](../concepts/GM016.md) | 子弹频繁创建销毁 |
| [GM017 · 碰撞体 Collider; 刚体 Rigidbody; Trigger](../concepts/GM017.md) | 穿墙、区域触发、掉落 |
| [GM018 · Broad phase; Narrow phase](../concepts/GM018.md) | 大量物体碰撞慢 |
| [GM019 · 离散/连续碰撞 CCD; Swept test](../concepts/GM019.md) | 高速子弹穿透 |
| [GM020 · 射线 Raycast; Shape cast; Hitbox/Hurtbox](../concepts/GM020.md) | 点选、攻击判定 |
| [GM021 · 空间分区 Spatial partition; Quadtree; Octree](../concepts/GM021.md) | 附近查询、海量对象 |
| [GM022 · A*; 寻路 Pathfinding; NavMesh](../concepts/GM022.md) | NPC 绕墙找路 |
| [GM023 · Steering; Local avoidance](../concepts/GM023.md) | 群体移动、不要挤一起 |
| [GM024 · FSM; 行为树 Behavior tree; Utility AI; GOAP](../concepts/GM024.md) | 敌人决策、巡逻追击 |
| [GM025 · Blackboard; 感知 Perception](../concepts/GM025.md) | AI 共享目标、看见听见 |
| [GM026 · 动画状态机; Blend tree; Root motion](../concepts/GM026.md) | 跑走切换、脚滑 |
| [GM027 · 相机跟随; Dead zone; Damping; Shake](../concepts/GM027.md) | 镜头晕、跟随生硬 |
| [GM028 · HUD; Diegetic UI; 世界空间 UI](../concepts/GM028.md) | 血条、头顶名字、沉浸界面 |
| [GM029 · 存档 Save; 序列化 Serialization; 版本迁移](../concepts/GM029.md) | 保存进度、旧存档打不开 |
| [GM030 · 权威服务器 Server authoritative](../concepts/GM030.md) | 防作弊、联机谁说了算 |
| [GM031 · 状态同步 Snapshot; Delta compression](../concepts/GM031.md) | 联机位置、带宽太大 |
| [GM032 · 插值 Interpolation; 外推 Extrapolation](../concepts/GM032.md) | 远端人物抖动 |
| [GM033 · 客户端预测 Prediction; Reconciliation](../concepts/GM033.md) | 自己移动延迟大 |
| [GM034 · 延迟补偿 Lag compensation](../concepts/GM034.md) | 明明瞄准却没打中 |
| [GM035 · 锁步 Lockstep; 确定性 Determinism](../concepts/GM035.md) | RTS 同步、相同输入相同结果 |
| [GM036 · 回滚网络 Rollback netcode](../concepts/GM036.md) | 格斗联机、预测错误修正 |
| [GM037 · Tick rate; 更新率; 网络延迟 Latency](../concepts/GM037.md) | 服务器几赫兹、响应慢 |
| [GM038 · Interest management; AOI](../concepts/GM038.md) | 只同步附近玩家 |
| [GM039 · Matchmaking; Lobby; Session](../concepts/GM039.md) | 匹配对手、房间 |
| [GM040 · Draw call; Batching; Instancing](../concepts/GM040.md) | 绘制调用多、同类物体很多 |
| [GM041 · Frustum/Occlusion culling; LOD](../concepts/GM041.md) | 看不见也在渲染、远处降模 |
| [GM042 · Overdraw; Fill rate; GPU bound/CPU bound](../concepts/GM042.md) | 粒子多就卡、瓶颈在哪 |
| [GM043 · Forward/Deferred rendering](../concepts/GM043.md) | 灯光很多、渲染路径 |
| [GM044 · PBR; BRDF; Shader](../concepts/GM044.md) | 材质真实、着色器效果 |
| [GM045 · Shadow map; Bias; Cascade](../concepts/GM045.md) | 阴影痤疮、漂浮、远处锯齿 |
| [GM046 · SSAO; SSR; GI; Ray tracing](../concepts/GM046.md) | 接触阴影、反射、间接光 |
| [GM047 · Anti-aliasing; MSAA; TAA; Upscaling](../concepts/GM047.md) | 边缘锯齿、拖影、低分辨率提速 |
| [GM048 · HDR; Tone mapping; Bloom](../concepts/GM048.md) | 高亮、曝光、泛光 |
| [GM049 · 粒子系统 Particle system; VFX](../concepts/GM049.md) | 火焰、烟雾、爆炸 |
| [GM050 · 音频总线 Bus; Spatial audio; Ducking](../concepts/GM050.md) | 音量分组、方位声、说话压背景 |
| [GM051 · 资源流式加载 Streaming; Asset bundle](../concepts/GM051.md) | 大世界、切场景卡顿 |
| [GM052 · Profiler; Memory budget; GC](../concepts/GM052.md) | 内存涨、周期卡顿 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为游戏领域基线，将玩法概念落实为规则、模拟状态和玩家反馈，沿用项目已有引擎与运行模型。

### 关键特征

- 先明确玩法规则与胜负或完成条件，再选择表现和实现机制。
- 区分模拟时间、渲染时间和输入采样，时间单位与状态更新责任保持一致。
- 联机、存档和程序化生成仅在需求涉及时纳入，不因游戏领域命中而自动增加。

### 如何落实

- 把一次核心玩法循环写成输入、合法动作、状态变化及反馈，明确暂停、失败和重开入口。
- 将规则状态放入现有模拟层，通过既有碰撞或规则设施处理约束，表现读取明确的模拟结果。
- 为对象生成、回收和场景切换安排生命周期，避免重开后残留计时器、实体或输入监听。
- 按涉及的功能界定随机种子、存档内容或联机权威；记录可复现的输入序列用于比较行为。

### 如何验收

- 执行完整玩法循环与失败重开，核对规则结果、计分和反馈一致。
- 改变渲染帧率或引入帧间抖动，核对移动、计时及碰撞在约定容差内保持规则一致。
- 反复进入退出场景，核对实体数量、输入响应和资源占用不会因残留持续增长。

### 常见误用

- 把每帧常量当作每秒速度，导致玩法随帧率变化。
- 先增加视觉效果或联机结构，再发现核心动作与状态规则尚未定义。
