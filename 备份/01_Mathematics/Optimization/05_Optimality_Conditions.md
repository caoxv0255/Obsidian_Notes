---
type: note
subject: optimization
chapter: 05
created: 2026-04-03
status: complete
---

# 05 - 最优性条件

## 1. 无约束优化问题

### 1.1 问题形式

**无约束优化问题**：
$$\min_{x \in \mathbb{R}^n} f(x)$$

**目标**：
- 找到全局最优解 x*（若存在）
- 或局部最优解

### 1.2 最优解的类型

**全局最优解**：x* 满足 f(x*) ≤ f(x)，∀x

**局部最优解**：x* 满足 f(x*) ≤ f(x)，∀x ∈ B(x*, r)

**严格局部最优解**：f(x*) < f(x)，∀x ∈ B(x*, r)\{x*}

## 2. 一阶必要条件

### 2.1 梯度为零条件

**定理**（一阶必要条件）：设 f 在 x* 处可微，若 x* 是局部最优解，则：
$$\nabla f(x^*) = 0$$

**证明**：
反证法。设 ∇f(x*) ≠ 0，取方向 d = -∇f(x*)。

对充分小的 t > 0：
$$f(x^* + td) = f(x^*) + t \nabla f(x^*)^T d + o(t) = f(x^*) - t \|\nabla f(x^*)\|^2 + o(t)$$

对充分小的 t，f(x* + td) < f(x*)，矛盾。

### 2.2 稳定点

**定义**：满足 ∇f(x) = 0 的点称为**稳定点**（或驻点、临界点）。

**稳定点的类型**：
- **局部极小值点**：f 在附近最小
- **局部极大值点**：f 在附近最大
- **鞍点**：既不是极小也不是极大

### 2.3 一阶条件的局限性

**问题**：∇f(x*) = 0 不能保证 x* 是局部最优解。

**例**：f(x) = x³
- f'(0) = 0
- 但 x = 0 既不是极小也不是极大（是拐点）

## 3. 二阶条件

### 3.1 二阶必要条件

**定理**（二阶必要条件）：设 f 在 x* 处二阶可微，若 x* 是局部极小值点，则：
1. ∇f(x*) = 0
2. ∇²f(x*) ≽ 0（Hessian矩阵半正定）

**证明**：
对任意方向 d，考虑函数 φ(t) = f(x* + td)。

φ(t) 在 t = 0 处有局部极小值，故：
$$\phi'(0) = \nabla f(x^*)^T d = 0$$
$$\phi''(0) = d^T \nabla^2 f(x^*) d \geq 0$$

对所有 d 成立 ⟺ ∇²f(x*) ≽ 0。

### 3.2 二阶充分条件

**定理**（二阶充分条件）：若 x* 满足：
1. ∇f(x*) = 0
2. ∇²f(x*) ≻ 0（Hessian矩阵正定）

则 x* 是严格局部极小值点。

**证明**：
由 Taylor 展开：
$$f(x) = f(x^*) + \nabla f(x^*)^T (x-x^*) + \frac{1}{2}(x-x^*)^T \nabla^2 f(x^*) (x-x^*) + o(\|x-x^*\|^2)$$

由于 ∇f(x*) = 0 且 ∇²f(x*) ≻ 0，存在 λ > 0 使得：
$$d^T \nabla^2 f(x^*) d \geq \lambda \|d\|^2$$

因此：
$$f(x) \geq f(x^*) + \frac{\lambda}{2}\|x-x^*\|^2 + o(\|x-x^*\|^2) > f(x^*)$$

对充分小的 ‖x - x*‖ 成立。

### 3.3 二阶条件的总结

| 条件 | ∇f(x*) | ∇²f(x*) | 结论 |
|------|---------|---------|------|
| 一阶必要 | = 0 | — | 局部极小值的必要条件 |
| 二阶必要 | = 0 | ≽ 0 | 局部极小值的必要条件 |
| 二阶充分 | = 0 | ≻ 0 | 严格局部极小值 |
| 一阶必要（极大值） | = 0 | — | — |
| 二阶必要（极大值） | = 0 | ≼ 0 | 局部极大值的必要条件 |

### 3.4 鞍点判别

**鞍点**：∇f(x*) = 0，但 ∇²f(x*) 不定（既有正特征值又有负特征值）。

**判别方法**：
1. 计算 ∇²f(x*) 的特征值
2. 若有正有负，则为鞍点
3. 若全为正，可能为局部极小
4. 若全为负，可能为局部极大

## 4. 凸函数的最优性条件

### 4.1 全局最优性

**定理**：若 f 为可微凸函数，则：
$$x^* \text{ 是全局最优解} \iff \nabla f(x^*) = 0$$

**证明**：
（⟹）由一阶必要条件即得。

（⟸）由凸函数的一阶条件：
$$f(x) \geq f(x^*) + \nabla f(x^*)^T (x - x^*) = f(x^*)$$

对所有 x 成立。

### 4.2 凸函数的特殊性

**优点**：
- 局部最优 = 全局最优
- 一阶条件既必要又充分
- 不需要二阶条件

**意义**：凸优化问题的理论保证。

### 4.3 强凸函数

**定理**：若 f 为 μ-强凸函数，∇f 为 L-Lipschitz 连续，则：
1. 存在唯一全局最优解 x*
2. 从任意点 x 出发：
   $$f(x) - f(x^*) \geq \frac{\mu}{2}\|x - x^*\|^2$$

