---
type: concept
topic: linear_maps
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[10_Basis_Dimension]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 23
---

# 线性映射 (Linear Maps)

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

## 1. 线性映射的定义

### 1.1 定义

映射 $T: V \to W$ 是线性的，如果满足：

1. **可加性**：$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ 对所有 $\mathbf{u}, \mathbf{v} \in V$
2. **齐次性**：$T(\lambda\mathbf{v}) = \lambda T(\mathbf{v})$ 对所有 $\mathbf{v} \in V$ 和标量 $\lambda$

**等价条件**：$T(\lambda\mathbf{u} + \mu\mathbf{v}) = \lambda T(\mathbf{u}) + \mu T(\mathbf{v})$

### 1.2 矩阵表示

如果 $T: \mathbb{R}^n \to \mathbb{R}^m$ 是线性映射，则存在唯一的 $m \times n$ 矩阵 $A$ 使得：
$$T(\mathbf{x}) = A\mathbf{x}$$

### 1.3 矩阵的计算

设 $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2, \ldots, \mathbf{b}_n\}$ 是 $\mathbb{R}^n$ 的标准基，则：
$$A = [T(\mathbf{b}_1), T(\mathbf{b}_2), \ldots, T(\mathbf{b}_n)]$$

## 2. 线性映射的子空间

### 2.1 核（Kernel）

$$\text{ker}(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}\}$$

**性质**：
- $\text{ker}(T)$ 是 $V$ 的子空间
- $T$ 是单射当且仅当 $\text{ker}(T) = \{\mathbf{0}\}$

### 2.2 像（Image）

$$\text{im}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\}$$

**性质**：
- $\text{im}(T)$ 是 $W$ 的子空间
- $T$ 是满射当且仅当 $\text{im}(T) = W$

## 3. 线性映射的运算

### 3.1 线性映射的和

$(S + T)(\mathbf{v}) = S(\mathbf{v}) + T(\mathbf{v})$

### 3.2 标量乘法

$(\lambda T)(\mathbf{v}) = \lambda T(\mathbf{v})$

### 3.3 复合映射

$(S \circ T)(\mathbf{v}) = S(T(\mathbf{v}))$

### 3.4 逆映射

如果 $T$ 是可逆的（双射），则存在 $T^{-1}$ 使得：
$$T^{-1}(T(\mathbf{v})) = \mathbf{v}, \quad T(T^{-1}(\mathbf{w})) = \mathbf{w}$$

## 代码示例

```python
import numpy as np

def linear_map(A, x):
    """定义线性映射 T(x) = Ax"""
    return A @ x

# 示例
A = np.array([[1, 2], [3, 4]])
T = lambda x: linear_map(A, x)

print(f"矩阵 A:\n{A}")
print(f"\nT([1, 0]) = {T(np.array([1, 0]))}")
print(f"T([0, 1]) = {T(np.array([0, 1]))}")
```

## 机器学习应用

### 应用 1：神经网络中的线性映射

神经网络的全连接层是线性映射。

## 严格证明

### 证明：线性映射的矩阵表示唯一性

**定理**：如果 $T: \mathbb{R}^n \to \mathbb{R}^m$ 是线性映射，则存在唯一的 $m \times n$ 矩阵 $A$ 使得 $T(\mathbf{x}) = A\mathbf{x}$。

**证明**：

**存在性**：设 $\mathcal{E} = \{\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n\}$ 是 $\mathbb{R}^n$ 的标准基。定义 $A = [T(\mathbf{e}_1), T(\mathbf{e}_2), \ldots, T(\mathbf{e}_n)]$。对于任意 $\mathbf{x} = [x_1, x_2, \ldots, x_n]^T = \sum_{i=1}^n x_i \mathbf{e}_i$：$T(\mathbf{x}) = T\left(\sum_{i=1}^n x_i \mathbf{e}_i\right) = \sum_{i=1}^n x_i T(\mathbf{e}_i) = A\mathbf{x}$

