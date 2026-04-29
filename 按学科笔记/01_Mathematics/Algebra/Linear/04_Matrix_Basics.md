---
type: concept
topic: matrix_basics
category: linear_algebra
difficulty: beginner
prerequisites:
  - [[02_Linear_Equations]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 04
---

# 矩阵基础 (Matrix Basics)

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

## 1. 矩阵的定义

### 1.1 基本定义

矩阵是一个 $m \times n$ 的数字排列：
$$A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}$$

其中 $a_{ij}$ 表示第 $i$ 行第 $j$ 列的元素。

### 1.2 特殊矩阵

#### 1. 方阵

行数等于列数的矩阵，即 $m = n$。

#### 2. 对角矩阵

非对角线元素为零的方阵：
$$D = \begin{bmatrix}
d_1 & 0 & \cdots & 0 \\
0 & d_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & d_n
\end{bmatrix}$$

#### 3. 单位矩阵

对角线元素为1，其他元素为0的对角矩阵：
$$I_n = \begin{bmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{bmatrix}$$

#### 4. 零矩阵

所有元素均为零的矩阵。

#### 5. 对称矩阵

满足 $A^T = A$ 的方阵，即 $a_{ij} = a_{ji}$。

#### 6. 反对称矩阵

满足 $A^T = -A$ 的方阵，即 $a_{ij} = -a_{ji}$，且 $a_{ii} = 0$。

#### 7. 正交矩阵

满足 $A^T A = AA^T = I$ 的方阵。

## 2. 矩阵运算

### 2.1 矩阵加法

两个同阶矩阵可以相加：
$$C = A + B, \quad c_{ij} = a_{ij} + b_{ij}$$

**性质**：
- 交换律：$A + B = B + A$
- 结合律：$(A + B) + C = A + (B + C)$
- 零元素：$A + O = A$

### 2.2 标量乘法

标量 $\lambda$ 乘以矩阵 $A$：
$$C = \lambda A, \quad c_{ij} = \lambda a_{ij}$$

**性质**：
- 分配律：$\lambda(A + B) = \lambda A + \lambda B$
- 结合律：$(\lambda \mu)A = \lambda(\mu A)$
- 单位元：$1 \cdot A = A$

### 2.3 矩阵乘法

矩阵 $A \in \mathbb{R}^{m \times n}$ 与矩阵 $B \in \mathbb{R}^{n \times p}$ 相乘：
$$C = AB \in \mathbb{R}^{m \times p}, \quad c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$$

**重要性质**：
- **不满足交换律**：$AB \neq BA$（一般情况）
- 结合律：$(AB)C = A(BC)$
- 分配律：$A(B + C) = AB + AC$
- 单位矩阵：$I_m A = A I_n = A$

### 2.4 矩阵转置

矩阵 $A \in \mathbb{R}^{m \times n}$ 的转置 $A^T \in \mathbb{R}^{n \times m}$：
$$(A^T)_{ij} = A_{ji}$$

**性质**：
- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(\lambda A)^T = \lambda A^T$
- $(AB)^T = B^T A^T$

### 2.5 矩阵的迹

方阵 $A$ 的迹是主对角线元素之和：
$$\text{tr}(A) = \sum_{i=1}^n a_{ii}$$

**性质**：
- $\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)$
- $\text{tr}(\lambda A) = \lambda \text{tr}(A)$
- $\text{tr}(AB) = \text{tr}(BA)$
- $\text{tr}(A^T) = \text{tr}(A)$

## 3. 代码示例

### 3.1 基本矩阵运算

```python
import numpy as np

# 创建矩阵
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"矩阵 A:\n{A}")
print(f"矩阵 B:\n{B}")

# 矩阵加法
C = A + B
print(f"A + B =\n{C}")

# 标量乘法
D = 2 * A
print(f"2A =\n{D}")

# 矩阵乘法
E = A @ B  # 或 np.dot(A, B)
print(f"A @ B =\n{E}")

# 矩阵转置
A_T = A.T
print(f"A^T =\n{A_T}")

# 迹
trace_A = np.trace(A)
print(f"tr(A) = {trace_A}")

# 验证性质
print(f"tr(AB) = {np.trace(A @ B):.2f}")
print(f"tr(BA) = {np.trace(B @ A):.2f}")
```

### 3.2 特殊矩阵的创建

```python
import numpy as np

# 单位矩阵
I3 = np.eye(3)
print(f"3×3单位矩阵:\n{I3}")

# 零矩阵
Z2_3 = np.zeros((2, 3))
print(f"2×3零矩阵:\n{Z2_3}")

# 对角矩阵
D = np.diag([1, 2, 3, 4])
print(f"对角矩阵:\n{D}")

# 对称矩阵
S = np.array([[1, 2, 3],
              [2, 5, 6],
              [3, 6, 9]])
print(f"对称矩阵:\n{S}")
print(f"是否对称: {np.allclose(S, S.T)}")

# 反对称矩阵
K = np.array([[0, 1, 2],
              [-1, 0, 3],
              [-2, -3, 0]])
print(f"反对称矩阵:\n{K}")
print(f"是否反对称: {np.allclose(K, -K.T)}")
```

