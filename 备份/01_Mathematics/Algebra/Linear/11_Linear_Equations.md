---
type: concept
topic: linear_equations
category: linear_algebra
difficulty: beginner
prerequisites:
  - [[08_Vectors]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 11
---

# 线性方程组 (Linear Equations)

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

## 1. 线性方程组的定义

### 1.1 线性方程

一个线性方程是形如：
$$a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = b$$

的方程，其中：
- $x_1, x_2, \ldots, x_n$ 是未知数
- $a_1, a_2, \ldots, a_n$ 是系数（不全为零）
- $b$ 是常数项

**关键特征**：
- 每个未知数都是一次的
- 没有未知数的乘积或幂
- 没有超越函数（如 $\sin$, $\ln$ 等）

### 1.2 线性方程组

$m \times n$ 线性方程组由 $m$ 个线性方程组成，包含 $n$ 个未知数：

$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m
\end{cases}
$$

### 1.3 矩阵表示

线性方程组可以用矩阵形式表示：

$$A\mathbf{x} = \mathbf{b}$$

其中：
- $A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}$ 是 $m \times n$ 系数矩阵
- $\mathbf{x} = \begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}$ 是 $n \times 1$ 未知数向量
- $\mathbf{b} = \begin{bmatrix}
b_1 \\
b_2 \\
\vdots \\
b_m
\end{bmatrix}$ 是 $m \times 1$ 常数向量

**增广矩阵**：
$$[A|\mathbf{b}] = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} & | & b_1 \\
a_{21} & a_{22} & \cdots & a_{2n} & | & b_2 \\
\vdots & \vdots & \ddots & \vdots & | & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn} & | & b_m
\end{bmatrix}$$

## 2. 解的分类

### 2.1 解的存在性

**定理**：线性方程组 $A\mathbf{x} = \mathbf{b}$ 有解的充要条件是 $\mathbf{b}$ 在 $A$ 的列空间中。

即：$\text{rank}(A) = \text{rank}([A|\mathbf{b}])$

### 2.2 解的唯一性

**定理**：
- 如果 $\text{rank}(A) = n$（未知数的个数），则解唯一
- 如果 $\text{rank}(A) < n$，则解不唯一（有无限多解）

### 2.3 三种情况

1. **唯一解**：$\text{rank}(A) = \text{rank}([A|\mathbf{b}]) = n$
2. **无限多解**：$\text{rank}(A) = \text{rank}([A|\mathbf{b}]) < n$
3. **无解**：$\text{rank}(A) \neq \text{rank}([A|\mathbf{b}])$

### 2.4 解的结构

对于有解的方程组 $A\mathbf{x} = \mathbf{b}$：

- **通解**：$\mathbf{x} = \mathbf{x}_p + \mathbf{x}_h$
  - $\mathbf{x}_p$：特解（满足 $A\mathbf{x}_p = \mathbf{b}$）
  - $\mathbf{x}_h$：齐次方程组的通解（满足 $A\mathbf{x}_h = \mathbf{0}$）

## 3. 高斯消元法

### 3.1 行初等变换

高斯消元法使用三种行初等变换：

1. **交换两行**：$R_i \leftrightarrow R_j$
2. **用非零常数乘以某行**：$R_i \rightarrow kR_i$（$k \neq 0$）
3. **将一行的倍数加到另一行**：$R_i \rightarrow R_i + kR_j$

**关键性质**：行初等变换保持方程组的解集不变。

### 3.2 行阶梯形（REF）

矩阵的行阶梯形满足：
1. 每个非零行的第一个非零元素（主元）的列数严格大于上一行主元的列数
2. 全零行在所有非零行的下方

**示例**：
$$
\begin{bmatrix}
1 & 2 & 3 & 4 \\
0 & 0 & 2 & 3 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

### 3.3 简化行阶梯形（RREF）

简化行阶梯形是行阶梯形的进一步简化：
1. 主元都是 1
2. 主元所在列的其他元素都是 0

**示例**：
$$
\begin{bmatrix}
1 & 2 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

### 3.4 高斯消元法的步骤

1. 构造增广矩阵 $[A|\mathbf{b}]$
2. 使用行初等变换将其化为行阶梯形
3. 继续化为简化行阶梯形
4. 写出解

### 3.5 选主元策略

为了避免数值不稳定，可以使用选主元策略：

1. **部分选主元**：在第 $k$ 列中选择绝对值最大的元素作为主元
2. **完全选主元**：在整个右下子矩阵中选择绝对值最大的元素作为主元

