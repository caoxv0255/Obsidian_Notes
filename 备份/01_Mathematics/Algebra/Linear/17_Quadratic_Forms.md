---
type: concept
topic: quadratic_forms
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[13_Eigenvalues]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 17
---

# 二次型 (Quadratic Forms)

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

## 1. 定义

### 1.1 二次型

**定义**：$n$ 元二次型是关于 $n$ 个变量的二次齐次多项式：

$$Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x} = \sum_{i,j=1}^n a_{ij} x_i x_j$$

其中：
- $\mathbf{x} = [x_1, x_2, \ldots, x_n]^T$
- $A$ 是 $n \times n$ 对称矩阵（$A^T = A$）
- $a_{ij} = a_{ji}$（交叉项的系数平分）

**矩阵表示**：
对于二元二次型 $Q(x_1, x_2) = ax_1^2 + 2bx_1x_2 + cx_2^2$：
$$A = \begin{bmatrix} a & b \\ b & c \end{bmatrix}$$

### 1.2 矩阵的对称化

任何二次型都可以用对称矩阵表示。如果原矩阵不对称，可以对称化：

$$A_{sym} = \frac{A + A^T}{2}$$

因为 $\mathbf{x}^T A \mathbf{x} = \mathbf{x}^T \left(\frac{A + A^T}{2}\right) \mathbf{x}$

### 1.3 标准形

通过正交变换 $\mathbf{x} = P\mathbf{y}$（$P$ 是正交矩阵），可以将二次型化为标准形：

$$Q(\mathbf{y}) = \mathbf{y}^T (P^T AP) \mathbf{y} = \mathbf{y}^T \Lambda \mathbf{y} = \sum_{i=1}^n \lambda_i y_i^2$$

其中 $\Lambda = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$ 是 $A$ 的特征值对角矩阵。

### 1.4 规范形

通过可逆变换，可以进一步化为规范形：
- 实数域：$z_1^2 + \cdots + z_p^2 - z_{p+1}^2 - \cdots - z_{p+q}^2$
- 其中 $p$ 是正特征值个数，$q$ 是负特征值个数

## 2. 二次型的分类

### 2.1 按特征值符号分类

根据对称矩阵 $A$ 的特征值符号，二次型可以分为：

1. **正定（Positive Definite）**：所有 $\lambda_i > 0$
   - 对于任意 $\mathbf{x} \neq \mathbf{0}$，$Q(\mathbf{x}) > 0$

2. **半正定（Positive Semidefinite）**：所有 $\lambda_i \geq 0$，至少有一个 $\lambda_i = 0$
   - 对于任意 $\mathbf{x}$，$Q(\mathbf{x}) \geq 0$

3. **负定（Negative Definite）**：所有 $\lambda_i < 0$
   - 对于任意 $\mathbf{x} \neq \mathbf{0}$，$Q(\mathbf{x}) < 0$

4. **半负定（Negative Semidefinite）**：所有 $\lambda_i \leq 0$，至少有一个 $\lambda_i = 0$
   - 对于任意 $\mathbf{x}$，$Q(\mathbf{x}) \leq 0$

5. **不定（Indefinite）**：既有正特征值又有负特征值
   - $Q(\mathbf{x})$ 可正可负

### 2.2 惯性定理（Sylvester's Law of Inertia）

**定理**：二次型的规范形中正平方项的个数 $p$、负平方项的个数 $q$ 和零的个数 $r$ 是唯一确定的，与所用的可逆变换无关。

$(p, q, r)$ 称为二次型的**惯性指数**。

### 2.3 判定方法

**方法 1：特征值法**
计算 $A$ 的所有特征值，检查符号。

**方法 2：主子式法（Sylvester 准则）**
- 正定：所有顺序主子式都为正
- 负定：奇数阶顺序主子式为负，偶数阶为正

**方法 3：配方法**
通过配方将二次型化为标准形。

## 3. 几何意义

### 3.1 二次曲线

二元二次型 $Q(x_1, x_2) = ax_1^2 + 2bx_1x_2 + cx_2^2$ 表示：
- 正定：椭圆
- 半正定：点或退化椭圆
- 不定：双曲线
- 半负定：点或退化双曲线

