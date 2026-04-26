---
type: note
subject: optimization
chapter: 07
created: 2026-04-03
status: complete
---

# 07 - 牛顿法与拟牛顿法

## 1. 牛顿法的基本原理

### 1.1 一维牛顿法

**思想**：用二次函数近似目标函数。

**迭代公式**：
$$x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$$

**推导**：在 xₖ 处 Taylor 展开：
$$f(x) \approx f(x_k) + f'(x_k)(x - x_k) + \frac{1}{2}f''(x_k)(x - x_k)^2$$

最小化近似函数，对 x 求导令其为 0。

### 1.2 多维牛顿法

**迭代公式**：
$$x_{k+1} = x_k - [\nabla^2 f(x_k)]^{-1} \nabla f(x_k)$$

**等价形式**：求解线性方程组：
$$\nabla^2 f(x_k) d_k = -\nabla f(x_k)$$
$$x_{k+1} = x_k + d_k$$

### 1.3 牛顿法的几何意义

**解释**：
- 梯度下降：用一阶近似（切平面）
- 牛顿法：用二阶近似（二次曲面）
- 牛顿方向考虑了曲率信息

## 2. 牛顿法的收敛性

### 2.1 局部收敛性

**定理**：设 f 在 x* 处二阶连续可微，∇f(x*) = 0，∇²f(x*) 正定。若初始点 x₀ 充分接近 x*，则牛顿法收敛，且：
$$\|x_{k+1} - x^*\| \leq C \|x_k - x^*\|^2$$

即**二次收敛**。

### 2.2 全局收敛性

**问题**：牛顿法可能不收敛。

**原因**：
1. Hessian 矩阵可能不定
2. 步长可能过大
3. 初始点远离最优解

### 2.3 阻尼牛顿法

**修正**：引入步长 αₖ
$$x_{k+1} = x_k - \alpha_k [\nabla^2 f(x_k)]^{-1} \nabla f(x_k)$$

**步长选择**：
- 精确线搜索
- Armijo 回溯
- Wolfe 条件

### 2.4 修正牛顿法

**问题**：Hessian 可能不正定。

**修正策略**：
1. **对角修正**：∇²f + λI，λ > 0
2. **Cholesky 分解**：B = LLᵀ + E
3. **信赖域方法**

## 3. 拟牛顿法的基本思想

### 3.1 动机

**牛顿法的问题**：
- 需要 Hessian 矩阵（计算量大）
- 需要求解线性方程组
- Hessian 可能不正定

**拟牛顿法的思路**：
- 用近似矩阵 Bₖ 代替 Hessian
- Bₖ 通过梯度信息更新
- 保证正定性

### 3.2 拟牛顿条件（割线方程）

**要求**：近似矩阵 Hₖ 应满足：
$$H_{k+1} s_k = y_k$$

其中：
- sₖ = xₖ₊₁ - xₖ（位移）
- yₖ = ∇f(xₖ₊₁) - ∇f(xₖ)（梯度差）

**意义**：保持曲率信息的一致性。

## 4. BFGS方法

### 4.1 BFGS更新公式

**Hessian 逆的更新**：
$$H_{k+1} = \left(I - \frac{s_k y_k^T}{y_k^T s_k}\right) H_k \left(I - \frac{y_k s_k^T}{y_k^T s_k}\right) + \frac{s_k s_k^T}{y_k^T s_k}$$

**等价形式**：
$$H_{k+1} = H_k - \frac{H_k y_k y_k^T H_k}{y_k^T H_k y_k} + \frac{s_k s_k^T}{y_k^T s_k}$$

### 4.2 算法步骤

```
初始化 x₀, H₀ = I
for k = 0, 1, 2, ...
    计算搜索方向: d_k = -H_k ∇f(x_k)
    线搜索求步长 α_k
    更新: x_{k+1} = x_k + α_k d_k
    
    计算位移和梯度差:
    s_k = x_{k+1} - x_k
    y_k = ∇f(x_{k+1}) - ∇f(x_k)
    
    BFGS 更新 H_{k+1}
```

### 4.3 正定性保持

