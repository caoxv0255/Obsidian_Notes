---
type: concept
topic: determinant_computation
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[01_Determinants]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 03
---

# 行列式的计算技巧 (Determinant Computation)

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

## 1. 初等变换法

### 1.1 初等变换对行列式的影响

| 初等变换 | 行列式变化 |
|---------|-----------|
| 交换两行 | 变号 |
| 行倍加 | 不变 |
| 某行乘以 $k$ | 乘以 $k$ |

### 1.2 计算步骤

1. 使用初等变换化为上三角矩阵
2. 计算对角线元素的乘积
3. 根据交换次数确定符号

### 1.3 策略

- 优先使用行倍加（行列式不变）
- 选择合适的主元以减少计算量
- 尽量使某些位置出现零

## 2. 展开法

### 2.1 按某行或某列展开

**选择原则**：
- 选择含零较多的行或列
- 选择数值较简单的行或列
- 选择能产生较多零的行或列

### 2.2 拉普拉斯展开

$$\det(A) = \sum_{j=1}^n (-1)^{i+j} a_{ij} M_{ij}$$

### 2.3 递归关系

对于某些特殊矩阵，可以建立递归关系。

## 3. 范德蒙行列式

### 3.1 定义

$$V_n = \begin{vmatrix}
1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\\\
1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\\\
\vdots & \vdots & \vdots & \ddots & \vdots \\\\
1 & x_n & x_n^2 & \cdots & x_n^{n-1}
\end{vmatrix}$$

### 3.2 结果

$$V_n = \prod_{1 \leq i < j \leq n} (x_j - x_i)$$

### 3.3 性质

- 当 $x_i \neq x_j$（$i \neq j$）时，$V_n \neq 0$
- $V_n$ 是关于 $x_1, \ldots, x_n$ 的对称函数
- $V_n$ 的次数为 $\frac{n(n-1)}{2}$

## 4. 特殊矩阵的行列式

### 4.1 三角矩阵

$$\det\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\\\
0 & a_{22} & \cdots & a_{2n} \\\\
\vdots & \vdots & \ddots & \vdots \\\\
0 & 0 & \cdots & a_{nn}
\end{bmatrix} = \prod_{i=1}^n a_{ii}$$

### 4.2 对角矩阵

$$\det(\text{diag}(\lambda_1, \ldots, \lambda_n)) = \prod_{i=1}^n \lambda_i$$

### 4.3 分块矩阵

**分块三角矩阵**：
$$\det\begin{bmatrix} A & B \\\\ 0 & D \end{bmatrix} = \det(A)\det(D)$$

**分块对角矩阵**：
$$\det\begin{bmatrix} A & 0 \\\\ 0 & D \end{bmatrix} = \det(A)\det(D)$$

### 4.4 反对称矩阵

对于 $n$ 阶反对称矩阵 $A$（$A^T = -A$）：
- 如果 $n$ 是奇数，则 $\det(A) = 0$
- 如果 $n$ 是偶数，$\det(A)$ 是某个多项式的平方

## 5. 代码示例

### 5.1 行变换法实现

```python
import numpy as np

def determinant_by_row_reduction(A):
    """
    通过行变换计算行列式
    
    参数:
        A: 方阵 (n×n)
    
    返回:
        det: 行列式值
    """
    A = A.copy().astype(float)
    n = A.shape[0]
    det = 1
    swaps = 0
    
    for i in range(n):
        # 寻找主元
        pivot_row = i
        while pivot_row < n and abs(A[pivot_row, i]) < 1e-10:
            pivot_row += 1
        
        if pivot_row == n:
            return 0  # 行列式为0
        
        # 交换行
        if pivot_row != i:
            A[[i, pivot_row]] = A[[pivot_row, i]]
            swaps += 1
            det *= -1
        
        # 主元
        pivot = A[i, i]
        det *= pivot
        
        # 消元
        for j in range(i+1, n):
            factor = A[j, i] / pivot
            A[j, i:] -= factor * A[i, i:]
    
    # 考虑交换次数
    if swaps % 2 == 1:
        det *= -1
    
    return det

# 示例
A = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 2]])
det_manual = determinant_by_row_reduction(A)
det_numpy = np.linalg.det(A)

print(f"手动计算: {det_manual:.6f}")
print(f"NumPy: {det_numpy:.6f}")
```

