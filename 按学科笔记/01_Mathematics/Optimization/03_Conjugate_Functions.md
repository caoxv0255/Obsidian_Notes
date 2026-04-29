---
type: note
subject: optimization
chapter: 03
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 03 - 共轭函数

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

## 1. 共轭函数的定义

### 1.1 基本定义

**定义**：函数 f : ℝⁿ → ℝ 的**共轭函数**（或Fenchel共轭）定义为：
$$f^*(y) = \sup_{x \in \text{dom} f} (y^T x - f(x))$$

**几何解释**：
- yᵀx 是过原点的超平面
- f*(y) 是 f 与超平面之间的最大垂直距离
- 对每个 y，找使 yᵀx - f(x) 最大的 x

### 1.2 基本性质

**定理**：共轭函数 f* 具有以下性质：

1. **凸性**：f* 是凸函数（即使 f 不是凸的）

2. **下界**：对所有 x, y：
   $$f(x) + f^*(y) \geq x^T y$$

   这是 **Fenchel不等式**。

3. **闭包**：f* 是闭函数（下水平集是闭集）

## 2. 共轭函数的计算

### 2.1 基本例子

**例1**：f(x) = ax + b
$$f^*(y) = \sup_x (yx - ax - b) = \begin{cases} -b, & y = a \\ +\infty, & y \neq a \end{cases}$$

**例2**：f(x) = (1/2)xᵀQx，Q ≻ 0
$$f^*(y) = \sup_x (y^T x - \frac{1}{2}x^T Q x)$$

在 x = Q⁻¹y 处取得最大值：
$$f^*(y) = \frac{1}{2} y^T Q^{-1} y$$

**例3**：f(x) = ‖x‖₁
$$f^*(y) = \sup_x (y^T x - \|x\|_1)$$

若 ‖y‖∞ > 1，取 x 沿 y 的最大分量方向趋向无穷，f*(y) = +∞。

若 ‖y‖∞ ≤ 1，由 Hölder 不等式：
$$y^T x - \|x\|_1 \leq \|y\|_\infty \|x\|_1 - \|x\|_1 \leq 0$$

当 x = 0 时取等号，故 f*(y) = 0。

$$f^*(y) = \begin{cases} 0, & \|y\|_\infty \leq 1 \\ +\infty, & \text{其他} \end{cases}$$

**例4**：f(x) = eˣ
$$f^*(y) = \sup_x (yx - e^x)$$

由一阶条件：y - e^x = 0 ⟹ x = ln y（y > 0）

$$f^*(y) = \begin{cases} y \ln y - y, & y > 0 \\ 0, & y = 0 \\ +\infty, & y < 0 \end{cases}$$

### 2.2 指示函数的共轭

**定义**：集合 C 的指示函数：
$$\delta_C(x) = \begin{cases} 0, & x \in C \\ +\infty, & x \notin C \end{cases}$$

**共轭函数**：
$$\delta_C^*(y) = \sup_{x \in C} y^T x$$

这是集合 C 的**支撑函数**。

**例**：C = {x : Ax = b}
$$\delta_C^*(y) = \begin{cases} b^T \nu, & y = A^T \nu \\ +\infty, & \text{其他} \end{cases}$$

### 2.3 对数障碍的共轭

**例**：f(x) = -Σln xᵢ, x > 0
$$f^*(y) = \sup_{x>0} (y^T x + \sum_i \ln x_i)$$

一阶条件：yᵢ + 1/xᵢ = 0 ⟹ xᵢ = -1/yᵢ（要求 yᵢ < 0）

$$f^*(y) = \begin{cases} -n - \sum_i \ln(-y_i), & y \prec 0 \\ +\infty, & \text{其他} \end{cases}$$

## 3. Fenchel不等式

### 3.1 不等式陈述

**定理**（Fenchel不等式）：对所有 x, y：
$$f(x) + f^*(y) \geq x^T y$$

**证明**：由共轭函数定义：
$$f^*(y) = \sup_x (y^T x - f(x)) \geq y^T x - f(x)$$

移项得 f(x) + f*(y) ≥ xᵀy。

### 3.2 等号成立的条件

**定理**：f(x) + f*(y) = xᵀy ⟺ y ∈ ∂f(x)

其中 ∂f(x) 是 f 在 x 处的**次梯度集合**。

