---
type: note
subject: probability
chapter: 16
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 16 - 协方差与相关系数

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层

- **基础**：定义与直接计算
- **进阶**：性质证明与综合应用
- **拓展**：跨章节联系与建模

## 自测（3问速测）

1. 本章最核心的定义是什么？
2. 本章一个关键结论的适用条件是什么？
3. 如何把本章方法应用到一个具体问题？

## 1. 协方差

### 1.1 协方差的定义

**定义**：设随机变量 X, Y 的期望分别为 μₓ, μᵧ，则 X, Y 的**协方差**定义为：
$$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]$$

**计算公式**：
$$\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$$

**证明**：
$$\text{Cov}(X, Y) = E[XY - X\mu_Y - Y\mu_X + \mu_X\mu_Y]$$
$$= E[XY] - \mu_Y E[X] - \mu_X E[Y] + \mu_X\mu_Y = E[XY] - \mu_X\mu_Y$$

### 1.2 协方差的意义

**符号解释**：
- Cov(X, Y) > 0：X, Y **正相关**（同时增大或减小）
- Cov(X, Y) < 0：X, Y **负相关**（一个增大，一个减小）
- Cov(X, Y) = 0：X, Y **不相关**

**几何解释**：
- 将 (X, Y) 看作平面向量
- 协方差度量"联合偏离"的程度
- 正协方差：点主要分布在一、三象限
- 负协方差：点主要分布在二、四象限

### 1.3 协方差的性质

**定理**：协方差具有以下性质：

1. **对称性**：Cov(X, Y) = Cov(Y, X)

2. **自身协方差**：Cov(X, X) = Var(X)

3. **线性性质**：
   $$\text{Cov}(aX + b, cY + d) = ac \cdot \text{Cov}(X, Y)$$

4. **双线性性质**：
   $$\text{Cov}(X_1 + X_2, Y) = \text{Cov}(X_1, Y) + \text{Cov}(X_2, Y)$$

5. **独立性蕴含**：若 X, Y 独立，则 Cov(X, Y) = 0

**证明**（双线性）：
$$\text{Cov}(X_1 + X_2, Y) = E[(X_1 + X_2)Y] - E[X_1 + X_2]E[Y]$$
$$= E[X_1Y] + E[X_2Y] - E[X_1]E[Y] - E[X_2]E[Y]$$
$$= \text{Cov}(X_1, Y) + \text{Cov}(X_2, Y)$$

### 1.4 协方差矩阵

**定义**：对于随机向量 X = (X₁, ..., Xₙ)ᵀ，**协方差矩阵**定义为：
$$\Sigma = (\sigma_{ij})_{n \times n}, \quad \sigma_{ij} = \text{Cov}(X_i, X_j)$$

**矩阵形式**：
$$\Sigma = E[(X - \mu)(X - \mu)^T] = E[XX^T] - \mu\mu^T$$

**性质**：
1. **对称性**：Σᵀ = Σ
2. **半正定性**：对任意向量 a，有 aᵀΣa ≥ 0
3. **对角元**：σᵢᵢ = Var(Xᵢ)

**证明**（半正定性）：
$$a^T \Sigma a = a^T E[(X-\mu)(X-\mu)^T] a = E[a^T(X-\mu)(X-\mu)^Ta] = E[(a^T(X-\mu))^2] \geq 0$$

## 2. 相关系数

### 2.1 相关系数的定义

**定义**：X, Y 的**相关系数**（Pearson相关系数）定义为：
$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} = \frac{E[(X-\mu_X)(Y-\mu_Y)]}{\sqrt{\text{Var}(X) \text{Var}(Y)}}$$

**标准化**：设 Zₓ = (X - μₓ)/σₓ，Zᵧ = (Y - μᵧ)/σᵧ，则：
$$\rho_{XY} = \text{Cov}(Z_X, Z_Y) = E[Z_X Z_Y]$$

### 2.2 相关系数的性质

**定理**：
1. **有界性**：-1 ≤ ρ ≤ 1

2. **尺度不变性**：ρ(aX + b, cY + d) = sign(ac) · ρ(X, Y)

3. **Cauchy-Schwarz不等式**：
   $$|\text{Cov}(X, Y)| \leq \sqrt{\text{Var}(X) \text{Var}(Y)}$$

**证明**（有界性）：
设 Zₓ, Zᵧ 为标准化变量，则：
$$E[Z_X^2] = E[Z_Y^2] = 1, \quad \rho = E[Z_X Z_Y]$$

