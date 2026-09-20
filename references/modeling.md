# 三维建模与资产管线概念

检索分组：几何与拓扑、建模方法、UV 与烘焙、绑定动画、管线与渲染。
相邻领域：[美术](art.md)、[游戏](game.md)。来源入口：S05、S16、S17，见 [sources.md](sources.md)。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| MD001 | Mesh; Vertex; Edge; Face | 点线面、网格模型 | 用顶点、边、面描述离散表面 | 与 CAD 实体及体积表示不同 |
| MD002 | Topology; Edge flow; 拓扑/布线 | 布线乱、关节变形差 | 组织连接关系以支持形状与变形 | 不是面数越多越好 |
| MD003 | Quad; Triangle; N-gon; Pole | 四边面、三角面、多边面 | 描述面边数与顶点连接结构 | 四边面并非所有用途的硬性要求 |
| MD004 | Manifold; Non-manifold; Watertight | 模型漏、打印失败、破面 | 检查局部连接合法性及闭合性 | 闭合、流形与无自交不是同义 |
| MD005 | Normal; Winding; Backface culling | 面翻了、背面消失 | 用方向及顶点顺序确定朝向和可见性 | 双面材质不修复错误拓扑 |
| MD006 | Smooth/Flat shading; Split normals; Hard edge | 表面有棱、黑斑、平滑 | 控制法线插值与分裂以改变光照外观 | 平滑着色不会增加几何细节 |
| MD007 | Weighted normals | 硬表面大平面发波 | 按面贡献调整顶点法线 | 不能替代所有倒角或合理几何 |
| MD008 | Transform; Local/World space; Pivot/Origin | 旋转中心不对、轴向错 | 区分对象变换、坐标空间和操作中心 | 应用变换可能影响绑定及修改器 |
| MD009 | Units; Scale; Handedness; Up axis | 导出太大、模型躺倒 | 统一单位、坐标手性与竖直方向 | 缩放外观不等于统一真实单位 |
| MD010 | Extrude; Inset; Bevel; 倒角 | 拉伸、内插、边缘太锋利 | 基础面体扩展与边缘处理 | 倒角宽度需符合尺度和拓扑 |
| MD011 | Boolean; 布尔 | 挖洞、并集差集 | 对形体进行体积式集合操作 | 结果可能需要清理以满足变形或细分 |
| MD012 | Subdivision surface; Support loop; Crease | 细分后塌、保持硬边 | 通过细分规则和约束产生平滑曲面 | 不等同于简单增加三角面数 |
| MD013 | Modifier stack; 非破坏建模 | 修改可回头、步骤可调 | 用可调操作链生成结果 | 堆栈顺序影响结果及导出 |
| MD014 | Mirror; Symmetry; Array | 左右对称、重复结构 | 基于规则复用建模操作 | 留意镜像法线、中心缝和最终差异 |
| MD015 | Sculpting; Dyntopo; Multires | 雕刻、细节塑形 | 自由塑形并按方式增加局部或层级细节 | 雕刻网格通常不是直接交付的最终拓扑 |
| MD016 | Retopology; 重拓扑 | 高模转可动画低模 | 为既有形体重新建立适合使用的拓扑 | 与只减面数的简化不同 |
| MD017 | Remesh; Voxel remesh | 网格分布乱、融合雕刻 | 按新采样重建表面连接 | 可能损失细节、UV 和已有拓扑 |
| MD018 | Decimation; Simplification | 减面、移动端优化 | 在误差约束下减少几何复杂度 | 需检查轮廓、法线、UV 和变形 |
| MD019 | High poly; Low poly | 高模烘低模、面数预算 | 按资产目的相对区分细节层级 | 无统一适用所有项目的面数阈值 |
| MD020 | Hard-surface; Organic modeling | 机械建模、生物建模 | 分别偏重工程式结构或柔性自然形态 | 可混合使用多种建模方法 |
| MD021 | Curve; NURBS; B-rep; CAD | 精确曲面、工业模型 | 使用参数曲线、曲面或边界实体表示 | 转网格会引入离散精度和拓扑问题 |
| MD022 | Procedural modeling; Geometry nodes | 参数化生成、批量变体 | 用规则图或程序生成几何 | 程序复杂度也需要维护与验证 |
| MD023 | Kitbash; Modular kit; 模块化资产 | 拼建筑、复用零件 | 用可组合资产快速构造场景 | 统一尺度、枢轴、接口与材质密度 |
| MD024 | UV; Unwrap; Seam; Island | 展 UV、贴图拉伸、切缝 | 把表面映射到纹理坐标空间 | UV 坐标与真实表面积不天然成比例 |
| MD025 | UV distortion; Checker map | 棋盘格变形、纹理拉长 | 检查展开的角度及面积失真 | 低失真与少接缝之间有取舍 |
| MD026 | Texel density; 纹素密度 | 有的模型清楚有的糊 | 控制单位世界尺寸对应的纹素数 | 与整张贴图分辨率不同 |
| MD027 | UV packing; Padding; Dilation | UV 利用率、远处串色 | 布局岛屿并为过滤及 mip 留空间 | 紧贴排布会造成边缘渗色 |
| MD028 | UV overlap; Mirrored UV | 共用纹理、左右一样 | 复用纹理区域降低存储需求 | 唯一烘焙或光照 UV 常有不同约束 |
| MD029 | UDIM | 多张大贴图、影视资产 | 用编号 UV 瓦片组织多贴图区域 | 目标渲染器或引擎支持需核对 |
| MD030 | Baking; Cage; Ray distance | 高模细节烘贴图、烘焙穿帮 | 投射高模信息到低模参数域 | 投射距离、交叠、命名隔离影响正确性 |
| MD031 | Tangent/Object-space normal map | 法线贴图接缝、凹凸反了 | 在切线或对象空间编码方向 | 切线基、三角化和通道约定需一致 |
| MD032 | Bump; Displacement; Height map | 表面凹凸、轮廓也要变化 | Bump 改着色法线，位移改变或细化几何 | 不能把法线纹理当高度数据直接使用 |
| MD033 | AO/Curvature/ID bake | 智能材质、边缘磨损遮罩 | 烘焙遮蔽、曲率或区域标识用于制作 | 不应将所有 AO 永久混入底色 |
| MD034 | Lightmap UV; Baked lighting | 烘焙光照接缝 | 为预计算照明提供所需展开布局 | 与材质 UV 的复用/重叠要求可能不同 |
| MD035 | Rig; Skeleton; Bone; Joint | 给角色装骨骼 | 建立可操纵结构及变形驱动 | 控制骨架与最终导出骨架可不同 |
| MD036 | Skinning; Weight painting; 蒙皮 | 关节塌、顶点跟错骨骼 | 将顶点变形关联到骨骼及权重 | 权重归一化和影响数限制需匹配目标 |
| MD037 | Bind pose; Rest pose | 动画导入炸开、初始姿态 | 定义绑定或骨架参考姿态 | 引擎/DCC 对术语及矩阵约定需核对 |
| MD038 | FK; IK; Forward/Inverse kinematics | 手够到目标、脚固定地面 | FK 逐关节控制；IK 求解目标约束 | IK 可能多解，需极向量等控制 |
| MD039 | Constraint; Driver | 自动跟随、参数联动 | 通过约束或表达式建立控制关系 | 导出格式未必保留 DCC 原生控制逻辑 |
| MD040 | Blendshape; Morph target; Shape key | 表情、口型、形变 | 在兼容顶点结构间插值形状 | 不替代所有骨骼动画，拓扑要求重要 |
| MD041 | Retargeting; 动画重定向 | 不同角色共用动作 | 将运动映射到不同骨架和比例 | 骨名相同不保证正确，需要映射及校正 |
| MD042 | Animation baking; 动画烘焙 | 约束动画导出不动 | 将程序或控制结果采样为可传输轨迹 | 采样率和简化影响误差与体积 |
| MD043 | Cloth; Soft body; Rigid body simulation | 衣服模拟、软体、碎块 | 模拟不同材料/约束下的动态形变 | 缓存、碰撞厚度与尺度影响稳定性 |
| MD044 | LOD; Proxy; Impostor | 远处简化、预览替身 | 用不同代价的表示适配距离或工作阶段 | 切换阈值、轮廓和阴影一致性要检查 |
| MD045 | Triangulation; Export validation | 引擎里阴影变了 | 将面稳定转换为目标三角形并验证输出 | 烘焙与运行时三角化不一致会造成差异 |
| MD046 | glTF; FBX; USD; 资产交换 | 导出模型、跨软件协作 | 用适合目标的格式交换几何、材质和动画 | 名义支持不保证完整保留全部特性 |
| MD047 | Instancing; Linked duplicate | 多个对象共用网格 | 分离对象变换与共享几何或资源 | 编辑共享数据可能影响全部实例 |
| MD048 | Material slot; Shader graph; Texture set | 多材质、节点材质 | 将几何区域关联到材质及其输入图 | DCC 节点图通常不能无损跨引擎 |
| MD049 | Mipmap; Texture filtering; Anisotropic | 远处纹理闪、斜面糊 | 通过多级采样及过滤降低混叠 | 无 mip 不意味着更清晰稳定 |
| MD050 | Path tracing; Samples; Denoising | 离线渲染噪点、渲染时间 | 采样光路并用降噪估计最终图像 | 降噪可能抹去细节，增加采样也有成本 |
