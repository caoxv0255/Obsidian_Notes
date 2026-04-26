---
type: concept
topic: diagonalization
category: linear_algebra
difficulty: advanced
prerequisites:
  - [[14_Similar_Matrices]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
---
# 矩阵对角化 (Matrix Diagonalization)

## 1. 定义

### 1.1 对角化

$A$ 可对角化，如果存在可逆矩阵 $P$ 和对角矩阵 $D$ 使得：
$$A = PDP^{-1}$$

其中 $D = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$。

### 1.2 充要条件

$A$ 可对角化 $\iff$ $A$ 有 $n$ 个线性无关的特征向量。

**等价条件**：
1. $A$ 有 $n$ 个线性无关的特征向量
2. $A$ 的所有特征值的几何重数等于代数重数
3. $A$ 的最小多项式无重根

## 2. 对角化步骤

### 2.1 标准步骤

1. **求特征值**：解特征方程 $|A - \lambda I| = 0$
2. **求特征向量**：对每个特征值 $\lambda_i$，求解 $(A - \lambda_i I)\mathbf{v} = \mathbf{0}$
3. **构造变换矩阵**：$P = [\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n]$
4. **构造对角矩阵**：$D = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$
5. **验证**：$A = PDP^{-1}$

### 2.2 特殊情况

**对称矩阵**：可以直接正交对角化，$A = Q\Lambda Q^T$，其中 $Q$ 是正交矩阵。

## 3. 代码示例

### 3.1 矩阵对角化实现

```python
import numpy as np

def diagonalize_matrix(A, tol=1e-10):
    """
    对角化矩阵
    
    参数:
        A: 方阵
        tol: 容差
    
    返回:
        P: 变换矩阵
        D: 对角矩阵
        success: 是否成功
    """
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    # 检查特征向量是否线性无关
    P = eigenvectors
    if abs(np.linalg.det(P)) < tol:
        return None, None, False
    
    D = np.diag(eigenvalues)
    return P, D, True

# 示例
A = np.array([[4, 1], [2, 3]])
P, D, success = diagonalize_matrix(A)

if success:
    print(f"矩阵 A:\n{A}")
    print(f"\n变换矩阵 P:\n{P}")
    print(f"\n对角矩阵 D:\n{D}")
    print(f"\n验证 PDP^{-1}:\n{P @ D @ np.linalg.inv(P)}")
    print(f"\n误差: {np.linalg.norm(A - P @ D @ np.linalg.inv(P)):.6e}")
else:
    print("矩阵不可对角化")
```

### 3.2 计算矩阵幂

```python
import numpy as np

def matrix_power_diagonalization(A, k):
    """
    使用对角化计算矩阵幂
    
    参数:
        A: 方阵
        k: 幂次
    
    返回:
        A^k: 矩阵的k次幂
    """
    P, D, success = diagonalize_matrix(A)
    
    if not success:
        raise ValueError("矩阵不可对角化")
    
    D_k = np.diag(np.diag(D) ** k)
    A_k = P @ D_k @ np.linalg.inv(P)
    
    return A_k

# 示例
A = np.array([[4, 1], [2, 3]])
for k in [1, 2, 5, 10]:
    A_k = matrix_power_diagonalization(A, k)
    print(f"\nA^{k}:\n{A_k}")
```

## 4. 例题

### 例题 1：对角化对称矩阵

**问题**：对角化 $A = \begin{bmatrix} 2 & 1 \\\\ 1 & 2 \end{bmatrix}$。

**解**：

**第一步：求特征值**

$$|A - \lambda I| = \begin{vmatrix} 2-\lambda & 1 \\\\ 1 & 2-\lambda \end{vmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0$$

$\lambda_1 = 3$，$\lambda_2 = 1$

**第二步：求特征向量**

对于 $\lambda_1 = 3$：
$$(A - 3I)\mathbf{v} = \begin{bmatrix} -1 & 1 \\\\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}$$

$-x + y = 0$，故 $x = y$。取 $\mathbf{v}_1 = \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}$。

对于 $\lambda_2 = 1$：
$$(A - I)\mathbf{v} = \begin{bmatrix} 1 & 1 \\\\ 1 & 1 \end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}$$

$x + y = 0$，故 $y = -x$。取 $\mathbf{v}_2 = \begin{bmatrix} 1 \\\\ -1 \end{bmatrix}$。

