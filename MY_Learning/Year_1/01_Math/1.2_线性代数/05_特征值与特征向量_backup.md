---
type: concept
topic: eigenvalues
category: linear_algebra
difficulty: intermediate
prerequisites: [[01_Determinants]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
---

# 特征值与特征向量 (Eigenvalues and Eigenvectors)

## 1. 定义

### 1.1 特征值和特征向量

对于 $n \times n$ 矩阵 $A$，如果存在非零向量 $\mathbf{v} \neq \mathbf{0}$ 和标量 $\lambda$ 使得：
$$A\mathbf{v} = \lambda\mathbf{v}$$

则称 $\lambda$ 为 $A$ 的**特征值**，$\mathbf{v}$ 为对应的**特征向量**。

**几何意义**：特征向量在 $A$ 的线性变换下只伸缩不改变方向，伸缩因子就是特征值。

### 1.2 特征方程

从 $A\mathbf{v} = \lambda\mathbf{v}$ 可得 $(A - \lambda I)\mathbf{v} = \mathbf{0}$。

由于 $\mathbf{v} \neq \mathbf{0}$，故 $|A - \lambda I| = 0$，这称为**特征方程**。

### 1.3 特征多项式

$$p(\lambda) = \det(A - \lambda I) = \lambda^n - (\text{tr}A)\lambda^{n-1} + \cdots + (-1)^n\det(A)$$

特征值是特征多项式的根。

## 2. 性质

### 2.1 基本性质

1. **迹与特征值**：$\sum_{i=1}^n \lambda_i = \text{tr}(A)$
2. **行列式与特征值**：$\prod_{i=1}^n \lambda_i = \det(A)$
3. **特征值的几何意义**：特征方向上的缩放因子

### 2.2 对称矩阵的性质

对于对称矩阵 $A$（$A^T = A$）：

1. **特征值都是实数**
2. **特征向量可以选为正交的**
3. **可以正交对角化**：$A = Q\Lambda Q^T$

### 2.3 特征值的估计

**Gershgorin圆定理**：
矩阵 $A$ 的每个特征值都至少位于一个Gershgorin圆内：
$$D_i = \{z \in \mathbb{C} : |z - a_{ii}| \leq \sum_{j \neq i} |a_{ij}|\}$$

## 3. 代码示例

### 3.1 计算特征值和特征向量

```python
import numpy as np

# 对称矩阵
A = np.array([[2, 1], [1, 2]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"矩阵 A:\n{A}")
print(f"\n特征值: {eigenvalues}")
print(f"特征向量:\n{eigenvectors}")

# 验证 A v = λ v
for i, (lam, vec) in enumerate(zip(eigenvalues, eigenvectors.T)):
    Av = A @ vec
    lam_v = lam * vec
    print(f"\n特征值 {i+1}: {lam:.6f}")
    print(f"A @ v = {Av}")
    print(f"λ @ v = {lam_v}")
    print(f"误差: {np.linalg.norm(Av - lam_v):.6e}")
```

### 3.2 可视化特征向量

```python
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, 1], [1, 2]])
eigenvalues, eigenvectors = np.linalg.eig(A)

plt.figure(figsize=(6, 6))

# 绘制单位圆
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x, y, 'k-', linewidth=0.5, label='单位圆')

# 绘制特征向量
colors = ['r', 'b']
for i, (lam, vec) in enumerate(zip(eigenvalues, eigenvectors.T)):
    plt.arrow(0, 0, vec[0], vec[1], head_width=0.1, 
              color=colors[i], label=f'特征向量 {i+1} (λ={lam:.2f})')

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.grid()
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.legend()
plt.title('特征向量可视化')
plt.show()
```

## 4. 例题

### 例题 1：计算 2×2 矩阵的特征值和特征向量

**问题**：求 $A = \begin{bmatrix} 2 & 1 \\\\ 1 & 2 \end{bmatrix}$ 的特征值和特征向量。

**解**：

**第一步：求特征方程**

$$|A - \lambda I| = \begin{vmatrix} 2-\lambda & 1 \\\\ 1 & 2-\lambda \end{vmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0$$

**第二步：求特征值**

$$\lambda = \frac{4 \pm \sqrt{16 - 12}}{2} = \frac{4 \pm 2}{2}$$

$\lambda_1 = 3$，$\lambda_2 = 1$

**第三步：求特征向量**

对于 $\lambda_1 = 3$：
$$(A - 3I)\mathbf{v} = \begin{bmatrix} -1 & 1 \\\\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}$$

$-x + y = 0$，故 $x = y$。取 $\mathbf{v}_1 = \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}$。

