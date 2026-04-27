---
type: concept
topic: determinant_applications
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[01_Determinants]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 02
---

# 行列式的应用 (Applications of Determinants)

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

## 1. 克莱姆法则

### 1.1 定理

对于 $n$ 元线性方程组 $A\mathbf{x} = \mathbf{b}$，如果 $\det(A) \neq 0$，则方程组有唯一解：
$$x_j = \frac{\det(A_j)}{\det(A)}$$

其中 $A_j$ 是将 $A$ 的第 $j$ 列替换为 $\mathbf{b}$ 得到的矩阵。

### 1.2 证明思路

1. 利用行列式的展开性质
2. 使用行列式的列运算性质
3. 唯一性证明：假设有两个解，相减得到矛盾

### 1.3 优缺点

**优点**：
- 理论意义重大
- 适合低阶方程组

**缺点**：
- 计算量大（需要计算 $n+1$ 个 $n$ 阶行列式）
- 数值稳定性差

## 2. 几何意义

### 2.1 二维行列式

行列式表示平行四边形的**有向面积**：

$$\text{Area} = |\det\begin{bmatrix} \mathbf{v}_1 & \mathbf{v}_2 \end{bmatrix}| = |v_{11}v_{22} - v_{12}v_{21}|$$

其中 $\mathbf{v}_1 = [v_{11}, v_{21}]^T$ 和 $\mathbf{v}_2 = [v_{12}, v_{22}]^T$ 是平行四边形的两条邻边。

### 2.2 三维行列式

行列式表示平行六面体的**有向体积**：

$$\text{Volume} = |\det\begin{bmatrix} \mathbf{v}_1 & \mathbf{v}_2 & \mathbf{v}_3 \end{bmatrix}|$$

### 2.3 n 维行列式

行列式表示 n 维平行体的**有向体积**（n 维超体积）。

### 2.4 定向的概念

- $\det(A) > 0$：保持定向（右手坐标系）
- $\det(A) < 0$：改变定向（左手坐标系）
- $\det(A) = 0$：降维（平行体体积为零）

## 3. 代数余子式与伴随矩阵

### 3.1 代数余子式

$$A_{ij} = (-1)^{i+j} M_{ij}$$

其中 $M_{ij}$ 是余子式。

### 3.2 伴随矩阵

$$A^* = (A_{ji})$$

即 $(i,j)$ 位置的元素是 $A_{ji}$。

### 3.3 逆矩阵公式

$$A^{-1} = \frac{1}{\det(A)} A^*$$

**条件**：$\det(A) \neq 0$

## 4. 代码示例

### 4.1 克莱姆法则实现

```python
import numpy as np

def cramer_rule(A, b):
    """
    使用克莱姆法则求解线性方程组 Ax = b
    
    参数:
        A: 系数矩阵 (n×n)
        b: 常数向量 (n)
    
    返回:
        x: 解向量 (n)
    """
    det_A = np.linalg.det(A)
    
    if abs(det_A) < 1e-10:
        raise ValueError("行列式为零，无法使用克莱姆法则")
    
    n = A.shape[0]
    x = np.zeros(n)
    
    for j in range(n):
        # 构造 A_j：将第 j 列替换为 b
        A_j = A.copy()
        A_j[:, j] = b
        x[j] = np.linalg.det(A_j) / det_A
    
    return x

# 示例
A = np.array([[2, 1], [1, 3]])
b = np.array([3, 4])
x = cramer_rule(A, b)
print(f"解: {x}")
print(f"验证: A @ x = {A @ x}")

# 对比 NumPy 的解
x_numpy = np.linalg.solve(A, b)
print(f"NumPy 解: {x_numpy}")
```

### 4.2 几何意义演示

