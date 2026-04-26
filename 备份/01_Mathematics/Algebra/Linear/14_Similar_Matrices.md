---
type: concept
topic: similar_matrices
category: linear_algebra
difficulty: advanced
prerequisites:
  - [[13_Eigenvalues]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
---
# 相似矩阵 (Similar Matrices)

## 1. 定义

### 1.1 相似

设 $A$ 和 $B$ 都是 $n \times n$ 矩阵，如果存在可逆矩阵 $P$ 使得：
$$B = P^{-1}AP$$

则称 $A$ 与 $B$ **相似**，记作 $A \sim B$。

**几何意义**：$A$ 和 $B$ 表示同一个线性变换在不同基下的矩阵表示。

### 1.2 相似关系

相似关系是等价关系，满足：

1. **自反性**：$A \sim A$
   - 取 $P = I$

2. **对称性**：$A \sim B \iff B \sim A$
   - 如果 $B = P^{-1}AP$，则 $A = PBP^{-1} = (P^{-1})^{-1}BP^{-1}$

3. **传递性**：$A \sim B$ 且 $B \sim C \Rightarrow A \sim C$
   - 如果 $B = P^{-1}AP$ 且 $C = Q^{-1}BQ$，则 $C = Q^{-1}P^{-1}APQ = (PQ)^{-1}A(PQ)$

## 2. 性质

### 2.1 相似不变量

相似矩阵具有相同的：

1. **特征多项式**：$p_A(\lambda) = p_B(\lambda)$
2. **特征值**（包括代数重数）
3. **迹**：$\text{tr}(A) = \text{tr}(B)$
4. **行列式**：$\det(A) = \det(B)$
5. **秩**：$\text{rank}(A) = \text{rank}(B)$
6. **可逆性**：$A$ 可逆 $\iff$ $B$ 可逆

### 2.2 证明

**证明特征多项式相同**：

$$\begin{aligned}
p_B(\lambda) &= \det(B - \lambda I) \\\\
&= \det(P^{-1}AP - \lambda I) \\\\
&= \det(P^{-1}AP - \lambda P^{-1}P) \\\\
&= \det(P^{-1}(A - \lambda I)P) \\\\
&= \det(P^{-1})\det(A - \lambda I)\det(P) \\\\
&= \det(A - \lambda I) \\\\
&= p_A(\lambda)
\end{aligned}$$

### 2.3 相似标准形

**定理**：任何 $n \times n$ 矩阵都相似于它的约当标准形。

**推论**：$A$ 可对角化 $\iff$ $A$ 的约当标准形是对角矩阵。

## 3. 代码示例

### 3.1 判断矩阵是否相似

```python
import numpy as np

def are_similar(A, B, tol=1e-10):
    """
    判断两个矩阵是否相似
    
    参数:
        A, B: 方阵
        tol: 容差
    
    返回:
        bool: 是否相似
    """
    # 检查形状
    if A.shape != B.shape:
        return False
    
    # 检查特征值
    eigA = np.sort(np.linalg.eigvals(A))
    eigB = np.sort(np.linalg.eigvals(B))
    
    if not np.allclose(eigA, eigB, atol=tol):
        return False
    
    # 检查迹
    if not np.isclose(np.trace(A), np.trace(B), atol=tol):
        return False
    
    # 检查行列式
    if not np.isclose(np.linalg.det(A), np.linalg.det(B), atol=tol):
        return False
    
    return True

# 示例
A = np.array([[2, 1], [0, 2]])
B = np.array([[2, 0], [1, 2]])
P = np.array([[0, 1], [1, 0]])

# 验证 B = P^(-1)AP
B_check = np.linalg.inv(P) @ A @ P
print(f"是否相似: {are_similar(A, B)}")
print(f"B_check:\n{B_check}")
print(f"B:\n{B}")
```

### 3.2 相似对角化

```python
import numpy as np

def diagonalize(A, tol=1e-10):
    """
    尝试对角化矩阵
    
    参数:
        A: 方阵
        tol: 容差
    
    返回:
        P: 变换矩阵（如果可对角化）
        D: 对角矩阵（如果可对角化）
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
A = np.array([[2, 1], [1, 2]])
P, D, success = diagonalize(A)

if success:
    print(f"矩阵 A:\n{A}")
    print(f"\n变换矩阵 P:\n{P}")
    print(f"\n对角矩阵 D:\n{D}")
    print(f"\n验证 P^{-1}AP:\n{np.linalg.inv(P) @ A @ P}")
else:
    print("矩阵不可对角化")
```

## 4. 例题

### 例题 1：判断矩阵是否相似

**问题**：判断 $A = \begin{bmatrix} 2 & 1 \\\\ 0 & 3 \end{bmatrix}$ 和 $B = \begin{bmatrix} 3 & 0 \\\\ 0 & 2 \end{bmatrix}$ 是否相似。

**解**：

**方法1：检查特征值**

对于 $A$：特征值是 $\lambda_1 = 2$，$\lambda_2 = 3$
对于 $B$：特征值是 $\lambda_1 = 3$，$\lambda_2 = 2$

特征值相同，可能相似。

**方法2：检查特征向量**

对于 $A$：
- $\lambda = 2$：$(A - 2I)\mathbf{v} = \begin{bmatrix} 0 & 1 \\\\ 0 & 1 \end{bmatrix} \mathbf{v} = \mathbf{0}$，$\mathbf{v}_1 = \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}$
- $\lambda = 3$：$(A - 3I)\mathbf{v} = \begin{bmatrix} -1 & 1 \\\\ 0 & 0 \end{bmatrix} \mathbf{v} = \mathbf{0}$，$\mathbf{v}_2 = \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}$

