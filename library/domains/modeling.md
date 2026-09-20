# 三维建模

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [MD001 · Mesh; Vertex; Edge; Face](../concepts/MD001.md) | 点线面、网格模型 |
| [MD002 · Topology; Edge flow; 拓扑/布线](../concepts/MD002.md) | 布线乱、关节变形差 |
| [MD003 · Quad; Triangle; N-gon; Pole](../concepts/MD003.md) | 四边面、三角面、多边面 |
| [MD004 · Manifold; Non-manifold; Watertight](../concepts/MD004.md) | 模型漏、打印失败、破面 |
| [MD005 · Normal; Winding; Backface culling](../concepts/MD005.md) | 面翻了、背面消失 |
| [MD006 · Smooth/Flat shading; Split normals; Hard edge](../concepts/MD006.md) | 表面有棱、黑斑、平滑 |
| [MD007 · Weighted normals](../concepts/MD007.md) | 硬表面大平面发波 |
| [MD008 · Transform; Local/World space; Pivot/Origin](../concepts/MD008.md) | 旋转中心不对、轴向错 |
| [MD009 · Units; Scale; Handedness; Up axis](../concepts/MD009.md) | 导出太大、模型躺倒 |
| [MD010 · Extrude; Inset; Bevel; 倒角](../concepts/MD010.md) | 拉伸、内插、边缘太锋利 |
| [MD011 · Boolean; 布尔](../concepts/MD011.md) | 挖洞、并集差集 |
| [MD012 · Subdivision surface; Support loop; Crease](../concepts/MD012.md) | 细分后塌、保持硬边 |
| [MD013 · Modifier stack; 非破坏建模](../concepts/MD013.md) | 修改可回头、步骤可调 |
| [MD014 · Mirror; Symmetry; Array](../concepts/MD014.md) | 左右对称、重复结构 |
| [MD015 · Sculpting; Dyntopo; Multires](../concepts/MD015.md) | 雕刻、细节塑形 |
| [MD016 · Retopology; 重拓扑](../concepts/MD016.md) | 高模转可动画低模 |
| [MD017 · Remesh; Voxel remesh](../concepts/MD017.md) | 网格分布乱、融合雕刻 |
| [MD018 · Decimation; Simplification](../concepts/MD018.md) | 减面、移动端优化 |
| [MD019 · High poly; Low poly](../concepts/MD019.md) | 高模烘低模、面数预算 |
| [MD020 · Hard-surface; Organic modeling](../concepts/MD020.md) | 机械建模、生物建模 |
| [MD021 · Curve; NURBS; B-rep; CAD](../concepts/MD021.md) | 精确曲面、工业模型 |
| [MD022 · Procedural modeling; Geometry nodes](../concepts/MD022.md) | 参数化生成、批量变体 |
| [MD023 · Kitbash; Modular kit; 模块化资产](../concepts/MD023.md) | 拼建筑、复用零件 |
| [MD024 · UV; Unwrap; Seam; Island](../concepts/MD024.md) | 展 UV、贴图拉伸、切缝 |
| [MD025 · UV distortion; Checker map](../concepts/MD025.md) | 棋盘格变形、纹理拉长 |
| [MD026 · Texel density; 纹素密度](../concepts/MD026.md) | 有的模型清楚有的糊 |
| [MD027 · UV packing; Padding; Dilation](../concepts/MD027.md) | UV 利用率、远处串色 |
| [MD028 · UV overlap; Mirrored UV](../concepts/MD028.md) | 共用纹理、左右一样 |
| [MD029 · UDIM](../concepts/MD029.md) | 多张大贴图、影视资产 |
| [MD030 · Baking; Cage; Ray distance](../concepts/MD030.md) | 高模细节烘贴图、烘焙穿帮 |
| [MD031 · Tangent/Object-space normal map](../concepts/MD031.md) | 法线贴图接缝、凹凸反了 |
| [MD032 · Bump; Displacement; Height map](../concepts/MD032.md) | 表面凹凸、轮廓也要变化 |
| [MD033 · AO/Curvature/ID bake](../concepts/MD033.md) | 智能材质、边缘磨损遮罩 |
| [MD034 · Lightmap UV; Baked lighting](../concepts/MD034.md) | 烘焙光照接缝 |
| [MD035 · Rig; Skeleton; Bone; Joint](../concepts/MD035.md) | 给角色装骨骼 |
| [MD036 · Skinning; Weight painting; 蒙皮](../concepts/MD036.md) | 关节塌、顶点跟错骨骼 |
| [MD037 · Bind pose; Rest pose](../concepts/MD037.md) | 动画导入炸开、初始姿态 |
| [MD038 · FK; IK; Forward/Inverse kinematics](../concepts/MD038.md) | 手够到目标、脚固定地面 |
| [MD039 · Constraint; Driver](../concepts/MD039.md) | 自动跟随、参数联动 |
| [MD040 · Blendshape; Morph target; Shape key](../concepts/MD040.md) | 表情、口型、形变 |
| [MD041 · Retargeting; 动画重定向](../concepts/MD041.md) | 不同角色共用动作 |
| [MD042 · Animation baking; 动画烘焙](../concepts/MD042.md) | 约束动画导出不动 |
| [MD043 · Cloth; Soft body; Rigid body simulation](../concepts/MD043.md) | 衣服模拟、软体、碎块 |
| [MD044 · LOD; Proxy; Impostor](../concepts/MD044.md) | 远处简化、预览替身 |
| [MD045 · Triangulation; Export validation](../concepts/MD045.md) | 引擎里阴影变了 |
| [MD046 · glTF; FBX; USD; 资产交换](../concepts/MD046.md) | 导出模型、跨软件协作 |
| [MD047 · Instancing; Linked duplicate](../concepts/MD047.md) | 多个对象共用网格 |
| [MD048 · Material slot; Shader graph; Texture set](../concepts/MD048.md) | 多材质、节点材质 |
| [MD049 · Mipmap; Texture filtering; Anisotropic](../concepts/MD049.md) | 远处纹理闪、斜面糊 |
| [MD050 · Path tracing; Samples; Denoising](../concepts/MD050.md) | 离线渲染噪点、渲染时间 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为建模领域基线，将三维资产概念落实为几何、坐标、表面与导入结果的对应约定。

### 关键特征

- 资产用途决定几何精度与拓扑需求，静态展示和变形动画分别判断。
- 明确单位、轴向、原点和变换约定，使制作端与消费端解释一致。
- 面数、材质槽和贴图预算依据目标场景确定，不凭模型类型编造限制。

### 如何落实

- 确定目标尺寸、朝向、原点及轮廓参考，先用基础形体核对比例和使用空间。
- 按可见轮廓与实际变形部位分配几何，检查连接、法线方向和不期望的重叠面。
- 若涉及贴图或烘焙，安排 UV 接缝、密度与边距；若涉及骨骼，明确绑定姿态和权重责任。
- 用项目实际导入链验证导出资产，核对变换、材质、法线以及任务涉及的骨骼或动画。

### 如何验收

- 在目标场景中对照已知尺寸核对比例、朝向、原点和包围范围。
- 从实际观察角度检查轮廓与光照接缝，变形资产在代表性姿态下检查拉伸和穿插。
- 比较导出前后材质、UV 和几何结果，并核对约定的资源预算。

### 常见误用

- 只在制作软件里确认外观，遗漏导入后的单位或法线解释差异。
- 把增加面数当作所有质量问题的修复，忽略轮廓、拓扑或烘焙来源。
