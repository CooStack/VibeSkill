# 音效设计与游戏音频

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [AU001 · Audio brief; 声音需求简报; 听觉目标](../concepts/AU001.md) | 更爽、更重、更科幻，但不知道怎么改 |
| [AU002 · Sonic identity; 声音语言; 声音家族](../concepts/AU002.md) | 技能各不相同又像同一阵营 |
| [AU003 · Auditory hierarchy; 听觉层级; Figure-ground](../concepts/AU003.md) | 战斗太吵、危险提示听不见 |
| [AU004 · Foley; Field recording; 拟音; 素材选型](../concepts/AU004.md) | 木头不像木头、想做机械摩擦 |
| [AU005 · Sample; Synthesis; Procedural audio](../concepts/AU005.md) | 采样还是合成、持续声如何变化 |
| [AU006 · Layering; Transient/body/texture/tail; 分层](../concepts/AU006.md) | 打击薄、法术没有主体 |
| [AU007 · Envelope; ADSR/AHDSR; 包络](../concepts/AU007.md) | 起音不脆、蓄力和松手像硬切 |
| [AU008 · Transient; Onset; Synchronization; 瞬态与动作同步](../concepts/AU008.md) | 命中软、先出声音后碰到、挥空也有命中声 |
| [AU009 · Spectrum; Timbre; Masking; EQ; 频谱与掩蔽](../concepts/AU009.md) | 刺耳、浑浊、谁都听不清 |
| [AU010 · Pitch contour; Resampling; Time stretching](../concepts/AU010.md) | 激光下坠、巨物更沉、变调后拖慢 |
| [AU011 · Phase; Polarity; Mono compatibility; 相位与极性](../concepts/AU011.md) | 叠低频反而变薄、耳机好听单声道没了 |
| [AU012 · Edit fade; Zero crossing; Loop seam; 编辑淡变与接缝](../concepts/AU012.md) | 开头啪一下、循环有咔哒或呼吸感 |
| [AU013 · Random variation; Shuffle; Anti-repeat](../concepts/AU013.md) | 脚步机关枪感、连击每次一样 |
| [AU014 · dBFS; dBTP; LUFS/LKFS; Loudness; 响度与电平](../concepts/AU014.md) | 归一化了还是忽大忽小、该设多少 LUFS |
| [AU015 · Gain staging; Headroom; 增益结构与余量](../concepts/AU015.md) | 单独正常一起爆、总线上一直限幅 |
| [AU016 · Compression; Limiting; Saturation; 动态处理](../concepts/AU016.md) | 冲击不稳定、想更密但不想更吵 |
| [AU017 · Bus; Send/return; Sidechain; Ducking; 分类混音](../concepts/AU017.md) | 对话时压低环境、音效音量要独立 |
| [AU018 · Snapshot; Mix state; Dynamic range mode](../concepts/AU018.md) | 战斗/菜单切换突兀、夜间模式 |
| [AU019 · Listener; Emitter; 2D/3D; Panning; HRTF](../concepts/AU019.md) | 声音从哪来、转镜头方向不对 |
| [AU020 · Distance attenuation; Air absorption; 距离衰减](../concepts/AU020.md) | 远近没差、走近突然爆响 |
| [AU021 · Occlusion; Obstruction; Diffraction; 遮挡与绕射](../concepts/AU021.md) | 隔墙仍很清、门边声音跳变 |
| [AU022 · Reverb; Early reflection; Pre-delay; Dry/wet](../concepts/AU022.md) | 室内外没差、尾巴糊、空间太假 |
| [AU023 · Ambience bed; Spot emitter; 环境底床与散点](../concepts/AU023.md) | 环境像死循环、整个森林贴在耳边 |
| [AU024 · Audio event; Semantic trigger; 语义事件](../concepts/AU024.md) | 每帧都播放、挥空触发命中、UI 重复响 |
| [AU025 · State; Switch; RTPC; Parameter mapping](../concepts/AU025.md) | 速度越快越响、材质换音、蓄力音连续变化 |
| [AU026 · One-shot; Loop; Start/sustain/stop; 音频生命周期](../concepts/AU026.md) | 松手仍在响、循环越开越多、销毁后幽灵声 |
| [AU027 · Concurrency; Voice stealing; Virtualization; 声部管理](../concepts/AU027.md) | 爆炸多了掉帧、关键音被吞 |
| [AU028 · Audio clock; Scheduling; Latency budget](../concepts/AU028.md) | 节奏飘、按键反馈迟、设备不同差很多 |
| [AU029 · Network audio; Prediction; Deduplication](../concepts/AU029.md) | 联机开枪响两次、远端音效错位置 |
| [AU030 · Footstep system; Surface mapping; 脚步与材质反馈](../concepts/AU030.md) | 鞋底没触地就响、地面材质错、跑步像走路 |
| [AU031 · Impact design; Whoosh; Hit confirmation; 挥击与命中](../concepts/AU031.md) | 连续挥剑砍击音效、打击没力量、重击只是轻击放大 |
| [AU032 · UI earcon; Confirmation/error cue; 界面提示音](../concepts/AU032.md) | 菜单吵、成功失败分不清、滚动响不停 |
| [AU033 · Sample rate; Bit depth; Channel layout; Export](../concepts/AU033.md) | 导入变音、文件太大、声道乱了 |
| [AU034 · Codec; Decode; Streaming; Preload; 音频资源加载](../concepts/AU034.md) | 第一次播放卡、包体大、内存飙 |
| [AU035 · Audio bank; Asset manifest; Ownership; 资产交付与归属](../concepts/AU035.md) | 编辑器有声打包没声、换场景丢音 |
| [AU036 · Audio profiling; Telemetry; Reproducibility; 音频剖析](../concepts/AU036.md) | 偶发没声、声部泄漏、只有真机卡 |
| [AU037 · Multisensory cue; Captions; Mono option; 音频无障碍](../concepts/AU037.md) | 静音玩不了、单耳漏警告、对白听不清 |
| [AU038 · Reference listening; Level-matched A/B; 试听验收](../concepts/AU038.md) | 独听很帅进游戏很糊、改了不知道更好没 |
| [AU039 · Silence; Density; Contrast; 留白与听觉疲劳](../concepts/AU039.md) | 一直轰、长时间玩累、重击不突出 |
| [AU040 · Interactive sound grammar; Charge/release/cancel; 蓄力交互](../concepts/AU040.md) | 蓄力满了不清楚、打断还放成功音 |
| [AU041 · Parameter smoothing; Hysteresis; 平滑与迟滞](../concepts/AU041.md) | 速度临界点抖音、淡出中重启啪一下 |
| [AU042 · Acceptance matrix; Regression; 端到端验收矩阵](../concepts/AU042.md) | 怎样算做好了、每次改音都出新问题 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为音效设计与交互音频领域基线，将听觉目标落实为声音语义、素材形态、触发契约和实际场景试听，不预设中间件或统一响度参数。