**第三步：构造变换矩阵**

$$P = [\mathbf{v}_1, \mathbf{v}_2] = \begin{bmatrix} 1 & 1 \\\\ 1 & -1 \end{bmatrix}$$

$$D = \text{diag}(3, 1) = \begin{bmatrix} 3 & 0 \\\\ 0 & 1 \end{bmatrix}$$

**第四步：验证**

$$P^{-1} = -\frac{1}{2}\begin{bmatrix} -1 & -1 \\\\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 1/2 & 1/2 \\\\ 1/2 & -1/2 \end{bmatrix}$$

$$PDP^{-1} = \begin{bmatrix} 1 & 1 \\\\ 1 & -1 \end{bmatrix} \begin{bmatrix} 3 & 0 \\\\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1/2 & 1/2 \\\\ 1/2 & -1/2 \end{bmatrix} = \begin{bmatrix} 3 & 1 \\\\ 3 & -1 \end{bmatrix} \begin{bmatrix} 1/2 & 1/2 \\\\ 1/2 & -1/2 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\\\ 1 & 2 \end{bmatrix} = A$$ ✓

### 例题 2：对角化 3×3 矩阵

**问题**：对角化 $A = \begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 2 & 1 \\\\ 0 & 1 & 2 \end{bmatrix}$。

**解**：

**第一步：求特征值**

由于 $A$ 是分块对角矩阵，特征值包括 $\lambda = 1$ 和 $\begin{bmatrix} 2 & 1 \\\\ 1 & 2 \end{bmatrix}$ 的特征值。

$\begin{vmatrix} 2-\lambda & 1 \\\\ 1 & 2-\lambda \end{vmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0$

$\lambda = 3$ 或 $\lambda = 1$

因此 $A$ 的特征值为 $\lambda_1 = 3$，$\lambda_2 = \lambda_3 = 1$（二重根）。

**第二步：求特征向量**

对于 $\lambda_1 = 3$：
$$(A - 3I)\mathbf{v} = \begin{bmatrix} -2 & 0 & 0 \\\\ 0 & -1 & 1 \\\\ 0 & 1 & -1 \end{bmatrix} \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix}$$

$x = 0$，$-y + z = 0$，故 $y = z$。取 $\mathbf{v}_1 = \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \end{bmatrix}$。

对于 $\lambda_2 = \lambda_3 = 1$：
$$(A - I)\mathbf{v} = \begin{bmatrix} 0 & 0 & 0 \\\\ 0 & 1 & 1 \\\\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix}$$

$y + z = 0$，故 $z = -y$。$x$ 是自由的。

取两个线性无关的特征向量：
$\mathbf{v}_2 = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}$，$\mathbf{v}_3 = \begin{bmatrix} 0 \\\\ 1 \\\\ -1 \end{bmatrix}$

**第三步：构造变换矩阵**

$$P = \begin{bmatrix} 0 & 1 & 0 \\\\ 1 & 0 & 1 \\\\ 1 & 0 & -1 \end{bmatrix}$$

$$D = \text{diag}(3, 1, 1) = \begin{bmatrix} 3 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \end{bmatrix}$$

### 例题 3：计算矩阵幂

**问题**：计算 $A^{10}$，其中 $A = \begin{bmatrix} 4 & 1 \\\\ 2 & 3 \end{bmatrix}$。

**解**：

**第一步：对角化 $A$**

特征方程：$(4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10 = 0$

$\lambda_1 = 5$，$\lambda_2 = 2$

对于 $\lambda_1 = 5$：$\mathbf{v}_1 = \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}$
对于 $\lambda_2 = 2$：$\mathbf{v}_2 = \begin{bmatrix} 1 \\\\ -2 \end{bmatrix}$

$$P = \begin{bmatrix} 1 & 1 \\\\ 1 & -2 \end{bmatrix}$$，$P^{-1} = \begin{bmatrix} 2/3 & 1/3 \\\\ 1/3 & -1/3 \end{bmatrix}$

$$D = \begin{bmatrix} 5 & 0 \\\\ 0 & 2 \end{bmatrix}$$

**第二步：计算 $A^{10}$**

