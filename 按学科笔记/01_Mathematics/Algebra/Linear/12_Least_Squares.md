---
type: concept
topic: least_squares
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[08_Vectors]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 12
---

# 最小二乘法 (Least Squares)

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

## 1. 最小二乘问题

### 1.1 问题陈述

给定 $A \in \mathbb{R}^{m \times n}$（$m > n$）和 $\mathbf{b} \in \mathbb{R}^m$，求 $\mathbf{x} \in \mathbb{R}^n$ 使得：
$$\min_{\mathbf{x}} \|A\mathbf{x} - \mathbf{b}\|^2$$

这是求解超定线性方程组 $A\mathbf{x} = \mathbf{b}$（方程数多于未知数）的方法。

### 1.2 几何解释

$A\mathbf{x}$ 应该是 $\mathbf{b}$ 在 $\text{Col}(A)$ 上的正交投影。

**关键观察**：
- 如果 $\mathbf{b} \in \text{Col}(A)$，则 $A\mathbf{x} = \mathbf{b}$ 有精确解
- 如果 $\mathbf{b} \notin \text{Col}(A)$，则 $A\mathbf{x} = \mathbf{b}$ 无解，需要求"最佳近似"

### 1.3 正规方程

最优解满足：
$$A^T A \mathbf{x} = A^T \mathbf{b}$$

如果 $A^T A$ 可逆（即 $A$ 满秩），则：
$$\mathbf{x} = (A^T A)^{-1} A^T \mathbf{b}$$

### 1.4 投影矩阵

投影到 $\text{Col}(A)$ 的矩阵为：
$$P = A(A^T A)^{-1} A^T$$

投影向量为：
$$\mathbf{p} = P\mathbf{b} = A\mathbf{x}$$

残差向量为：
$$\mathbf{r} = \mathbf{b} - \mathbf{p} = \mathbf{b} - A\mathbf{x}$$

### 1.5 最优性条件

最小二乘解的最优性条件是残差与 $A$ 的列正交：
$$A^T(\mathbf{b} - A\mathbf{x}) = \mathbf{0}$$

即 $A^T A \mathbf{x} = A^T \mathbf{b}$。

## 2. 求解方法

### 2.1 正规方程法

直接求解 $A^T A \mathbf{x} = A^T \mathbf{b}$。

**优点**：
- 计算简单
- 实现容易

**缺点**：
- 数值不稳定（条件数平方）
- 当 $A$ 病态时误差较大

### 2.2 QR 分解法

$A = QR$，则：
$$R \mathbf{x} = Q^T \mathbf{b}$$

其中 $Q$ 是正交矩阵，$R$ 是上三角矩阵。

**优点**：
- 数值稳定
- 条件数不变

**缺点**：
- 计算量较大

### 2.3 SVD 分解法

$A = U \Sigma V^T$，则：
$$\mathbf{x} = V \Sigma^+ U^T \mathbf{b}$$

其中 $\Sigma^+$ 是 $\Sigma$ 的伪逆。

**优点**：
- 最稳定
- 可处理秩亏情况
- 自动处理病态矩阵

**缺点**：
- 计算量最大

### 2.4 方法比较

| 方法 | 计算量 | 稳定性 | 适用情况 |
|------|--------|--------|----------|
| 正规方程 | $O(mn^2 + n^3)$ | 较差 | $A$ 满秩且条件数小 |
| QR 分解 | $O(mn^2)$ | 好 | 一般情况 |
| SVD 分解 | $O(mn^2 + n^3)$ | 最好 | 秩亏或病态情况 |

## 3. 加权最小二乘

### 3.1 问题陈述

$$\min_{\mathbf{x}} (A\mathbf{x} - \mathbf{b})^T W (A\mathbf{x} - \mathbf{b})$$

其中 $W$ 是正定权重矩阵。

### 3.2 正规方程

$$A^T W A \mathbf{x} = A^T W \mathbf{b}$$

### 3.3 应用场景