### 3.2 二次曲面

三元二次型 $Q(x_1, x_2, x_3)$ 表示：
- 正定：椭球面
- 不定：双曲面、抛物面

### 3.3 水平集

二次型的水平集 $\{\mathbf{x} : Q(\mathbf{x}) = c\}$ 是椭球（正定）或双曲面（不定）。

## 4. 正定矩阵的性质

### 4.1 等价条件

以下条件等价：
1. $A$ 是正定矩阵
2. $A$ 的所有特征值都为正
3. $A$ 的所有顺序主子式都为正
4. 存在可逆矩阵 $P$ 使得 $A = P^T P$
5. $A$ 的所有主子式都为正

### 4.2 Cholesky 分解

**定理**：如果 $A$ 是正定矩阵，则存在唯一的下三角矩阵 $L$（对角元为正）使得：
$$A = LL^T$$

这是 Cholesky 分解，是特殊的 LU 分解。

### 4.3 正定矩阵的运算

1. 如果 $A, B$ 正定，则 $A + B$ 正定
2. 如果 $A$ 正定且 $P$ 可逆，则 $P^T AP$ 正定
3. 如果 $A$ 正定，则 $A^{-1}$ 正定

## 代码示例

### 示例 1：判断二次型的正定性

```python
import numpy as np

def check_positive_definite(A, tolerance=1e-10):
    """判断矩阵是否正定"""
    A = np.array(A, dtype=float)
    
    # 检查对称性
    if not np.allclose(A, A.T):
        print("警告：矩阵不对称，使用对称化版本")
        A = (A + A.T) / 2
    
    # 方法 1：特征值法
    eigenvalues = np.linalg.eigvals(A)
    is_pd_eigen = np.all(eigenvalues > tolerance)
    
    # 方法 2：Cholesky 分解法
    try:
        L = np.linalg.cholesky(A)
        is_pd_cholesky = True
    except np.linalg.LinAlgError:
        is_pd_cholesky = False
    
    # 方法 3：主子式法
    is_pd_principal = True
    n = A.shape[0]
    for k in range(1, n + 1):
        principal_minor = np.linalg.det(A[:k, :k])
        if principal_minor <= tolerance:
            is_pd_principal = False
            break
    
    print(f"特征值: {eigenvalues}")
    print(f"特征值法: {'正定' if is_pd_eigen else '不正定'}")
    print(f"Cholesky 分解法: {'正定' if is_pd_cholesky else '不正定'}")
    print(f"主子式法: {'正定' if is_pd_principal else '不正定'}")
    
    return is_pd_eigen

# 示例
A1 = np.array([[2, 1], [1, 2]])
print("矩阵 A1 = [[2, 1], [1, 2]]:")
check_positive_definite(A1)
print()

A2 = np.array([[1, 2], [2, 1]])
print("矩阵 A2 = [[1, 2], [2, 1]]:")
check_positive_definite(A2)
print()

A3 = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
print("矩阵 A3 = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]:")
check_positive_definite(A3)
```

### 示例 2：将二次型化为标准形

```python
import numpy as np

def quadratic_form_standard_form(A):
    """将二次型化为标准形"""
    A = np.array(A, dtype=float)
    
    # 确保对称
    A = (A + A.T) / 2
    
    # 特征值分解
    eigenvalues, eigenvectors = np.linalg.eigh(A)
    
    # 正交矩阵 P
    P = eigenvectors
    
    # 对角矩阵 Lambda
    Lambda = np.diag(eigenvalues)
    
    # 验证
    A_reconstructed = P @ Lambda @ P.T
    if not np.allclose(A, A_reconstructed):
        print("警告：重构失败")
    
    return eigenvalues, P, Lambda

# 示例
A = np.array([[1, 2], [2, 1]])
eigenvalues, P, Lambda = quadratic_form_standard_form(A)

print(f"原矩阵 A:\n{A}")
print(f"\n特征值: {eigenvalues}")
print(f"正交矩阵 P:\n{P}")
print(f"对角矩阵 Lambda:\n{Lambda}")
print(f"\n标准形: Q(y) = {eigenvalues[0]:.2f}y_1^2 + {eigenvalues[1]:.2f}y_2^2")
print(f"正定性: {'正定' if np.all(eigenvalues > 0) else '不定' if np.any(eigenvalues > 0) and np.any(eigenvalues < 0) else '负定'}")
```

