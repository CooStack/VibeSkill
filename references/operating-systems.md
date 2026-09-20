# 操作系统与系统编程

按执行隔离、调度、虚拟内存、同步、IO 和文件系统检索。来源 S57，见 [sources.md](sources.md)。Linux 名称是例子，不保证 Windows/macOS 有同名 API；内核、平台和文件系统版本须单独核对。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| OS001 | Kernel; User space; System call | 用户态内核态、系统调用 | 分离特权资源管理与普通程序执行 | 进入内核不必发生进程切换 |
| OS002 | Process; Thread; Address space | 进程线程、任务隔离 | 进程拥有资源/地址空间，线程共享部分进程状态 | 隔离强度和共享内容不能只凭名字推断 |
| OS003 | Context switch; Scheduler | 线程切换多、调度开销 | 保存恢复执行状态并分配 CPU 使用机会 | 切换次数不单独决定延迟，阻塞和抢占需区分 |
| OS004 | Preemption; Priority; Fairness | 高优先级、抢占、公平调度 | 在吞吐、响应及公平目标之间分配执行 | 优先级高不保证满足实时截止时间 |
| OS005 | Priority inversion; 优先级反转 | 高优先级任务被低优先级挡住 | 共享资源依赖使调度优先顺序不能直接实现 | 提升线程优先级不必消除资源阻塞 |
| OS006 | Virtual memory; Paging; 虚拟内存 | 内存地址大于物理内存 | 用地址映射和按页管理组织隔离及资源利用 | 虚拟内存不等于“磁盘充当内存”这单一机制 |
| OS007 | Page fault; Demand paging; Swap | 缺页多、换页抖动 | 按需要处理尚未满足的映射或驻留访问 | 软缺页不必读取磁盘，缺页不是一律程序错误 |
| OS008 | Resident set; Working set; RSS | 进程内存涨、常驻集 | 观察驻留物理页及一段时间实际使用的数据集合 | RSS、虚拟地址空间和堆已用量不能互相替代 |
| OS009 | Copy-on-write; COW; 写时复制 | 快照共享、fork 内存 | 先共享数据，在修改时复制以隔离写入 | 写入高峰仍可能增加内存与延迟 |
| OS010 | Memory mapping; mmap; 文件映射 | 大文件映射读取、共享内存 | 将文件或共享对象映射到地址空间 | 映射成功不表示所有页已加载，也不保证写入已持久化 |
| OS011 | Allocation; Fragmentation; 内存碎片 | 总内存够却申请失败 | 分配布局与空闲空间形态影响可用性 | 应区分内部/外部碎片、虚拟与物理连续要求 |
| OS012 | Mutex; Semaphore; Condition variable | 互斥、计数许可、等待条件 | 分别保护临界区、管理许可和等待谓词变化 | 条件变量被唤醒仍需重新检查条件 |
| OS013 | Deadlock; Livelock; Starvation | 卡死、一直重试、任务饿死 | 区分循环等待、无进展活动和长期得不到资源 | CPU 很忙不意味着程序有业务进展 |
| OS014 | Race condition; Data race; 竞争 | 偶发共享状态错误 | 区分时间依赖逻辑问题和语言内存模型中的未同步冲突 | 无 data race 不等于没有更高层竞态 |
| OS015 | IPC; Pipe; Shared memory; Socket | 进程通信、管道传数据 | 为不同进程建立数据交换方式 | 共享内存仍需同步和生命周期管理 |
| OS016 | Blocking/Nonblocking; Sync/Async IO | 异步是否等于不阻塞 | 分别关注调用是否等待和完成结果如何交付 | 两组概念不能机械一一对应 |
| OS017 | IO multiplexing; select/poll/epoll; IOCP | 大量连接监听、IO 就绪 | 组织多 IO 对象的就绪或完成事件 | epoll 与 IOCP 模型不同，不能只换函数名 |
| OS018 | File descriptor; Handle; Resource leak | 打开文件太多、句柄耗尽 | 用内核管理引用访问 IO 等资源 | GC 存在不保证及时释放文件、连接等资源 |
| OS019 | File system; Inode; Directory entry | 文件名与文件对象、硬链接 | 区分目录映射、元数据对象与文件内容 | inode 是类 Unix 实现概念，路径不是稳定对象身份 |
| OS020 | Hard link; Symbolic link; Symlink | 软硬链接、路径重定向 | 硬链接关联同一对象，符号链接保存目标路径 | 符号链接目标可变化，安全路径检查要考虑实际解析 |
| OS021 | Page cache; Buffered IO; Direct IO | 文件写完没落盘、缓存 IO | 操作系统缓存或旁路部分缓存策略影响读写 | direct IO 不自动等同同步持久化 |
| OS022 | fsync; Flush; Crash consistency | 断电后文件坏、持久写入 | 区分缓冲清理、持久化请求和故障后一致性 | 文件内容和目录更新可能需要不同持久化步骤 |
| OS023 | Journaling; Copy-on-write filesystem | 日志文件系统、恢复元数据 | 用记录或写时更新组织可恢复的存储变更 | 文件系统一致性不保证应用多文件事务 |
| OS024 | Permissions; ACL; UID/GID | 文件读不了、操作系统权限 | 按主体及对象策略决定资源访问 | 进程用户名不等于应用用户身份 |
| OS025 | Namespace; cgroup; Container isolation | 容器看不到文件、CPU 限额 | 在支持的平台上隔离视图与控制资源使用 | 容器不是默认等价完整虚拟机安全边界 |
| OS026 | Hypervisor; VM; Virtualization | 虚拟机、硬件虚拟化 | 通过虚拟硬件边界承载客体系统 | 系统 VM、JVM 和虚拟内存的 VM 语义不同 |
| OS027 | Signal; Exit status; Graceful shutdown | 进程退出、优雅停机 | 处理通知、终止结果与资源收尾 | 强制终止可能跳过清理，处理方式依平台 |
| OS028 | OOM; Overcommit; Resource limit | 进程被杀、内存不足 | 内存压力、承诺与配额共同影响分配及终止 | 容器 OOM、宿主 OOM 与语言堆异常要分别诊断 |
