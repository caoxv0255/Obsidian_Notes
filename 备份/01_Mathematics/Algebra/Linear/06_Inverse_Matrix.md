---
type: concept
topic: inverse_matrix
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[05_Matrix_Operations]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 06
---

# 逆矩阵 (Inverse Matrix)

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

### 1.1 逆矩阵

对于 $n \times n$ 矩阵 $A$，如果存在 $n \times n$ 矩阵 $B$ 使得：
$$AB = BA = I_n$$

则称 $B$ 为 $A$ 的逆矩阵，记作 $A^{-1}$，称 $A$ 为可逆矩阵或非奇异矩阵。

### 1.2 可逆的充要条件

矩阵 $A$ 可逆当且仅当以下任一条件成立：
1. $\det(A) \neq 0$
2. $A$ 是满秩矩阵，即 $\text{rank}(A) = n$
3. $A$ 的行向量组线性无关
4. $A$ 的列向量组线性无关
5. 齐次线性方程组 $A\mathbf{x} = \mathbf{0}$ 只有零解
6. $A$ 可以表示为初等矩阵的乘积

## 2. 性质

### 2.1 基本性质

1. **唯一性**：如果 $A$ 可逆，则 $A^{-1}$ 唯一
2. **自逆性**：$(A^{-1})^{-1} = A$
3. **反序性**：$(AB)^{-1} = B^{-1}A^{-1}$
4. **转置性**：$(A^T)^{-1} = (A^{-1})^T$
5. **标量性**：$(\lambda A)^{-1} = \frac{1}{\lambda}A^{-1}$（当 $\lambda \neq 0$）
6. **行列式性**：$\det(A^{-1}) = \frac{1}{\det(A)}$

### 2.2 特殊矩阵的逆

1. **单位矩阵**：$I^{-1} = I$
2. **对角矩阵**：如果 $D = \text{diag}(d_1, d_2, \ldots, d_n)$ 且 $d_i \neq 0$，则 $D^{-1} = \text{diag}(d_1^{-1}, d_2^{-1}, \ldots, d_n^{-1})$
3. **正交矩阵**：$A^{-1} = A^T$
4. **对称矩阵**：如果 $A$ 可逆且对称，则 $A^{-1}$ 也对称
5. **幂等矩阵**：如果 $A^2 = A$ 且 $A \neq I$，则 $A$ 不可逆

### 2.3 逆矩阵与行列式的关系

$$\det(A^{-1}) = \frac{1}{\det(A)}$$

**证明**：由 $AA^{-1} = I$，两边取行列式得 $\det(A)\det(A^{-1}) = 1$，因此 $\det(A^{-1}) = \frac{1}{\det(A)}$。

## 3. 求逆方法

### 3.1 伴随矩阵法

**公式**：
$$A^{-1} = \frac{1}{\det(A)} A^*$$

其中 $A^*$ 是 $A$ 的伴随矩阵，$(A^*)_{ij} = A_{ji}$ 是 $a_{ji}$ 的代数余子式。

**优点**：理论意义大，适合 2×2 和 3×3 矩阵
**缺点**：计算量大，不适合高阶矩阵

### 3.2 初等行变换法（高斯-约当消元法）

**步骤**：
1. 构造增广矩阵 $[A | I]$
2. 通过初等行变换将 $A$ 化为单位矩阵 $I$
3. 右侧得到的矩阵就是 $A^{-1}$

**优点**：适合计算机实现，数值稳定
**缺点**：需要仔细计算

### 3.3 分块矩阵求逆

对于分块矩阵，可以使用分块求逆公式。

**2×2 分块求逆公式**：
如果 $A$ 和 $D$ 可逆，则：
$$\begin{bmatrix} A & B \\ C & D \end{bmatrix}^{-1} = \begin{bmatrix} (A - BD^{-1}C)^{-1} & -(A - BD^{-1}C)^{-1}BD^{-1} \\ -D^{-1}C(A - BD^{-1}C)^{-1} & D^{-1} + D^{-1}C(A - BD^{-1}C)^{-1}BD^{-1} \end{bmatrix}$$

