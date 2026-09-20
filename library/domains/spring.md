# Spring

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [SP001 · Spring Framework; Spring Boot; Spring ecosystem](../concepts/SP001.md) | Spring 和 Boot 有何区别 |
| [SP002 · IoC; DI; 控制反转; 依赖注入](../concepts/SP002.md) | 不想自己 new、替换实现 |
| [SP003 · Bean; BeanDefinition; ApplicationContext](../concepts/SP003.md) | 对象怎么进容器、Bean 找不到 |
| [SP004 · Component scan; Component/Service/Repository; Bean method](../concepts/SP004.md) | 自动扫描、配置类创建对象 |
| [SP005 · Constructor injection; Qualifier; Primary](../concepts/SP005.md) | 多个实现注入冲突 |
| [SP006 · Bean scope; Singleton; Prototype; Request scope](../concepts/SP006.md) | 每请求一个对象、单例安全吗 |
| [SP007 · Lifecycle callback; BeanPostProcessor; Lazy initialization](../concepts/SP007.md) | 初始化顺序、对象增强 |
| [SP008 · Configuration; Component proxying; Conditional bean](../concepts/SP008.md) | 条件装配、配置方法互调 |
| [SP009 · Auto-configuration; Starter; ConditionalOn](../concepts/SP009.md) | 为什么自动创建这个 Bean |
| [SP010 · ConfigurationProperties; Externalized configuration; Profile](../concepts/SP010.md) | 配置绑定、环境切换 |
| [SP011 · AOP; Advice; Pointcut; Join point; Proxy](../concepts/SP011.md) | 给方法统一日志/事务 |
| [SP012 · Self-invocation; 代理自调用](../concepts/SP012.md) | 同类调用事务失效 |
| [SP013 · Transactional; Transaction manager; 事务边界](../concepts/SP013.md) | 多步写库一起回滚 |
| [SP014 · Propagation; REQUIRED; REQUIRES_NEW; NESTED](../concepts/SP014.md) | 子方法开新事务、保存点 |
| [SP015 · Rollback rule; rollbackFor; UnexpectedRollbackException](../concepts/SP015.md) | 异常没回滚、被标记回滚 |
| [SP016 · Spring MVC; DispatcherServlet; Controller](../concepts/SP016.md) | HTTP 路由、控制器 |
| [SP017 · RequestMapping; PathVariable; RequestParam; RequestBody](../concepts/SP017.md) | 路径参数、查询参数、JSON 请求体 |
| [SP018 · Bean Validation; Valid; Validated; Constraint](../concepts/SP018.md) | 字段校验、校验分组 |
| [SP019 · ExceptionHandler; ControllerAdvice; ProblemDetail](../concepts/SP019.md) | 统一接口错误格式 |
| [SP020 · Filter; HandlerInterceptor; ArgumentResolver](../concepts/SP020.md) | 请求前后处理、自定义参数 |
| [SP021 · Spring Security; SecurityFilterChain; SecurityContext](../concepts/SP021.md) | 登录鉴权、接口保护 |
| [SP022 · Method security; PreAuthorize](../concepts/SP022.md) | 方法级权限、服务层鉴权 |
| [SP023 · Spring Data; Repository; Query derivation](../concepts/SP023.md) | 少写 CRUD、按方法名查询 |
| [SP024 · JdbcTemplate; JPA; MyBatis integration](../concepts/SP024.md) | JDBC 还是 ORM、手写 SQL |
| [SP025 · WebFlux; Reactor; Mono; Flux](../concepts/SP025.md) | 响应式接口、异步流 |
| [SP026 · WebClient; RestClient; HTTP client](../concepts/SP026.md) | 调另一个服务 |
| [SP027 · Async; TaskExecutor; Scheduled](../concepts/SP027.md) | 异步方法、定时任务 |
| [SP028 · ApplicationEvent; TransactionalEventListener](../concepts/SP028.md) | 业务事件、提交后通知 |
| [SP029 · Cacheable; CacheEvict; Cache abstraction](../concepts/SP029.md) | 方法结果缓存、更新后旧数据 |
| [SP030 · Actuator; Health indicator; Micrometer](../concepts/SP030.md) | 健康接口、运行指标 |
| [SP031 · SpringBootTest; Test slice; MockMvc; WebTestClient](../concepts/SP031.md) | 启动整应用测试、只测控制器 |
| [SP032 · AOT; Native image; Runtime hints](../concepts/SP032.md) | 原生镜像、启动变快 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 Spring 领域基线，将容器、请求和事务概念落实为实际装配关系与调用边界，按项目配置核对框架行为。

### 关键特征

- 注解只是声明入口，是否生效要结合对象来源、调用路径和运行配置判断。
- 业务事务、请求生命周期和外部副作用不能混为一个边界。
- 沿用项目已有的同步或响应式模型，不为局部功能无依据混接执行方式。

### 如何落实

- 定位相关对象由谁创建、如何注入和何时生效，核对配置条件及实际选中的实现。
- 追踪请求到业务与持久化的真实调用路径，标出校验、鉴权、代理和异常处理位置。
- 若涉及事务或异步行为，确认调用是否经过对应机制以及线程、提交和错误传播边界。
- 在现有层次内实现变更，为配置缺失、依赖失败及资源关闭安排与项目一致的处理。

### 如何验收

- 用实际应用配置启动受影响部分，确认目标对象与配置确实被装配。
- 通过真实入口触发成功、拒绝和异常路径，核对返回结果与数据库或外部状态。
- 对事务、代理或异步变更验证真实调用路径上的行为，而不只直接调用普通对象方法。

### 常见误用

- 仅凭注解存在就认定事务、权限或异步功能已经启用。
- 通过扩大扫描或自动装配范围修复单点问题，引入不明确的对象选择。