## 4. 矩阵的秩

### 4.1 秩的定义

矩阵 $A$ 的秩 $\text{rank}(A)$ 是：
- $A$ 的行阶梯形中非零行的行数
- 等价于 $A$ 的列空间的维数
- 等价于 $A$ 的行空间的维数

### 4.2 秩的性质

1. $\text{rank}(A) \leq \min(m, n)$
2. $\text{rank}(A) = \text{rank}(A^T)$
3. $\text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B))$

### 4.3 秩-零化度定理

**定理**：对于 $m \times n$ 矩阵 $A$：
$$\text{rank}(A) + \text{nullity}(A) = n$$

其中 $\text{nullity}(A)$ 是 $A$ 的零空间的维数（即 $A\mathbf{x} = \mathbf{0}$ 的解空间的维数）。

## 5. 特殊类型的线性方程组

### 5.1 齐次线性方程组

齐次线性方程组：$A\mathbf{x} = \mathbf{0}$

**性质**：
1. 永远有解（至少有零解）
2. 有非零解当且仅当 $\text{rank}(A) < n$
3. 解的集合构成一个向量空间（零空间）

### 5.2 超定方程组

超定方程组：$m > n$（方程数多于未知数）

**解法**：
- 使用最小二乘法：$\mathbf{x} = (A^T A)^{-1} A^T \mathbf{b}$（如果 $A^T A$ 可逆）
- 或使用伪逆：$\mathbf{x} = A^+ \mathbf{b}$

### 5.3 欠定方程组

欠定方程组：$m < n$（方程数少于未知数）

**性质**：
- 如果有解，则有无限多解
- 通解 = 特解 + 齐次方程组的通解

### 5.4 方程组

方程组：$m = n$（方程数等于未知数）

**解法**：
- 如果 $\det(A) \neq 0$，有唯一解：$\mathbf{x} = A^{-1}\mathbf{b}$
- 如果 $\det(A) = 0$，可能有无限多解或无解

## 代码示例

### 示例 1：高斯消元法

```python
import numpy as np

def gaussian_elimination(A, b):
    """
    高斯消元法求解线性方程组 Ax = b

    参数:
        A: 系数矩阵 (m x n)
        b: 常数向量 (m x 1)

    返回:
        x: 解向量
    """
    # 构造增广矩阵
    augmented = np.column_stack([A, b])
    m, n = augmented.shape
    n -= 1  # 未知数的个数

    # 高斯消元
    for col in range(min(m, n)):
        # 选择主元（部分选主元）
        pivot_row = max(range(col, m), key=lambda i: abs(augmented[i, col]))

        # 交换行
        if pivot_row != col:
            augmented[[col, pivot_row]] = augmented[[pivot_row, col]]

        # 消元
        for row in range(col + 1, m):
            factor = augmented[row, col] / augmented[col, col]
            augmented[row] -= factor * augmented[col]

    # 回代
    x = np.zeros(n)
    for i in range(min(m, n) - 1, -1, -1):
        if augmented[i, i] == 0:
            continue  # 处理奇异情况
        x[i] = augmented[i, -1] / augmented[i, i]
        for j in range(i + 1, n):
            x[i] -= augmented[i, j] * x[j]

    return x

# 示例
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)

x = gaussian_elimination(A, b)
print(f"解 x = {x}")

# 验证
print(f"验证 Ax = {A @ x}")
print(f"实际 b = {b}")
print(f"误差 = {np.linalg.norm(A @ x - b):.6f}")
```

### 示例 2：使用 NumPy 求解

```python
import numpy as np

# 唯一解的情况
A1 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 10]], dtype=float)  # 注意：最后一行修改为 10 以确保可逆
b1 = np.array([6, 15, 25], dtype=float)

x1 = np.linalg.solve(A1, b1)
print(f"唯一解 x = {x1}")

# 无限多解的情况（欠定系统）
A2 = np.array([[1, 2, 3],
               [4, 5, 6]], dtype=float)
b2 = np.array([6, 15], dtype=float)

# 使用最小范数解
x2, residuals, rank, singular_values = np.linalg.lstsq(A2, b2, rcond=None)
print(f"\n欠定系统的最小范数解 x = {x2}")
print(f"秩 = {rank}")

# 无解的情况（超定系统）
A3 = np.array([[1, 2],
               [3, 4],
               [5, 6]], dtype=float)
b3 = np.array([3, 7, 11], dtype=float)

# 使用最小二乘解
x3, residuals, rank, singular_values = np.linalg.lstsq(A3, b3, rcond=None)
print(f"\n超定系统的最小二乘解 x = {x3}")
print(f"残差 = {residuals}")
```

