# OpenGL 与 GPU 接口

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [GL001 · OpenGL; OpenGL ES; WebGL; Context; Profile](../concepts/GL001.md) | GL 环境、核心模式、移动端图形 |
| [GL002 · State machine; Binding; DSA](../concepts/GL002.md) | GL 状态串了、绑定对象 |
| [GL003 · Vertex; 顶点; Vertex attribute](../concepts/GL003.md) | Vertex 数据、位置颜色 UV |
| [GL004 · VBO; Buffer object; Vertex buffer](../concepts/GL004.md) | 顶点上传、显存缓冲 |
| [GL005 · VAO; Vertex array object; Attribute layout](../concepts/GL005.md) | 绑定了 VBO 却画不出、顶点格式 |
| [GL006 · glVertexAttribPointer; Stride; Offset; Integer attribute](../concepts/GL006.md) | 顶点错位、颜色乱、整型属性 |
| [GL007 · EBO; Index buffer; Indexed draw](../concepts/GL007.md) | 复用顶点、索引绘制 |
| [GL008 · Primitive; Topology; Triangle strip; Winding](../concepts/GL008.md) | 三角形连接、背面被剔除 |
| [GL009 · Instancing; Divisor; Instance attribute](../concepts/GL009.md) | 大量相同模型 |
| [GL010 · Draw call; Multi-draw; Indirect draw](../concepts/GL010.md) | 提交开销、GPU 驱动绘制 |
| [GL011 · Shader; GLSL; Shader stage](../concepts/GL011.md) | 写着色器、GPU 小程序 |
| [GL012 · Shader compilation; Program linking; Info log](../concepts/GL012.md) | 着色器编译失败、接口不匹配 |
| [GL013 · Vertex shader; 顶点着色器](../concepts/GL013.md) | 顶点变形、模型投影 |
| [GL014 · Fragment shader; 片元着色器](../concepts/GL014.md) | 逐像素颜色、材质计算 |
| [GL015 · Geometry/Tessellation shader](../concepts/GL015.md) | 扩展图元、曲面细分 |
| [GL016 · Compute shader; Workgroup; Invocation](../concepts/GL016.md) | GPU 并行计算、粒子更新 |
| [GL017 · Uniform; Uniform location](../concepts/GL017.md) | 每帧传矩阵、参数不更新 |
| [GL018 · UBO; SSBO; std140; std430](../concepts/GL018.md) | 批量参数、CPU GPU 结构对不上 |
| [GL019 · Varying; in/out; flat/smooth/noperspective](../concepts/GL019.md) | 顶点色插值、整数传片元 |
| [GL020 · Sampler; Texture unit; Image unit](../concepts/GL020.md) | 多张贴图、采样器绑定错 |
| [GL021 · Texture target; 2D/3D/Cubemap/Array texture](../concepts/GL021.md) | 立方体环境图、体积纹理、纹理数组 |
| [GL022 · Internal format; Upload format/type; Pixel unpack alignment](../concepts/GL022.md) | 纹理颜色错、上传行错位 |
| [GL023 · Texture filtering; Mipmap; Wrap mode](../concepts/GL023.md) | 远处闪、边缘重复、拉伸 |
| [GL024 · sRGB texture; Linear framebuffer; FRAMEBUFFER_SRGB](../concepts/GL024.md) | 画面太暗、伽马叠加 |
| [GL025 · FBO; Framebuffer; Attachment; Completeness](../concepts/GL025.md) | 离屏渲染、画到纹理、黑屏 |
| [GL026 · Renderbuffer; MRT; Blit](../concepts/GL026.md) | 多目标输出、深度附件、拷贝目标 |
| [GL027 · Viewport; Scissor; Clear](../concepts/GL027.md) | 渲染区域错、只清一块 |
| [GL028 · Depth test; Depth write; Depth function](../concepts/GL028.md) | 物体遮挡错、透明挡住后面 |
| [GL029 · Stencil test; Stencil operation](../concepts/GL029.md) | 轮廓遮罩、限定绘制区域 |
| [GL030 · Blending; Blend factors; Premultiplied alpha](../concepts/GL030.md) | 半透明黑边、加法特效 |
| [GL031 · MSAA; Multisample resolve](../concepts/GL031.md) | 几何边缘抗锯齿、解析多采样 |
| [GL032 · Memory barrier; Fence; Sync object](../concepts/GL032.md) | GPU 数据下一步读到旧值 |
| [GL033 · Buffer streaming; Orphaning; Persistent mapping](../concepts/GL033.md) | 动态顶点每帧更新卡顿 |
| [GL034 · PBO; Readback; Pipeline stall](../concepts/GL034.md) | 截图或读像素导致卡顿 |
| [GL035 · Debug context; KHR_debug; GPU capture](../concepts/GL035.md) | GL 黑屏、不知道哪次调用错 |
| [GL036 · Resource lifetime; Context loss; State restoration](../concepts/GL036.md) | 切场景显存泄露、引擎渲染被破坏 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为 OpenGL 领域基线，将渲染概念落实为上下文、资源与状态所有权，以及 GPU 读写顺序的可验证约定。

### 关键特征

- 每个资源和可变图形状态应有明确拥有者，创建、使用及释放必须处于项目允许的上下文。
- 区分命令提交顺序、内存可见性与执行完成，按真实资源访问关系选择同步机制。
- 只使用项目目标环境支持且已核对的能力，不以 API 名称或经验假定版本行为。

### 如何落实

- 列出相关缓冲、纹理、程序和渲染目标的创建者、使用阶段、读写用途及销毁时机。
- 为绘制或计算阶段记录输入布局、绑定关系和会修改的状态，按现有约定交接或恢复状态。
- 追踪 CPU 与 GPU 以及 GPU 各阶段对同一资源的生产和消费，核对复用、映射和读取前的同步要求。
- 先用可辨认的最小数据验证管线，再接回真实资产；在项目已有调试设施中保留阶段与资源标识。

### 如何验收

- 检查输出像素及已知几何或颜色样本，并结合可用的调试输出定位无效状态或资源配置。
- 交错运行其他渲染阶段并重复调整尺寸或重建资源，确认状态不会污染相邻绘制且资源可正确释放。
- 对资源快速更新、重复复用和读取结果施压，核对访问同步依据及输出；不以偶尔画面对了作为同步正确的证明。

### 常见误用

- 用全局等待掩盖所有同步问题，或把内存可见性处理误当作 GPU 已完成的证明。
- 依赖外部阶段碰巧留下的绑定状态，或在资源仍被访问时回收复用。
