# 游戏开发概念

检索分组：玩法与系统、运行与物理、AI、联机、渲染、内容制作。
相邻领域：[美术](art.md)、[建模](modeling.md)、[后端](backend.md)。来源入口：S04、S13、S14，见 [sources.md](sources.md)。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| GM001 | 核心循环 Core loop; Meta loop | 玩什么、为什么再玩一次 | 定义反复执行的行动反馈与局外成长 | 功能列表不等于可玩的循环 |
| GM002 | 机制 Mechanics; 动态 Dynamics; 体验 Aesthetics; MDA | 规则怎样形成体验 | 区分规则、运行时行为与玩家感受 | 此处 aesthetics 不只指画面美术 |
| GM003 | 游戏感 Game feel; Juice; 打击感 | 手感软、打击没力 | 用操作响应、视听反馈等表达行动结果 | 更多抖动或特效不一定更好 |
| GM004 | 输入缓冲 Input buffer; Coyote time | 按跳没反应、离边缘还能跳 | 容忍短暂输入时机偏差 | 需明确窗口，不等于任意放宽规则 |
| GM005 | 反馈循环 Feedback loop; 正/负反馈 | 越赢越强、追赶机制 | 强化或抑制系统差异 | 正负描述系统方向，不等于好坏 |
| GM006 | 资源源汇 Sources/Sinks; 经济平衡 | 金币泛滥、材料没用 | 设计资源产生、消耗与循环 | 不只调整单一价格 |
| GM007 | 成长曲线 Progression; 难度曲线 | 后期无聊、前期太难 | 协调能力、挑战与解锁节奏 | 区分玩家技巧与数值成长 |
| GM008 | 随机 RNG; 种子 Seed; 洗牌袋 Shuffle bag | 随机可复现、避免连续不出 | 管理随机序列及感知分布 | 固定种子不保证跨版本完全一致 |
| GM009 | 程序化生成 PCG; 约束生成 | 随机关卡、无限地图 | 用规则组合内容并满足可玩约束 | 随机摆放不等于有效生成 |
| GM010 | 关卡节奏 Pacing; 引导 Signposting | 不知道去哪、战斗太密 | 组织挑战、休息、视线和导航线索 | 不用箭头替代所有空间设计 |
| GM011 | 灰盒 Graybox; Blockout; 垂直切片 Vertical slice | 先验证玩法、一小段完整体验 | 灰盒验证空间；切片验证完整制作链路 | 两者验证目标不同 |
| GM012 | 实体组件 ECS; Entity/Component/System | 大量单位、数据驱动 | 按身份、数据和处理系统组织行为 | 普通组件组合不必就是 ECS |
| GM013 | 场景图 Scene graph; Prefab; Resource | 层级对象、可复用实体 | 管理对象关系、模板与共享资源 | 不同引擎概念映射需查文档 |
| GM014 | 游戏循环 Game loop; Delta time; 固定步长 | 帧率变化速度不同 | 区分模拟推进与画面更新 | 变量步长不适合所有稳定性要求 |
| GM015 | 帧时间 Frame time; FPS; Frame pacing | 卡顿、平均帧率很高仍不顺 | 测量每帧耗时和交付均匀性 | 平均 FPS 会掩盖尖峰 |
| GM016 | 对象池 Object pool; 生命周期 | 子弹频繁创建销毁 | 复用对象减少分配或初始化成本 | 回收时必须重置状态并解除引用 |
| GM017 | 碰撞体 Collider; 刚体 Rigidbody; Trigger | 穿墙、区域触发、掉落 | 碰撞形状、动力学主体及检测区域 | 可见网格不等于物理形状 |
| GM018 | Broad phase; Narrow phase | 大量物体碰撞慢 | 先筛候选对再精确检测 | 与物理约束求解分开 |
| GM019 | 离散/连续碰撞 CCD; Swept test | 高速子弹穿透 | 沿运动轨迹检测以减少漏碰撞 | 有性能与引擎支持限制 |
| GM020 | 射线 Raycast; Shape cast; Hitbox/Hurtbox | 点选、攻击判定 | 查询空间交点或区分攻击与受击体积 | 命中查询不自动产生物理响应 |
| GM021 | 空间分区 Spatial partition; Quadtree; Octree | 附近查询、海量对象 | 按空间组织检索候选 | 结构应匹配维度和移动频率 |
| GM022 | A*; 寻路 Pathfinding; NavMesh | NPC 绕墙找路 | 在图或可导航表面上搜索路径 | 寻路与局部避障不同 |
| GM023 | Steering; Local avoidance | 群体移动、不要挤一起 | 对运动方向进行局部控制 | 不能替代全局路径可达性 |
| GM024 | FSM; 行为树 Behavior tree; Utility AI; GOAP | 敌人决策、巡逻追击 | 以状态、树、评分或目标规划表达决策 | 依复杂度选择，不是必须叠加 |
| GM025 | Blackboard; 感知 Perception | AI 共享目标、看见听见 | 保存决策上下文并提取环境信息 | 记忆状态需过期及归属规则 |
| GM026 | 动画状态机; Blend tree; Root motion | 跑走切换、脚滑 | 混合动画并确定运动由动画或代码驱动 | 根运动与网络/物理控制需协调 |
| GM027 | 相机跟随; Dead zone; Damping; Shake | 镜头晕、跟随生硬 | 管理取景目标、延迟与反馈 | 区分镜头反馈和改变瞄准/模拟 |
| GM028 | HUD; Diegetic UI; 世界空间 UI | 血条、头顶名字、沉浸界面 | 定义信息呈现空间及是否属于游戏世界 | 可读性与遮挡仍要验证 |
| GM029 | 存档 Save; 序列化 Serialization; 版本迁移 | 保存进度、旧存档打不开 | 将必要状态持久化并支持演进 | 不直接持久化临时运行对象引用 |
| GM030 | 权威服务器 Server authoritative | 防作弊、联机谁说了算 | 由服务器验证并裁定关键游戏状态 | 不等于完全消除作弊或延迟 |
| GM031 | 状态同步 Snapshot; Delta compression | 联机位置、带宽太大 | 发送状态快照或相对变更 | 需考虑丢包、基线和序号 |
| GM032 | 插值 Interpolation; 外推 Extrapolation | 远端人物抖动 | 在已知样本间平滑或预测未来 | 插值引入展示延迟，外推可能猜错 |
| GM033 | 客户端预测 Prediction; Reconciliation | 自己移动延迟大 | 本地先模拟，再与权威结果校正 | 输入编号和重放一致性关键 |
| GM034 | 延迟补偿 Lag compensation | 明明瞄准却没打中 | 按策略回溯或补偿网络延迟影响 | 有公平性与滥用边界，不无限回溯 |
| GM035 | 锁步 Lockstep; 确定性 Determinism | RTS 同步、相同输入相同结果 | 各端按输入序列推进一致模拟 | 浮点、线程、随机和版本都影响确定性 |
| GM036 | 回滚网络 Rollback netcode | 格斗联机、预测错误修正 | 预测远端输入并回退重模拟 | 模拟必须能保存恢复，副作用需隔离 |
| GM037 | Tick rate; 更新率; 网络延迟 Latency | 服务器几赫兹、响应慢 | 区分模拟频率、发送频率和传输耗时 | 与显示帧率并非同一指标 |
| GM038 | Interest management; AOI | 只同步附近玩家 | 按关注范围减少状态分发 | 隐藏客户端可见性不等于安全隔离 |
| GM039 | Matchmaking; Lobby; Session | 匹配对手、房间 | 分别处理分组、准备与实际对局 | 匹配质量、等待时间和延迟有权衡 |
| GM040 | Draw call; Batching; Instancing | 绘制调用多、同类物体很多 | 合并提交或复用几何进行实例绘制 | 不自动降低像素着色或透明开销 |
| GM041 | Frustum/Occlusion culling; LOD | 看不见也在渲染、远处降模 | 跳过不可见对象或降低远处细节 | 与简化碰撞、停止逻辑更新不同 |
| GM042 | Overdraw; Fill rate; GPU bound/CPU bound | 粒子多就卡、瓶颈在哪 | 区分像素重复绘制及处理器耗时 | 先测量，减面数不一定解决透明过绘 |
| GM043 | Forward/Deferred rendering | 灯光很多、渲染路径 | 组织几何、材质与光照计算顺序 | 内存、透明、抗锯齿及平台限制各异 |
| GM044 | PBR; BRDF; Shader | 材质真实、着色器效果 | 描述材质光响应并用程序计算外观 | PBR 不是具体美术风格 |
| GM045 | Shadow map; Bias; Cascade | 阴影痤疮、漂浮、远处锯齿 | 通过深度贴图及分区表达阴影 | 偏移过大会产生脱离表面的阴影 |
| GM046 | SSAO; SSR; GI; Ray tracing | 接触阴影、反射、间接光 | 多类可见性与光传播技术 | 屏幕空间方法缺失屏幕外信息；SSR 在此是反射 |
| GM047 | Anti-aliasing; MSAA; TAA; Upscaling | 边缘锯齿、拖影、低分辨率提速 | 平滑采样或重建更高分辨率图像 | 不同方案有清晰度、时序与性能取舍 |
| GM048 | HDR; Tone mapping; Bloom | 高亮、曝光、泛光 | 表示高动态范围并映射显示及镜头效果 | Bloom 不是 HDR 本身 |
| GM049 | 粒子系统 Particle system; VFX | 火焰、烟雾、爆炸 | 用大量简化元素描述动态视觉 | 透明排序、过绘和池化都可能是约束 |
| GM050 | 音频总线 Bus; Spatial audio; Ducking | 音量分组、方位声、说话压背景 | 组织混音、空间定位及动态衰减 | 声音优先级和重复触发需要控制 |
| GM051 | 资源流式加载 Streaming; Asset bundle | 大世界、切场景卡顿 | 按需加载和卸载内容 | 异步磁盘加载仍可能有主线程整合成本 |
| GM052 | Profiler; Memory budget; GC | 内存涨、周期卡顿 | 量化 CPU/GPU/内存分配及回收成本 | 优化前后在目标设备验证 |
