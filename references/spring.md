# Spring

检索分组：容器与装配、配置、Web、事务与数据、安全、异步与测试。
基础入口保留 [java.md](java.md) JV040-JV043；这里细分机制。来源 S31、S44，见 [sources.md](sources.md)。先确认 Spring Framework/Boot 版本及 Servlet/Reactive 栈。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| SP001 | Spring Framework; Spring Boot; Spring ecosystem | Spring 和 Boot 有何区别 | Framework 提供基础框架，Boot 提供应用配置与运行整合 | 不能把所有 Spring 项目都当同一发布版本 |
| SP002 | IoC; DI; 控制反转; 依赖注入 | 不想自己 new、替换实现 | 将依赖构建与业务使用分离，由外部提供协作者 | 注入不自动消除循环依赖或不良职责边界 |
| SP003 | Bean; BeanDefinition; ApplicationContext | 对象怎么进容器、Bean 找不到 | 定义受容器管理的对象及其创建元信息 | 普通手工 new 的对象不自动拥有容器服务 |
| SP004 | Component scan; Component/Service/Repository; Bean method | 自动扫描、配置类创建对象 | 用扫描或显式工厂方法注册容器对象 | 扫描范围和条件不符会导致未注册 |
| SP005 | Constructor injection; Qualifier; Primary | 多个实现注入冲突 | 通过构造参数明确依赖并选择候选 | 不靠任意命名掩盖职责不清或重复实现 |
| SP006 | Bean scope; Singleton; Prototype; Request scope | 每请求一个对象、单例安全吗 | 按容器及请求等范围控制对象生命周期 | Spring singleton 通常以容器为范围，且不自动线程安全 |
| SP007 | Lifecycle callback; BeanPostProcessor; Lazy initialization | 初始化顺序、对象增强 | 在创建与销毁阶段配置、包装或延迟创建 | 初始化阶段不宜假定所有代理已具备运行期行为 |
| SP008 | Configuration; Component proxying; Conditional bean | 条件装配、配置方法互调 | 按配置和条件决定 Bean 结构 | 配置代理模式影响方法互调语义，需看实际注解设置 |
| SP009 | Auto-configuration; Starter; ConditionalOn | 为什么自动创建这个 Bean | Boot 根据类路径、属性和已有 Bean 等条件装配 | starter 是依赖整合，不等于单一自动配置类 |
| SP010 | ConfigurationProperties; Externalized configuration; Profile | 配置绑定、环境切换 | 将外部配置结构化绑定并按环境选择配置 | 优先级和校验需要确认，不向客户端或日志泄露密钥 |
| SP011 | AOP; Advice; Pointcut; Join point; Proxy | 给方法统一日志/事务 | 在明确连接点通过通知实施横切行为 | Spring 代理 AOP 与任意字节码织入能力不同 |
| SP012 | Self-invocation; 代理自调用 | 同类调用事务失效 | 默认代理模式下内部 this 调用不穿过外部代理（S44） | 换代理类型不自动解决所有自调用问题 |
| SP013 | Transactional; Transaction manager; 事务边界 | 多步写库一起回滚 | 由事务管理器协调适配资源并应用事务规则 | 不能自动原子覆盖任意外部 HTTP 服务 |
| SP014 | Propagation; REQUIRED; REQUIRES_NEW; NESTED | 子方法开新事务、保存点 | 声明事务调用与外层事务的参与关系 | NESTED 支持依管理器；新事务可能额外占用连接 |
| SP015 | Rollback rule; rollbackFor; UnexpectedRollbackException | 异常没回滚、被标记回滚 | 根据异常和传播状态决定提交或回滚 | 默认规则及全局配置依版本，捕获异常不自动恢复事务 |
| SP016 | Spring MVC; DispatcherServlet; Controller | HTTP 路由、控制器 | 在 Servlet 栈分派请求、绑定输入并产生响应 | 不等同 WebFlux 的反应式执行模型 |
| SP017 | RequestMapping; PathVariable; RequestParam; RequestBody | 路径参数、查询参数、JSON 请求体 | 从不同请求位置绑定输入到处理参数 | 输入校验和权限验证仍需显式设计 |
| SP018 | Bean Validation; Valid; Validated; Constraint | 字段校验、校验分组 | 用约束及校验入口验证对象或方法输入 | 注解存在不保证每个路径都触发校验 |
| SP019 | ExceptionHandler; ControllerAdvice; ProblemDetail | 统一接口错误格式 | 在 Web 边界转换异常为一致响应 | 不把内部堆栈和敏感细节直接暴露给客户端 |
| SP020 | Filter; HandlerInterceptor; ArgumentResolver | 请求前后处理、自定义参数 | Servlet 过滤、MVC 拦截和参数解析位于不同处理阶段 | 不能用简单日志拦截器代替完整安全链 |
| SP021 | Spring Security; SecurityFilterChain; SecurityContext | 登录鉴权、接口保护 | 通过安全链建立身份及访问决策上下文 | 默认行为、CSRF 和会话策略依应用类型配置 |
| SP022 | Method security; PreAuthorize | 方法级权限、服务层鉴权 | 在受支持的调用边界检查授权表达式 | 需启用相应支持并注意代理调用路径 |
| SP023 | Spring Data; Repository; Query derivation | 少写 CRUD、按方法名查询 | 由数据模块生成仓储实现或声明查询 | 仓储抽象不消除 SQL 计划、事务及 N+1 |
| SP024 | JdbcTemplate; JPA; MyBatis integration | JDBC 还是 ORM、手写 SQL | 区分 JDBC 辅助、ORM 规范及 SQL 映射整合 | MyBatis 不是 Spring Framework 核心实现 |
| SP025 | WebFlux; Reactor; Mono; Flux | 响应式接口、异步流 | 使用反应式类型组织异步处理和流式结果 | 返回 Mono 不自动把阻塞数据库调用变非阻塞 |
| SP026 | WebClient; RestClient; HTTP client | 调另一个服务 | 按反应式或同步调用模型选择客户端 | 超时、连接池、重试与错误映射仍需设计 |
| SP027 | Async; TaskExecutor; Scheduled | 异步方法、定时任务 | 通过执行器或调度器管理后台工作 | 自调用、上下文传播和关闭生命周期需核对 |
| SP028 | ApplicationEvent; TransactionalEventListener | 业务事件、提交后通知 | 在进程内传播事件并可关联事务阶段 | 本地事件不是持久消息队列，不自动保证可靠投递 |
| SP029 | Cacheable; CacheEvict; Cache abstraction | 方法结果缓存、更新后旧数据 | 通过缓存键和失效规则复用结果 | 代理边界、并发穿透及一致性策略不能忽略 |
| SP030 | Actuator; Health indicator; Micrometer | 健康接口、运行指标 | 提供应用运维观测与健康信息整合 | 管理端点暴露范围和敏感内容应受控制 |
| SP031 | SpringBootTest; Test slice; MockMvc; WebTestClient | 启动整应用测试、只测控制器 | 按验证边界加载完整或裁剪上下文 | mock HTTP 测试不等于真实网络及部署验证 |
| SP032 | AOT; Native image; Runtime hints | 原生镜像、启动变快 | 提前处理部分配置并支持原生编译 | 反射、动态代理和资源发现可能需要显式描述 |
