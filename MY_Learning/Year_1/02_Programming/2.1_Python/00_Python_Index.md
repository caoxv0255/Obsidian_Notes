---
type: index
subject: python
created: 2026-02-20
status: in-progress
updated: 2026-04-08
---

# Python 科学计算与应用

> Year_1 Python 学习路径（面向数据科学 + 量化方向）

## 目录结构

| 序号 | 笔记 | 状态 | 核心内容 |
|------|------|------|----------|
| 01 | [[01_Python基础语法]] | ✅ 完成 | 变量/控制流/函数/模块 |
| 02 | [[02.5_NumPy数值计算]] | ✅ 新增 | 数组/收益率/GBM/蒙特卡洛 |
| 03 | [[02_科学计算入门]] | 🟡 进行中 | NumPy进阶/SciPy/可视化 |
| 04 | [[03_Pandas数据处理]] | ✅ 完成 | Series/DataFrame/金融数据 |

> 🟡 = 进行中/待补充 | ✅ = 有实质内容 | 🔴 = 待补

## 当前进度

**已完成**：基础语法、NumPy量化应用（新增）、Pandas数据处理
**进行中**：SciPy科学计算、可视化（Matplotlib）
**待补充**：Python面向对象、数据结构（与算法竞赛衔接）、统计检验

## 学习路径

```
01_Python基础语法（变量、函数、控制流）
    ↓
02.5_NumPy数值计算 ← NEW（量化方向重点：收益率、GBM、蒙特卡洛）
    ↓
02_科学计算入门（NumPy进阶、SciPy）
    ↓
03_Pandas数据处理（DataFrame、金融数据）
    ↓
[后续] Matplotlib可视化 → 统计检验 → 小项目
```

## 量化方向重点

- [[02.5_NumPy数值计算]] 中的 **GBM模拟** 和 **蒙特卡洛定价** 是量化核心
- [[03_Pandas数据处理]] 中的 **收益率计算** 和 **时间序列** 直接用于策略回测
- 建议优先完成 02.5_NumPy数值计算 的练习题

## 数学基础关联

| Python 技能 | 对应数学笔记 |
|------------|-------------|
| 数组运算/矩阵乘法 | [[1.2_线性代数/00_Linear_Algebra_Index]] |
| 随机模拟 | [[1.3_概率论/04_大数定律与中心极限定理]] |
| 统计检验 | [[1.3_概率论/01_概率论基础]] |

## 相关链接

- [[00_Math_Index|数学总索引]]
- [[../../../00_Index|主索引]]、[[01_Mathematics/Linear_Algebra/02_Matrices|矩阵]] |
| Pandas | 数据处理、分析 | 数据获取、清洗、分析 | [[01_Mathematics/Probability/04_Expectation_Variance|期望方差]] |
| Matplotlib/Seaborn | 数据可视化 | 数据可视化 | [[01_Mathematics/Probability/03_Distributions|概率分布]] |
| Scikit-learn | 机器学习 | ML 全流程 | [[01_Mathematics/Calculus/05_Derivatives|导数]]、[[01_Mathematics/Optimization/01_Gradient_Descent|梯度下降]] |
| PyTorch | 深度学习 | PyTorch | [[01_Mathematics/Calculus/18_Partial_Derivatives|偏导数]]、[[01_Mathematics/Calculus/05_Derivatives|导数]] |

## 数学基础关联

### NumPy 与数学关联
- 数组运算 → [[01_Mathematics/Linear_Algebra/03_Matrix_Operations|矩阵运算]]
- 广播机制 → [[01_Mathematics/Linear_Algebra/01_Vectors|向量运算]]
- 线性代数 → [[00_Linear_Algebra_Index|线性代数]]

### Pandas 与数学关联
- 统计函数 → [[01_Mathematics/Probability/04_## 相关链接
- [[00_Calculus_Index|微积分]]
- [[00_Linear_Algebra_Index|线性代数]]
- [[00_Probability_Index|概率统计]]
- [[../../../../备份/02_Programming/Python/00_Pytorch_Index|PyTorch]]
- [[../../../00_Index|主索引]]