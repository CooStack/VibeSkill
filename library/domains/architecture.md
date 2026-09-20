# 计算机体系结构与数字表示

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [HW001 · Bit; Byte; Binary; 位与字节](../concepts/HW001.md) | 二进制、字节大小、位宽 |
| [HW002 · Signed integer; Two's complement; 补码](../concepts/HW002.md) | 负数表示、整数溢出 |
| [HW003 · Endianness; 大端/小端; Byte order](../concepts/HW003.md) | 跨平台读二进制数值错 |
| [HW004 · Fixed-point; Floating-point; 定点/浮点](../concepts/HW004.md) | 小数精度、嵌入式数值 |
| [HW005 · Logic gate; Combinational/Sequential logic](../concepts/HW005.md) | 逻辑门、寄存状态、电路 |
| [HW006 · ISA; Instruction set architecture; 指令集](../concepts/HW006.md) | x86、ARM、RISC-V、二进制兼容 |
| [HW007 · Microarchitecture; 微架构](../concepts/HW007.md) | 同指令集不同芯片速度 |
| [HW008 · CPU core; Hardware thread; SMT](../concepts/HW008.md) | 核心线程数、超线程 |
| [HW009 · Register; ALU; Program counter](../concepts/HW009.md) | 寄存器、运算器、指令位置 |
| [HW010 · Pipeline; Hazard; 指令流水线](../concepts/HW010.md) | 流水停顿、相关冒险 |
| [HW011 · Branch prediction; Speculative execution](../concepts/HW011.md) | 分支多变慢、预测失败 |
| [HW012 · Out-of-order execution; Instruction-level parallelism](../concepts/HW012.md) | 乱序执行、指令并行 |
| [HW013 · Cache hierarchy; Cache line; Locality](../concepts/HW013.md) | CPU 缓存命中、顺序访问快 |
| [HW014 · Cache coherence; False sharing; 伪共享](../concepts/HW014.md) | 多线程改不同变量仍然慢 |
| [HW015 · Memory consistency; Fence; 内存序](../concepts/HW015.md) | 多核看到的写入顺序不同 |
| [HW016 · MMU; Page table; TLB](../concepts/HW016.md) | 虚实地址转换、地址缓存 |
| [HW017 · NUMA; Memory affinity](../concepts/HW017.md) | 多路机器远端内存慢 |
| [HW018 · SIMD; Vectorization; 向量化](../concepts/HW018.md) | 批量同类运算、向量指令 |
| [HW019 · SIMT; GPU warp/wave; 分支发散](../concepts/HW019.md) | GPU 分支多、线程束效率 |
| [HW020 · DMA; Memory-mapped IO; 直接存储器访问](../concepts/HW020.md) | 设备搬数据、硬件寄存器 |
| [HW021 · Interrupt; Exception; Trap](../concepts/HW021.md) | 硬件中断、异常进入内核 |
| [HW022 · Amdahl's law; Parallel speedup](../concepts/HW022.md) | 加核心不提速、串行瓶颈 |
| [HW023 · Memory bandwidth; Latency; Roofline](../concepts/HW023.md) | 算力高却跑不快 |
| [HW024 · ECC; Bit error; 硬件可靠性](../concepts/HW024.md) | 内存位翻转、纠错 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为计算机体系结构领域基线，将数字表示、存储层级和执行概念落实为目标硬件约束与可比较的运行证据。

### 关键特征

- 区分语言保证、指令集约定与微架构表现，不能跨层推断。
- 位宽、符号、字节序、对齐和数值精度应在数据边界明确。
- 优化依据实际计算、访存或同步瓶颈，不从核心数量或理论峰值直接推算收益。

### 如何落实

- 确认目标平台及相关数据表示，用已知字节模式核对跨边界编码和解释。
- 识别工作负载的访问顺序、共享写入和计算密度，提出能够被测量证伪的瓶颈假设。
- 在语言与平台允许的范围调整布局、批量操作或并行划分，涉及共享访问时单独核对同步语义。
- 使用目标环境可用的计时与硬件指标比较前后结果，记录输入规模、预热及并行度。

### 如何验收

- 用边界数值和已知编码核对溢出、精度与字节解释，不依赖偶然回绕。
- 比较不同规模和并行度下的耗时与相关指标，确认改善来自预期瓶颈变化。
- 对共享数据的正确性与性能分别验证，确认布局或向量化没有改变约定结果。

### 常见误用

- 将缓存一致性视为应用同步，或把源码顺序当作跨核可见顺序。
- 未测量就绑核、填充或向量化，用硬件术语代替收益证据。
