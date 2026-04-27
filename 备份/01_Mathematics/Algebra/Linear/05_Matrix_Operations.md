---
type: concept
topic: matrix_operations
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[03_Matrix_Basics]]
acm_relevant: false
created: 2026-03-11
status: complete
subject: linear_algebra
chapter: 05
updated: 2026-04-27
---

# 矩阵运算 (Matrix Operations)

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

## 1. 矩阵运算的几何意义

### 1.1 矩阵作为线性变换

**核心洞察**：矩阵不仅仅是数字的表格，它代表了一种**线性变换**。

当矩阵 $A$ 乘以向量 $\mathbf{x}$ 时，实际上是在应用 $A$ 所描述的线性变换：
$$\mathbf{y} = A\mathbf{x}$$

### 1.2 线性变换的性质

线性变换 $T: \mathbb{R}^n \to \mathbb{R}^m$ 满足：
1. **可加性**：$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
2. **齐次性**：$T(\lambda\mathbf{v}) = \lambda T(\mathbf{v})$

**几何解释**：
- 直线保持为直线（不会弯曲）
- 原点保持固定（不会平移）

### 1.3 基向量的变换

要理解一个线性变换，只需要知道基向量 $\hat{\imath}$ 和 $\hat{\jmath}$ 被变换到哪里。

矩阵 $A = \begin{bmatrix} a & c \\ b & d \end{bmatrix}$ 表示：
- $\hat{\imath} = [1, 0]^T$ 变换到 $[a, b]^T$
- $\hat{\jmath} = [0, 1]^T$ 变换到 $[c, d]^T$

### 1.4 常见的线性变换

#### 1. 旋转矩阵（逆时针旋转 $\theta$ 度）

$$R(\theta) = \begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}$$

#### 2. 缩放矩阵

$$S(s_x, s_y) = \begin{bmatrix}
s_x & 0 \\
0 & s_y
\end{bmatrix}$$

#### 3. 剪切矩阵（$x$ 方向剪切）

$$H(k) = \begin{bmatrix}
1 & k \\
0 & 1
\end{bmatrix}$$

#### 4. 投影矩阵（投影到 $x$ 轴）

$$P_x = \begin{bmatrix}
1 & 0 \\
0 & 0
\end{bmatrix}$$

## 2. 矩阵的逆

### 2.1 可逆矩阵的定义

如果存在矩阵 $B$ 使得 $AB = BA = I$，则称 $A$ 可逆，记 $B = A^{-1}$。

### 2.2 可逆的条件

**定理**：矩阵 $A$ 可逆当且仅当：
1. $A$ 是方阵
2. $\det(A) \neq 0$
3. $A$ 是满秩的（$\text{rank}(A) = n$）
4. $A$ 的列向量线性无关
5. $A\mathbf{x} = \mathbf{0}$ 只有零解

### 2.3 逆矩阵的性质

1. **唯一性**：如果 $A$ 可逆，则 $A^{-1}$ 唯一
2. **自逆性**：$(A^{-1})^{-1} = A$
3. **反序性**：$(AB)^{-1} = B^{-1}A^{-1}$
4. **转置性**：$(A^T)^{-1} = (A^{-1})^T$
5. **标量性**：$(\lambda A)^{-1} = \lambda^{-1}A^{-1}$

### 2.4 逆矩阵的计算

#### 伴随矩阵法（2×2 矩阵）

对于 $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$：
$$A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

#### 高斯消元法

将 $[A | I]$ 通过行初等变换化为 $[I | A^{-1}]$。

## 3. 矩阵分解

### 3.1 LU 分解

对于可逆矩阵 $A$，可以分解为：
$$A = LU$$

其中：
- $L$ 是下三角矩阵（对角线为 1）
- $U$ 是上三角矩阵

**应用**：求解线性方程组 $A\mathbf{x} = \mathbf{b}$

### 3.2 Cholesky 分解

