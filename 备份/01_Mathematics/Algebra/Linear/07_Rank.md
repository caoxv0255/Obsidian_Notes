---
type: concept
topic: rank
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[05_Matrix_Operations]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 07
---

# 矩阵的秩 (Rank)

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

### 1.1 矩阵的秩

对于 $m \times n$ 矩阵 $A$，其秩 $\text{rank}(A)$ 定义为：
- $A$ 的行向量组的最大线性无关向量的个数（行秩）
- $A$ 的列向量组的最大线性无关向量的个数（列秩）

**重要结论**：行秩 = 列秩，因此简称"秩"。

### 1.2 等价定义

1. **子式定义**：秩是 $A$ 中非零子式的最高阶数
2. **行阶梯形定义**：秩是 $A$ 的行阶梯形矩阵中非零行的个数
3. **线性映射定义**：秩是 $A$ 作为线性映射的像空间的维数

### 1.3 满秩矩阵

- **行满秩**：$\text{rank}(A) = m$（行数）
- **列满秩**：$\text{rank}(A) = n$（列数）
- **满秩**（对于方阵）：$\text{rank}(A) = n$

## 2. 性质

### 2.1 基本性质

1. **转置不变性**：$\text{rank}(A) = \text{rank}(A^T)$
2. **乘法不等式**：$\text{rank}(AB) \leq \min\{\text{rank}(A), \text{rank}(B)\}$
3. **加法不等式**：$\text{rank}(A + B) \leq \text{rank}(A) + \text{rank}(B)$
4. **秩的界**：$0 \leq \text{rank}(A) \leq \min\{m, n\}$

### 2.2 可逆性与秩的关系

对于 $n \times n$ 矩阵 $A$：
$$A \text{ 可逆 } \iff \text{rank}(A) = n$$

### 2.3 零化度（Nullity）

对于 $m \times n$ 矩阵 $A$，零化度 $\text{nullity}(A)$ 是齐次方程组 $A\mathbf{x} = \mathbf{0}$ 的解空间的维数。

### 2.4 秩-零化度定理

对于 $m \times n$ 矩阵 $A$：
$$\text{rank}(A) + \text{nullity}(A) = n$$

**证明思路**：$A$ 的列空间的维数是 $\text{rank}(A)$，零空间的维数是 $\text{nullity}(A)$，它们共同构成 $\mathbb{R}^n$ 的正交补。

## 3. 秩的计算方法

### 3.1 行阶梯形法

1. 通过初等行变换将 $A$ 化为行阶梯形
2. 非零行的个数就是 $\text{rank}(A)$

### 3.2 子式法

寻找非零子式的最高阶数。

### 3.3 奇异值分解法

对于 $m \times n$ 矩阵 $A$，奇异值分解 $A = U\Sigma V^T$，$\text{rank}(A)$ 等于非零奇异值的个数。

## 4. 代码示例

### 4.1 计算矩阵的秩

```python
import numpy as np

# 示例 1：满秩矩阵
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]], dtype=float)
rank_A = np.linalg.matrix_rank(A)

print(f"矩阵 A:\n{A}")
print(f"rank(A) = {rank_A}")

# 示例 2：秩亏矩阵
B = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]], dtype=float)
rank_B = np.linalg.matrix_rank(B)

print(f"\n矩阵 B:\n{B}")
print(f"rank(B) = {rank_B}")

# 示例 3：非方阵
C = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
rank_C = np.linalg.matrix_rank(C)

print(f"\n矩阵 C:\n{C}")
print(f"rank(C) = {rank_C}")
print(f"shape(C) = {C.shape}")
```

### 4.2 验证秩-零化度定理

```python
import numpy as np

def verify_rank_nullity(A):
    """
    验证秩-零化度定理
    
    参数:
        A: 矩阵
    
    返回:
        rank: 秩
        nullity: 零化度
    """
    m, n = A.shape
    
    # 计算秩
    rank = np.linalg.matrix_rank(A)
    
    # 计算零化度（解空间的维数）
    # 使用 SVD 计算零空间
    U, s, Vt = np.linalg.svd(A)
    nullity = np.sum(s < 1e-10)
    
    print(f"矩阵形状: {A.shape}")
    print(f"rank(A) = {rank}")
    print(f"nullity(A) = {nullity}")
    print(f"rank + nullity = {rank + nullity}")
    print(f"n = {n}")
    print(f"定理成立: {rank + nullity == n}")
    
    return rank, nullity

# 示例
A = np.array([[1, 2, 3], [2, 4, 6], [1, 1, 1]], dtype=float)
rank, nullity = verify_rank_nullity(A)
```

