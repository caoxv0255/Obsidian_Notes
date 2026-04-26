---
type: concept
topic: determinants
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[04_Matrix_Operations]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
---
# 行列式 (Determinants)

## 1. 行列式的定义

### 1.1 2×2 行列式

$$\det\begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$$

### 1.2 n×n 行列式（拉普拉斯展开）

$$\det(A) = \sum_{j=1}^n (-1)^{i+j} a_{ij} M_{ij}$$

其中 $M_{ij}$ 是余子式，即去掉第 $i$ 行第 $j$ 列后得到的 $(n-1) \times (n-1)$ 子矩阵的行列式。

### 1.3 性质

1. **乘法性质**：$\det(AB) = \det(A)\det(B)$
2. **转置不变**：$\det(A^T) = \det(A)$
3. **齐次性**：$\det(\lambda A) = \lambda^n \det(A)$
4. **可逆判定**：$A$ 可逆 $\iff \det(A) \neq 0$

### 1.4 排列定义

$n$ 阶行列式可以定义为：
$$\det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n a_{i,\sigma(i)}$$

其中 $S_n$ 是 $n$ 阶排列的集合，$\text{sgn}(\sigma)$ 是排列 $\sigma$ 的符号。

## 2. 计算

### 2.1 三角矩阵

**上三角矩阵**：
$$\det\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
0 & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & a_{nn}
\end{bmatrix} = \prod_{i=1}^n a_{ii}$$

**下三角矩阵**同样成立：
$$\det\begin{bmatrix}
a_{11} & 0 & \cdots & 0 \\
a_{21} & a_{22} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{bmatrix} = \prod_{i=1}^n a_{ii}$$

### 2.2 初等变换

| 初等变换 | 行列式变化 |
|---------|-----------|
| 交换两行 | 变号 |
| 某行乘以 $k$ | 乘以 $k$ |
| 行倍加 | 不变 |

### 2.3 对角矩阵

$$\det(\text{diag}(\lambda_1, \ldots, \lambda_n)) = \prod_{i=1}^n \lambda_i$$

## 3. 几何意义

行列式表示线性变换对体积的缩放因子：

- **2D**：行列式表示平行四边形的面积（有向）
- **3D**：行列式表示平行六面体的体积（有向）
- **nD**：行列式表示 n 维平行体的体积（有向）

**重要结论**：
- $\det(A) > 0$：保持定向
- $\det(A) < 0$：改变定向
- $\det(A) = 0$：降维（信息丢失）

## 4. 代码示例

```python
import numpy as np

# 2×2 行列式
A = np.array([[1, 2], [3, 4]])
print(f"det(A) = {np.linalg.det(A):.6f}")  # 输出: -2.000000

# 3×3 行列式
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"det(B) = {np.linalg.det(B):.6f}")  # 输出: 0.000000（行列式为零）

# 上三角矩阵
C = np.array([[2, 1, 3], [0, 5, 2], [0, 0, 7]])
print(f"det(C) = {np.linalg.det(C):.6f}")  # 输出: 70.000000 = 2×5×7
```

## 5. 例题

### 例题 1：计算 2×2 行列式

**问题**：计算 $D = \begin{vmatrix} 3 & -1 \\\\ 2 & 5 \end{vmatrix}$

**解**：
$$D = 3 \times 5 - (-1) \times 2 = 15 + 2 = 17$$

### 例题 2：计算 3×3 行列式（展开法）