**唯一性**：假设存在矩阵 $B$ 使得 $T(\mathbf{x}) = B\mathbf{x}$ 对所有 $\mathbf{x}$。特别地，对于 $\mathbf{e}_i$：$T(\mathbf{e}_i) = B\mathbf{e}_i = B[:, i]$。因此 $A[:, i] = T(\mathbf{e}_i) = B[:, i]$ 对所有 $i$ 成立，故 $A = B$。

## 例题

### 例题 1：判断线性性

**问题**：判断以下映射是否线性：

1. $T(x, y) = (2x + 3y, x - y)$
2. $T(x, y) = (x^2, y^2)$

**解**：

1. **线性**：可加性和齐次性都成立。

2. **非线性**：$T(2(x, y)) = (4x^2, 4y^2) \neq 2T(x, y) = (2x^2, 2y^2)$（除非 $x = y = 0$）。

### 例题 2：矩阵表示

**问题**：求 $T(x, y) = (x + 2y, 3x - y)$ 的矩阵表示。

**解**：

计算基向量的像：
$T(1, 0) = (1, 3)$
$T(0, 1) = (2, -1)$

因此 $A = \begin{bmatrix} 1 & 2 \\ 3 & -1 \end{bmatrix}$。

验证：$A\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 3 & -1 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} x + 2y \\ 3x - y \end{bmatrix} = T(x, y)$ ✓

### 例题 3：核和像

**问题**：设 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$，求 $T(\mathbf{x}) = A\mathbf{x}$ 的核和像。

**解**：

**核**：解 $A\mathbf{x} = \mathbf{0}$：
$\begin{cases} x_1 + 2x_2 = 0 \\ 3x_1 + 4x_2 = 0 \end{cases}$

从第一个方程：$x_1 = -2x_2$

代入第二个：$3(-2x_2) + 4x_2 = -2x_2 = 0$，所以 $x_2 = 0$，$x_1 = 0$。

因此 $\text{ker}(T) = \{\mathbf{0}\}$，$T$ 是单射。

**像**：$\text{im}(T) = \text{Col}(A)$

由于 $A$ 的列向量线性无关，$\text{im}(T) = \mathbb{R}^2$，$T$ 是满射。

### 例题 4：复合映射

**问题**：设 $T(x, y) = (x + y, x - y)$，$S(u, v) = (2u, 3v)$，求 $S \circ T$ 的矩阵表示。

**解**：

$T$ 的矩阵：$A = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$

$S$ 的矩阵：$B = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$

$S \circ T$ 的矩阵：$BA = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} = \begin{bmatrix} 2 & 2 \\ 3 & -3 \end{bmatrix}$

验证：$(S \circ T)(x, y) = S(x + y, x - y) = (2(x + y), 3(x - y)) = (2x + 2y, 3x - 3y)$

$BA\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2 & 2 \\ 3 & -3 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2x + 2y \\ 3x - 3y \end{bmatrix}$ ✓

### 例题 5：可逆映射

**问题**：判断 $T(x, y) = (2x + y, x + 2y)$ 是否可逆，如果可逆，求 $T^{-1}$。

**解**：

$T$ 的矩阵：$A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$

$\det(A) = 4 - 1 = 3 \neq 0$，所以 $A$ 可逆，$T$ 可逆。

$A^{-1} = \frac{1}{3}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$

因此 $T^{-1}(u, v) = \frac{1}{3}(2u - v, -u + 2v)$

验证：$T^{-1}(T(x, y)) = T^{-1}(2x + y, x + 2y) = \frac{1}{3}(2(2x + y) - (x + 2y), -(2x + y) + 2(x + 2y)) = \frac{1}{3}(3x, 3y) = (x, y)$ ✓

## 习题

### 基础题

1. 判断 $T(x, y, z) = (x + y, y + z, z + x)$ 是否线性。

2. 设 $T(x, y) = (x + 2y, 3x - y)$，求 $T$ 的矩阵表示。

3. 设 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$，求 $T(\mathbf{x}) = A\mathbf{x}$ 的核和像。

