---
type: note
subject: optimization
chapter: 13
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 13 - 增广拉格朗日法

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

## 1. 动机与基本思想

### 1.1 罚函数法的问题

**外点罚函数法**的困难：
- 罚参数 μ → ∞ 导致病态
- Hessian条件数随 μ 增大而增大
- 数值求解不稳定

### 1.2 增广拉格朗日函数

**定义**：结合拉格朗日函数和罚函数：
$$L_A(x, \lambda, \mu) = f(x) + \sum_{i=1}^{m} \left[ \lambda_i g_i(x) + \frac{\mu}{2} g_i(x)^2 \right] + \sum_{j=1}^{p} \left[ \nu_j h_j(x) + \frac{\mu}{2} h_j(x)^2 \right]$$

**关键思想**：
- 引入拉格朗日乘子估计
- 罚参数不必趋于无穷
- 交替更新原始变量和对偶变量

## 2. 等式约束问题

### 2.1 问题形式

$$\min f(x) \quad \text{s.t.} \quad h(x) = 0$$

### 2.2 增广拉格朗日函数

$$L_A(x, \nu, \mu) = f(x) + \nu^T h(x) + \frac{\mu}{2}\|h(x)\|^2$$

### 2.3 乘子更新

**最优性条件**：
$$\nabla_x L_A(x, \nu, \mu) = 0$$

**乘子更新公式**：
$$\nu^{k+1} = \nu^k + \mu h(x^{k+1})$$

**推导**：由KKT条件，最优乘子 ν* 满足：
$$\nabla f(x^*) + \nu^{*T} \nabla h(x^*) = 0$$

若 h(x^k) → 0，则 ν^k → ν*。

### 2.4 算法流程

```
算法：增广拉格朗日法（等式约束）
初始化：x₀, ν₀, μ₀ > 0
for k = 0, 1, 2, ...:
    # 最小化增广拉格朗日函数
    x^{k+1} = argmin_x L_A(x, ν^k, μ_k)
    
    # 更新乘子
    ν^{k+1} = ν^k + μ_k · h(x^{k+1})
    
    # 检查收敛
    if ‖h(x^{k+1})‖ < ε:
        返回 x^{k+1}, ν^{k+1}
    
    # 更新罚参数（可选）
    if ‖h(x^{k+1})‖ > 0.25‖h(x^k)‖:
        μ_{k+1} = β · μ_k  (β > 1)
```

## 3. 不等式约束问题

### 3.1 问题形式

$$\min f(x) \quad \text{s.t.} \quad g(x) \leq 0$$

### 3.2 转化为等式约束

引入松弛变量 s ≥ 0：
$$g(x) + s = 0, \quad s \geq 0$$

增广拉格朗日函数：
$$L_A(x, s, \lambda, \mu) = f(x) + \lambda^T(g(x) + s) + \frac{\mu}{2}\|g(x) + s\|^2$$

### 3.3 乘子更新

对 s 最小化得到（解析解）：
$$s_i = \max\left(0, -g_i(x) - \frac{\lambda_i}{\mu}\right)$$

代入后得到**投影梯度**形式：
$$\lambda_i^{k+1} = \max\left(0, \lambda_i^k + \mu g_i(x^{k+1})\right)$$

### 3.4 一般约束的算法

```
算法：增广拉格朗日法（一般约束）
初始化：x₀, λ₀ ≥ 0, ν₀, μ₀ > 0
for k = 0, 1, 2, ...:
    # 最小化增广拉格朗日函数
    x^{k+1} = argmin_x L_A(x, λ^k, ν^k, μ_k)
    
    # 更新乘子
    λ_i^{k+1} = max(0, λ_i^k + μ_k · g_i(x^{k+1}))  # 不等式
    ν^{k+1} = ν^k + μ_k · h(x^{k+1})  # 等式
    
    # 检查收敛
    约束违反 = max(max(0, g(x^{k+1})), ‖h(x^{k+1})‖)
    if 约束违反 < ε:
        返回 x^{k+1}
    
    # 更新罚参数
    if 约束违反 > 0.25 × 上一次违反:
        μ_{k+1} = β · μ_k
```

## 4. 收敛性分析

### 4.1 局部收敛性

**定理**：设 f, g, h 二阶连续可微，x* 是正则点且满足二阶充分条件，则存在 μ̄ > 0，当 μ > μ̄ 时，增广拉格朗日法局部线性收敛。

### 4.2 收敛速度

**与罚函数法对比**：
| 方法 | 收敛速度 | 罚参数要求 |
|------|----------|------------|
| 罚函数法 | 线性 | μ → ∞ |
| 增广拉格朗日法 | 线性 | μ 固定足够大 |

**关键优势**：μ 不必趋于无穷，避免病态。

### 4.3 全局收敛性

**条件**：
- 无约束子问题精确求解
- 满足约束规范

**结果**：聚点是KKT点。

## 5. 罚参数的选择

### 5.1 理论下界

**定理**：若强对偶成立，最优乘子为 (λ*, ν*)，则当：
$$\mu > \frac{\|\lambda^*\|}{\delta}$$

时，增广拉格朗日函数在最优解附近是凸的。

### 5.2 自适应策略

**标准策略**：
- 若约束违反减少不够快，增大 μ
- 系数通常取 β = 2 或 10
- 典型初始值 μ₀ = 1