**问题**：计算 $D = \begin{vmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 9 \end{vmatrix}$

**解**：按第一行展开
$$\begin{aligned}
D &= 1 \times \begin{vmatrix} 5 & 6 \\\\ 8 & 9 \end{vmatrix} - 2 \times \begin{vmatrix} 4 & 6 \\\\ 7 & 9 \end{vmatrix} + 3 \times \begin{vmatrix} 4 & 5 \\\\ 7 & 8 \end{vmatrix} \\\\
&= 1 \times (45 - 48) - 2 \times (36 - 42) + 3 \times (32 - 35) \\\\
&= 1 \times (-3) - 2 \times (-6) + 3 \times (-3) \\\\
&= -3 + 12 - 9 \\\\
&= 0
\end{aligned}$$

**说明**：由于行列式为零，说明矩阵不可逆，行向量线性相关。

### 例题 3：使用初等变换计算行列式

**问题**：计算 $D = \begin{vmatrix} 1 & 2 & 3 \\\\ 2 & 5 & 7 \\\\ 3 & 4 & 8 \end{vmatrix}$

**解**：使用行倍加化为上三角矩阵
$$\begin{vmatrix}
1 & 2 & 3 \\\\
2 & 5 & 7 \\\\
3 & 4 & 8
\end{vmatrix}
\overset{r_2-2r_1}{\underset{r_3-3r_1}{=}}
\begin{vmatrix}
1 & 2 & 3 \\\\
0 & 1 & 1 \\\\
0 & -2 & -1
\end{vmatrix}
\overset{r_3+2r_2}{=}
\begin{vmatrix}
1 & 2 & 3 \\\\
0 & 1 & 1 \\\\
0 & 0 & 1
\end{vmatrix}
= 1 \times 1 \times 1 = 1$$

### 例题 4：范德蒙行列式

**问题**：计算 $V_3 = \begin{vmatrix} 1 & x_1 & x_1^2 \\\\ 1 & x_2 & x_2^2 \\\\ 1 & x_3 & x_3^2 \end{vmatrix}$

**解**：使用列运算
$$\begin{aligned}
V_3 &= \begin{vmatrix}
1 & x_1 & x_1^2 \\\\
1 & x_2 & x_2^2 \\\\
1 & x_3 & x_3^2
\end{vmatrix}
\overset{c_3-x_1c_2}{\underset{c_2-x_1c_1}{=}}
\begin{vmatrix}
1 & 0 & 0 \\\\
1 & x_2-x_1 & x_2(x_2-x_1) \\\\
1 & x_3-x_1 & x_3(x_3-x_1)
\end{vmatrix} \\\\
&= (x_2-x_1)(x_3-x_1) \begin{vmatrix}
1 & 0 \\\\
1 & x_3-x_2
\end{vmatrix} \\\\
&= (x_2-x_1)(x_3-x_1)(x_3-x_2) \\\\
&= \prod_{1 \leq i < j \leq 3} (x_j - x_i)
\end{aligned}$$

**一般形式**：$V_n = \prod_{1 \leq i < j \leq n} (x_j - x_i)$

### 例题 5：证明行列式性质

**问题**：证明 $\det(AB) = \det(A)\det(B)$

**证明**：

**方法一：初等矩阵分解法**

**引理**：对于初等矩阵 $E$ 和任意矩阵 $A$，有 $\det(EA) = \det(E)\det(A)$

**证明引理**：
1. **交换两行的初等矩阵** $E_{ij}$：
   - $\det(E_{ij}) = -1$
   - $\det(E_{ij}A)$ 是交换 $A$ 的第 $i$ 行和第 $j$ 行后的行列式
   - 根据行列式性质，交换两行，行列式变号
   - 因此 $\det(E_{ij}A) = -\det(A) = \det(E_{ij})\det(A)$

2. **某行乘以 $k$ 的初等矩阵** $E_i(k)$：
   - $\det(E_i(k)) = k$
   - $\det(E_i(k)A)$ 是将 $A$ 的第 $i$ 行乘以 $k$ 后的行列式
   - 根据行列式性质，某行乘以 $k$，行列式乘以 $k$
   - 因此 $\det(E_i(k)A) = k\det(A) = \det(E_i(k))\det(A)$

3. **行倍加的初等矩阵** $E_{ij}(k)$：
   - $\det(E_{ij}(k)) = 1$
   - $\det(E_{ij}(k)A)$ 是将 $A$ 的第 $j$ 行加到第 $i$ 行后的行列式
   - 根据行列式性质，行倍加不改变行列式
   - 因此 $\det(E_{ij}(k)A) = \det(A) = \det(E_{ij}(k))\det(A)$

**定理证明**：

**情况 1：$A$ 可逆**

当 $A$ 可逆时，$A$ 可以表示为初等矩阵的乘积：
$$A = E_1 E_2 \cdots E_k$$

其中每个 $E_i$ 都是初等矩阵。

则：
$$\begin{aligned}
\det(AB) &= \det(E_1 E_2 \cdots E_k B) \\
&= \det(E_1) \det(E_2 \cdots E_k B) \quad \text{(反复应用引理)} \\
&= \det(E_1) \det(E_2) \det(E_3 \cdots E_k B) \\
&= \cdots \\
&= \det(E_1) \det(E_2) \cdots \det(E_k) \det(B)
\end{aligned}$$

另一方面：
$$\begin{aligned}
\det(A) &= \det(E_1 E_2 \cdots E_k) \\
&= \det(E_1) \det(E_2) \cdots \det(E_k)
\end{aligned}$$

因此：
$$\det(AB) = \det(A)\det(B)$$

**情况 2：$A$ 不可逆**

当 $A$ 不可逆时，$\det(A) = 0$。

由于 $A$ 不可逆，$A$ 的行向量线性相关，因此 $AB$ 的行向量也线性相关，所以 $AB$ 也不可逆。

因此：
$$\det(AB) = 0 = \det(A)\det(B)$$

**方法二：排列定义法**

使用行列式的排列定义：

$$\det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n a_{i,\sigma(i)}$$

$$\det(B) = \sum_{\tau \in S_n} \text{sgn}(\tau) \prod_{j=1}^n b_{j,\tau(j)}$$

$$\begin{aligned}
\det(A)\det(B) &= \left(\sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n a_{i,\sigma(i)}\right) \left(\sum_{\tau \in S_n} \text{sgn}(\tau) \prod_{j=1}^n b_{j,\tau(j)}\right) \\
&= \sum_{\sigma, \tau \in S_n} \text{sgn}(\sigma)\text{sgn}(\tau) \prod_{i=1}^n a_{i,\sigma(i)} b_{\sigma(i),\tau(\sigma(i))}
\end{aligned}$$

令 $\pi = \tau \circ \sigma$，则 $\tau = \pi \circ \sigma^{-1}$，且 $\text{sgn}(\tau) = \text{sgn}(\pi)\text{sgn}(\sigma)$：

$$\begin{aligned}
\det(A)\det(B) &= \sum_{\sigma, \pi \in S_n} \text{sgn}(\sigma)\text{sgn}(\pi)\text{sgn}(\sigma) \prod_{i=1}^n a_{i,\sigma(i)} b_{\sigma(i),\pi(i)} \\
&= \sum_{\sigma, \pi \in S_n} \text{sgn}(\pi) \prod_{i=1}^n a_{i,\sigma(i)} b_{\sigma(i),\pi(i)}
\end{aligned}$$

另一方面：

$$\begin{aligned}
\det(AB) &= \sum_{\pi \in S_n} \text{sgn}(\pi) \prod_{i=1}^n (AB)_{i,\pi(i)} \\
&= \sum_{\pi \in S_n} \text{sgn}(\pi) \prod_{i=1}^n \left(\sum_{j=1}^n a_{i,j} b_{j,\pi(i)}\right)
\end{aligned}$$

通过展开和重新组合各项，可以证明：

$$\det(AB) = \sum_{\pi \in S_n} \text{sgn}(\pi) \prod_{i=1}^n \sum_{j=1}^n a_{i,j} b_{j,\pi(i)} = \sum_{\sigma, \pi \in S_n} \text{sgn}(\pi) \prod_{i=1}^n a_{i,\sigma(i)} b_{\sigma(i),\pi(i)} = \det(A)\det(B)$$

**推论**：
1. $\det(A^{-1}) = \frac{1}{\det(A)}$（当 $A$ 可逆时）
2. $\det(A^k) = (\det A)^k$（$k$ 为正整数）
3. 相似矩阵的行列式相同：$\det(P^{-1}AP) = \det(A)$

## 6. 机器学习应用

### 应用 1：Jacobian行列式

在变量替换中，Jacobian行列式表示体积缩放因子：
$$\frac{d\mathbf{y}}{d\mathbf{x}} = \det\left(\frac{\partial \mathbf{y}}{\partial \mathbf{x}}\right)$$

**应用场景**：
- 概率密度变换
- 坐标变换
- 正态化流（Normalizing Flows）

### 应用 2：矩阵可逆性判断

在训练神经网络时，检查Hessian矩阵的行列式：
- $\det(H) \neq 0$：Hessian可逆，可以使用牛顿法
- $\det(H) = 0$：Hessian奇异，需要使用拟牛顿法

## 题型总结与思路技巧

### 行列式计算的五大方法

#### 📋 方法选择决策树

```
行列式计算
    │
    ├── 2阶、3阶？
    │       └── 直接展开法
    │
    ├── 上/下三角矩阵？
    │       └── 对角线元素乘积
    │
    ├── 含大量零元素？
    │       └── 按零多的行/列展开
    │
    ├── 特殊结构（如范德蒙）？
    │       └── 利用特殊公式
    │
    └── 一般矩阵？
            └── 初等变换化为三角矩阵
```

#### ✏️ 计算方法详解

**方法一：直接展开法**
- 适用：低阶行列式（2、3阶）
- 技巧：按含零多的行/列展开

**方法二：初等变换法**
- 适用：一般矩阵
- 步骤：用行倍加化为上三角，注意：
  - 交换两行：变号
  - 某行乘$k$：结果乘$k$
  - 行倍加：不变

**方法三：性质法**
- 利用行列式性质化简
- 常用：提取公因子、拆分、递推

**方法四：特殊行列式公式**
- 范德蒙行列式：$V_n = \prod_{1 \leq i < j \leq n} (x_j - x_i)$
- 对角行列式：$\prod \lambda_i$
- 对称/反对称矩阵的特殊性质

### 💡 核心技巧与常用结论

#### 1. 行列式性质速查

| 操作 | 行列式变化 |
|-----|-----------|
| 转置 $A^T$ | 不变 |
| 交换两行/列 | 变号 |
| 某行/列乘$k$ | 乘以$k$ |
| 行/列倍加 | 不变 |
| $A \to kA$ | 变为 $k^n \det(A)$ |
| $AB$ | $\det(A)\det(B)$ |
| $A^{-1}$ | $1/\det(A)$ |

#### 2. 常见特殊行列式

**对角矩阵**：$\det(\text{diag}(\lambda_1,\ldots,\lambda_n)) = \lambda_1\cdots\lambda_n$

**三角矩阵**：行列式等于对角线元素乘积

**范德蒙行列式**：
$$\begin{vmatrix}
1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\
1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n & x_n^2 & \cdots & x_n^{n-1}
\end{vmatrix} = \prod_{1 \leq i < j \leq n}(x_j - x_i)$$

**反对称矩阵**：奇数阶行列式为0

#### 3. 证明题常用技巧

**证明行列式为0**：
- 证明两行/列相同或成比例
- 证明行向量线性相关
- 奇数阶反对称矩阵

**证明行列式等式**：
- 初等变换化简
- 利用已知公式展开
- 数学归纳法

#### 4. 计算中的常见陷阱

**陷阱一**：$kA$ 的行列式
- ❌ $\det(kA) = k\det(A)$
- ✅ $\det(kA) = k^n\det(A)$

**陷阱二**：初等变换记录
- 行倍加不变号，但行交换要变号
- 多次变换要累计符号变化

**陷阱三**：展开法的选择
- 选择零元素最多的行/列展开
- 避免盲目按第一行展开

### 🎯 题型分类与对策

| 题型 | 关键技巧 | 典型方法 |
|-----|---------|---------|
| 低阶行列式计算 | 直接展开 | 按行/列展开 |
| 高阶数字行列式 | 初等变换 | 化为三角矩阵 |
| 含字母行列式 | 因式分解 | 提公因式、递推 |
| 范德蒙型 | 利用公式 | 范德蒙公式 |
| 证明行列式为0 | 性质分析 | 线性相关、反对称 |
| 证明等式 | 化简比较 | 初等变换、归纳法 |

### ⚠️ 常见错误与纠正

**错误一**：混淆行列式与矩阵
- 行列式是一个**数**
- 矩阵是一个**数表**

**错误二**：展开时忘记符号
- 代数余子式有符号 $(-1)^{i+j}$
- 记忆口诀：奇负偶正

**错误三**：行列式乘法公式滥用
- $\det(A+B) \neq \det(A) + \det(B)$（一般情况）
- 但 $\det(AB) = \det(A)\det(B)$ 成立

## 7. 课后练习

### 7.1 基础题

**教材参考**：《高等代数简明教程》第一章习题

1. 计算下列行列式：
   - (1) $\begin{vmatrix} 2 & -1 \\\\ 3 & 4 \end{vmatrix}$
   
   - (2) $\begin{vmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 10 \end{vmatrix}$
   
   - (3) $\begin{vmatrix} 1 & 1 & 1 \\\\ a & b & c \\\\ a^2 & b^2 & c^2 \end{vmatrix}$

2. 利用行列式的性质证明：
   - (1) $\det(A^T) = \det(A)$
   - (2) $\det(kA) = k^n \det(A)$（$A$ 为 $n$ 阶方阵）

3. 计算下列上三角矩阵的行列式：
   $$D = \begin{vmatrix}
   2 & 3 & 1 \\\\
   0 & 5 & 4 \\\\
   0 & 0 & 6
   \end{vmatrix}$$

### 7.2 进阶题

**教材参考**：《高等代数简明教程》第一章习题

4. 使用初等变换计算行列式：
   $$D = \begin{vmatrix}
   1 & 2 & 3 & 4 \\\\
   2 & 3 & 4 & 5 \\\\
   3 & 4 & 5 & 6 \\\\
   4 & 5 & 6 & 7
   \end{vmatrix}$$

5. 证明：如果 $A$ 是奇数阶反对称矩阵，则 $\det(A) = 0$。

6. 计算 $n$ 阶行列式：
   $$D_n = \begin{vmatrix}
   a & b & 0 & \cdots & 0 \\\\
   0 & a & b & \cdots & 0 \\\\
   \vdots & \vdots & \ddots & \ddots & \vdots \\\\
   0 & 0 & \cdots & a & b \\\\
   b & 0 & \cdots & 0 & a
   \end{vmatrix}$$

### 7.3 挑战题

**教材参考**：《高等代数简明教程》第一章习题

7. 计算 $n$ 阶行列式（循环行列式）：
   $$D_n = \begin{vmatrix}
   1 & 1 & 1 & \cdots & 1 \\\\
   1 & 2 & 3 & \cdots & n \\\\
   1 & 2^2 & 3^2 & \cdots & n^2 \\\\
   \vdots & \vdots & \vdots & \ddots & \vdots \\\\
   1 & 2^{n-1} & 3^{n-1} & \cdots & n^{n-1}
   \end{vmatrix}$$

8. 证明柯西-比内公式（Cauchy-Binet formula）：
   $$\det(AB) = \sum_{S} \det(A_S) \det(B_S)$$
   其中 $A$ 是 $m \times n$ 矩阵，$B$ 是 $n \times m$ 矩阵，$S$ 遍历所有 $m$ 元子集。

9. 在机器学习中，Jacobian行列式用于变量替换。设 $\mathbf{y} = \sigma(\mathbf{x})$，其中 $\sigma$ 是sigmoid函数，计算 $\frac{d\mathbf{y}}{d\mathbf{x}}$ 并讨论其性质。

## 8. 教材参考

### 国内教材
1. **《高等代数简明教程》（第2版）** - 北京大学数学系
   - 第一章：行列式
   - 重点：排列定义、性质、计算方法

2. **《线性代数》（第6版）** - 同济大学数学系
   - 第一章：行列式
   - 重点：克莱姆法则、几何意义

### 国外教材
3. **《Introduction to Linear Algebra》（第5版）** - Gilbert Strang
   - Chapter 4: Determinants
   - 重点：几何解释、计算技巧

4. **《Linear Algebra Done Right》（第3版）** - Sheldon Axler
   - Chapter 10: Trace and Determinant
   - 重点：现代视角、特征值关系

## 9. 本章小结

### 9.1 重要定义
1. 行列式的排列定义
2. 拉普拉斯展开
3. 初等变换对行列式的影响

### 9.2 重要性质
1. 乘法性质：$\det(AB) = \det(A)\det(B)$
2. 转置不变：$\det(A^T) = \det(A)$
3. 齐次性：$\det(\lambda A) = \lambda^n \det(A)$
4. 可逆判定：$A$ 可逆 $\iff \det(A) \neq 0$

### 9.3 重要公式
1. 三角矩阵：$\det(\text{diag}(\lambda_1, \ldots, \lambda_n)) = \prod_{i=1}^n \lambda_i$
2. 范德蒙行列式：$V_n = \prod_{1 \leq i < j \leq n} (x_j - x_i)$

### 9.4 几何意义
- 2D：平行四边形面积
- 3D：平行六面体体积
- nD：n 维平行体体积

---

**创建时间：2026年3月11日**  
**最后更新：2026年3月11日**  
**参考教材**：《高等代数简明教程》、《Introduction to Linear Algebra》

## 相关概念

- [[02_Determinant_Applications]] - 行列式的应用
- [[03_Determinant_Computation]] - 行列式的计算技巧
- [[04_Matrix_Basics]] - 矩阵基础
- [[06_Inverse_Matrix]] - 逆矩阵

