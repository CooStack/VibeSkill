# 操作系统与系统编程

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [OS001 · Kernel; User space; System call](../concepts/OS001.md) | 用户态内核态、系统调用 |
| [OS002 · Process; Thread; Address space](../concepts/OS002.md) | 进程线程、任务隔离 |
| [OS003 · Context switch; Scheduler](../concepts/OS003.md) | 线程切换多、调度开销 |
| [OS004 · Preemption; Priority; Fairness](../concepts/OS004.md) | 高优先级、抢占、公平调度 |
| [OS005 · Priority inversion; 优先级反转](../concepts/OS005.md) | 高优先级任务被低优先级挡住 |
| [OS006 · Virtual memory; Paging; 虚拟内存](../concepts/OS006.md) | 内存地址大于物理内存 |
| [OS007 · Page fault; Demand paging; Swap](../concepts/OS007.md) | 缺页多、换页抖动 |
| [OS008 · Resident set; Working set; RSS](../concepts/OS008.md) | 进程内存涨、常驻集 |
| [OS009 · Copy-on-write; COW; 写时复制](../concepts/OS009.md) | 快照共享、fork 内存 |
| [OS010 · Memory mapping; mmap; 文件映射](../concepts/OS010.md) | 大文件映射读取、共享内存 |
| [OS011 · Allocation; Fragmentation; 内存碎片](../concepts/OS011.md) | 总内存够却申请失败 |
| [OS012 · Mutex; Semaphore; Condition variable](../concepts/OS012.md) | 互斥、计数许可、等待条件 |
| [OS013 · Deadlock; Livelock; Starvation](../concepts/OS013.md) | 卡死、一直重试、任务饿死 |
| [OS014 · Race condition; Data race; 竞争](../concepts/OS014.md) | 偶发共享状态错误 |
| [OS015 · IPC; Pipe; Shared memory; Socket](../concepts/OS015.md) | 进程通信、管道传数据 |
| [OS016 · Blocking/Nonblocking; Sync/Async IO](../concepts/OS016.md) | 异步是否等于不阻塞 |
| [OS017 · IO multiplexing; select/poll/epoll; IOCP](../concepts/OS017.md) | 大量连接监听、IO 就绪 |
| [OS018 · File descriptor; Handle; Resource leak](../concepts/OS018.md) | 打开文件太多、句柄耗尽 |
| [OS019 · File system; Inode; Directory entry](../concepts/OS019.md) | 文件名与文件对象、硬链接 |
| [OS020 · Hard link; Symbolic link; Symlink](../concepts/OS020.md) | 软硬链接、路径重定向 |
| [OS021 · Page cache; Buffered IO; Direct IO](../concepts/OS021.md) | 文件写完没落盘、缓存 IO |
| [OS022 · fsync; Flush; Crash consistency](../concepts/OS022.md) | 断电后文件坏、持久写入 |
| [OS023 · Journaling; Copy-on-write filesystem](../concepts/OS023.md) | 日志文件系统、恢复元数据 |
| [OS024 · Permissions; ACL; UID/GID](../concepts/OS024.md) | 文件读不了、操作系统权限 |
| [OS025 · Namespace; cgroup; Container isolation](../concepts/OS025.md) | 容器看不到文件、CPU 限额 |
| [OS026 · Hypervisor; VM; Virtualization](../concepts/OS026.md) | 虚拟机、硬件虚拟化 |
| [OS027 · Signal; Exit status; Graceful shutdown](../concepts/OS027.md) | 进程退出、优雅停机 |
| [OS028 · OOM; Overcommit; Resource limit](../concepts/OS028.md) | 进程被杀、内存不足 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为操作系统领域基线，将进程、内存、句柄和调度概念落实为资源归属、运行证据与可验证的回收行为。

### 关键特征

- 先区分资源泄漏、负载增长和配额限制，不把提高上限作为默认修复。
- 虚拟内存、驻留内存、文件或设备句柄等指标分别解释，单个总量不能直接证明根因。
- 进程、线程与系统资源的所有者和退出路径明确，平台行为按目标环境核对。

### 如何落实

- 用稳定复现步骤记录进程身份、操作次数和资源基线，选择与症状对应的内存、句柄或调度证据。
- 沿分配或打开到释放路径追踪拥有者，区分仍被使用、可回收和丢失引用的资源。
- 对阻塞与卡顿区分计算、等待、缺页和 I/O，使用对应线程或系统证据定位等待对象。
- 针对责任缺失修复释放、取消或访问模式；只有合法负载确实触及限制时才评估配额调整。

### 如何验收

- 反复执行复现操作并等待合理回收阶段，核对相关资源曲线是否稳定而非持续累积。
- 在异常、取消和进程退出路径检查文件、连接或句柄释放及子任务终止。
- 用相同负载对照等待和资源指标，确认根因改善，未只是把失败推迟到更高上限。

### 常见误用

- 看到内存数字升高就认定泄漏，忽略指标含义、缓存和负载阶段。
- 通过增加内存或句柄配额掩盖所有权缺失，未保留资源证据。
