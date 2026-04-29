---
type: note
subject: optimization
chapter: 14
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 14 - 序列二次规划 (SQP)

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

## 1. 基本思想

### 1.1 牛顿法回顾

**无约束优化的牛顿法**：
$$x_{k+1} = x_k - [\nabla^2 f(x_k)]^{-1} \nabla f(x_k)$$

**解释**：求解最优性条件 ∇f(x) = 0 的牛顿迭代。

### 1.2 约束优化的最优性条件

**KKT条件**：
$$\nabla f(x) + \sum_i \lambda_i \nabla g_i(x) + \sum_j \nu_j \nabla h_j(x) = 0$$
$$g_i(x) \leq 0, \quad h_j(x) = 0$$
$$\lambda_i \geq 0, \quad \lambda_i g_i(x) = 0$$

**SQP思想**：对KKT条件应用牛顿法，得到二次规划子问题。

## 2. 二次规划子问题

### 2.1 拉格朗日函数的二次逼近

**拉格朗日函数**：
$$L(x, \lambda, \nu) = f(x) + \lambda^T g(x) + \nu^T h(x)$$

**在当前点 (x_k, λ_k, ν_k) 处的二次逼近**：
$$q_k(d) = \nabla f_k^T d + \frac{1}{2} d^T H_k d$$
$$\text{s.t.} \quad g_k + \nabla g_k^T d \leq 0$$
$$\quad\quad h_k + \nabla h_k^T d = 0$$

其中：
- d = x - x_k 为搜索方向
- H_k ≈ ∇²ₓₓL(x_k, λ_k, ν_k) 为Hessian近似

### 2.2 子问题的形式

**标准形式**：
$$\min_d \frac{1}{2} d^T H_k d + \nabla f_k^T d$$
$$\text{s.t.} \quad \nabla g_k^T d + g_k \leq 0$$
$$\quad\quad \nabla h_k^T d + h_k = 0$$

这是一个**二次规划(QP)问题**，可以高效求解。

## 3. SQP算法

### 3.1 基本算法

```
算法：SQP
初始化：x₀, λ₀, ν₀, H₀ = I
for k = 0, 1, 2, ...:
    # 求解QP子问题
    (d_k, λ_qp, ν_qp) = QP子问题的解
    
    # 线搜索确定步长
    α_k = 线搜索(x_k, d_k, λ_k, ν_k, λ_qp, ν_qp)
    
    # 更新
    x_{k+1} = x_k + α_k d_k
    λ_{k+1} = λ_k + α_k (λ_qp - λ_k)
    ν_{k+1} = ν_k + α_k (ν_qp - ν_k)
    
    # 更新Hessian近似
    H_{k+1} = BFGS更新(H_k, ...)
    
    if ‖d_k‖ < ε:
        返回 x_{k+1}
```

### 3.2 线搜索与效益函数

**问题**：QP子问题的方向不一定是下降方向

**效益函数（Merit Function）**：
$$\phi_1(x, \mu) = f(x) + \mu \sum_i \max(0, g_i(x)) + \mu \sum_j |h_j(x)|$$

**l₁效益函数的线搜索**：
$$\alpha_k = \arg\min_\alpha \phi_1(x_k + \alpha d_k, \mu_k)$$

**罚参数选择**：
$$\mu_k \geq \max\left(\lambda_{QP,i}, \frac{|\lambda_{QP,i}| + \lambda_k}{2}\right)$$

## 4. Hessian矩阵的处理

### 4.1 精确Hessian

**优点**：超线性收敛
**缺点**：
- 计算代价高
- 可能不是正定
- 需要约束二阶导数

### 4.2 BFGS拟牛顿近似

**更新公式**：
$$H_{k+1} = H_k - \frac{H_k s_k s_k^T H_k}{s_k^T H_k s_k} + \frac{y_k y_k^T}{y_k^T s_k}$$

其中：
- s_k = x_{k+1} - x_k
- y_k = ∇ₓL(x_{k+1}, λ_{k+1}) - ∇ₓL(x_k, λ_{k+1})

**正定性修正**：
若 s_k^T y_k < 0.2 s_k^T H_k s_k：
$$y_k \leftarrow \theta y_k + (1-\theta) H_k s_k$$

### 4.3 SR1近似

**更新公式**：
$$H_{k+1} = H_k + \frac{(y_k - H_k s_k)(y_k - H_k s_k)^T}{(y_k - H_k s_k)^T s_k}$$

**特点**：不保证正定，但可逼近不定Hessian。

## 5. QP子问题的求解

### 5.1 积极集法

**思想**：识别起作用约束，在积极集上求解等式约束QP。

**算法**：
1. 确定当前积极集
2. 求解等式约束QP
3. 检查乘子符号，更新积极集
4. 迭代直到收敛

### 5.2 内点法

适用于大规模QP，详见[[16_Interior_Point]]。

### 5.3 QP求解的复杂性

- 凸QP：多项式时间
- 非凸QP：NP困难（H不定时）

SQP要求子问题有解，需H正定或采用特殊处理。

## 6. 全局化策略

### 6.1 线搜索

**Armijo条件**：
$$\phi(x_k + \alpha d_k) \leq \phi(x_k) + c_1 \alpha D\phi(x_k; d_k)$$