对于 $B$：
- $\lambda = 3$：$\mathbf{v}_1 = \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}$
- $\lambda = 2$：$\mathbf{v}_2 = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}$

由于 $A$ 有两个线性无关的特征向量，$A$ 可对角化。$B$ 已经是对角矩阵，且与 $A$ 有相同的特征值，因此 $A \sim B$。

**构造相似变换矩阵**：

$P = [\mathbf{v}_1, \mathbf{v}_2] = \begin{bmatrix} 1 & 1 \\\\ 0 & 1 \end{bmatrix}$

$P^{-1} = \begin{bmatrix} 1 & -1 \\\\ 0 & 1 \end{bmatrix}$

验证：
$$P^{-1}AP = \begin{bmatrix} 1 & -1 \\\\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 1 \\\\ 0 & 3 \end{bmatrix} \begin{bmatrix} 1 & 1 \\\\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & -2 \\\\ 0 & 3 \end{bmatrix} \begin{bmatrix} 1 & 1 \\\\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\\\ 0 & 3 \end{bmatrix}$$

注意：特征值的顺序不同，结果也不同。如果调整特征值的顺序，可以得到 $B$。

### 例题 2：证明相似的性质

**问题**：证明：如果 $A \sim B$，则 $A^k \sim B^k$。

**证明**：

由于 $A \sim B$，存在可逆矩阵 $P$ 使得 $B = P^{-1}AP$。

则：
$$\begin{aligned}
B^k &= (P^{-1}AP)^k \\\\
&= P^{-1}AP \cdot P^{-1}AP \cdots P^{-1}AP \\\\
&= P^{-1}A(P P^{-1})A(P P^{-1}) \cdots AP \\\\
&= P^{-1}A^k P
\end{aligned}$$

因此 $A^k \sim B^k$。

### 例题 3：判断矩阵是否可对角化

**问题**：判断 $A = \begin{bmatrix} 2 & 1 \\\\ 0 & 2 \end{bmatrix}$ 是否可对角化。

**解**：

**第一步：求特征值**

特征方程：
$$\begin{vmatrix} 2-\lambda & 1 \\\\ 0 & 2-\lambda \end{vmatrix} = (2-\lambda)^2 = 0$$

$\lambda = 2$（二重根）

**第二步：求特征向量**

