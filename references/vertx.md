# Vert.x 与 Vertex 消歧

这里把 JVM 技术栈中的 Vert.x 单独列出，不认定用户写 Vertex 一定是拼写错误。
出现 VBO、顶点、GLSL 时读 [opengl.md](opengl.md) GL003；出现图论时读 [data-structures.md](data-structures.md) DT013；出现 Google Cloud/模型托管时查 Vertex AI 对应平台文档。来源 S45、S46，见 [sources.md](sources.md)。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| VX001 | Eclipse Vert.x; Vertx; JVM reactive toolkit | Java 事件驱动工具集、vertx 后端 | 在 JVM 上组织事件驱动与异步应用的工具集 | 不是图形学 Vertex，也不是云平台 Vertex AI |
| VX002 | Event loop; Multi-reactor; 事件循环 | 事件循环被卡住、blocked thread | 分配事件处理到循环线程以处理并发（S45） | 回调中阻塞 IO 或长计算会阻碍其他事件 |
| VX003 | Verticle; Deployment; Lifecycle | 部署单元、启动关闭 | 用运行单元封装组件及其生命周期 | Verticle 不等同操作系统进程或自动微服务边界 |
| VX004 | Context; Context affinity | 回调在哪个线程、上下文 | 以执行上下文组织回调及相关状态 | 不把某一版本/模式的线程行为推为全部情况 |
| VX005 | Worker verticle; executeBlocking | 老 JDBC、阻塞库怎么接 | 将必要阻塞工作交给适配的工作执行机制 | 工作池也有容量限制，不是无限并发通道 |
| VX006 | Future; Promise; compose; map; recover | 异步链、组合结果 | 用完成结果和组合操作连接异步步骤 | Vert.x Future 与 Java Future、JS Promise API 不同 |
| VX007 | Event bus; send; publish; request/reply | 模块发消息、一对多广播 | 在地址上组织点对点、发布及请求回复 | 不等于自动持久可靠的外部消息队列 |
| VX008 | Message codec; Delivery options; Timeout | 自定义消息、回复超时 | 指定消息编码及投递/等待参数 | 超时不证明接收方未执行，需要业务幂等 |
| VX009 | Router; Route; RoutingContext | Web 路由、中间件链 | 用匹配路由和上下文组成 HTTP 处理过程 | 阻塞处理、失败处理和响应结束需要明确 |
| VX010 | ReadStream; WriteStream; Backpressure; Pipe | 流量积压、写得比读快 | 暂停/恢复生产并按写入能力协调传输 | 不能把无限内存缓冲当背压 |
| VX011 | Reactive SQL client; Pool; Transaction | 异步查询数据库 | 以客户端协议和连接池执行异步数据库操作 | 异步等待不会消除数据库端锁与查询成本 |
| VX012 | Coroutine integration; coAwait; Suspend bridge | Kotlin 接 Vert.x Future | 通过适配库连接协程及异步结果 | suspend 仍不能在事件循环直接运行阻塞调用 |
| VX013 | Cluster manager; Clustered event bus | 多节点消息、集群发现 | 用指定集群机制连接节点及路由消息 | 不是共识数据库，投递和分区语义需独立核对 |
| VX014 | Vertex AI; Vertex; 云平台名称消歧 | Google Cloud、模型端点、训练部署 | 云 AI/ML 产品语境下的名称线索；使用时核对当前官方入口（S46） | 不据缩写把它纠正为 Vert.x；产品命名和能力可能变更 |