对于 $\lambda_2 = 1$：
$$(A - I)\mathbf{v} = \begin{bmatrix} 1 & 1 \\\\ 1 & 1 \end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}$$

$x + y = 0$，故 $y = -x$。取 $\mathbf{v}_2 = \begin{bmatrix} 1 \\\\ -1 \end{bmatrix}$。

**验证**：
- 迹：$\lambda_1 + \lambda_2 = 3 + 1 = 4 = \text{tr}(A) = 2 + 2$ ✓
- 行列式：$\lambda_1 \lambda_2 = 3 \times 1 = 3 = \det(A) = 4 - 1 = 3$ ✓

### 例题 2：计算 3×3 矩阵的特征值和特征向量

**问题**：求 $A = \begin{bmatrix} 1 & 2 & 1 \\\\ 0 & 3 & 1 \\\\ 0 & 0 & 2 \end{bmatrix}$ 的特征值和特征向量。

**解**：这是上三角矩阵，特征值就是对角线元素。

$\lambda_1 = 1$，$\lambda_2 = 3$，$\lambda_3 = 2$

**求特征向量**：

对于 $\lambda_1 = 1$：
$$(A - I)\mathbf{v} = \begin{bmatrix} 0 & 2 & 1 \\\\ 0 & 2 & 1 \\\\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix}$$

从第三行：$z = 0$
从第一行：$2y + z = 0$，故 $y = 0$
$x$ 是自由的。取 $\mathbf{v}_1 = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}$。

对于 $\lambda_2 = 3$：
$$(A - 3I)\mathbf{v} = \begin{bmatrix} -2 & 2 & 1 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & -1 \end{bmatrix} \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix}$$

从第三行：$-z = 0$，故 $z = 0$
从第二行：$z = 0$（无新信息）
从第一行：$-2x + 2y = 0$，故 $x = y$
取 $\mathbf{v}_2 = \begin{bmatrix} 1 \\\\ 1 \\\\ 0 \end{bmatrix}$。

对于 $\lambda_3 = 2$：
$$(A - 2I)\mathbf{v} = \begin{bmatrix} -1 & 2 & 1 \\\\ 0 & 1 & 1 \\\\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix}$$

从第二行：$y + z = 0$，故 $y = -z$
从第一行：$-x + 2y + z = 0$，代入 $y = -z$ 得 $-x - z = 0$，故 $x = -z$
$z$ 是自由的。取 $z = 1$，则 $\mathbf{v}_3 = \begin{bmatrix} -1 \\\\ -1 \\\\ 1 \end{bmatrix}$。

### 例题 3：对称矩阵的特征值和特征向量

**问题**：求 $A = \begin{bmatrix} 0 & 1 \\\\ 1 & 0 \end{bmatrix}$ 的特征值和特征向量。

**解**：

特征方程：
$$\begin{vmatrix} -\lambda & 1 \\\\ 1 & -\lambda \end{vmatrix} = \lambda^2 - 1 = 0$$

$\lambda_1 = 1$，$\lambda_2 = -1$

对于 $\lambda_1 = 1$：
$$\begin{bmatrix} -1 & 1 \\\\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}$$

$-x + y = 0$，故 $x = y$。取 $\mathbf{v}_1 = \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}$。

对于 $\lambda_2 = -1$：
$$\begin{bmatrix} 1 & 1 \\\\ 1 & 1 \end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}$$

$x + y = 0$，故 $y = -x$。取 $\mathbf{v}_2 = \begin{bmatrix} 1 \\\\ -1 \end{bmatrix}$。

**验证正交性**：
$\mathbf{v}_1 \cdot \mathbf{v}_2 = 1 \times 1 + 1 \times (-1) = 0$ ✓

### 例题 4：特征值的几何意义

**问题**：设 $A = \begin{bmatrix} 2 & 0 \\\\ 0 & 3 \end{bmatrix}$，说明特征值的几何意义。

