---
type: note
subject: optimization
chapter: 16
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 16 - 内点法

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

## 1. 内点法的基本思想

### 1.1 障碍函数法回顾

**问题**：线性规划的标准形式
$$\min_x c^T x$$
$$\text{s.t.} \quad Ax = b$$
$$\quad\quad\; x \geq 0$$

**对数障碍函数**：
$$\phi(x) = c^T x - \mu \sum_{i=1}^{n} \ln x_i$$

其中 μ > 0 为障碍参数。

**障碍函数法**：
- 当 μ → 0，障碍问题趋向原问题
- 但 μ 很小时，Hessian 病态
- 需要精心设计路径跟踪策略

### 1.2 内点法的核心思想

**关键观察**：
1. **中心路径**：μ 从 ∞ 递减到 0，最优解沿一条"路径"移动
2. **牛顿法**：每个障碍问题可用牛顿法高效求解
3. **多项式时间**：适当选择 μ 的更新策略，可保证多项式时间收敛

**分类**：
- **原始-对偶内点法**：最实用
- **原始内点法**：理论分析
- **对偶内点法**：某些问题更有效

## 2. 中心路径

### 2.1 原始障碍问题

**障碍问题**：
$$\min_x \phi_\mu(x) = c^T x - \mu \sum_{i=1}^{n} \ln x_i$$
$$\text{s.t.} \quad Ax = b$$

**最优性条件**：
$$c - \mu X^{-1} e + A^T y = 0$$
$$Ax = b$$
$$x > 0$$

其中 X = diag(x)，e = (1, ..., 1)ᵀ。

### 2.2 中心路径的定义

**定义**：中心路径 C 是参数 μ > 0 下最优解的轨迹：
$$\mathcal{C} = \{(x(\mu), y(\mu)) : \mu > 0\}$$

**性质**：
1. x(μ) 严格可行（x > 0）
2. 当 μ → 0，x(μ) → x*（原问题最优解）
3. 中心路径是光滑的

### 2.3 中心路径的特征

**定理**：中心路径可刻画为：
$$\min_x c^T x - \mu \sum_{i=1}^{n} \ln x_i$$
$$\text{s.t.} \quad Ax = b$$

**等价条件**：
$$c - \mu X^{-1} e + A^T y = 0$$
$$Ax = b, \quad x > 0$$

**引入松弛变量 s = c - Aᵀy**：
$$s = \mu X^{-1} e$$
$$XSe = \mu e$$

这是**互补松弛条件**的扰动形式！

### 2.4 原始-对偶中心路径

**原问题**：
$$\min_x c^T x \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**对偶问题**：
$$\max_y b^T y \quad \text{s.t.} \quad A^T y + s = c, \quad s \geq 0$$

**中心路径方程**：
$$Ax = b$$
$$A^T y + s = c$$
$$XSe = \mu e$$
$$x > 0, \quad s > 0$$

**意义**：
- 前两式：可行性
- 第三式：扰动互补松弛
- 第四式：严格可行性

## 3. 原始-对偶内点法

### 3.1 算法框架

**基本思想**：沿中心路径从 μ 较大处走向 μ → 0。

**算法**：
```
初始化 (x⁰, y⁰, s⁰) 严格可行，μ₀ > 0
for k = 0, 1, 2, ...
    // 牛顿步
    求解线性方程组得到搜索方向 (Δx, Δy, Δs)
    
    // 步长选择
    选择步长 α 使 (x^{k+1}, s^{k+1}) > 0
    
    // 更新 μ
    μ_{k+1} = (x^{k+1})^T s^{k+1} / n
    
    // 收敛判断
    if μ_{k+1} < ε:
        停止
```

### 3.2 牛顿方向

**目标**：求解扰动 KKT 系统：
$$Ax = b$$
$$A^T y + s = c$$
$$XSe = \mu e$$

**牛顿方向**：(Δx, Δy, Δs) 满足：
$$A \Delta x = 0$$
$$A^T \Delta y + \Delta s = 0$$
$$S \Delta x + X \Delta s = \mu e - XSe$$

**矩阵形式**：
$$\begin{bmatrix}
0 & A^T & I \\
A & 0 & 0 \\
S & 0 & X
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta y \\
\Delta s
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0 \\
\mu e - XSe
\end{bmatrix}$$

### 3.3 求解牛顿方程

**消元法**：
由第二式：Δs = -AᵀΔy

代入第三式：SΔx - XAᵀΔy = μe - XSe

由第一式：AΔx = 0

**简化**：
$$\Delta x = X S^{-1} (\mu e - XSe + X A^T \Delta y)$$

代入 AΔx = 0：
$$A X S^{-1} A^T \Delta y = A X S^{-1} (\mu e - XSe)$$

**求解**：
1. 分解矩阵 AXS⁻¹Aᵀ（对称正定）
2. 解线性方程组得 Δy
3. 计算 Δx, Δs

### 3.4 步长选择

**目标**：保证 x + αΔx > 0, s + αΔs > 0

**最大步长**：
$$\alpha_{\max} = \min\left\{1, \min_{\Delta x_i < 0} \frac{-x_i}{\Delta x_i}, \min_{\Delta s_i < 0} \frac{-s_i}{\Delta s_i}\right\}$$

**实际步长**：取 α = ηα_{max}，其中 η ∈ (0, 1)，通常 η = 0.99 或 0.9995。

### 3.5 参数更新策略

**μ 的更新**：
- **对偶间隙**：μ = xᵀs/n
- 更新策略：μ_{new} = σμ，其中 σ ∈ (0, 1) 为缩减因子

**预测-校正方法**：
1. **预测步**：μ = 0（仿射缩放方向）
2. **校正步**：用预测步的结果调整 μ