### 示例 3：Cholesky 分解

```python
import numpy as np

def cholesky_decomposition(A):
    """Cholesky 分解"""
    A = np.array(A, dtype=float)
    
    # 检查对称性
    if not np.allclose(A, A.T):
        raise ValueError("矩阵必须对称")
    
    n = A.shape[0]
    L = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i + 1):
            if i == j:
                # 对角元素
                sum_k = np.sum(L[i, :j] ** 2)
                L[i, j] = np.sqrt(A[i, i] - sum_k)
            else:
                # 非对角元素
                sum_k = np.sum(L[i, :j] * L[j, :j])
                L[i, j] = (A[i, j] - sum_k) / L[j, j]
    
    return L

# 示例
A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
print(f"矩阵 A:\n{A}")

# Cholesky 分解
L = cholesky_decomposition(A)
print(f"\n下三角矩阵 L:\n{L}")

# 验证
A_reconstructed = L @ L.T
print(f"\n验证 LL^T:\n{A_reconstructed}")
print(f"是否相等: {np.allclose(A, A_reconstructed)}")

# 使用 NumPy 的 Cholesky 分解
L_numpy = np.linalg.cholesky(A)
print(f"\nNumPy 的 Cholesky 分解:\n{L_numpy}")
```

### 示例 4：二次型的几何可视化

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic_form(A, c=1, grid_size=5, n_points=200):
    """绘制二次型的水平集"""
    A = np.array(A, dtype=float)
    A = (A + A.T) / 2
    
    # 创建网格
    x = np.linspace(-grid_size, grid_size, n_points)
    y = np.linspace(-grid_size, grid_size, n_points)
    X, Y = np.meshgrid(x, y)
    
    # 计算二次型值
    Z = np.zeros_like(X)
    for i in range(n_points):
        for j in range(n_points):
            point = np.array([X[i, j], Y[i, j]])
            Z[i, j] = point.T @ A @ point
    
    # 绘制
    plt.figure(figsize=(10, 8))
    contour = plt.contour(X, Y, Z, levels=[c, 2*c, 3*c, 4*c], colors='blue')
    plt.clabel(contour, inline=True, fontsize=10)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title(f'二次型水平集 Q(x) = {c}, 2{c}, 3{c}, 4{c}')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.show()

# 示例 1：正定（椭圆）
A1 = np.array([[2, 1], [1, 2]])
print("示例 1：正定二次型（椭圆）")
plot_quadratic_form(A1, c=1)

# 示例 2：不定（双曲线）
A2 = np.array([[1, 2], [2, 1]])
print("示例 2：不定二次型（双曲线）")
plot_quadratic_form(A2, c=1)
```

### 示例 5：协方差矩阵和二次型

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_confidence_ellipse(mean, cov, n_std=2.0, n_points=200):
    """绘制置信椭圆"""
    # 计算特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    
    # 椭圆的半轴长度
    a = n_std * np.sqrt(eigenvalues[0])
    b = n_std * np.sqrt(eigenvalues[1])
    
    # 生成椭圆点
    theta = np.linspace(0, 2*np.pi, n_points)
    ellipse = np.array([a * np.cos(theta), b * np.sin(theta)])
    
    # 旋转椭圆
    ellipse = eigenvectors @ ellipse
    
    # 平移
    ellipse = ellipse + mean.reshape(-1, 1)
    
    return ellipse[0, :], ellipse[1, :]

# 生成数据
np.random.seed(42)
mean = np.array([0, 0])
cov = np.array([[3, 1], [1, 2]])
data = np.random.multivariate_normal(mean, cov, 1000)

# 绘制
plt.figure(figsize=(10, 8))
plt.scatter(data[:, 0], data[:, 1], alpha=0.5, label='数据点')

# 绘制置信椭圆
ellipse_x, ellipse_y = plot_confidence_ellipse(mean, cov, n_std=2)
plt.plot(ellipse_x, ellipse_y, 'r-', linewidth=2, label='95% 置信椭圆')

# 绘制特征向量
eigenvalues, eigenvectors = np.linalg.eigh(cov)
for i in range(2):
    scale = 3 * np.sqrt(eigenvalues[i])
    plt.arrow(mean[0], mean[1], 
              scale * eigenvectors[0, i], 
              scale * eigenvectors[1, i],
              head_width=0.2, head_length=0.2, 
              fc='blue', ec='blue', 
              label=f'特征向量 {i+1}')

plt.xlabel('x1')
plt.ylabel('x2')
plt.title('协方差矩阵的二次型（置信椭圆）')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.show()

print(f"协方差矩阵:\n{cov}")
print(f"特征值: {eigenvalues}")
print(f"特征向量:\n{eigenvectors}")
```

