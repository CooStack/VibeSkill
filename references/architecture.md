# 计算机体系结构与数字表示

按硬件表示、指令执行、存储层级和并行访存检索。来源入口 S56、S65，见 [sources.md](sources.md)；操作系统行为另见 [operating-systems.md](operating-systems.md)。不是硬件选购建议，具体指令、内存序和性能须查目标架构。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| HW001 | Bit; Byte; Binary; 位与字节 | 二进制、字节大小、位宽 | 区分信息位、字节和多位编码的数值解释 | 网络速率的 bit 与文件大小的 byte 不能混算 |
| HW002 | Signed integer; Two's complement; 补码 | 负数表示、整数溢出 | 用固定宽度编码整数并按规则解释符号 | 溢出行为由语言/指令规定，不总是可依赖的回绕 |
| HW003 | Endianness; 大端/小端; Byte order | 跨平台读二进制数值错 | 多字节值在存储中的字节顺序 | 字节顺序与位序、矩阵行列存储不是同一概念 |
| HW004 | Fixed-point; Floating-point; 定点/浮点 | 小数精度、嵌入式数值 | 在范围、精度和计算成本之间选择数值表示 | 浮点值不是精确实数；定点也有缩放和溢出限制 |
| HW005 | Logic gate; Combinational/Sequential logic | 逻辑门、寄存状态、电路 | 区分只依当前输入与含存储状态的数字逻辑 | 软件条件表达式不直接代表物理时序电路 |
| HW006 | ISA; Instruction set architecture; 指令集 | x86、ARM、RISC-V、二进制兼容 | 规定软件可见的指令及体系结构接口 | ISA 相同不意味着微架构、扩展或性能相同 |
| HW007 | Microarchitecture; 微架构 | 同指令集不同芯片速度 | 硬件对指令集的实际流水、执行和缓存实现 | 不用产品频率单独推断吞吐 |
| HW008 | CPU core; Hardware thread; SMT | 核心线程数、超线程 | 区分独立计算核与共享核资源的执行上下文 | 逻辑线程数量不等于等量完整核心 |
| HW009 | Register; ALU; Program counter | 寄存器、运算器、指令位置 | 处理器保存操作数、执行运算并跟踪控制流 | 寄存器是硬件资源，不等于所有语言局部变量 |
| HW010 | Pipeline; Hazard; 指令流水线 | 流水停顿、相关冒险 | 重叠执行阶段，并协调数据/控制/结构冲突 | 单条指令延迟和稳态吞吐不同 |
| HW011 | Branch prediction; Speculative execution | 分支多变慢、预测失败 | 预测控制流并提前执行可能需要的工作 | 无分支代码未必更快，副作用可见性由架构限制 |
| HW012 | Out-of-order execution; Instruction-level parallelism | 乱序执行、指令并行 | 在保持规定可观察行为的条件下重排可执行工作 | 不能据此假定源码顺序就是跨核可见顺序 |
| HW013 | Cache hierarchy; Cache line; Locality | CPU 缓存命中、顺序访问快 | 利用时间/空间局部性减少高延迟访存 | CPU 缓存与业务结果缓存的失效机制不同 |
| HW014 | Cache coherence; False sharing; 伪共享 | 多线程改不同变量仍然慢 | 协调核间缓存行副本；独立变量共用行可造成争用 | 一致性协议不替代应用层同步或语言内存模型 |
| HW015 | Memory consistency; Fence; 内存序 | 多核看到的写入顺序不同 | 规定并发内存操作可观察顺序及约束手段 | 屏障语义依架构和语言，不能仅靠 volatile 名称推断 |
| HW016 | MMU; Page table; TLB | 虚实地址转换、地址缓存 | 用页表和地址转换缓存映射虚拟地址 | TLB miss 不一定等于缺页或磁盘 IO |
| HW017 | NUMA; Memory affinity | 多路机器远端内存慢 | 不同计算节点访问内存有不同成本 | 绑核/绑内存需测量，不能默认为所有工作负载优化 |
| HW018 | SIMD; Vectorization; 向量化 | 批量同类运算、向量指令 | 用一个操作同时处理多份数据 | 数据对齐、分支和带宽可能限制收益 |
| HW019 | SIMT; GPU warp/wave; 分支发散 | GPU 分支多、线程束效率 | 以成组执行方式组织大量线程 | SIMT 不代表线程完全独立地以不同指令同时运行 |
| HW020 | DMA; Memory-mapped IO; 直接存储器访问 | 设备搬数据、硬件寄存器 | 区分设备直接传输与用地址空间访问设备 | 需要适当同步和缓存一致性处理，不能当普通内存随意优化 |
| HW021 | Interrupt; Exception; Trap | 硬件中断、异常进入内核 | 区分外部事件和指令执行触发的控制转移 | 术语细节依架构，异常不都代表错误 |
| HW022 | Amdahl's law; Parallel speedup | 加核心不提速、串行瓶颈 | 用不可并行部分约束理想整体加速 | 实际还受通信、同步及工作量变化影响 |
| HW023 | Memory bandwidth; Latency; Roofline | 算力高却跑不快 | 区分数据传输量、等待时间及计算/带宽上限 | 理论峰值不等于可持续业务性能 |
| HW024 | ECC; Bit error; 硬件可靠性 | 内存位翻转、纠错 | 用冗余检测或纠正特定错误模式 | ECC 不保证修复所有错误，也不是备份机制 |