```python
import numpy as np
import matplotlib.pyplot as plt

# 定义两个向量
v1 = np.array([3, 1])
v2 = np.array([1, 2])

# 计算行列式
det_val = np.linalg.det(np.column_stack([v1, v2]))
area = abs(det_val)

print(f"向量 v1: {v1}")
print(f"向量 v2: {v2}")
print(f"行列式: {det_val:.6f}")
print(f"平行四边形面积: {area:.6f}")

# 可视化
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2')
plt.quiver(v2[0], v2[1], v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', linestyle='--')
plt.quiver(v1[0], v1[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', linestyle='--')
plt.plot([0, v1[0], v1[0]+v2[0], v2[0], 0], [0, v1[1], v1[1]+v2[1], v2[1], 0], 'k-')
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid()
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.legend()
plt.title(f'平行四边形面积 = {area:.2f}')
plt.show()
```

## 5. 例题

### 例题 1：克莱姆法则求解方程组

**问题**：使用克莱姆法则求解
$$\begin{cases}
2x + y = 3 \\\\
x + 3y = 4
\end{cases}$$

**解**：
$$A = \begin{bmatrix} 2 & 1 \\\\ 1 & 3 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 3 \\\\ 4 \end{bmatrix}$$

计算行列式：
$$\det(A) = 2 \times 3 - 1 \times 1 = 5$$

构造 $A_1$ 和 $A_2$：
$$A_1 = \begin{bmatrix} 3 & 1 \\\\ 4 & 3 \end{bmatrix}, \quad A_2 = \begin{bmatrix} 2 & 3 \\\\ 1 & 4 \end{bmatrix}$$

$$\det(A_1) = 3 \times 3 - 1 \times 4 = 5$$
$$\det(A_2) = 2 \times 4 - 3 \times 1 = 5$$

因此：
$$x = \frac{\det(A_1)}{\det(A)} = \frac{5}{5} = 1$$
$$y = \frac{\det(A_2)}{\det(A)} = \frac{5}{5} = 1$$

验证：$2 \times 1 + 1 = 3$，$1 + 3 \times 1 = 4$ ✓

### 例题 2：计算平行四边形面积

**问题**：求由向量 $\mathbf{v}_1 = [3, 1]^T$ 和 $\mathbf{v}_2 = [1, 2]^T$ 构成的平行四边形面积。

**解**：
$$\text{Area} = \left|\det\begin{bmatrix} 3 & 1 \\\\ 1 & 2 \end{bmatrix}\right| = |3 \times 2 - 1 \times 1| = |6 - 1| = 5$$

### 例题 3：使用伴随矩阵求逆

**问题**：求 $A = \begin{bmatrix} 2 & 1 \\\\ 1 & 3 \end{bmatrix}$ 的逆矩阵。

**解**：
$$\det(A) = 2 \times 3 - 1 \times 1 = 5$$

计算代数余子式：
$$A_{11} = (-1)^{1+1} \times 3 = 3$$
$$A_{12} = (-1)^{1+2} \times 1 = -1$$
$$A_{21} = (-1)^{2+1} \times 1 = -1$$
$$A_{22} = (-1)^{2+2} \times 2 = 2$$

伴随矩阵：
$$A^* = \begin{bmatrix} A_{11} & A_{21} \\\\ A_{12} & A_{22} \end{bmatrix} = \begin{bmatrix} 3 & -1 \\\\ -1 & 2 \end{bmatrix}$$

逆矩阵：
$$A^{-1} = \frac{1}{5} \begin{bmatrix} 3 & -1 \\\\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 0.6 & -0.2 \\\\ -0.2 & 0.4 \end{bmatrix}$$

验证：
$$A A^{-1} = \begin{bmatrix} 2 & 1 \\\\ 1 & 3 \end{bmatrix} \begin{bmatrix} 0.6 & -0.2 \\\\ -0.2 & 0.4 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix} = I$$ ✓

### 例题 4：判定线性相关性

**问题**：判断向量组 $\mathbf{v}_1 = [1, 2, 3]^T$，$\mathbf{v}_2 = [4, 5, 6]^T$，$\mathbf{v}_3 = [7, 8, 9]^T$ 是否线性相关。

