---
type: note
subject: optimization
chapter: 02
created: 2026-04-03
status: complete
---

# 02 - 凸函数

## 1. 凸函数的定义

### 1.1 基本定义

**定义**：设 f : ℝⁿ → ℝ 为定义在凸集 dom f 上的函数。若对任意 x, y ∈ dom f 和任意 θ ∈ [0, 1]，有：
$$f(\theta x + (1-\theta) y) \leq \theta f(x) + (1-\theta) f(y)$$

则称 f 为**凸函数**（convex function）。

**几何意义**：函数图像上任意两点的连线在函数图像之上（"弦在弧上"）。

### 1.2 严格凸与强凸

**严格凸函数**：若不等式严格成立（θ ∈ (0, 1) 且 x ≠ y）：
$$f(\theta x + (1-\theta) y) < \theta f(x) + (1-\theta) f(y)$$

**强凸函数**：若存在 μ > 0 使得：
$$f(\theta x + (1-\theta) y) \leq \theta f(x) + (1-\theta) f(y) - \frac{\mu}{2} \theta(1-\theta) \|x - y\|^2$$

等价地：f(x) - (μ/2)‖x‖² 是凸函数。

**关系**：强凸 ⟹ 严格凸 ⟹ 凸

### 1.3 凹函数

**定义**：若 -f 为凸函数，则 f 为**凹函数**（concave function）。

**等价定义**：
$$f(\theta x + (1-\theta) y) \geq \theta f(x) + (1-\theta) f(y)$$

## 2. 凸函数的判定条件

### 2.1 一阶条件

**定理**：设 f 可微，则 f 为凸函数 ⟺ 对任意 x, y ∈ dom f，有：
$$f(y) \geq f(x) + \nabla f(x)^T (y - x)$$

**几何意义**：函数图像位于其切线的上方。

**证明**：
（⟹）设 f 为凸函数，取 θ → 0⁺，由凸性定义：
$$f((1-\theta)x + \theta y) \leq (1-\theta)f(x) + \theta f(y)$$
$$\frac{f(x + \theta(y-x)) - f(x)}{\theta} \leq f(y) - f(x)$$

令 θ → 0⁺，得 ∇f(x)ᵀ(y-x) ≤ f(y) - f(x)。

（⟸）对 x₁, x₂ ∈ dom f 和 θ ∈ [0,1]，设 x = θx₁ + (1-θ)x₂。

由条件：f(x₁) ≥ f(x) + ∇f(x)ᵀ(x₁ - x)
f(x₂) ≥ f(x) + ∇f(x)ᵀ(x₂ - x)

两式分别乘以 θ 和 1-θ 后相加，得：
θf(x₁) + (1-θ)f(x₂) ≥ f(x) = f(θx₁ + (1-θ)x₂)

### 2.2 二阶条件

**定理**：设 f 二阶连续可微，则：
- f 为凸函数 ⟺ ∇²f(x) ≽ 0（半正定），∀x ∈ dom f
- f 为严格凸函数 ⟺ ∇²f(x) ≻ 0（正定），∀x ∈ dom f
- f 为强凸函数 ⟺ ∇²f(x) ≽ μI，∀x ∈ dom f

**证明**：由泰勒展开：
$$f(y) = f(x) + \nabla f(x)^T (y-x) + \frac{1}{2} (y-x)^T \nabla^2 f(x) (y-x) + o(\|y-x\|^2)$$

由一阶条件，f 为凸 ⟺ f(y) ≥ f(x) + ∇f(x)ᵀ(y-x)，这等价于：
$$\frac{1}{2} (y-x)^T \nabla^2 f(x) (y-x) + o(\|y-x\|^2) \geq 0$$

对任意 y-x 成立，故 ∇²f(x) ≽ 0。

### 2.3 Jensen不等式

**定理**（Jensen不等式）：若 f 为凸函数，则对任意 x₁, ..., xₖ ∈ dom f 和 θᵢ ≥ 0, Σθᵢ = 1，有：
$$f\left(\sum_{i=1}^{k} \theta_i x_i\right) \leq \sum_{i=1}^{k} \theta_i f(x_i)$$

**连续版本**：对随机变量 X：
$$f(E[X]) \leq E[f(X)]$$

**例**：
1. f(x) = x²：(E[X])² ≤ E[X²]
2. f(x) = eˣ：e^{E[X]} ≤ E[e^X]
3. f(x) = -ln x：-ln(E[X]) ≤ E[-ln X]，即 E[ln X] ≤ ln(E[X])

## 3. 常见凸函数

### 3.1 ℝ 上的凸函数

**凸函数**：
- x^α (α ≥ 1 或 α ≤ 0, x > 0)
- |x|^p (p ≥ 1)
- e^x
- -ln x (x > 0)
- x ln x (x > 0)