- 数据点有不同的重要性
- 测量误差不同
- 异常值检测

## 4. 正则化

### 4.1 Ridge 回归（L2 正则化）

$$\min_{\mathbf{x}} \|A\mathbf{x} - \mathbf{b}\|^2 + \lambda \|\mathbf{x}\|^2$$

正规方程：
$$(A^T A + \lambda I) \mathbf{x} = A^T \mathbf{b}$$

**特点**：
- 总是有唯一解
- 减小系数大小
- 改善条件数

### 4.2 Lasso 回归（L1 正则化）

$$\min_{\mathbf{x}} \|A\mathbf{x} - \mathbf{b}\|^2 + \lambda \|\mathbf{x}\|_1$$

无法得到解析解，需要数值优化（如坐标下降法）。

**特点**：
- 产生稀疏解
- 特征选择
- 无法求导（在零点）

### 4.3 Elastic Net

$$\min_{\mathbf{x}} \|A\mathbf{x} - \mathbf{b}\|^2 + \lambda_1 \|\mathbf{x}\|_1 + \lambda_2 \|\mathbf{x}\|^2$$

结合了 L1 和 L2 正则化的优点。

## 5. 最小二乘的性质

### 5.1 解的性质

1. **唯一性**：如果 $A$ 满秩，则最小二乘解唯一
2. **最优性**：最小二乘解是最小化残差范数的解
3. **投影性**：$A\mathbf{x}$ 是 $\mathbf{b}$ 在 $\text{Col}(A)$ 上的投影

### 5.2 残差性质

1. **正交性**：残差 $\mathbf{r} = \mathbf{b} - A\mathbf{x}$ 与 $\text{Col}(A)$ 正交
2. **最小性**：$\|\mathbf{r}\|^2$ 是所有可能的最小值

### 5.3 统计性质

如果误差 $\mathbf{\varepsilon}$ 满足：
- $E[\mathbf{\varepsilon}] = \mathbf{0}$（零均值）
- $\text{Cov}(\mathbf{\varepsilon}) = \sigma^2 I$（同方差，不相关）

则最小二乘估计：
1. 是无偏估计
2. 是 BLUE（最佳线性无偏估计）

## 代码示例

### 示例 1：三种求解方法比较

```python
import numpy as np
from scipy.linalg import qr, svd
import matplotlib.pyplot as plt

def least_squares_normal(A, b):
    """正规方程法"""
    x = np.linalg.solve(A.T @ A, A.T @ b)
    return x

def least_squares_qr(A, b):
    """QR 分解法"""
    Q, R = qr(A, mode='economic')
    x = np.linalg.solve(R, Q.T @ b)
    return x

def least_squares_svd(A, b):
    """SVD 分解法"""
    U, S, Vt = svd(A, full_matrices=False)
    S_pinv = np.diag(1 / S)
    x = Vt.T @ S_pinv @ U.T @ b
    return x

# 生成测试数据
np.random.seed(42)
n = 100
X = np.linspace(0, 10, n).reshape(-1, 1)
y = 2 * X + 3 + np.random.randn(n, 1) * 2

# 添加偏置项
A = np.column_stack([np.ones((n, 1)), X])
b = y

# 求解
x_normal = least_squares_normal(A, b)
x_qr = least_squares_qr(A, b)
x_svd = least_squares_svd(A, b)

print(f"正规方程法: {x_normal.T}")
print(f"QR 分解法: {x_qr.T}")
print(f"SVD 分解法: {x_svd.T}")

# 验证
y_pred = A @ x_normal
residuals = b - y_pred
print(f"\n残差范数: {np.linalg.norm(residuals):.6f}")
print(f"残差平方和: {np.sum(residuals**2):.6f}")

# 绘图
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.5, label='数据')
plt.plot(X, y_pred, 'r-', label='拟合直线', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('最小二乘回归')
plt.grid(True, alpha=0.3)
plt.show()
```

