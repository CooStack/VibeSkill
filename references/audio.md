# 音效设计、游戏音频与交互实现

检索分组：需求与声音语言、素材与层次、包络与频谱、响度与混音、空间与场景、触发与参数、资源与验收。前缀 AU；表内同组术语有关联，但不保证同义。

操作配方见 [audio-recipes.json](audio-recipes.json)，以本表 AUxxx 为 key；完整流程见 [audio-design-guide.md](audio-design-guide.md)。三份文件可独立读取、按文件名及 AU 编号检索，不依赖主索引已完成集成。配方是设计与工程建议，不是特定 SDK 的可直接运行代码。本文尾部逐项列出一手来源、URL、适用条目和核查边界，不使用全局 Sxx 编号。

使用时先保留用户的体验目标、现有引擎/版本、播放设备、资产规范、性能预算和修改范围。命中“空间音频”不意味着必须安装中间件；命中“厚重”也不意味着必须增大低频或响度。未知数值应留作项目实测与确认。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| AU001 | Audio brief; 声音需求简报; 听觉目标 | 更爽、更重、更科幻，但不知道怎么改 | 把形容词转成玩家应识别的信息、情绪、动作时刻与使用场景，并记录参考和反例 | 艺术方向、功能要求和可选处理分开；不能将“震撼”擅自改成更大声 |
| AU002 | Sonic identity; 声音语言; 声音家族 | 技能各不相同又像同一阵营 | 定义共同材质、节奏、音高运动与质感，再给不同功能保留可辨的轮廓 | 一致性不是所有声音同频同包络；语义辨认优先于装饰统一 |
| AU003 | Auditory hierarchy; 听觉层级; Figure-ground | 战斗太吵、危险提示听不见 | 按当前任务安排前景反馈、中景行动和背景环境，让重要信息获得时间与频谱空间 | 层级随情境改变；不是把所有“重要”资产永久增益拉满 |
| AU004 | Foley; Field recording; 拟音; 素材选型 | 木头不像木头、想做机械摩擦 | 从接触动作、共振材质与录音视角选择或录制声源，保留适合后续变形的干净素材 | 录音真实性不等于游戏可读性；素材可用性及授权需另行确认 |
| AU005 | Sample; Synthesis; Procedural audio | 采样还是合成、持续声如何变化 | 采样保留具体质感，合成提供受控声学结构，程序化规则组织运行时变化 | 随机播放采样不等同物理建模；实时合成要另算 CPU 与可复现性 |
| AU006 | Layering; Transient/body/texture/tail; 分层 | 打击薄、法术没有主体 | 按起音辨识、主体重量、表面细节、收尾空间分工，每层只补一个明确缺口 | 不要求固定层数；层越多可能越糊，单素材足够时不强拆 |
| AU007 | Envelope; ADSR/AHDSR; 包络 | 起音不脆、蓄力和松手像硬切 | 设计随时间变化的音量、滤波或音高；用起音、保持、衰减、持续、释放描述形态 | sustain 常是保持值而非固定时长；采样包络、调制包络与压缩器响应不是同一参数 |
| AU008 | Transient; Onset; Synchronization; 瞬态与动作同步 | 命中软、先出声音后碰到、挥空也有命中声 | 将可感知起音对应到动作或结果，用短时能量变化表达触感 | 文件开头不等于听觉起点；不能靠硬切攻击段换取低延迟 |
| AU009 | Spectrum; Timbre; Masking; EQ; 频谱与掩蔽 | 刺耳、浑浊、谁都听不清 | 结合试听和频谱找冲突，先删重复层或错开时序，再选择滤波和均衡 | 频谱图不是审美评分；不存在适合所有音效的必削或必提频段 |
| AU010 | Pitch contour; Resampling; Time stretching | 激光下坠、巨物更沉、变调后拖慢 | 用音高轨迹和时间伸缩塑造运动、体量与能量变化 | 改播放速率常同时改变音高和时长；独立变调/伸缩算法有伪影和成本 |
| AU011 | Phase; Polarity; Mono compatibility; 相位与极性 | 叠低频反而变薄、耳机好听单声道没了 | 检查相关素材的时间关系、极性及声道求和，避免核心信息因抵消消失 | 极性翻转不是任意相位校正；对齐波形峰值也不保证全频段相容 |
| AU012 | Edit fade; Zero crossing; Loop seam; 编辑淡变与接缝 | 开头啪一下、循环有咔哒或呼吸感 | 检查边界波形、声道和底噪连续性，用合适淡变或交叉淡化连接 | 零交叉不保证斜率、左右声道或音色连续；交叉淡化可能造成音量鼓包 |
| AU013 | Random variation; Shuffle; Anti-repeat | 脚步机关枪感、连击每次一样 | 在同一语义家族中组织素材变体、权重、避免紧邻重复及受限参数变化 | 无约束随机会破坏身份和同步；shuffle 的记忆范围需按实现确认 |
| AU014 | dBFS; dBTP; LUFS/LKFS; Loudness; 响度与电平 | 归一化了还是忽大忽小、该设多少 LUFS | 分别观察数字峰值、真峰值估计与感知加权节目响度，记录测量窗口和信号路径 | 峰值相同不代表同样响；节目测量标准不是所有短音效的统一目标，更不是声压安全保证 |
| AU015 | Gain staging; Headroom; 增益结构与余量 | 单独正常一起爆、总线上一直限幅 | 从资产、事件、分类总线到输出检查叠加电平，为最密集场景保留处理余量 | 文件未削波不代表混合输出未过载；浮点内部余量不消除最终输出问题 |
| AU016 | Compression; Limiting; Saturation; 动态处理 | 冲击不稳定、想更密但不想更吵 | 按峰值控制、动态整形或谐波着色的目的选择处理，并以匹配听感响度比较 | 三者不是互换的“变好按钮”；过快响应会改变瞬态，限幅不能修复错误层级 |
| AU017 | Bus; Send/return; Sidechain; Ducking; 分类混音 | 对话时压低环境、音效音量要独立 | 以总线组织类别和共享处理，以侧链或状态控制需要临时让位的信号 | 侧链是控制信号路径，不一定是可听素材；用户音量设置不能被混音状态覆盖 |
| AU018 | Snapshot; Mix state; Dynamic range mode | 战斗/菜单切换突兀、夜间模式 | 用场景状态改变多个混音参数，并定义过渡、优先级与退出恢复 | 小动态范围模式不是简单主音量变小；多状态叠加规则依引擎核对 |
| AU019 | Listener; Emitter; 2D/3D; Panning; HRTF | 声音从哪来、转镜头方向不对 | 明确听者、发声点和声道格式，再选择声像或双耳空间化 | HRTF 不是混响或距离衰减；相机与角色不一定同位，耳机处理不宜重复叠加 |
| AU020 | Distance attenuation; Air absorption; 距离衰减 | 远近没差、走近突然爆响 | 用距离控制直达声电平及必要的频谱变化，结合地图尺度设计可听范围 | 物理近似不自动符合玩法；不能把引擎世界单位直接当米，参数上下限要验证 |
| AU021 | Occlusion; Obstruction; Diffraction; 遮挡与绕射 | 隔墙仍很清、门边声音跳变 | 根据声路受阻情况处理电平和频谱，需要时引入门洞或传播路径近似 | 一条射线加低通不是完整绕射/透射模拟；各产品对术语和算法的划分不同 |
| AU022 | Reverb; Early reflection; Pre-delay; Dry/wet | 室内外没差、尾巴糊、空间太假 | 分别安排直达声、早期反射与衰减尾声来表达空间，同时保留行动辨识 | 混响时长不能唯一决定房间大小；烘焙尾声和运行时混响容易重复 |
| AU023 | Ambience bed; Spot emitter; 环境底床与散点 | 环境像死循环、整个森林贴在耳边 | 稳定底床承接场景，局部声源和稀疏事件提供位置与变化 | 底床不应长期抢占提示频谱；随机散点需要密度、区域及语义约束 |
| AU024 | Audio event; Semantic trigger; 语义事件 | 每帧都播放、挥空触发命中、UI 重复响 | 用确认、接触、进入、离开等语义边沿驱动音频，明确生产者和去重范围 | 动画通知、碰撞回调、网络消息可能描述同一次事件；不能全部无差别播放 |
| AU025 | State; Switch; RTPC; Parameter mapping | 速度越快越响、材质换音、蓄力音连续变化 | 离散类别选音，连续参数调曲线；注明单位、值域、默认值、平滑和所有者 | RTPC 是产品相关术语；状态与参数作用域不可互换，不能直接搬 API 名称 |
| AU026 | One-shot; Loop; Start/sustain/stop; 音频生命周期 | 松手仍在响、循环越开越多、销毁后幽灵声 | 为瞬发与持续事件分别定义创建、更新、释放及异常退出责任 | stop、淡出、尾声完成与释放句柄可能不同步；静音不等于资源释放 |
| AU027 | Concurrency; Voice stealing; Virtualization; 声部管理 | 爆炸多了掉帧、关键音被吞 | 按类别/所有者限制同时发声，明确拒绝或替换策略及虚拟声恢复语义 | 活跃实例不等于可听声部；虚拟化不等于停止，后台逻辑仍可能运行 |
| AU028 | Audio clock; Scheduling; Latency budget | 节奏飘、按键反馈迟、设备不同差很多 | 将素材前导、游戏调度、音频缓冲和设备输出分别计入端到端延迟 | 帧回调不是采样级时钟；调小缓冲不是无成本优化，蓝牙链路需单独实测 |
| AU029 | Network audio; Prediction; Deduplication | 联机开枪响两次、远端音效错位置 | 区分本地预测反馈和权威结果，随事件标识传递足够的声音语义并去重 | 通常同步事件而非逐采样波形；是否同步随机变体由玩法决定，不强制全局一致 |
| AU030 | Footstep system; Surface mapping; 脚步与材质反馈 | 鞋底没触地就响、地面材质错、跑步像走路 | 结合触地时刻、接触材质、步态与力度选择素材，再用变体避免机械重复 | 动画事件不保证真实接触；多人共享一个去重计时器会吞掉不同角色的脚步 |
| AU031 | Impact design; Whoosh; Hit confirmation; 挥击与命中 | 连续挥剑砍击音效、打击没力量、重击只是轻击放大 | 将动作前导、接触瞬态、材质主体与结果反馈区分，按强度改变结构而非只改增益 | 挥空、格挡、护盾、受伤不能误用同一确认语义；镜头特效不是声音成功的证据 |
| AU032 | UI earcon; Confirmation/error cue; 界面提示音 | 菜单吵、成功失败分不清、滚动响不停 | 用简洁且可辨的节奏/轮廓建立交互语法，限制导航密度并区分操作结果 | 不默认高音就是成功；要验证产品语境，不能用声音替代错误文本 |
| AU033 | Sample rate; Bit depth; Channel layout; Export | 导入变音、文件太大、声道乱了 | 按项目格式保留母版和交付版本，记录采样率、位深、声道布局、循环及尾声信息 | 格式选项不是质量排名；dither 只在相关量化流程中评估，不应每次导出重复叠加 |
| AU034 | Codec; Decode; Streaming; Preload; 音频资源加载 | 第一次播放卡、包体大、内存飙 | 根据首次响应、时长、并发和目标设备，在预解码、压缩驻留与流式读取间权衡 | 文件尺寸不等于解码内存；有损编码、平台转换可能改变起音和循环，需打包后验证 |
| AU035 | Audio bank; Asset manifest; Ownership; 资产交付与归属 | 编辑器有声打包没声、换场景丢音 | 记录事件到媒体的依赖、构建版本、加载完成条件和卸载责任 | bank 元数据就绪不保证所有样本已就绪；素材来源记录不等于完成法律授权审查 |
| AU036 | Audio profiling; Telemetry; Reproducibility; 音频剖析 | 偶发没声、声部泄漏、只有真机卡 | 关联事件日志、声部数、解码/流式开销和场景轨迹，区分未触发、被拒绝、不可听及未加载 | 不只看主线程平均耗时；记录设备、构建、混音状态和随机种子才有可比性 |
| AU037 | Multisensory cue; Captions; Mono option; 音频无障碍 | 静音玩不了、单耳漏警告、对白听不清 | 为关键声音提供非听觉通道，合理拆分音量控制并检查单声道可辨性 | 触觉也可能被关闭；字幕不是所有空间信息的自动替代，需验证实际决策能力 |
| AU038 | Reference listening; Level-matched A/B; 试听验收 | 独听很帅进游戏很糊、改了不知道更好没 | 固定场景、播放链路和监听设置，对同一语义做响度相近的对比及盲辨 | “更响”容易被误判成“更好”；响度匹配是比较控制，不要求最终资产同响度 |
| AU039 | Silence; Density; Contrast; 留白与听觉疲劳 | 一直轰、长时间玩累、重击不突出 | 从事件密度、持续高频、尾声重叠和安静窗口设计对比，保留听觉恢复空间 | 留白不是删除必要反馈；数字电平不能直接推导耳边声压或安全暴露时间 |
| AU040 | Interactive sound grammar; Charge/release/cancel; 蓄力交互 | 蓄力满了不清楚、打断还放成功音 | 将开始、维持、阶段达成、释放、取消映射成一致的声音状态机 | 可听进度应与实际玩法对应；音高无限上升不是唯一表达，也可能疲劳 |
| AU041 | Parameter smoothing; Hysteresis; 平滑与迟滞 | 速度临界点抖音、淡出中重启啪一下 | 连续量平滑，离散切换用不同进入/退出条件，并明确重入时接续当前状态 | 平滑会增加响应延迟；不能为消抖而掩盖重要瞬时事件，曲线需在实际参数域验证 |
| AU042 | Acceptance matrix; Regression; 端到端验收矩阵 | 怎样算做好了、每次改音都出新问题 | 分别验收识别、同步、混音、空间、生命周期、资源、可访问性与目标设备表现 | 没有实际资产/构建时只能验收规格完整性，不能声称音效质量或性能已经达标 |