### 示例 3：计算矩阵的秩

```python
import numpy as np

def matrix_rank(A, tol=None):
    """计算矩阵的秩"""
    A = np.array(A, dtype=float)
    s = np.linalg.svd(A, compute_uv=False)
    if tol is None:
        tol = np.max(A.shape) * np.finfo(s.dtype).eps
    rank = np.sum(s > tol)
    return rank

# 示例
A1 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
print(f"矩阵 A1 的秩 = {matrix_rank(A1)}")

A2 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 10]])
print(f"矩阵 A2 的秩 = {matrix_rank(A2)}")

# 验证秩-零化度定理
for A, name in [(A1, "A1"), (A2, "A2")]:
    rank = matrix_rank(A)
    nullity = A.shape[1] - rank
    print(f"{name}: rank = {rank}, nullity = {nullity}, rank + nullity = {rank + nullity}")
```

### 示例 4：判断解的情况

```python
import numpy as np

def analyze_solution(A, b):
    """分析线性方程组解的情况"""
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    # 计算秩
    rank_A = np.linalg.matrix_rank(A)
    rank_Ab = np.linalg.matrix_rank(np.column_stack([A, b]))
    n = A.shape[1]

    print(f"rank(A) = {rank_A}")
    print(f"rank([A|b]) = {rank_Ab}")
    print(f"未知数个数 n = {n}")

    if rank_A != rank_Ab:
        print("结论：无解（方程组不相容）")
    elif rank_A == n:
        print("结论：有唯一解")
    else:
        print(f"结论：有无限多解（自由变量个数 = {n - rank_A}）")

# 示例
print("示例 1：唯一解")
A1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 10]]
b1 = [6, 15, 25]
analyze_solution(A1, b1)

print("\n示例 2：无限多解")
A2 = [[1, 2, 3],
      [4, 5, 6]]
b2 = [6, 15]
analyze_solution(A2, b2)

print("\n示例 3：无解")
A3 = [[1, 2],
      [3, 4],
      [5, 6]]
b3 = [1, 2, 4]
analyze_solution(A3, b3)
```

### 示例 5：齐次方程组的解

```python
import numpy as np

def homogeneous_solution(A):
    """求解齐次方程组 Ax = 0 的通解"""
    A = np.array(A, dtype=float)
    m, n = A.shape

    # 计算 SVD
    U, s, Vt = np.linalg.svd(A)
    rank = np.sum(s > 1e-10)

    # 零空间的基
    null_space = Vt[rank:].T

    return null_space, rank

# 示例
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], dtype=float)

null_space, rank = homogeneous_solution(A)
print(f"矩阵 A 的秩 = {rank}")
print(f"零空间的维数 = {A.shape[1] - rank}")
print(f"零空间的基:\n{null_space}")

# 验证
print("\n验证:")
for i in range(null_space.shape[1]):
    x = null_space[:, i]
    print(f"v{i+1}: {x}")
    print(f"A @ v{i+1} = {A @ x}")
```

## 机器学习应用

### 应用 1：线性回归

线性回归是求解超定线性方程组 $A\mathbf{x} = \mathbf{b}$ 的最小二乘解。

```python
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
np.random.seed(42)
x = np.linspace(0, 10, 20)
y = 2 * x + 3 + np.random.randn(20) * 2  # 真实模型：y = 2x + 3

# 构造设计矩阵
A = np.column_stack([np.ones_like(x), x])
b = y

# 最小二乘解
theta, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)

print(f"拟合参数: {theta}")
print(f"真实参数: [3, 2]")
print(f"残差: {residuals}")

# 绘图
plt.scatter(x, y, label='数据点')
plt.plot(x, A @ theta, 'r-', label='拟合直线')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('线性回归')
plt.show()
```

### 应用 2：线性分类（SVM）

支持向量机（SVM）求解的是一个线性方程组。

