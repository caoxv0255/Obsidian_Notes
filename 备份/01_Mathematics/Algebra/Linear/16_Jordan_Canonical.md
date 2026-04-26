---
type: concept
topic: jordan_canonical
category: linear_algebra
difficulty: advanced
prerequisites:
  - [[15_Diagonalization]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
---
# 约当标准形 (Jordan Canonical Form)

## 1. 定义

### 1.1 约当块

形如
$$J_k(\lambda) = \begin{bmatrix}
\lambda & 1 & & \\\\
& \lambda & \ddots & \\\\
& & \ddots & 1 \\\\
& & & \lambda
\end{bmatrix}_{k \times k}$$

的矩阵称为 $k$ 阶约当块，对角线元素都是 $\lambda$，超对角线元素都是 1。

### 1.2 约当矩阵

约当矩阵是分块对角矩阵，每个对角块是一个约当块：
$$J = \begin{bmatrix}
J_{k_1}(\lambda_1) & & & \\\\
& J_{k_2}(\lambda_2) & & \\\\
& & \ddots & \\\\
& & & J_{k_m}(\lambda_m)
\end{bmatrix}$$

### 1.3 约当标准形

对于任意 $n \times n$ 复矩阵 $A$，存在可逆矩阵 $P$ 使得：
$$A = PJP^{-1}$$

其中 $J$ 是约当矩阵，称为 $A$ 的约当标准形。

## 2. 性质

### 2.1 唯一性

约当标准形在约当块的排列顺序下是唯一的。

### 2.2 与对角化的关系

- 如果 $A$ 可对角化，其约当标准形就是对角矩阵
- 约当标准形是对角化的推广

### 2.3 几何意义

每个约当块对应一个不变子空间。

## 3. 代码示例

### 3.1 计算约当标准形

```python
import numpy as np
from scipy import linalg

def jordan_canonical_form(A):
    """
    计算约当标准形
    
    参数:
        A: 方阵
    
    返回:
        P: 变换矩阵
        J: 约当标准形
        Jordan_blocks: 约当块信息
    """
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    # 这里简化处理，实际约当标准形计算更复杂
    # 使用 SciPy 的 jordan 函数（如果可用）
    try:
        from scipy.linalg import jordan
        P, J = jordan(A)
        return P, J
    except ImportError:
        print("Scipy的jordan函数不可用，使用特征值分解代替")
        # 对于可对角化的矩阵，特征值分解就是约当标准形
        return eigenvectors, np.diag(eigenvalues)

# 示例
A = np.array([[2, 1], [0, 2]])
P, J = jordan_canonical_form(A)

print(f"矩阵 A:\n{A}")
print(f"\n约当标准形 J:\n{J}")
print(f"\n变换矩阵 P:\n{P}")
```

## 4. 例题

### 例题 1：求约当标准形（可对角化）

**问题**：求 $A = \begin{bmatrix} 2 & 0 \\\\ 0 & 3 \end{bmatrix}$ 的约当标准形。

**解**：$A$ 已经是对角矩阵，因此其约当标准形就是它自己：
$$J = \begin{bmatrix} 2 & 0 \\\\ 0 & 3 \end{bmatrix}$$

### 例题 2：求约当标准形（不可对角化）

**问题**：求 $A = \begin{bmatrix} 2 & 1 \\\\ 0 & 2 \end{bmatrix}$ 的约当标准形。

**解**：$A$ 本身就是一个约当块：
$$J = \begin{bmatrix} 2 & 1 \\\\ 0 & 2 \end{bmatrix} = J_2(2)$$

### 例题 3：求约当标准形（3×3矩阵）

**问题**：求 $A = \begin{bmatrix} 3 & 1 & 0 \\\\ 0 & 3 & 1 \\\\ 0 & 0 & 3 \end{bmatrix}$ 的约当标准形。

**解**：$A$ 是一个约当块：
$$J = \begin{bmatrix} 3 & 1 & 0 \\\\ 0 & 3 & 1 \\\\ 0 & 0 & 3 \end{bmatrix} = J_3(3)$$

### 例题 4：约当块的性质

**问题**：设 $J = J_k(\lambda)$，求 $J^m$。

**解**：

$$J = \lambda I + N$$

其中 $N$ 是幂零矩阵（$N^k = 0$）：
$$N = \begin{bmatrix}
0 & 1 & & \\\\
& 0 & \ddots & \\\\
& & \ddots & 1 \\\\
& & & 0
\end{bmatrix}$$

利用二项式定理：
$$J^m = (\lambda I + N)^m = \sum_{j=0}^{m} \binom{m}{j} \lambda^{m-j} N^j$$

由于 $N^k = 0$，求和只到 $j = \min(m, k-1)$。

### 例题 5：利用约当标准形计算矩阵函数

**问题**：计算 $e^{At}$，其中 $A = \begin{bmatrix} 2 & 1 \\\\ 0 & 2 \end{bmatrix}$。

**解**：

$A = J_2(2) = 2I + N$，其中 $N = \begin{bmatrix} 0 & 1 \\\\ 0 & 0 \end{bmatrix}$，$N^2 = 0$。

$$e^{At} = e^{(2I + N)t} = e^{2It} \cdot e^{Nt} = e^{2t} I \cdot (I + Nt) = e^{2t} \begin{bmatrix} 1 & t \\\\ 0 & 1 \end{bmatrix}$$

## 题型总结与思路技巧

### Jordan标准形核心要点

#### 📋 Jordan标准形的结构

每个方阵的Jordan标准形是准对角块矩阵，由若干Jordan块组成。

### 💡 核心技巧与常用结论

#### 1. Jordan块的形式

$$J_k(\lambda) = \begin{bmatrix} \lambda & 1 & & \\ & \lambda & \ddots & \\ & & \ddots & 1 \\ & & & \lambda \end{bmatrix}_{k \times k}$$

#### 2. 求Jordan标准形步骤

1. 求特征值：解$|A-\lambda I|=0$
2. 对每个特征值，求Jordan块
3. 构造变换矩阵$P$
4. 验证：$A = PJP^{-1}$

#### 3. 几何重数与代数重数

- **代数重数**：特征值在特征多项式中的重数
- **几何重数**：对应特征空间的维数
- **关键**：几何重数 = Jordan块个数

#### 4. 可对角化判定

- 可对角化 ⟺ 所有Jordan块都是$1\times 1$
- ⟺ 每个特征值的几何重数 = 代数重数

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 求Jordan标准形 | 特征值+广义特征向量 | 唯一性 |
| 判断可对角化 | 检查Jordan块大小 | 全为1×1？ |
| 求矩阵函数 | $f(A)=Pf(J)P^{-1}$ | 利用Jordan块函数 |
| 计算矩阵幂 | $A^n=PJ^nP^{-1}$ | Jordan块幂公式 |

### ⚠️ 常见错误

**错误一**：混淆特征向量与广义特征向量
- 特征向量：$(A-\lambda I)\mathbf{v}=\mathbf{0}$
- 广义特征向量：$(A-\lambda I)^k\mathbf{v}=\mathbf{0}$

**错误二**：Jordan块构造顺序
- Jordan块排列顺序不唯一
- 但标准形结构唯一

**错误三**：可对角化误判
- Jordan块有大小>1 ⟹ 不可对角化

## 5. 课后练习

### 5.1 基础题

**教材参考**：《高等代数简明教程》第五章习题

1. 求下列矩阵的约当标准形：
   - (1) $A = \begin{bmatrix} 1 & 0 \\\\ 0 & 2 \end{bmatrix}$
   - (2) $A = \begin{bmatrix} 1 & 1 \\\\ 0 & 1 \end{bmatrix}$

2. 设 $J = J_3(2)$，计算 $J^2$ 和 $J^3$。

3. 证明：约当块 $J_k(\lambda)$ 的特征值是 $\lambda$，代数重数是 $k$。

### 5.2 进阶题

**教材参考**：《高等代数简明教程》第五章习题

4. 求矩阵 $A = \begin{bmatrix} 3 & 1 & 0 \\\\ 0 & 3 & 0 \\\\ 0 & 0 & 2 \end{bmatrix}$ 的约当标准形。

5. 设 $A = PJP^{-1}$，证明 $e^A = Pe^JP^{-1}$。

6. 证明：任何方阵都相似于它的约当标准形。

### 5.3 挑战题

**教材参考**：《高等代数简明教程》第五章习题

7. 研究约当标准形在求解线性微分方程组中的应用。

8. 证明：矩阵 $A$ 可对角化 $\iff$ $A$ 的最小多项式无重根。

9. 在控制理论中，研究约当标准形对系统可控性和可观性的影响。

## 6. 教材参考

### 国内教材
1. **《高等代数简明教程》（第2版）** - 北京大学数学系
   - 第五章：相似矩阵
   - 重点：约当标准形理论

2. **《线性代数》（第6版）** - 同济大学数学系
   - 第五章：相似矩阵及二次型
   - 重点：对角化应用

### 国外教材
3. **《Introduction to Linear Algebra》（第5版）** - Gilbert Strang
   - Chapter 6: Eigenvalues and Eigenvectors
   - 重点：特征值应用

4. **《Linear Algebra Done Right》（第3版）** - Sheldon Axler
   - Chapter 8: Operators on Complex Vector Spaces
   - 重点：广义特征向量

## 7. 本章小结

### 7.1 重要定义
1. 约当块的定义
2. 约当矩阵的定义
3. 约当标准形的存在性

### 7.2 重要性质
1. 约当标准形的唯一性
2. 约当块的结构

### 7.3 重要应用
1. 计算矩阵函数
2. 求解微分方程组

---

**创建时间：2026年3月11日**  
**最后更新：2026年3月11日**  
**参考教材**：《高等代数简明教程》、《Introduction to Linear Algebra》

## 相关概念

- [[13_Eigenvalues]] - 特征值与特征向量
- [[14_Similar_Matrices]] - 相似矩阵
- [[15_Diagonalization]] - 矩阵对角化

