# 数学与计算应用

检索分组：代数与几何、变换、微积分与数值、概率统计、离散数学与优化。
图形用途见 [graphics.md](graphics.md)，结构算法见 [data-structures.md](data-structures.md)。来源 S47、S51、S53-S55，见 [sources.md](sources.md)。本表是选用与释义入口，不代替完整证明；涉及公式时注明定义域、单位、坐标约定和误差。

| ID | 概念 / 英文 / 别名 | 需求线索 | 含义与用途 | 边界 / 易混淆 |
| --- | --- | --- | --- | --- |
| MA001 | Scalar; Vector; Matrix; Tensor | 标量向量矩阵、数据维度 | 分别表达量、线性空间元素、线性映射表示及更一般多线性对象 | 程序中的数组形状不能单独确定数学意义 |
| MA002 | Coordinate; Basis; Linear combination | 同一个点不同坐标、换基 | 用基与系数表达对象并在表示之间转换 | 改坐标表示与真实移动对象是不同操作 |
| MA003 | Dot product; Inner product; 点积 | 夹角、方向相似、投影 | 用内积连接长度、正交及方向关系 | 点积不直接就是角度；归一化和度量要明确 |
| MA004 | Cross product; 叉积 | 求法线、左右方向 | 在约定的三维定向欧氏空间构造垂直向量及面积关系 | 次序决定符号，平行向量叉积为零 |
| MA005 | Norm; Distance; Normalization | 单位向量、向量长度 | 选择度量并将非零向量缩放到单位长度 | 零或极小向量需处理，L1/L2 度量不可随意互换 |
| MA006 | Projection; Orthogonality | 把速度分到某方向、正交 | 分解对象在子空间上的分量 | 投影算子与相机透视投影的具体形式不同 |
| MA007 | Matrix multiplication; Composition | 变换顺序不同结果不同 | 矩阵积表示兼容线性映射的复合 | 通常不交换，存储行列顺序不等于数学乘法约定 |
| MA008 | Determinant; Rank; Inverse; Singularity | 矩阵不可逆、维度丢失 | 描述映射的维数、体积比例及可逆性 | 接近奇异也可能数值不稳定，不只检查是否恰好为零 |
| MA009 | Transpose; Inverse transpose | 行列交换、法线变换 | 转置交换指标，逆转置用于相关对偶变换 | transpose 与 inverse 不同，仅特殊矩阵有对应关系 |
| MA010 | Affine transform; Homogeneous coordinates | 平移也放进矩阵、齐次坐标 | 用增广表示统一平移与线性部分 | 点和方向的齐次分量不同；投影变换更一般 |
| MA011 | Translation; Rotation; Scale; Shear; TRS | 平移旋转缩放、错切 | 分解常见空间变换以表达物体姿态 | 非均匀缩放与旋转组合可能引入分解歧义 |
| MA012 | Euler angle; Gimbal lock | 欧拉角、旋转轴卡住 | 用依次绕轴旋转表达姿态 | 顺序相关，某些姿态下参数化会失去独立自由度 |
| MA013 | Quaternion; Unit quaternion; 四元数 | 平滑旋转、相机朝向 | 用单位四元数表达三维旋转并方便组合/插值 | 四元数不直接是四维空间中的旋转角；需归一化且 q/-q 可表示同一旋转 |
| MA014 | Axis-angle; Rotation matrix; SO(3) | 绕任意轴旋转、旋转群 | 以不同表示描述适当三维旋转及其组合 | 每种参数化有自身约束，不把一般 3x3 矩阵都当旋转 |
| MA015 | Lerp; Nlerp; Slerp | 线性插值、球面插值 | 沿线性或球面路径连接端点 | 对旋转使用 lerp 时需考虑归一化及最短弧选择 |
| MA016 | Barycentric coordinates; 重心坐标 | 三角形内部插值 | 用权重组合顶点表达点与属性 | 权重和、符号及退化三角形影响解释 |
| MA017 | Trigonometry; Radian; atan2 | 角度弧度、由方向求角 | 三角函数关联周期与几何，atan2 保留象限信息 | 库通常用弧度，二维平面轴约定需说明 |
| MA018 | Line/Ray/Plane; Intersection | 射线点选、线面求交 | 用参数与约束求几何交点 | 平行、重合、背向及有限线段范围需分别处理 |
| MA019 | Bezier curve; Spline; Continuity | 平滑路径、曲线控制点 | 用分段多项式及连续性条件描述曲线 | 控制点一般不都在曲线上，参数匀速不等于空间匀速 |
| MA020 | Easing; Smoothstep; 时间重映射 | 动画缓入缓出 | 变换归一化时间以控制变化速度 | 不是物理动力学模型，也不自动支持中途无缝打断 |
| MA021 | Derivative; Partial derivative; Gradient | 瞬时速度、斜率、最陡方向 | 描述局部变化率及多变量标量函数的敏感方向 | 梯度依度量和坐标，差分估计存在误差 |
| MA022 | Integral; Numerical quadrature | 累计路程、光照积分 | 汇总连续变化或用离散采样近似积分 | 步长和函数光滑性影响误差 |
| MA023 | Jacobian; Hessian | 多维变换变化、优化曲率 | 分别组织一阶及二阶导数信息 | 不假定任意函数都光滑可微 |
| MA024 | ODE; Initial value problem | 速度加速度随时间变化 | 用微分方程及初始条件描述演化 | 建模方程、求解器和采样显示需要区分 |
| MA025 | Euler integration; Semi-implicit Euler; Verlet | 粒子运动、弹簧模拟 | 用不同离散更新规则近似动力系统 | 数值稳定性依步长/系统，不能只乘 deltaTime 就保证稳定 |
| MA026 | Runge-Kutta; Adaptive step | 更精确积分、误差控制 | 通过多阶段估计或调整步长控制数值误差 | 更高阶不意味着任何刚性系统都稳定 |
| MA027 | Interpolation vs extrapolation | 样本间补值、预测未来 | 区分已知范围内估计与范围外推断 | 外推对模型误差往往更敏感 |
| MA028 | Floating-point; Rounding; Machine epsilon | 小数误差、接近零比较 | 有限表示导致舍入与精度限制 | 固定 epsilon 不适合所有尺度和物理单位 |
| MA029 | Absolute/Relative error; Conditioning; Stability | 很小误差被放大 | 区分误差尺度、问题敏感性与算法误差传播 | 良好算法不能完全消除病态输入的影响 |
| MA030 | Root finding; Bisection; Newton method | 求方程根、反求参数 | 通过区间缩小或局部导数迭代求解 | 二分需适当包根条件，牛顿可能不收敛 |
| MA031 | Eigenvalue/Eigenvector; 特征值/特征向量 | 主方向、变换不改方向 | 识别在线性映射下仅被缩放的方向 | 不保证实数域可找到完整独立特征基 |
| MA032 | SVD; PCA; Least squares | 降维、拟合、最小误差 | 分解矩阵或按平方误差求近似解，PCA 寻找方差主方向 | PCA 的中心化/尺度处理影响含义，相关不等于因果 |
| MA033 | Probability; Random variable; Distribution | 概率掉落、随机数分布 | 区分事件概率、随机量和分布规律 | 均匀随机数的非线性变换通常不再均匀 |
| MA034 | Expectation; Variance; Standard deviation | 平均收益、波动大小 | 描述随机量的中心和离散程度 | 相同均值不等于相同风险或体验分布 |
| MA035 | Conditional probability; Bayes theorem | 已知证据更新概率 | 在明确事件关系下调整条件信念 | 需考虑先验和证据概率，不反转条件概率 |
| MA036 | Sampling; Monte Carlo; Importance sampling | 随机估计积分、路径追踪采样 | 用样本及适当权重估计量或积分 | 有偏/无偏、方差和覆盖支持范围需区分 |
| MA037 | Uniform sphere/disk sampling | 粒子均匀向外发射 | 按面积/体积测度生成空间分布 | 直接均匀取经纬角通常不均匀覆盖球面 |
| MA038 | Fourier transform; Frequency; Convolution | 滤波、模糊、频率分析 | 用频率分解或卷积组合研究信号 | 离散边界、采样率及核归一化改变结果 |
| MA039 | Set; Relation; Function; Mapping | 集合关系、输入输出 | 明确成员、关系及映射的定义域和值域 | 数学函数通常要求每个输入唯一输出，不等同任意副作用程序 |
| MA040 | Boolean algebra; Logic; Predicate | 条件组合、与或非 | 用命题及逻辑运算组织真假推理 | SQL 三值逻辑与普通二值逻辑需区别 |
| MA041 | Combinatorics; Permutation; Combination | 排列组合、状态数量爆炸 | 根据是否计顺序及重复计算配置数量 | 模型前提不同会给出不同公式 |
| MA042 | Graph theory; Connectivity; Shortest path | 网络连通、路径成本 | 用关系结构研究连接和优化路线 | 带负权、环及动态变化时算法前提不同 |
| MA043 | Optimization; Objective; Constraint; Gradient descent | 找最小损失、约束最优值 | 明确目标与可行域并逐步寻找解 | 局部下降不保证非凸问题的全局最优 |
| MA044 | Dimensional analysis; Units; Scale | 单位错、速度乘时间不对 | 通过量纲检查运算是否物理一致 | 无量纲参数与单位制转换仍需明确记录 |