```python
import numpy as np
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt

# 生成线性可分的数据
np.random.seed(42)
class_1 = np.random.randn(20, 2) + [2, 2]
class_2 = np.random.randn(20, 2) + [-2, -2]

X = np.vstack([class_1, class_2])
y = np.hstack([np.ones(20), -np.ones(20)])

# 训练线性 SVM
svm = LinearSVC(random_state=42)
svm.fit(X, y)

print(f"权重向量 w = {svm.coef_[0]}")
print(f"偏置 b = {svm.intercept_[0]}")

# 绘图
plt.scatter(class_1[:, 0], class_1[:, 1], label='类别 1')
plt.scatter(class_2[:, 0], class_2[:, 1], label='类别 -1')

# 绘制决策边界
xx, yy = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contour(xx, yy, Z, levels=[0], colors='r', linestyles='--')

plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.title('线性 SVM')
plt.show()
```

### 应用 3：神经网络的前向传播

神经网络的前向传播可以看作是一系列线性变换和非线性变换的组合。

```python
import numpy as np

class SimpleNN:
    def __init__(self, input_size, hidden_size, output_size):
        # 初始化权重
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros(hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros(output_size)

    def forward(self, X):
        """前向传播"""
        # 第一层：z1 = X * W1 + b1
        self.z1 = X @ self.W1 + self.b1
        # 激活函数：a1 = ReLU(z1)
        self.a1 = np.maximum(0, self.z1)

        # 第二层：z2 = a1 * W2 + b2
        self.z2 = self.a1 @ self.W2 + self.b2
        # 输出：a2 = softmax(z2)
        exp_z2 = np.exp(self.z2 - np.max(self.z2, axis=1, keepdims=True))
        self.a2 = exp_z2 / np.sum(exp_z2, axis=1, keepdims=True)

        return self.a2

# 示例
nn = SimpleNN(input_size=2, hidden_size=4, output_size=3)
X = np.array([[1, 2], [3, 4], [5, 6]])
output = nn.forward(X)

print(f"输入:\n{X}")
print(f"输出:\n{output}")
print(f"输出概率和: {np.sum(output, axis=1)}")
```

## 严格证明

### 证明 1：线性方程组有解的充要条件

**定理**：线性方程组 $A\mathbf{x} = \mathbf{b}$ 有解的充要条件是 $\mathbf{b}$ 在 $A$ 的列空间中。

**证明**：

**必要性**：
设 $\mathbf{x}_0$ 是方程组的解，即 $A\mathbf{x}_0 = \mathbf{b}$。

将 $A$ 按列分块：$A = [\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n]$，则：
$$\mathbf{b} = A\mathbf{x}_0 = x_{01}\mathbf{a}_1 + x_{02}\mathbf{a}_2 + \cdots + x_{0n}\mathbf{a}_n$$

这是 $\mathbf{b}$ 表示为 $A$ 的列向量的线性组合，因此 $\mathbf{b}$ 在 $A$ 的列空间中。

**充分性**：
设 $\mathbf{b}$ 在 $A$ 的列空间中，即存在 $c_1, c_2, \ldots, c_n$ 使得：
$$\mathbf{b} = c_1\mathbf{a}_1 + c_2\mathbf{a}_2 + \cdots + c_n\mathbf{a}_n$$

令 $\mathbf{x}_0 = [c_1, c_2, \ldots, c_n]^T$，则：
$$A\mathbf{x}_0 = c_1\mathbf{a}_1 + c_2\mathbf{a}_2 + \cdots + c_n\mathbf{a}_n = \mathbf{b}$$

因此 $\mathbf{x}_0$ 是方程组的解。

### 证明 2：秩-零化度定理

**定理**：对于 $m \times n$ 矩阵 $A$，$\text{rank}(A) + \text{nullity}(A) = n$。

**证明**：

设 $\text{rank}(A) = r$，则 $A$ 的行阶梯形有 $r$ 个主元，对应 $r$ 个基本变量。

剩余的 $n - r$ 个变量是自由变量，可以任意取值。

齐次方程组 $A\mathbf{x} = \mathbf{0}$ 的解可以表示为自由变量的线性组合，每个自由变量对应一个基向量。

因此 $\text{nullity}(A) = n - r = n - \text{rank}(A)$。

### 证明 3：行初等变换保持解集不变

**定理**：行初等变换保持线性方程组的解集不变。

**证明**：

我们只需要证明三种行初等变换都保持解集不变。

1. **交换两行 $R_i \leftrightarrow R_j$**：
   - 这只是改变了方程的顺序，不影响解集。

2. **用非零常数乘以某行 $R_i \rightarrow kR_i$（$k \neq 0$）**：
   - 原方程：$a_{i1}x_1 + \cdots + a_{in}x_n = b_i$
   - 变换后：$ka_{i1}x_1 + \cdots + ka_{in}x_n = kb_i$
   - 由于 $k \neq 0$，两个方程等价。