## 机器学习应用

### 应用 1：高斯分布

多元高斯分布的概率密度函数为：
$$p(\mathbf{x}) = \frac{1}{(2\pi)^{n/2} |\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \Sigma^{-1} (\mathbf{x} - \boldsymbol{\mu})\right)$$

其中二次型 $(\mathbf{x} - \boldsymbol{\mu})^T \Sigma^{-1} (\mathbf{x} - \boldsymbol{\mu})$ 定义了马氏距离。

### 应用 2：协方差矩阵

协方差矩阵是对称正半定矩阵，其特征值表示数据在各个主成分方向上的方差。

### 应用 3：二次优化

许多优化问题涉及二次型，如：
- 最小二乘问题
- 正则化
- 支持向量机

### 应用 4：核方法

在核方法中，核矩阵必须是正半定的。

## 严格证明

### 证明 1：正定矩阵的等价条件

**定理**：以下条件等价：
1. $A$ 是正定矩阵
2. $A$ 的所有特征值都为正
3. $A$ 的所有顺序主子式都为正

**证明**：

$(1) \Rightarrow (2)$：
设 $\lambda$ 是 $A$ 的特征值，$\mathbf{v}$ 是对应的特征向量（$\mathbf{v} \neq \mathbf{0}$）。
$$\mathbf{v}^T A \mathbf{v} = \mathbf{v}^T (\lambda \mathbf{v}) = \lambda \|\mathbf{v}\|^2 > 0$$
因此 $\lambda > 0$。

$(2) \Rightarrow (1)$：
由于 $A$ 是对称矩阵，存在正交矩阵 $P$ 使得 $A = P^T \Lambda P$，其中 $\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_n)$。
对于任意 $\mathbf{x} \neq \mathbf{0}$，令 $\mathbf{y} = P\mathbf{x}$（$\mathbf{y} \neq \mathbf{0}$）：
$$\mathbf{x}^T A \mathbf{x} = \mathbf{x}^T P^T \Lambda P \mathbf{x} = \mathbf{y}^T \Lambda \mathbf{y} = \sum_{i=1}^n \lambda_i y_i^2 > 0$$

$(1) \Leftrightarrow (3)$：
这是 Sylvester 准则，证明略。

### 证明 2：Cholesky 分解的存在性

**定理**：如果 $A$ 是正定矩阵，则存在唯一的下三角矩阵 $L$（对角元为正）使得 $A = LL^T$。

**证明**：

**存在性**：
使用数学归纳法。对于 $n = 1$，$A = [a_{11}]$，取 $L = [\sqrt{a_{11}}]$。

假设对 $n-1$ 阶正定矩阵成立。对于 $n$ 阶正定矩阵 $A$：
$$A = \begin{bmatrix} A_{n-1} & \mathbf{a} \\ \mathbf{a}^T & a_{nn} \end{bmatrix}$$

其中 $A_{n-1}$ 是 $n-1$ 阶正定矩阵。

取 $L = \begin{bmatrix} L_{n-1} & \mathbf{0} \\ \mathbf{l}^T & l_{nn} \end{bmatrix}$，使得：
$$LL^T = \begin{bmatrix} L_{n-1}L_{n-1}^T & L_{n-1}\mathbf{l} \\ \mathbf{l}^T L_{n-1}^T & \mathbf{l}^T \mathbf{l} + l_{nn}^2 \end{bmatrix}$$