## 4. 例题

### 例题 1：矩阵加法和标量乘法

**问题**：设 $A = \begin{bmatrix} 1 & 2 \\\\ 3 & 4 \end{bmatrix}$，$B = \begin{bmatrix} 5 & 6 \\\\ 7 & 8 \end{bmatrix}$，计算：
(1) $A + B$
(2) $2A - 3B$

**解**：

(1) $A + B = \begin{bmatrix} 1+5 & 2+6 \\\\ 3+7 & 4+8 \end{bmatrix} = \begin{bmatrix} 6 & 8 \\\\ 10 & 12 \end{bmatrix}$

(2) $2A - 3B = 2\begin{bmatrix} 1 & 2 \\\\ 3 & 4 \end{bmatrix} - 3\begin{bmatrix} 5 & 6 \\\\ 7 & 8 \end{bmatrix}$

$= \begin{bmatrix} 2 & 4 \\\\ 6 & 8 \end{bmatrix} - \begin{bmatrix} 15 & 18 \\\\ 21 & 24 \end{bmatrix} = \begin{bmatrix} -13 & -14 \\\\ -15 & -16 \end{bmatrix}$

### 例题 2：矩阵乘法

**问题**：设 $A = \begin{bmatrix} 1 & 2 \\\\ 3 & 4 \end{bmatrix}$，$B = \begin{bmatrix} 5 & 6 \\\\ 7 & 8 \end{bmatrix}$，计算 $AB$ 和 $BA$，并比较它们是否相等。

**解**：

$$AB = \begin{bmatrix} 1 & 2 \\\\ 3 & 4 \end{bmatrix} \begin{bmatrix} 5 & 6 \\\\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 1×5+2×7 & 1×6+2×8 \\\\ 3×5+4×7 & 3×6+4×8 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\\\ 43 & 50 \end{bmatrix}$$

$$BA = \begin{bmatrix} 5 & 6 \\\\ 7 & 8 \end{bmatrix} \begin{bmatrix} 1 & 2 \\\\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 5×1+6×3 & 5×2+6×4 \\\\ 7×1+8×3 & 7×2+8×4 \end{bmatrix} = \begin{bmatrix} 23 & 34 \\\\ 31 & 46 \end{bmatrix}$$

**结论**：$AB \neq BA$，矩阵乘法不满足交换律。

### 例题 3：矩阵转置

**问题**：设 $A = \begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \end{bmatrix}$，计算 $A^T$ 和 $(A^T)^T$。

**解**：

$$A^T = \begin{bmatrix} 1 & 4 \\\\ 2 & 5 \\\\ 3 & 6 \end{bmatrix}$$

$$(A^T)^T = \begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \end{bmatrix} = A$$

**结论**：$(A^T)^T = A$，符合转置的性质。

### 例题 4：矩阵的迹

**问题**：设 $A = \begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 9 \end{bmatrix}$，计算 $\text{tr}(A)$。

**解**：

$$\text{tr}(A) = 1 + 5 + 9 = 15$$

### 例题 5：对称矩阵的判定

**问题**：判断 $A = \begin{bmatrix} 1 & 2 & 3 \\\\ 2 & 5 & 6 \\\\ 3 & 6 & 9 \end{bmatrix}$ 是否为对称矩阵。

**解**：

计算 $A^T$：
$$A^T = \begin{bmatrix} 1 & 2 & 3 \\\\ 2 & 5 & 6 \\\\ 3 & 6 & 9 \end{bmatrix}$$

由于 $A^T = A$，因此 $A$ 是对称矩阵。

### 例题 6：反对称矩阵的判定

**问题**：判断 $B = \begin{bmatrix} 0 & 1 & 2 \\\\ -1 & 0 & 3 \\\\ -2 & -3 & 0 \end{bmatrix}$ 是否为反对称矩阵。

**解**：

计算 $B^T$：
$$B^T = \begin{bmatrix} 0 & -1 & -2 \\\\ 1 & 0 & -3 \\\\ 2 & 3 & 0 \end{bmatrix} = -\begin{bmatrix} 0 & 1 & 2 \\\\ -1 & 0 & 3 \\\\ -2 & -3 & 0 \end{bmatrix} = -B$$

由于 $B^T = -B$，因此 $B$ 是反对称矩阵。

### 例题 7：正交矩阵的判定

**问题**：判断 $Q = \begin{bmatrix} \cos\theta & -\sin\theta \\\\ \sin\theta & \cos\theta \end{bmatrix}$ 是否为正交矩阵。