**凹函数**：
- x^α (0 ≤ α ≤ 1, x > 0)
- ln x (x > 0)
- -e^{-x}
- √x (x ≥ 0)

### 3.2 ℝⁿ 上的凸函数

#### 3.2.1 范数
**定理**：任意范数 ‖·‖ 都是凸函数。

**证明**：对任意 x, y 和 θ ∈ [0,1]：
$$\|\theta x + (1-\theta) y\| \leq \|\theta x\| + \|(1-\theta) y\| = \theta \|x\| + (1-\theta) \|y\|$$

**例**：
- l_p 范数：‖x‖_p = (Σ|xᵢ|^p)^{1/p} (p ≥ 1) 是凸函数
- l_∞ 范数：‖x‖_∞ = max|xᵢ| 是凸函数

#### 3.2.2 二次型
**定理**：f(x) = xᵀAx + bᵀx + c 是凸函数 ⟺ A ≽ 0。

**证明**：∇²f(x) = A，由二阶条件即得。

**例**：
- f(x) = ‖x‖² = xᵀx（严格凸）
- f(x) = xᵀAx，A ≽ 0（凸）
- f(x) = (1/2)xᵀQx - bᵀx，Q ≽ 0（凸）

#### 3.2.3 最大值函数
$$f(x) = \max_{i=1,\ldots,m} (a_i^T x + b_i)$$

是凸函数（仿射函数的最大值是凸的）。

**证明**：仿射函数是凸的，凸函数的最大值仍是凸的。

### 3.3 矩阵凸函数

#### 3.3.1 矩阵范数
- Frobenius 范数：‖X‖_F = √(tr(XᵀX)) 是凸函数
- 谱范数：‖X‖₂ = σ_max(X) 是凸函数
- 核范数：‖X‖_* = Σσᵢ(X) 是凸函数

#### 3.3.2 矩阵函数
- tr(X)：线性函数，既凸又凹
- -ln det(X) (X ≻ 0)：凸函数
- tr(X⁻¹) (X ≻ 0)：凸函数
- λ_max(X)：凸函数

**例**：证明 -ln det(X) 在 S₊ⁿ 上是凸函数。

**证明**：对 X, Y ≻ 0 和 θ ∈ [0,1]：
$$-\ln \det(\theta X + (1-\theta)Y) = -\ln \det(X^{1/2}(\theta I + (1-\theta)X^{-1/2}YX^{-1/2})X^{1/2})$$
$$= -\ln \det(X) - \ln \det(\theta I + (1-\theta)X^{-1/2}YX^{-1/2})$$
$$= -\ln \det(X) - \sum_{i=1}^{n} \ln(\theta + (1-\theta)\lambda_i)$$

其中 λᵢ 是 X^{-1/2}YX^{-1/2} 的特征值。由于 -ln 是凸函数，由 Jensen 不等式：
$$-\sum_{i=1}^{n} \ln(\theta + (1-\theta)\lambda_i) \leq \theta(-\ln 1) + (1-\theta)(-\sum_{i} \ln \lambda_i)$$
$$= (1-\theta)(-\ln \det(X^{-1/2}YX^{-1/2})) = (1-\theta)(-\ln \det(Y) + \ln \det(X))$$

因此：
$$-\ln \det(\theta X + (1-\theta)Y) \leq -\ln \det(X) + (1-\theta)(-\ln \det(Y) + \ln \det(X))$$
$$= \theta(-\ln \det(X)) + (1-\theta)(-\ln \det(Y))$$

## 4. 保凸运算

### 4.1 非负组合

**定理**：若 f₁, ..., fₘ 为凸函数，αᵢ ≥ 0，则：
$$f(x) = \alpha_1 f_1(x) + \cdots + \alpha_m f_m(x)$$

为凸函数。

**证明**：由凸函数定义直接验证。

### 4.2 仿射变换

**定理**：若 g : ℝᵐ → ℝ 为凸函数，A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ，则：
$$f(x) = g(Ax + b)$$

为凸函数。

**证明**：对 θ ∈ [0,1]：
$$f(\theta x_1 + (1-\theta) x_2) = g(A(\theta x_1 + (1-\theta) x_2) + b)$$
$$= g(\theta(Ax_1 + b) + (1-\theta)(Ax_2 + b))$$
$$\leq \theta g(Ax_1 + b) + (1-\theta) g(Ax_2 + b) = \theta f(x_1) + (1-\theta) f(x_2)$$

### 4.3 最大值与上确界

**定理**：若 f(x, y) 对每个 y ∈ A 都是 x 的凸函数，则：
$$g(x) = \sup_{y \in A} f(x, y)$$

是凸函数。