**解**：构造矩阵并计算行列式
$$\det\begin{bmatrix} 1 & 4 & 7 \\\\ 2 & 5 & 8 \\\\ 3 & 6 & 9 \end{bmatrix} = 0$$

由于行列式为零，向量组线性相关。

**说明**：实际上 $\mathbf{v}_3 = 2\mathbf{v}_2 - \mathbf{v}_1$。

## 6. 机器学习应用

### 应用 1：概率密度变换

在正态化流（Normalizing Flows）中，需要计算变换的Jacobian行列式：

$$p_Y(\mathbf{y}) = p_X(\mathbf{x}) \left|\det\left(\frac{d\mathbf{x}}{d\mathbf{y}}\right)\right|$$

其中 $\mathbf{y} = f(\mathbf{x})$ 是可逆变换。

### 应用 2：Hessian矩阵的行列式

在优化问题中，Hessian矩阵的行列式用于判断极值性质：
- $\det(H) > 0$ 且 $H$ 正定：局部极小值
- $\det(H) < 0$：鞍点
- $\det(H) = 0$：无法判断

### 应用 3：特征值判别

特征值是特征方程 $\det(A - \lambda I) = 0$ 的根，这在PCA、PageRank等算法中至关重要。

## 题型总结与思路技巧

### 行列式应用的核心场景

#### 📋 应用类型识别

| 应用场景       | 判别条件                    | 结论   |
| ---------- | ----------------------- | ---- |
| **矩阵可逆性**  | $\det(A) \neq 0$        | 可逆   |
| **方程组解**   | $\det(A) \neq 0$        | 唯一解  |
| **向量线性相关** | $\det = 0$              | 线性相关 |
| **面积/体积**  | $\vert\det\vert有向面积/体积$ |      |


### 💡 核心技巧与常用结论

#### 1. 克莱姆法则应用要点

**适用条件**：
- 方程个数 = 未知数个数
- 系数行列式 $\neq 0$

**公式**：$x_i = \frac{D_i}{D}$

**注意**：克莱姆法则计算量大，实际求解多用高斯消元法。

#### 2. 伴随矩阵求逆

**公式**：$A^{-1} = \frac{1}{\det(A)} A^*$

**步骤**：
1. 计算 $\det(A)$
2. 计算所有代数余子式
3. 构造伴随矩阵（转置排列）
4. 除以行列式

**技巧**：伴随矩阵是代数余子式矩阵的转置！

#### 3. 几何应用

**面积公式**（2D）：
$$S = \frac{1}{2}|\det(\mathbf{v}_1, \mathbf{v}_2)|$$

**体积公式**（3D）：
$$V = \frac{1}{6}|\det(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3)|$$

**三角形面积**：
$$S = \frac{1}{2}\left|\det\begin{bmatrix}
x_1 & y_1 & 1 \\
x_2 & y_2 & 1 \\
x_3 & y_3 & 1
\end{bmatrix}\right|$$

#### 4. 特殊结论

- 对称矩阵的行列式 = 特征值乘积
- 正交矩阵的行列式 = ±1
- 正定矩阵的行列式 > 0
- 奇异矩阵的行列式 = 0

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 判断矩阵可逆 | 计算$\det$ | $\det \neq 0$ 则可逆 |
| 求逆矩阵 | 伴随矩阵法 | 别忘了除以$\det$ |
| 判断线性相关 | 构造矩阵求$\det$ | $\det=0$则相关 |
| 计算面积/体积 | 行列式公式 | 取绝对值 |
| 证明题 | 利用性质 | 乘法性质、转置不变 |

### ⚠️ 常见错误

**错误一**：伴随矩阵排列错误
- 伴随矩阵是代数余子式的**转置**
- 不是简单的余子式矩阵

**错误二**：克莱姆法则条件
- 要求系数行列式非零
- 只适用于方阵方程组