$$A^{10} = PD^{10}P^{-1} = \begin{bmatrix} 1 & 1 \\\\ 1 & -2 \end{bmatrix} \begin{bmatrix} 5^{10} & 0 \\\\ 0 & 2^{10} \end{bmatrix} \begin{bmatrix} 2/3 & 1/3 \\\\ 1/3 & -1/3 \end{bmatrix}$$

$$= \begin{bmatrix} 5^{10} & 2^{10} \\\\ 5^{10} & -2^{11} \end{bmatrix} \begin{bmatrix} 2/3 & 1/3 \\\\ 1/3 & -1/3 \end{bmatrix}$$

$$= \frac{1}{3} \begin{bmatrix} 2 \cdot 5^{10} + 2^{10} & 5^{10} - 2^{10} \\\\ 2 \cdot 5^{10} - 2^{11} & 5^{10} + 2^{11} \end{bmatrix}$$

### 例题 4：判断矩阵是否可对角化

**问题**：判断 $A = \begin{bmatrix} 3 & 1 \\\\ 0 & 3 \end{bmatrix}$ 是否可对角化。

**解**：

特征方程：$(3-\lambda)^2 = 0$

$\lambda = 3$（二重根）

求特征向量：
$$(A - 3I)\mathbf{v} = \begin{bmatrix} 0 & 1 \\\\ 0 & 0 \end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}$$

$y = 0$，$x$ 是自由的。只有一个线性无关的特征向量 $\mathbf{v} = \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}$。

**结论**：由于只有一个线性无关的特征向量（少于2个），$A$ 不可对角化。

### 例题 5：正交对角化对称矩阵

**问题**：正交对角化 $A = \begin{bmatrix} 1 & 2 \\\\ 2 & 1 \end{bmatrix}$。

**解**：

**第一步：求特征值**

$\lambda_1 = 3$，$\lambda_2 = -1$

**第二步：求特征向量并正交化**

对于 $\lambda_1 = 3$：$\mathbf{v}_1 = \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}$
对于 $\lambda_2 = -1$：$\mathbf{v}_2 = \begin{bmatrix} 1 \\\\ -1 \end{bmatrix}$

**第三步：归一化**

$$\mathbf{q}_1 = \frac{\mathbf{v}_1}{\|\mathbf{v}_1\|} = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\\\ 1 \end{bmatrix}$$

$$\mathbf{q}_2 = \frac{\mathbf{v}_2}{\|\mathbf{v}_2\|} = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\\\ -1 \end{bmatrix}$$

**第四步：构造正交矩阵**

$$Q = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\\\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}$$

$$\Lambda = \begin{bmatrix} 3 & 0 \\\\ 0 & -1 \end{bmatrix}$$

**验证**：$Q^T AQ = \Lambda$

## 5. 机器学习应用

### 应用 1：PCA中的对角化

PCA使用协方差矩阵的对角化进行降维：
$$C = \frac{1}{n}XX^T = Q\Lambda Q^T$$

其中 $Q$ 是特征向量矩阵，$\Lambda$ 是特征值对角矩阵。

### 应用 2：求解线性微分方程组

对角化用于求解常系数线性微分方程组：
$$\frac{d\mathbf{x}}{dt} = A\mathbf{x}$$

解为 $\mathbf{x}(t) = Pe^{Dt}P^{-1}\mathbf{x}(0)$。

## 题型总结与思路技巧

### 对角化的判定与实现

#### 📋 可对角化的等价条件

以下条件等价：
- $A$可对角化
- $A$有$n$个线性无关的特征向量
- 每个特征值的几何重数等于代数重数
- 极小多项式无重根

### 💡 核心技巧与常用结论

#### 1. 对角化步骤

1. 求特征值：解$|A - \lambda I| = 0$
2. 求特征向量：对每个$\lambda_i$，解$(A - \lambda_i I)\mathbf{v} = 0$
3. 检查可对角化：$\sum \dim(E_\lambda) = n$？
4. 构造$P$和$\Lambda$：$P = [\mathbf{v}_1 \cdots \mathbf{v}_n]$，$\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_n)$

#### 2. 几何重数与代数重数

- **代数重数**：特征值在特征多项式中的重数
- **几何重数**：对应特征空间的维数
- **关键**：几何重数 ≤ 代数重数

#### 3. 对角化应用

**求矩阵幂**：$A^n = P\Lambda^n P^{-1}$

**求矩阵函数**：$f(A) = Pf(\Lambda)P^{-1}$

