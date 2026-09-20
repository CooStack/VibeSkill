# 计算机图形学、模型、纹理与特效

检索分组：变换与可见性、采样、几何、材质光照、纹理、后期与特效。
OpenGL 机制见 [opengl.md](opengl.md)，数学见 [mathematics.md](mathematics.md)，制作流程见 [art.md](art.md) / [modeling.md](modeling.md)。来源 S05、S16、S51、S52，见 [sources.md](sources.md)。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| CG001 | Rendering pipeline; 渲染管线 | 模型怎样变成屏幕图像 | 将几何、变换、可见性、着色及显示组合成处理过程 | API 管线与引擎渲染框架的阶段划分不必完全相同 |
| CG002 | Rasterization; Ray tracing; Path tracing | 光栅化还是光追 | 分别通过投影覆盖或追踪射线/光路估计可见性及光照 | 可混合使用，不是简单“快与真实”的二分 |
| CG003 | Local/World/View/Clip/NDC/Screen space | 坐标变换、屏幕位置不对 | 区分对象、场景、相机、裁剪、归一化和屏幕空间 | 每个向量和矩阵应注明来源/目标空间 |
| CG004 | Model/View/Projection matrix; MVP | 模型相机投影矩阵 | 将对象空间位置逐步映射到裁剪空间 | 乘法顺序依行/列向量约定，不能背固定顺序乱套 |
| CG005 | Perspective divide; Homogeneous clipping | w 分量、近处大远处小 | 在适当裁剪后以齐次分量归一化投影坐标 | 透视除法前后空间语义不同 |
| CG006 | Orthographic/Perspective projection; FOV | 正交相机、视野角度 | 选择平行或透视投影来控制空间映射 | FOV 是水平还是垂直需确认，不能忽略宽高比 |
| CG007 | View frustum; Near/Far plane | 近裁剪、远处消失 | 限定相机可见体积并影响深度分布 | 裁剪平面与物理碰撞不是一回事 |
| CG008 | Depth precision; Z-fighting; Reversed-Z | 共面闪烁、深度精度 | 处理有限深度表示和投影分布引起的遮挡误差 | reversed-Z 依 API/投影/格式，不是只改深度比较函数 |
| CG009 | Back-face/Frustum/Occlusion culling | 不可见东西别画 | 分别按面朝向、视锥和遮挡减少工作 | 剔除包围范围需涵盖实际变形/特效 |
| CG010 | Barycentric coordinate; Attribute interpolation | 三角形内部点、UV 插值 | 用相对顶点权重表达位置与属性 | 屏幕空间线性权重需与透视正确插值区分 |
| CG011 | Visibility; Coverage; Fragment; Sample | 一个像素多个片元 | 区分是否被看见、覆盖比例及采样位置 | 片元着色不意味着一定写入最终像素 |
| CG012 | Sampling; Reconstruction; Aliasing; Nyquist | 锯齿、摩尔纹、纹理闪 | 有限采样需要匹配信号频率和重建滤波 | 增加分辨率不是唯一解，空间与时间混叠要分开 |
| CG013 | Temporal reprojection; Motion vector; History buffer | TAA 拖影、复用上一帧 | 用运动信息将历史样本映射到当前帧 | 遮挡变化、错误运动向量和历史失效会造成伪影 |
| CG014 | Mesh; Vertex/index data; Submesh | 模型拆材质、多部分网格 | 用顶点、索引和分组描述可绘制几何 | 模型资产还可能含骨骼、材质和动画，不只是网格 |
| CG015 | Surface normal; Tangent; Bitangent; TBN | 法线贴图方向不对 | 构造表面局部方向基以解释切线空间数据 | 镜像 UV、切线手性和非均匀缩放都影响结果 |
| CG016 | Normal matrix; Inverse transpose | 缩放后光照变形 | 用适配变换保持法线与变换后切面正交 | 通常使用相应线性变换逆转置；奇异变换不可直接求逆 |
| CG017 | Skinning; Bone matrix palette; Dual quaternion skinning | 骨骼模型扭曲、糖纸效应 | 以骨骼变换和权重驱动几何形变 | 线性混合与双四元数适用变换及限制不同 |
| CG018 | Morph target; Blend shape; Vertex animation | 表情、顶点动画 | 用顶点目标或缓存轨迹描述变形 | 需保持兼容的顶点对应关系 |
| CG019 | BRDF; BSDF; BTDF | 材质如何反射透射 | 描述表面散射在方向之间的响应 | 材质函数与入射光、可见性和几何项共同决定结果 |
| CG020 | Rendering equation; 光照传输 | 间接光从哪来 | 用自发光及入射光散射积分描述出射辐射 | 通常要近似或数值估计，不能只用一个局部公式解决全部场景 |
| CG021 | Radiance; Irradiance; Radiometry | 光的单位、入射能量 | 区分方向性辐亮度与单位面积辐照度 | 不与感知亮度或 UI 颜色值混作同一物理量 |
| CG022 | Microfacet; Fresnel; Energy conservation | 金属反光、掠射角反射 | 微表面模型及角度相关反射约束材质响应 | 物理模型参数不同于任意艺术调色值 |
| CG023 | Metallic/roughness; Specular/glossiness | PBR 工作流转换 | 用不同参数组织材质的漫反射/镜面行为 | 粗糙度与光泽度转换及纹理通道需确认规范 |
| CG024 | IBL; Environment map; Importance sampling | 环境光照、HDR 天空反射 | 利用环境辐射分布估计材质受光 | 环境背景图不自动提供正确的预滤波照明 |
| CG025 | Shadow map; PCF; Shadow acne; Bias | 阴影锯齿、漂浮、痤疮 | 从光源视角比较深度并过滤或调整偏差 | 偏差是权衡，不可无限加大掩盖错误 |
| CG026 | Global illumination; Ambient occlusion | 反弹光、角落接触阴影 | GI 考虑间接传输，AO 估计局部遮蔽 | AO 不是完整全局光照解 |
| CG027 | UV; Texture coordinates; Texture atlas | 贴图定位、合图 | 参数坐标连接表面与纹理域，图集打包多块内容 | 坐标接缝、留边与 mip 共同影响可见接缝 |
| CG028 | Texel; Pixel; Texel density | 纹素像素区别、局部贴图糊 | 区分纹理采样格、输出图像格及单位表面纹理密度 | 贴图文件变大不保证模型每处都有足够纹素 |
| CG029 | Bilinear/Trilinear/Anisotropic filtering | 斜地面糊、缩小闪 | 分别在级内、级间或各向异性足迹上过滤 | 三线性过滤不是三维纹理独有机制 |
| CG030 | Texture compression; BC/ETC/ASTC | 贴图显存大、压缩伪影 | 用 GPU 支持的块格式减少带宽和存储 | PNG/JPEG 文件压缩不等于 GPU 纹理压缩 |
| CG031 | Virtual texturing; Sparse texture; Residency | 超大贴图、按需纹理页 | 用分页/驻留策略管理超出常驻预算的资源 | 缺页反馈和低级别回退是实现的一部分 |
| CG032 | Normal/Bump/Displacement mapping | 凹凸不改轮廓、真实位移 | 区分改变着色方向与改变实际几何 | 法线图通常不能直接当高度场使用 |
| CG033 | Parallax mapping; Parallax occlusion | 平面纹理有深度感 | 通过视角相关坐标偏移近似表面深度 | 多数实现不产生完整几何轮廓或真实碰撞 |
| CG034 | HDR; Exposure; Tone mapping; Color management | 高亮过曝、显示一致 | 区分工作动态范围、曝光、显示映射及色彩转换 | 调色 LUT 不能代替正确的线性色彩计算 |
| CG035 | Bloom; DOF; Motion blur; Post-processing | 发光晕、景深、运动模糊 | 在渲染结果或中间数据上构造镜头/视觉效果 | 需考虑时序、遮挡、交互可读性与性能 |
| CG036 | Render graph; Render pass; Resource dependency | 多遍渲染、临时目标管理 | 描述各渲染步骤及读写依赖来组织资源与执行 | 引擎 render graph 不等于某 API 的单个 render pass |
| CG037 | Particle emitter; Spawn rate; Lifetime | 发射器、粒子出生和消亡 | 通过生成、更新和回收阶段定义粒子系统 | 改发射率与延长寿命都会改变同时存活数量 |
| CG038 | Billboard; Sprite sheet; Flipbook | 粒子始终朝镜头、序列帧特效 | 用朝向和纹理帧模拟细节丰富的二维特效 | 朝向轴、帧插值与透明排序需设计 |
| CG039 | Trail; Ribbon; Beam | 拖尾、丝带、激光束 | 按历史轨迹或控制点构造连续带状几何 | 点间距离、转角与断段会影响宽度和稳定性 |
| CG040 | Soft particle; Depth fade; 软粒子; 深度淡出 | 烟雾穿地硬边 | 比较粒子与场景深度来衰减交界透明度 | 深度比较须同空间，不能代替实体碰撞 |
| CG041 | Distortion; Refraction; Flow map | 热浪扭曲、水面折射 | 通过偏移采样或折射计算表现介质/流动 | 屏幕空间扭曲不具备完整场景外信息 |
| CG042 | Noise; Curl noise; Domain warping | 云雾、随机流动、湍流感 | 用结构化噪声及坐标扭曲构造连贯变化 | 看起来像流体不意味着满足完整流体物理 |
| CG043 | SDF; Signed distance field; Ray marching | 距离场轮廓、程序化形状 | 用到边界的有符号距离组织隐式几何和步进 | 任意函数不一定是真实距离，步长过大可能漏面 |
| CG044 | Volume rendering; Ray integration; Beer-Lambert | 体积雾、光束、吸收 | 沿路径积分介质散射和透射衰减 | 简单均匀介质近似不等于所有非均匀多次散射 |
| CG045 | OIT; Weighted blended transparency; Sorting | 透明层排序错、烟雾混合 | 用排序或次序无关近似解决透明组合 | 加权 OIT 是近似，不能假定与精确逐层混合一致 |
| CG046 | GPU particles; Simulation buffer; Ping-pong | 大量粒子模拟、双缓冲更新 | 将状态更新放到 GPU 并交替读写资源 | 绘制与模拟同步、缓冲容量和回读成本仍需处理 |
