# 构建、依赖与技术栈工具链

检索分组：JVM 构建、包管理、模块解析、Web 构建、交付验证。
语言参考：[Java](java.md)、[Kotlin](kotlin.md)、[JS](javascript.md)、[TS](typescript.md)、[Vue](vue.md)。来源 S30-S34、S39-S42，见 [sources.md](sources.md)。品牌名仅用于定位其负责的能力，不将工具名当架构要求。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| TL001 | Build tool; Gradle; Maven | 项目如何构建、构建自动化 | 组织依赖解析、编译、测试和产物生成 | 工具版本、插件版本与 JDK 是不同兼容轴 |
| TL002 | Gradle Wrapper; Maven Wrapper | 别人电脑能跑、构建版本一致 | 项目封装并固定所需构建工具入口 | wrapper 不自动固定全部外部依赖 |
| TL003 | Gradle task; DAG; Maven phase/goal | 编译先后顺序、生命周期阶段 | 任务图或生命周期目标定义工作关系 | Maven 阶段与 Gradle task 不一一对应 |
| TL004 | Groovy DSL; Kotlin DSL; build.gradle.kts | 构建脚本是 Kotlin 吗 | 用特定 DSL 配置构建模型 | Kotlin DSL 脚本不代表应用源代码必须用 Kotlin |
| TL005 | Source set; Module; Multi-project build | main/test、公共模块、拆子项目 | 划分源码、编译配置和项目依赖边界 | 构建模块不同于 JPMS 模块或游戏维度 |
| TL006 | Toolchain; source/target compatibility; jvmTarget | 编译 JDK 和运行 JDK 不同 | 控制使用的工具和目标字节码/API 约束 | javac release 与只设置 target 的保障不同 |
| TL007 | Dependency scope/configuration; api/implementation; compileOnly/runtimeOnly | 编译有库运行没库、依赖泄露 | 区分编译、运行及公开依赖边界 | Gradle 配置与 Maven scope 不能机械互换 |
| TL008 | Dependency coordinates; Repository; Transitive dependency | group/artifact/version、间接依赖 | 从仓库解析直接和传递依赖 | 依赖仓库不等同 Git 源码仓库 |
| TL009 | BOM; Platform; Version catalog | 多库版本对齐、libs.versions.toml | 分别通过约束平台或集中别名/版本声明治理依赖 | version catalog 不自动强制所有传递依赖一致 |
| TL010 | Dependency resolution; Conflict; Constraint; Locking | 同一库两个版本、锁依赖 | 定义冲突选择并记录解析结果 | 强行固定版本可能违反下游二进制兼容 |
| TL011 | Shading; Relocation; Fat/Uber JAR | 打包依赖、同名库冲突 | 聚合依赖并可重定位名称空间 | 服务资源、反射和许可证也可能受影响 |
| TL012 | Build cache; Incremental build; Configuration cache | 构建太慢、缓存结果错误 | 复用任务输出、变化分析或配置结果 | 三种缓存不同，输入声明及插件兼容很重要 |
| TL013 | KSP; kapt; Annotation processor | Kotlin 自动生成、处理器兼容 | KSP 面向 Kotlin 符号，kapt 衔接 Java 注解处理生态 | 处理器通常不能无修改在两者间互换 |
| TL014 | Node.js; Runtime; npm script | 前端为什么装 Node、执行脚本 | Node 提供 JS 宿主环境，包脚本组织命令 | 浏览器 API 与 Node API 并非相同集合 |
| TL015 | npm; pnpm; Yarn; Package manager | 安装依赖、node_modules 布局 | 解析包、维护依赖图和安装产物 | 不随意混用多个管理器及锁文件 |
| TL016 | package.json; dependencies; devDependencies; peerDependencies | 插件依赖宿主、生产少依赖 | 声明运行、开发或对使用方的兼容要求 | 最终部署需要哪些包由构建和运行模式决定 |
| TL017 | Lockfile; Reproducible install; Frozen/CI install | 同版本装出不同东西 | 锁定具体解析图并按约束重现安装 | 平台条件、运行时与外部脚本仍影响结果 |
| TL018 | SemVer; Version range; Prerelease | 升级小版本坏了、范围符号 | 用版本语义及范围表达兼容意图 | 不是对所有包实际行为的绝对保证 |
| TL019 | Workspace; Monorepo; Local package | 多包共仓、共用组件库 | 管理相关包的本地链接及构建关系 | 共仓不表示全部模块必须一起发布 |
| TL020 | Module resolution; exports; imports; Alias | 开发能导入生产找不到 | 连接声明的导入路径与真实可加载资源 | TS paths、Vite alias 与运行时解析需协调 |
| TL021 | Vite; Dev server; Production build | 开发秒开、生产打包 | 工具在开发与生产阶段采用相应处理流程 | 不把开发成功当生产构建和部署成功 |
| TL022 | HMR; Hot module replacement | 热更新、保存后不刷新整页 | 替换部分模块并按边界保留或重建状态 | 热更新状态不保证与完整重载一致 |
| TL023 | Bundler; Rollup; webpack; esbuild; Rolldown | 打包器、依赖图、产物切块 | 工具实现模块图处理与产物生成 | Vite 内部所用工具依版本核对，不硬编码为永恒架构 |
| TL024 | Transpiler; Babel; SWC; Type stripping | 语法能编译但类型没查 | 转换语法或擦除类型以生成可执行代码 | 转译不等于类型检查，也不自动补全部运行时 API |
| TL025 | Polyfill; Browserslist; Compatibility target | 旧浏览器 API 不存在 | 依据支持目标补足部分运行时能力 | 语法转换和 API polyfill 是不同步骤 |
| TL026 | Environment variable; .env; Build-time replacement | 环境变量泄露、线上没更新 | 区分构建时注入与服务器运行时读取 | 打进前端产物的值不能作为秘密 |
| TL027 | Lint; ESLint; Formatter; Prettier | 代码规范、格式检查 | 静态规则检查与排版格式化分别处理不同问题 | 不替代类型检查、测试和安全审查 |
| TL028 | Vitest; JUnit; Playwright; Test runner | 单元测试、浏览器流程测试 | 用适合执行环境的工具验证行为 | 测试运行器、断言库与浏览器自动化各有职责 |