### 关键特征

- 先明确玩家需要识别的动作与结果，再决定素材层次和处理；厚重或震撼不直接等于更响。
- 区分素材质量、触发时机、空间表现和混音层级，每种问题使用对应证据。
- 沿用项目音频系统与资产规范，数字电平、感知响度和实际声压不互相替代。

### 如何落实

- 把体验形容词转成参考片段、关键听觉信息和不能被掩蔽的提示，制作最小可试听版本。
- 按起音、主体和尾声的实际缺口调整包络、频谱或层次，用听感响度相近的对照判断改善。
- 为事件明确触发者、参数单位、空间归属、重复处理及开始到释放的责任，持续音覆盖取消与重入。
- 接入真实混音和目标构建，核对最密集场景、资源加载与播放设备；只按已确认预算安排声部或加载策略。

### 如何验收

- 在相同场景和监听设置下对比辨识度、动作同步及关键提示可懂度，不把音量增大当作质量证据。
- 重复触发、取消、暂停和卸载，核对循环、尾声与实例释放；空间声音沿固定路径检查方向及远近变化。
- 在实际构建检查首播、循环接缝、混合输出和资源趋势，并按需求验证单声道或非听觉替代信息。

### 常见误用

- 不断叠层、增加低频或依靠总线限幅，掩盖错误同步与听觉层级。
- 仅试听编辑器中的单个资产，就宣称运行时混音、延迟与设备性能已经达标。