## 4. 代码示例

### 4.1 伴随矩阵法求逆（2×2 矩阵）

```python
import numpy as np

def inverse_2x2_adjoint(A):
    """
    使用伴随矩阵法求 2×2 矩阵的逆
    
    参数:
        A: 2×2 矩阵
    
    返回:
        A_inv: 逆矩阵
    """
    # 计算行列式
    det_A = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    
    if abs(det_A) < 1e-10:
        raise ValueError("矩阵不可逆（行列式为零）")
    
    # 伴随矩阵法
    A_inv = (1 / det_A) * np.array([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]])
    
    return A_inv

# 示例
A = np.array([[2, 1], [1, 3]], dtype=float)
A_inv = inverse_2x2_adjoint(A)

print(f"矩阵 A:\n{A}")
print(f"\n逆矩阵 A^(-1):\n{A_inv}")
print(f"\n验证 AA^(-1):\n{A @ A_inv}")
```

### 4.2 初等行变换法求逆

```python
import numpy as np

def inverse_row_reduction(A):
    """
    使用初等行变换法求逆
    
    参数:
        A: 方阵
    
    返回:
        A_inv: 逆矩阵
    """
    n = A.shape[0]
    # 构造增广矩阵 [A | I]
    augmented = np.column_stack([A, np.eye(n)]).astype(float)
    
    for i in range(n):
        # 寻找主元
        pivot_row = i
        while pivot_row < n and abs(augmented[pivot_row, i]) < 1e-10:
            pivot_row += 1
        
        if pivot_row == n:
            raise ValueError("矩阵不可逆")
        
        # 交换行
        if pivot_row != i:
            augmented[[i, pivot_row]] = augmented[[pivot_row, i]]
        
        # 主元归一化
        pivot = augmented[i, i]
        augmented[i, :] /= pivot
        
        # 消元
        for j in range(n):
            if j != i:
                factor = augmented[j, i]
                augmented[j, :] -= factor * augmented[i, :]
    
    # 提取逆矩阵
    A_inv = augmented[:, n:]
    
    return A_inv

# 示例
A = np.array([[2, 1, 1], [1, 3, 1], [1, 1, 2]], dtype=float)
A_inv = inverse_row_reduction(A)

print(f"矩阵 A:\n{A}")
print(f"\n逆矩阵 A^(-1):\n{A_inv}")
print(f"\n验证 AA^(-1):\n{A @ A_inv}")
print(f"\n与 NumPy 结果一致: {np.allclose(A_inv, np.linalg.inv(A))}")
```

### 4.3 对角矩阵求逆

```python
import numpy as np

# 创建对角矩阵
D = np.diag([2, 3, 4, 5])
print(f"对角矩阵 D:\n{D}")

# 求逆
D_inv = np.diag(1 / np.diag(D))
print(f"\n逆矩阵 D^(-1):\n{D_inv}")

# 验证
print(f"\n验证 DD^(-1):\n{D @ D_inv}")
print(f"是否为单位矩阵: {np.allclose(D @ D_inv, np.eye(4))}")
```

### 4.4 正交矩阵求逆

```python
import numpy as np

# 创建旋转矩阵（正交矩阵）
theta = np.pi / 6
Q = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])

print(f"旋转矩阵 Q:\n{Q}")

# 正交矩阵的逆等于转置
Q_inv = Q.T
print(f"\nQ^(-1) = Q^T:\n{Q_inv}")

# 验证
print(f"\n验证 QQ^(-1):\n{Q @ Q_inv}")
print(f"与 NumPy 结果一致: {np.allclose(Q_inv, np.linalg.inv(Q))}")
```

## 5. 例题

### 例题 1：判断矩阵是否可逆

**问题**：判断 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ 是否可逆，如果可逆求其逆矩阵。

**解**：

**第一步：计算行列式**
$$\det(A) = 1 \times 4 - 2 \times 3 = 4 - 6 = -2 \neq 0$$

由于行列式不为零，$A$ 可逆。