**解**：

特征方程：
$$\begin{vmatrix} 2-\lambda & 0 \\\\ 0 & 3-\lambda \end{vmatrix} = (2-\lambda)(3-\lambda) = 0$$

$\lambda_1 = 2$，$\lambda_2 = 3$

对于 $\lambda_1 = 2$：$\mathbf{v}_1 = \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}$（x轴方向）
对于 $\lambda_2 = 3$：$\mathbf{v}_2 = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}$（y轴方向）

**几何意义**：
- 在 x 轴方向，向量伸长 2 倍
- 在 y 轴方向，向量伸长 3 倍
- $A$ 表示一个沿坐标轴的伸缩变换

### 例题 5：证明对称矩阵的特征值都是实数

**问题**：证明：如果 $A$ 是实对称矩阵，则 $A$ 的特征值都是实数。

**证明**：

设 $\lambda$ 是 $A$ 的特征值，$\mathbf{v}$ 是对应的特征向量，即 $A\mathbf{v} = \lambda\mathbf{v}$。

两边取共轭转置（$\overline{\mathbf{v}}^T$ 表示 $\mathbf{v}$ 的共轭转置）：
$$\overline{\mathbf{v}}^T A \mathbf{v} = \overline{\mathbf{v}}^T \lambda \mathbf{v} = \lambda \overline{\mathbf{v}}^T \mathbf{v}$$

由于 $A$ 是实对称矩阵，$A = A^T = \overline{A}$，故：
$$\overline{\mathbf{v}}^T A \mathbf{v} = \overline{\mathbf{v}}^T A^T \mathbf{v} = (\overline{A \mathbf{v}})^T \mathbf{v} = \overline{\lambda} \overline{\mathbf{v}}^T \mathbf{v}$$

因此：
$$\lambda \overline{\mathbf{v}}^T \mathbf{v} = \overline{\lambda} \overline{\mathbf{v}}^T \mathbf{v}$$

由于 $\mathbf{v} \neq \mathbf{0}$，故 $\overline{\mathbf{v}}^T \mathbf{v} = \|\mathbf{v}\|^2 > 0$，所以：
$$\lambda = \overline{\lambda}$$

即 $\lambda$ 是实数。

## 5. 机器学习应用

### 应用 1：主成分分析（PCA）

PCA 使用协方差矩阵的特征值和特征向量进行数据降维。

**步骤**：
1. 计算数据的协方差矩阵 $C = \frac{1}{n}XX^T$
2. 求 $C$ 的特征值和特征向量
3. 按特征值大小排序，选择前 $k$ 个特征向量
4. 将数据投影到这 $k$ 个特征向量构成的子空间

**代码示例**：
```python
import numpy as np

# 生成示例数据
np.random.seed(42)
X = np.random.randn(100, 3)

# 计算协方差矩阵
C = np.cov(X, rowvar=False)

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eigh(C)

# 按特征值大小排序
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

print(f"特征值: {eigenvalues}")
print(f"解释方差比例: {eigenvalues / np.sum(eigenvalues)}")
```

### 应用 2：PageRank算法

PageRank 使用特征向量计算网页的重要性。

**原理**：
网页的重要性向量 $\mathbf{v}$ 满足 $M\mathbf{v} = \mathbf{v}$，其中 $M$ 是转移矩阵。

**代码示例**：
```python
import numpy as np

# 简单的3个网页的链接矩阵
M = np.array([[0.5, 0.5, 0],
              [0.5, 0, 1],
              [0, 0.5, 0]])

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(M.T)

# 找到特征值为1的特征向量
idx = np.argmin(np.abs(eigenvalues - 1))
pagerank = np.real(eigenvectors[:, idx])

# 归一化
pagerank = pagerank / np.sum(pagerank)

print(f"PageRank得分: {pagerank}")
```

### 应用 3：特征值在优化中的应用

在优化问题中，Hessian矩阵的特征值用于判断极值性质：
- 所有特征值 > 0：局部极小值
- 所有特征值 < 0：局部极大值
- 特征值有正有负：鞍点

## 6. 课后练习

### 6.1 基础题

**教材参考**：《高等代数简明教程》第五章习题