**解**：

计算 $Q^T Q$：
$$Q^T Q = \begin{bmatrix} \cos\theta & \sin\theta \\\\ -\sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} \cos\theta & -\sin\theta \\\\ \sin\theta & \cos\theta \end{bmatrix}$$

$$= \begin{bmatrix} \cos^2\theta + \sin^2\theta & -\cos\theta\sin\theta + \sin\theta\cos\theta \\\\ -\sin\theta\cos\theta + \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta \end{bmatrix} = \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix} = I$$

因此 $Q$ 是正交矩阵（这是旋转矩阵）。

## 5. 机器学习应用

### 应用 1：权重矩阵

在神经网络中，权重矩阵连接不同层的神经元。

```python
import numpy as np

# 定义神经网络结构
input_size = 784    # MNIST 图像：28×28
hidden_size = 128   # 隐藏层神经元数
output_size = 10    # 输出类别数

# 权重矩阵
W1 = np.random.randn(input_size, hidden_size) * 0.01  # 输入层到隐藏层
b1 = np.zeros((1, hidden_size))                      # 隐藏层偏置

W2 = np.random.randn(hidden_size, output_size) * 0.01  # 隐藏层到输出层
b2 = np.zeros((1, output_size))                       # 输出层偏置

# 前向传播
def forward(X):
    """前向传播"""
    # 隐藏层
    Z1 = X @ W1 + b1
    A1 = np.maximum(0, Z1)  # ReLU 激活

    # 输出层
    Z2 = A1 @ W2 + b2
    A2 = 1 / (1 + np.exp(-Z2))  # Sigmoid 激活

    return A2

# 测试
X = np.random.randn(32, 784)  # 32 个样本
output = forward(X)

print(f"输入形状: {X.shape}")
print(f"输出形状: {output.shape}")
print(f"输出范围: [{output.min():.4f}, {output.max():.4f}]")
```

### 应用 2：协方差矩阵

协方差矩阵描述数据中各变量之间的关系。

```python
import numpy as np

# 生成数据
np.random.seed(42)
n_samples = 1000
n_features = 3

X = np.random.randn(n_samples, n_features)
X[:, 0] *= 2  # 第一个特征的方差更大
X[:, 1] = 0.5 * X[:, 0] + 0.5 * np.random.randn(n_samples)  # 第一个和第二个特征相关

# 计算协方差矩阵
mean = np.mean(X, axis=0)
X_centered = X - mean
cov_matrix = (X_centered.T @ X_centered) / (n_samples - 1)

print(f"协方差矩阵:\n{cov_matrix}")

# 使用 NumPy 验证
cov_matrix_np = np.cov(X.T)
print(f"NumPy 协方差矩阵:\n{cov_matrix_np}")

print(f"相等: {np.allclose(cov_matrix, cov_matrix_np)}")
```

## 题型总结与思路技巧

### 特殊矩阵的识别与性质

#### 📋 特殊矩阵类型识别

| 矩阵类型 | 定义条件 | 关键性质 |
|---------|---------|---------|
| **对称矩阵** | $A^T = A$ | 特征值为实数，可正交对角化 |
| **反对称矩阵** | $A^T = -A$ | 对角线全为0，奇数阶行列式为0 |
| **正交矩阵** | $Q^T Q = I$ | $\det Q = \pm 1$，保持向量长度 |
| **对角矩阵** | 非对角元全为0 | 运算简单，$\det = \prod \lambda_i$ |
| **三角矩阵** | 上/下三角 | $\det = \prod$ 对角元 |

### 💡 核心技巧与常用结论

#### 1. 矩阵运算要点

**矩阵乘法**：
- 不满足交换律：$AB \neq BA$（一般情况）
- 满足结合律：$(AB)C = A(BC)$
- 转置法则：$(AB)^T = B^T A^T$

**特殊矩阵的运算**：
- 对称矩阵之和仍对称
- 正交矩阵之积仍正交
- 对角矩阵之积对应元素相乘

#### 2. 矩阵类型的判定

**判定对称矩阵**：检查 $a_{ij} = a_{ji}$

**判定反对称矩阵**：
- 对角元 $a_{ii} = 0$
- $a_{ij} = -a_{ji}$

**判定正交矩阵**：
- 方法一：验证 $Q^T Q = I$
- 方法二：各行/列向量单位正交

#### 3. 常见矩阵构造

**零矩阵**：$O_{m×n}$

**单位矩阵**：$I_n$ 或 $E_n$

**对角矩阵**：$\text{diag}(\lambda_1, \ldots, \lambda_n)$

**旋转矩阵**（2D）：
$$\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$