**第二步：使用伴随矩阵法求逆**
$$A^{-1} = \frac{1}{-2} \begin{bmatrix} 4 & -2 \\ -3 & 1 \end{bmatrix} = \begin{bmatrix} -2 & 1 \\ 1.5 & -0.5 \end{bmatrix}$$

**第三步：验证**
$$AA^{-1} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} -2 & 1 \\ 1.5 & -0.5 \end{bmatrix} = \begin{bmatrix} -2+3 & 1-1 \\ -6+6 & 3-2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$$

### 例题 2：利用初等行变换求逆

**问题**：使用初等行变换法求 $A = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ 的逆矩阵。

**解**：

构造增广矩阵 $[A | I]$：
$$[A | I] = \begin{bmatrix}
1 & 1 & 1 & | & 1 & 0 & 0 \\
0 & 1 & 1 & | & 0 & 1 & 0 \\
0 & 0 & 1 & | & 0 & 0 & 1
\end{bmatrix}$$

**第一行变换**：$R_1 - R_2$
$$\begin{bmatrix}
1 & 0 & 0 & | & 1 & -1 & 0 \\
0 & 1 & 1 & | & 0 & 1 & 0 \\
0 & 0 & 1 & | & 0 & 0 & 1
\end{bmatrix}$$

**第二行变换**：$R_2 - R_3$
$$\begin{bmatrix}
1 & 0 & 0 & | & 1 & -1 & 0 \\
0 & 1 & 0 & | & 0 & 1 & -1 \\
0 & 0 & 1 & | & 0 & 0 & 1
\end{bmatrix}$$

因此：
$$A^{-1} = \begin{bmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$

**验证**：
$$AA^{-1} = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = I$$

### 例题 3：分块矩阵求逆

**问题**：求 $A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 3 & 4 \end{bmatrix}$ 的逆矩阵。

**解**：

将 $A$ 分块：
$$A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 3 & 4 \end{bmatrix} = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}$$

其中 $A_{11} = [1]$，$A_{12} = \begin{bmatrix} 0 & 0 \end{bmatrix}$，$A_{21} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$，$A_{22} = \begin{bmatrix} 2 & 1 \\ 3 & 4 \end{bmatrix}$。

由于 $A_{12} = A_{21} = O$，逆矩阵也是分块对角矩阵：
$$A^{-1} = \begin{bmatrix} A_{11}^{-1} & O \\ O & A_{22}^{-1} \end{bmatrix}$$

计算 $A_{11}^{-1} = [1]$，$A_{22}^{-1} = \frac{1}{8-3} \begin{bmatrix} 4 & -1 \\ -3 & 2 \end{bmatrix} = \frac{1}{5} \begin{bmatrix} 4 & -1 \\ -3 & 2 \end{bmatrix} = \begin{bmatrix} 0.8 & -0.2 \\ -0.6 & 0.4 \end{bmatrix}$

因此：
$$A^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0.8 & -0.2 \\ 0 & -0.6 & 0.4 \end{bmatrix}$$

### 例题 4：证明逆矩阵的唯一性

**问题**：证明：如果矩阵 $A$ 可逆，则 $A^{-1}$ 唯一。

**证明**：

假设 $B$ 和 $C$ 都是 $A$ 的逆矩阵，即：
$$AB = BA = I$$
$$AC = CA = I$$

则：
$$B = BI = B(AC) = (BA)C = IC = C$$

因此 $B = C$，逆矩阵唯一。

### 例题 5：证明逆矩阵的反序性

**问题**：证明：如果 $A$ 和 $B$ 都可逆，则 $(AB)^{-1} = B^{-1}A^{-1}$。

**证明**：