对于对称正定矩阵 $A$，可以分解为：
$$A = LL^T$$

其中 $L$ 是下三角矩阵。

**应用**：求解对称正定线性方程组、计算协方差矩阵。

### 3.3 QR 分解

对于 $m \times n$ 矩阵 $A$（$m \geq n$），可以分解为：
$$A = QR$$

其中：
- $Q$ 是 $m \times n$ 正交矩阵（$Q^T Q = I$）
- $R$ 是 $n \times n$ 上三角矩阵

**应用**：最小二乘问题、特征值计算。

## 代码示例

### 示例 1：矩阵求逆

```python
import numpy as np

# 创建可逆矩阵
A = np.array([[1, 2], [3, 4]], dtype=float)

# 计算逆矩阵
A_inv = np.linalg.inv(A)
print(f"A =\\n{A}")
print(f"A^(-1) =\\n{A_inv}")

# 验证
I = A @ A_inv
print(f"AA^(-1) =\\n{I}")
print(f"是否为单位矩阵: {np.allclose(I, np.eye(2))}")

# 2×2 矩阵的伴随矩阵法
det_A = np.linalg.det(A)
A_inv_manual = (1/det_A) * np.array([[4, -2], [-3, 1]])
print(f"手动计算的逆矩阵:\\n{A_inv_manual}")
print(f"与 NumPy 结果一致: {np.allclose(A_inv, A_inv_manual)}")
```

### 示例 2：LU 分解

```python
import numpy as np
from scipy.linalg import lu

# 创建矩阵
A = np.array([[2, 1, 1], [4, 3, 3], [8, 7, 9]], dtype=float)

# LU 分解
P, L, U = lu(A)

print(f"原始矩阵 A:\\n{A}")
print(f"置换矩阵 P:\\n{P}")
print(f"下三角矩阵 L:\\n{L}")
print(f"上三角矩阵 U:\\n{U}")

# 验证：PA = LU
print(f"PA =\\n{P @ A}")
print(f"LU =\\n{L @ U}")
print(f"PA = LU: {np.allclose(P @ A, L @ U)}")

# 使用 LU 分解求解线性方程组
b = np.array([1, 2, 3])

# PAx = Pb => LUx = Pb
Pb = P @ b

# 先解 Ly = Pb
y = np.linalg.solve(L, Pb)

# 再解 Ux = y
x = np.linalg.solve(U, y)

print(f"解 x = {x}")

# 验证
print(f"验证 Ax = {A @ x}")
print(f"实际 b = {b}")
```

### 示例 3：QR 分解

```python
import numpy as np
from scipy.linalg import qr

# 创建矩阵
A = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)

# QR 分解
Q, R = qr(A, mode='economic')

print(f"原始矩阵 A:\\n{A}")
print(f"正交矩阵 Q:\\n{Q}")
print(f"上三角矩阵 R:\\n{R}")

# 验证：A = QR
print(f"QR =\\n{Q @ R}")
print(f"A = QR: {np.allclose(A, Q @ R)}")

# 验证 Q 的正交性
print(f"Q^T Q =\\n{Q.T @ Q}")
print(f"Q 是否正交: {np.allclose(Q.T @ Q, np.eye(2))}")

# 使用 QR 分解求解最小二乘问题
b = np.array([1, 2, 3])

# Ax = b => QRx = b => Rx = Q^T b
Qt_b = Q.T @ b
x = np.linalg.solve(R, Qt_b)

print(f"最小二乘解 x = {x}")

# 与 NumPy 的 lstsq 比较
x_lstsq, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
print(f"NumPy lstsq 解 x = {x_lstsq}")
```

