---
type: concept
topic: pseudoinverse
category: linear_algebra
difficulty: advanced
prerequisites:
  - [[21_SVD]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 22
---

# 伪逆与广义逆 (Pseudoinverse)

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

### 1.1 Moore-Penrose 伪逆

对于任意 $m \times n$ 矩阵 $A$，伪逆 $A^+$ 是唯一的 $n \times m$ 矩阵，满足以下四个条件（Moore-Penrose 条件）：

1. **$AA^+A = A$**
2. **$A^+AA^+ = A^+$**
3. **$(AA^+)^T = AA^+$**（对称性）
4. **$(A^+A)^T = A^+A$**（对称性）

### 1.2 计算（SVD 方法）

使用 SVD：$A = U\Sigma V^T$，则：
$$A^+ = V\Sigma^+ U^T$$

其中 $\Sigma^+$ 是 $\Sigma$ 的伪逆，通过对角线上非零元素取倒数然后转置得到。

### 1.3 其他计算方法

**满秩情况**：
- 如果 $m \geq n$ 且 $\text{rank}(A) = n$（列满秩）：$A^+ = (A^T A)^{-1} A^T$
- 如果 $m \leq n$ 且 $\text{rank}(A) = m$（行满秩）：$A^+ = A^T (AA^T)^{-1}$

## 2. 性质

### 2.1 基本性质

1. **唯一性**：对于任意矩阵 $A$，伪逆 $A^+$ 唯一
2. **对称性**：$(A^+)^+ = A$
3. **幂等性**：$A A^+$ 和 $A^+ A$ 都是投影矩阵
4. **转置关系**：$(A^T)^+ = (A^+)^T$

### 2.2 与逆矩阵的关系

如果 $A$ 是 $n \times n$ 可逆矩阵，则 $A^+ = A^{-1}$。

### 2.3 解的性质

对于方程组 $A\mathbf{x} = \mathbf{b}$：
- 如果有解，$\mathbf{x} = A^+\mathbf{b}$ 给出最小范数解
- 如果无解，$\mathbf{x} = A^+\mathbf{b}$ 给出最小二乘解中的最小范数解

### 2.4 投影矩阵

- $P = AA^+$ 是 $\text{Col}(A)$ 上的投影矩阵
- $Q = A^+ A$ 是 $\text{Col}(A^T)$ 上的投影矩阵

## 3. 应用

### 3.1 最小二乘解

$\mathbf{x} = A^+\mathbf{b}$ 给出 $\min \|A\mathbf{x} - \mathbf{b}\|^2$ 的最小范数解。

### 3.2 欠定系统

对于欠定系统（无限多解），$A^+\mathbf{b}$ 给出最小范数解。

### 3.3 超定系统

对于超定系统（无解），$A^+\mathbf{b}$ 给出最小二乘解。

### 3.4 最小范数解

在所有解中，$\mathbf{x} = A^+\mathbf{b}$ 的范数最小。

## 代码示例

### 示例 1：计算伪逆

```python
import numpy as np

def pseudoinverse_svd(A, tolerance=1e-10):
    """使用SVD计算伪逆"""
    U, S, Vt = np.linalg.svd(A, full_matrices=False)

    # 计算伪逆
    S_plus = np.zeros((Vt.shape[0], U.shape[0]), dtype=float)
    for i in range(len(S)):
        if S[i] > tolerance:
            S_plus[i, i] = 1 / S[i]

    A_plus = Vt.T @ S_plus @ U.T

    return A_plus

# 示例
A = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
A_plus = pseudoinverse_svd(A)

print(f"矩阵 A:\n{A}")
print(f"\n伪逆 A^+:\n{A_plus}")

# 验证Moore-Penrose条件
print(f"\n验证 Moore-Penrose 条件:")
print(f"1. AA^+A = A: {np.allclose(A @ A_plus @ A, A)}")
print(f"2. A^+AA^+ = A^+: {np.allclose(A_plus @ A @ A_plus, A_plus)}")
print(f"3. (AA^+)^T = AA^+: {np.allclose((A @ A_plus).T, A @ A_plus)}")
print(f"4. (A^+A)^T = A^+A: {np.allclose((A_plus @ A).T, A_plus @ A)}")
```

### 示例 2：最小二乘解

```python
import numpy as np

def least_squares_pseudoinverse(A, b):
    """使用伪逆求解最小二乘问题"""
    A_plus = pseudoinverse_svd(A)
    x = A_plus @ b
    return x

# 示例：超定系统
A = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
b = np.array([3, 7, 11], dtype=float)

x = least_squares_pseudoinverse(A, b)

print(f"系数矩阵 A:\n{A}")
print(f"\n常数向量 b: {b}")
print(f"\n最小二乘解 x: {x}")
print(f"\n残差: {np.linalg.norm(A @ x - b):.6f}")

# 验证投影
projection = A @ A_plus @ b
print(f"\n投影到 Col(A): {projection}")
```

### 示例 3：欠定系统

```python
import numpy as np

# 示例：欠定系统
A = np.array([[1, 1, 1], [1, 1, 1]], dtype=float)
b = np.array([2, 2], dtype=float)

A_plus = pseudoinverse_svd(A)
x = A_plus @ b

print(f"系数矩阵 A:\n{A}")
print(f"\n常数向量 b: {b}")
print(f"\n最小范数解 x: {x}")
print(f"\n解的范数: {np.linalg.norm(x):.6f}")

# 验证解的正确性
print(f"\n验证 Ax = b: {np.allclose(A @ x, b)}")

# 构造另一个解
x2 = np.array([2, 0, 0])
print(f"\n另一个解 x2: {x2}")
print(f"x2 的范数: {np.linalg.norm(x2):.6f}")
print(f"x2 也是解: {np.allclose(A @ x2, b)}")
print(f"x 的范数更小: {np.linalg.norm(x) < np.linalg.norm(x2)}")
```

### 示例 4：投影矩阵

```python
import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
A_plus = pseudoinverse_svd(A)

# 投影矩阵
P_col_A = A @ A_plus  # Col(A) 上的投影
P_col_AT = A_plus @ A  # Col(A^T) 上的投影

print(f"Col(A) 上的投影矩阵:\n{P_col_A}")
print(f"\nCol(A^T) 上的投影矩阵:\n{P_col_AT}")

# 验证幂等性
print(f"\nP_col_A 是幂等的: {np.allclose(P_col_A @ P_col_A, P_col_A)}")
print(f"P_col_AT 是幂等的: {np.allclose(P_col_AT @ P_col_AT, P_col_AT)}")

# 验证对称性
print(f"\nP_col_A 是对称的: {np.allclose(P_col_A.T, P_col_A)}")
print(f"P_col_AT 是对称的: {np.allclose(P_col_AT.T, P_col_AT)}")
```

### 示例 5：可逆矩阵的伪逆

```python
import numpy as np

# 可逆矩阵
A = np.array([[2, 1], [1, 2]], dtype=float)

# 伪逆
A_plus = pseudoinverse_svd(A)

# 逆矩阵
A_inv = np.linalg.inv(A)

print(f"矩阵 A:\n{A}")
print(f"\n伪逆 A^+:\n{A_plus}")
print(f"\n逆矩阵 A^{-1}:\n{A_inv}")
print(f"\nA^+ = A^{-1}: {np.allclose(A_plus, A_inv)}")
```

## 机器学习应用

### 应用 1：线性回归

使用伪逆求解线性回归。

### 应用 2：岭回归

岭回归是正则化的最小二乘问题。

## 严格证明

### 证明：伪逆的唯一性

**定理**：对于任意矩阵 $A$，满足 Moore-Penrose 条件的矩阵 $A^+$ 唯一。

**证明**：

假设 $X$ 和 $Y$ 都满足 Moore-Penrose 条件。证明 $X = Y$。

由条件1和3：
$AXA = A$，$(AX)^T = AX$

因此 $AX$ 是对称的投影矩阵。

类似地，$AY$ 也是对称的投影矩阵。

可以证明 $AX = AY$，进一步得到 $X = Y$。

## 例题

### 例题 1：计算伪逆

**问题**：计算 $A = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ 的伪逆。

**解**：

$A^T A = [1, 2, 3]\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} = 14$

