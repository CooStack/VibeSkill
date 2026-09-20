# 数学与计算应用

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [MA001 · Scalar; Vector; Matrix; Tensor](../concepts/MA001.md) | 标量向量矩阵、数据维度 |
| [MA002 · Coordinate; Basis; Linear combination](../concepts/MA002.md) | 同一个点不同坐标、换基 |
| [MA003 · Dot product; Inner product; 点积](../concepts/MA003.md) | 夹角、方向相似、投影 |
| [MA004 · Cross product; 叉积](../concepts/MA004.md) | 求法线、左右方向 |
| [MA005 · Norm; Distance; Normalization](../concepts/MA005.md) | 单位向量、向量长度 |
| [MA006 · Projection; Orthogonality](../concepts/MA006.md) | 把速度分到某方向、正交 |
| [MA007 · Matrix multiplication; Composition](../concepts/MA007.md) | 变换顺序不同结果不同 |
| [MA008 · Determinant; Rank; Inverse; Singularity](../concepts/MA008.md) | 矩阵不可逆、维度丢失 |
| [MA009 · Transpose; Inverse transpose](../concepts/MA009.md) | 行列交换、法线变换 |
| [MA010 · Affine transform; Homogeneous coordinates](../concepts/MA010.md) | 平移也放进矩阵、齐次坐标 |
| [MA011 · Translation; Rotation; Scale; Shear; TRS](../concepts/MA011.md) | 平移旋转缩放、错切 |
| [MA012 · Euler angle; Gimbal lock](../concepts/MA012.md) | 欧拉角、旋转轴卡住 |
| [MA013 · Quaternion; Unit quaternion; 四元数](../concepts/MA013.md) | 平滑旋转、相机朝向 |
| [MA014 · Axis-angle; Rotation matrix; SO(3)](../concepts/MA014.md) | 绕任意轴旋转、旋转群 |
| [MA015 · Lerp; Nlerp; Slerp](../concepts/MA015.md) | 线性插值、球面插值 |
| [MA016 · Barycentric coordinates; 重心坐标](../concepts/MA016.md) | 三角形内部插值 |
| [MA017 · Trigonometry; Radian; atan2](../concepts/MA017.md) | 角度弧度、由方向求角 |
| [MA018 · Line/Ray/Plane; Intersection](../concepts/MA018.md) | 射线点选、线面求交 |
| [MA019 · Bezier curve; Spline; Continuity](../concepts/MA019.md) | 平滑路径、曲线控制点 |
| [MA020 · Easing; Smoothstep; 时间重映射](../concepts/MA020.md) | 动画缓入缓出 |
| [MA021 · Derivative; Partial derivative; Gradient](../concepts/MA021.md) | 瞬时速度、斜率、最陡方向 |
| [MA022 · Integral; Numerical quadrature](../concepts/MA022.md) | 累计路程、光照积分 |
| [MA023 · Jacobian; Hessian](../concepts/MA023.md) | 多维变换变化、优化曲率 |
| [MA024 · ODE; Initial value problem](../concepts/MA024.md) | 速度加速度随时间变化 |
| [MA025 · Euler integration; Semi-implicit Euler; Verlet](../concepts/MA025.md) | 粒子运动、弹簧模拟 |
| [MA026 · Runge-Kutta; Adaptive step](../concepts/MA026.md) | 更精确积分、误差控制 |
| [MA027 · Interpolation vs extrapolation](../concepts/MA027.md) | 样本间补值、预测未来 |
| [MA028 · Floating-point; Rounding; Machine epsilon](../concepts/MA028.md) | 小数误差、接近零比较 |
| [MA029 · Absolute/Relative error; Conditioning; Stability](../concepts/MA029.md) | 很小误差被放大 |
| [MA030 · Root finding; Bisection; Newton method](../concepts/MA030.md) | 求方程根、反求参数 |
| [MA031 · Eigenvalue/Eigenvector; 特征值/特征向量](../concepts/MA031.md) | 主方向、变换不改方向 |
| [MA032 · SVD; PCA; Least squares](../concepts/MA032.md) | 降维、拟合、最小误差 |
| [MA033 · Probability; Random variable; Distribution](../concepts/MA033.md) | 概率掉落、随机数分布 |
| [MA034 · Expectation; Variance; Standard deviation](../concepts/MA034.md) | 平均收益、波动大小 |
| [MA035 · Conditional probability; Bayes theorem](../concepts/MA035.md) | 已知证据更新概率 |
| [MA036 · Sampling; Monte Carlo; Importance sampling](../concepts/MA036.md) | 随机估计积分、路径追踪采样 |
| [MA037 · Uniform sphere/disk sampling](../concepts/MA037.md) | 粒子均匀向外发射 |
| [MA038 · Fourier transform; Frequency; Convolution](../concepts/MA038.md) | 滤波、模糊、频率分析 |
| [MA039 · Set; Relation; Function; Mapping](../concepts/MA039.md) | 集合关系、输入输出 |
| [MA040 · Boolean algebra; Logic; Predicate](../concepts/MA040.md) | 条件组合、与或非 |
| [MA041 · Combinatorics; Permutation; Combination](../concepts/MA041.md) | 排列组合、状态数量爆炸 |
| [MA042 · Graph theory; Connectivity; Shortest path](../concepts/MA042.md) | 网络连通、路径成本 |
| [MA043 · Optimization; Objective; Constraint; Gradient descent](../concepts/MA043.md) | 找最小损失、约束最优值 |
| [MA044 · Dimensional analysis; Units; Scale](../concepts/MA044.md) | 单位错、速度乘时间不对 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为数学领域基线，将公式与数值概念落实为单位、坐标、定义域、误差预算及参考解对照。

### 关键特征

- 变量的物理意义、单位、定义域和坐标约定先于公式代入。
- 区分精确数学关系与有限精度计算，误差和退化条件需要显式处理。
- 选择足以满足任务的模型和求解精度，不凭术语扩大问题或承诺未知误差界。

### 如何落实

- 列出输入输出、量纲、坐标基、角度单位和乘法顺序，标记不允许或需要单独处理的输入。
- 从任务约束写出公式或目标函数，明确前提、边界条件和多解时的选择规则。
- 选择适配规模与精度的现有数值方法，安排收敛条件、迭代上限及非有限结果的处理。
- 建立可手算、解析或高精度参考解，并约定绝对或相对误差及接近零时的比较方式。

### 如何验收

- 用单位分析和已知坐标变换核对表达式，确认转换顺序及输出意义一致。
- 覆盖零值、边界、退化和接近奇异的输入，核对定义域外行为与失败报告。
- 与参考解比较误差；改变步长、采样或精度时核对结果趋势及任务允许的误差范围。

### 常见误用

- 把公式适用前提省略，或混用度与弧度、局部与世界坐标。
- 用随意容差、钳制或归一化掩盖数值失稳，未检查误差来源。
