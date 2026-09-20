# 算法设计与分析

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [AL001 · Algorithm specification; 算法规格](../concepts/AL001.md) | 什么算正确、输入范围 |
| [AL002 · Asymptotic analysis; 渐近分析; Big O](../concepts/AL002.md) | 数据翻倍慢多少、时间空间复杂度 |
| [AL003 · Amortized analysis; 摊还分析](../concepts/AL003.md) | 数组扩容偶尔慢、均摊成本 |
| [AL004 · Divide and conquer; 分治](../concepts/AL004.md) | 拆成子问题再合并 |
| [AL005 · Dynamic programming; DP; 动态规划](../concepts/AL005.md) | 重复子问题、背包、状态转移 |
| [AL006 · Memoization; 记忆化搜索](../concepts/AL006.md) | 递归反复算相同参数 |
| [AL007 · Greedy algorithm; 贪心](../concepts/AL007.md) | 每步选最好、局部最优 |
| [AL008 · Backtracking; 回溯; Pruning](../concepts/AL008.md) | 穷举组合、撤销试探、剪枝 |
| [AL009 · Binary search; 二分查找; Lower bound](../concepts/AL009.md) | 有序列表定位、找最小可行值 |
| [AL010 · Sorting; Stable sort; 排序稳定性](../concepts/AL010.md) | 相同分数保留原顺序 |
| [AL011 · BFS; Breadth-first search; 广度优先搜索](../concepts/AL011.md) | 最少步数、按层遍历 |
| [AL012 · DFS; Depth-first search; 深度优先搜索](../concepts/AL012.md) | 深入遍历、环检测、递归爆栈 |
| [AL013 · Dijkstra; 最短路](../concepts/AL013.md) | 非负权路径、地图路程 |
| [AL014 · Bellman-Ford; Negative cycle](../concepts/AL014.md) | 带负权的路径、负环 |
| [AL015 · A-star; A*; 启发式搜索](../concepts/AL015.md) | 搜索目标路径太慢 |
| [AL016 · Topological sort; 拓扑排序](../concepts/AL016.md) | 任务依赖、构建顺序、依赖环 |
| [AL017 · Minimum spanning tree; MST; 最小生成树](../concepts/AL017.md) | 低成本连通所有节点 |
| [AL018 · Strongly connected components; SCC](../concepts/AL018.md) | 相互依赖、循环依赖分组 |
| [AL019 · Maximum flow; Min cut; 最大流最小割](../concepts/AL019.md) | 容量分配、网络运输 |
| [AL020 · Sliding window; Two pointers; 双指针](../concepts/AL020.md) | 连续区间、滑动窗口去重 |
| [AL021 · Prefix sum; Difference array; 前缀和与差分](../concepts/AL021.md) | 区间求和、批量范围更新 |
| [AL022 · Randomized algorithm; Monte Carlo; Las Vegas](../concepts/AL022.md) | 随机算法、概率正确性 |
| [AL023 · Approximation algorithm; 近似算法](../concepts/AL023.md) | 最优太慢、容许近似 |
| [AL024 · Online algorithm; Streaming algorithm](../concepts/AL024.md) | 数据流只能看一遍、未来未知 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为算法领域基线，将求解概念落实为问题定义、正确性条件与目标规模下的成本证据。

### 关键特征

- 输入模型、输出目标和约束先于算法名称。
- 正确性、终止性与性能分别论证，近似结果需说明允许偏差。
- 优先使用项目已有可靠实现，只有需求差异明确时才编写专用算法。

### 如何落实

- 写出合法输入、解的判定条件、最优或任意可行解要求，以及无解和多解的处理。
- 根据规模、数据分布和在线或离线约束选择方法，明确需要维持的不变量或递推关系。
- 实现边界与终止条件，安排数值范围、重复元素和退化结构的处理。
- 准备小规模穷举或简单参考算法，在代表性和最坏倾向输入上分别比较正确性与成本。

### 如何验收

- 对小规模输入与参考解逐项比较，核对无解、多解及边界情况。
- 检查循环或递归中的不变量与进展量，确认终止条件不会遗漏合法输入。
- 随输入规模增长记录时间和空间，核对实际增长趋势与任务限制。

### 常见误用

- 从几个样例正确推断算法普遍正确，遗漏结构性反例。
- 只比较平均耗时，忽略退化输入、递归深度或中间数值溢出。