$(A^T A)^{-1} = \frac{1}{14}$

$A^+ = (A^T A)^{-1} A^T = \frac{1}{14}[1, 2, 3] = [\frac{1}{14}, \frac{1}{7}, \frac{3}{14}]$

### 例题 2：最小二乘解

**问题**：用伪逆求解 $\min \|A\mathbf{x} - \mathbf{b}\|^2$，其中 $A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}$，$\mathbf{b} = \begin{bmatrix} 2 \\ 3 \\ 5 \end{bmatrix}$。

**解**：

$A^T A = \begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}$

$(A^T A)^{-1} = \frac{1}{6}\begin{bmatrix} 14 & -6 \\ -6 & 3 \end{bmatrix}$

$A^+ = (A^T A)^{-1} A^T = \frac{1}{6}\begin{bmatrix} 14 & -6 \\ -6 & 3 \end{bmatrix}\begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix} = \frac{1}{6}\begin{bmatrix} 8 & 2 & -4 \\ -3 & 0 & 3 \end{bmatrix}$

解：$\mathbf{x} = A^+ \mathbf{b} = \frac{1}{6}\begin{bmatrix} 8 & 2 & -4 \\ -3 & 0 & 3 \end{bmatrix}\begin{bmatrix} 2 \\ 3 \\ 5 \end{bmatrix} = \frac{1}{6}\begin{bmatrix} 2 \\ 9 \end{bmatrix} = \begin{bmatrix} 1/3 \\ 3/2 \end{bmatrix}$