### 5.2 范德蒙行列式计算

```python
import numpy as np

def vandermonde_determinant(x):
    """
    计算范德蒙行列式
    
    参数:
        x: 数值列表 [x1, x2, ..., xn]
    
    返回:
        det: 范德蒙行列式值
    """
    n = len(x)
    det = 1
    
    for i in range(n):
        for j in range(i+1, n):
            det *= (x[j] - x[i])
    
    return det

# 示例
x = [1, 2, 3, 4]
det_vandermonde = vandermonde_determinant(x)
print(f"范德蒙行列式: {det_vandermonde}")

# 验证
V = np.vander(x, increasing=True)
det_numpy = np.linalg.det(V)
print(f"NumPy 计算: {det_numpy:.6f}")
```

## 6. 例题

### 例题 1：使用行变换计算行列式

**问题**：计算
$$D = \begin{vmatrix}
1 & 2 & 3 & 4 \\\\
2 & 3 & 4 & 5 \\\\
3 & 4 & 5 & 6 \\\\
4 & 5 & 6 & 7
\end{vmatrix}$$

**解**：使用行倍加
$$\begin{aligned}
D &= \begin{vmatrix}
1 & 2 & 3 & 4 \\\\
2 & 3 & 4 & 5 \\\\
3 & 4 & 5 & 6 \\\\
4 & 5 & 6 & 7
\end{vmatrix}
\overset{r_2-r_1}{\underset{r_3-r_1}{=}}
\begin{vmatrix}
1 & 2 & 3 & 4 \\\\
1 & 1 & 1 & 1 \\\\
2 & 2 & 2 & 2 \\\\
3 & 3 & 3 & 3
\end{vmatrix} \\\\
&= 0
\end{aligned}$$

**说明**：后三行成比例，行列式为零。

### 例题 2：计算范德蒙行列式

**问题**：计算
$$V_3 = \begin{vmatrix}
1 & 1 & 1 \\\\
1 & 2 & 4 \\\\
1 & 3 & 9
\end{vmatrix}$$

**解**：
$$V_3 = (2-1)(3-1)(3-2) = 1 \times 2 \times 1 = 2$$

验证：
$$\begin{vmatrix}
1 & 1 & 1 \\\\
1 & 2 & 4 \\\\
1 & 3 & 9
\end{vmatrix}
= 1 \times (18 - 12) - 1 \times (9 - 4) + 1 \times (3 - 2)
= 6 - 5 + 1
= 2$$ ✓

### 例题 3：分块矩阵行列式

**问题**：计算
$$D = \begin{vmatrix}
2 & 1 & 0 & 0 \\\\
3 & 4 & 0 & 0 \\\\
0 & 0 & 5 & 2 \\\\
0 & 0 & 1 & 3
\end{vmatrix}$$

**解**：这是分块对角矩阵
$$D = \begin{vmatrix} 2 & 1 \\\\ 3 & 4 \end{vmatrix} \times \begin{vmatrix} 5 & 2 \\\\ 1 & 3 \end{vmatrix} = (8 - 3) \times (15 - 2) = 5 \times 13 = 65$$

### 例题 4：递推关系

**问题**：计算 $n$ 阶行列式
$$D_n = \begin{vmatrix}
a & b & 0 & \cdots & 0 \\\\
c & a & b & \cdots & 0 \\\\
0 & c & a & \cdots & 0 \\\\
\vdots & \vdots & \vdots & \ddots & \vdots \\\\
0 & 0 & 0 & \cdots & a
\end{vmatrix}$$

**解**：按第一行展开
$$D_n = a D_{n-1} - bc D_{n-2}$$