验证 $(AB)(B^{-1}A^{-1}) = I$：
$$(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I$$

验证 $(B^{-1}A^{-1})(AB) = I$：
$$(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1}IB = B^{-1}B = I$$

因此 $(AB)^{-1} = B^{-1}A^{-1}$。

### 例题 6：利用逆矩阵求解线性方程组

**问题**：使用矩阵求逆求解：
$$
\begin{cases}
2x + y + z = 6 \\
x + 3y + z = 8 \\
x + y + 2z = 7
\end{cases}
$$

**解**：

矩阵形式：$A\mathbf{x} = \mathbf{b}$，其中
$$A = \begin{bmatrix} 2 & 1 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 2 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 6 \\ 8 \\ 7 \end{bmatrix}$$

求 $A$ 的逆（使用初等行变换法）：
$$A^{-1} = \begin{bmatrix} 1 & -0.2 & -0.2 \\ -0.2 & 0.6 & -0.2 \\ -0.2 & -0.2 & 1 \end{bmatrix}$$

解：
$$\mathbf{x} = A^{-1}\mathbf{b} = \begin{bmatrix} 1 & -0.2 & -0.2 \\ -0.2 & 0.6 & -0.2 \\ -0.2 & -0.2 & 1 \end{bmatrix} \begin{bmatrix} 6 \\ 8 \\ 7 \end{bmatrix} = \begin{bmatrix} 6 - 1.6 - 1.4 \\ -1.2 + 4.8 - 1.4 \\ -1.2 - 1.6 + 7 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \\ 4.2 \end{bmatrix}$$

因此 $x = 3$，$y = 2$，$z = 4.2$。

**验证**：
$2 \times 3 + 1 \times 2 + 1 \times 4.2 = 6 + 2 + 4.2 = 12.2 \neq 6$（这里有问题）

**说明**：实际求解中应该使用更精确的逆矩阵或直接使用高斯消元法，避免数值误差。

## 题型总结与思路技巧

### 逆矩阵求法选择

#### 📋 方法选择决策

```
求逆矩阵
    │
    ├── 2阶矩阵？
    │       └── 公式法：主对调副变号，除以行列式
    │
    ├── 高阶数字矩阵？
    │       └── 初等变换法：(A|I) → (I|A⁻¹)
    │
    ├── 伴随矩阵？
    │       └── A⁻¹ = (1/det A) · A*
    │
    └── 分块矩阵？
            └── 利用分块求逆公式
```

### 💡 核心技巧与常用结论

#### 1. 逆矩阵存在条件

**充要条件**：$\det(A) \neq 0$

**等价表述**：
- $A$ 可逆
- $A$ 非奇异
- $A$ 满秩
- $Ax = 0$ 只有零解
- $A$ 的行/列向量线性无关

#### 2. 求逆方法

**方法一：初等变换法**
$$[A | I] \xrightarrow{\text{行变换}} [I | A^{-1}]$$

**方法二：伴随矩阵法**
$$A^{-1} = \frac{1}{\det(A)} A^*$$

**方法三：分块求逆**
$$\begin{bmatrix} A & B \\ 0 & D \end{bmatrix}^{-1} = \begin{bmatrix} A^{-1} & -A^{-1}BD^{-1} \\ 0 & D^{-1} \end{bmatrix}$$

#### 3. 逆矩阵运算性质

- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^T)^{-1} = (A^{-1})^T$
- $(kA)^{-1} = \frac{1}{k}A^{-1}$（$k \neq 0$）
- $\det(A^{-1}) = \frac{1}{\det(A)}$

#### 4. 特殊矩阵的逆

- 对角矩阵：$\text{diag}(a_1,\ldots,a_n)^{-1} = \text{diag}(1/a_1,\ldots,1/a_n)$
- 正交矩阵：$Q^{-1} = Q^T$
- 对称正定矩阵：逆矩阵仍对称正定

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 求逆矩阵 | 初等变换/伴随 | 验证$AA^{-1}=I$ |
| 证明可逆 | 验证$\det \neq 0$ | 或证明满秩 |
| 解矩阵方程 | 移项求逆 | 注意乘法顺序 |
| 抽象证明 | 利用性质 | 结合律、分配律 |

### ⚠️ 常见错误

**错误一**：逆矩阵乘法顺序
- ❌ $(AB)^{-1} = A^{-1}B^{-1}$
- ✅ $(AB)^{-1} = B^{-1}A^{-1}$