### 例题 3：欠定系统的最小范数解

**问题**：求 $\begin{cases} x_1 + x_2 = 1 \end{cases}$ 的最小范数解。

**解**：

$A = [1, 1]$，$\mathbf{b} = [1]$

$A^T A = [1, 1]^T [1, 1] = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$

$(A^T A)^{-1}$ 不存在（奇异），使用 SVD。

SVD：$A = [1, 1] = \sqrt{2} [1] [1/\sqrt{2}, 1/\sqrt{2}] = U\Sigma V^T$

$A^+ = V\Sigma^+ U^T = [1/\sqrt{2}, 1/\sqrt{2}]^T \frac{1}{\sqrt{2}} [1] = \frac{1}{2}\begin{bmatrix} 1 \\ 1 \end{bmatrix}$

最小范数解：$\mathbf{x} = A^+ \mathbf{b} = \frac{1}{2}\begin{bmatrix} 1 \\ 1 \end{bmatrix} [1] = \begin{bmatrix} 1/2 \\ 1/2 \end{bmatrix}$

验证：$x_1 + x_2 = 1/2 + 1/2 = 1$

范数：$\|\mathbf{x}\| = \sqrt{(1/2)^2 + (1/2)^2} = \sqrt{1/2} \approx 0.707$

另一个解如 $[1, 0]$ 的范数为 $1 > 0.707$，确实是最小范数解。

### 例题 4：投影矩阵

**问题**：求 $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ 的投影矩阵 $AA^+$。

**解**：

SVD：$A = I \cdot \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \cdot I$

$A^+ = I \cdot \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \cdot I = A$

$AA^+ = A^2 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$

这是投影到 $x$ 轴的投影矩阵。

### 例题 5：验证Moore-Penrose条件

**问题**：验证 $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$，$A^+ = A$ 满足 Moore-Penrose 条件。

**解**：

1. $AA^+A = A^3 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}^3 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} = A$ ✓

2. $A^+AA^+ = A^3 = A$ ✓

3. $(AA^+)^T = A^T = A = AA^+$ ✓

4. $(A^+A)^T = A^T = A = A^+A$ ✓

## 习题

### 基础题

1. 计算 $A = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ 的伪逆。

2. 计算 $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ 的伪逆。

3. 证明：如果 $A$ 可逆，则 $A^+ = A^{-1}$。

4. 证明：$(A^+)^+ = A$。

5. 计算 $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ 的伪逆。

### 进阶题

6. 证明：伪逆的唯一性。

7. 证明：$AA^+$ 和 $A^+A$ 都是投影矩阵。

8. 证明：$(A^T)^+ = (A^+)^T$。

9. 证明：$(AB)^+ = B^+ A^+$ 在某些条件下成立。

10. 研究伪逆的迭代计算方法。