**错误三**：面积公式漏系数
- 三角形面积 = $\frac{1}{2}|\det|$
- 平行四边形面积 = $|\det|$

## 7. 课后练习

### 7.1 基础题

**教材参考**：《高等代数简明教程》第一章习题

1. 使用克莱姆法则求解方程组：
   $$\begin{cases}
   x + 2y = 5 \\\\
   3x + 4y = 11
   \end{cases}$$

2. 计算由向量 $\mathbf{v}_1 = [2, -1]^T$ 和 $\mathbf{v}_2 = [3, 4]^T$ 构成的平行四边形面积。

3. 使用伴随矩阵法求 $A = \begin{bmatrix} 1 & 2 \\\\ 3 & 4 \end{bmatrix}$ 的逆矩阵。

### 7.2 进阶题

**教材参考**：《高等代数简明教程》第一章习题

4. 使用克莱姆法则求解 3 元方程组：
   $$\begin{cases}
   x + y + z = 6 \\\\
   2x - y + z = 3 \\\\
   x + 2y - z = 2
   \end{cases}$$

5. 计算由向量 $\mathbf{v}_1 = [1, 0, 0]^T$，$\mathbf{v}_2 = [1, 2, 0]^T$，$\mathbf{v}_3 = [1, 2, 3]^T$ 构成的平行六面体体积。

6. 证明：如果 $A$ 是正交矩阵，则 $\det(A) = \pm 1$。

### 7.3 挑战题

**教材参考**：《高等代数简明教程》第一章习题

7. 设 $A$ 是 $n$ 阶矩阵，证明：
   $$\det(A + I) = \det(A) + \sum_{k=1}^n S_k(A)$$
   其中 $S_k(A)$ 是 $A$ 的所有 $k$ 阶主子式之和。

8. 在正态化流中，设变换 $\mathbf{y} = \mathbf{x} + \tanh(W\mathbf{x} + \mathbf{b})$，计算Jacobian行列式并讨论其性质。

9. 证明：对于任何方阵 $A$，存在可逆矩阵 $P$ 使得 $P^{-1}AP$ 是上三角矩阵，且其对角线元素是 $A$ 的特征值（Schur分解）。

## 8. 教材参考

### 国内教材
1. **《高等代数简明教程》（第2版）** - 北京大学数学系
   - 第一章：行列式
   - 重点：克莱姆法则、几何意义

2. **《线性代数》（第6版）** - 同济大学数学系
   - 第一章：行列式
   - 重点：逆矩阵计算、几何应用

### 国外教材
3. **《Introduction to Linear Algebra》（第5版）** - Gilbert Strang
   - Chapter 4: Determinants
   - 重点：几何解释、应用案例

4. **《Linear Algebra Done Right》（第3版）** - Sheldon Axler
   - Chapter 10: Trace and Determinant
   - 重点：理论深度、特征值关系

## 9. 本章小结

### 9.1 重要应用
1. 克莱姆法则：求解线性方程组
2. 几何意义：面积、体积计算
3. 逆矩阵：伴随矩阵法求逆

### 9.2 重要公式
1. 克莱姆法则：$x_j = \frac{\det(A_j)}{\det(A)}$
2. 逆矩阵：$A^{-1} = \frac{1}{\det(A)} A^*$
3. 面积/体积：$|\det(V)|$，其中 $V$ 的列是邻边向量

### 9.3 机器学习应用
1. 概率密度变换：正态化流
2. 优化理论：Hessian矩阵分析
3. 特征值计算：特征方程求解

---

**创建时间：2026年3月11日**  
**最后更新：2026年3月11日**  
**参考教材**：《高等代数简明教程》、《Introduction to Linear Algebra》

## 相关概念

- [[01_Determinants]] - 行列式
- [[03_Determinant_Computation]] - 行列式的计算技巧
- [[06_Inverse_Matrix]] - 逆矩阵
- [[11_Linear_Equations]] - 线性方程组


