---
type: note
subject: optimization
chapter: 12
created: 2026-04-03
status: complete
---

# 12 - 罚函数法

## 1. 罚函数法的基本思想

### 1.1 约束优化的困难

**约束优化问题**：
$$\min f(x) \quad \text{s.t.} \quad g_i(x) \leq 0, h_j(x) = 0$$

**困难**：
- 约束使可行域复杂
- 需要专门处理边界条件
- KKT条件求解复杂

### 1.2 罚函数思想

**核心思想**：将约束违反程度加到目标函数中，转化为无约束问题。

**好处**：
- 可使用无约束优化方法
- 算法实现简单
- 适用范围广

## 2. 外点罚函数法

### 2.1 二次罚函数

**定义**：对于约束优化问题，构造罚函数：
$$P(x, \mu) = f(x) + \mu \left( \sum_{i=1}^{m} [\max(0, g_i(x))]^2 + \sum_{j=1}^{p} h_j(x)^2 \right)$$

其中 μ > 0 为罚参数。

**性质**：
- 若约束被违反，罚项为正
- 约束违反越大，罚项越大
- μ → ∞ 时，解趋近于可行解

### 2.2 算法流程

```
算法：外点罚函数法
初始化：x₀, μ₀ > 0, 增长因子 β > 1, 容差 ε
for k = 0, 1, 2, ...:
    x_k = argmin_x P(x, μ_k)  # 无约束优化
    if 约束违反程度 < ε:
        返回 x_k
    μ_{k+1} = β · μ_k
```

### 2.3 收敛性

**定理**：设 {μ_k} → ∞，{x_k} 为罚函数子问题的解序列，则：
- 若原问题有解，{x_k} 的聚点是原问题的解
- 若强对偶成立，目标函数值和罚函数值趋于原问题最优值

**收敛速度**：线性收敛

### 2.4 罚参数的选择

**问题**：μ 太大导致病态

**Hessian矩阵的条件数**：
$$\kappa(\nabla^2 P) = O(\mu)$$

μ 大时条件数大，数值求解困难。

**策略**：
- 从较小的 μ₀ 开始，逐步增大
- 使用前期迭代结果作为后续热启动
- 结合其他方法（如SQP）

## 3. 障碍函数法（内点法）

### 3.1 障碍函数

**定义**：对于不等式约束 gᵢ(x) ≤ 0，构造障碍函数：
$$B(x, \mu) = f(x) - \mu \sum_{i=1}^{m} \ln(-g_i(x))$$

或
$$B(x, \mu) = f(x) + \mu \sum_{i=1}^{m} \frac{1}{-g_i(x)}$$

**特点**：
- 只适用于不等式约束
- 迭代点始终在可行域内部
- 当 x 接近边界时，障碍项趋向无穷

### 3.2 算法流程

```
算法：障碍函数法
初始化：可行点 x₀（在可行域内部），μ₀ > 0, 收缩因子 β ∈ (0, 1)
for k = 0, 1, 2, ...:
    x_k = argmin_x B(x, μ_k)  # 保持可行性的无约束优化
    if μ_k < ε:
        返回 x_k
    μ_{k+1} = β · μ_k
```

### 3.3 收敛性

**定理**：设 μ_k → 0，{x_k} 为障碍函数子问题的解序列，则：
- x_k 趋近于原问题的最优解
- 收敛速度：线性收敛

### 3.4 中心路径

**定义**：中心路径是 {x(μ) : μ > 0}，其中 x(μ) 是障碍问题的最优解。

**性质**：
- 中心路径是可行域内部的一条曲线
- μ → 0 时，中心路径趋近于最优解
- 沿中心路径收敛更快

## 4. 混合罚函数法

### 4.1 基本形式

结合外点法和内点法：
$$P(x, \mu) = f(x) - \mu \sum_{i=1}^{m} \ln(-g_i(x)) + \frac{1}{\mu} \sum_{j=1}^{p} h_j(x)^2$$

- 不等式约束用障碍函数（内点法）
- 等式约束用二次罚函数（外点法）

### 4.2 优点

- 可以处理等式和不等式约束
- 不需要初始可行点
- 数值稳定性较好

## 5. 精确罚函数

### 5.1 l₁精确罚函数

**定义**：
$$P_1(x, \mu) = f(x) + \mu \left( \sum_{i=1}^{m} |g_i(x)|_+ + \sum_{j=1}^{p} |h_j(x)| \right)$$

其中 |t|₊ = max(0, t)。

**精确性**：存在 μ* 使得当 μ > μ* 时，无约束问题的解就是原问题的解。

**μ* 的下界**：
$$\mu^* \geq \|\lambda^*\|_1 + \|\nu^*\|_1$$