这是一个二阶线性递推关系，可以求解得到：
$$D_n = \begin{cases}
\frac{\alpha^{n+1} - \beta^{n+1}}{\alpha - \beta}, & \text{如果 } \alpha \neq \beta \\\\
(n+1)\alpha^n, & \text{如果 } \alpha = \beta
\end{cases}$$

其中 $\alpha, \beta$ 是方程 $x^2 - ax + bc = 0$ 的根。

## 题型总结与思路技巧

### 行列式计算方法选择

#### 📋 方法决策树

```
行列式计算
    │
    ├── 特殊结构？
    │       ├── 范德蒙型 → 范德蒙公式
    │       ├── 三对角型 → 递推法
    │       ├── 分块型 → 分块行列式公式
    │       └── 对称/反对称 → 利用特殊性质
    │
    ├── 低阶（≤4阶）？
    │       └── 展开 + 初等变换
    │
    ├── 高阶数字行列式？
    │       └── 初等变换化三角
    │
    └── 含字母行列式？
            ├── 提公因式
            ├── 因式分解
            └── 数学归纳法
```

### 💡 核心计算技巧

#### 1. 初等变换法步骤

**目标**：化为上三角矩阵

**步骤**：
1. 选主元，消去下方元素
2. 记录变换过程中的符号变化
3. 最终结果 = 对角线乘积 × 符号累计

**注意**：
- 交换两行：变号
- 行倍加：不变
- 某行乘$k$：结果乘$k$

#### 2. 展开法技巧

**选择原则**：
- 选择零最多的行/列
- 先做初等变换增加零元素

**降阶策略**：
- 利用性质创造零元素
- 分块降阶

#### 3. 特殊行列式公式

**范德蒙行列式**：
$$V_n = \prod_{1 \leq i < j \leq n}(x_j - x_i)$$

**三对角行列式**：
递推关系 $D_n = a D_{n-1} - bc D_{n-2}$

**分块行列式**：
$$\det\begin{bmatrix} A & B \\ 0 & D \end{bmatrix} = \det(A)\det(D)$$

#### 4. 证明行列式等式的方法

- **初等变换法**：两边化简到相同形式
- **数学归纳法**：验证$n=1$，假设$n=k$成立，证明$n=k+1$
- **递推法**：建立递推关系求解

### 🎯 题型分类与对策

| 题型 | 关键方法 | 注意事项 |
|-----|---------|---------|
| 数字行列式 | 初等变换 | 记录符号变化 |
| 含字母行列式 | 因式分解 | 避免遗漏因子 |
| 三对角型 | 递推法 | 建立递推关系 |
| 范德蒙型 | 公式法 | 直接套用 |
| 分块行列式 | 分块公式 | 判断分块是否可交换 |
| 证明题 | 归纳/递推 | 检查边界条件 |

### ⚠️ 常见错误

**错误一**：忘记累计符号
- 每次交换两行都要变号
- 建议边算边记录

**错误二**：展开时余子式位置
- 代数余子式有$(-1)^{i+j}$符号
- 伴随矩阵是转置排列

**错误三**：分块行列式滥用公式
- $\det\begin{bmatrix} A & B \\ C & D \end{bmatrix} \neq \det(A)\det(D) - \det(B)\det(C)$
- 需要$C=0$或$A$与$D$可交换等条件

## 7. 课后练习

### 7.1 基础题

**教材参考**：《高等代数简明教程》第一章习题

1. 使用行变换法计算行列式：
   $$D = \begin{vmatrix}
   1 & 2 & 3 \\\\
   4 & 5 & 6 \\\\
   7 & 8 & 10
   \end{vmatrix}$$

2. 计算范德蒙行列式：
   $$V_3 = \begin{vmatrix}
   1 & 2 & 4 \\\\
   1 & 3 & 9 \\\\
   1 & 4 & 16
   \end{vmatrix}$$