### 4.3 使用行阶梯形计算秩

```python
import numpy as np

def rank_by_row_echelon(A, tol=1e-10):
    """
    使用行阶梯形计算秩
    
    参数:
        A: 矩阵
        tol: 容差
    
    返回:
        rank: 秩
    """
    A = A.copy().astype(float)
    m, n = A.shape
    rank = 0
    
    for i in range(min(m, n)):
        # 寻找主元
        pivot_row = i
        while pivot_row < m and abs(A[pivot_row, i]) < tol:
            pivot_row += 1
        
        if pivot_row == m:
            break
        
        # 交换行
        if pivot_row != i:
            A[[i, pivot_row]] = A[[pivot_row, i]]
        
        # 主元归一化
        pivot = A[i, i]
        A[i, :] /= pivot
        
        # 消元
        for j in range(i + 1, m):
            factor = A[j, i]
            A[j, :] -= factor * A[i, :]
        
        rank += 1
    
    return rank

# 示例
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]], dtype=float)
rank_manual = rank_by_row_echelon(A)
rank_numpy = np.linalg.matrix_rank(A)

print(f"矩阵 A:\n{A}")
print(f"手动计算 rank = {rank_manual}")
print(f"NumPy 计算 rank = {rank_numpy}")
print(f"结果一致: {rank_manual == rank_numpy}")
```

## 5. 例题

### 例题 1：计算矩阵的秩（满秩）

**问题**：计算 $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{bmatrix}$ 的秩。

**解**：

**方法1：行阶梯形**

