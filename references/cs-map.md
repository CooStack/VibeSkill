# 计算机科学覆盖地图

面向智能体的需求路由，不是课程学习顺序。先从对象、症状、约束选择领域，保留跨层候选；不要因为“卡”“安全”“模型”等泛词就同时加载所有表。

| 领域 / 检索过滤名 | 问题线索 | 参考与 ID |
| --- | --- | --- |
| 体系结构 `architecture` / `hw` | 字节序、指令集、缓存行、SIMD、NUMA | [architecture.md](architecture.md)，HW001-HW024 |
| 操作系统 `operating-systems` / `os` | 进程、页故障、文件描述符、OOM、系统调用 | [operating-systems.md](operating-systems.md)，OS001-OS028 |
| 网络与互联网 `networking` / `network` | TCP 半包、DNS、BGP、TLS、QUIC、NAT、域名 | [networking.md](networking.md)，NW001-NW036 |
| 算法 `algorithms` / `algo` | 状态转移、最短路、拓扑、排序、复杂度 | [algorithms.md](algorithms.md)，AL001-AL024 |
| 语言与编译 `languages-compilers` / `compiler` | AST、SSA、ABI、链接、类型、所有权 | [languages-compilers.md](languages-compilers.md)，LC001-LC024 |
| 安全与密码 `security` / `sec` | 威胁模型、越权、密钥、签名、注入 | [security.md](security.md)，SE001-SE024 |
| 分布式 `distributed` / `dist` | 部分失败、共识、脑裂、租约、复制一致性 | [distributed.md](distributed.md)，DC001-DC024 |
| 数据工程 `data-engineering` / `data` | ETL、CDC、流窗口、列存、全文及向量检索 | [data-engineering.md](data-engineering.md)，DE001-DE022 |
| AI 与机器学习 `machine-learning` / `ml` / `ai` | 数据划分、过拟合、召回率、RAG、模型评估 | [machine-learning.md](machine-learning.md)，ML001-ML026 |
| 可靠性 `reliability` / `sre` | SLO、监控、尾延迟、部署、恢复、形式验证 | [reliability.md](reliability.md)，RE001-RE024 |
| 计算理论 `computation-theory` / `theory` | 自动机、可计算性、P/NP、逻辑、信息熵 | [computation-theory.md](computation-theory.md)，TC001-TC020 |
| 嵌入式 `embedded` / `iot` | RTOS、中断、固件、截止期限、设备升级 | [embedded.md](embedded.md)，EM001-EM018 |
| 人与计算 `human-computing` / `hci` | 可用性、隐私、公平性、个人信息、认知 | [human-computing.md](human-computing.md)，HC001-HC012 |

## 复用既有领域

- 数据结构与离散/数值工具：[数据结构](data-structures.md)、[数学](mathematics.md)。
- 图形、视觉资产与交互：[图形学](graphics.md)、[OpenGL](opengl.md)、[建模](modeling.md)、[设计](design.md)。机器学习的 computer vision 与美术/渲染不是同义词。
- 软件设计与业务实现：[设计模式](design-patterns.md)、[工程表达](engineering.md)、[后端](backend.md)、[前端](frontend.md)。
- 数据库和语言实现优先相应技术栈：[MySQL](mysql.md)、[Java](java.md)、[Kotlin](kotlin.md)、[TypeScript](typescript.md) 等；抽象机制不覆盖具体运行时契约。

## 容易跨层误判

| 用户说法 | 候选与检查 |
| --- | --- |
| “内存泄漏 / OOM” | 区分 OS028 主机/容器限制、OS008 驻留内存、JVM 堆和原生资源；先看证据，不立即加内存 |
| “消息粘一起” | NW012 字节流分帧，不应假设一次发送对应一次接收；不未经允许更改协议 |
| “结果不一致” | 数据口径 DE008、并发竞态 OS014、副本一致性 DC006-DC009 都可能；先确认观察范围 |
| “模型更准确” | 先确认三维模型还是预测模型；ML005/ML006 检查划分及泄漏，不能默认微调 |
| “实时” | 页面即时反馈、流数据时效 DE009-011、截止期限 EM004 含义不同 |
| “DP / CS / MAC / CFG / ANN” | 读取缩写映射，结合对象和领域消歧，不能仅按出现频率纠正用户 |

## 使用边界

这里覆盖主要方向及常见交叉问题，并非整个学科的全部概念。缺项先查相邻领域与一手资料；普通调用不自行扩库。来源目录记录实际核查程度，不能把课程入口或协议标题已访问当作每条摘要都逐项证实。
