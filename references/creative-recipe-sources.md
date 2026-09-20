# Creative Recipes 来源与核查边界

核查日期：2026-09-20。

本次仅新增 `creative-recipes.json` 与本记录，不修改已有表、技能实施规则、脚本或生成页。JSON 的 200 条指南按现有稳定 ID 编写，覆盖 GM、DS、AR、MD、MC、GL、CG、MA 各 25 条，不涉及 DL、AU 或音效制作。它们是将本地概念转化为实施与验收的作者指南，不是官方文档逐条翻译，也不声称 200 条均有独立外部验证。

## 使用边界

- 现有项目规范、引擎约定和专门 Skill 优先；这里不授权改技术栈、添加依赖或覆盖实施流程。
- Minecraft 实施前仍须查实际游戏版本、加载器及版本、映射、JDK、物理侧与逻辑侧。下列文档只验证所列机制，不承诺示例类名或方法签名在其他版本可用。
- OpenGL 实施前仍须查桌面 GL、ES 或 WebGL 家族、配置、版本及扩展，并服从引擎的资源与状态所有权。gl4 参考页不是所有图形 API 的通用契约。
- 数学条目假定写明的定义域、单位、空间和数值前提；不构成完整证明。容差和预算必须由任务尺度确定。
- 设计、美术、建模中的比例、层级和观察方法是可用于验证的制作建议，不把审美经验写成普适定律或用户已经要求的风格。

## 本次实际读取

网页工具对两次官方页面打开未返回可用正文，因此改用 HTTP 读取并提取以下段落。HTTP 获取成功不等于整本手册或所有关联 API 已核验。

| 一手资料入口 | 实际读取内容 | 对应核查边界 |
| --- | --- | --- |
| [Khronos glVertexAttribPointer](https://registry.khronos.org/OpenGL-Refpages/gl4/html/glVertexAttribPointer.xhtml) | Description 与参数中的字节步长、偏移、整数保留或转换、归一化、当前缓冲关联及属性启用 | 支持 GL005/GL006 的布局机制；未逐个验证所有类型在各版本的支持矩阵 |
| [Khronos glMemoryBarrier](https://registry.khronos.org/OpenGL-Refpages/gl4/html/glMemoryBarrier.xhtml) | Description 及顶点、索引、纹理读取、图像访问、间接命令等 barrier 位说明 | 支持 GL032 与 CG046 中按消费访问选择可见性的原则；未运行驱动或核验具体工程同步实现 |
| [Blender Render Baking](https://docs.blender.org/manual/en/latest/render/cycles/baking.html) | Setup、Selected to Active、Cage、Max Ray Distance、Output 与 Margin 段落 | 支持 MD027/MD030 的 UV 目标、投射范围、笼体与边缘扩展；latest 为移动入口，不锁定项目 Blender 版本 |
| [NeoForge Sides](https://docs.neoforged.net/docs/concepts/sides/) | Physical Side、Logical Side 及单人/多人区别 | 支持 MC011/MC012 的双端与类加载边界；不据此宣称 Fabric、Forge 或各历史版本入口相同 |
| [Fabric Block Entities](https://docs.fabricmc.net/develop/blocks/block-entities) | Saving and Loading Data、Syncing Data、Tickers 相关正文和示例 | 支持 MC022/MC048 的保存、初始状态及持续同步区别；未将页面中的 ValueInput 等具体签名写成通用承诺 |
| [SciPy bisect](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html) | 连续性、端点异号、xtol/rtol 与最大迭代及收敛结果说明 | 支持 MA030 的求根前提和停止条件；JSON 不固定库版本、默认容差或要求安装 SciPy |
| [SciPy solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) | ODE 输入、初始条件、显式/刚性方法选择、误差控制及事件跨步遗漏说明 | 支持 MA026 的求解器选择与内部步长区别；未对任意动力系统做稳定性保证 |
| [PBRT 4 Sampling Multidimensional Functions](https://pbr-book.org/4ed/Sampling_Algorithms/Sampling_Multidimensional_Functions) | A.5.2 半球/球面均匀采样的 PDF、测度与角度分布推导片段 | 核查 MA037 中不能直接均匀采纬角的原因；未逐项运行书中实现或验证本库所有概率条目 |
| [PBRT 4 Transmittance](https://pbr-book.org/4ed/Volume_Scattering/Transmittance) | 消光、路径透射定义及均匀介质 Beer 定律 | 支持 CG044 的长度单位、光学厚度及步长依赖；未验证完整非均匀介质或多次散射实现 |

## 仅确认入口

[Godot Physics Introduction](https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html) 的 HTTP 返回了页面与导航目录。本次关键词提取落在目录而非所需物理过程正文，因此不将固定步长、CCD 或具体回调规则记为本次官方正文已核验。GM 条目保持引擎无关，并要求使用项目现有物理与导航实现。

## 本地核查范围

本次读取 `references/game.md`、`design.md`、`art.md`、`modeling.md`、`minecraft.md`、`opengl.md`、`graphics.md`、`mathematics.md` 作为 ID 与概念边界依据，并读取现有 `SKILL.md`、来源维护规则及相关技能写作约束。完成时检查 JSON 可解析、键无重复、ID 属于上述原表、字段集合严格一致及数组为 1-3 个非空字符串。此结构校验不等同引擎运行、视觉资产制作或数值实现测试。