## 4. 收敛性分析

### 4.1 收敛性定理

**定理**：原始-对偶内点法在 O(√n log(1/ε)) 次迭代内达到精度 ε。

**证明要点**：
- 中心路径邻域的定义
- 牛顿法的二次收敛性
- μ 的缩减速度

### 4.2 多项式时间复杂度

**定理**：线性规划的原始-对偶内点法是多项式时间算法。

**复杂度**：O(n³ L)
- n：变量维数
- L：输入规模（二进制位数）

**对比**：
- 单纯形法：指数时间（最坏情况）
- 内点法：多项式时间（保证）

### 4.3 实际性能

**优点**：
- 理论保证的多项式时间
- 大规模问题表现良好
- 迭代次数通常很少（20-50 次）

**缺点**：
- 每次迭代计算量大（矩阵分解）
- 小规模问题可能不如单纯形法

## 5. 实用变体

### 5.1 Mehrotra预测-校正法

**思想**：每步同时计算预测和校正方向。

**算法**：
1. **预测方向**（仿射缩放）：
   $$(\Delta x^{aff}, \Delta y^{aff}, \Delta s^{aff})$$ at μ = 0

2. **中心参数**：
   $$\sigma = \left(\frac{\mu_{aff}}{\mu}\right)^3$$
   
   其中 μ_{aff} 是预测步后的对偶间隙。

3. **校正方向**：
   修正预测方向，添加二阶项。

**优点**：
- 超线性收敛
- 实践中非常高效
- 是商业求解器的默认方法

### 5.2 长步长方法

**思想**：使用更宽松的邻域，允许更大步长。

**邻域**：
$$\mathcal{N}_\infty(\gamma) = \{(x, s) : x > 0, s > 0, \min_i(x_i s_i) \geq \gamma \mu\}$$

**优点**：步长更大，收敛更快。

### 5.3 启动策略

**严格可行解的获取**：
1. **大M法**：添加人工变量
2. **自对偶嵌入**：构造总有问题解的问题
3. **原问题-对偶问题的均匀嵌入**

## 6. 扩展到凸优化

### 6.1 凸规划的障碍函数

**问题**：
$$\min_x f(x)$$
$$\text{s.t.} \quad g_i(x) \leq 0, \quad i = 1, \ldots, m$$
$$\quad\quad\; Ax = b$$

**对数障碍**：
$$\phi_\mu(x) = f(x) - \mu \sum_{i=1}^m \ln(-g_i(x))$$

**自一致性**：
障碍函数需满足自一致性，保证牛顿法的良好性质。

### 6.2 自和谐函数

**定义**：函数 f 是**自和谐**的，若：
$$|f'''(x)| \leq 2 f''(x)^{3/2}$$

**性质**：
- 对数障碍函数是自和谐的
- 自和谐函数的牛顿法有良好收敛性
- 内点法的理论保证

### 6.3 半定规划的内点法

**问题**：
$$\min_X \langle C, X \rangle$$
$$\text{s.t.} \quad \mathcal{A}(X) = b$$
$$\quad\quad\; X \succeq 0$$

**障碍函数**：φ(X) = -ln det(X)

**牛顿方向**：求解矩阵方程。

**复杂度**：O(√n log(1/ε)) 迭代。

## 7. 数值实验

### 7.1 Python实现

```python
import numpy as np
from scipy.optimize import linprog

# 定义线性规划问题
c = np.array([-1, -2])  # 目标函数系数
A_ub = np.array([[1, 1], [2, 1], [1, 0]])
b_ub = np.array([4, 6, 2])

# 使用内点法求解
result = linprog(c, A_ub=A_ub, b_ub=b_ub, method='interior-point')

print(f"最优解: {result.x}")
print(f"最优值: {-result.fun}")  # 取负号还原
print(f"迭代次数: {result.nit}")
```

### 7.2 大规模测试

```python
import time

# 生成大规模线性规划
np.random.seed(42)
n = 1000  # 变量数
m = 500   # 约束数

c = np.random.randn(n)
A = np.random.randn(m, n)
b = np.random.randn(m)

# 比较内点法和单纯形法
start = time.time()
result_ip = linprog(c, A_eq=A, b_eq=b, method='interior-point')
time_ip = time.time() - start

start = time.time()
result_simplex = linprog(c, A_eq=A, b_eq=b, method='simplex')
time_simplex = time.time() - start

print(f"内点法: {time_ip:.3f}秒, 迭代{result_ip.nit}次")
print(f"单纯形法: {time_simplex:.3f}秒, 迭代{result_simplex.nit}次")
```

## 8. 小结

### 8.1 核心概念

| 概念 | 定义 | 性质 |
|------|------|------|
| 中心路径 | μ 递减时最优解的轨迹 | 光滑、趋向最优解 |
| 障碍函数 | -μΣln(xᵢ) | 严格可行时有限 |
| 牛顿方向 | 线性化方程的解 | 二次收敛 |

### 8.2 算法特点

**优点**：
- 多项式时间保证
- 大规模问题高效
- 迭代次数少

**缺点**：
- 每次迭代计算量大
- 需要严格可行解
- 数值稳定性要求高

### 8.3 应用

- **线性规划**：大规模问题首选
- **半定规划**：控制、组合优化
- **二阶锥规划**：鲁棒优化
- **几何规划**：工程设计

---

**参考文献**：
1. 《Primal-Dual Interior-Point Methods》- Wright
2. 《Interior-Point Polynomial Algorithms in Convex Programming》- Nesterov & Nemirovski
3. 《Linear Programming》- Vasek Chvatal

**下一章**：[[17_Semidefinite_Programming]] - 半定规划