**定理**：若 Hₖ 正定且 yₖᵀsₖ > 0，则 Hₖ₊₁ 正定。

**保证 yₖᵀsₖ > 0**：
- Wolfe 条件
- 曲率条件

### 4.4 收敛性

**定理**：对于凸函数，BFGS 方法超线性收敛。

## 5. DFP方法

### 5.1 DFP更新公式

**对称形式**：
$$H_{k+1} = H_k - \frac{H_k y_k y_k^T H_k}{y_k^T H_k y_k} + \frac{s_k s_k^T}{s_k^T y_k}$$

### 5.2 与BFGS的关系

**对称性**：DFP 更新 H，BFGS 更新 B = H⁻¹。

**BFGS 更优**：
- 数值稳定性更好
- 实践中表现更佳

## 6. L-BFGS方法

### 6.1 动机

**问题**：BFGS 存储 Hₖ 需要 O(n²) 空间。

**L-BFGS**：Limited-memory BFGS，只存储最近 m 对 (sₖ, yₖ)。

### 6.2 双循环递推算法

**思想**：不显式构造 Hₖ，通过递推计算 Hₖ∇f(xₖ)。

**算法**：
```
输入: {s_i, y_i}_{i=k-m}^{k-1}, ∇f(x_k), H_k^0
q = ∇f(x_k)
for i = k-1, k-2, ..., k-m
    α_i = s_i^T q / (y_i^T s_i)
    q = q - α_i y_i
r = H_k^0 q
for i = k-m, k-m+1, ..., k-1
    β_i = y_i^T r / (y_i^T s_i)
    r = r + (α_i - β_i) s_i
输出: d_k = -r
```

### 6.3 存储和计算复杂度

- **存储**：O(mn)，m 通常取 5-20
- **计算**：O(mn) 每次迭代

### 6.4 应用

**大规模优化**：
- 机器学习（深度学习）
- 自然语言处理
- 计算机视觉

## 7. 其他拟牛顿方法

### 7.1 SR1方法

**更新公式**：
$$H_{k+1} = H_k + \frac{(s_k - H_k y_k)(s_k - H_k y_k)^T}{(s_k - H_k y_k)^T y_k}$$

**特点**：
- 公式简单
- 不保证正定
- 可用于约束优化

### 7.2 Broyden族

**定义**：
$$H_\phi = (1-\phi) H_{BFGS} + \phi H_{DFP}$$

其中 φ ∈ [0, 1]。

### 7.3 比较总结

| 方法 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| 牛顿法 | 二次收敛 | 计算Hessian | 小规模问题 |
| BFGS | 超线性收敛 | O(n²)存储 | 中等规模 |
| L-BFGS | 低存储 | 收敛略慢 | 大规模问题 |

## 8. 数值实验

### 8.1 Python实现

```python
import numpy as np
from scipy.optimize import minimize

# 定义 Rosenbrock 函数
def rosenbrock(x):
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

def rosenbrock_grad(x):
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    der = np.zeros_like(x)
    der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
    der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    der[-1] = 200*(x[-1]-x[-2]**2)
    return der

# 初始点
x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])

# 使用 BFGS
result_bfgs = minimize(rosenbrock, x0, method='BFGS', 
                       jac=rosenbrock_grad, options={'disp': True})

# 使用 L-BFGS-B
result_lbfgs = minimize(rosenbrock, x0, method='L-BFGS-B',
                        jac=rosenbrock_grad, options={'disp': True})
```

## 9. 小结

### 9.1 核心方法

| 方法 | 更新方式 | 收敛速度 | 存储需求 |
|------|----------|----------|----------|
| 牛顿法 | Hessian逆 | 二次 | O(n²) |
| BFGS | 秩-2更新 | 超线性 | O(n²) |
| L-BFGS | 有限记忆 | 超线性 | O(mn) |

### 9.2 选择指南

- **小规模**：牛顿法或BFGS
- **中规模**：BFGS
- **大规模**：L-BFGS

---

**参考文献**：
1. 《Numerical Optimization》- Nocedal & Wright
2. 《Convex Optimization》- Boyd & Vandenberghe

**下一章**：[[08_Conjugate_Gradient]] - 共轭梯度法