1. 求下列矩阵的特征值和特征向量：
   - (1) $A = \begin{bmatrix} 1 & 2 \\\\ 2 & 1 \end{bmatrix}$
   - (2) $A = \begin{bmatrix} 3 & 1 \\\\ 0 & 2 \end{bmatrix}$
   - (3) $A = \begin{bmatrix} 1 & 1 & 1 \\\\ 0 & 2 & 2 \\\\ 0 & 0 & 3 \end{bmatrix}$

2. 证明：$\text{tr}(A) = \sum_{i=1}^n \lambda_i$，$\det(A) = \prod_{i=1}^n \lambda_i$。

3. 设 $A$ 是 $n$ 阶矩阵，$\lambda$ 是 $A$ 的特征值，证明 $\lambda^k$ 是 $A^k$ 的特征值。

### 6.2 进阶题

**教材参考**：《高等代数简明教程》第五章习题

4. 求矩阵 $A = \begin{bmatrix} 1 & 1 & 1 \\\\ 1 & 1 & 1 \\\\ 1 & 1 & 1 \end{bmatrix}$ 的特征值和特征向量。

5. 证明：如果 $A$ 是正交矩阵，则 $|\lambda| = 1$。

6. 设 $A$ 是实对称矩阵，证明：属于不同特征值的特征向量正交。

### 6.3 挑战题

**教材参考**：《高等代数简明教程》第五章习题

7. 设 $A$ 是 $n$ 阶矩阵，证明 $A$ 和 $A^T$ 有相同的特征值。

8. 在PCA中，证明协方差矩阵的特征向量是数据方差最大的方向。

9. 设 $A$ 是 $n$ 阶实矩阵，证明 $A^T A$ 的特征值都是非负的。

## 7. 教材参考

### 国内教材
1. **《高等代数简明教程》（第2版）** - 北京大学数学系
   - 第五章：特征值与特征向量
   - 重点：特征值计算、对称矩阵的性质

2. **《线性代数》（第6版）** - 同济大学数学系
   - 第五章：相似矩阵及二次型
   - 重点：特征值应用、几何意义

### 国外教材
3. **《Introduction to Linear Algebra》（第5版）** - Gilbert Strang
   - Chapter 6: Eigenvalues and Eigenvectors
   - 重点：几何解释、差分方程

4. **《Linear Algebra Done Right》（第3版）** - Sheldon Axler
   - Chapter 5: Eigenvalues and Eigenvectors
   - 重点：复特征值、不变子空间

## 题型总结与思路技巧

### 特征值问题分析方法

**求特征值和特征向量**：
1. 求特征方程：$|A-\lambda I|=0$
2. 解特征多项式得特征值
3. 对每个特征值，解$(A-\lambda I)v=0$得特征向量

**判别法**：
- 对称矩阵：特征值都是实数，可正交对角化
- 正定矩阵：所有特征值>0
- 正交矩阵：$|\lambda|=1$

**重要公式**：
- $\sum \lambda_i = \text{tr}(A)$
- $\prod \lambda_i = \det(A)$
- $A$的特征值是$A^k$的特征值的$k$次幂

### 常见题型

| 题型 | 方法 |
|-----|------|
| 求特征值/特征向量 | 特征方程 |
| 判断矩阵可对角化 | 有$n$个线性无关特征向量 |
| 对称矩阵对角化 | 正交对角化 |
| 求矩阵的幂 | 利用对角化$A^k=P\Lambda^kP^{-1}$ |

## 8. 本章小结

### 8.1 重要定义
1. 特征值和特征向量的定义
2. 特征方程
3. 特征多项式

### 8.2 重要性质
1. 迹与特征值的关系
2. 行列式与特征值的关系
3. 对称矩阵的特征值都是实数
4. 对称矩阵的特征向量可以正交

### 8.3 重要应用
1. PCA降维
2. PageRank算法
3. 优化理论中的极值判断

---

**创建时间：2026年3月11日**  
**最后更新：2026年3月11日**  
**参考教材**：《高等代数简明教程》、《Introduction to Linear Algebra》

## 相关概念

- [[14_Similar_Matrices]] - 相似矩阵
- [[15_Diagonalization]] - 矩阵对角化
- [[16_Jordan_Canonical]] - 约当标准形
- [[21_SVD]] - 奇异值分解