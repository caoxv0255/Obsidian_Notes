---
type: concept
topic: improper_integrals
category: calculus
difficulty: advanced
prerequisites:
    - [[09_Indefinite_Integrals]]
    - [[10_Definite_Integrals]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-03-09
status: complete
subject: calculus
chapter: 12
updated: 2026-04-27
---

# 反常积分 (Improper Integrals)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解无限区间积分与无界函数积分的定义与极限化方法
- 掌握比较判别法、极限比较判别法与 p-判别法
- 能区分收敛、绝对收敛和条件收敛，并处理典型例题

## 先修
- [[09_Indefinite_Integrals]] - 不定积分
- [[10_Definite_Integrals]] - 定积分
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：反常积分定义、分情况化为极限
- B档（进阶）：比较判别法、p-判别法与典型收敛性判断
- C档（挑战）：绝对/条件收敛、广义积分与特殊函数联系

## 高数/数分附件补充

### 高数题型补充（同济/托马斯/吉米多维奇）
- **p-型判别**：先看端点奇性，再与 $1/x^p$ 比较
- **Dirichlet/Abel 思路**：振荡因子 + 单调衰减因子
- **常见积分**：高斯型、伽马型、对数型尾积分

### 数分严谨补充（华师大/Rudin）
- **必须拆段**：$\int_{-\infty}^{\infty}$ 不是“直接一口气算完”，而是两侧分别判断
- **条件收敛警惕**：收敛不等于绝对收敛，交换顺序前先证控制条件

### 完整例题（条件收敛）
判断
$$
\int_1^{\infty} \frac{\sin x}{x}\,dx
$$
的敛散性。

解：
由于 $1/x$ 单调趋于 0，且 $\int_1^b \sin x\,dx$ 有界，可用 Dirichlet 判别法判断该积分收敛。
故它是一个典型的收敛但不绝对收敛的反常积分。

## 自测（3问速测）
1. 无限区间和无界函数两类反常积分分别如何化为极限？
2. 为什么 $\int_{-\infty}^{\infty} f(x)dx$ 要拆成两段分别判断？
3. 比较判别法和极限比较判别法各适用于什么情形？

## 1. 定义

**直观理解**：
反常积分是定积分的推广，处理以下两种情况：
1. **无限区间上的积分**：积分区间为 $[a, \infty)$、$(-\infty, b]$ 或 $(-\infty, \infty)$
2. **无界函数的积分**：被积函数在积分区间内某点无界

### 无限区间积分

想象计算"无限延伸"区域的面积：

- 计算 $[1, \infty)$ 上 $y = \frac{1}{x^2}$ 下的面积
- 这是一个"尾巴"无限延伸的区域
- 如果这个"尾巴"的面积是有限的，则反常积分收敛

### 无界函数积分

想象计算"无限高"但"无限窄"区域的面积：

- 计算 $[0, 1]$ 上 $y = \frac{1}{\sqrt{x}}$ 下的面积
- 函数在 $x = 0$ 处无界（趋于无穷大）
- 但由于函数在 $x = 0$ 附近"非常窄"，总面积可能是有限的

## 2. 定理与性质

### 1. 无限区间上的反常积分

#### 类型1：$[a, \infty)$ 上的积分

$$\int_a^{\infty} f(x) dx = \lim_{b \to \infty} \int_a^b f(x) dx$$

**示例**：计算 $\int_1^{\infty} \frac{1}{x^2} dx$

**解**：
$$\int_1^{\infty} \frac{1}{x^2} dx = \lim_{b \to \infty} \int_1^b \frac{1}{x^2} dx$$
$$= \lim_{b \to \infty} \left[-\frac{1}{x}\right]_1^b = \lim_{b \to \infty} \left(-\frac{1}{b} + 1\right) = 1$$

因此，该反常积分收敛，值为 1。

#### 类型2：$(-\infty, b]$ 上的积分

$$\int_{-\infty}^b f(x) dx = \lim_{a \to -\infty} \int_a^b f(x) dx$$

#### 类型3：$(-\infty, \infty)$ 上的积分

$$\int_{-\infty}^{\infty} f(x) dx = \int_{-\infty}^c f(x) dx + \int_c^{\infty} f(x) dx$$

其中 $c$ 是任意实数（通常取 $c = 0$）。

**重要**：只有当两部分都收敛时，整个积分才收敛。

**示例**：计算 $\int_{-\infty}^{\infty} e^{-x^2} dx$

**解**：
$$\int_{-\infty}^{\infty} e^{-x^2} dx = 2 \int_0^{\infty} e^{-x^2} dx$$

这个积分被称为**高斯积分**，其值为 $\sqrt{\pi}$。

### 2. 无界函数的反常积分

#### 类型1：函数在左端点无界

如果 $f(x)$ 在 $(a, b]$ 上连续，但在 $a$ 处无界，则：

$$\int_a^b f(x) dx = \lim_{c \to a^+} \int_c^b f(x) dx$$

**示例**：计算 $\int_0^1 \frac{1}{\sqrt{x}} dx$

**解**：
$$\int_0^1 \frac{1}{\sqrt{x}} dx = \lim_{c \to 0^+} \int_c^1 x^{-1/2} dx$$
$$= \lim_{c \to 0^+} \left[2\sqrt{x}\right]_c^1 = \lim_{c \to 0^+} (2 - 2\sqrt{c}) = 2$$

#### 类型2：函数在右端点无界

如果 $f(x)$ 在 $[a, b)$ 上连续，但在 $b$ 处无界，则：

$$\int_a^b f(x) dx = \lim_{c \to b^-} \int_a^c f(x) dx$$

#### 类型3：函数在内部某点无界

如果 $f(x)$ 在 $[a, b]$ 上除 $c$ 点外连续，但在 $c$ 处无界（$a < c < b$），则：

$$\int_a^b f(x) dx = \int_a^c f(x) dx + \int_c^b f(x) dx$$

只有当两部分都收敛时，整个积分才收敛。

### 3. 收敛判别法

#### 比较判别法

**定理**：设 $0 \leq f(x) \leq g(x)$ 对所有 $x \geq a$ 成立。

- 如果 $\int_a^{\infty} g(x) dx$ 收敛，则 $\int_a^{\infty} f(x) dx$ 收敛
- 如果 $\int_a^{\infty} f(x) dx$ 发散，则 $\int_a^{\infty} g(x) dx$ 发散

**示例**：判断 $\int_1^{\infty} \frac{1}{x^2 + 1} dx$ 的收敛性

**解**：
由于 $\frac{1}{x^2 + 1} < \frac{1}{x^2}$ 对所有 $x \geq 1$ 成立，且 $\int_1^{\infty} \frac{1}{x^2} dx = 1$ 收敛，因此 $\int_1^{\infty} \frac{1}{x^2 + 1} dx$ 收敛。

#### 极限比较判别法

**定理**：设 $f(x) > 0$ 和 $g(x) > 0$ 对所有 $x \geq a$ 成立。如果：

$$\lim_{x \to \infty} \frac{f(x)}{g(x)} = L \quad (0 < L < \infty)$$

则 $\int_a^{\infty} f(x) dx$ 和 $\int_a^{\infty} g(x) dx$ 同敛散。

**示例**：判断 $\int_1^{\infty} \frac{1}{x^2 + 3x + 2} dx$ 的收敛性

**解**：
比较 $\frac{1}{x^2 + 3x + 2}$ 和 $\frac{1}{x^2}$：

$$\lim_{x \to \infty} \frac{\frac{1}{x^2 + 3x + 2}}{\frac{1}{x^2}} = \lim_{x \to \infty} \frac{x^2}{x^2 + 3x + 2} = 1$$

由于 $0 < 1 < \infty$，且 $\int_1^{\infty} \frac{1}{x^2} dx$ 收敛，因此 $\int_1^{\infty} \frac{1}{x^2 + 3x + 2} dx$ 收敛。

#### p-积分判别法

**定理**：$\int_1^{\infty} \frac{1}{x^p} dx$
- 当 $p > 1$ 时收敛
- 当 $p \leq 1$ 时发散

**证明**：
$$\int_1^{\infty} \frac{1}{x^p} dx = \lim_{b \to \infty} \int_1^b x^{-p} dx$$

如果 $p \neq 1$：
$$= \lim_{b \to \infty} \left[\frac{x^{1-p}}{1-p}\right]_1^b = \lim_{b \to \infty} \left(\frac{b^{1-p}}{1-p} - \frac{1}{1-p}\right)$$

- 当 $p > 1$ 时，$1-p < 0$，故 $b^{1-p} \to 0$，积分收敛
- 当 $p < 1$ 时，$1-p > 0$，故 $b^{1-p} \to \infty$，积分发散

如果 $p = 1$：
$$\int_1^{\infty} \frac{1}{x} dx = \lim_{b \to \infty} \left[\ln x\right]_1^b = \lim_{b \to \infty} \ln b = \infty$$

发散！

### 4. 绝对收敛与条件收敛

#### 定义

- **绝对收敛**：$\int |f(x)| dx$ 收敛
- **条件收敛**：$\int f(x) dx$ 收敛，但 $\int |f(x)| dx$ 发散

#### 定理

如果 $\int |f(x)| dx$ 收敛，则 $\int f(x) dx$ 收敛。

**示例**：判断 $\int_1^{\infty} \frac{\sin x}{x^2} dx$ 的收敛性

**解**：
首先判断绝对收敛：
$$\int_1^{\infty} \left|\frac{\sin x}{x^2}\right| dx \leq \int_1^{\infty} \frac{1}{x^2} dx = 1$$

因此 $\int_1^{\infty} \frac{\sin x}{x^2} dx$ 绝对收敛，故收敛。

## 机器学习中的应用

### 1. 概率分布

#### 正态分布的归一化

正态分布的概率密度函数：
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

需要验证：
$$\int_{-\infty}^{\infty} f(x) dx = 1$$

这涉及高斯积分的计算。

#### 指数分布

概率密度函数：
$$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

验证：
$$\int_0^{\infty} \lambda e^{-\lambda x} dx = \lambda \cdot \left[-\frac{1}{\lambda} e^{-\lambda x}\right]_0^{\infty} = 1$$

### 2. 贝叶斯推断中的边缘似然

$$P(D) = \int P(D|\theta) P(\theta) d\theta$$

这是一个反常积分，因为参数 $\theta$ 的取值范围可能是无限的。

### 3. 变分推断

在变分推断中，需要计算KL散度：

$$\text{KL}(q \| p) = \int q(z) \log \frac{q(z)}{p(z)} dz$$

这个积分通常涉及反常积分。

## 3. 代码示例

### 1. 数值计算反常积分

```python
import numpy as np
from scipy.integrate import quad

# 示例1：无限区间积分
f1 = lambda x: 1 / x**2
result1, error1 = quad(f1, 1, np.inf)
print(f"∫₁^∞ 1/x² dx = {result1:.10f} (误差: {error1:.2e})")

# 示例2：高斯积分
f2 = lambda x: np.exp(-x**2)
result2, error2 = quad(f2, -np.inf, np.inf)
print(f"∫₋∞^∞ e^(-x²) dx = {result2:.10f} (精确值: {np.sqrt(np.pi):.10f})")

# 示例3：无界函数积分
f3 = lambda x: 1 / np.sqrt(x)
result3, error3 = quad(f3, 0, 1)
print(f"∫₀¹ 1/√x dx = {result3:.10f} (精确值: 2)")

# 示例4：条件收敛积分
f4 = lambda x: np.sin(x) / x
result4, error4 = quad(f4, 0, np.inf)
print(f"∫₀^∞ sin(x)/x dx = {result4:.10f} (精确值: π/2 ≈ {np.pi/2:.10f})")
```

### 2. 收敛性判断

```python
def check_convergence(f, a, b):
    """
    检查反常积分的收敛性

    参数:
        f: 被积函数
        a: 积分下限（可以是 -np.inf）
        b: 积分上限（可以是 np.inf）

    返回:
        converges: 是否收敛
        result: 积分值（如果收敛）
    """
    try:
        result, error = quad(f, a, b)
        return True, result
    except:
        return False, None

# 测试不同的函数
functions = [
    (lambda x: 1 / x**2, 1, np.inf, "1/x²"),
    (lambda x: 1 / x, 1, np.inf, "1/x"),
    (lambda x: np.exp(-x), 0, np.inf, "e^(-x)"),
    (lambda x: np.sin(x) / x, 0, np.inf, "sin(x)/x"),
]

for f, a, b, name in functions:
    converges, result = check_convergence(f, a, b)
    status = "收敛" if converges else "发散"
    if converges:
        print(f"{name}: {status}, 值 = {result:.6f}")
    else:
        print(f"{name}: {status}")
```

### 3. 可视化反常积分

```python
import matplotlib.pyplot as plt

def plot_improper_integral(f, a, b_limit, title):
    """
    可视化反常积分

    参数:
        f: 被积函数
        a: 积分下限
        b_limit: 上限的最大值（用于可视化）
        title: 标题
    """
    x = np.linspace(a, b_limit, 1000)
    y = f(x)

    plt.figure(figsize=(10, 6))

    # 绘制函数曲线
    plt.plot(x, y, 'b-', linewidth=2, label='f(x)')

    # 填充不同区间的面积
    colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral']
    for i, b in enumerate([2, 5, 10, 20]):
        if b <= b_limit:
            x_fill = np.linspace(a, b, 500)
            y_fill = f(x_fill)
            plt.fill_between(x_fill, 0, y_fill, alpha=0.3, color=colors[i % len(colors)],
                           label=f'∫ᵃ^{b} f(x)dx')

    plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    plt.axvline(x=a, color='k', linestyle='--', alpha=0.5)
    plt.title(title, fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# 示例1：收敛的积分
plot_improper_integral(lambda x: 1/x**2, 1, 10, "∫₁^∞ 1/x² dx (收敛)")

# 示例2：发散的积分
plot_improper_integral(lambda x: 1/x, 1, 10, "∫₁^∞ 1/x dx (发散)")

# 示例3：高斯积分
plot_improper_integral(lambda x: np.exp(-x**2), 0, 5, "∫₀^∞ e^(-x²) dx (收敛)")
```

### 4. 贝叶斯推断中的边缘似然

```python
import scipy.stats as stats

def marginal_likelihood(likelihood_func, prior_func, param_range, num_samples=1000):
    """
    计算边缘似然 P(D) = ∫P(D|θ)·P(θ) dθ

    参数:
        likelihood_func: 似然函数 P(D|θ)
        prior_func: 先验分布 P(θ)
        param_range: 参数范围 [a, b]
        num_samples: 采样点数

    返回:
        marginal: 边缘似然
    """
    theta = np.linspace(param_range[0], param_range[1], num_samples)
    likelihood = likelihood_func(theta)
    prior = prior_func(theta)

    # 使用梯形法则数值积分
    integrand = likelihood * prior
    dtheta = (param_range[1] - param_range[0]) / (num_samples - 1)
    marginal = np.trapz(integrand, theta)

    return marginal

# 示例：Beta-Bernoulli模型
def bernoulli_likelihood(p, data):
    """似然函数：P(D|p) = p^success * (1-p)^failure"""
    success = np.sum(data == 1)
    failure = np.sum(data == 0)
    return p**success * (1-p)**failure

def beta_prior(p, alpha=1, beta=1):
    """先验分布：Beta(alpha, beta)"""
    return stats.beta.pdf(p, alpha, beta)

# 观测数据
data = np.array([1, 1, 0, 1, 0])

# 计算边缘似然
marginal = marginal_likelihood(
    lambda p: bernoulli_likelihood(p, data),
    lambda p: beta_prior(p, alpha=1, beta=1),
    [0, 1]
)

print(f"边缘似然 P(D) = {marginal:.10f}")

# 解析解：Beta(4, 3) 的归一化常数
alpha_post = 4
beta_post = 3
analytical = stats.beta.pdf(0.5, alpha_post, beta_post)  # Beta分布在某点的值
print(f"解析解：Beta({alpha_post}, {beta_post}) 的归一化常数")
```

## 根据题型整理的做题方法
### 计算反常积分的三步走策略

掌握这个流程，大部分题目都能迎刃而解。

#### 🧐 第一步：识别类型与瑕点

这是最关键的一步，决定了后续如何处理。你需要判断这个反常积分属于哪种类型，并找出所有的"问题点"——即瑕点或奇点。

- **无穷区间型**：积分上限或下限为无穷大（$+\infty$ 或 $-\infty$）。这种瑕点一目了然。
  - 例如：$\int_1^{+\infty} \frac{1}{x^2} dx$，瑕点是 $+\infty$。

- **无界函数型（瑕积分）**：被积函数在积分区间内（包括端点）的某一点趋于无穷大。
  - 例如：$\int_0^1 \ln x\, dx$，瑕点是 $x=0$，因为 $\lim_{x \to 0^+} \ln x = -\infty$。

- **混合型**：同时包含上述两种情况。
  - 例如：$\int_0^{+\infty} \frac{1}{\sqrt{x}} dx$，瑕点有 $x=0$ 和 $+\infty$。

**特别注意**：瑕点可能在积分区间的内部。例如 $\int_{-1}^1 \frac{1}{x^2} dx$，瑕点是 $x=0$，它在区间 $[-1, 1]$ 的内部。

#### ✂️ 第二步：拆分区间

如果积分区间内存在瑕点，必须从瑕点处将积分拆开，确保每个子积分只在一个端点处是反常的。

- **瑕点在端点**：无需拆分，直接进入第三步。

- **瑕点在内部**：必须拆分。
  - 例如，对于瑕点在 $c$ 的积分 $\int_a^b f(x) dx$，应拆分为 $\int_a^c f(x) dx + \int_c^b f(x) dx$。

- **混合型**：必须拆分，将无穷区间和瑕点分离开。
  - 例如，$\int_0^{+\infty} f(x) dx$（瑕点在0），可拆分为 $\int_0^1 f(x) dx + \int_1^{+\infty} f(x) dx$。

**重要原则**：一个反常积分只有在其拆分后的所有子积分都收敛时，原积分才收敛。只要有一个子积分发散，整个积分就发散。

#### 🧮 第三步：计算与判断

对拆分后的每个子积分，将其转化为极限形式，然后计算。

1. **写出极限形式**：
   - 无穷限：$\int_a^{+\infty} f(x) dx = \lim_{t \to +\infty} \int_a^t f(x) dx$
   - 瑕点在 $a$：$\int_a^b f(x) dx = \lim_{t \to a^+} \int_t^b f(x) dx$
   - 瑕点在 $b$：$\int_a^b f(x) dx = \lim_{t \to b^-} \int_a^t f(x) dx$

2. **计算定积分**：使用常规的积分方法（如凑微分、换元法、分部积分法等）计算 $\int f(x) dx$，得到原函数 $F(x)$。

3. **代入并求极限**：
   - 利用推广的牛顿-莱布尼茨公式，将上下限代入原函数，并对瑕点取极限。
   - 例如：$\lim_{t \to +\infty} [F(x)] \big|_a^t = \lim_{t \to +\infty} (F(t) - F(a))$。

4. **得出结论**：
   - 如果极限存在且为一个有限值，则该积分收敛，此极限值即为积分结果。
   - 如果极限不存在（为 $\infty$ 或振荡），则该积分发散。

### 💡 核心技巧与常用结论

掌握以下技巧可以让你事半功倍：

#### 1. p-积分判别法（必须熟记）

这是判断敛散性最快的方法，尤其适用于比较判别法。

| 积分类型 | 形式 | 收敛条件 | 发散条件 |
|---------|------|---------|---------|
| 无穷区间 | $\int_1^{+\infty} \frac{1}{x^p} dx$ | $p > 1$ | $p \leq 1$ |
| 瑕积分 | $\int_0^1 \frac{1}{x^p} dx$ | $p < 1$ | $p \geq 1$ |

**记忆口诀**：无穷区间 $p$ 大于1收敛，瑕积分 $p$ 小于1收敛。

#### 2. 比较判别法的极限形式

当直接比较难以找到合适的 $g(x)$ 时，使用极限形式：

$$\lim_{x \to +\infty} \frac{f(x)}{g(x)} = L$$

- 若 $0 < L < +\infty$：两积分同敛散
- 若 $L = 0$：$g(x)$ 收敛 $\Rightarrow$ $f(x)$ 收敛
- 若 $L = +\infty$：$g(x)$ 发散 $\Rightarrow$ $f(x)$ 发散

**应用示例**：判断 $\int_1^{+\infty} \frac{1}{x^2 + x} dx$ 的收敛性。

取 $g(x) = \frac{1}{x^2}$，则 $\lim_{x \to +\infty} \frac{\frac{1}{x^2+x}}{\frac{1}{x^2}} = \lim_{x \to +\infty} \frac{x^2}{x^2+x} = 1$。

由于 $\int_1^{+\infty} \frac{1}{x^2} dx$ 收敛（$p=2 > 1$），所以原积分也收敛。

#### 3. 常见函数增长阶

了解函数的增长快慢有助于快速找到比较对象：

$$\ln x \text{（对数）} < x^a \text{（幂函数，} a > 0 \text{）} < e^x \text{（指数）}$$

- 例如，$e^{-x}$ 的衰减速度远快于 $\frac{1}{x^p}$，因此 $\int_1^{+\infty} x^a e^{-x} dx$ 对任意实数 $a$ 都收敛。

#### 4. 分部积分法

当被积函数是不同类型函数的乘积（如多项式×对数、多项式×三角函数）时，分部积分法是求原函数的利器。它常常能建立递推关系，简化计算。

**常见模式**：
- $\int x^n e^x dx$：反复分部积分
- $\int x^n \ln x dx$：选 $u = \ln x$
- $\int e^{ax} \sin bx dx$：两次分部积分，建立方程求解

#### 5. 绝对收敛与条件收敛的判断

- **绝对收敛判定**：判断 $\int |f(x)| dx$ 是否收敛
- **条件收敛**：积分收敛但绝对值发散

**常见技巧**：对于振荡函数（如 $\frac{\sin x}{x}$），使用 Dirichlet 判别法或 Abel 判别法。

#### 6. 对称性利用

- 若 $f(x)$ 是偶函数：$\int_{-\infty}^{+\infty} f(x) dx = 2\int_0^{+\infty} f(x) dx$
- 若 $f(x)$ 是奇函数：$\int_{-\infty}^{+\infty} f(x) dx = 0$（若积分收敛）

**经典应用**：高斯积分 $\int_{-\infty}^{+\infty} e^{-x^2} dx = 2\int_0^{+\infty} e^{-x^2} dx = \sqrt{\pi}$

## 习题

### 基础题

1. 计算以下反常积分：
   - $\int_1^{\infty} \frac{1}{x^3} dx$
   - $\int_0^{\infty} e^{-2x} dx$
   - $\int_0^1 \frac{1}{\sqrt[3]{x}} dx$

2. 判断以下积分的收敛性：
   - $\int_1^{\infty} \frac{1}{x \ln x} dx$
   - $\int_0^{\infty} \frac{\sin x}{x} dx$
   - $\int_0^1 \frac{1}{x} dx$

3. 证明：$\int_0^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$

### 进阶题

4. 判断以下积分是绝对收敛还是条件收敛：
   - $\int_1^{\infty} \frac{\sin x}{x} dx$
   - $\int_0^{\infty} \frac{\cos x}{1 + x^2} dx$

5. 计算 $\int_{-\infty}^{\infty} \frac{1}{1 + x^2} dx$

6. 证明：如果 $f$ 是偶函数，则 $\int_{-a}^a f(x) dx = 2 \int_0^a f(x) dx$。利用这个性质简化 $\int_{-\infty}^{\infty} e^{-x^2} dx$ 的计算。

### 挑战题

7. 研究伽马函数 $\Gamma(s) = \int_0^{\infty} x^{s-1} e^{-x} dx$ 的性质，并证明 $\Gamma(n+1) = n!$。

8. 在贝叶斯推断中，为什么边缘似然的计算通常是困难的？讨论数值方法的优缺点。

9. 研究"积分变换"（如拉普拉斯变换、傅里叶变换）与反常积分的关系。

## 经典教材参考

- **Rudin《数学分析原理》**：第6章"黎曼-斯蒂尔杰斯积分"
- **华东师大《数学分析》**：第3章第3节"反常积分"
- **同济《高等数学》**：第5章"定积分应用"
- **Thomas《托马斯微积分》**：第8章"无穷序列和级数"

### 5. 含参变量积分 (Integrals with Parameters)

含参变量积分是研究积分中被积函数依赖于参数的理论，在微分方程、数学物理和概率论中有广泛应用。

#### 5.1 基本概念

**定义**：设 $f(x, y)$ 定义在矩形区域 $R = [a, b] \times [c, d]$ 上，对每个固定的 $y \in [c, d]$，$f(x, y)$ 作为 $x$ 的函数在 $[a, b]$ 上可积，则：

$$F(y) = \int_a^b f(x, y) dx$$

称为**含参变量的常义积分**，$y$ 称为参变量。

**直观理解**：
- $F(y)$ 是一个关于 $y$ 的函数
- 对每个 $y$，计算一个定积分
- 积分值随参数 $y$ 变化

#### 5.2 连续性定理

**定理（连续性）**：如果 $f(x, y)$ 在矩形区域 $R = [a, b] \times [c, d]$ 上连续，则：

$$F(y) = \int_a^b f(x, y) dx$$

在 $[c, d]$ 上连续。

**证明思路**：
1. 利用一致连续性
2. 证明 $|F(y) - F(y_0)| < \epsilon$

**示例**：验证 $F(y) = \int_0^1 \frac{dx}{1 + x^2 y}$ 关于 $y$ 在 $[0, 1]$ 上连续。

**解**：被积函数 $f(x, y) = \frac{1}{1 + x^2 y}$ 在 $[0, 1] \times [0, 1]$ 上连续，故 $F(y)$ 在 $[0, 1]$ 上连续。

#### 5.3 可微性定理

**定理（可微性）**：如果 $f(x, y)$ 和 $\frac{\partial f}{\partial y}$ 都在矩形区域 $R = [a, b] \times [c, d]$ 上连续，则：

$$F(y) = \int_a^b f(x, y) dx$$

在 $[c, d]$ 上可微，且：

$$F'(y) = \int_a^b \frac{\partial f}{\partial y}(x, y) dx$$

**核心理念**：求导与积分可以交换顺序！

$$\frac{d}{dy} \int_a^b f(x, y) dx = \int_a^b \frac{\partial f}{\partial y} dx$$

**证明思路**：
1. 定义 $G(y) = \int_a^b \frac{\partial f}{\partial y} dx$
2. 证明 $F(y) = F(c) + \int_c^y G(t) dt$
3. 由微积分基本定理，$F'(y) = G(y)$

**示例**：计算 $F(y) = \int_0^1 \sin(xy) dx$ 的导数。

**解法1**（先积分后求导）：
$$F(y) = \left[-\frac{\cos(xy)}{y}\right]_{x=0}^{x=1} = \frac{1 - \cos y}{y}$$
$$F'(y) = \frac{y\sin y + \cos y - 1}{y^2}$$

**解法2**（交换求导与积分）：
$$F'(y) = \int_0^1 \frac{\partial}{\partial y} \sin(xy) dx = \int_0^1 x\cos(xy) dx$$
$$= \left[\frac{x\sin(xy)}{y}\right]_0^1 - \int_0^1 \frac{\sin(xy)}{y} dx = \frac{\sin y}{y} - \frac{1 - \cos y}{y^2}$$
$$= \frac{y\sin y + \cos y - 1}{y^2}$$

两种方法结果一致！

#### 5.4 积分顺序交换定理

**定理（积分交换）**：如果 $f(x, y)$ 在矩形区域 $R = [a, b] \times [c, d]$ 上连续，则：

$$\int_c^d \left[\int_a^b f(x, y) dx\right] dy = \int_a^b \left[\int_c^d f(x, y) dy\right] dx$$

**即**：

$$\int_c^d F(y) dy = \int_a^b G(x) dx$$

其中 $F(y) = \int_a^b f(x, y) dx$，$G(x) = \int_c^d f(x, y) dy$。

**应用**：计算重积分、证明积分恒等式。

**示例**：计算 $I = \int_0^1 \frac{x^b - x^a}{\ln x} dx$ （$b > a > -1$）。

**解**：注意到 $\frac{x^b - x^a}{\ln x} = \int_a^b x^y dy$，故：

$$I = \int_0^1 \left[\int_a^b x^y dy\right] dx = \int_a^b \left[\int_0^1 x^y dx\right] dy = \int_a^b \frac{1}{y+1} dy = \ln\frac{b+1}{a+1}$$

#### 5.5 含参变量的反常积分

**定义**：积分区间无限或被积函数无界的含参积分：

$$F(y) = \int_a^{\infty} f(x, y) dx$$

**一致收敛**：如果对任意 $\epsilon > 0$，存在 $A > 0$，使得对所有 $y \in [c, d]$，当 $A' > A$ 时：

$$\left|\int_A^{A'} f(x, y) dx\right| < \epsilon$$

则称反常积分关于 $y$ 在 $[c, d]$ 上一致收敛。

**Weierstrass 判别法**：如果 $|f(x, y)| \leq g(x)$ 对所有 $y \in [c, d]$ 成立，且 $\int_a^{\infty} g(x) dx$ 收敛，则 $\int_a^{\infty} f(x, y) dx$ 关于 $y$ 一致收敛。

**性质**：在一致收敛条件下，连续性、可微性、积分交换性仍然成立。

#### 5.6 典型应用

**应用1：Gamma 函数**

$$\Gamma(s) = \int_0^{\infty} x^{s-1} e^{-x} dx$$

这是含参变量的反常积分，具有以下性质：

1. $\Gamma(s+1) = s\Gamma(s)$（分部积分）
2. $\Gamma(n+1) = n!$（自然数阶乘）
3. $\Gamma(1/2) = \sqrt{\pi}$

**证明** $\Gamma(s+1) = s\Gamma(s)$：

$$\Gamma(s+1) = \int_0^{\infty} x^s e^{-x} dx = -x^s e^{-x}\Big|_0^{\infty} + s\int_0^{\infty} x^{s-1} e^{-x} dx = s\Gamma(s)$$

**应用2：Beta 函数**

$$B(p, q) = \int_0^1 x^{p-1}(1-x)^{q-1} dx$$

**关系**：
$$B(p, q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$$

**应用3：概率论中的矩**

随机变量 $X$ 的 $k$ 阶矩：

$$E[X^k] = \int_{-\infty}^{\infty} x^k f(x) dx$$

这是含参变量的积分，参数是概率密度函数 $f$。

**应用4：微分方程的解**

某些微分方程的解可以用积分形式表示：

$$u(x) = \int_a^b G(x, t) f(t) dt$$

其中 $G(x, t)$ 是格林函数（含参变量）。

#### 5.7 代码示例

```python
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# 示例1：含参积分的数值计算
def parametric_integral(y):
    """计算 F(y) = ∫₀¹ sin(xy) dx"""
    f = lambda x, y_param=y: np.sin(x * y_param)
    result, _ = quad(f, 0, 1)
    return result

# 理论值
def theoretical_F(y):
    """理论值：F(y) = (1 - cos y) / y"""
    if np.abs(y) < 1e-10:
        return 0
    return (1 - np.cos(y)) / y

# 比较
y_values = np.linspace(0.1, 5, 50)
numerical = [parametric_integral(y) for y in y_values]
theoretical = [theoretical_F(y) for y in y_values]

plt.figure(figsize=(10, 6))
plt.plot(y_values, numerical, 'b-', linewidth=2, label='数值积分')
plt.plot(y_values, theoretical, 'r--', linewidth=2, label='理论值')
plt.xlabel('y', fontsize=12)
plt.ylabel('F(y)', fontsize=12)
plt.title('含参积分: F(y) = ∫₀¹ sin(xy) dx', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 示例2：交换积分顺序计算
def compute_double_integral_exchange():
    """演示积分顺序交换"""
    # 计算 ∫₀¹ ∫₀¹ x^y dx dy
    
    # 方法1：先对x积分
    def inner_x(y):
        f = lambda x, y_param=y: x**y_param
        result, _ = quad(f, 0, 1)
        return result
    
    result1, _ = quad(inner_x, 0, 1)
    
    # 方法2：先对y积分
    def inner_y(x):
        f = lambda y, x_param=x: x_param**y
        result, _ = quad(f, 0, 1)
        return result
    
    result2, _ = quad(inner_y, 0, 1)
    
    print(f"方法1（先对x积分）: {result1:.10f}")
    print(f"方法2（先对y积分）: {result2:.10f}")
    print(f"两者差异: {abs(result1 - result2):.2e}")

compute_double_integral_exchange()

# 示例3：Gamma函数
def gamma_function(s):
    """
    计算 Gamma(s) = ∫₀^∞ x^(s-1) e^(-x) dx
    """
    f = lambda x: x**(s-1) * np.exp(-x)
    result, _ = quad(f, 0, np.inf)
    return result

# 验证 Gamma(n+1) = n!
from scipy.special import factorial

for n in range(1, 6):
    gamma_val = gamma_function(n + 1)
    factorial_val = factorial(n)
    print(f"Γ({n+1}) = {gamma_val:.6f}, {n}! = {factorial_val:.6f}, 差异 = {abs(gamma_val - factorial_val):.2e}")

# 示例4：Beta函数
def beta_function(p, q):
    """
    计算 B(p, q) = ∫₀¹ x^(p-1)(1-x)^(q-1) dx
    """
    f = lambda x: x**(p-1) * (1-x)**(q-1)
    result, _ = quad(f, 0, 1)
    return result

# 验证 B(p, q) = Γ(p)Γ(q) / Γ(p+q)
p, q = 2, 3
beta_val = beta_function(p, q)
gamma_relation = gamma_function(p) * gamma_function(q) / gamma_function(p + q)
print(f"\nB({p}, {q}) = {beta_val:.6f}")
print(f"Γ({p})Γ({q})/Γ({p+q}) = {gamma_relation:.6f}")
print(f"差异 = {abs(beta_val - gamma_relation):.2e}")

# 示例5：含参积分的导数
def parametric_derivative(y):
    """
    计算 F'(y) 其中 F(y) = ∫₀¹ sin(xy) dx
    使用两种方法：数值微分和积分交换
    """
    # 方法1：数值微分
    h = 1e-5
    F = lambda y: (1 - np.cos(y)) / y if np.abs(y) > 1e-10 else 0
    deriv_numerical = (F(y + h) - F(y - h)) / (2 * h)
    
    # 方法2：积分交换 F'(y) = ∫₀¹ x cos(xy) dx
    f = lambda x: x * np.cos(x * y)
    deriv_integral, _ = quad(f, 0, 1)
    
    return deriv_numerical, deriv_integral

y_test = 2.0
deriv_num, deriv_int = parametric_derivative(y_test)
print(f"\nF'({y_test}) 的两种计算方法:")
print(f"  数值微分: {deriv_num:.10f}")
print(f"  积分交换: {deriv_int:.10f}")
print(f"  差异: {abs(deriv_num - deriv_int):.2e}")
```

### 3.8 典型例题

**例1**：求 $F(y) = \int_0^{\pi/2} \ln(1 + y\sin x) dx$ 的导数（$|y| < 1$）。

**解**：
$$F'(y) = \int_0^{\pi/2} \frac{\partial}{\partial y} \ln(1 + y\sin x) dx = \int_0^{\pi/2} \frac{\sin x}{1 + y\sin x} dx$$

令 $t = \tan\frac{x}{2}$，则 $\sin x = \frac{2t}{1+t^2}$，$dx = \frac{2}{1+t^2} dt$：

$$F'(y) = \int_0^1 \frac{\frac{2t}{1+t^2}}{1 + \frac{2yt}{1+t^2}} \cdot \frac{2}{1+t^2} dt = \int_0^1 \frac{4t}{(1+t^2)(1+t^2+2yt)} dt$$

这需要进一步计算（留作练习）。

**例2**：计算 $I = \int_0^{\infty} \frac{e^{-ax} - e^{-bx}}{x} dx$（$b > a > 0$）。

**解法1**（含参积分）：
$$I = \int_0^{\infty} \left[\int_a^b e^{-xy} dy\right] dx = \int_a^b \left[\int_0^{\infty} e^{-xy} dx\right] dy = \int_a^b \frac{1}{y} dy = \ln\frac{b}{a}$$

**解法2**（Frullani积分）：
对于 $f(x)$ 满足 $f(0)$ 和 $f(\infty)$ 存在：

$$\int_0^{\infty} \frac{f(ax) - f(bx)}{x} dx = [f(0) - f(\infty)]\ln\frac{b}{a}$$

取 $f(x) = e^{-x}$，$f(0) = 1$，$f(\infty) = 0$：

$$I = (1 - 0)\ln\frac{b}{a} = \ln\frac{b}{a}$$

## 相关链接

- [[09_Indefinite_Integrals]] - 不定积分（反常积分的基础）
- [[10_Definite_Integrals]] - 定积分（反常积分的推广）
- [[13_Series]] - 级数（反常积分与级数的关系）
- [[../../01_Mathematics/Probability/03_Distributions]] - 概率分布（反常积分的应用）
- [[06_Case_Finance]] - 金融案例（概率分布的应用）
## 易错点
- 把“积分区间无限”与“被积函数无界”混为一谈
- 判断 $\int_{-\infty}^{\infty}$ 时只看一侧收敛
- 比较判别法中不等式方向写反
- 误把绝对收敛当成条件收敛

## 10. 总结
### 10.1 重要定义
1. 反常积分：积分区间无限或被积函数无界的积分
2. 无穷限积分：积分限为无穷的积分
3. 瑕积分：被积函数在积分区间内无界的积分
4. 绝对收敛：积分的绝对值收敛
5. 条件收敛：积分收敛但绝对值发散

### 10.2 重要定理
1. 比较判别法：比较函数与已知敛散性的函数
2. 极限比较判别法：利用函数比的极限判断
3. p-判别法：$\int_1^\infty \frac{1}{x^p}dx$ 收敛当且仅当 $p > 1$
4. 绝对收敛定理：绝对收敛的反常积分必收敛

### 10.3 重要证明
1. p-判别法的证明：计算 $\int_1^\infty \frac{1}{x^p}dx$ 的值
2. 比较判别法的证明：利用积分的单调性
3. 绝对收敛定理的证明：利用绝对值不等式

### 10.4 重要性质
1. 线性性：反常积分保持线性关系
2. 区间可加性：可以分割积分区间
3. 收敛的反常积分具有定积分的大部分性质
4. Gamma函数与Beta函数的关系
## 11. 练习（分层）
本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 计算并判断敛散性：$$\int_1^{\infty} \frac{1}{x^2} \, dx$$。
2. 计算并判断敛散性：$$\int_0^1 \frac{1}{\sqrt{x}} \, dx$$。
3. 计算并判断敛散性：$$\int_0^{\infty} e^{-2x} \, dx$$。
4. 写出 $$\int_{-\infty}^{\infty} \frac{1}{1+x^2} \, dx$$ 的正确拆分方式，并说明为什么不能直接当作一个普通定积分处理。

### B档（进阶）
1. 用比较判别法判断 $$\int_1^{\infty} \frac{1}{x^2+x} \, dx$$ 的敛散性。
2. 用极限比较判别法判断 $$\int_0^1 \frac{1}{x^{1/2}(1+x)} \, dx$$ 的敛散性。
3. 判断 $$\int_1^{\infty} \frac{\sin x}{x} \, dx$$ 是否收敛，并说明它属于绝对收敛还是条件收敛。
4. 证明：若 $$f(x)\ge 0$$ 且 $$\int_1^{\infty} f(x)\,dx$$ 收敛，则对任意常数 $$c>0$$，$$\int_1^{\infty} cf(x)\,dx$$ 也收敛。

### C档（挑战）
1. 设 $$\Gamma(s)=\int_0^{\infty} x^{s-1}e^{-x}\,dx$$，证明 $$\Gamma(s+1)=s\Gamma(s)$$，并说明它在何种条件下收敛。
2. 证明 Frullani 型积分公式：$$\int_0^{\infty} \frac{e^{-ax}-e^{-bx}}{x} \, dx = \ln\frac{b}{a}$$（$$b>a>0$$）。
3. 设 $$I(a,b)=\int_0^1 \frac{x^a-x^b}{\ln x} \, dx$$（$$b>a>-1$$），尝试用含参变量积分方法计算它。
4. 研究 $$\int_0^{\infty} \frac{\sin x}{x} \, dx$$ 的收敛性，并说明它为什么是经典的条件收敛例子。