### 示例 4：线性变换的可视化

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_transform(A, title):
    """可视化线性变换"""
    # 定义单位正方形
    square = np.array([[0, 1, 1, 0, 0],
                       [0, 0, 1, 1, 0]])

    # 应用变换
    transformed = A @ square

    # 绘图
    plt.figure(figsize=(6, 6))
    plt.plot(square[0, :], square[1, :], 'b-', label='原始', linewidth=2)
    plt.plot(transformed[0, :], transformed[1, :], 'r-', label='变换后', linewidth=2)

    # 绘制基向量
    plt.arrow(0, 0, 1, 0, head_width=0.1, head_length=0.1, fc='b', ec='b', linestyle='--')
    plt.arrow(0, 0, 0, 1, head_width=0.1, head_length=0.1, fc='b', ec='b', linestyle='--')
    plt.arrow(0, 0, A[0, 0], A[1, 0], head_width=0.1, head_length=0.1, fc='r', ec='r', linestyle='--')
    plt.arrow(0, 0, A[0, 1], A[1, 1], head_width=0.1, head_length=0.1, fc='r', ec='r', linestyle='--')

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.title(title)
    plt.show()

# 旋转 45 度
theta = np.pi / 4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
plot_transform(R, f'旋转 {np.degrees(theta)}°')

# 缩放
S = np.array([[2, 0],
              [0, 0.5]])
plot_transform(S, '缩放 (2, 0.5)')

# 剪切
H = np.array([[1, 1],
              [0, 1]])
plot_transform(H, '剪切 (x方向)')

# 反射
F = np.array([[-1, 0],
              [0, 1]])
plot_transform(F, '反射 (y轴)')
```

## 机器学习应用

### 应用 1：线性回归的正规方程

使用矩阵运算求解线性回归的最优参数。

```python
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
np.random.seed(42)
n_samples = 100
X = np.random.randn(n_samples, 1)
y = 2 * X + 3 + np.random.randn(n_samples, 1) * 0.5

# 添加偏置项
X_b = np.column_stack([np.ones((n_samples, 1)), X])

# 正规方程：θ = (X^T X)^(-1) X^T y
theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

print(f"估计参数: {theta.T}")
print(f"真实参数: [3, 2]")

# 预测
y_pred = X_b @ theta

# 绘图
plt.scatter(X, y, alpha=0.5, label='数据')
plt.plot(X, y_pred, 'r-', label='拟合直线')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('线性回归（正规方程）')
plt.show()

# 计算 R²
y_mean = np.mean(y)
ss_total = np.sum((y - y_mean) ** 2)
ss_residual = np.sum((y - y_pred) ** 2)
r_squared = 1 - (ss_residual / ss_total)
print(f"R² = {r_squared:.4f}")
```

### 应用 2：协方差矩阵和主成分分析（PCA）

协方差矩阵是对称正定矩阵，可以使用 Cholesky 分解。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# 生成二维数据
np.random.seed(42)
n_samples = 500

# 第一个主成分方向
angle = np.pi / 4
v1 = np.array([np.cos(angle), np.sin(angle)])
v2 = np.array([-np.sin(angle), np.cos(angle)])

# 生成数据
X1 = np.random.randn(n_samples) * 3
X2 = np.random.randn(n_samples) * 1
X = X1.reshape(-1, 1) * v1 + X2.reshape(-1, 1) * v2

# 计算协方差矩阵
cov_matrix = np.cov(X.T)
print(f"协方差矩阵:\\n{cov_matrix}")

# Cholesky 分解
L = np.linalg.cholesky(cov_matrix)
print(f"Cholesky 分解 L:\\n{L}")
print(f"验证 LL^T =\\n{L @ L.T}")
print(f"与协方差矩阵相等: {np.allclose(L @ L.T, cov_matrix)}")

# 使用 PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print(f"主成分（特征向量）:\\n{pca.components_}")
print(f"解释方差比: {pca.explained_variance_ratio_}")

# 可视化
plt.figure(figsize=(12, 5))

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], alpha=0.5)
plt.quiver(*np.mean(X, axis=0), *pca.components_[0] * 3, color='r', scale=1, scale_units='xy')
plt.quiver(*np.mean(X, axis=0), *pca.components_[1] * 3, color='g', scale=1, scale_units='xy')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('原始数据')

plt.subplot(122)
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.5)
plt.xlabel('主成分 1')
plt.ylabel('主成分 2')
plt.title('PCA 变换后')

plt.tight_layout()
plt.show()
```