与 $A$ 比较：
1. $L_{n-1}L_{n-1}^T = A_{n-1}$，由归纳假设存在 $L_{n-1}$
2. $L_{n-1}\mathbf{l} = \mathbf{a}$，解得 $\mathbf{l} = L_{n-1}^{-1}\mathbf{a}$
3. $\mathbf{l}^T \mathbf{l} + l_{nn}^2 = a_{nn}$，解得 $l_{nn} = \sqrt{a_{nn} - \mathbf{l}^T \mathbf{l}}$

由于 $A$ 正定，$a_{nn} > 0$ 且 $A_{n-1}$ 正定，可以保证 $l_{nn} > 0$。

**唯一性**：
假设 $A = L_1 L_1^T = L_2 L_2^T$，则 $L_2^{-1} L_1 = (L_2^{-1} L_1)^{-T}$。

由于 $L_2^{-1} L_1$ 是下三角矩阵，且等于其转置的逆，所以 $L_2^{-1} L_1 = I$，即 $L_1 = L_2$。

### 证明 3：惯性定理

**定理**：二次型的规范形中正平方项的个数 $p$、负平方项的个数 $q$ 和零的个数 $r$ 是唯一确定的。

**证明**（略）：
这是 Sylvester 惯性定理，证明需要用到线性代数和拓扑学的方法。

## 例题

### 例题 1：判断二次型的正定性

**问题**：判断二次型 $Q(x_1, x_2) = x_1^2 + 2x_1x_2 + x_2^2$ 的正定性。

**解**：

**方法 1：配方法**
$$Q(x_1, x_2) = x_1^2 + 2x_1x_2 + x_2^2 = (x_1 + x_2)^2$$

这是完全平方，对于任意 $(x_1, x_2) \neq (0, 0)$，$Q(x_1, x_2) \geq 0$，但存在 $(x_1, x_2) = (1, -1)$ 使 $Q = 0$。

因此是**半正定**。

**方法 2：矩阵法**
矩阵 $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$

特征值：$\det(A - \lambda I) = (1 - \lambda)^2 - 1 = \lambda^2 - 2\lambda = \lambda(\lambda - 2) = 0$

特征值：$\lambda_1 = 0, \lambda_2 = 2$

由于有零特征值且非负，是**半正定**。

### 例题 2：将二次型化为标准形

**问题**：将二次型 $Q(x_1, x_2) = x_1^2 + 4x_1x_2 + x_2^2$ 化为标准形。

**解**：

矩阵 $A = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$

特征值：$\det(A - \lambda I) = (1 - \lambda)^2 - 4 = \lambda^2 - 2\lambda - 3 = (\lambda - 3)(\lambda + 1) = 0$

特征值：$\lambda_1 = 3, \lambda_2 = -1$

对于 $\lambda_1 = 3$：
$$(A - 3I)\mathbf{v} = \begin{bmatrix} -2 & 2 \\ 2 & -2 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \mathbf{0}$$
$v_1 = v_2$，取 $\mathbf{v}_1 = [1, 1]^T$，归一化：$\mathbf{e}_1 = \frac{1}{\sqrt{2}}[1, 1]^T$

对于 $\lambda_2 = -1$：
$$(A + I)\mathbf{v} = \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \mathbf{0}$$
$v_1 = -v_2$，取 $\mathbf{v}_2 = [1, -1]^T$，归一化：$\mathbf{e}_2 = \frac{1}{\sqrt{2}}[1, -1]^T$

正交矩阵 $P = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}$

标准形：$Q(y_1, y_2) = 3y_1^2 - y_2^2$

这是**不定**二次型。

### 例题 3：配方法化标准形

**问题**：用配方法将 $Q(x_1, x_2, x_3) = x_1^2 + 2x_1x_2 + 2x_1x_3 + x_2^2 + 2x_2x_3 + x_3^2$ 化为标准形。

**解**：

$$Q = x_1^2 + 2x_1(x_2 + x_3) + (x_2 + x_3)^2 = (x_1 + x_2 + x_3)^2$$

令 $y_1 = x_1 + x_2 + x_3$，$y_2 = x_2$，$y_3 = x_3$，则：
$$Q = y_1^2$$

这是**半正定**二次型，标准形中只有一个正平方项。

惯性指数：$(p, q, r) = (1, 0, 2)$