### 示例 2：Ridge 回归 vs Lasso 回归

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 生成数据
np.random.seed(42)
n_samples = 100
n_features = 10
X = np.random.randn(n_samples, n_features)
# 只有前3个特征有信号
true_coef = np.array([3, -2, 1.5] + [0] * (n_features - 3))
y = X @ true_coef + np.random.randn(n_samples) * 0.5

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Ridge 回归
ridge = Ridge(alpha=1.0)
ridge.fit(X_scaled, y)

# Lasso 回归
lasso = Lasso(alpha=0.1)
lasso.fit(X_scaled, y)

# 普通最小二乘
ls_coef = np.linalg.lstsq(X_scaled, y, rcond=None)[0]

# 比较系数
plt.figure(figsize=(12, 6))
x_pos = np.arange(n_features)
width = 0.25

plt.bar(x_pos - width, true_coef, width, label='真实系数', alpha=0.8)
plt.bar(x_pos, ls_coef, width, label='最小二乘', alpha=0.8)
plt.bar(x_pos + width, ridge.coef_, width, label='Ridge', alpha=0.8)
plt.bar(x_pos + 2*width, lasso.coef_, width, label='Lasso', alpha=0.8)

plt.xlabel('特征索引')
plt.ylabel('系数值')
plt.title('不同回归方法的系数比较')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("真实系数:", true_coef)
print("最小二乘系数:", ls_coef)
print("Ridge 系数:", ridge.coef_)
print("Lasso 系数:", lasso.coef_)
```

### 示例 3：加权最小二乘

```python
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
np.random.seed(42)
n = 50
x = np.linspace(0, 10, n)
# 不同点有不同的噪声水平
noise_levels = 1 + x / 5  # 噪声随 x 增加
y = 2 * x + 3 + np.random.randn(n) * noise_levels

# 构造设计矩阵
A = np.column_stack([np.ones(n), x])
b = y

# 普通最小二乘
x_ls = np.linalg.lstsq(A, b, rcond=None)[0]

# 加权最小二乘（权重与噪声方差成反比）
weights = 1 / noise_levels**2
W = np.diag(weights)
x_wls = np.linalg.solve(A.T @ W @ A, A.T @ W @ b)

# 绘图
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.5, s=noise_levels*20, label='数据（大小表示噪声）')
plt.plot(x, A @ x_ls, 'r-', label='普通最小二乘', linewidth=2)
plt.plot(x, A @ x_wls, 'g--', label='加权最小二乘', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('普通最小二乘 vs 加权最小二乘')
plt.grid(True, alpha=0.3)
plt.show()

print(f"普通最小二乘: y = {x_ls[0]:.2f} + {x_ls[1]:.2f}x")
print(f"加权最小二乘: y = {x_wls[0]:.2f} + {x_wls[1]:.2f}x")
```

### 示例 4：多项式回归

```python
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

# 生成非线性数据
np.random.seed(42)
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x) + np.random.randn(50) * 0.2

# 多项式拟合
degrees = [1, 3, 5, 9]
plt.figure(figsize=(12, 8))