3. 计算分块矩阵行列式：
   $$D = \begin{vmatrix}
   1 & 2 & 0 & 0 \\\\
   3 & 4 & 0 & 0 \\\\
   0 & 0 & 5 & 6 \\\\
   0 & 0 & 7 & 8
   \end{vmatrix}$$

### 7.2 进阶题

**教材参考**：《高等代数简明教程》第一章习题

4. 计算 $n$ 阶行列式（三对角矩阵）：
   $$D_n = \begin{vmatrix}
   2 & 1 & 0 & \cdots & 0 \\\\
   1 & 2 & 1 & \cdots & 0 \\\\
   0 & 1 & 2 & \cdots & 0 \\\\
   \vdots & \vdots & \vdots & \ddots & \vdots \\\\
   0 & 0 & 0 & \cdots & 2
   \end{vmatrix}$$

5. 计算 $n$ 阶行列式（循环矩阵）：
   $$D_n = \begin{vmatrix}
   0 & 1 & 0 & \cdots & 0 \\\\
   0 & 0 & 1 & \cdots & 0 \\\\
   \vdots & \vdots & \vdots & \ddots & \vdots \\\\
   0 & 0 & 0 & \cdots & 1 \\\\
   1 & 0 & 0 & \cdots & 0
   \end{vmatrix}$$

6. 证明：对于任何 $n$ 阶矩阵 $A$，存在上三角矩阵 $U$ 使得 $\det(A) = \det(U)$。

### 7.3 挑战题

**教材参考**：《高等代数简明教程》第一章习题

7. 计算 $n$ 阶行列式（Hankel矩阵）：
   $$D_n = \begin{vmatrix}
   1 & 2 & 3 & \cdots & n \\\\
   2 & 3 & 4 & \cdots & n+1 \\\\
   3 & 4 & 5 & \cdots & n+2 \\\\
   \vdots & \vdots & \vdots & \ddots & \vdots \\\\
   n & n+1 & n+2 & \cdots & 2n-1
   \end{vmatrix}$$

8. 设 $A$ 是 $n$ 阶矩阵，$A_{ij}$ 是代数余子式，证明：
   $$\sum_{k=1}^n a_{ik} A_{jk} = \begin{cases}
   \det(A), & i = j \\\\
   0, & i \neq j
   \end{cases}$$

9. 在数值计算中，行列式的计算可能不稳定。研究行列式计算的数值稳定性，并给出改进建议。

## 8. 教材参考

### 国内教材
1. **《高等代数简明教程》（第2版）** - 北京大学数学系
   - 第一章：行列式
   - 重点：计算技巧、特殊行列式

2. **《线性代数》（第6版）** - 同济大学数学系
   - 第一章：行列式
   - 重点：实际应用、计算方法

### 国外教材
3. **《Introduction to Linear Algebra》（第5版）** - Gilbert Strang
   - Chapter 4: Determinants
   - 重点：计算技巧、几何意义

4. **《Linear Algebra Done Right》（第3版）** - Sheldon Axler
   - Chapter 10: Trace and Determinant
   - 重点：理论分析、性质证明

## 9. 本章小结

### 9.1 计算方法
1. 初等变换法：化为上三角矩阵
2. 展开法：按行或列展开
3. 特殊矩阵：利用结构特点

### 9.2 重要公式
1. 范德蒙行列式：$V_n = \prod_{1 \leq i < j \leq n} (x_j - x_i)$
2. 分块矩阵：$\det\begin{bmatrix} A & B \\\\ 0 & D \end{bmatrix} = \det(A)\det(D)$

### 9.3 计算策略
1. 优先使用行倍加
2. 选择合适的展开位置
3. 利用矩阵的特殊结构

---

**创建时间：2026年3月11日**  
**最后更新：2026年3月11日**  
**参考教材**：《高等代数简明教程》、《Introduction to Linear Algebra》

## 相关概念

- [[01_Determinants]] - 行列式
- [[02_Determinant_Applications]] - 行列式的应用
- [[04_Matrix_Basics]] - 矩阵基础