4. 证明：线性映射的复合是线性映射。

5. 证明：如果 $T$ 可逆，则 $T^{-1}$ 也是线性映射。

### 进阶题

6. 证明：线性映射的矩阵表示唯一性。

7. 证明：$\dim(\text{im}(T)) + \dim(\text{ker}(T)) = \dim(V)$（秩-零化度定理）。

8. 证明：$T$ 是单射当且仅当 $\text{ker}(T) = \{\mathbf{0}\}$。

9. 证明：$T$ 是满射当且仅当 $\text{im}(T) = W$。

10. 设 $T_1, T_2$ 是线性映射，证明 $T_1 + T_2$ 和 $\lambda T_1$ 也是线性映射。

### 挑战题

11. 研究算子范数的定义和性质。

12. 证明：有限维向量空间上的线性映射都是连续的。

13. 在深度学习中，为什么线性层需要配合激活函数？

14. 研究卷积神经网络（CNN）中的卷积层作为线性映射的性质。

15. 证明：如果 $T$ 是线性映射，则 $T$ 在不同基下的矩阵表示相似。

## 题型总结与思路技巧

### 线性映射核心要点

#### 📋 线性映射的判定

**定义**：$T: V \to W$满足
- $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
- $T(c\mathbf{u}) = cT(\mathbf{u})$

#### 📋 核心概念

| 概念 | 定义 | 维数关系 |
|-----|------|---------|
| **核** | $\ker T = \{\mathbf{v} : T(\mathbf{v}) = \mathbf{0}\}$ | $\dim(\ker T) = \text{nullity}(T)$ |
| **像** | $\text{Im } T = \{T(\mathbf{v}) : \mathbf{v} \in V\}$ | $\dim(\text{Im } T) = \text{rank}(T)$ |
| **秩-零化度** | $\text{rank}(T) + \text{nullity}(T) = \dim V$ | 维数定理 |

### 💡 核心技巧与常用结论

#### 1. 矩阵表示

**定理**：线性映射$T$在基$\mathcal{B}_V$和$\mathcal{B}_W$下的矩阵$[T]_{\mathcal{B}_V}^{\mathcal{B}_W}$

$$[T(\mathbf{v})]_{\mathcal{B}_W} = [T]_{\mathcal{B}_V}^{\mathcal{B}_W} [\mathbf{v}]_{\mathcal{B}_V}$$

#### 2. 线性映射与矩阵

- 固定基后，线性映射与矩阵一一对应
- 不同基下的矩阵相似

#### 3. 同构

**定理**：$V \cong W$ 当且仅当 $\dim V = \dim W$

#### 4. 逆映射

$T$可逆 $\Leftrightarrow$ $T$是双射 $\Leftrightarrow$ $\ker T = \{\mathbf{0}\}$ 且 $\text{Im } T = W$

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 判定线性映射 | 验证两条性质 | 可加性、齐次性 |
| 求矩阵表示 | 基向量的像 | 列向量构成矩阵 |
| 求核 | 解$T(\mathbf{v}) = \mathbf{0}$ | 齐次方程组 |
| 求像 | 找生成集 | 极大线性无关组 |
| 证明同构 | 构造双射 | 维数相等 |

### ⚠️ 常见错误

**错误一**：混淆核与零空间
- 核是定义域的子空间
- 零空间通常指矩阵的核

**错误二**：秩-零化度定理
- $\text{rank} + \text{nullity} = \dim(\text{定义域})$
- 不是$\dim(\text{值域})$

**错误三**：矩阵表示
- 矩阵的列是基向量的像的坐标
- 需要明确使用哪组基

## 相关概念

- [[10_Basis_Dimension]] - 基与维数
- [[12_Least_Squares]] - 最小二乘法
- [[04_Matrix_Operations]] - 矩阵运算

## 参考教材

- 《线性代数》（第6版），同济大学数学系，第七章
- 《Introduction to Linear Algebra》（第5版），Gilbert Strang, Chapter 3