### 应用 3：批量归一化

批量归一化使用矩阵运算来标准化数据。

```python
import numpy as np

def batch_norm(X, gamma=1, beta=0, epsilon=1e-5):
    """
    批量归一化

    参数:
        X: 输入数据 (batch_size, n_features)
        gamma: 缩放参数
        beta: 平移参数
        epsilon: 数值稳定性参数

    返回:
        normalized: 归一化后的数据
    """
    # 计算均值和方差
    mean = np.mean(X, axis=0, keepdims=True)
    variance = np.var(X, axis=0, keepdims=True)

    # 归一化
    normalized = (X - mean) / np.sqrt(variance + epsilon)

    # 缩放和平移
    normalized = gamma * normalized + beta

    return normalized, mean, variance

# 生成测试数据
np.random.seed(42)
X = np.random.randn(32, 128) * 10 + 5

# 应用批量归一化
X_normalized, mean, variance = batch_norm(X)

print(f"原始数据:")
print(f"  均值: {np.mean(X, axis=0)[:5]}")
print(f"  方差: {np.var(X, axis=0)[:5]}")

print(f"\\n归一化后数据:")
print(f"  均值: {np.mean(X_normalized, axis=0)[:5]}")
print(f"  方差: {np.var(X_normalized, axis=0)[:5]}")

# 矩阵形式的批量归一化
def batch_norm_matrix(X, gamma=1, beta=0, epsilon=1e-5):
    """矩阵形式的批量归一化"""
    batch_size, n_features = X.shape

    # 使用矩阵运算计算均值
    ones_batch = np.ones((batch_size, 1))
    mean = (ones_batch.T @ X) / batch_size  # (1, n_features)

    # 计算方差
    X_centered = X - ones_batch @ mean
    variance = (ones_batch.T @ (X_centered ** 2)) / batch_size

    # 归一化
    normalized = (X - ones_batch @ mean) / np.sqrt(ones_batch @ variance + epsilon)

    # 缩放和平移
    normalized = gamma * normalized + beta

    return normalized

# 验证
X_normalized_matrix = batch_norm_matrix(X)
print(f"\\n矩阵形式归一化后:")
print(f"  均值: {np.mean(X_normalized_matrix, axis=0)[:5]}")
print(f"  方差: {np.var(X_normalized_matrix, axis=0)[:5]}")
print(f"与逐元素形式一致: {np.allclose(X_normalized, X_normalized_matrix)}")
```

## 严格证明

### 证明 1：逆矩阵的唯一性

**定理**：如果矩阵 $A$ 可逆，则 $A^{-1}$ 唯一。

**证明**：

假设 $B$ 和 $C$ 都是 $A$ 的逆矩阵，即：
$$AB = BA = I$$
$$AC = CA = I$$

则：
$$B = BI = B(AC) = (BA)C = IC = C$$

因此 $B = C$，逆矩阵唯一。

### 证明 2：逆矩阵的反序性

**定理**：如果 $A$ 和 $B$ 都可逆，则 $(AB)^{-1} = B^{-1}A^{-1}$。

**证明**：

