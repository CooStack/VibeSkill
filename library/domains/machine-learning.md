# 人工智能与机器学习

[返回总目录](../index.md)

选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。

| 概念 | 你可能遇到的问题 |
| --- | --- |
| [ML001 · AI; Artificial intelligence; 人工智能](../concepts/ML001.md) | 智能决策、规则还是模型 |
| [ML002 · Supervised learning; 监督学习](../concepts/ML002.md) | 有标签样本、分类回归 |
| [ML003 · Unsupervised learning; 无监督学习](../concepts/ML003.md) | 没标签分组、发现结构 |
| [ML004 · Reinforcement learning; RL; 强化学习](../concepts/ML004.md) | 试错奖励、策略学习 |
| [ML005 · Train/Validation/Test split; 数据划分](../concepts/ML005.md) | 测试集越调越好 |
| [ML006 · Data leakage; 数据泄漏](../concepts/ML006.md) | 离线准确率很高上线很差 |
| [ML007 · Overfitting; Underfitting; 过拟合与欠拟合](../concepts/ML007.md) | 训练好测试差、两边都差 |
| [ML008 · Regularization; 正则化](../concepts/ML008.md) | 限制模型复杂度 |
| [ML009 · Cross-validation; CV; 交叉验证](../concepts/ML009.md) | 样本少、评估波动 |
| [ML010 · Precision; Recall; F1; 查准率与召回率](../concepts/ML010.md) | 误报漏报、类别不均衡 |
| [ML011 · ROC-AUC; PR-AUC; Threshold](../concepts/ML011.md) | 选分类阈值、排名能力 |
| [ML012 · Calibration; 概率校准](../concepts/ML012.md) | 说九成把握却经常错 |
| [ML013 · Distribution shift; Data/Concept drift](../concepts/ML013.md) | 上线后数据变了、模型退化 |
| [ML014 · Feature engineering; Scaling](../concepts/ML014.md) | 数值量纲差很多、特征构造 |
| [ML015 · Gradient descent; Backpropagation](../concepts/ML015.md) | 训练损失下降、梯度计算 |
| [ML016 · Neural network; ANN; 深度学习](../concepts/ML016.md) | 神经网络层、参数训练 |
| [ML017 · Transformer; Attention](../concepts/ML017.md) | 注意力、上下文建模 |
| [ML018 · Embedding; 嵌入向量](../concepts/ML018.md) | 文本变向量、相似内容 |
| [ML019 · LLM; Large language model](../concepts/ML019.md) | 大语言模型、文本生成 |
| [ML020 · Tokenization; Context window](../concepts/ML020.md) | token 超限、上下文太长 |
| [ML021 · RAG; Retrieval-augmented generation](../concepts/ML021.md) | 根据知识库回答、附依据 |
| [ML022 · Fine-tuning; PEFT; LoRA](../concepts/ML022.md) | 微调、低秩适配 |
| [ML023 · Inference; Training; 推理与训练](../concepts/ML023.md) | 部署预测、训练模型 |
| [ML024 · Quantization; Distillation; 模型压缩](../concepts/ML024.md) | 显存不够、模型瘦身 |
| [ML025 · Grounding; Hallucination; 依据与幻觉](../concepts/ML025.md) | 编造引用、答案无依据 |
| [ML026 · Prompt injection; Tool boundary](../concepts/ML026.md) | 文档叫模型忽略用户指令 |

## 领域实施方法

以下为领域基线，不是每个概念的专用配方。

作为机器学习领域基线，将模型概念落实为预测任务、数据划分和可比较评估，不默认引入训练或复杂模型。

### 关键特征

- 先定义输入、目标与使用时能获得的信息，再选择模型或特征。
- 训练拟合、离线评估和实际使用效果分别判断，避免数据泄漏。
- 指标与错误成本对应，模型复杂度和部署方式受既定任务范围约束。

### 如何落实

- 明确预测单位、标签来源及使用场景，区分相关性预测与需要额外证据的因果目标。
- 按实体、时间或任务适用方式划分数据，确保预处理与特征构建不借用评估集信息。
- 建立简单基线并固定评估流程，用训练或验证范围内的比较选择方案，保留最终评估边界。
- 将推理前处理、输出解释和失败行为接入现有使用流程；仅在任务要求时安排上线监测或再训练。

### 如何验收

- 追踪关键特征来源和时间，确认预测时确实可用且没有标签或重复实体泄漏。
- 在保留数据及相关子群上与基线比较，报告指标、样本量和明显失效场景。
- 用缺失、异常及分布变化输入核对推理输出、延迟和约定的拒绝或降级行为。

### 常见误用

- 反复用最终评估集挑选方案，随后把其分数当作独立泛化证据。
- 以单一平均指标或更大模型替代错误分析，忽略数据与使用场景差异。