**方向导数**：
$$D\phi_1(x_k; d_k) = \nabla f_k^T d_k - \mu_k \sum_{i \in A_k} |\lambda_{QP,i}|$$

### 6.2 信赖域方法

**子问题**：
$$\min_d \frac{1}{2} d^T H_k d + \nabla f_k^T d$$
$$\text{s.t.} \quad \nabla g_k^T d + g_k \leq 0$$
$$\quad\quad \nabla h_k^T d + h_k = 0$$
$$\quad\quad \|d\| \leq \Delta_k$$

**优点**：更稳健，可处理不定Hessian

## 7. 收敛性分析

### 7.1 局部收敛性

**定理**：若Hessian使用精确值或BFGS近似，SQP具有超线性收敛速度：
$$\|x_{k+1} - x^*\| = o(\|x_k - x^*\|)$$

### 7.2 全局收敛性

**条件**：
- 效益函数适当选择
- 罚参数足够大
- Hessian正定或使用信赖域

**结果**：聚点满足KKT条件。

## 8. Python实现

```python
import numpy as np
from scipy.optimize import minimize

def sqp_solve(f, grad_f, g, grad_g, h, grad_h, x0, max_iter=100, tol=1e-8):
    """
    简化的SQP实现
    """
    n = len(x0)
    m_ineq = len(g) if g else 0
    m_eq = len(h) if h else 0
    
    x = x0.copy()
    lam = np.zeros(m_ineq)
    nu = np.zeros(m_eq)
    H = np.eye(n)  # 初始Hessian近似
    
    for k in range(max_iter):
        # 计算梯度和约束值
        gf = grad_f(x)
        gg = np.array([grad_g[i](x) for i in range(m_ineq)]) if m_ineq > 0 else None
        gh = np.array([grad_h[i](x) for i in range(m_eq)]) if m_eq > 0 else None
        gv = np.array([g[i](x) for i in range(m_ineq)]) if m_ineq > 0 else None
        hv = np.array([h[i](x) for i in range(m_eq)]) if m_eq > 0 else None
        
        # 构造并求解QP子问题
        # min 0.5 * d'H*d + gf'd
        # s.t. gg'd + gv <= 0
        #      gh'd + hv = 0
        
        # 简化：使用scipy的约束优化
        def qp_obj(d):
            return 0.5 * d @ H @ d + gf @ d
        
        constraints = []
        if m_ineq > 0:
            for i in range(m_ineq):
                constraints.append({
                    'type': 'ineq',
                    'fun': lambda d, i=i: -gg[i] @ d - gv[i]
                })
        if m_eq > 0:
            for j in range(m_eq):
                constraints.append({
                    'type': 'eq',
                    'fun': lambda d, j=j: gh[j] @ d + hv[j]
                })
        
        result = minimize(qp_obj, np.zeros(n), constraints=constraints, method='SLSQP')
        d = result.x
        
        # 检查收敛
        if np.linalg.norm(d) < tol:
            return x, k+1, True
        
        # 线搜索（简化版）
        alpha = 1.0
        for _ in range(20):
            x_new = x + alpha * d
            if f(x_new) < f(x):
                break
            alpha *= 0.5
        
        # 更新
        s = alpha * d
        x = x + s
        
        # BFGS更新Hessian
        y = grad_f(x) - gf
        if s @ y > 0.2 * s @ H @ s:
            rho = 1.0 / (s @ y)
            H = H - rho * np.outer(H @ s, s @ H) / (s @ H @ s) + rho * np.outer(y, y)
    
    return x, max_iter, False

# 示例
if __name__ == "__main__":
    # min (x1-1)^2 + (x2-2.5)^2, s.t. x1^2 + x2^2 <= 5
    f = lambda x: (x[0]-1)**2 + (x[1]-2.5)**2
    grad_f = lambda x: np.array([2*(x[0]-1), 2*(x[1]-2.5)])
    g = [lambda x: x[0]**2 + x[1]**2 - 5]
    grad_g = [lambda x: np.array([2*x[0], 2*x[1]])]
    
    x0 = np.array([0.0, 0.0])
    x_opt, iters, converged = sqp_solve(f, grad_f, g, grad_g, [], [], x0)
    print(f"最优解: {x_opt}, 迭代: {iters}")
```

## 9. 与其他方法比较

| 方法 | 收敛速度 | 每步计算量 | 适用问题 |
|------|----------|------------|----------|
| 罚函数法 | 线性 | 低 | 一般约束 |
| 增广拉格朗日法 | 线性 | 中 | 一般约束 |
| SQP | 超线性 | 高 | 中小规模 |
| 内点法 | 多项式 | 高 | 大规模凸 |

## 10. 总结

**SQP的特点**：
- 收敛速度快（超线性）
- 每步求解一个QP子问题
- 需要处理Hessian矩阵
- 对大规模问题计算量大

**适用场景**：
- 中小规模非线性约束优化
- 对精度要求高
- 可以利用问题的稀疏结构

**发展趋势**：
- 与内点法结合
- 矩阵分解技术
- 并行计算

---

**相关链接**：
- [[07_Newton_Method]] - 牛顿法
- [[13_Augmented_Lagrangian]] - 增广拉格朗日法
- [[15_Simplex_Method]] - 单纯形法
- [[16_Interior_Point]] - 内点法