3. **将一行的倍数加到另一行 $R_i \rightarrow R_i + kR_j$**：
   - 原方程组：
     $$
     \begin{cases}
     a_{i1}x_1 + \cdots + a_{in}x_n = b_i \\
     a_{j1}x_1 + \cdots + a_{jn}x_n = b_j
     \end{cases}
     $$
   - 变换后：
     $$
     \begin{cases}
     (a_{i1} + ka_{j1})x_1 + \cdots + (a_{in} + ka_{jn})x_n = b_i + kb_j \\
     a_{j1}x_1 + \cdots + a_{jn}x_n = b_j
     \end{cases}
     $$
   - 如果 $\mathbf{x}$ 满足原方程组，则它也满足变换后的方程组（第一行是原第一行加上 $k$ 倍的第二行）。
   - 反之，如果 $\mathbf{x}$ 满足变换后的方程组，则从第一行减去 $k$ 倍的第二行就得到原第一行，所以 $\mathbf{x}$ 也满足原方程组。

因此，行初等变换保持解集不变。

## 例题

### 例题 1：求解线性方程组（唯一解）

**问题**：求解以下线性方程组：
$$
\begin{cases}
2x_1 + x_2 - x_3 = 1 \\
-3x_1 - x_2 + 2x_3 = 2 \\
-2x_1 + x_2 + 2x_3 = 3
\end{cases}
$$

**解**：

增广矩阵：
$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & 1 \\
-3 & -1 & 2 & 2 \\
-2 & 1 & 2 & 3
\end{array}\right]
$$

高斯消元：
1. $R_1 \rightarrow \frac{1}{2}R_1$
$$
\left[\begin{array}{ccc|c}
1 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
-3 & -1 & 2 & 2 \\
-2 & 1 & 2 & 3
\end{array}\right]
$$

2. $R_2 \rightarrow R_2 + 3R_1$，$R_3 \rightarrow R_3 + 2R_1$
$$
\left[\begin{array}{ccc|c}
1 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
0 & \frac{1}{2} & \frac{1}{2} & \frac{7}{2} \\
0 & 2 & 1 & 4
\end{array}\right]
$$

3. $R_2 \rightarrow 2R_2$
$$
\left[\begin{array}{ccc|c}
1 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
0 & 1 & 1 & 7 \\
0 & 2 & 1 & 4
\end{array}\right]
$$

4. $R_1 \rightarrow R_1 - \frac{1}{2}R_2$，$R_3 \rightarrow R_3 - 2R_2$
$$
\left[\begin{array}{ccc|c}
1 & 0 & -1 & -3 \\
0 & 1 & 1 & 7 \\
0 & 0 & -1 & -10
\end{array}\right]
$$

5. $R_3 \rightarrow -R_3$
$$
\left[\begin{array}{ccc|c}
1 & 0 & -1 & -3 \\
0 & 1 & 1 & 7 \\
0 & 0 & 1 & 10
\end{array}\right]
$$

6. $R_1 \rightarrow R_1 + R_3$，$R_2 \rightarrow R_2 - R_3$
$$
\left[\begin{array}{ccc|c}
1 & 0 & 0 & 7 \\
0 & 1 & 0 & -3 \\
0 & 0 & 1 & 10
\end{array}\right]
$$

唯一解：$x_1 = 7, x_2 = -3, x_3 = 10$。

### 例题 2：求解线性方程组（无限多解）

**问题**：求解以下线性方程组：
$$
\begin{cases}
x_1 + 2x_2 + 3x_3 = 6 \\
2x_1 + 3x_2 + 4x_3 = 9 \\
3x_1 + 4x_2 + 5x_3 = 12
\end{cases}
$$

**解**：

增广矩阵：
$$
\left[\begin{array}{ccc|c}
1 & 2 & 3 & 6 \\
2 & 3 & 4 & 9 \\
3 & 4 & 5 & 12
\end{array}\right]
$$

高斯消元：
1. $R_2 \rightarrow R_2 - 2R_1$，$R_3 \rightarrow R_3 - 3R_1$
$$
\left[\begin{array}{ccc|c}
1 & 2 & 3 & 6 \\
0 & -1 & -2 & -3 \\
0 & -2 & -4 & -6
\end{array}\right]
$$