**对称分解**：任意方阵可分解为
$$A = \frac{A+A^T}{2} + \frac{A-A^T}{2}$$（对称部分 + 反对称部分）

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 矩阵运算 | 按定义计算 | 注意维数匹配 |
| 判定矩阵类型 | 验证定义条件 | 特殊元素检查 |
| 证明矩阵性质 | 利用定义推导 | 转置性质 |
| 构造特殊矩阵 | 按需求设计 | 参数化表达 |

### ⚠️ 常见错误

**错误一**：矩阵乘法交换律
- ❌ $AB = BA$
- ✅ 矩阵乘法一般不可交换

**错误二**：转置乘积顺序
- ❌ $(AB)^T = A^T B^T$
- ✅ $(AB)^T = B^T A^T$

**错误三**：正交矩阵行列式
- ❌ $\det(Q) = 1$
- ✅ $\det(Q) = \pm 1$

## 6. 课后练习

### 6.1 基础题

**教材参考**：《高等代数简明教程》第二章习题

1. 设 $A = \begin{bmatrix} 1 & 0 \\\\ 2 & 3 \end{bmatrix}$，$B = \begin{bmatrix} 4 & 1 \\\\ 0 & 2 \end{bmatrix}$，计算：
   - (1) $A + B$
   - (2) $2A - B$
   - (3) $AB$
   - (4) $BA$

2. 设 $A = \begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \end{bmatrix}$，计算 $A^T$ 和 $(A^T)^T$。

3. 计算 $A = \begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 9 \end{bmatrix}$ 的迹。

### 6.2 进阶题

**教材参考**：《高等代数简明教程》第二章习题

4. 设 $A$ 和 $B$ 都是 $n$ 阶方阵，证明 $\text{tr}(AB) = \text{tr}(BA)$。

5. 判断下列矩阵是否为对称矩阵、反对称矩阵或都不是：
   - (1) $A = \begin{bmatrix} 1 & 2 \\\\ 2 & 3 \end{bmatrix}$
   - (2) $B = \begin{bmatrix} 0 & 1 \\\\ -1 & 0 \end{bmatrix}$
   - (3) $C = \begin{bmatrix} 1 & 2 \\\\ 3 & 4 \end{bmatrix}$

6. 证明：任何方阵都可以表示为一个对称矩阵和一个反对称矩阵的和。

### 6.3 挑战题

**教材参考**：《高等代数简明教程》第二章习题

7. 设 $A$ 是 $n$ 阶方阵，证明 $\text{tr}(A^k) = \sum_{i=1}^n \lambda_i^k$，其中 $\lambda_i$ 是 $A$ 的特征值。

8. 在图像处理中，卷积操作可以用矩阵乘法表示。研究如何将一个 $3 \times 3$ 的卷积核表示为矩阵，并应用于图像。

9. 设 $A$ 是正交矩阵，证明 $|\det(A)| = 1$。

## 7. 教材参考

### 国内教材
1. **《高等代数简明教程》（第2版）** - 北京大学数学系
   - 第二章：矩阵
   - 重点：矩阵运算、特殊矩阵

2. **《线性代数》（第6版）** - 同济大学数学系
   - 第二章：矩阵及其运算
   - 重点：矩阵乘法、转置

### 国外教材
3. **《Introduction to Linear Algebra》（第5版）** - Gilbert Strang
   - Chapter 1: Vectors and Linear Combinations
   - 重点：矩阵的几何意义

4. **《Linear Algebra Done Right》（第3版）** - Sheldon Axler
   - Chapter 3: Linear Maps
   - 重点：矩阵表示

## 8. 本章小结

### 8.1 重要定义
1. 矩阵：数字的矩形排列
2. 特殊矩阵：方阵、对角矩阵、单位矩阵、对称矩阵、反对称矩阵、正交矩阵
3. 矩阵的迹：主对角线元素之和

### 8.2 重要运算
1. 矩阵加法：对应元素相加
2. 标量乘法：每个元素乘以标量
3. 矩阵乘法：$c_{ij} = \sum_{k} a_{ik} b_{kj}$
4. 矩阵转置：$(A^T)_{ij} = A_{ji}$

### 8.3 重要性质
1. 矩阵乘法满足结合律和分配律，但不满足交换律
2. $(AB)^T = B^T A^T$
3. $\text{tr}(AB) = \text{tr}(BA)$

### 8.4 重要应用
1. 神经网络的权重矩阵
2. 协方差矩阵
3. 图像卷积

---

**创建时间：2026年3月11日**  
**最后更新：2026年3月11日**  
**参考教材**：《高等代数简明教程》、《Introduction to Linear Algebra》

## 相关概念

- [[05_Matrix_Operations]] - 矩阵运算
- [[06_Inverse_Matrix]] - 逆矩阵
- [[07_Rank]] - 矩阵的秩
- [[01_Determinants]] - 行列式