$$\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 10
\end{bmatrix}
\xrightarrow{R_2 - 4R_1}
\begin{bmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
7 & 8 & 10
\end{bmatrix}
\xrightarrow{R_3 - 7R_1}
\begin{bmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & -6 & -11
\end{bmatrix}$$

$$\xrightarrow{R_3 - 2R_2}
\begin{bmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 0 & 1
\end{bmatrix}$$

非零行有 3 行，因此 $\text{rank}(A) = 3$。

**方法2：行列式**

计算 $3 \times 3$ 子式（即 $\det(A)$）：
$$\det(A) = 1 \times (5 \times 10 - 6 \times 8) - 2 \times (4 \times 10 - 6 \times 7) + 3 \times (4 \times 8 - 5 \times 7)$$

$$= 1 \times (50 - 48) - 2 \times (40 - 42) + 3 \times (32 - 35) = 2 + 4 - 9 = -3 \neq 0$$

由于 $3 \times 3$ 子式非零，$\text{rank}(A) = 3$。

### 例题 2：计算矩阵的秩（秩亏）

**问题**：计算 $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{bmatrix}$ 的秩。

**解**：

**方法1：行阶梯形**

$$\begin{bmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
3 & 6 & 9
\end{bmatrix}
\xrightarrow{R_2 - 2R_1}
\begin{bmatrix}
1 & 2 & 3 \\
0 & 0 & 0 \\
3 & 6 & 9
\end{bmatrix}
\xrightarrow{R_3 - 3R_1}
\begin{bmatrix}
1 & 2 & 3 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}$$

非零行只有 1 行，因此 $\text{rank}(A) = 1$。

**方法2：观察**

注意到 $A$ 的第二行是第一行的 2 倍，第三行是第一行的 3 倍，所有行向量成比例，因此 $\text{rank}(A) = 1$。

### 例题 3：证明秩的性质

**问题**：证明 $\text{rank}(A) = \text{rank}(A^T)$。

**证明**：

设 $A$ 是 $m \times n$ 矩阵。

**定义法**：
- $\text{rank}(A)$ 是 $A$ 的列向量组的最大线性无关向量的个数
- $\text{rank}(A^T)$ 是 $A^T$ 的列向量组的最大线性无关向量的个数
- $A^T$ 的列向量组就是 $A$ 的行向量组

因此需要证明 $A$ 的行秩 = $A$ 的列秩。

**证明思路**：
1. 设 $A$ 的列秩为 $r$，则 $A$ 有 $r$ 个线性无关的列向量
2. 对应于这 $r$ 列的 $r \times r$ 子式非零
3. 这个 $r \times r$ 子式的转置也是 $A^T$ 的 $r \times r$ 子式，非零
4. 因此 $A^T$ 的列秩至少为 $r$
5. 同理可证 $A$ 的行秩至少为 $r$
6. 因此行秩 = 列秩

### 例题 4：证明秩-零化度定理

**问题**：对于 $m \times n$ 矩阵 $A$，证明 $\text{rank}(A) + \text{nullity}(A) = n$。

**证明**：

设 $\text{rank}(A) = r$，则 $A$ 的列空间 $\text{Im}(A)$ 的维数为 $r$。

设 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_r$ 是 $A$ 的列空间的一组基。

扩展 $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_r\}$ 为 $\mathbb{R}^m$ 的一组基：
$\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_r, \mathbf{w}_{r+1}, \ldots, \mathbf{w}_m\}$

定义线性映射 $T: \mathbb{R}^n \to \mathbb{R}^m$ 为 $T(\mathbf{x}) = A\mathbf{x}$。

根据维数定理：
$$\dim(\mathbb{R}^n) = \dim(\ker(T)) + \dim(\text{Im}(T))$$

即：
$$n = \text{nullity}(A) + \text{rank}(A)$$

因此 $\text{rank}(A) + \text{nullity}(A) = n$。

### 例题 5：计算零化度

**问题**：设 $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$，求 $\text{nullity}(A)$。

**解**：

首先计算 $\text{rank}(A)$：

$$\begin{bmatrix}
1 & 2 & 3 \\
2 & 4 & 6
\end{bmatrix}
\xrightarrow{R_2 - 2R_1}
\begin{bmatrix}
1 & 2 & 3 \\
0 & 0 & 0
\end{bmatrix}$$

非零行有 1 行，因此 $\text{rank}(A) = 1$。

根据秩-零化度定理：
$$\text{nullity}(A) = n - \text{rank}(A) = 3 - 1 = 2$$

**验证**：解齐次方程组 $A\mathbf{x} = \mathbf{0}$：
$$x + 2y + 3z = 0$$

解空间的维数为 2，基向量可以取：
$$\mathbf{v}_1 = \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}, \quad \mathbf{v}_2 = \begin{bmatrix} -3 \\ 0 \\ 1 \end{bmatrix}$$

### 例题 6：利用秩判断线性方程组的解

**问题**：判断线性方程组 $A\mathbf{x} = \mathbf{b}$ 的解的情况，其中
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 0 & 1 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 6 \\ 12 \\ 2 \end{bmatrix}$$

**解**：

计算增广矩阵 $[A | \mathbf{b}]$ 的秩：

$$[A | \mathbf{b}] = \begin{bmatrix}
1 & 2 & 3 & | & 6 \\
2 & 4 & 6 & | & 12 \\
1 & 0 & 1 & | & 2
\end{bmatrix}
$$

化为行阶梯形：
$$\xrightarrow{R_2 - 2R_1}
\begin{bmatrix}
1 & 2 & 3 & | & 6 \\
0 & 0 & 0 & | & 0 \\
1 & 0 & 1 & | & 2
\end{bmatrix}
\xrightarrow{R_3 - R_1}
\begin{bmatrix}
1 & 2 & 3 & | & 6 \\
0 & 0 & 0 & | & 0 \\
0 & -2 & -2 & | & -4
\end{bmatrix}
$$

$\text{rank}(A) = 2$，$\text{rank}([A | \mathbf{b}]) = 2$。

由于 $\text{rank}(A) = \text{rank}([A | \mathbf{b}])$，方程组有解。

又因为 $\text{rank}(A) = 2 < 3$（未知数个数），方程组有无限多解。

## 6. 机器学习应用

### 应用 1：特征选择

使用矩阵的秩判断特征是否冗余。

