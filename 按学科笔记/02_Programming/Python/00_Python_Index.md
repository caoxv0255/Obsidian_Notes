---
type: index
subject: python
created: 2026-02-20
status: complete
---

# Python 科学计算与深度学习

> 基于 ML 学习的 Python 应用场景参考指南，PyTorch 章节已并入同一目录。

## 目录结构

### 机器学习全流程
- [[01_ML_Pipeline]] - 机器学习端到端流程参考

### 数据科学场景
- [[02_Data_Acquisition]] - 数据获取与导入
- [[03_Data_Cleaning]] - 数据清洗与预处理
- [[04_Data_Analysis]] - 数据分析与统计
- [[05_Data_Visualization]] - 可视化与报告

### 深度学习框架
- [[00_Pytorch_Index]] - PyTorch 学习索引
- [[01_Tensors]] - 张量基础
- [[02_Autograd]] - 自动微分
- [[03_NN_Module]] - 神经网络模块
- [[04_Training_Loop]] - 训练循环
- [[05_Advanced]] - 高级特性

### 实际案例
- [[06_Case_Finance]] - 金融分析案例
- [[07_Case_Image]] - 图像处理案例
- [[08_Case_NLP]] - 自然语言处理案例

## 学习路径

### 初学者路径（数据科学）
1. 数据获取 → 2. 数据清洗 → 3. 数据分析 → 4. 数据可视化

### 机器学习路径
1. 数据获取 → 2. 数据清洗 → 3. ML 全流程 → 4. 实际案例

### 深度学习路径
1. 张量基础 → 2. 自动微分 → 3. 神经网络模块 → 4. 训练循环 → 5. 高级特性

### 实战路径
1. 选择感兴趣的实际案例（金融/图像/NLP）
2. 按照案例中的步骤逐步实现
3. 参考相关场景笔记解决问题

## 核心库速查

| 库 | 用途 | 对应笔记 | 数学基础 |
|----|------|----------|----------|
| NumPy | 数值计算 | 数据分析 | [[../../01_Mathematics/Algebra/Linear/08_Vectors|向量]]、[[../../01_Mathematics/Algebra/Linear/05_Matrix_Operations|矩阵]] |
| Pandas | 数据处理、分析 | 数据获取、清洗、分析 | [[../../01_Mathematics/Probability/14_Expectation|期望]]、[[../../01_Mathematics/Probability/15_Variance|方差]] |
| Matplotlib/Seaborn | 数据可视化 | 数据可视化 | [[../../01_Mathematics/Probability/09_Common_Distributions|常见分布]] |
| Scikit-learn | 机器学习 | ML 全流程 | [[../../01_Mathematics/Calculus/05_Derivatives|导数]]、[[../../01_Mathematics/Optimization/06_Gradient_Methods|梯度下降]] |
| PyTorch | 深度学习 | PyTorch 章节 | [[../../01_Mathematics/Calculus/19_Partial_Derivatives|偏导数]]、[[../../01_Mathematics/Calculus/05_Derivatives|导数]] |

## 数学基础关联

### NumPy 与数学关联
- 数组运算 → [[../../01_Mathematics/Algebra/Linear/05_Matrix_Operations|矩阵运算]]
- 广播机制 → [[../../01_Mathematics/Algebra/Linear/08_Vectors|向量运算]]
- 线性代数 → [[../../01_Mathematics/Algebra/Linear/00_Linear_Algebra_Index|线性代数]]

### Pandas 与数学关联
- 统计函数 → [[../../01_Mathematics/Probability/14_Expectation|期望]]
- 波动分析 → [[../../01_Mathematics/Probability/15_Variance|方差]]
- 分布建模 → [[../../01_Mathematics/Probability/09_Common_Distributions|常见分布]]

### 机器学习与优化关联
- 损失函数 → [[../../01_Mathematics/Calculus/05_Derivatives|导数]]
- 梯度下降 → [[../../01_Mathematics/Optimization/06_Gradient_Methods|梯度方法]]
- 优化器 → [[../../01_Mathematics/Optimization/18_Stochastic_Optimization|随机优化]]

## 相关链接
- [[../../01_Mathematics/Calculus/00_Calculus_Index|微积分]]
- [[../../01_Mathematics/Algebra/Linear/00_Linear_Algebra_Index|线性代数]]
- [[../../01_Mathematics/Probability/00_Probability_Index|概率统计]]
- [[../../01_Mathematics/Optimization/00_Optimization_Index|优化理论]]
- [[00_Pytorch_Index|PyTorch]]
- [[../../../MY_Learning/00_Index|主索引]]