## 来源与核查范围

核查日期：2026-09-20。已发起 web 搜索，并以 HTTP 获取官方正文补充核查；搜索工具未提供可用于正文验证的返回内容，不据此声称已读到搜索摘要。下列标识只在本音频专题内定位，不占全局 Sxx 编号。每项给出真实 URL、对应概念和证据范围；部分站点本次无法取得正文，单独列为待核查。设计配方与测试流程是结合机制整理的建议，不是官方逐字规范，也不是官方保证的最佳参数。

- **音频来源：W3C Web Audio 1.0**。URL：https://www.w3.org/TR/webaudio-1.0/ 。核查：规范正文中的 AudioParam 自动化、AudioBufferSourceNode、PannerNode、时间调度模型；对应 AU007、AU019、AU026、AU028、AU033、AU041。边界：只确认该规范机制，不证明任意浏览器/设备的支持程度、自动播放许可或端到端延迟。
- **音频来源：Ableton Live 11 音频效果器**。URL：https://www.ableton.com/en/live-manual/11/live-audio-effect-reference/ 。核查：Compressor、EQ、Limiter 等处理器的用途和响应参数；对应 AU009、AU011、AU015、AU016、AU017、AU022。边界：不将此 DAW 的参数定义及预设数值视作所有插件的规则；本文不照搬数值。
- **音频来源：Ableton Live 11 音频剪辑与变形**。URL：https://www.ableton.com/en/live-manual/11/audio-clips-tempo-and-warping/ 。核查：变形与速度/音高关系、不同素材对应的算法选择；对应 AU005、AU008、AU010。边界：算法描述不是引擎实时变调能力或质量保证。
- **音频来源：Ableton Live 11 Clip View**。URL：https://www.ableton.com/en/live-manual/11/clip-view/ 。核查：剪辑首尾淡变用于减少边缘点击、循环设置；对应 AU012。边界：DAW 的循环操作不保证游戏编码与解码后无缝，也不将软件默认淡变时长定为制作标准。
- **音频来源：Ableton Live 11 乐器参考**。URL：https://www.ableton.com/en/live-manual/11/live-instrument-reference/ 。核查：ADSR 的 attack/decay 时间、sustain level、release 以及 legato 重触发说明；对应 AU005、AU007、AU040、AU041。边界：用于包络机制与设计取舍，不将键盘乐器触发方式直接当作游戏状态机实现。
- **音频来源：ITU-R BS.1770**。URL：https://www.itu.int/rec/R-REC-BS.1770 。核查：官方条目页确认 BS.1770-5（11/2023）的标题、状态和节目响度/真峰值测量范围；对应 AU014。边界：未逐条审阅标准算法附件；未验证平台交付响度规范，不据此给短音效、游戏整体或听力安全指定数值。
- **音频来源：Epic Sound Cue Reference**。URL：https://dev.epicgames.com/documentation/en-us/unreal-engine/sound-cue-reference-for-unreal-engine 。核查：Mixer 分层电平、Random 权重、Modulator 的随机时机、Enveloper 曲线、Continuous Modulator 与参数交叉淡化，以及逻辑 Looping 不保证无缝的限制；对应 AU006、AU007、AU012、AU013、AU025、AU040。边界：只确认这些节点的文档语义，不将声音设计配方或其他引擎的行为归于此页。
- **音频来源：Epic Sound Concurrency Reference Guide**。URL：https://dev.epicgames.com/documentation/unreal-engine/sound-concurrency-reference-guide 。核查：Max Count、Limit to Owner、Resolution Rule、Retrigger Time、Voice Steal Release Time，以及活跃组件不等同实际可听声音的说明；对应 AU027、AU036。边界：动态版本页，不当作用户版本或发布状态承诺；运行时资源计数要在项目版本复核。
- **音频来源：Epic Sound Attenuation**。URL：https://dev.epicgames.com/documentation/unreal-engine/sound-attenuation-in-unreal-engine 。核查：距离、空间化、空气吸收、遮挡低通/音量、混响发送的独立配置；对应 AU019、AU020、AU021、AU022、AU023。边界：同为动态版本页；射线遮挡配置不证明完整声学传播或特定插件能力。
- **音频来源：Unity AudioClipLoadType**。URL：https://docs.unity.com/en-us/engine/6000.7/script-reference/unityengine/audiocliploadtype 。核查：HTTP 正文中 CompressedInMemory、DecompressOnLoad、Streaming 的定义与内存/解码取舍；对应 AU034。边界：未运行该版本，不采用其中任何资源比例作为预算；路径版本不代表用户项目版本。
- **音频来源：Microsoft XAG 103**。URL：https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103 。核查：关键视觉/听觉信息使用额外感官通道、触觉不能作为唯一替代的建议；对应 AU003、AU024、AU037、AU042。边界：设计指南不是项目已通过无障碍测试或平台认证的证明。
- **音频来源：Microsoft XAG 105**。URL：https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105 。核查：音频类别控制、单声道输出等可访问性建议；对应 AU017、AU019、AU037。边界：仍需结合设备、实际用户和玩法验证可理解性。