### 例题 4：主子式法判定正定性

**问题**：用主子式法判定 $A = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix}$ 的正定性。

**解**：

计算顺序主子式：

1. 一阶主子式：$D_1 = |2| = 2 > 0$

2. 二阶主子式：$D_2 = \begin{vmatrix} 2 & -1 \\ -1 & 2 \end{vmatrix} = 4 - 1 = 3 > 0$

3. 三阶主子式：
$$D_3 = \begin{vmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{vmatrix} = 2 \begin{vmatrix} 2 & -1 \\ -1 & 2 \end{vmatrix} - (-1) \begin{vmatrix} -1 & -1 \\ 0 & 2 \end{vmatrix} + 0$$
$$= 2 \times 3 - (-1) \times (-2) = 6 - 2 = 4 > 0$$

所有顺序主子式都为正，因此 $A$ 是**正定**矩阵。

### 例题 5：Cholesky 分解

**问题**：对 $A = \begin{bmatrix} 4 & 12 & -16 \\ 12 & 37 & -43 \\ -16 & -43 & 98 \end{bmatrix}$ 进行 Cholesky 分解。

**解**：

设 $L = \begin{bmatrix} l_{11} & 0 & 0 \\ l_{21} & l_{22} & 0 \\ l_{31} & l_{32} & l_{33} \end{bmatrix}$

由 $LL^T = A$：

1. $l_{11}^2 = a_{11} = 4 \implies l_{11} = 2$

2. $l_{11}l_{21} = a_{21} = 12 \implies 2l_{21} = 12 \implies l_{21} = 6$

3. $l_{11}l_{31} = a_{31} = -16 \implies 2l_{31} = -16 \implies l_{31} = -8$

4. $l_{21}^2 + l_{22}^2 = a_{22} = 37 \implies 36 + l_{22}^2 = 37 \implies l_{22} = 1$

5. $l_{21}l_{31} + l_{22}l_{32} = a_{32} = -43 \implies 6(-8) + 1 \cdot l_{32} = -43 \implies l_{32} = 5$

6. $l_{31}^2 + l_{32}^2 + l_{33}^2 = a_{33} = 98 \implies 64 + 25 + l_{33}^2 = 98 \implies l_{33} = 3$

因此：
$$L = \begin{bmatrix} 2 & 0 & 0 \\ 6 & 1 & 0 \\ -8 & 5 & 3 \end{bmatrix}$$

验证：
$$LL^T = \begin{bmatrix} 2 & 0 & 0 \\ 6 & 1 & 0 \\ -8 & 5 & 3 \end{bmatrix} \begin{bmatrix} 2 & 6 & -8 \\ 0 & 1 & 5 \\ 0 & 0 & 3 \end{bmatrix} = \begin{bmatrix} 4 & 12 & -16 \\ 12 & 37 & -43 \\ -16 & -43 & 98 \end{bmatrix} = A$$

## 习题

### 基础题

1. 判断二次型 $Q(x_1, x_2) = 2x_1^2 + 2x_1x_2 + 2x_2^2$ 的正定性。

2. 将二次型 $Q(x_1, x_2) = 3x_1^2 + 4x_1x_2 + 3x_2^2$ 化为标准形。

3. 用主子式法判定 $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$ 的正定性。

4. 对 $A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix}$ 进行 Cholesky 分解。

5. 写出二次型 $Q(x_1, x_2, x_3) = x_1^2 - 2x_1x_2 + x_2^2 + 3x_3^2$ 的矩阵表示。

### 进阶题

6. 证明：正定矩阵的对角元都为正。

7. 证明：如果 $A$ 正定，则 $A^{-1}$ 也正定。

8. 用配方法将 $Q(x_1, x_2, x_3) = x_1^2 + 2x_1x_2 + 2x_2^2 + 2x_2x_3 + 2x_3^2$ 化为标准形。

9. 求二次型 $Q(x_1, x_2) = x_1^2 + 4x_1x_2 + x_2^2 = 1$ 表示的曲线类型。

10. 证明：惯性定理（Sylvester's Law of Inertia）。

### 挑战题