验证 $(AB)(B^{-1}A^{-1}) = I$：
$$(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I$$

验证 $(B^{-1}A^{-1})(AB) = I$：
$$(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1}IB = B^{-1}B = I$$

因此 $(AB)^{-1} = B^{-1}A^{-1}$。

### 证明 3：可逆矩阵的等价条件

**定理**：对于 $n \times n$ 矩阵 $A$，以下条件等价：
1. $A$ 可逆
2. $\det(A) \neq 0$
3. $\text{rank}(A) = n$
4. $A$ 的列向量线性无关
5. $A\mathbf{x} = \mathbf{0}$ 只有零解

**证明**（简略）：

$(1) \Rightarrow (2)$：如果 $A$ 可逆，则 $AA^{-1} = I$，两边取行列式得 $\det(A)\det(A^{-1}) = 1$，因此 $\det(A) \neq 0$。

$(2) \Rightarrow (3)$：$\det(A) \neq 0$ 意味着 $A$ 的行阶梯形有 $n$ 个主元，因此 $\text{rank}(A) = n$。

$(3) \Rightarrow (4)$：$\text{rank}(A) = n$ 意味着 $A$ 的列向量线性无关。

$(4) \Rightarrow (5)$：如果 $A\mathbf{x} = \mathbf{0}$ 有非零解，则 $A$ 的列向量线性相关。

$(5) \Rightarrow (1)$：如果 $A\mathbf{x} = \mathbf{0}$ 只有零解，则 $A$ 的列向量线性无关，因此 $A$ 可逆。

## 例题

### 例题 1：求逆矩阵

**问题**：求 $A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$ 的逆矩阵。

**解**：

计算行列式：
$$\det(A) = 2 \times 1 - 1 \times 1 = 1$$

使用伴随矩阵法：
$$A^{-1} = \frac{1}{1} \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}$$

验证：
$$AA^{-1} = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$$

### 例题 2：求解线性方程组

**问题**：使用矩阵求逆求解：
$$
\begin{cases}
2x + y = 3 \\
x + y = 2
\end{cases}
$$

**解**：

矩阵形式：$A\mathbf{x} = \mathbf{b}$，其中
$$A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} x \\ y \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}$$

求 $A$ 的逆（由例题1）：
$$A^{-1} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}$$

解：
$$\mathbf{x} = A^{-1}\mathbf{b} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$

因此 $x = 1$，$y = 1$。

## 习题

### 基础题

1. 求 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ 的逆矩阵。

2. 证明：如果 $A$ 可逆，则 $(A^T)^{-1} = (A^{-1})^T$。

3. 设 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$，$B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$，求 $(AB)^{-1}$。

4. 判断 $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ 是否可逆。

5. 使用高斯消元法求 $A = \begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix}$ 的逆矩阵。

### 进阶题

6. 证明：$(A^{-1})^T = (A^T)^{-1}$。

7. 证明：如果 $A$ 和 $B$ 可逆，则 $(AB)^{-1} = B^{-1}A^{-1}$。

8. 证明：正交矩阵的逆等于其转置。

9. 设 $A$ 是对称正定矩阵，证明 Cholesky 分解 $A = LL^T$ 存在。

10. 证明：QR 分解中，$Q$ 的列向量是正交的。

### 挑战题

11. 研究 Moore-Penrose 伪逆的定义和性质。

12. 证明：对于任何 $m \times n$ 矩阵 $A$（$m \geq n$），都存在 QR 分解。

13. 在深度学习中，为什么批量归一化可以提高训练速度？用矩阵运算的角度解释。

14. 研究 Schur 分解及其在特征值计算中的应用。

15. 证明：对称正定矩阵的所有特征值都是正数。

## 注意事项

⚠️ **常见错误**

1. **混淆矩阵求逆和转置**
   - $A^{-1}$ 是逆矩阵，$A^T$ 是转置
   - 正交矩阵满足 $A^{-1} = A^T$，但一般矩阵不满足

2. **矩阵乘法不满足交换律**
   - $(AB)^{-1} = B^{-1}A^{-1}$，不是 $A^{-1}B^{-1}$

3. **忽略数值稳定性**
   - 直接求逆可能产生大的数值误差
   - 应该使用 LU 分解、QR 分解等数值稳定的方法

✅ **最佳实践**