```python
import numpy as np

# 生成数据
np.random.seed(42)
n_samples = 100
n_features = 5

X = np.random.randn(n_samples, n_features)
X[:, 1] = 2 * X[:, 0] + np.random.randn(n_samples) * 0.1  # 第2个特征是第1个特征的2倍
X[:, 2] = X[:, 0] + X[:, 3]  # 第3个特征是第1和第4个特征的和

# 计算秩
rank_X = np.linalg.matrix_rank(X)

print(f"数据矩阵形状: {X.shape}")
print(f"数据矩阵的秩: {rank_X}")

# 使用奇异值分解
U, s, Vt = np.linalg.svd(X)
print(f"奇异值: {s}")

# 判断特征冗余
effective_rank = np.sum(s > 1e-10)
print(f"有效秩（奇异值 > 1e-10）: {effective_rank}")

# 计算特征相关性
correlation_matrix = np.corrcoef(X.T)
print(f"\n相关系数矩阵:\n{correlation_matrix}")
```

### 应用 2：低秩近似

使用奇异值分解进行低秩近似。

```python
import numpy as np
import matplotlib.pyplot as plt

# 生成图像数据
np.random.seed(42)
image = np.random.rand(50, 50)

# 计算秩
rank_original = np.linalg.matrix_rank(image)
print(f"原始图像的秩: {rank_original}")

# 奇异值分解
U, s, Vt = np.linalg.svd(image)

# 低秩近似
ranks_to_try = [5, 10, 20, 30]
fig, axes = plt.subplots(1, len(ranks_to_try) + 1, figsize=(15, 3))

axes[0].imshow(image, cmap='gray')
axes[0].set_title(f'原始 (rank={rank_original})')

for i, r in enumerate(ranks_to_try):
    # 保留前 r 个奇异值
    S_r = np.zeros_like(s)
    S_r[:r] = s[:r]
    
    # 重构图像
    image_approx = U @ np.diag(S_r) @ Vt
    
    axes[i+1].imshow(image_approx, cmap='gray')
    axes[i+1].set_title(f'rank={r}')

plt.tight_layout()
plt.show()
```

## 题型总结与思路技巧

### 矩阵秩的计算与判断

#### 📋 秩的计算方法

| 方法 | 适用场景 | 步骤 |
|-----|---------|------|
| **初等变换法** | 一般矩阵 | 化为行阶梯形，非零行数即为秩 |
| **子式法** | 理论证明 | 最高阶非零子式的阶数 |
| **SVD分解** | 数值计算 | 非零奇异值个数 |

### 💡 核心技巧与常用结论

#### 1. 秩的基本性质

- $0 \leq \text{rank}(A_{m×n}) \leq \min(m, n)$
- $\text{rank}(A) = \text{rank}(A^T)$
- $\text{rank}(A) = n \Leftrightarrow A$ 列满秩
- $\text{rank}(A) = m \Leftrightarrow A$ 行满秩

#### 2. 秩的不等式

- $\text{rank}(A+B) \leq \text{rank}(A) + \text{rank}(B)$
- $\text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B))$
- $\text{rank}(A) + \text{rank}(B) - n \leq \text{rank}(AB)$

#### 3. 满秩矩阵的等价条件

对于$n$阶方阵$A$，以下等价：
- $\text{rank}(A) = n$
- $A$可逆
- $\det(A) \neq 0$
- $Ax = 0$只有零解
- $A$的行/列向量线性无关

#### 4. 线性方程组解的判定

设$A$为$m×n$矩阵，$\tilde{A} = [A|b]$为增广矩阵：
- $\text{rank}(A) = \text{rank}(\tilde{A}) = n$：唯一解
- $\text{rank}(A) = \text{rank}(\tilde{A}) < n$：无穷多解
- $\text{rank}(A) < \text{rank}(\tilde{A})$：无解

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 求矩阵的秩 | 初等变换法 | 化为行阶梯形 |
| 证明秩的不等式 | 利用秩的性质 | 结合维数公式 |
| 讨论方程组解 | 增广矩阵秩 | Rouché-Capelli定理 |
| 证明满秩 | 等价条件转换 | 可逆、行列式、线性无关 |

### ⚠️ 常见错误

**错误一**：秩的不等式方向
- $\text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B))$，不是$\geq$