### 待核查的官方入口

以下链接保留为独立可检索的后续核查入口，不计入已验证内容，不支持任何版本/API 已确认的结论。本文通用建议不能替代这些产品的项目级复核。

- **待核查：FMOD Studio 2.03 Concepts**。URL：https://www.fmod.com/docs/2.03/studio/fmod-studio-concepts.html 。拟核查 instrument、trigger region、playlist 与播放生命周期，对应 AU006、AU013、AU024、AU026。本次 HTTP 200 但无可读正文，未确认具体机制。
- **待核查：FMOD Studio 2.03 Parameters**。URL：https://www.fmod.com/docs/2.03/studio/parameters.html 。拟核查参数作用域与自动化，对应 AU018、AU025、AU040、AU041。本次 HTTP 200 但无可读正文，未确认 snapshot 或总线 API。
- **待核查：FMOD Studio 2.03 Advanced Topics**。URL：https://www.fmod.com/docs/2.03/studio/advanced-topics.html 。拟核查事件虚拟化、停止与后台推进，对应 AU026、AU027。本次 HTTP 200 但无可读正文；虚拟化恢复规则必须在实际 SDK 复核。
- **待核查：FMOD Studio 2.03 Bank API**。URL：https://www.fmod.com/docs/2.03/api/studio-api-bank.html 。拟核查 bank 元数据与媒体就绪、样本加载、卸载责任，对应 AU034、AU035。本次 HTTP 200 但无可读正文，未验证接口、线程或打包行为。
- **待核查：Audiokinetic Creating Random Containers**。URL：https://www.audiokinetic.com/en/public-library/2024.1.4_8780/?id=creating_random_container&source=Help 。拟核查 random、shuffle、weight 及记忆范围，对应 AU013。本次 HTTP 返回验证码页，未取得产品正文，不声称已核对这些选项。
- **待核查：Audiokinetic The Wwise Project**。URL：https://www.audiokinetic.com/download/documents/WwiseProjectAdventure_en.pdf 。拟用于分层与变化的制作实践补充，对应 AU006、AU013、AU031。本次 HTTP 客户端处理失败，未取得可审阅正文、目录或试听内容，不作为配方证据。

尚未核查：用户工程及目标平台 SDK、闭源平台响度/认证要求、具体素材授权文本、目标耳机/扬声器、真实资产试听、联网重放与负载测试。AU001、AU002、AU004、AU029 至 AU032、AU038 至 AU042 中的需求组织、测试案例与创作决策主要为综合设计建议，不冒充来自某条规范。没有实际执行的步骤均不得写成已验收。