### 挑战题

11. 研究加权伪逆。

12. 在图像复原中，如何使用伪逆？

13. 证明：$\|A^+\|_2 = 1/\sigma_r$（$\sigma_r$ 是最小非零奇异值）。

14. 研究伪逆在约束优化中的应用。

15. 比较 SVD 和正规方程法计算伪逆的数值稳定性。

## 注意事项

⚠️ **常见错误**

1. **混淆伪逆和逆**
   - 伪逆适用于任意矩阵
   - 逆只适用于可逆方阵

2. **错误计算伪逆**
   - 零奇异值不取倒数
   - 要转置 $\Sigma$

3. **忽略最小范数性质**
   - 伪逆解是最小范数解
   - 欠定系统时很重要

✅ **最佳实践**

1. **使用 SVD 计算伪逆**
   - 数值稳定
   - 适用于所有情况

2. **理解几何意义**
   - 投影矩阵
   - 最小范数解

3. **应用范围**
   - 最小二乘
   - 欠定系统
   - 超定系统

## 题型总结与思路技巧

### 伪逆核心要点

#### 📋 Moore-Penrose条件

伪逆$A^+$满足：
1. $AA^+A = A$
2. $A^+AA^+ = A^+$
3. $(AA^+)^T = AA^+$
4. $(A^+A)^T = A^+A$

### 💡 核心技巧与常用结论

#### 1. 伪逆的计算

**方法一：SVD**
$$A^+ = V\Sigma^+ U^T$$

**方法二：满秩分解**
若$A = BC$（$B$列满秩，$C$行满秩）：
$$A^+ = C^T(CC^T)^{-1}(B^TB)^{-1}B^T$$

#### 2. 伪逆的应用

| 问题类型 | 解的形式 |
|---------|---------|
| 超定系统（$m > n$） | $A^+\mathbf{b}$ = 最小二乘解 |
| 欠定系统（$m < n$） | $A^+\mathbf{b}$ = 最小范数解 |
| 一般情况 | $A^+\mathbf{b}$ = 最小范数最小二乘解 |

#### 3. 投影矩阵

- $P = AA^+$：投影到$\text{Col}(A)$
- $I - A^+A$：投影到$\text{Null}(A)$

#### 4. 特殊情况的伪逆

| 矩阵类型 | 伪逆 |
|---------|------|
| 可逆方阵 | $A^{-1}$ |
| 列满秩 | $(A^TA)^{-1}A^T$ |
| 行满秩 | $A^T(AA^T)^{-1}$ |
| 对角矩阵 | 非零元取倒数 |

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 计算伪逆 | SVD法 | 非零奇异值取倒数 |
| 求最小二乘解 | $A^+\mathbf{b}$ | 超定系统 |
| 求最小范数解 | $A^+\mathbf{b}$ | 欠定系统 |
| 验证伪逆 | 检验四个条件 | Moore-Penrose条件 |
| 构造投影矩阵 | $AA^+$或$A^+A$ | 区分列空间和零空间 |

### ⚠️ 常见错误

**错误一**：混淆$(A^TA)^{-1}A^T$与$A^+$
- $(A^TA)^{-1}A^T$仅适用于列满秩
- $A^+$适用于任意矩阵

**错误二**：伪逆的性质
- $(AB)^+ \neq B^+A^+$（一般情况）
- 需要额外条件才成立

**错误三**：最小范数解
- 欠定系统有无穷多解
- 伪逆给出的是最小范数解

## 本章小结

### 重要定义
1. Moore-Penrose 伪逆：满足四个条件的唯一矩阵
2. 计算：$A^+ = V\Sigma^+ U^T$

### 重要定理
1. 伪逆的唯一性
2. 最小范数最小二乘解

### 重要方法
1. SVD 计算伪逆
2. 满秩情况简化计算

### 重要应用
1. 最小二乘解
2. 欠定系统
3. 投影矩阵

## 相关概念

- [[21_SVD]] - 奇异值分解
- [[12_Least_Squares]] - 最小二乘法

## 参考教材

- 《线性代数》（第6版），同济大学数学系，第五章
- 《Introduction to Linear Algebra》（第5版），Gilbert Strang, Chapter 7