由 Cauchy-Schwarz：
$$|\rho| = |E[Z_X Z_Y]| \leq \sqrt{E[Z_X^2] E[Z_Y^2]} = 1$$

### 2.3 相关系数的几何意义

**解释**：
- ρ = 1：完全正相关（线性关系 Y = aX + b, a > 0）
- ρ = -1：完全负相关（线性关系 Y = aX + b, a < 0）
- ρ = 0：无线性关系（不相关）
- |ρ| 接近 1：强线性关系
- |ρ| 接近 0：弱线性关系

**注意**：相关系数只度量**线性关系**，不相关 ≠ 独立。

### 2.4 相关系数的计算

**例**：设 (X, Y) 的联合分布为：

| X\Y | 1 | 2 |
|-----|---|---|
| 1   | 0.2 | 0.3 |
| 2   | 0.3 | 0.2 |

**解**：
- E[X] = 1×0.5 + 2×0.5 = 1.5
- E[Y] = 1×0.5 + 2×0.5 = 1.5
- E[XY] = 1×1×0.2 + 1×2×0.3 + 2×1×0.3 + 2×2×0.2 = 2.4
- Cov(X,Y) = 2.4 - 1.5×1.5 = 0.15

- E[X²] = 1×0.5 + 4×0.5 = 2.5, Var(X) = 2.5 - 2.25 = 0.25
- Var(Y) = 0.25

- ρ = 0.15/(0.5×0.5) = 0.6

## 3. 不相关与独立性

### 3.1 关系

**定理**：独立 ⟹ 不相关（反之不成立）

**证明**：
若 X, Y 独立，则 E[XY] = E[X]E[Y]，故：
$$\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = 0$$

### 3.2 不相关但非独立的例子

**例**：设 X ~ N(0, 1)，Y = X²

**验证**：
- E[X] = 0
- Cov(X, Y) = E[XY] - E[X]E[Y] = E[X³] = 0（奇函数）
- 故 X, Y 不相关

- 但 Y 完全由 X 决定，显然不独立

**几何解释**：X 和 Y 有很强的非线性关系，但无线性关系。

### 3.3 不相关且独立的条件

**定理**：若 (X, Y) 服从二元正态分布，则：
$$X, Y \text{ 独立} \iff X, Y \text{ 不相关} \iff \rho = 0$$

**意义**：正态分布的特殊性。

## 4. 相关性的应用

### 4.1 线性回归

**问题**：给定 X，预测 Y 的最佳线性预测？

**模型**：Ŷ = a + bX

**最优参数**（最小二乘）：
$$b = \frac{\text{Cov}(X, Y)}{\text{Var}(X)} = \rho \frac{\sigma_Y}{\sigma_X}$$
$$a = E[Y] - b E[X] = \mu_Y - \rho \frac{\sigma_Y}{\sigma_X} \mu_X$$

**决定系数**：R² = ρ²

**意义**：ρ² 度量线性回归的解释力。

### 4.2 投资组合

**两资产组合**：
$$\text{Var}(w_1 X_1 + w_2 X_2) = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2w_1 w_2 \rho \sigma_1 \sigma_2$$

**分散化效应**：
- ρ = 1：无分散化（完全正相关）
- ρ = 0：部分分散化
- ρ = -1：完全分散化（可构造无风险组合）

### 4.3 特征选择

**方法**：选择与目标变量高度相关的特征。

**指标**：|ρ(X, Y)| 大的特征更重要。

### 4.4 主成分分析（PCA）

**协方差矩阵的特征分解**：
$$\Sigma = V \Lambda V^T$$

**主成分**：
- 第一主成分：方差最大方向
- 相关系数矩阵的特征向量给出主成分方向

## 5. 其他相关性度量

### 5.1 秩相关系数（Spearman）

**定义**：设 R(Xᵢ), R(Yᵢ) 为秩，则：
$$\rho_s = \frac{\text{Cov}(R(X), R(Y))}{\sqrt{\text{Var}(R(X)) \text{Var}(R(Y))}}$$

**优点**：
- 对异常值稳健
- 可检测单调非线性关系

### 5.2 Kendall秩相关系数

**定义**：
$$\tau = \frac{\text{一致对数} - \text{不一致对数}}{n(n-1)/2}$$

**解释**：
- 一致对：(Xᵢ - Xⱼ)(Yᵢ - Yⱼ) > 0
- 不一致对：(Xᵢ - Xⱼ)(Yᵢ - Yⱼ) < 0