**Powell的策略**：
$$\mu_{k+1} = \begin{cases}
\mu_k & \text{if } \|h(x^{k+1})\| \leq 0.25\|h(x^k)\| \\
\beta \mu_k & \text{otherwise}
\end{cases}$$

## 6. Python实现

```python
import numpy as np
from scipy.optimize import minimize

def augmented_lagrangian(f, g, h, x0, mu0=1, beta=10, tol=1e-8, max_iter=100):
    """
    增广拉格朗日法
    f: 目标函数
    g: 不等式约束列表, gi(x) <= 0
    h: 等式约束列表
    """
    n_ineq = len(g) if g else 0
    n_eq = len(h) if h else 0
    
    x = x0.copy()
    lam = np.zeros(n_ineq)  # 不等式乘子
    nu = np.zeros(n_eq)     # 等式乘子
    mu = mu0
    
    prev_violation = np.inf
    
    for k in range(max_iter):
        # 定义增广拉格朗日函数
        def L_A(x):
            obj = f(x)
            
            # 不等式约束
            if g:
                g_vals = np.array([gi(x) for gi in g])
                obj += lam @ g_vals + (mu/2) * np.sum(np.maximum(g_vals, -lam/mu)**2)
            
            # 等式约束
            if h:
                h_vals = np.array([hj(x) for hj in h])
                obj += nu @ h_vals + (mu/2) * np.sum(h_vals**2)
            
            return obj
        
        # 无约束优化
        result = minimize(L_A, x, method='BFGS')
        x = result.x
        
        # 计算约束违反
        g_violation = max([0] + [max(0, gi(x)) for gi in g]) if g else 0
        h_violation = max([abs(hj(x)) for hj in h]) if h else 0
        violation = max(g_violation, h_violation)
        
        # 更新乘子
        if g:
            g_vals = np.array([gi(x) for gi in g])
            lam = np.maximum(0, lam + mu * g_vals)
        if h:
            h_vals = np.array([hj(x) for hj in h])
            nu = nu + mu * h_vals
        
        # 检查收敛
        if violation < tol:
            return x, k+1, True
        
        # 更新罚参数
        if violation > 0.25 * prev_violation:
            mu *= beta
        
        prev_violation = violation
    
    return x, max_iter, False

# 示例
if __name__ == "__main__":
    # min (x1-1)^2 + (x2-2)^2, s.t. x1 + x2 = 3, x1 >= 0
    f = lambda x: (x[0]-1)**2 + (x[1]-2)**2
    g = [lambda x: -x[0]]  # -x1 <= 0 即 x1 >= 0
    h = [lambda x: x[0] + x[1] - 3]
    x0 = np.array([1.0, 1.0])
    
    x_opt, iters, converged = augmented_lagrangian(f, g, h, x0)
    print(f"最优解: {x_opt}")
    print(f"迭代次数: {iters}, 收敛: {converged}")
```

## 7. ADMM算法

### 7.1 分离结构

**问题形式**：
$$\min f(x) + g(z) \quad \text{s.t.} \quad Ax + Bz = c$$

**增广拉格朗日函数**：
$$L_A(x, z, y) = f(x) + g(z) + y^T(Ax + Bz - c) + \frac{\rho}{2}\|Ax + Bz - c\|^2$$

### 7.2 ADMM迭代

```
x^{k+1} = argmin_x L_A(x, z^k, y^k)
z^{k+1} = argmin_z L_A(x^{k+1}, z, y^k)
y^{k+1} = y^k + ρ(Ax^{k+1} + Bz^{k+1} - c)
```

### 7.3 应用场景

- 分布式优化
- 大规模机器学习
- 统计学习（LASSO, 稀疏编码）
- 信号处理

## 8. 与其他方法的关系

### 8.1 与罚函数法

| 特点 | 罚函数法 | 增广拉格朗日法 |
|------|----------|----------------|
| 乘子更新 | 无 | 有 |
| 罚参数 | μ → ∞ | μ 固定或缓慢增长 |
| 病态程度 | 严重 | 较轻 |
| 收敛速度 | 线性 | 线性（但更稳定） |

### 8.2 与SQP

- SQP求解二次逼近子问题
- 增广拉格朗日法求解无约束子问题
- 可以结合：用增广拉格朗日函数作为SQP的目标

## 9. 应用实例

### 9.1 带约束的最小二乘

```python
# min ||Ax - b||^2, s.t. ||x||_1 <= t
def constrained_l1_ls(A, b, t, x0):
    f = lambda x: np.sum((A @ x - b)**2)
    g = [lambda x: np.sum(np.abs(x)) - t]
    h = []
    return augmented_lagrangian(f, g, h, x0)
```

### 9.2 力学平衡问题

```python
# 结构力学中的约束优化
def structural_optimization(stiffness, load, constraints):
    # 增广拉格朗日法求解
    pass
```

## 10. 总结

**增广拉格朗日法的优势**：
1. 罚参数不必趋于无穷
2. 数值稳定性好
3. 可处理一般约束
4. 易于实现

**关键要素**：
- 乘子更新：核心机制
- 罚参数策略：平衡效率与稳定性
- 子问题求解：可用各种无约束方法

**应用建议**：
- 中小规模问题：直接使用
- 大规模问题：结合分解技术（ADMM）
- 需要高精度：作为SQP的子问题求解器

---

**相关链接**：
- [[11_Duality_Theory]] - 对偶理论
- [[12_Penalty_Methods]] - 罚函数法
- [[14_Sequential_Quadratic]] - 序列二次规划