2. $R_3 \rightarrow R_3 - 2R_2$
$$
\left[\begin{array}{ccc|c}
1 & 2 & 3 & 6 \\
0 & -1 & -2 & -3 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

3. $R_2 \rightarrow -R_2$
$$
\left[\begin{array}{ccc|c}
1 & 2 & 3 & 6 \\
0 & 1 & 2 & 3 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

4. $R_1 \rightarrow R_1 - 2R_2$
$$
\left[\begin{array}{ccc|c}
1 & 0 & -1 & 0 \\
0 & 1 & 2 & 3 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

$\text{rank}(A) = 2 < n = 3$，有无限多解。

基本变量：$x_1, x_2$；自由变量：$x_3$。

从矩阵得到：
$$
\begin{cases}
x_1 - x_3 = 0 \\
x_2 + 2x_3 = 3
\end{cases}
$$

即：
$$
\begin{cases}
x_1 = x_3 \\
x_2 = 3 - 2x_3
\end{cases}
$$

通解：
$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}
=
\begin{bmatrix}
t \\
3 - 2t \\
t
\end{bmatrix}
=
\begin{bmatrix}
0 \\
3 \\
0
\end{bmatrix}
+
t
\begin{bmatrix}
1 \\
-2 \\
1
\end{bmatrix}, \quad t \in \mathbb{R}
$$

### 例题 3：判断解的情况（无解）

**问题**：判断以下线性方程组解的情况：
$$
\begin{cases}
x_1 + x_2 + x_3 = 1 \\
x_1 + 2x_2 + 3x_3 = 2 \\
2x_1 + 3x_2 + 4x_3 = 4
\end{cases}
$$

**解**：

增广矩阵：
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
1 & 2 & 3 & 2 \\
2 & 3 & 4 & 4
\end{array}\right]
$$

高斯消元：
1. $R_2 \rightarrow R_2 - R_1$，$R_3 \rightarrow R_3 - 2R_1$
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
0 & 1 & 2 & 1 \\
0 & 1 & 2 & 2
\end{array}\right]
$$

2. $R_3 \rightarrow R_3 - R_2$
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
0 & 1 & 2 & 1 \\
0 & 0 & 0 & 1
\end{array}\right]
$$

$\text{rank}(A) = 2$，$\text{rank}([A|\mathbf{b}]) = 3$

因为 $\text{rank}(A) \neq \text{rank}([A|\mathbf{b}])$，所以方程组无解。

实际上，第三行表示 $0 \cdot x_1 + 0 \cdot x_2 + 0 \cdot x_3 = 1$，这是不可能的。

### 例题 4：齐次方程组的解

**问题**：求解齐次方程组：
$$
\begin{cases}
x_1 + 2x_2 + 3x_3 = 0 \\
2x_1 + 4x_2 + 6x_3 = 0
\end{cases}
$$

**解**：

系数矩阵：
$$
A = \begin{bmatrix}
1 & 2 & 3 \\
2 & 4 & 6
\end{bmatrix}
$$

高斯消元：
1. $R_2 \rightarrow R_2 - 2R_1$
$$
\begin{bmatrix}
1 & 2 & 3 \\
0 & 0 & 0
\end{bmatrix}
$$

$\text{rank}(A) = 1 < n = 3$，有非零解。

基本变量：$x_1$；自由变量：$x_2, x_3$。

从矩阵得到：$x_1 + 2x_2 + 3x_3 = 0$

即：$x_1 = -2x_2 - 3x_3$

通解：
$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}
=
\begin{bmatrix}
-2s - 3t \\
s \\
t
\end{bmatrix}
=
s
\begin{bmatrix}
-2 \\
1 \\
0
\end{bmatrix}
+
t
\begin{bmatrix}
-3 \\
0 \\
1
\end{bmatrix}, \quad s, t \in \mathbb{R}
$$

零空间的基：$\left\{\begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} -3 \\ 0 \\ 1 \end{bmatrix}\right\}$

验证秩-零化度定理：$\text{rank}(A) + \text{nullity}(A) = 1 + 2 = 3 = n$ ✓

### 例题 5：解的结构

**问题**：求解非齐次方程组，并表示解的结构：
$$
\begin{cases}
x_1 + x_2 + 2x_3 = 4 \\
2x_1 + 2x_2 + 4x_3 = 8
\end{cases}
$$

**解**：

增广矩阵：
$$
\left[\begin{array}{ccc|c}
1 & 1 & 2 & 4 \\
2 & 2 & 4 & 8
\end{array}\right]
$$

