# 数据结构

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [DT001 · Data structure; ADT; 抽象数据类型](../concepts/DT001.md) | 数据怎么组织、接口与实现 |
| [DT002 · Big O; Time/Space complexity; 摊还分析](../concepts/DT002.md) | 数据多了会多慢、内存代价 |
| [DT003 · Array; Dynamic array; 动态数组](../concepts/DT003.md) | 按下标访问、尾部追加 |
| [DT004 · Linked list; 单向/双向链表](../concepts/DT004.md) | 已知节点快速插入删除 |
| [DT005 · Stack; LIFO; 栈](../concepts/DT005.md) | 最近操作先撤销、递归调用 |
| [DT006 · Queue; FIFO; 队列](../concepts/DT006.md) | 先到先处理、任务排队 |
| [DT007 · Deque; 双端队列; Ring buffer](../concepts/DT007.md) | 两端进出、固定容量循环写 |
| [DT008 · Hash table; HashMap; 哈希表](../concepts/DT008.md) | 按 ID 快速查找、键值映射 |
| [DT009 · Hash collision; Load factor; Rehash](../concepts/DT009.md) | 哈希冲突、扩容卡顿 |
| [DT010 · Set; Multiset; 集合/多重集合](../concepts/DT010.md) | 去重、记录出现次数 |
| [DT011 · BST; Balanced tree; AVL; Red-black tree](../concepts/DT011.md) | 有序查找、范围查询 |
| [DT012 · Heap; Binary heap; Priority queue](../concepts/DT012.md) | 每次取最高优先级、Top K |
| [DT013 · Graph; Vertex; Edge; 图/顶点/边](../concepts/DT013.md) | 依赖关系、好友网络、路径 |
| [DT014 · Adjacency list/matrix; 邻接表/矩阵](../concepts/DT014.md) | 稀疏关系、判断两点相连 |
| [DT015 · BFS; DFS; 广度/深度优先](../concepts/DT015.md) | 遍历层级、连通性、无权最短路 |
| [DT016 · DAG; Topological sort; 拓扑排序](../concepts/DT016.md) | 构建依赖顺序、检测循环 |
| [DT017 · Trie; Radix tree; 前缀树](../concepts/DT017.md) | 前缀搜索、自动补全 |
| [DT018 · B-tree; B+ tree](../concepts/DT018.md) | 数据库索引、多路搜索树 |
| [DT019 · Skip list; 跳表](../concepts/DT019.md) | 有序集合、分层索引 |
| [DT020 · Union-find; Disjoint set; 并查集](../concepts/DT020.md) | 判断是否同组、动态合并集合 |
| [DT021 · Bitmap; Bitset; 位图](../concepts/DT021.md) | 大量布尔状态、整数集合 |
| [DT022 · Bloom filter; 布隆过滤器](../concepts/DT022.md) | 快速排除不存在、缓存穿透 |
| [DT023 · LRU; LFU; Cache eviction](../concepts/DT023.md) | 缓存满了淘汰谁 |
| [DT024 · Prefix sum; Fenwick tree; Segment tree](../concepts/DT024.md) | 区间求和、动态范围统计 |
| [DT025 · Sparse matrix; CSR; 稀疏矩阵](../concepts/DT025.md) | 大矩阵多数是零 |
| [DT026 · Quadtree; Octree; KD-tree; BVH](../concepts/DT026.md) | 空间查询、射线找附近 |
| [DT027 · Immutable/Persistent structure; 结构共享](../concepts/DT027.md) | 保留历史版本、快照更新 |
| [DT028 · AoS; SoA; Data locality](../concepts/DT028.md) | 批量处理属性、缓存效率 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为数据结构领域基线，将集合与组织方式概念落实为操作需求、不变量和真实负载下的成本。

### 关键特征

- 根据查询、插入、删除和遍历的实际比例选结构，而非只看一种操作的复杂度。
- 键相等、顺序、重复元素和所有权语义先于具体容器选择。
- 渐进复杂度、常数成本和内存布局分别评价，不把理论阶数直接当作运行耗时。

### 如何落实

- 列出元素身份、规模范围、操作组合及顺序要求，明确是否需要并发访问或持久化。
- 优先匹配现有容器及辅助索引，写出每次修改后必须成立的结构不变量。
- 实现更新时协调主数据与索引，定义迭代期间修改、空集合及重复键的处理。
- 用代表性分布及退化输入比较候选结构的时间和空间，仅在证据支持时增加专用结构。

### 如何验收

- 在连续插入、删除和查询后核对结构不变量及元素数量。
- 用简单参考容器对照随机操作序列，核对重复键、顺序与边界行为。
- 在目标规模与偏斜分布下记录耗时和内存，确认没有不可接受的退化。

### 常见误用

- 为加速单次查询增加索引，却未维护删除、更新与内存成本。
- 忽略可变键或比较规则不一致，使容器无法可靠定位元素。
