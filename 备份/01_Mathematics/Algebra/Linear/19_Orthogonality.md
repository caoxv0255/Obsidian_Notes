---
type: concept
topic: orthogonality
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[18_Inner_Product]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
---
# 正交性 (Orthogonality)

## 1. 正交的定义

### 1.1 向量正交

$\mathbf{u} \perp \mathbf{v}$ 当且仅当 $\langle \mathbf{u}, \mathbf{v} \rangle = 0$。

### 1.2 正交补

对于子空间 $W \subseteq V$，$W$ 的正交补定义为：
$$W^\perp = \{\mathbf{v} \in V \mid \langle \mathbf{v}, \mathbf{w} \rangle = 0, \forall \mathbf{w} \in W\}$$

### 1.3 正交子空间

两个子空间 $W_1$ 和 $W_2$ 正交，如果 $\forall \mathbf{w}_1 \in W_1, \mathbf{w}_2 \in W_2$，有 $\mathbf{w}_1 \perp \mathbf{w}_2$。

## 2. 正交基

### 2.1 定义

基 $\{\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n\}$ 是正交基，如果：
$$\langle \mathbf{e}_i, \mathbf{e}_j \rangle = 0, \quad i \neq j$$

### 2.2 标准正交基

如果基向量还满足 $\|\mathbf{e}_i\| = 1$，则称为标准正交基。

### 2.3 坐标计算

在标准正交基下，坐标计算简化为：
$$[\mathbf{v}]_{\mathcal{E}} = \begin{bmatrix}
\langle \mathbf{v}, \mathbf{e}_1 \rangle \\
\langle \mathbf{v}, \mathbf{e}_2 \rangle \\
\vdots \\
\langle \mathbf{v}, \mathbf{e}_n \rangle
\end{bmatrix}$$

## 3. 正交矩阵

### 3.1 定义

方阵 $Q$ 是正交矩阵，如果：
$$Q^T Q = Q Q^T = I$$

### 3.2 性质

1. $Q$ 的列向量是标准正交的
2. $Q$ 的行向量是标准正交的
3. $Q^{-1} = Q^T$
4. $|\det(Q)| = 1$

### 3.3 几何意义

正交矩阵代表保距变换（旋转、反射）。

## 4. 正交投影

### 4.1 到子空间的投影

$\mathbf{v}$ 到子空间 $W$ 的投影 $\text{proj}_W(\mathbf{v})$ 是 $W$ 中最接近 $\mathbf{v}$ 的向量。

### 4.2 投影公式

如果 $W$ 有标准正交基 $\{\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_k\}$，则：
$$\text{proj}_W(\mathbf{v}) = \sum_{i=1}^k \langle \mathbf{v}, \mathbf{e}_i \rangle \mathbf{e}_i$$

### 4.3 矩阵形式

如果 $Q$ 的列是 $W$ 的标准正交基，则：
$$\text{proj}_W(\mathbf{v}) = QQ^T \mathbf{v}$$

## 代码示例

```python
import numpy as np

def is_orthogonal(Q, tolerance=1e-10):
    """检查矩阵是否正交"""
    return np.allclose(Q.T @ Q, np.eye(Q.shape[0]), atol=tolerance)

def orthonormal_projection(v, basis):
    """到标准正交基张成子空间的投影"""
    basis = np.array(basis, dtype=float)
    v = np.array(v, dtype=float).reshape(-1, 1)

    # 标准正交化
    from sklearn.preprocessing import normalize
    basis_orthonormal = normalize(basis, axis=0, norm='l2')

    # 投影
    projection = basis_orthonormal @ (basis_orthonormal.T @ v)

    return projection.flatten()

# 示例 1：正交矩阵
Q = np.array([[0, -1],
              [1, 0]])
print(f"Q 是否正交: {is_orthogonal(Q)}")
print(f"Q^T Q =\n{Q.T @ Q}")

# 示例 2：投影
v = np.array([3, 4])
basis = np.array([[1, 0], [0, 1]])  # 标准基
projection = orthonormal_projection(v, basis)
print(f"\n向量 v = {v}")
print(f"投影 = {projection}")
```

## 机器学习应用

### 应用 1：注意力机制

自注意力使用正交投影。

### 应用 2：特征选择

正交投影用于特征降维。

## 严格证明

### 证明：正交投影的最优性

**定理**：$\text{proj}_W(\mathbf{v})$ 是 $W$ 中最接近 $\mathbf{v}$ 的向量。