$(A - 2I)\mathbf{v} = \begin{bmatrix} 0 & 1 \\\\ 0 & 0 \end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}$

$y = 0$，$x$ 是自由的。只有一个线性无关的特征向量 $\mathbf{v} = \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}$。

**结论**：由于只有一个线性无关的特征向量（少于2个），$A$ 不可对角化。

**说明**：$A$ 的约当标准形是 $\begin{bmatrix} 2 & 1 \\\\ 0 & 2 \end{bmatrix}$ 本身。

### 例题 4：相似矩阵的特征向量关系

**问题**：设 $B = P^{-1}AP$，$\mathbf{v}$ 是 $A$ 的特征向量，证明 $P^{-1}\mathbf{v}$ 是 $B$ 的特征向量。

**证明**：

设 $A\mathbf{v} = \lambda\mathbf{v}$。

则：
$$\begin{aligned}
B(P^{-1}\mathbf{v}) &= P^{-1}AP(P^{-1}\mathbf{v}) \\\\
&= P^{-1}A(PP^{-1})\mathbf{v} \\\\
&= P^{-1}A\mathbf{v} \\\\
&= P^{-1}\lambda\mathbf{v} \\\\
&= \lambda(P^{-1}\mathbf{v})
\end{aligned}$$

因此 $P^{-1}\mathbf{v}$ 是 $B$ 的特征向量，对应的特征值仍为 $\lambda$。

### 例题 5：对称矩阵的相似对角化

**问题**：证明任何实对称矩阵都相似于对角矩阵。

**证明**：

设 $A$ 是 $n \times n$ 实对称矩阵。

1. 由特征值理论，$A$ 的特征值都是实数。
2. 对于不同的特征值，对应的特征向量正交。
3. 对于重特征值，可以找到线性无关的特征向量，并且可以正交化。
4. 因此，$A$ 有 $n$ 个正交的特征向量 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$。

构造正交矩阵 $Q = [\frac{\mathbf{v}_1}{\|\mathbf{v}_1\|}, \frac{\mathbf{v}_2}{\|\mathbf{v}_2\|}, \ldots, \frac{\mathbf{v}_n}{\|\mathbf{v}_n\|}]$。

则 $Q^{-1}AQ = Q^T AQ = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$。

因此 $A$ 相似于对角矩阵。

## 5. 机器学习应用

### 应用 1：协方差矩阵的对角化

在PCA中，协方差矩阵是对称正定的，可以正交对角化：
$$C = Q\Lambda Q^T$$

其中 $Q$ 是特征向量矩阵，$\Lambda$ 是特征值对角矩阵。

### 应用 2：马尔可夫链的稳态分析

转移矩阵 $P$ 的稳态分布是特征值为1的特征向量。

## 题型总结与思路技巧

### 相似矩阵核心要点

#### 📋 相似矩阵的等价条件

设$A, B$为$n$阶方阵，以下等价：
- 存在可逆矩阵$P$使$B = P^{-1}AP$
- $A$和$B$表示同一线性变换在不同基下的矩阵
- $A$和$B$有相同的特征多项式

### 💡 核心技巧与常用结论

#### 1. 相似不变量

相似矩阵具有相同的：
- 特征值（相同重数）
- 迹：$\text{tr}(A) = \text{tr}(B)$
- 行列式：$\det(A) = \det(B)$
- 特征多项式
- 秩

#### 2. 相似矩阵的判定

**判定相似**：
- 找可逆矩阵$P$使$B = P^{-1}AP$
- 证明有相同的Jordan标准形

**判定不相似**：
- 特征值不同
- 特征值相同但重数不同
- 相同特征值对应的Jordan块结构不同

#### 3. 相似对角化

$A$可对角化 $\Leftrightarrow$ $A$有$n$个线性无关的特征向量

**充分条件**：
- $n$个互异特征值
- 实对称矩阵

**必要条件**：
- 特征多项式的根全为实数

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 判断相似 | 找过渡矩阵 | 验证$B = P^{-1}AP$ |
| 判断不相似 | 比较不变量 | 特征值、迹、行列式 |
| 求相似标准形 | 对角化或Jordan | 特征向量个数 |
| 证明相似 | Jordan标准形 | 唯一性 |