**证明**：
由强凸性：
$$f(x^*) \geq f(x) + \nabla f(x)^T (x^* - x) + \frac{\mu}{2}\|x^* - x\|^2$$

由于 ∇f(x*) = 0：
$$f(x) - f(x^*) \leq \nabla f(x)^T (x - x^*) - \frac{\mu}{2}\|x - x^*\|^2$$

由 Cauchy-Schwarz：
$$f(x) - f(x^*) \leq \|\nabla f(x)\| \cdot \|x - x^*\| - \frac{\mu}{2}\|x - x^*\|^2$$

## 5. 约束优化问题的最优性条件

### 5.1 等式约束问题

**问题**：
$$\min_x f(x)$$
$$\text{s.t.} \quad h(x) = 0$$

**一阶必要条件**（拉格朗日乘子条件）：
$$\nabla f(x^*) + \nabla h(x^*) \nu^* = 0$$
$$h(x^*) = 0$$

### 5.2 不等式约束问题

**问题**：
$$\min_x f(x)$$
$$\text{s.t.} \quad g(x) \leq 0$$

**KKT条件**：
1. ∇f(x*) + ∇g(x*)λ* = 0
2. g(x*) ≤ 0
3. λ* ≥ 0
4. λ*g(x*) = 0

详见 [[09_KKT_Conditions]]。

## 6. 下降方向

### 6.1 下降方向的定义

**定义**：方向 d 称为 f 在点 x 处的**下降方向**，若存在 ε > 0 使得：
$$f(x + td) < f(x), \quad \forall t \in (0, \varepsilon)$$

### 6.2 下降方向的判定

**定理**：若 f 在 x 处可微，则 d 是下降方向的必要条件是：
$$\nabla f(x)^T d < 0$$

**证明**：
$$f(x + td) = f(x) + t \nabla f(x)^T d + o(t)$$

当 t → 0⁺，f(x + td) < f(x) ⟺ ∇f(x)ᵀd < 0。

### 6.3 最速下降方向

**定义**：最速下降方向是使 f 下降最快的方向。

**定理**：最速下降方向为 d = -∇f(x)（或其单位化）。

**证明**：
$$\min_{\|d\|=1} \nabla f(x)^T d$$

由 Cauchy-Schwarz：
$$\nabla f(x)^T d \geq -\|\nabla f(x)\| \cdot \|d\| = -\|\nabla f(x)\|$$

等号成立 ⟺ d = -∇f(x)/‖∇f(x)‖。

## 7. 数值验证

### 7.1 验证最优性条件

```python
import numpy as np
from scipy.optimize import check_grad

# 定义函数
def f(x):
    return x[0]**2 + 2*x[1]**2 + x[0]*x[1] + x[0] - x[1]

def grad_f(x):
    return np.array([2*x[0] + x[1] + 1, 4*x[1] + x[0] - 1])

def hess_f(x):
    return np.array([[2, 1], [1, 4]])

# 求稳定点
# ∇f = 0 求解
# 2x₀ + x₁ + 1 = 0
# x₀ + 4x₁ - 1 = 0
# 解得 x* = (-5/7, 3/7)

x_star = np.array([-5/7, 3/7])

# 验证梯度为零
print(f"梯度在 x* 处: {grad_f(x_star)}")

# 验证 Hessian 正定
print(f"Hessian 在 x* 处:\n{hess_f(x_star)}")
print(f"特征值: {np.linalg.eigvals(hess_f(x_star))}")
```

### 7.2 可视化

```python
import matplotlib.pyplot as plt

# 创建网格
x1 = np.linspace(-2, 1, 100)
x2 = np.linspace(-1, 2, 100)
X1, X2 = np.meshgrid(x1, x2)
Z = X1**2 + 2*X2**2 + X1*X2 + X1 - X2

# 绘制等高线
plt.figure(figsize=(10, 8))
plt.contour(X1, X2, Z, levels=20)
plt.plot(x_star[0], x_star[1], 'r*', markersize=15)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Contour Plot')
plt.colorbar()
plt.show()
```

## 8. 小结

### 8.1 最优性条件总结

| 问题类型 | 必要条件 | 充分条件 |
|----------|----------|----------|
| 无约束一般 | ∇f = 0, ∇²f ≽ 0 | ∇f = 0, ∇²f ≻ 0 |
| 无约束凸 | ∇f = 0 | ∇f = 0（全局最优） |
| 等式约束 | ∇L = 0, h = 0 | + 二阶条件 |
| 不等式约束 | KKT条件 | 凸 + KKT（全局最优） |

### 8.2 关键概念

- **稳定点**：∇f = 0 的点
- **下降方向**：∇fᵀd < 0
- **最速下降方向**：d = -∇f
- **正定Hessian**：保证局部极小

### 8.3 应用

1. **验证解**：检查是否满足最优性条件
2. **算法设计**：基于最优性条件设计迭代算法
3. **理论分析**：证明算法收敛性

---

**参考文献**：
1. 《Numerical Optimization》- Nocedal & Wright
2. 《Convex Optimization》- Boyd & Vandenberghe
3. 《Nonlinear Programming》- Bertsekas

**下一章**：[[06_Gradient_Methods]] - 梯度下降法