**特殊情况**：若 f 可微，则：
$$f(x) + f^*(y) = x^T y \iff y = \nabla f(x)$$

### 3.3 Young不等式

**特例**：f(x) = xᵖ/p (p > 1)，则 f*(y) = y^q/q，其中 1/p + 1/q = 1。

**Young不等式**：
$$\frac{x^p}{p} + \frac{y^q}{q} \geq xy$$

等号成立 ⟺ x^{p-1} = y。

## 4. 二次共轭

### 4.1 定义

**定义**：f 的二次共轭：
$$f^{**}(x) = (f^*)^*(x) = \sup_y (x^T y - f^*(y))$$

### 4.2 性质

**定理**：
1. f**(x) ≤ f(x)（对所有 x）
2. 若 f 是闭凸函数，则 f** = f

**意义**：闭凸函数可由其共轭函数完全刻画。

### 4.3 例子

**例**：f(x) = eˣ（非凸）
- f*(y) = y ln y - y (y > 0)
- f**(x) = eˣ

虽然 f 非凸，但 f** 是 f 的**凸包**。

## 5. 共轭函数的运算

### 5.1 缩放与平移

**定理**：设 g(x) = af(x) + b，则：
$$g^*(y) = a f^*\left(\frac{y}{a}\right) - b$$

### 5.2 仿射变换

**定理**：设 g(x) = f(Ax + b)，则：
$$g^*(y) = f^*(A^{-T}y) - b^T A^{-T} y$$

### 5.3 共轭的和

**定理**：设 h(x) = f(x) + g(x)，则：
$$h^*(y) = (f^* \square g^*)(y)$$

其中 □ 是 **infimal卷积**：
$$(f \square g)(y) = \inf_z (f(z) + g(y-z))$$

### 5.4 与变量的和

**定理**：设 h(x₁, x₂) = f₁(x₁) + f₂(x₂)，则：
$$h^*(y_1, y_2) = f_1^*(y_1) + f_2^*(y_2)$$

## 6. Lagrange对偶

### 6.1 原问题

$$\min_x f(x)$$
$$\text{s.t.} \quad g_i(x) \leq 0, \quad h_j(x) = 0$$

### 6.2 Lagrange函数

$$L(x, \lambda, \nu) = f(x) + \sum_{i=1}^{m} \lambda_i g_i(x) + \sum_{j=1}^{p} \nu_j h_j(x)$$

### 6.3 对偶函数

$$g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$$

**用共轭函数表示**：
$$g(\lambda, \nu) = -f^*(-\lambda, -\nu)$$

（在适当条件下）

## 7. 应用实例

### 7.1 支持向量机

**原问题**：
$$\min_w \frac{1}{2}\|w\|^2$$
$$\text{s.t.} \quad y_i(w^T x_i + b) \geq 1$$

**对偶问题**：
$$\max_\alpha \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j$$
$$\text{s.t.} \quad \alpha_i \geq 0, \quad \sum_i \alpha_i y_i = 0$$

### 7.2 稀疏优化

**问题**：min ‖x‖₁ s.t. Ax = b

**利用共轭**：
$$\|x\|_1 = \sup_{\|y\|_\infty \leq 1} y^T x$$

对偶问题：
$$\max_y b^T y \quad \text{s.t.} \quad \|A^T y\|_\infty \leq 1$$

### 7.3 图像去噪

**ROF模型**：
$$\min_u \|u - f\|^2 + \lambda \text{TV}(u)$$

对偶方法可有效求解。

## 8. 小结

### 8.1 核心概念

| 概念 | 定义 | 性质 |
|------|------|------|
| 共轭函数 | f*(y) = sup(yᵀx - f(x)) | 凸、闭 |
| Fenchel不等式 | f(x) + f*(y) ≥ xᵀy | 恒成立 |
| 二次共轭 | f**(x) | f** ≤ f，凸时相等 |

### 8.2 重要定理

1. **凸性**：f* 总是凸函数
2. **二次共轭**：f 是闭凸 ⟺ f** = f
3. **Fenchel对偶**：对偶问题的框架

### 8.3 应用

- Lagrange对偶
- 凸优化算法
- 机器学习模型

---

**参考文献**：
1. 《Convex Optimization》- Boyd & Vandenberghe
2. 《Convex Analysis》- Rockafellar
3. 《凸分析》- 史树中

**下一章**：[[04_Convex_Optimization_Basics]] - 凸优化基础