1. **选择合适的数值方法**
   - 求解线性方程组：使用 LU 分解而非直接求逆
   - 对称正定矩阵：使用 Cholesky 分解
   - 最小二乘问题：使用 QR 分解或 SVD

2. **理解矩阵运算的几何意义**
   - 矩阵代表线性变换
   - 逆矩阵代表逆变换
   - 正交矩阵代表保距变换（旋转、反射）

3. **利用矩阵运算的向量化**
   - 避免使用循环进行矩阵运算
   - 使用 NumPy 的向量化操作提高效率

## 题型总结与思路技巧

### 矩阵运算的核心方法

#### 📋 运算类型识别

| 运算类型 | 条件 | 结果形状 |
|---------|------|---------|
| 加法 $A+B$ | 同型矩阵 | 与$A$相同 |
| 数乘 $kA$ | 无限制 | 与$A$相同 |
| 乘法 $AB$ | $A$列数=$B$行数 | $A$行×$B$列 |
| 转置 $A^T$ | 无限制 | 行列互换 |
| 逆 $A^{-1}$ | 方阵且可逆 | 与$A$相同 |

### 💡 核心技巧与常用结论

#### 1. 矩阵乘法技巧

**分块乘法**：将大矩阵分块后逐块计算

**特殊矩阵乘法**：
- 对角矩阵相乘：对应元素相乘
- 正交矩阵相乘：结果仍是正交矩阵
- $AI = IA = A$

#### 2. 转置的性质

- $(A^T)^T = A$
- $(A+B)^T = A^T + B^T$
- $(AB)^T = B^T A^T$
- $(kA)^T = kA^T$

#### 3. 逆矩阵运算

- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1} A^{-1}$
- $(A^T)^{-1} = (A^{-1})^T$
- $(kA)^{-1} = \frac{1}{k} A^{-1}$

#### 4. 矩阵幂运算

- $A^n = A \cdot A \cdots A$（$n$个$A$相乘）
- 当$A$可对角化时：$A^n = P \Lambda^n P^{-1}$

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 矩阵乘法计算 | 按定义或分块 | 维数匹配 |
| 证明运算恒等式 | 利用运算律 | 转置、逆的性质 |
| 简化矩阵表达式 | 分配律、结合律 | 特殊矩阵性质 |
| 矩阵方程求解 | 移项、求逆 | 注意乘法顺序 |

### ⚠️ 常见错误

**错误一**：矩阵乘法交换律
- $AB$ 和 $BA$ 不一定相等，甚至维数都可能不同

**错误二**：逆矩阵乘法顺序
- $(AB)^{-1} = B^{-1} A^{-1}$，顺序相反

**错误三**：消去律滥用
- $AB = AC$ 且 $A \neq 0$ 不能推出 $B = C$
- 需要$A$可逆才能消去

## 本章小结

### 重要概念
1. 矩阵作为线性变换
2. 矩阵的逆和可逆条件
3. 矩阵分解（LU、Cholesky、QR）

### 重要性质
1. 逆矩阵的唯一性：$(A^{-1})^{-1} = A$
2. 逆矩阵的反序性：$(AB)^{-1} = B^{-1}A^{-1}$
3. 正交矩阵的性质：$A^{-1} = A^T$

### 重要应用
1. 线性回归的正规方程
2. 协方差矩阵和 PCA
3. 批量归一化

### 重要算法
1. 高斯消元法求逆
2. LU 分解
3. QR 分解
4. Cholesky 分解

本章为后续学习内积空间和特征理论奠定了基础。

## 相关概念

- [[03_Matrix_Basics]] - 矩阵基础
- [[02_Linear_Equations]] - 线性方程组
- [[13_Determinants]] - 行列式
- [[14_Eigenvalues]] - 特征值
- [[09_Inner_Product]] - 内积空间
- [[00_Python_Index|Python]] - NumPy 线性代数