**证明**：

设 $\mathbf{w} \in W$，则：
$$\|\mathbf{v} - \mathbf{w}\|^2 = \|\mathbf{v} - \text{proj}_W(\mathbf{v}) + \text{proj}_W(\mathbf{v}) - \mathbf{w}\|^2$$

由于 $\mathbf{v} - \text{proj}_W(\mathbf{v}) \perp W$，由勾股定理：
$$= \|\mathbf{v} - \text{proj}_W(\mathbf{v})\|^2 + \|\text{proj}_W(\mathbf{v}) - \mathbf{w}\|^2$$

当 $\mathbf{w} = \text{proj}_W(\mathbf{v})$ 时取最小值。

## 例题

### 例题 1：求投影

**问题**：求 $\mathbf{v} = [3, 1]^T$ 到直线 $y = x$ 的投影。

**解**：

直线的方向向量为 $\mathbf{u} = [1, 1]^T$，归一化得 $\mathbf{e} = [1/\sqrt{2}, 1/\sqrt{2}]^T$。

投影：
$$\text{proj}_W(\mathbf{v}) = \langle \mathbf{v}, \mathbf{e} \rangle \mathbf{e} = \frac{4}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}[1, 1]^T = [2, 2]^T$$

### 例题 2：验证正交矩阵

**问题**：验证 $Q = \begin{bmatrix} 1/\sqrt{2} & -1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix}$ 是正交矩阵。

**解**：

计算 $Q^T Q$：
$$Q^T Q = \begin{bmatrix} 1/\sqrt{2} & 1/\sqrt{2} \\ -1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix} \begin{bmatrix} 1/\sqrt{2} & -1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix}$$

$$= \begin{bmatrix} \frac{1}{2} + \frac{1}{2} & -\frac{1}{2} + \frac{1}{2} \\ -\frac{1}{2} + \frac{1}{2} & \frac{1}{2} + \frac{1}{2} \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$$

因此 $Q$ 是正交矩阵。

### 例题 3：正交补的维数

**问题**：设 $W = \text{span}\{[1, 1, 0]^T, [0, 1, 1]^T\}$，求 $\dim(W^\perp)$。

**解**：

$W$ 由两个向量生成，且这两个向量线性无关，所以 $\dim(W) = 2$。

由于 $\mathbb{R}^3$ 的维数为 3，所以：
$$\dim(W^\perp) = \dim(\mathbb{R}^3) - \dim(W) = 3 - 2 = 1$$

### 例题 4：投影矩阵

**问题**：求到 $\text{span}\{[1, 1]^T\}$ 的投影矩阵。

**解**：

方向向量为 $\mathbf{u} = [1, 1]^T$，归一化得 $\mathbf{e} = [1/\sqrt{2}, 1/\sqrt{2}]^T$。

投影矩阵为：
$$P = \mathbf{e}\mathbf{e}^T = \frac{1}{2}\begin{bmatrix} 1 \\ 1 \end{bmatrix}[1, 1] = \frac{1}{2}\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$$

验证 $P^2 = P$：
$$P^2 = \frac{1}{4}\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}^2 = \frac{1}{4}\begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix} = \frac{1}{2}\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} = P$$

### 例题 5：正交基的构造

**问题**：将 $\{[1, 1, 1]^T, [1, 1, 0]^T\}$ 扩充为 $\mathbb{R}^3$ 的标准正交基。

**解**：

先正交化：
$\mathbf{u}_1 = [1, 1, 1]^T$
$\mathbf{u}_2 = [1, 1, 0]^T - \frac{2}{3}[1, 1, 1]^T = [1/3, 1/3, -2/3]^T$

找与 $\mathbf{u}_1, \mathbf{u}_2$ 都正交的向量：
设 $\mathbf{u}_3 = [a, b, c]^T$，则：
$a + b + c = 0$
$a + b - 2c = 0$

解得 $c = 0$，$a + b = 0$，取 $\mathbf{u}_3 = [1, -1, 0]^T$。

归一化：
$\mathbf{e}_1 = \frac{1}{\sqrt{3}}[1, 1, 1]^T$
$\mathbf{e}_2 = \frac{1}{\sqrt{6}}[1, 1, -2]^T$
$\mathbf{e}_3 = \frac{1}{\sqrt{2}}[1, -1, 0]^T$

## 习题

### 基础题