### ⚠️ 常见错误

**错误一**：相似矩阵的特征向量相同
- 相似矩阵特征值相同，但特征向量不同
- 若$\mathbf{v}$是$A$的特征向量，则$P^{-1}\mathbf{v}$是$B$的特征向量

**错误二**：相似与合同混淆
- 相似：$B = P^{-1}AP$
- 合同：$B = P^TAP$

## 6. 课后练习

### 6.1 基础题

**教材参考**：《高等代数简明教程》第五章习题

1. 判断下列矩阵对是否相似：
   - (1) $A = \begin{bmatrix} 1 & 2 \\\\ 0 & 3 \end{bmatrix}$，$B = \begin{bmatrix} 3 & 0 \\\\ 0 & 1 \end{bmatrix}$
   - (2) $A = \begin{bmatrix} 2 & 0 \\\\ 0 & 2 \end{bmatrix}$，$B = \begin{bmatrix} 2 & 1 \\\\ 0 & 2 \end{bmatrix}$

2. 设 $A \sim B$，证明 $A^T \sim B^T$。

3. 证明：相似矩阵有相同的秩。

### 6.2 进阶题

**教材参考**：《高等代数简明教程》第五章习题

4. 判断 $A = \begin{bmatrix} 1 & 1 \\\\ 0 & 1 \end{bmatrix}$ 是否可对角化。

5. 设 $A$ 是 $n \times n$ 矩阵，证明 $A$ 可对角化 $\iff$ $A$ 有 $n$ 个线性无关的特征向量。

6. 证明：如果 $A$ 是幂等矩阵（$A^2 = A$），则 $A$ 相似于 $\begin{bmatrix} I_r & 0 \\\\ 0 & 0 \end{bmatrix}$，其中 $r = \text{rank}(A)$。

### 6.3 挑战题

**教材参考**：《高等代数简明教程》第五章习题

7. 设 $A$ 是 $n \times n$ 实矩阵，证明 $A$ 相似于 $A^T$。

8. 设 $A$ 是 $n \times n$ 矩阵，且 $A^2 = I$，证明 $A$ 可对角化，并求其相似标准形。

9. 在马尔可夫链中，证明转移矩阵的特征值满足 $|\lambda| \leq 1$，且 $\lambda = 1$ 是特征值。

## 7. 教材参考

### 国内教材
1. **《高等代数简明教程》（第2版）** - 北京大学数学系
   - 第五章：相似矩阵
   - 重点：相似性质、对角化条件

2. **《线性代数》（第6版）** - 同济大学数学系
   - 第五章：相似矩阵及二次型
   - 重点：相似对角化、应用

### 国外教材
3. **《Introduction to Linear Algebra》（第5版）** - Gilbert Strang
   - Chapter 6: Eigenvalues and Eigenvectors
   - 重点：相似变换、对角化

4. **《Linear Algebra Done Right》（第3版）** - Sheldon Axler
   - Chapter 5: Eigenvalues and Eigenvectors
   - 重点：不变子空间、谱定理

## 8. 本章小结

### 8.1 重要定义
1. 相似矩阵的定义
2. 相似关系的等价性

### 8.2 重要性质
1. 相似不变量：特征多项式、特征值、迹、行列式、秩
2. 相似关系的传递性

### 8.3 重要定理
1. 相似矩阵有相同的特征多项式
2. $A$ 可对角化 $\iff$ $A$ 有 $n$ 个线性无关的特征向量
3. 实对称矩阵可正交对角化

---

**创建时间：2026年3月11日**  
**最后更新：2026年3月11日**  
**参考教材**：《高等代数简明教程》、《Introduction to Linear Algebra》

## 相关概念

- [[13_Eigenvalues]] - 特征值与特征向量
- [[15_Diagonalization]] - 矩阵对角化
- [[16_Jordan_Canonical]] - 约当标准形