for i, degree in enumerate(degrees, 1):
    # 多项式特征
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(x.reshape(-1, 1))
    
    # 岭回归
    ridge = Ridge(alpha=0.01)
    ridge.fit(X_poly, y)
    
    # 预测
    x_fine = np.linspace(0, 2*np.pi, 200)
    X_fine_poly = poly.fit_transform(x_fine.reshape(-1, 1))
    y_pred = ridge.predict(X_fine_poly)
    
    # 绘图
    plt.subplot(2, 2, i)
    plt.scatter(x, y, alpha=0.5, label='数据')
    plt.plot(x_fine, y_pred, 'r-', label=f'{degree} 次多项式', linewidth=2)
    plt.plot(x_fine, np.sin(x_fine), 'g--', label='真实函数', linewidth=1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title(f'{degree} 次多项式拟合')
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### 示例 5：正则化路径

```python
import numpy as np
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

# 生成数据
np.random.seed(42)
n_samples, n_features = 50, 10
X = np.random.randn(n_samples, n_features)
true_coef = np.array([3, -2, 1.5, 0.5, -0.3] + [0] * 5)
y = X @ true_coef + np.random.randn(n_samples) * 0.5

# Ridge 正则化路径
alphas = np.logspace(-4, 4, 50)
coefs = []

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)

coefs = np.array(coefs)

# 绘图
plt.figure(figsize=(10, 6))
for i in range(n_features):
    plt.plot(alphas, coefs[:, i], label=f'系数 {i+1}')

plt.xscale('log')
plt.xlabel('正则化参数 α')
plt.ylabel('系数值')
plt.title('Ridge 回归的正则化路径')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## 机器学习应用

### 应用 1：线性回归

线性回归是最小二乘法的直接应用，用于预测连续值。

### 应用 2：曲线拟合

用多项式或其他基函数拟合非线性数据。

### 应用 3：正则化防止过拟合

在机器学习中，L2 正则化（Ridge）和 L1 正则化（Lasso）用于：
- 防止过拟合
- 特征选择
- 处理多重共线性

### 应用 4：深度学习中的正则化

在神经网络中，L2 正则化（权重衰减）用于：
- 防止过拟合
- 提高泛化能力

## 严格证明

### 证明 1：正规方程

**定理**：最小二乘解满足 $A^T A \mathbf{x} = A^T \mathbf{b}$。

**证明**：

定义目标函数：
$$f(\mathbf{x}) = \|A\mathbf{x} - \mathbf{b}\|^2 = (A\mathbf{x} - \mathbf{b})^T (A\mathbf{x} - \mathbf{b})$$

展开：
$$f(\mathbf{x}) = \mathbf{x}^T A^T A \mathbf{x} - 2\mathbf{b}^T A \mathbf{x} + \mathbf{b}^T \mathbf{b}$$

求梯度并令为零：
$$\nabla f(\mathbf{x}) = 2A^T A \mathbf{x} - 2A^T \mathbf{b} = \mathbf{0}$$

因此 $A^T A \mathbf{x} = A^T \mathbf{b}$。

### 证明 2：投影性质

**定理**：最小二乘解 $A\mathbf{x}$ 是 $\mathbf{b}$ 在 $\text{Col}(A)$ 上的正交投影。

**证明**：

设 $\mathbf{p} = A\mathbf{x}$ 是最小二乘解对应的投影，$\mathbf{r} = \mathbf{b} - \mathbf{p}$ 是残差。

由正规方程：
$$A^T A \mathbf{x} = A^T \mathbf{b}$$

$$A^T (\mathbf{b} - A\mathbf{x}) = \mathbf{0}$$

$$A^T \mathbf{r} = \mathbf{0}$$

这意味着 $\mathbf{r}$ 与 $A$ 的每一列都正交，因此 $\mathbf{r} \perp \text{Col}(A)$。

由于 $\mathbf{b} = \mathbf{p} + \mathbf{r}$，且 $\mathbf{p} \in \text{Col}(A)$，$\mathbf{r} \perp \text{Col}(A)$，所以 $\mathbf{p}$ 是 $\mathbf{b}$ 在 $\text{Col}(A)$ 上的正交投影。

### 证明 3：Ridge 回归的正规方程

**定理**：Ridge 回归问题 $\min \|A\mathbf{x} - \mathbf{b}\|^2 + \lambda \|\mathbf{x}\|^2$ 的最优解满足 $(A^T A + \lambda I)\mathbf{x} = A^T \mathbf{b}$。

**证明**：

定义目标函数：
$$f(\mathbf{x}) = \|A\mathbf{x} - \mathbf{b}\|^2 + \lambda \|\mathbf{x}\|^2$$

展开：
$$f(\mathbf{x}) = \mathbf{x}^T A^T A \mathbf{x} - 2\mathbf{b}^T A \mathbf{x} + \mathbf{b}^T \mathbf{b} + \lambda \mathbf{x}^T \mathbf{x}$$

$$f(\mathbf{x}) = \mathbf{x}^T (A^T A + \lambda I) \mathbf{x} - 2\mathbf{b}^T A \mathbf{x} + \mathbf{b}^T \mathbf{b}$$

求梯度并令为零：
$$\nabla f(\mathbf{x}) = 2(A^T A + \lambda I)\mathbf{x} - 2A^T \mathbf{b} = \mathbf{0}$$

因此 $(A^T A + \lambda I)\mathbf{x} = A^T \mathbf{b}$。

由于 $A^T A + \lambda I$ 总是正定的（$\lambda > 0$），所以解总是存在且唯一。

## 例题

### 例题 1：求解最小二乘问题

**问题**：求解 $\min \|A\mathbf{x} - \mathbf{b}\|^2$，其中：
$$A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 2 \\ 3 \\ 5 \end{bmatrix}$$

**解**：

正规方程：
$$A^T A \mathbf{x} = A^T \mathbf{b}$$

计算：
$$A^T A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix} = \begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}$$

$$A^T \mathbf{b} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} 2 \\ 3 \\ 5 \end{bmatrix} = \begin{bmatrix} 10 \\ 23 \end{bmatrix}$$

解方程组：
$$\begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 10 \\ 23 \end{bmatrix}$$

解得 $x_1 = 1/3$，$x_2 = 3/2$。

验证：$\mathbf{x} = [1/3, 3/2]^T$

投影向量：
$$\mathbf{p} = A\mathbf{x} = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} 1/3 \\ 3/2 \end{bmatrix} = \begin{bmatrix} 11/6 \\ 10/3 \\ 11/2 \end{bmatrix}$$

残差：
$$\mathbf{r} = \mathbf{b} - \mathbf{p} = \begin{bmatrix} 2 \\ 3 \\ 5 \end{bmatrix} - \begin{bmatrix} 11/6 \\ 10/3 \\ 11/2 \end{bmatrix} = \begin{bmatrix} 1/6 \\ -1/3 \\ -1/6 \end{bmatrix}$$

验证正交性：
$$A^T \mathbf{r} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} 1/6 \\ -1/3 \\ -1/6 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

### 例题 2：拟合直线

**问题**：用最小二乘法拟合直线 $y = ax + b$ 到数据点 $(1, 2), (2, 3), (3, 5)$。

**解**：

设 $y = ax + b$，即 $b + ax = y$。

构造矩阵：
$$A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 2 \\ 3 \\ 5 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} b \\ a \end{bmatrix}$$

这与例题 1 相同，解得 $a = 3/2$，$b = 1/3$。

拟合直线：$y = \frac{3}{2}x + \frac{1}{3}$

### 例题 3：加权最小二乘

**问题**：对例题 1 的数据，使用加权最小二乘，权重为 $w_1 = 1, w_2 = 2, w_3 = 1$。

**解**：

权重矩阵：
$$W = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

加权正规方程：
$$A^T W A \mathbf{x} = A^T W \mathbf{b}$$

计算：
$$A^T W A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix} = \begin{bmatrix} 4 & 8 \\ 8 & 18 \end{bmatrix}$$

$$A^T W \mathbf{b} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 3 \\ 5 \end{bmatrix} = \begin{bmatrix} 13 \\ 29 \end{bmatrix}$$

解方程组：
$$\begin{bmatrix} 4 & 8 \\ 8 & 18 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 13 \\ 29 \end{bmatrix}$$

解得 $x_1 = 5/4$，$x_2 = 7/4$。

加权最小二乘解：$\mathbf{x} = [5/4, 7/4]^T$

### 例题 4：Ridge 回归

**问题**：对例题 1 的数据，使用 Ridge 回归，正则化参数 $\lambda = 1$。

**解**：

Ridge 正规方程：
$$(A^T A + \lambda I)\mathbf{x} = A^T \mathbf{b}$$

计算：
$$A^T A + \lambda I = \begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 4 & 6 \\ 6 & 15 \end{bmatrix}$$

$$A^T \mathbf{b} = \begin{bmatrix} 10 \\ 23 \end{bmatrix}$$

解方程组：
$$\begin{bmatrix} 4 & 6 \\ 6 & 15 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 10 \\ 23 \end{bmatrix}$$

解得 $x_1 = 4/3$，$x_2 = 11/9$。

Ridge 回归解：$\mathbf{x} = [4/3, 11/9]^T \approx [1.333, 1.222]^T$

与普通最小二乘解 $[1/3, 3/2]^T \approx [0.333, 1.500]^T$ 相比，Ridge 回归的系数更小。

### 例题 5：多项式拟合

**问题**：用二次多项式 $y = ax^2 + bx + c$ 拟合数据点 $(-1, 1), (0, 0), (1, 1), (2, 4)$。

**解**：

设 $y = c + bx + ax^2$，即 $c + bx + ax^2 = y$。

构造矩阵：
$$A = \begin{bmatrix} 1 & -1 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 1 \\ 1 & 2 & 4 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 1 \\ 0 \\ 1 \\ 4 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} c \\ b \\ a \end{bmatrix}$$

正规方程：
$$A^T A \mathbf{x} = A^T \mathbf{b}$$

计算：
$$A^T A = \begin{bmatrix} 4 & 2 & 6 \\ 2 & 6 & 8 \\ 6 & 8 & 18 \end{bmatrix}$$

$$A^T \mathbf{b} = \begin{bmatrix} 6 \\ 8 \\ 18 \end{bmatrix}$$

解方程组：
$$\begin{bmatrix} 4 & 2 & 6 \\ 2 & 6 & 8 \\ 6 & 8 & 18 \end{bmatrix} \begin{bmatrix} c \\ b \\ a \end{bmatrix} = \begin{bmatrix} 6 \\ 8 \\ 18 \end{bmatrix}$$

解得 $c = 0$，$b = 0$，$a = 1$。

拟合多项式：$y = x^2$

这完美拟合了所有数据点（因为数据确实来自 $y = x^2$）。

## 习题

### 基础题

1. 求解最小二乘问题：$\min \|A\mathbf{x} - \mathbf{b}\|^2$，其中 $A = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$，$\mathbf{b} = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}$。

2. 用最小二乘法拟合直线 $y = ax + b$ 到数据点 $(1, 1), (2, 2), (3, 2), (4, 3)$。

3. 证明：最小二乘解满足 $A^T A \mathbf{x} = A^T \mathbf{b}$。

4. 用三种方法（正规方程、QR、SVD）求解同一个最小二乘问题。

5. 推导 Ridge 回归的正规方程。

### 进阶题

6. 比较正规方程、QR 分解、SVD 分解的数值稳定性。

7. 证明：最小二乘解是 $\mathbf{b}$ 在 $\text{Col}(A)$ 上的投影。

8. 研究 Lasso 回归的几何意义。

9. 推导加权最小二乘的正规方程。

10. 证明：$\text{rank}(A^T A) = \text{rank}(A)$。

### 挑战题

11. 研究 Total Least Squares（TLS）方法。

12. 证明：正则化可以改善条件数。

13. 在深度学习中，为什么 L2 正则化可以防止过拟合？

14. 研究迭代最小二乘算法（如 IRLS）。

15. 证明：最小二乘问题的解空间是仿射子空间。

## 注意事项

⚠️ **常见错误**

1. **忽略数值稳定性**
   - 正规方程法可能导致数值不稳定
   - 应该使用 QR 或 SVD 分解

2. **混淆不同正则化方法**
   - Ridge（L2）总是有唯一解
   - Lasso（L1）可能没有解析解

3. **忘记标准化**
   - 不同特征的尺度不同会影响结果
   - 应该先标准化数据

✅ **最佳实践**

1. **选择合适的求解方法**
   - 一般情况：QR 分解
   - 病态矩阵：SVD 分解
   - 快速原型：正规方程

2. **理解正则化的作用**
   - L2 正则化：防止过拟合，减小系数
   - L1 正则化：特征选择，产生稀疏解

3. **验证结果的合理性**
   - 检查残差
   - 验证投影性质
   - 可视化结果

## 题型总结与思路技巧

### 最小二乘问题求解流程

#### 📋 解法选择

| 情况 | 推荐方法 |
|-----|---------|
| $A^TA$ 可逆 | 正规方程法 |
| $A$ 列满秩 | QR分解法 |
| 一般情况 | SVD分解法 |
| 大规模问题 | 梯度下降法 |

### 💡 核心技巧与常用结论

#### 1. 正规方程

$$A^TA\mathbf{x} = A^T\mathbf{b}$$

**解**：$\mathbf{x}^* = (A^TA)^{-1}A^T\mathbf{b}$（当$A^TA$可逆时）

**注意**：数值稳定性问题，建议用QR或SVD

#### 2. 几何意义

- 最小二乘解是$\mathbf{b}$在$\text{Col}(A)$上的投影
- 残差$\mathbf{r} = \mathbf{b} - A\mathbf{x}^*$与$\text{Col}(A)$正交

#### 3. 正则化

**Ridge回归（L2）**：
$$\min \|A\mathbf{x} - \mathbf{b}\|^2 + \lambda\|\mathbf{x}\|^2$$
- 解：$\mathbf{x} = (A^TA + \lambda I)^{-1}A^T\mathbf{b}$
- 始终有解，且稳定

**Lasso回归（L1）**：
$$\min \|A\mathbf{x} - \mathbf{b}\|^2 + \lambda\|\mathbf{x}\|_1$$
- 产生稀疏解，无闭式解，需迭代求解

#### 4. 投影矩阵

**性质**：
- $P^2 = P$（幂等）
- $P^T = P$（对称）
- $\text{rank}(P) = \text{rank}(A)$

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 求最小二乘解 | 正规方程/QR | 检验$A^TA$可逆 |
| 计算投影 | 投影矩阵公式 | $P = A(A^TA)^{-1}A^T$ |
| 带正则化 | 修改正规方程 | 加$\lambda I$ |
| 证明正交性 | 残差与列空间正交 | $A^T(\mathbf{b}-A\mathbf{x})=0$ |

### ⚠️ 常见错误

**错误一**：正规方程条件
- 需要$A$列满秩才能直接用$(A^TA)^{-1}$
- 否则需用伪逆或SVD

**错误二**：正则化混淆
- L2正则：有闭式解，系数收缩
- L1正则：无闭式解，产生稀疏解

**错误三**：投影公式
- $P = A(A^TA)^{-1}A^T$ 仅适用于列满秩
- 一般情况用伪逆：$P = AA^+$

## 本章小结

### 重要定义
1. 最小二乘问题：$\min \|A\mathbf{x} - \mathbf{b}\|^2$
2. 正规方程：$A^T A \mathbf{x} = A^T \mathbf{b}$
3. 投影矩阵：$P = A(A^T A)^{-1} A^T$

### 重要定理
1. 正规方程的推导
2. 投影性质
3. Ridge 回归的正规方程

### 重要方法
1. 正规方程法
2. QR 分解法
3. SVD 分解法

### 重要应用
1. 线性回归
2. 曲线拟合
3. 正则化防止过拟合

本章为后续学习正则化和优化奠定了基础。

## 相关概念

- [[08_Vectors]] - 向量基础
- [[11_Linear_Equations]] - 线性方程组
- [[04_Matrix_Basics]] - 矩阵基础

## 参考教材

- 《线性代数》（第6版），同济大学数学系，第三章
- 《Introduction to Linear Algebra》（第5版），Gilbert Strang, Chapter 4
- 《高等代数简明教程》（第2版），北京大学数学系，第三章