高斯消元：
1. $R_2 \rightarrow R_2 - 2R_1$
$$
\left[\begin{array}{ccc|c}
1 & 1 & 2 & 4 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

$\text{rank}(A) = \text{rank}([A|\mathbf{b}]) = 1 < n = 3$，有无限多解。

基本变量：$x_1$；自由变量：$x_2, x_3$。

从矩阵得到：$x_1 + x_2 + 2x_3 = 4$

即：$x_1 = 4 - x_2 - 2x_3$

通解：
$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}
=
\begin{bmatrix}
4 - s - 2t \\
s \\
t
\end{bmatrix}
=
\begin{bmatrix}
4 \\
0 \\
0
\end{bmatrix}
+
s
\begin{bmatrix}
-1 \\
1 \\
0
\end{bmatrix}
+
t
\begin{bmatrix}
-2 \\
0 \\
1
\end{bmatrix}, \quad s, t \in \mathbb{R}
$$

解的结构：
- 特解：$\mathbf{x}_p = \begin{bmatrix} 4 \\ 0 \\ 0 \end{bmatrix}$
- 齐次方程组的通解：$\mathbf{x}_h = s\begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix} + t\begin{bmatrix} -2 \\ 0 \\ 1 \end{bmatrix}$

通解：$\mathbf{x} = \mathbf{x}_p + \mathbf{x}_h$

## 习题

### 基础题

1. 求解以下线性方程组：
   $$
   \begin{cases}
   2x_1 + x_2 - x_3 = 1 \\
   3x_1 - 2x_2 + x_3 = 2 \\
   x_1 + 3x_2 - 2x_3 = 3
   \end{cases}
   $$

2. 判断以下线性方程组解的情况：
   $$
   \begin{cases}
   x_1 + 2x_2 + 3x_3 = 4 \\
   2x_1 + 4x_2 + 6x_3 = 8 \\
   3x_1 + 6x_2 + 9x_3 = 12
   \end{cases}
   $$

3. 计算矩阵 $A = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}$ 的秩。

4. 验证秩-零化度定理对于矩阵 $A = \begin{bmatrix}
1 & 1 & 2 \\
2 & 2 & 4
\end{bmatrix}$。

5. 将矩阵 $A = \begin{bmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
3 & 6 & 9
\end{bmatrix}$ 化为行阶梯形。

### 进阶题

6. 证明：行初等变换保持方程组的解集不变。

7. 设 $A$ 是 $m \times n$ 矩阵，证明：$\text{rank}(A) = \text{rank}(A^T)$。

8. 证明：如果 $A\mathbf{x} = \mathbf{b}$ 有解，且 $\text{rank}(A) = n$，则解唯一。

9. 设 $A$ 是 $n \times n$ 可逆矩阵，证明：$A\mathbf{x} = \mathbf{b}$ 有唯一解 $\mathbf{x} = A^{-1}\mathbf{b}$。

10. 证明：$\text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B))$。

### 挑战题

11. 研究条件数 $\kappa(A) = \|A\| \cdot \|A^{-1}\|$ 对线性方程组数值稳定性的影响。

12. 证明：对于任何 $m \times n$ 矩阵 $A$，存在可逆矩阵 $P$ 和 $Q$，使得 $PAQ = \begin{bmatrix}
I_r & 0 \\
0 & 0
\end{bmatrix}$，其中 $r = \text{rank}(A)$。

13. 在机器学习中，为什么使用正则化（如 Ridge 回归）来处理病态矩阵？给出具体例子。

14. 研究 QR 分解在求解线性方程组中的应用，并与高斯消元法比较。

15. 证明：如果 $A$ 是对称正定矩阵，则 Cholesky 分解 $A = LL^T$ 存在且唯一，其中 $L$ 是下三角矩阵。

## 注意事项

⚠️ **常见错误**

1. **忽略无解的情况**
   - 不是所有线性方程组都有解
   - 需要检查 $\text{rank}(A) = \text{rank}([A|\mathbf{b}])$

2. **混淆行阶梯形和简化行阶梯形**
   - 行阶梯形：主元非零，下方零
   - 简化行阶梯形：主元为1，所在列其他元素为零

3. **数值稳定性问题**
   - 直接高斯消元可能产生大的舍入误差
   - 应该使用部分选主元或完全选主元

✅ **最佳实践**

1. **使用矩阵形式**
   - $A\mathbf{x} = \mathbf{b}$ 比方程组形式更简洁
   - 便于理论分析和编程实现

