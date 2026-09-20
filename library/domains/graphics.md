# 计算机图形学与特效

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [CG001 · Rendering pipeline; 渲染管线](../concepts/CG001.md) | 模型怎样变成屏幕图像 |
| [CG002 · Rasterization; Ray tracing; Path tracing](../concepts/CG002.md) | 光栅化还是光追 |
| [CG003 · Local/World/View/Clip/NDC/Screen space](../concepts/CG003.md) | 坐标变换、屏幕位置不对 |
| [CG004 · Model/View/Projection matrix; MVP](../concepts/CG004.md) | 模型相机投影矩阵 |
| [CG005 · Perspective divide; Homogeneous clipping](../concepts/CG005.md) | w 分量、近处大远处小 |
| [CG006 · Orthographic/Perspective projection; FOV](../concepts/CG006.md) | 正交相机、视野角度 |
| [CG007 · View frustum; Near/Far plane](../concepts/CG007.md) | 近裁剪、远处消失 |
| [CG008 · Depth precision; Z-fighting; Reversed-Z](../concepts/CG008.md) | 共面闪烁、深度精度 |
| [CG009 · Back-face/Frustum/Occlusion culling](../concepts/CG009.md) | 不可见东西别画 |
| [CG010 · Barycentric coordinate; Attribute interpolation](../concepts/CG010.md) | 三角形内部点、UV 插值 |
| [CG011 · Visibility; Coverage; Fragment; Sample](../concepts/CG011.md) | 一个像素多个片元 |
| [CG012 · Sampling; Reconstruction; Aliasing; Nyquist](../concepts/CG012.md) | 锯齿、摩尔纹、纹理闪 |
| [CG013 · Temporal reprojection; Motion vector; History buffer](../concepts/CG013.md) | TAA 拖影、复用上一帧 |
| [CG014 · Mesh; Vertex/index data; Submesh](../concepts/CG014.md) | 模型拆材质、多部分网格 |
| [CG015 · Surface normal; Tangent; Bitangent; TBN](../concepts/CG015.md) | 法线贴图方向不对 |
| [CG016 · Normal matrix; Inverse transpose](../concepts/CG016.md) | 缩放后光照变形 |
| [CG017 · Skinning; Bone matrix palette; Dual quaternion skinning](../concepts/CG017.md) | 骨骼模型扭曲、糖纸效应 |
| [CG018 · Morph target; Blend shape; Vertex animation](../concepts/CG018.md) | 表情、顶点动画 |
| [CG019 · BRDF; BSDF; BTDF](../concepts/CG019.md) | 材质如何反射透射 |
| [CG020 · Rendering equation; 光照传输](../concepts/CG020.md) | 间接光从哪来 |
| [CG021 · Radiance; Irradiance; Radiometry](../concepts/CG021.md) | 光的单位、入射能量 |
| [CG022 · Microfacet; Fresnel; Energy conservation](../concepts/CG022.md) | 金属反光、掠射角反射 |
| [CG023 · Metallic/roughness; Specular/glossiness](../concepts/CG023.md) | PBR 工作流转换 |
| [CG024 · IBL; Environment map; Importance sampling](../concepts/CG024.md) | 环境光照、HDR 天空反射 |
| [CG025 · Shadow map; PCF; Shadow acne; Bias](../concepts/CG025.md) | 阴影锯齿、漂浮、痤疮 |
| [CG026 · Global illumination; Ambient occlusion](../concepts/CG026.md) | 反弹光、角落接触阴影 |
| [CG027 · UV; Texture coordinates; Texture atlas](../concepts/CG027.md) | 贴图定位、合图 |
| [CG028 · Texel; Pixel; Texel density](../concepts/CG028.md) | 纹素像素区别、局部贴图糊 |
| [CG029 · Bilinear/Trilinear/Anisotropic filtering](../concepts/CG029.md) | 斜地面糊、缩小闪 |
| [CG030 · Texture compression; BC/ETC/ASTC](../concepts/CG030.md) | 贴图显存大、压缩伪影 |
| [CG031 · Virtual texturing; Sparse texture; Residency](../concepts/CG031.md) | 超大贴图、按需纹理页 |
| [CG032 · Normal/Bump/Displacement mapping](../concepts/CG032.md) | 凹凸不改轮廓、真实位移 |
| [CG033 · Parallax mapping; Parallax occlusion](../concepts/CG033.md) | 平面纹理有深度感 |
| [CG034 · HDR; Exposure; Tone mapping; Color management](../concepts/CG034.md) | 高亮过曝、显示一致 |
| [CG035 · Bloom; DOF; Motion blur; Post-processing](../concepts/CG035.md) | 发光晕、景深、运动模糊 |
| [CG036 · Render graph; Render pass; Resource dependency](../concepts/CG036.md) | 多遍渲染、临时目标管理 |
| [CG037 · Particle emitter; Spawn rate; Lifetime](../concepts/CG037.md) | 发射器、粒子出生和消亡 |
| [CG038 · Billboard; Sprite sheet; Flipbook](../concepts/CG038.md) | 粒子始终朝镜头、序列帧特效 |
| [CG039 · Trail; Ribbon; Beam](../concepts/CG039.md) | 拖尾、丝带、激光束 |
| [CG040 · Soft particle; Depth fade; 软粒子; 深度淡出](../concepts/CG040.md) | 烟雾穿地硬边 |
| [CG041 · Distortion; Refraction; Flow map](../concepts/CG041.md) | 热浪扭曲、水面折射 |
| [CG042 · Noise; Curl noise; Domain warping](../concepts/CG042.md) | 云雾、随机流动、湍流感 |
| [CG043 · SDF; Signed distance field; Ray marching](../concepts/CG043.md) | 距离场轮廓、程序化形状 |
| [CG044 · Volume rendering; Ray integration; Beer-Lambert](../concepts/CG044.md) | 体积雾、光束、吸收 |
| [CG045 · OIT; Weighted blended transparency; Sorting](../concepts/CG045.md) | 透明层排序错、烟雾混合 |
| [CG046 · GPU particles; Simulation buffer; Ping-pong](../concepts/CG046.md) | 大量粒子模拟、双缓冲更新 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为计算机图形学领域基线，将几何、采样和光照概念落实为坐标、信号与图像结果，不限定图形 API。

### 关键特征

- 每次变换都标明输入输出空间、单位和方向约定。
- 区分几何误差、采样误差和色彩处理问题，用可控制的场景定位来源。
- 视觉近似与性能取舍以任务目标为准，不默认追求物理精确或增加渲染阶段。

### 如何落实

- 写清数据从模型或场景到最终像素的路径，标注坐标空间、矩阵约定与颜色编码边界。
- 构造已知朝向、尺度和颜色的参考场景，逐段验证变换、可见性及法线等相关数据。
- 按问题选择采样、混合或光照处理，明确精度、分辨率和时间历史的使用条件。
- 将效果接入现有渲染流程，分别记录图像差异与时间或内存成本，保留任务需要的开关对照。

### 如何验收

- 用轴向、已知距离与正反面样本核对变换、裁剪及方向关系。
- 改变视角、尺度和分辨率，检查边缘、透明区域与细节是否出现未约定伪影。
- 与参考图或简化参考实现比较结果，并在相同场景下核对资源成本。

### 常见误用

- 混用坐标空间、角度单位或颜色编码，再通过经验系数补偿。
- 只比较一张静态截图，遗漏运动、采样和视角变化造成的不稳定。