### 5.3 互信息

**定义**：
$$I(X; Y) = \int \int p(x,y) \log \frac{p(x,y)}{p(x)p(y)} dx dy$$

**性质**：
- I(X; Y) ≥ 0
- I(X; Y) = 0 ⟺ X, Y 独立
- 可检测任意依赖关系

## 6. 协方差的估计

### 6.1 样本协方差

**定义**：给定样本 (X₁, Y₁), ..., (Xₙ, Yₙ)，样本协方差为：
$$\hat{\text{Cov}}(X, Y) = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})$$

**性质**：无偏估计。

### 6.2 样本相关系数

$$\hat{\rho} = \frac{\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^n (X_i - \bar{X})^2 \sum_{i=1}^n (Y_i - \bar{Y})^2}}$$

### 6.3 协方差矩阵的估计

$$\hat{\Sigma} = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})(X_i - \bar{X})^T$$

**注意**：高维情形下，需要正则化（如收缩估计）。

## 7. 数值实验

### 7.1 计算协方差和相关系数

```python
import numpy as np

# 生成数据
np.random.seed(42)
n = 1000
X = np.random.randn(n)
Y = 0.8 * X + 0.2 * np.random.randn(n)

# 计算协方差
cov = np.cov(X, Y)[0, 1]
print(f"样本协方差: {cov:.4f}")

# 计算相关系数
corr = np.corrcoef(X, Y)[0, 1]
print(f"样本相关系数: {corr:.4f}")
```

### 7.2 可视化

```python
import matplotlib.pyplot as plt

# 不同相关性的散点图
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 正相关
np.random.seed(42)
X1 = np.random.randn(200)
Y1 = 0.9 * X1 + 0.1 * np.random.randn(200)
axes[0].scatter(X1, Y1, alpha=0.5)
axes[0].set_title(f'ρ = {np.corrcoef(X1, Y1)[0,1]:.3f}')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')

# 不相关
X2 = np.random.randn(200)
Y2 = np.random.randn(200)
axes[1].scatter(X2, Y2, alpha=0.5)
axes[1].set_title(f'ρ = {np.corrcoef(X2, Y2)[0,1]:.3f}')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')

# 负相关
X3 = np.random.randn(200)
Y3 = -0.9 * X3 + 0.1 * np.random.randn(200)
axes[2].scatter(X3, Y3, alpha=0.5)
axes[2].set_title(f'ρ = {np.corrcoef(X3, Y3)[0,1]:.3f}')
axes[2].set_xlabel('X')
axes[2].set_ylabel('Y')

plt.tight_layout()
plt.show()
```

### 7.3 协方差矩阵

```python
import seaborn as sns

# 多维数据的协方差矩阵
np.random.seed(42)
mean = [0, 0, 0]
cov_matrix = [[1, 0.8, 0.3],
              [0.8, 1, 0.5],
              [0.3, 0.5, 1]]
data = np.random.multivariate_normal(mean, cov_matrix, 500)

# 计算样本协方差矩阵
sample_cov = np.cov(data.T)
print("样本协方差矩阵:")
print(sample_cov)

# 热图
plt.figure(figsize=(8, 6))
sns.heatmap(sample_cov, annot=True, fmt='.3f', cmap='coolwarm', center=0)
plt.title('Covariance Matrix Heatmap')
plt.show()
```

## 8. 小结

### 8.1 核心概念

| 概念 | 定义 | 性质 |
|------|------|------|
| 协方差 | Cov(X,Y) = E[(X-μₓ)(Y-μᵧ)] | 双线性、对称 |
| 相关系数 | ρ = Cov(X,Y)/(σₓσᵧ) | -1 ≤ ρ ≤ 1 |
| 协方差矩阵 | Σ = E[(X-μ)(X-μ)ᵀ] | 对称、半正定 |

### 8.2 重要关系

- 独立 ⟹ 不相关
- 不相关 ⟸̸ 独立（一般情况）
- 二元正态：独立 ⟺ 不相关

### 8.3 应用领域

- **投资组合**：风险分散
- **回归分析**：线性预测
- **特征选择**：变量重要性
- **多元统计**：PCA、因子分析

---

**参考文献**：
1. 《概率论与数理统计》（第5版）- 浙江大学
2. 《多元统计分析》- Anderson
3. 《The Elements of Statistical Learning》- Hastie et al.

**下一章**：[[17_Moment_Characteristic]] - 矩与特征函数

