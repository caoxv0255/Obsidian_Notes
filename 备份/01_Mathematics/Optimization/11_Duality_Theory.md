---
type: note
subject: optimization
chapter: 11
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 11 - 对偶理论

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

## 1. 拉格朗日对偶

### 1.1 原问题

**标准形式**：
$$\min_x f_0(x)$$
$$\text{s.t.} \quad f_i(x) \leq 0, \quad i = 1, \ldots, m$$
$$\quad\quad\quad h_j(x) = 0, \quad j = 1, \ldots, p$$

**可行域**：
$$\mathcal{D} = \{x : f_i(x) \leq 0, h_j(x) = 0\}$$

**最优值**：p* = inf{f₀(x) : x ∈ D}

### 1.2 拉格朗日函数

**定义**：
$$L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^{m} \lambda_i f_i(x) + \sum_{j=1}^{p} \nu_j h_j(x)$$

其中：
- λ = (λ₁, ..., λₘ) ≥ 0 为不等式约束乘子
- ν = (ν₁, ..., νₚ) 为等式约束乘子

### 1.3 对偶函数

**定义**：
$$g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$$

**性质**：
1. 对偶函数是凹函数（无论原问题是否凸）
2. 定义域 dom g = {(λ, ν) : g(λ, ν) > -∞}
3. 对任意 λ ≥ 0 和任意 ν，有 g(λ, ν) ≤ p*

### 1.4 对偶问题

**形式**：
$$\max_{\lambda, \nu} g(\lambda, \nu)$$
$$\text{s.t.} \quad \lambda \geq 0$$

**最优值**：d* = sup{g(λ, ν) : λ ≥ 0}

## 2. 弱对偶性

### 2.1 弱对偶定理

**定理**：对偶问题的最优值不大于原问题的最优值：
$$d^* \leq p^*$$

**对偶间隙**：
$$p^* - d^* \geq 0$$

**证明**：
对于任意可行 x 和任意 λ ≥ 0：
$$L(x, \lambda, \nu) = f_0(x) + \sum_i \lambda_i f_i(x) + \sum_j \nu_j h_j(x) \leq f_0(x)$$

因此：
$$g(\lambda, \nu) = \inf_x L(x, \lambda, \nu) \leq f_0(x)$$

对所有可行 x 成立，故 g(λ, ν) ≤ p*。

### 2.2 弱对偶的意义

- 对偶问题提供了原问题最优值的下界
- 即使原问题不可解，对偶问题可能可解
- 对偶问题总是凸优化问题

## 3. 强对偶性

### 3.1 强对偶定理

**定理**：在适当条件下，对偶间隙为零：
$$d^* = p^*$$

### 3.2 Slater条件

**定义**：若存在 x₀ 使得：
1. x₀ ∈ int(dom f₀)
2. fᵢ(x₀) < 0，i = 1, ..., m（严格可行）
3. hⱼ(x₀) = 0，j = 1, ..., p

则称 Slater 条件成立。

**定理**：若原问题是凸问题且 Slater 条件成立，则强对偶性成立。

**弱化版本**：若 fᵢ(x₀) < 0 仅对非仿射不等式约束成立，强对偶性仍然成立。

### 3.3 其他强对偶条件

1. **线性约束凸问题**：可行域非空即可
2. **二次规划**：可行域非空
3. **一般条件**：约束规范（constraint qualification）

## 4. 对偶问题的几何解释

### 4.1 值函数

**定义**：原问题最优值作为约束上界的函数：
$$p^*(u, v) = \inf\{f_0(x) : f_i(x) \leq u_i, h_j(x) = v_j\}$$

**性质**：
- p*(0, 0) = p*
- p*(u, v) 是凸函数

### 4.2 对偶函数与值函数的关系

**定理**：对偶函数是值函数的共轭函数的下界：
$$g(\lambda, \nu) = -p^*(-\lambda, -\nu)^*$$

**几何意义**：对偶问题在值函数的epigraph外寻找最佳支撑超平面。

## 5. 对偶变量的解释

### 5.1 影子价格

**解释**：λᵢ 表示第 i 个约束放宽一个单位时，目标函数的变化率。

**数学表示**：
$$\lambda_i^* = -\frac{\partial p^*}{\partial u_i}\bigg|_{u=0}$$

### 5.2 敏感性分析

若最优对偶变量 λᵢ* 大：
- 第 i 个约束对最优值影响大
- 放宽该约束可能显著改善目标值

若 λᵢ* 接近零：
- 第 i 个约束相对不紧
- 微小放宽影响不大

## 6. 典型问题的对偶

### 6.1 线性规划的对偶