1. 检查 $Q = \begin{bmatrix} 1/\sqrt{2} & -1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix}$ 是否正交。

2. 求 $\mathbf{v} = [1, 2, 3]^T$ 到 $\text{span}\{[1, 0, 0]^T, [0, 1, 0]^T\}$ 的投影。

3. 证明：如果 $Q$ 正交，则 $|\det(Q)| = 1$。

4. 构造 $\mathbb{R}^3$ 的一个标准正交基。

5. 证明：$(W^\perp)^\perp = W$。

### 进阶题

6. 证明：正交投影矩阵是对称幂等矩阵。

7. 证明：正交矩阵的列向量是标准正交的。

8. 证明：$\dim(W) + \dim(W^\perp) = \dim(V)$。

9. 证明：$(W_1 \cap W_2)^\perp = W_1^\perp + W_2^\perp$。

10. 证明：$(W_1 + W_2)^\perp = W_1^\perp \cap W_2^\perp$。

### 挑战题

11. 研究正交多项式（Legendre、Chebyshev 等）。

12. 证明：任何实对称矩阵都可以正交对角化。

13. 在图像处理中，为什么正交变换（如 DCT）优于非正交变换？

14. 研究快速正交变换算法（FFT、DWT）。

15. 证明：正交投影的残差 $\mathbf{v} - \text{proj}_W(\mathbf{v})$ 正交于 $W$。

## 题型总结与思路技巧

### 正交性核心要点

#### 📋 正交的关键概念

| 概念 | 定义 | 判定方法 |
|-----|------|---------|
| **向量正交** | $\langle \mathbf{u}, \mathbf{v} \rangle = 0$ | 内积为零 |
| **正交补** | $W^\perp$ | 与$W$中所有向量正交 |
| **正交基** | 基向量两两正交 | $\langle \mathbf{e}_i, \mathbf{e}_j \rangle = 0$（$i \neq j$） |
| **标准正交基** | 正交且单位化 | $\langle \mathbf{e}_i, \mathbf{e}_j \rangle = \delta_{ij}$ |

### 💡 核心技巧与常用结论

#### 1. 正交补的性质

- $(W^\perp)^\perp = W$
- $\dim W + \dim W^\perp = n$
- $V = W \oplus W^\perp$（直和分解）

#### 2. 正交投影

**公式**：$P_W = \mathbf{e}_1\mathbf{e}_1^T + \cdots + \mathbf{e}_k\mathbf{e}_k^T$

**性质**：
- $P_W^2 = P_W$（幂等）
- $P_W^T = P_W$（对称）
- $\text{rank}(P_W) = \dim W$

#### 3. 正交矩阵

**判定**：$Q^T Q = I$

**性质**：
- $\det Q = \pm 1$
- $Q^{-1} = Q^T$
- 保持内积：$\langle Q\mathbf{u}, Q\mathbf{v} \rangle = \langle \mathbf{u}, \mathbf{v} \rangle$
- 保持长度：$\|Q\mathbf{v}\| = \|\mathbf{v}\|$

#### 4. 最小二乘解

**问题**：$\min \|A\mathbf{x} - \mathbf{b}\|$

**解**：$\mathbf{x}^*$ 是$A\mathbf{x} = \text{proj}_{\text{Col}(A)} \mathbf{b}$的解

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 判断正交 | 计算内积 | 内积为零 |
| 求正交补 | 找正交向量 | 解方程组 |
| 正交化 | Gram-Schmidt | 逐个减去投影 |
| 求正交投影 | 投影公式 | $P = \sum \mathbf{e}_i\mathbf{e}_i^T$ |
| 证明题 | 利用性质 | 正交补、投影性质 |

### ⚠️ 常见错误

**错误一**：混淆正交基与标准正交基
- 正交基：向量两两正交
- 标准正交基：正交且单位长

**错误二**：正交补的范围
- 正交补是所有与$W$正交的向量
- 不是"不在$W$中的向量"

**错误三**：正交投影公式
- 投影矩阵需用标准正交基
- 若基不正交，需用$P = A(A^TA)^{-1}A^T$

## 相关概念

- [[18_Inner_Product]] - 内积空间
- [[20_Orthogonal_Transformations]] - 正交变换
- [[21_SVD]] - 奇异值分解

## 参考教材

- 《线性代数》（第6版），同济大学数学系，第五章
- 《Introduction to Linear Algebra》（第5版），Gilbert Strang, Chapter 4