**证明**：
$$g(\theta x_1 + (1-\theta) x_2) = \sup_{y \in A} f(\theta x_1 + (1-\theta) x_2, y)$$
$$\leq \sup_{y \in A} [\theta f(x_1, y) + (1-\theta) f(x_2, y)]$$
$$\leq \theta \sup_{y \in A} f(x_1, y) + (1-\theta) \sup_{y \in A} f(x_2, y)$$
$$= \theta g(x_1) + (1-\theta) g(x_2)$$

**例**：
- f(x) = sup_{y∈C} ‖x - y‖（到集合 C 的距离）
- f(x) = max_{i=1,...,m} |aᵢᵀx - bᵢ|（Chebyshev逼近）

### 4.4 复合函数

**定理**：设 h : ℝ → ℝ，g : ℝⁿ → ℝ，f(x) = h(g(x))。

若 h 单调不减且凸，g 凸，则 f 凸。

若 h 单调不增且凸，g 凹，则 f 凸。

**例**：
- f(x) = exp(g(x))：若 g 凸，则 f 凸（h = exp 单调增且凸）
- f(x) = 1/g(x)：若 g 凹且正，则 f 凸（h(t) = 1/t 在 t > 0 上单调减且凸）
- f(x) = -log g(x)：若 g 凹且正，则 f 凸

### 4.5 最小化

**定理**：若 f(x, y) 是凸函数，则：
$$g(x) = \inf_y f(x, y)$$

是凸函数（定义域可能非凸）。

**证明**：对 x₁, x₂ ∈ dom g，任取 ε > 0，存在 y₁, y₂ 使得：
$$f(x_1, y_1) \leq g(x_1) + \varepsilon, \quad f(x_2, y_2) \leq g(x_2) + \varepsilon$$

对 θ ∈ [0,1]：
$$g(\theta x_1 + (1-\theta) x_2) \leq f(\theta x_1 + (1-\theta) x_2, \theta y_1 + (1-\theta) y_2)$$
$$\leq \theta f(x_1, y_1) + (1-\theta) f(x_2, y_2)$$
$$\leq \theta g(x_1) + (1-\theta) g(x_2) + \varepsilon$$

由 ε 的任意性，得 g 是凸函数。

### 4.6 透视函数

**定义**：函数 f : ℝⁿ → ℝ 的**透视函数**定义为：
$$g(x, t) = t f(x/t), \quad \text{dom}\, g = \{(x, t) : x/t \in \text{dom}\, f, t > 0\}$$

**定理**：f 为凸函数 ⟺ g 为凸函数。

**例**：
- f(x) = x² 的透视函数：g(x, t) = x²/t
- f(x) = -log x 的透视函数：g(x, t) = -t log(x/t) = t log t - t log x

## 5. 共轭函数

### 5.1 定义

**定义**：函数 f : ℝⁿ → ℝ 的**共轭函数**（或Fenchel共轭）定义为：
$$f^*(y) = \sup_{x \in \text{dom}\, f} (y^T x - f(x))$$

**性质**：
1. f* 是凸函数（凸函数的上确界）
2. f* 可能为 +∞
3. Young不等式：f(x) + f*(y) ≥ xᵀy

### 5.2 共轭函数的例子

**例1**：f(x) = (1/2)xᵀQx（Q ≻ 0）
$$f^*(y) = \sup_x (y^T x - \frac{1}{2} x^T Q x) = \frac{1}{2} y^T Q^{-1} y$$

（在 x = Q⁻¹y 处取得最大值）

**例2**：f(x) = ‖x‖₁
$$f^*(y) = \begin{cases} 0, & \|y\|_\infty \leq 1 \\ +\infty, & \text{其他} \end{cases}$$

**例3**：f(x) = eˣ
$$f^*(y) = \begin{cases} y \ln y - y, & y > 0 \\ 0, & y = 0 \\ +\infty, & y < 0 \end{cases}$$

### 5.3 二次共轭

**定理**：若 f 为闭凸函数，则 f** = f。

**意义**：凸函数可由其共轭函数完全刻画。

## 6. 水平集与下水平集

### 6.1 定义

**定义**：函数 f 的 **α-下水平集**定义为：
$$C_\alpha = \{x \in \text{dom}\, f : f(x) \leq \alpha\}$$

### 6.2 性质

**定理**：凸函数的所有下水平集都是凸集。

**注意**：逆命题不成立。函数的所有下水平集都是凸集，但函数本身可能不是凸函数。

**例**：f(x) = -e^{-x} 的下水平集是凸集（半无限区间），但 f 不是凸函数（是凹函数）。

### 6.3 拟凸函数

**定义**：若函数 f 的所有下水平集都是凸集，则称 f 为**拟凸函数**。

