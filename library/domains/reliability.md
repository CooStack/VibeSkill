# 可靠性、云基础设施与质量验证

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [RE001 · SRE; Site reliability engineering](../concepts/RE001.md) | 稳定性治理、运维自动化 |
| [RE002 · SLI; SLO; SLA](../concepts/RE002.md) | 可用率目标、服务承诺 |
| [RE003 · Error budget; 错误预算](../concepts/RE003.md) | 发布速度与稳定性冲突 |
| [RE004 · Observability; 可观测性](../concepts/RE004.md) | 不知道为什么慢 |
| [RE005 · Metrics; Logs; Traces](../concepts/RE005.md) | 指标日志链路如何关联 |
| [RE006 · Distributed tracing; Span; Context propagation](../concepts/RE006.md) | 一次请求跨多个服务很慢 |
| [RE007 · Cardinality; Metric labels](../concepts/RE007.md) | 监控费用暴涨、指标爆炸 |
| [RE008 · Tail latency; P95; P99](../concepts/RE008.md) | 平均很快但偶尔很慢 |
| [RE009 · Health check; Liveness; Readiness](../concepts/RE009.md) | 启动就接流量、反复重启 |
| [RE010 · Load shedding; Admission control](../concepts/RE010.md) | 过载拖垮全部请求 |
| [RE011 · Autoscaling; HPA; 弹性伸缩](../concepts/RE011.md) | 峰值自动扩容 |
| [RE012 · Container image; OCI; 镜像](../concepts/RE012.md) | 打包运行环境、镜像层 |
| [RE013 · Orchestration; Kubernetes; K8s](../concepts/RE013.md) | 容器调度、期望状态 |
| [RE014 · IaC; Infrastructure as code](../concepts/RE014.md) | 环境配置可重复 |
| [RE015 · GitOps; Reconciliation](../concepts/RE015.md) | Git 改配置自动部署 |
| [RE016 · Canary; Blue-green; 灰度与蓝绿](../concepts/RE016.md) | 新版本先给少量流量 |
| [RE017 · RTO; RPO; Recovery objectives](../concepts/RE017.md) | 多久恢复、能丢多久数据 |
| [RE018 · Backup restore drill; 恢复演练](../concepts/RE018.md) | 备份有了却恢复不了 |
| [RE019 · Chaos engineering; Fault injection](../concepts/RE019.md) | 模拟节点断网、故障演练 |
| [RE020 · Property-based testing; 性质测试](../concepts/RE020.md) | 边界组合太多、随机生成测试 |
| [RE021 · Fuzzing; 模糊测试](../concepts/RE021.md) | 解析器奇怪输入崩溃 |
| [RE022 · Model checking; 模型检查](../concepts/RE022.md) | 并发状态组合太多 |
| [RE023 · Formal verification; Hoare logic](../concepts/RE023.md) | 想证明关键不变量 |
| [RE024 · Contract testing; 契约测试](../concepts/RE024.md) | 接口升级破坏消费者 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为可靠性领域基线，将可用性和恢复概念落实为用户可见失败、容量边界与恢复证据。

### 关键特征

- 用用户操作的成功与延迟定义目标，不仅以进程存活判断服务健康。
- 容量、恢复和故障隔离分别分析，防护机制不能无依据增加重试与负载。
- 沿用现有观测与运维方式，指标阈值和可用性承诺需由需求或基线支持。

### 如何落实

- 定义本次关键操作、成功判定和已有目标，标出依赖及可接受的降级结果。
- 从实际失败和负载证据识别瓶颈，选择与根因对应的超时、限流或隔离调整。
- 若涉及恢复，明确恢复触发、数据状态及流量重新进入条件，不只安排重启。
- 用现有指标、日志或探针关联用户症状与依赖状态，保留能够支持处置的信号。

### 如何验收

- 在代表性负载和依赖失败时观察用户成功率与延迟，确认降级行为符合目标。
- 核对重试、排队和恢复期间的流量，确认不会持续放大故障或形成积压失控。
- 执行任务涉及的恢复路径，比较恢复耗时、数据完整性与功能可用结果。

### 常见误用

- 通过自动重启或增加副本掩盖状态损坏、资源泄漏和依赖瓶颈。
- 监控很多内部数值，却没有能关联用户失败和实际处置的证据。