其中 λ*, ν* 是最优对偶变量。

### 5.2 精确罚函数的优缺点

**优点**：
- 不需要 μ → ∞
- 可以直接得到精确解

**缺点**：
- 罚函数不可微，需要非光滑优化方法
- μ* 的估计困难
- 可能陷入局部极小

## 6. 罚函数法的实现

### 6.1 Python实现

```python
import numpy as np
from scipy.optimize import minimize

def penalty_method(f, g, h, x0, mu0=1, beta=10, tol=1e-6, max_iter=50):
    """
    外点罚函数法
    f: 目标函数
    g: 不等式约束列表 [g1, g2, ...], gi(x) <= 0
    h: 等式约束列表 [h1, h2, ...]
    """
    x = x0.copy()
    mu = mu0
    
    for k in range(max_iter):
        # 定义罚函数
        def penalty(x):
            obj = f(x)
            # 不等式约束惩罚
            for gi in g:
                obj += mu * max(0, gi(x))**2
            # 等式约束惩罚
            for hj in h:
                obj += mu * hj(x)**2
            return obj
        
        # 无约束优化
        result = minimize(penalty, x, method='BFGS')
        x = result.x
        
        # 检查约束违反程度
        violation = 0
        for gi in g:
            violation = max(violation, max(0, gi(x)))
        for hj in h:
            violation = max(violation, abs(hj(x)))
        
        if violation < tol:
            return x, k+1
        
        mu *= beta
    
    return x, max_iter

# 示例：min x1^2 + x2^2, s.t. x1 + x2 >= 1
f = lambda x: x[0]**2 + x[1]**2
g = [lambda x: 1 - x[0] - x[1]]  # g(x) <= 0 对应 x1+x2 >= 1
h = []
x0 = np.array([0.0, 0.0])

x_opt, iters = penalty_method(f, g, h, x0)
print(f"最优解: {x_opt}")
print(f"迭代次数: {iters}")
```

### 6.2 障碍函数法实现

```python
def barrier_method(f, g, x0, mu0=1, beta=0.2, tol=1e-8, max_iter=50):
    """
    障碍函数法（内点法）
    注意：x0 必须在可行域内部
    """
    x = x0.copy()
    mu = mu0
    
    for k in range(max_iter):
        # 定义障碍函数
        def barrier(x):
            obj = f(x)
            for gi in g:
                if gi(x) >= 0:  # 在边界外
                    return np.inf
                obj -= mu * np.log(-gi(x))
            return obj
        
        # 无约束优化
        result = minimize(barrier, x, method='BFGS')
        x = result.x
        
        # 检查收敛
        if mu < tol:
            return x, k+1
        
        mu *= beta
    
    return x, max_iter
```

## 7. 与其他方法的关系

### 7.1 与增广拉格朗日法

- 增广拉格朗日法是罚函数法的改进
- 同时更新罚参数和对偶变量
- 数值稳定性更好

### 7.2 与内点法

- 障碍函数法是原始内点法
- 现代内点法（如原始-对偶内点法）效率更高
- 适用于大规模问题

## 8. 应用实例

### 8.1 投资组合优化

```python
# min w'Σw, s.t. w'μ >= r_min, sum(w) = 1, w >= 0
import numpy as np

def portfolio_penalty(Sigma, mu, r_min, w0):
    f = lambda w: w @ Sigma @ w
    g = [lambda w: r_min - mu @ w] + [lambda w, i=i: -w[i] for i in range(len(w0))]
    h = [lambda w: np.sum(w) - 1]
    
    w_opt, _ = penalty_method(f, g, h, w0)
    return w_opt
```

### 8.2 机器学习中的应用

- **约束回归**：LASSO可视为带约束问题
- **支持向量机**：软间隔的罚函数解释
- **神经网络训练**：正则化作为罚函数

## 9. 总结

| 方法 | 适用约束 | 特点 | 缺点 |
|------|----------|------|------|
| 外点罚函数法 | 任意约束 | 简单通用 | 病态问题 |
| 障碍函数法 | 不等式约束 | 始终可行 | 需要可行初始点 |
| 精确罚函数法 | 任意约束 | 精确解 | 不可微 |
| 混合罚函数法 | 任意约束 | 综合优点 | 实现复杂 |

**关键参数**：
- 初始罚参数 μ₀
- 增长/收缩因子 β
- 收敛容差 ε

**选择建议**：
- 小规模问题：外点罚函数法
- 需要保持可行：障碍函数法
- 追求效率：增广拉格朗日法或SQP

---

**相关链接**：
- [[11_Duality_Theory]] - 对偶理论
- [[13_Augmented_Lagrangian]] - 增广拉格朗日法
- [[16_Interior_Point]] - 内点法