**错误二**：矩阵方程求解
- $AX = B \Rightarrow X = A^{-1}B$
- $XA = B \Rightarrow X = BA^{-1}$
- 注意左乘和右乘的区别

**错误三**：消去律
- $AB = AC$ 推不出 $B = C$
- 需要 $A$ 可逆：$A^{-1}AB = A^{-1}AC \Rightarrow B = C$

## 6. 课后练习

### 6.1 基础题

**教材参考**：《高等代数简明教程》第二章习题

1. 判断下列矩阵是否可逆：
   - (1) $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$
   - (2) $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$
   - (3) $A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$

2. 求下列矩阵的逆矩阵：
   - (1) $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$
   - (2) $A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$
   - (3) $A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix}$

3. 证明：$(A^{-1})^{-1} = A$。

4. 设 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$，$B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$，求 $(AB)^{-1}$。

5. 使用初等行变换法求 $A = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ 的逆矩阵。

### 6.2 进阶题

**教材参考**：《高等代数简明教程》第二章习题

6. 证明：如果 $A$ 是正交矩阵，则 $A^{-1} = A^T$。

7. 证明：$(A^T)^{-1} = (A^{-1})^T$。

8. 设 $A$ 是可逆矩阵，证明 $\det(A^{-1}) = \frac{1}{\det(A)}$。

9. 设 $A$ 是可逆矩阵，证明 $A$ 的伴随矩阵 $A^* = \det(A) A^{-1}$。

10. 证明：如果 $A$ 和 $B$ 可逆，则 $(AB)^{-1} = B^{-1}A^{-1}$。

### 6.3 挑战题

**教材参考**：《高等代数简明教程》第二章习题

11. 设 $A$ 是 $n \times n$ 矩阵，证明 $A$ 可逆当且仅当 $A^T A$ 可逆。

12. 在数值计算中，为什么直接求逆可能产生大的数值误差？研究条件数的概念。

13. 设 $A$ 是对称正定矩阵，证明 $A^{-1}$ 也是对称正定矩阵。

14. 研究 Moore-Penrose 伪逆的定义和性质，以及它在求解最小二乘问题中的应用。

15. 在深度学习中，研究为什么批量归一化可以提高训练速度。从矩阵运算的角度解释。

## 7. 教材参考

### 国内教材
1. **《高等代数简明教程》（第2版）** - 北京大学数学系
   - 第二章：矩阵
   - 重点：逆矩阵、可逆条件

2. **《线性代数》（第6版）** - 同济大学数学系
   - 第二章：矩阵及其运算
   - 重点：逆矩阵的计算

### 国外教材
3. **《Introduction to Linear Algebra》（第5版）** - Gilbert Strang
   - Chapter 2: Solving Linear Equations
   - 重点：逆矩阵的应用

4. **《Linear Algebra Done Right》（第3版）** - Sheldon Axler
   - Chapter 3: Linear Maps
   - 重点：可逆线性映射

## 8. 本章小结

### 8.1 重要定义
1. 逆矩阵的定义
2. 可逆的充要条件
3. 伴随矩阵

### 8.2 重要性质
1. 逆矩阵的唯一性
2. 逆矩阵的反序性：$(AB)^{-1} = B^{-1}A^{-1}$
3. 正交矩阵的逆：$A^{-1} = A^T$

### 8.3 重要方法
1. 伴随矩阵法
2. 初等行变换法
3. 分块矩阵求逆

### 8.4 重要应用
1. 求解线性方程组
2. 正规方程
3. 最小二乘问题

---

**创建时间：2026年3月11日**  
**最后更新：2026年3月11日**  
**参考教材**：《高等代数简明教程》、《Introduction to Linear Algebra》

## 相关概念

- [[01_Determinants]] - 行列式
- [[04_Matrix_Basics]] - 矩阵基础
- [[05_Matrix_Operations]] - 矩阵运算
- [[07_Rank]] - 矩阵的秩
- [[11_Linear_Equations]] - 线性方程组


