# 设计模式

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [DP001 · Design pattern; 设计模式; GoF](../concepts/DP001.md) | 复用设计经验、结构命名 |
| [DP002 · Factory method; 工厂方法](../concepts/DP002.md) | 子类决定创建哪类对象 |
| [DP003 · Abstract factory; 抽象工厂](../concepts/DP003.md) | 一整套兼容产品实现 |
| [DP004 · Builder; 建造者](../concepts/DP004.md) | 多步骤构造、参数太多 |
| [DP005 · Prototype; 原型模式](../concepts/DP005.md) | 从模板对象克隆 |
| [DP006 · Singleton; 单例模式](../concepts/DP006.md) | 一个共享实例、全局管理器 |
| [DP007 · Adapter; 适配器](../concepts/DP007.md) | 接口不兼容、接旧系统 |
| [DP008 · Bridge; 桥接](../concepts/DP008.md) | 两个独立维度都要扩展 |
| [DP009 · Composite; 组合模式](../concepts/DP009.md) | 树形对象统一操作 |
| [DP010 · Decorator; 装饰器](../concepts/DP010.md) | 动态叠加日志压缩等能力 |
| [DP011 · Facade; 外观模式](../concepts/DP011.md) | 多个复杂接口统一入口 |
| [DP012 · Flyweight; 享元](../concepts/DP012.md) | 大量重复对象占内存 |
| [DP013 · Proxy; 代理模式](../concepts/DP013.md) | 延迟加载、控制访问、远程替身 |
| [DP014 · Chain of responsibility; 责任链](../concepts/DP014.md) | 逐层校验、过滤请求 |
| [DP015 · Command; 命令模式](../concepts/DP015.md) | 撤销重做、动作排队 |
| [DP016 · Interpreter; 解释器](../concepts/DP016.md) | 小规则语言、表达式求值 |
| [DP017 · Iterator; 迭代器模式](../concepts/DP017.md) | 不暴露存储结构地遍历 |
| [DP018 · Mediator; 中介者](../concepts/DP018.md) | 多对象互相引用太多 |
| [DP019 · Memento; 备忘录](../concepts/DP019.md) | 保存状态恢复、编辑器撤销 |
| [DP020 · Observer; 观察者模式](../concepts/DP020.md) | 状态变化通知多个订阅者 |
| [DP021 · State; 状态模式](../concepts/DP021.md) | 不同状态行为不同 |
| [DP022 · Strategy; 策略模式](../concepts/DP022.md) | 多种计价算法、替换寻路算法 |
| [DP023 · Template method; 模板方法](../concepts/DP023.md) | 流程固定部分步骤可换 |
| [DP024 · Visitor; 访问者](../concepts/DP024.md) | 稳定节点类型上添加多种操作 |
| [DP025 · SOLID; SRP; OCP; LSP; ISP; DIP](../concepts/DP025.md) | 职责过多、接口难替换 |
| [DP026 · Composition over inheritance; 组合优先](../concepts/DP026.md) | 继承层级爆炸 |
| [DP027 · Dependency inversion vs injection](../concepts/DP027.md) | 依赖倒置与注入区别 |
| [DP028 · Repository; Unit of work; 仓储/工作单元](../concepts/DP028.md) | 隔离持久化、汇总变更 |
| [DP029 · MVC; MVP; MVVM](../concepts/DP029.md) | 界面与业务分离 |
| [DP030 · Hexagonal architecture; Ports and adapters](../concepts/DP030.md) | 核心业务不依赖外部框架 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为设计模式领域基线，将模式候选还原为具体变化点和协作责任，不把模式名称作为必须实现的目标。

### 关键特征

- 先描述已有耦合或变化压力，再判断某种模式是否减少实际复杂度。
- 抽象边界应由真实替换点和调用关系支持，单一用途不自动需要接口层。
- 保持业务行为和对象生命周期明确，不能用模式包装隐藏副作用。

### 如何落实

- 列出当前难以修改的责任、受影响调用方和已经存在的变体，区分真实需求与假想扩展。
- 比较沿用现有结构、局部提取与引入模式的修改成本，选择最小可解释方案。
- 定义协作者的输入输出、创建责任及依赖方向，在现有命名与组织方式内落地。
- 若替换了分支或事件关系，保留原行为对照，并验证取消订阅、对象销毁等相关生命周期。

### 如何验收

- 用相同输入比较改造前后可观察行为，确认结构变更没有改变业务语义。
- 增加或替换一个已确认变体，核对修改是否确实集中在预期位置。
- 检查依赖关系、对象数量与生命周期，确认新增间接层没有制造循环或泄漏。

### 常见误用

- 为了命中模式名称建立接口、工厂和管理器，却没有真实变化点。
- 把继承或事件广播当作默认复用方式，隐藏状态与执行顺序依赖。
