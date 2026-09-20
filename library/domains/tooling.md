# 构建与工具链

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [TL001 · Build tool; Gradle; Maven](../concepts/TL001.md) | 项目如何构建、构建自动化 |
| [TL002 · Gradle Wrapper; Maven Wrapper](../concepts/TL002.md) | 别人电脑能跑、构建版本一致 |
| [TL003 · Gradle task; DAG; Maven phase/goal](../concepts/TL003.md) | 编译先后顺序、生命周期阶段 |
| [TL004 · Groovy DSL; Kotlin DSL; build.gradle.kts](../concepts/TL004.md) | 构建脚本是 Kotlin 吗 |
| [TL005 · Source set; Module; Multi-project build](../concepts/TL005.md) | main/test、公共模块、拆子项目 |
| [TL006 · Toolchain; source/target compatibility; jvmTarget](../concepts/TL006.md) | 编译 JDK 和运行 JDK 不同 |
| [TL007 · Dependency scope/configuration; api/implementation; compileOnly/runtimeOnly](../concepts/TL007.md) | 编译有库运行没库、依赖泄露 |
| [TL008 · Dependency coordinates; Repository; Transitive dependency](../concepts/TL008.md) | group/artifact/version、间接依赖 |
| [TL009 · BOM; Platform; Version catalog](../concepts/TL009.md) | 多库版本对齐、libs.versions.toml |
| [TL010 · Dependency resolution; Conflict; Constraint; Locking](../concepts/TL010.md) | 同一库两个版本、锁依赖 |
| [TL011 · Shading; Relocation; Fat/Uber JAR](../concepts/TL011.md) | 打包依赖、同名库冲突 |
| [TL012 · Build cache; Incremental build; Configuration cache](../concepts/TL012.md) | 构建太慢、缓存结果错误 |
| [TL013 · KSP; kapt; Annotation processor](../concepts/TL013.md) | Kotlin 自动生成、处理器兼容 |
| [TL014 · Node.js; Runtime; npm script](../concepts/TL014.md) | 前端为什么装 Node、执行脚本 |
| [TL015 · npm; pnpm; Yarn; Package manager](../concepts/TL015.md) | 安装依赖、node_modules 布局 |
| [TL016 · package.json; dependencies; devDependencies; peerDependencies](../concepts/TL016.md) | 插件依赖宿主、生产少依赖 |
| [TL017 · Lockfile; Reproducible install; Frozen/CI install](../concepts/TL017.md) | 同版本装出不同东西 |
| [TL018 · SemVer; Version range; Prerelease](../concepts/TL018.md) | 升级小版本坏了、范围符号 |
| [TL019 · Workspace; Monorepo; Local package](../concepts/TL019.md) | 多包共仓、共用组件库 |
| [TL020 · Module resolution; exports; imports; Alias](../concepts/TL020.md) | 开发能导入生产找不到 |
| [TL021 · Vite; Dev server; Production build](../concepts/TL021.md) | 开发秒开、生产打包 |
| [TL022 · HMR; Hot module replacement](../concepts/TL022.md) | 热更新、保存后不刷新整页 |
| [TL023 · Bundler; Rollup; webpack; esbuild; Rolldown](../concepts/TL023.md) | 打包器、依赖图、产物切块 |
| [TL024 · Transpiler; Babel; SWC; Type stripping](../concepts/TL024.md) | 语法能编译但类型没查 |
| [TL025 · Polyfill; Browserslist; Compatibility target](../concepts/TL025.md) | 旧浏览器 API 不存在 |
| [TL026 · Environment variable; .env; Build-time replacement](../concepts/TL026.md) | 环境变量泄露、线上没更新 |
| [TL027 · Lint; ESLint; Formatter; Prettier](../concepts/TL027.md) | 代码规范、格式检查 |
| [TL028 · Vitest; JUnit; Playwright; Test runner](../concepts/TL028.md) | 单元测试、浏览器流程测试 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为构建与工具链领域基线，将依赖和产物概念落实为可复现输入、任务关系与实际运行结果。

### 关键特征

- 区分源码、生成物、缓存和发布产物，修改其各自的真实来源。
- 依赖声明、解析结果和运行时加载结果需要分别核对。
- 遵循项目固定的工具链及锁定策略，不把排障变成全量升级或清空环境。

### 如何落实

- 识别项目入口、工具版本来源、锁定文件及目标任务，明确当前失败发生在解析、编译、打包还是运行阶段。
- 追踪涉及的依赖和任务输入输出，确认生成步骤与消费者之间的依赖关系。
- 在最小范围调整配置或声明，保留环境差异与解析结果的证据，不直接编辑缓存中的副本。
- 执行受影响任务并检查产物内容，在隔离输出或已有复现方式下比较冷构建与增量构建结果。

### 如何验收

- 核对实际解析的依赖及工具版本与项目约定一致，没有未解释的重复或替换。
- 修改相关输入后重建，确认产物更新；输入未变时确认增量行为符合任务定义。
- 从构建产物启动或加载目标功能，确认必需资源和运行依赖确实被打包。

### 常见误用

- 反复清缓存掩盖任务依赖或生成顺序错误，却没有形成可复现诊断。
- 只看到编译成功就宣告交付，遗漏产物内容与运行环境。
