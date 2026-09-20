# Vert.x 与 Vertex 消歧

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [VX001 · Eclipse Vert.x; Vertx; JVM reactive toolkit](../concepts/VX001.md) | Java 事件驱动工具集、vertx 后端 |
| [VX002 · Event loop; Multi-reactor; 事件循环](../concepts/VX002.md) | 事件循环被卡住、blocked thread |
| [VX003 · Verticle; Deployment; Lifecycle](../concepts/VX003.md) | 部署单元、启动关闭 |
| [VX004 · Context; Context affinity](../concepts/VX004.md) | 回调在哪个线程、上下文 |
| [VX005 · Worker verticle; executeBlocking](../concepts/VX005.md) | 老 JDBC、阻塞库怎么接 |
| [VX006 · Future; Promise; compose; map; recover](../concepts/VX006.md) | 异步链、组合结果 |
| [VX007 · Event bus; send; publish; request/reply](../concepts/VX007.md) | 模块发消息、一对多广播 |
| [VX008 · Message codec; Delivery options; Timeout](../concepts/VX008.md) | 自定义消息、回复超时 |
| [VX009 · Router; Route; RoutingContext](../concepts/VX009.md) | Web 路由、中间件链 |
| [VX010 · ReadStream; WriteStream; Backpressure; Pipe](../concepts/VX010.md) | 流量积压、写得比读快 |
| [VX011 · Reactive SQL client; Pool; Transaction](../concepts/VX011.md) | 异步查询数据库 |
| [VX012 · Coroutine integration; coAwait; Suspend bridge](../concepts/VX012.md) | Kotlin 接 Vert.x Future |
| [VX013 · Cluster manager; Clustered event bus](../concepts/VX013.md) | 多节点消息、集群发现 |
| [VX014 · Vertex AI; Vertex; 云平台名称消歧](../concepts/VX014.md) | Google Cloud、模型端点、训练部署 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 Vert.x 领域基线，将事件驱动概念落实为上下文、异步完成和生命周期责任，先排除 Vertex 的其他含义。

### 关键特征

- 先确认任务指向 Vert.x，再依据项目依赖核对使用方式。
- 每段工作需要明确执行上下文与阻塞性质，不把异步返回当作内部没有阻塞。
- 消息交付、处理完成和业务副作用成功分别定义，失败与关闭路径同样需要完成信号。

### 如何落实

- 画出请求、回调及消息的实际流向，标明状态所有者和可能共享的可变数据。
- 识别阻塞或长计算段，按现有执行设施安排位置，并核对切换上下文后的状态访问方式。
- 为异步链约定成功、失败、超时和取消处理，任务涉及消息时明确回复与重复处理语义。
- 将消费者、计时器、连接和待完成任务纳入部署与停止流程，定义停止接收和释放的顺序。

### 如何验收

- 在代表性负载下观察回调延迟与执行上下文，确认关键事件处理不会被长任务拖住。
- 注入超时和处理异常，核对调用方得到一次明确终态且相关资源被释放。
- 重复部署与停止，确认没有遗留消费者、计时器或悬空请求。

### 常见误用

- 把工作包装成异步接口就认定不会阻塞事件处理。
- 将消息已发送等同于业务已提交，忽略超时后可能继续发生的副作用。
