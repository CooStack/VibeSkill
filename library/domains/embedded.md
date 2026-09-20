# 嵌入式、实时系统与物联网

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [EM001 · MCU; Microcontroller; 微控制器](../concepts/EM001.md) | 单片机、板上控制 |
| [EM002 · Firmware; Bare metal; 固件与裸机](../concepts/EM002.md) | 没操作系统的程序 |
| [EM003 · RTOS; Real-time operating system](../concepts/EM003.md) | 实时任务调度 |
| [EM004 · Hard/Soft real-time; 硬实时软实时](../concepts/EM004.md) | 必须准时响应、偶尔迟到 |
| [EM005 · WCET; Worst-case execution time](../concepts/EM005.md) | 最坏耗时、时间预算 |
| [EM006 · Interrupt; ISR; 中断服务程序](../concepts/EM006.md) | 外设到数据马上响应 |
| [EM007 · GPIO; General-purpose I/O](../concepts/EM007.md) | 控制引脚、读取开关 |
| [EM008 · UART; SPI; I2C; 外设总线](../concepts/EM008.md) | 串口、传感器通信 |
| [EM009 · ADC; DAC; 模数与数模转换](../concepts/EM009.md) | 传感器读数、输出模拟量 |
| [EM010 · PWM; Pulse-width modulation](../concepts/EM010.md) | 调占空比、调光 |
| [EM011 · Watchdog; 看门狗](../concepts/EM011.md) | 程序卡死自动恢复 |
| [EM012 · Debouncing; 按键消抖](../concepts/EM012.md) | 按一次触发多次 |
| [EM013 · MMIO; Memory-mapped I/O](../concepts/EM013.md) | 读写外设寄存器 |
| [EM014 · Bootloader; Secure boot](../concepts/EM014.md) | 启动验证、固件加载 |
| [EM015 · OTA; Firmware update; 空中升级](../concepts/EM015.md) | 远程更新设备、断电变砖 |
| [EM016 · IoT; MQTT; QoS](../concepts/EM016.md) | 设备遥测、消息服务质量 |
| [EM017 · Edge computing; 边缘计算](../concepts/EM017.md) | 离线也能处理、减少回云 |
| [EM018 · Power budget; Sleep mode; 功耗预算](../concepts/EM018.md) | 电池续航、低功耗唤醒 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为嵌入式领域基线，将设备、实时和低功耗概念落实为平台约束、时序与失效处理；不充当接线或安全关键操作手册。

### 关键特征

- 硬件电气条件、寄存器语义和执行上下文必须按目标资料核对，不能从通用示例推断。
- 实时目标应表达为截止期限及错过后的后果，而非仅比较平均速度。
- 中断、任务和外设之间的资源所有权明确，复位或重试不应掩盖业务失效。

### 如何落实

- 确认目标板、外设和运行模型，列出本次功能的输入范围、时限与允许的失败状态。
- 按已核对的硬件约束安排采样、通信或输出，将中断内工作与可延后的处理划分清楚。
- 为共享缓冲、设备传输和任务交接定义访问责任与同步；涉及功耗时按完整工作周期记录能量。
- 在受控测试条件下安排超时、复位或更新中断的恢复路径，避免未验证的软件直接驱动有风险负载。

### 如何验收

- 使用目标环境的时间证据核对响应与抖动，并标明实测最大值与已证明上界的区别。
- 模拟通信错误、输入抖动及资源忙，核对状态机不会卡住或重复执行动作。
- 按任务范围验证重启或更新失败后的可恢复状态，功耗目标按完整工作周期核对。

### 常见误用

- 使用实时系统或提高频率后就宣称满足截止期限，没有端到端时序证据。
- 无条件维持看门狗或重复复位，让系统看似存活却无法完成业务。