11. 研究 Rayleigh 商：$R(\mathbf{x}) = \frac{\mathbf{x}^T A \mathbf{x}}{\mathbf{x}^T \mathbf{x}}$，证明其最大值和最小值分别是 $A$ 的最大和最小特征值。

12. 在机器学习中，为什么协方差矩阵必须是正半定的？给出具体例子说明。

13. 研究广义特征值问题：$A\mathbf{x} = \lambda B\mathbf{x}$，其中 $B$ 是正定矩阵。

14. 证明：任何正定矩阵都可以写成 $A = P^T P$ 的形式，其中 $P$ 是可逆矩阵。

15. 研究条件数 $\kappa(A) = \frac{\lambda_{\max}}{\lambda_{\min}}$ 对二次优化问题收敛速度的影响。

## 注意事项

⚠️ **常见错误**

1. **忽略对称性**
   - 二次型的矩阵必须是对称的
   - 如果不对称，需要对称化

2. **混淆正定和半正定**
   - 正定：所有特征值 > 0
   - 半正定：所有特征值 ≥ 0

3. **错误使用配方法**
   - 配方时要注意交叉项
   - 可能需要多次配方

✅ **最佳实践**

1. **使用多种方法验证**
   - 特征值法
   - 主子式法
   - 配方法

2. **理解几何意义**
   - 正定：椭圆
   - 不定：双曲线

3. **掌握 Cholesky 分解**
   - 比一般 LU 分解更高效
   - 专门用于正定矩阵

## 题型总结与思路技巧

### 二次型核心要点

#### 📋 二次型的标准化

**步骤**：
1. 写出二次型的矩阵$A$（对称矩阵）
2. 求特征值
3. 正交变换化为标准形
4. 判断正定性

### 💡 核心技巧与常用结论

#### 1. 正定性判断方法

| 方法 | 判定条件 |
|-----|---------|
| 特征值法 | 所有特征值 > 0 |
| 顺序主子式法 | 所有顺序主子式 > 0 |
| 配方法 | 可化为全正系数形式 |
| Cholesky分解 | 存在分解$A=LL^T$ |

#### 2. 惯性定理

二次型的标准形中：
- 正项个数（正惯性指数）不变
- 负项个数（负惯性指数）不变

#### 3. 化标准形方法

**正交变换法**：
$$A = Q\Lambda Q^T, \quad \mathbf{x} = Q\mathbf{y}$$
$$f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x} = \mathbf{y}^T \Lambda \mathbf{y} = \sum \lambda_i y_i^2$$

**配方法**：逐步配方

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 化标准形 | 正交变换/配方法 | 求特征值和特征向量 |
| 判断正定性 | 特征值法或主子式法 | 所有正？ |
| 求正交变换 | 特征向量正交化 | Gram-Schmidt |
| 证明题 | 惯性定理 | 正负惯性指数 |

### ⚠️ 常见错误

**错误一**：配方法忘记换元
- 配方后要用新变量表示

**错误二**：正交矩阵构造
- 特征向量需单位正交化
- 重根特征值对应的特征向量需正交化

**错误三**：正定性判断
- 必须所有特征值 > 0才是正定
- 有一个特征值 ≤ 0就不是正定

## 本章小结

### 重要定义
1. 二次型：$Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$
2. 标准形：$Q(\mathbf{y}) = \sum_{i=1}^n \lambda_i y_i^2$
3. 正定矩阵：所有特征值 > 0

### 重要定理
1. 惯性定理
2. Sylvester 准则
3. Cholesky 分解存在性

### 重要方法
1. 特征值法
2. 主子式法
3. 配方法
4. Cholesky 分解

### 重要应用
1. 高斯分布
2. 协方差矩阵
3. 二次优化
4. 核方法

本章为后续学习内积空间和优化奠定了基础。

## 相关概念

- [[13_Eigenvalues]] - 特征值与特征向量
- [[18_Inner_Product]] - 内积空间
- [[19_Orthogonality]] - 正交性
- [[23_Optimization]] - 最优化应用

## 参考教材

- 《线性代数》（第6版），同济大学数学系，第五章
- 《Introduction to Linear Algebra》（第5版），Gilbert Strang, Chapter 6
- 《高等代数简明教程》（第2版），北京大学数学系，第七章