**解微分方程**：$\mathbf{x}(t) = Pe^{\Lambda t}P^{-1}\mathbf{x}_0$

#### 4. 正交对角化（对称矩阵）

对称矩阵$A$：$A = Q\Lambda Q^T$
- $Q$是正交矩阵
- 特征向量可以选为正交

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 判断可否对角化 | 检查几何重数 | $\dim E_\lambda = m_\lambda$ |
| 求对角化 | 特征值+特征向量 | 构造$P$和$\Lambda$ |
| 正交对角化 | 对称矩阵+Gram-Schmidt | 特征向量单位正交化 |
| 应用：求$A^n$ | 对角化 | $\Lambda^n$对角元素n次幂 |

### ⚠️ 常见错误

**错误一**：可对角化条件
- 特征值互异 ⟹ 可对角化（充分条件）
- 特征值有重根时，必须检查几何重数

**错误二**：特征向量选择
- 对角化要求特征向量线性无关
- 每个特征值对应的特征向量要取极大线性无关组

**错误三**：对角化顺序
- $P$的列向量与$\Lambda$的对角元素一一对应
- 顺序不能搞错

## 6. 课后练习

### 6.1 基础题

**教材参考**：《高等代数简明教程》第五章习题

1. 对角化下列矩阵：
   - (1) $A = \begin{bmatrix} 1 & 2 \\\\ 2 & 1 \end{bmatrix}$
   - (2) $A = \begin{bmatrix} 2 & 1 \\\\ 0 & 3 \end{bmatrix}$

2. 计算 $A^5$，其中 $A = \begin{bmatrix} 3 & 1 \\\\ 0 & 2 \end{bmatrix}$。

3. 判断 $A = \begin{bmatrix} 1 & 1 \\\\ 0 & 1 \end{bmatrix}$ 是否可对角化。

### 6.2 进阶题

**教材参考**：《高等代数简明教程》第五章习题

4. 对角化 $A = \begin{bmatrix} 1 & 0 & 1 \\\\ 0 & 2 & 0 \\\\ 1 & 0 & 1 \end{bmatrix}$。

5. 证明：如果 $A$ 是可对角化的矩阵，则 $A^k$ 也是可对角化的。

6. 设 $A$ 是 $n \times n$ 矩阵，证明 $A$ 可对角化 $\iff$ $A$ 的最小多项式无重根。

### 6.3 挑战题

**教材参考**：《高等代数简明教程》第五章习题

7. 设 $A$ 是 $n \times n$ 矩阵，证明 $A$ 可对角化 $\iff$ 对于每个特征值 $\lambda$，$\text{dim}(N(A - \lambda I)) = \text{代数重数}$。

8. 在PCA中，证明协方差矩阵的特征向量对应最大方差的方向。

9. 设 $A$ 是实对称矩阵，证明 $A$ 可以正交对角化，且特征向量构成正交基。

## 7. 教材参考

### 国内教材
1. **《高等代数简明教程》（第2版）** - 北京大学数学系
   - 第五章：相似矩阵与对角化
   - 重点：对角化条件、应用

2. **《线性代数》（第6版）** - 同济大学数学系
   - 第五章：相似矩阵及二次型
   - 重点：实对称矩阵对角化

### 国外教材
3. **《Introduction to Linear Algebra》（第5版）** - Gilbert Strang
   - Chapter 6: Eigenvalues and Eigenvectors
   - 重点：对角化应用

4. **《Linear Algebra Done Right》（第3版）** - Sheldon Axler
   - Chapter 5: Eigenvalues and Eigenvectors
   - 重点：谱定理

## 8. 本章小结

### 8.1 重要定义
1. 矩阵对角化的定义
2. 可对角化的充要条件

### 8.2 重要性质
1. 对角化矩阵的计算
2. 矩阵幂的计算

### 8.3 重要应用
1. 计算矩阵幂
2. 求解微分方程组
3. PCA降维

---

**创建时间：2026年3月11日**  
**最后更新：2026年3月11日**  
**参考教材**：《高等代数简明教程》、《Introduction to Linear Algebra》

## 相关概念

- [[13_Eigenvalues]] - 特征值与特征向量
- [[14_Similar_Matrices]] - 相似矩阵
- [[16_Jordan_Canonical]] - 约当标准形