**错误二**：增广矩阵处理
- 讨论方程组时，要比较$A$和$\tilde{A}=[A|b]$的秩

**错误三**：初等变换改变秩
- 初等变换不改变秩
- 但改变行列式的值

## 7. 课后练习

### 7.1 基础题

**教材参考**：《高等代数简明教程》第三章习题

1. 计算下列矩阵的秩：
   - (1) $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$
   - (2) $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$
   - (3) $A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix}$

2. 设 $A$ 是 $3 \times 4$ 矩阵，$\text{rank}(A) = 2$，求 $\text{nullity}(A)$。

3. 判断 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ 是否可逆。

4. 证明：$\text{rank}(A) \leq \min\{m, n\}$，其中 $A$ 是 $m \times n$ 矩阵。

5. 使用行阶梯形法计算 $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 5 & 6 \end{bmatrix}$ 的秩。

### 7.2 进阶题

**教材参考**：《高等代数简明教程》第三章习题

6. 证明：$\text{rank}(AB) \leq \min\{\text{rank}(A), \text{rank}(B)\}$。

7. 证明：$\text{rank}(A + B) \leq \text{rank}(A) + \text{rank}(B)$。

8. 设 $A$ 是 $m \times n$ 矩阵，证明 $\text{rank}(A) = \text{rank}(A^T)$。

9. 证明秩-零化度定理：$\text{rank}(A) + \text{nullity}(A) = n$。

10. 设 $A$ 是 $n \times n$ 矩阵，证明 $A$ 可逆 $\iff \text{rank}(A) = n$。

### 7.3 挑战题

**教材参考**：《高等代数简明教程》第三章习题

11. 设 $A$ 是 $m \times n$ 矩阵，$P$ 是 $m \times m$ 可逆矩阵，$Q$ 是 $n \times n$ 可逆矩阵，证明 $\text{rank}(PAQ) = \text{rank}(A)$。

12. 在推荐系统中，研究矩阵分解（如 SVD）在低秩矩阵补全中的应用。

13. 证明：对于任何 $m \times n$ 矩阵 $A$，都存在奇异值分解 $A = U\Sigma V^T$。

14. 在图像处理中，研究如何利用低秩近似进行图像压缩。

15. 设 $A$ 是 $n \times n$ 对称矩阵，证明 $A$ 可对角化 $\iff$ $A$ 有 $n$ 个线性无关的特征向量。

## 8. 教材参考

### 国内教材
1. **《高等代数简明教程》（第2版）** - 北京大学数学系
   - 第三章：线性方程组
   - 重点：秩、线性方程组的解

2. **《线性代数》（第6版）** - 同济大学数学系
   - 第三章：向量组的线性相关性
   - 重点：秩的性质

### 国外教材
3. **《Introduction to Linear Algebra》（第5版）** - Gilbert Strang
   - Chapter 3: Vector Spaces and Subspaces
   - 重点：秩的定义和计算

4. **《Linear Algebra Done Right》（第3版）** - Sheldon Axler
   - Chapter 3: Linear Maps
   - 重点：秩和零化度

## 9. 本章小结

### 9.1 重要定义
1. 矩阵的秩：行（列）向量组的最大线性无关向量的个数
2. 满秩矩阵：秩等于行数或列数的矩阵
3. 零化度：齐次方程组解空间的维数

### 9.2 重要性质
1. $\text{rank}(A) = \text{rank}(A^T)$
2. $\text{rank}(AB) \leq \min\{\text{rank}(A), \text{rank}(B)\}$
3. 秩-零化度定理：$\text{rank}(A) + \text{nullity}(A) = n$

### 9.3 重要方法
1. 行阶梯形法
2. 子式法
3. 奇异值分解法

### 9.4 重要应用
1. 特征选择
2. 低秩近似
3. 线性方程组解的判断

---

**创建时间：2026年3月11日**  
**最后更新：2026年3月11日**  
**参考教材**：《高等代数简明教程》、《Introduction to Linear Algebra》

## 相关概念

- [[04_Matrix_Basics]] - 矩阵基础
- [[05_Matrix_Operations]] - 矩阵运算
- [[09_Linear_Relations]] - 线性相关性
- [[11_Linear_Equations]] - 线性方程组


