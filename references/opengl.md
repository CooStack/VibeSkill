# OpenGL 与 GPU 接口

检索分组：上下文与管线、几何数据、着色器接口、纹理、帧缓冲、同步与诊断。
图形学原理见 [graphics.md](graphics.md)，数学见 [mathematics.md](mathematics.md)，资产制作见 [modeling.md](modeling.md)。来源 S49、S50，见 [sources.md](sources.md)。使用前确认 OpenGL/OpenGL ES/WebGL、核心/兼容配置、版本与扩展；不在引擎封装之外擅自修改共享 GL 状态。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| GL001 | OpenGL; OpenGL ES; WebGL; Context; Profile | GL 环境、核心模式、移动端图形 | 区分 API 家族、当前上下文及功能配置 | 桌面 OpenGL 调用不一定能用于 ES 或 WebGL |
| GL002 | State machine; Binding; DSA | GL 状态串了、绑定对象 | 状态式 API 通过当前绑定或直接对象操作配置资源 | DSA 可用性依版本/扩展；仍需管理生命周期和上下文 |
| GL003 | Vertex; 顶点; Vertex attribute | Vertex 数据、位置颜色 UV | GPU 输入顶点通常是一组位置及其他属性，不只是一个坐标点 | 同一空间点因法线/UV 不同可能需要多个渲染顶点 |
| GL004 | VBO; Buffer object; Vertex buffer | 顶点上传、显存缓冲 | 用缓冲对象存放供 GPU 使用的数据 | VBO 是常见用途名，不等于所有 Buffer 只能放顶点 |
| GL005 | VAO; Vertex array object; Attribute layout | 绑定了 VBO 却画不出、顶点格式 | 保存顶点输入状态及相关缓冲引用（S49） | VAO 不复制顶点内容；索引缓冲绑定也有 VAO 关联 |
| GL006 | glVertexAttribPointer; Stride; Offset; Integer attribute | 顶点错位、颜色乱、整型属性 | 描述分量类型、步长和偏移来解释缓冲字节 | 整型输入和转换型输入需匹配相应 API，字节布局不能猜 |
| GL007 | EBO; Index buffer; Indexed draw | 复用顶点、索引绘制 | 用索引序列引用顶点并减少重复输入 | 索引类型、偏移与范围必须匹配实际缓冲 |
| GL008 | Primitive; Topology; Triangle strip; Winding | 三角形连接、背面被剔除 | 指定顶点如何组合成图元及正反面方向 | 此处 topology 不等同建模中的完整网格布线质量 |
| GL009 | Instancing; Divisor; Instance attribute | 大量相同模型 | 一次提交多个实例并按实例读取差异数据 | 不自动降低单个实例的像素着色或透明过绘 |
| GL010 | Draw call; Multi-draw; Indirect draw | 提交开销、GPU 驱动绘制 | 区分 CPU 直接提交与缓冲中存储绘制参数 | 间接绘制能力和同步规则需核对版本 |
| GL011 | Shader; GLSL; Shader stage | 写着色器、GPU 小程序 | 使用阶段专用程序处理几何、片元或计算工作 | shader 不只是“加光影滤镜”，各阶段可用输入不同 |
| GL012 | Shader compilation; Program linking; Info log | 着色器编译失败、接口不匹配 | 编译阶段程序并链接可共同执行的程序接口 | 编译通过不保证链接或运行期资源绑定正确 |
| GL013 | Vertex shader; 顶点着色器 | 顶点变形、模型投影 | 处理输入顶点并输出裁剪坐标及插值数据 | 写 gl_Position 时要遵守裁剪空间约定 |
| GL014 | Fragment shader; 片元着色器 | 逐像素颜色、材质计算 | 为光栅化产生的片元计算输出 | 片元不严格等于最终显示像素，可能被测试丢弃或多采样 |
| GL015 | Geometry/Tessellation shader | 扩展图元、曲面细分 | 在支持的管线阶段生成图元或细化曲面 | 性能与平台支持不同，不默认优于其他几何方案 |
| GL016 | Compute shader; Workgroup; Invocation | GPU 并行计算、粒子更新 | 以工作组和调用组织通用计算 | 不是所有目标 API 都支持；需显式处理数据竞争和同步 |
| GL017 | Uniform; Uniform location | 每帧传矩阵、参数不更新 | 向程序提供一次绘制中共享的参数 | 未使用参数可能被优化掉；位置与具体链接程序关联 |
| GL018 | UBO; SSBO; std140; std430 | 批量参数、CPU GPU 结构对不上 | 用接口块共享常量或可读写存储并遵守布局规则 | 对齐、填充和可用布局依缓冲类别/版本而定 |
| GL019 | Varying; in/out; flat/smooth/noperspective | 顶点色插值、整数传片元 | 在阶段之间声明数据并控制插值方式 | 默认平滑插值不等于简单屏幕线性插值 |
| GL020 | Sampler; Texture unit; Image unit | 多张贴图、采样器绑定错 | 区分纹理采样绑定与图像读写绑定 | sampler uniform 的整数通常指定纹理单元，不是纹理对象 ID |
| GL021 | Texture target; 2D/3D/Cubemap/Array texture | 立方体环境图、体积纹理、纹理数组 | 按维度和寻址方式选择纹理资源 | array 层与 3D 深度插值语义不同 |
| GL022 | Internal format; Upload format/type; Pixel unpack alignment | 纹理颜色错、上传行错位 | 区分 GPU 存储格式、源数据解释与行对齐 | 通道数相同不代表类型、色彩空间或精度相同 |
| GL023 | Texture filtering; Mipmap; Wrap mode | 远处闪、边缘重复、拉伸 | 配置多级采样、插值和坐标越界行为 | 需要 mip 的过滤配置必须与实际级别数据相符 |
| GL024 | sRGB texture; Linear framebuffer; FRAMEBUFFER_SRGB | 画面太暗、伽马叠加 | 让颜色纹理与目标在适当阶段进行线性/编码转换 | 法线、粗糙度等数据纹理不按颜色一律解码 |
| GL025 | FBO; Framebuffer; Attachment; Completeness | 离屏渲染、画到纹理、黑屏 | 将颜色/深度等附件组合为渲染目标并验证完整性 | 绑定 FBO 不自动设置匹配的 viewport |
| GL026 | Renderbuffer; MRT; Blit | 多目标输出、深度附件、拷贝目标 | 分别提供附件存储、多渲染目标输出和传输操作 | renderbuffer 不当普通纹理直接采样，格式约束需匹配 |
| GL027 | Viewport; Scissor; Clear | 渲染区域错、只清一块 | 分别配置坐标映射、裁剪区域和缓冲清除 | scissor 及写掩码可能影响清除结果 |
| GL028 | Depth test; Depth write; Depth function | 物体遮挡错、透明挡住后面 | 区分深度比较与是否写回深度 | 关闭深度写入不等于关闭深度测试 |
| GL029 | Stencil test; Stencil operation | 轮廓遮罩、限定绘制区域 | 用模板缓冲及比较/更新规则控制片元通过 | 模板不是任意精度颜色缓冲 |
| GL030 | Blending; Blend factors; Premultiplied alpha | 半透明黑边、加法特效 | 按源/目标因子混合输出 | 预乘与直通 alpha 需匹配，普通透明往往依赖绘制顺序 |
| GL031 | MSAA; Multisample resolve | 几何边缘抗锯齿、解析多采样 | 多采样目标随后按规则解析成可显示/采样结果 | 不自动消除材质、时间或着色混叠 |
| GL032 | Memory barrier; Fence; Sync object | GPU 数据下一步读到旧值 | 内存屏障控制相应访问可见性；栅栏表达完成同步（S50） | glMemoryBarrier 不是让 CPU 等待所有 GPU 工作完成 |
| GL033 | Buffer streaming; Orphaning; Persistent mapping | 动态顶点每帧更新卡顿 | 选择存储替换或映射策略避免读写互相等待 | 持久映射仍需遵守同步及可见性约束 |
| GL034 | PBO; Readback; Pipeline stall | 截图或读像素导致卡顿 | 用传输缓冲与延迟消费减轻同步回读影响 | 异步传输后立刻等待仍可能造成停顿 |
| GL035 | Debug context; KHR_debug; GPU capture | GL 黑屏、不知道哪次调用错 | 结合调试消息、状态与帧捕获定位问题 | 扩展和工具支持需核对，不能只靠 glGetError 判断画面正确 |
| GL036 | Resource lifetime; Context loss; State restoration | 切场景显存泄露、引擎渲染被破坏 | 对齐 GPU 资源创建、释放、上下文与引擎状态所有权 | 不在无正确上下文的线程直接销毁/操作资源 |