**原问题**：
$$\min c^T x \quad \text{s.t.} \quad Ax = b, x \geq 0$$

**对偶问题**：
$$\max b^T y \quad \text{s.t.} \quad A^T y \leq c$$

**对偶关系表**：

| 原问题 | 对偶问题 |
|--------|----------|
| min | max |
| 变量 x ≥ 0 | 约束 Aᵀy ≤ c |
| 约束 Ax = b | 变量 y 无约束 |
| 约束 Ax ≥ b | 变量 y ≤ 0 |

### 6.2 二次规划的对偶

**原问题**：
$$\min \frac{1}{2}x^T Q x + c^T x \quad \text{s.t.} \quad Ax \leq b$$

**对偶问题**：
$$\max -\frac{1}{2}(A^T \lambda + c)^T Q^{-1}(A^T \lambda + c) - b^T \lambda$$
$$\text{s.t.} \quad \lambda \geq 0$$

### 6.3 SVM的对偶

**原问题**：
$$\min \frac{1}{2}\|w\|^2 + C\sum_i \xi_i$$
$$\text{s.t.} \quad y_i(w^T x_i + b) \geq 1 - \xi_i, \xi_i \geq 0$$

**对偶问题**：
$$\max \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j$$
$$\text{s.t.} \quad 0 \leq \alpha_i \leq C, \sum_i \alpha_i y_i = 0$$

## 7. KKT条件与对偶

### 7.1 KKT条件的推导

**强对偶成立时**：
$$p^* = d^* = L(x^*, \lambda^*, \nu^*)$$

由于 $g(\lambda^*, \nu^*) = \inf_x L(x, \lambda^*, \nu^*)$，故 x* 使 L(x, λ*, ν*) 最小化。

**由此推出KKT条件**：

1. **原始可行性**：fᵢ(x*) ≤ 0, hⱼ(x*) = 0
2. **对偶可行性**：λ* ≥ 0
3. **稳定性条件**：∇f₀(x*) + Σλᵢ*∇fᵢ(x*) + Σνⱼ*∇hⱼ(x*) = 0
4. **互补松弛**：λᵢ*fᵢ(x*) = 0

### 7.2 KKT充分性

**定理**：若强对偶成立，且 x*, λ*, ν* 满足 KKT 条件，则 x* 是原问题最优解，λ*, ν* 是对偶问题最优解。

## 8. 对偶上升法

### 8.1 基本思想

利用对偶问题的结构，交替更新原始变量和对偶变量。

**算法**：
```
重复：
    x^{k+1} = argmin_x L(x, λ^k, ν^k)  # 原始变量更新
    λ^{k+1} = λ^k + α_k · ∇_λ g(λ^k, ν^k)  # 对偶变量更新
```

### 8.2 收敛性

**条件**：
- 强凸性：f₀ 强凸
- 约束满足Lipschitz条件

**收敛速度**：O(1/k)

## 9. 应用实例

### 9.1 资源分配问题

```python
import numpy as np
from scipy.optimize import minimize

# 原问题：min sum(x_i^2), s.t. sum(x_i) = 1, x_i >= 0
# 对偶问题：max -lambda^2/4 + lambda

def dual_objective(nu):
    # 对偶函数 g(nu) = -nu^2/4 + nu
    return -0.25 * nu**2 + nu

# 求解对偶问题
result = minimize(lambda nu: -dual_objective(nu), x0=0)
nu_star = result.x[0]

# 恢复原始解
x_star = np.maximum(nu_star / 2, 0)  # 由KKT条件
print(f"对偶最优解: ν* = {nu_star}")
print(f"原始最优值: p* = {sum(x_star**2) if len(x_star) > 0 else dual_objective(nu_star)}")
```

### 9.2 机器学习中的应用

- **SVM对偶**：核方法的关键
- **正则化**：正则化参数的对偶解释
- **分布式优化**：ADMM的理论基础

## 10. 总结

| 概念 | 说明 |
|------|------|
| 弱对偶 | d* ≤ p*，总是成立 |
| 强对偶 | d* = p*，需要条件 |
| Slater条件 | 凸问题强对偶的充分条件 |
| 对偶变量 | 影子价格，敏感性分析 |
| KKT条件 | 强对偶下的最优性条件 |

**对偶理论的价值**：
1. 提供最优值的下界
2. 简化约束处理
3. 揭示问题的经济解释
4. 为算法设计提供基础

---

**相关链接**：
- [[09_KKT_Conditions]] - KKT条件
- [[10_Linear_Programming]] - 线性规划的对偶
- [[12_Penalty_Methods]] - 罚函数法
- [[13_Augmented_Lagrangian]] - 增广拉格朗日法