**等价定义**：对任意 x, y 和 θ ∈ [0,1]：
$$f(\theta x + (1-\theta) y) \leq \max\{f(x), f(y)\}$$

**关系**：凸 ⟹ 拟凸（反之不成立）

## 7. 凸函数的重要性质

### 7.1 极小值唯一性

**定理**：若 f 为严格凸函数，则 f 至多有一个全局极小值点。

**证明**：反证法。设 x₁ ≠ x₂ 都是全局极小值点，f(x₁) = f(x₂) = f*。

对 θ ∈ (0,1)：
$$f(\theta x_1 + (1-\theta) x_2) < \theta f(x_1) + (1-\theta) f(x_2) = f^*$$

这与 f* 是最小值矛盾。

### 7.2 局部极小即全局极小

**定理**：若 f 为凸函数，则 f 的局部极小值点也是全局极小值点。

**证明**：设 x* 为局部极小值点，即存在 r > 0 使得：
$$f(x^*) \leq f(x), \quad \forall x \in B(x^*, r)$$

反证：设存在 y 使得 f(y) < f(x*)。取 θ 充分小使得 x = x* + θ(y - x*) ∈ B(x*, r)。

由凸性：
$$f(x) = f((1-\theta)x^* + \theta y) \leq (1-\theta)f(x^*) + \theta f(y) < f(x^*)$$

这与 x* 为局部极小矛盾。

### 7.3 可微凸函数的下降方向

**定理**：若 f 为可微凸函数，则：
- d 是下降方向 ⟺ ∇f(x)ᵀd < 0
- x* 是极小值点 ⟺ ∇f(x*) = 0

**证明**：由一阶条件：
$$f(x + td) \geq f(x) + t \nabla f(x)^T d$$

若 ∇f(x)ᵀd < 0，则存在 t > 0 使得 f(x + td) < f(x)。

### 7.4 Lipschitz连续梯度

**定义**：若存在 L > 0 使得：
$$\|\nabla f(x) - \nabla f(y)\| \leq L \|x - y\|, \quad \forall x, y$$

则称 ∇f 是 L-Lipschitz 连续的。

**定理**：对 L-光滑凸函数，有：
$$f(y) \leq f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \|y - x\|^2$$

**意义**：提供函数值的上界估计，用于分析算法收敛性。

## 8. 应用实例

### 8.1 机器学习中的凸函数

**线性回归**：
$$f(w) = \frac{1}{2}\|Xw - y\|^2 = \frac{1}{2} w^T (X^T X) w - (X^T y)^T w + \frac{1}{2} y^T y$$

是凸函数（当 X 满秩时严格凸）。

**逻辑回归**：
$$f(w) = \sum_{i=1}^{m} \left[ \log(1 + e^{w^T x_i}) - y_i w^T x_i \right]$$

是凸函数。

**SVM**：
$$f(w, b) = \frac{1}{2}\|w\|^2 + C \sum_{i=1}^{m} \max(0, 1 - y_i(w^T x_i + b))$$

是凸函数。

### 8.2 投资组合优化

**均值-方差模型**：
$$\min_w \frac{1}{2} w^T \Sigma w - \mu^T w$$
$$\text{s.t.} \quad \mathbf{1}^T w = 1, \quad w \geq 0$$

目标函数是凸函数（Σ ≽ 0）。

### 8.3 信号处理

**LASSO**：
$$\min_x \frac{1}{2}\|Ax - b\|^2 + \lambda \|x\|_1$$

目标函数是凸函数（二次函数加凸函数）。

**压缩感知**：
$$\min_x \|x\|_1$$
$$\text{s.t.} \quad Ax = b$$

目标函数是凸函数。

## 9. 小结

### 9.1 核心概念

| 概念 | 定义 | 判定条件 |
|------|------|----------|
| 凸函数 | f(θx+(1-θ)y) ≤ θf(x)+(1-θ)f(y) | 一阶条件/二阶条件 |
| 严格凸 | 不等式严格成立 | ∇²f ≻ 0 |
| 强凸 | f - (μ/2)‖x‖² 凸 | ∇²f ≽ μI |

### 9.2 保凸运算

1. 非负线性组合
2. 仿射变换
3. 最大值与上确界
4. 复合函数（特定条件）
5. 部分最小化
6. 透视函数

### 9.3 重要性质

- 局部极小即全局极小
- 极小值唯一（严格凸）
- 下水平集是凸集
- 梯度为0的点即为极小值点（无约束情况）

---

**参考文献**：
1. 《Convex Optimization》- Stephen Boyd & Lieven Vandenberghe
2. 《凸分析》- 史树中
3. 《Convex Analysis》- R. Tyrrell Rockafellar

**下一章**：[[03_Conjugate_Functions]] - 共轭函数