2. **理解秩的几何意义**
   - 秩是列空间（或行空间）的维数
   - 秩-零化度定理：$\text{rank}(A) + \text{nullity}(A) = n$

3. **选择合适的数值方法**
   - 对于方阵：LU 分解、Cholesky 分解
   - 对于超定系统：QR 分解、SVD
   - 对于对称正定矩阵：Cholesky 分解

## 题型总结与思路技巧

### 线性方程组求解流程

#### 📋 解的判定定理（Rouché-Capelli）

设 $A$ 为 $m \times n$ 矩阵，$\tilde{A} = [A|\mathbf{b}]$ 为增广矩阵：

| 条件 | 解的情况 |
|-----|---------|
| $\text{rank}(A) \neq \text{rank}(\tilde{A})$ | 无解 |
| $\text{rank}(A) = \text{rank}(\tilde{A}) = n$ | 唯一解 |
| $\text{rank}(A) = \text{rank}(\tilde{A}) < n$ | 无穷多解 |

### 💡 核心技巧与常用结论

#### 1. 高斯消元法步骤

1. 写出增广矩阵 $[A|\mathbf{b}]$
2. 用行变换化为行阶梯形
3. 判断解的存在性
4. 若有解，回代求解或继续化为简化行阶梯形

#### 2. 解的结构

**齐次方程组 $A\mathbf{x} = \mathbf{0}$**：
- 解空间维数 = $n - \text{rank}(A)$
- 找基础解系（$n-r$个线性无关解向量）

**非齐次方程组 $A\mathbf{x} = \mathbf{b}$**：
- 通解 = 特解 + 齐次通解
- $\mathbf{x} = \mathbf{x}_p + \sum c_i \mathbf{x}_i$

#### 3. 数值方法选择

| 矩阵类型 | 推荐方法 | 特点 |
|---------|---------|------|
| 一般方阵 | LU分解 | 稳定 |
| 正定对称 | Cholesky | 高效 |
| 超定系统 | QR/SVD | 最小二乘 |
| 稀疏矩阵 | 迭代法 | 节省存储 |

#### 4. 秩-零化度定理

$$\text{rank}(A) + \text{nullity}(A) = n$$

其中 $\text{nullity}(A) = \dim(\ker A)$ 是零空间的维数。

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 判断解的存在性 | 比较秩 | $\text{rank}(A)$ vs $\text{rank}([A|b])$ |
| 求唯一解 | 高斯消元/求逆 | $A$可逆时可直接求逆 |
| 求通解 | 找特解+基础解系 | 解空间的基 |
| 求基础解系 | 齐次方程 | 自由变量个数=维数 |
| 最小二乘解 | 正则方程 | $A^TA\mathbf{x} = A^T\mathbf{b}$ |

### ⚠️ 常见错误

**错误一**：增广矩阵处理
- 判断解必须比较$A$和$[A|b]$的秩
- 不能只看$A$的秩

**错误二**：通解结构
- 非齐次通解 = 特解 + 齐次通解
- 不要忘记特解

**错误三**：自由变量选择
- 自由变量可以任意选择
- 但基础解系通常选主元列对应的非主元变量

## 本章小结

### 重要定义
1. 线性方程组：$A\mathbf{x} = \mathbf{b}$
2. 增广矩阵：$[A|\mathbf{b}]$
3. 行阶梯形和简化行阶梯形
4. 矩阵的秩：列空间或行空间的维数

### 重要定理
1. 线性方程组有解的充要条件：$\mathbf{b}$ 在 $A$ 的列空间中
2. 解的唯一性：$\text{rank}(A) = n$ 时解唯一
3. 秩-零化度定理：$\text{rank}(A) + \text{nullity}(A) = n$

### 重要方法
1. 高斯消元法
2. 行初等变换
3. 最小二乘法

### 重要应用
1. 线性回归
2. 线性分类（SVM）
3. 神经网络前向传播

本章为后续学习矩阵运算和向量空间奠定了基础。

## 相关概念

- [[08_Vectors]] - 向量基础
- [[04_Matrix_Basics]] - 矩阵基础
- [[07_Matrix_Rank]] - 矩阵的秩
- [[12_Least_Squares]] - 最小二乘法

## 参考教材

- 《线性代数》（第6版），同济大学数学系，第三章
- 《Introduction to Linear Algebra》（第5版），Gilbert Strang, Chapter 2
- 《高等代数简明教程》（第2版），北京大学数学系，第二章


