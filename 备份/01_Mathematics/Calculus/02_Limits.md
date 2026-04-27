---
type: concept

topic: limits

category: calculus

difficulty: intermediate

prerequisites:
    - [[01_Real_Numbers]]

acm_relevant: false

created: 2026-02-20

status: complete

subject: calculus
chapter: 02
updated: 2026-04-27
---

# 极限 (Limits)

## 📌 学习目标

- 说清楚函数极限/数列极限的定义与“存在”的含义
- 熟练处理常见未定式（$\frac{0}{0}$、$\frac{\infty}{\infty}$、$0\cdot\infty$、$1^\infty$ 等）
- 能为核心定理（夹逼、唯一性、四则运算）写出证明主线

## ✅ 先修

- [[01_Real_Numbers]]
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层

- **基础**：定义 + 常用等价无穷小 + 五步法 + 常见题型
- **进阶**：夹逼/唯一性/四则运算等证明与条件边界
- **拓展**：数值近似与机器学习中的极限视角

## 1. 定义

**直观理解**：
极限是微积分的基础概念，描述函数在某一点附近的行为。当自变量趋近于某个值时，如果函数值趋近于一个确定的数，这个数就是函数在该点的极限。

想象你在观察一个物体逐渐靠近一个目标。虽然物体可能永远不会真正到达目标（比如你只能无限接近），但你可以清楚地看到它越来越接近某个位置。极限就是描述这种"无限接近"但不一定"到达"的概念。

例如：当你不断地把 1/2, 1/4, 1/8, 1/16... 加起来时，和越来越接近 2，但永远不会超过 2。这里的 2 就是这个级数的极限。

## 2. 定理与性质

### 极限的定义

对于函数 f(x)，当 x 趋近于 a 时，f(x) 的极限是 L，记作：
$$\lim_{x \to a} f(x) = L$$

这意味着：当 x 无限接近 a 时（但不等于 a），f(x) 无限接近 L。

### 极限的性质

1. **唯一性**：如果极限存在，则极限值唯一
2. **局部有界性**：如果极限存在，函数在该点附近有界
3. **保号性**：如果极限为正（负），函数在该点附近也为正（负）

### 计算极限的方法

1. **直接代入法**：对于连续函数，直接代入
2. **因式分解法**：分解后约去零因子
3. **有理化法**：分子分母有理化
4. **等价无穷小代换**：使用常见的等价无穷小
5. **洛必达法则**：0/0 或 ∞/∞ 型

## 3. 代码示例

### 示例 1：计算基本极限

```python
import numpy as np

def calculate_limit(func, x0, h=1e-10):
    """使用数值方法计算极限"""
    x_left = x0 - h
    x_right = x0 + h
    return (func(x_left) + func(x_right)) / 2

# 示例 1: lim(x→0) sin(x)/x = 1
f1 = lambda x: np.sin(x) / x
limit1 = calculate_limit(f1, 0)
print(f"lim(x→0) sin(x)/x = {limit1}")

# 示例 2: lim(x→∞) (1 + 1/x)^x = e
f2 = lambda x: (1 + 1/x)**x
limit2 = calculate_limit(f2, 1e6, h=1e4)
print(f"lim(x→∞) (1 + 1/x)^x ≈ {limit2}")
```

### 示例 2：左右极限

```python
def left_limit(func, x0, h=1e-10):
    """计算左极限"""
    return func(x0 - h)

def right_limit(func, x0, h=1e-10):
    """计算右极限"""
    return func(x0 + h)

# 示例: lim(x→0) |x|/x
f = lambda x: abs(x) / x if x != 0 else None

lim_left = left_limit(f, 0)
lim_right = right_limit(f, 0)

print(f"左极限 lim(x→0-) |x|/x = {lim_left}")
print(f"右极限 lim(x→0+) |x|/x = {lim_right}")

if lim_left == lim_right:
    print(f"极限存在: {lim_left}")
else:
    print("极限不存在（左右极限不等）")
```

### 示例 3：使用 sympy 计算符号极限

```python
from sympy import limit, oo, sin, cos, exp, log, sqrt, symbols

x = symbols('x')

# 各种极限计算
limits = [
    (sin(x)/x, 0, "lim(x→0) sin(x)/x"),
    ((1 + 1/x)**x, oo, "lim(x→∞) (1 + 1/x)^x"),
    ((x**2 - 1)/(x - 1), 1, "lim(x→1) (x²-1)/(x-1)"),
    (exp(-x)*x, oo, "lim(x→∞) x·e^(-x)"),
    ((sqrt(x+1)-1)/x, 0, "lim(x→0) (√(x+1)-1)/x"),
]

for expr, point, desc in limits:
    result = limit(expr, x, point)
    print(f"{desc} = {result}")
```

### 示例 4：洛必达法则

```python
from sympy import limit, diff, symbols, sin, exp, log

x = symbols('x')

def lhopital_rule(expr, x, point):
    """使用洛必达法则计算极限"""
    try:
        # 检查是否为 0/0 或 ∞/∞ 型
        num = limit(expr.as_numer_denom()[0], x, point)
        den = limit(expr.as_numer_denom()[1], x, point)
        
        # 如果满足条件，应用洛必达法则
        if (num == 0 and den == 0) or (abs(num) == oo and abs(den) == oo):
            derivative = diff(expr.as_numer_denom()[0], x) / diff(expr.as_numer_denom()[1], x)
            return limit(derivative, x, point)
        else:
            return limit(expr, x, point)
    except:
        return limit(expr, x, point)

# 示例
expr1 = sin(x) / x
result1 = lhopital_rule(expr1, x, 0)
print(f"洛必达法则: lim(x→0) sin(x)/x = {result1}")

expr2 = (exp(x) - 1) / x
result2 = lhopital_rule(expr2, x, 0)
print(f"洛必达法则: lim(x→0) (e^x-1)/x = {result2}")
```

### 示例 5：极限在机器学习中的应用

```python
import numpy as np

def sigmoid(x):
    """Sigmoid 函数"""
    return 1 / (1 + np.exp(-x))

def sigmoid_limit():
    """分析 Sigmoid 函数的极限"""
    # lim(x→∞) sigmoid(x) = 1
    x_large = 100
    print(f"sigmoid({x_large}) ≈ {sigmoid(x_large)}")
    
    # lim(x→-∞) sigmoid(x) = 0
    x_small = -100
    print(f"sigmoid({x_small}) ≈ {sigmoid(x_small)}")
    
    # lim(x→0) sigmoid(x) = 0.5
    x_zero = 0
    print(f"sigmoid({x_zero}) = {sigmoid(x_zero)}")

sigmoid_limit()

# 梯度消失问题（极限趋近于 0）
def tanh_derivative(x):
    """Tanh 函数的导数"""
    return 1 - np.tanh(x)**2

print(f"\nTanh 导数在 x=10 处: {tanh_derivative(10)}")
print("当 x 很大时，梯度趋近于 0（梯度消失问题）")
```

## 4. 机器学习应用

### 损失函数的极限分析

```python
import numpy as np

def logistic_loss(y_true, y_pred):
    """逻辑回归损失函数"""
    epsilon = 1e-15  # 避免对数为 0
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# 分析损失函数的极限
print("逻辑回归损失函数极限分析:")
print(f"当 y_pred→0, y_true=1 时: {logistic_loss(1, 1e-10)}")
print(f"当 y_pred→1, y_true=0 时: {logistic_loss(0, 1 - 1e-10)}")
print("损失函数在这些情况下趋近于无穷大")
```

### 正则化的极限行为

```python
def l2_regularization(weights, lambda_reg):
    """L2 正则化"""
    return lambda_reg * np.sum(weights**2)

# 当 λ→0 时，正则化效果消失
weights = np.array([1, 2, 3])
for lam in [1, 0.1, 0.01, 0.001]:
    reg = l2_regularization(weights, lam)
    print(f"λ={lam}: L2 正则化 = {reg}")
print("当 λ→0 时，正则化项趋近于 0")
```

## 根据题型整理的做题方法

### 求极限的五步分析法

遇到极限题目，按以下步骤分析，能快速找到解题思路。

#### 📊 第一步：判断极限类型

首先观察极限的形式，判断属于哪种类型：

| 类型 | 特征 | 典型例子 |
|-----|------|---------|
| **确定型** | 可直接代入 | $\lim_{x \to 2} x^2 + 1$ |
| **$\frac{0}{0}$ 型** | 分子分母同时趋于0 | $\lim_{x \to 0} \frac{\sin x}{x}$ |
| **$\frac{\infty}{\infty}$ 型** | 分子分母同时趋于无穷 | $\lim_{x \to \infty} \frac{x^2+1}{2x^2+3}$ |
| **$\infty - \infty$ 型** | 两个无穷大相减 | $\lim_{x \to 0} \frac{1}{x} - \frac{1}{x^2}$ |
| **$0 \cdot \infty$ 型** | 零与无穷大相乘 | $\lim_{x \to 0^+} x \ln x$ |
| **$1^\infty$ 型** | 底趋于1，指数趋于无穷 | $\lim_{x \to \infty} (1 + \frac{1}{x})^x$ |
| **$0^0$ 型** 或 **$\infty^0$ 型** | 幂指函数 | $\lim_{x \to 0^+} x^x$ |

#### 🔍 第二步：选择合适方法

根据极限类型，选择对应的求解方法：

```
确定型 → 直接代入法
↓
0/0 或 ∞/∞ 型 → 洛必达法则 / 等价无穷小 / 泰勒展开
↓
∞ - ∞ 型 → 通分或有理化，化为分式形式
↓
0·∞ 型 → 转化为 0/0 或 ∞/∞ 型
↓
1^∞ 型 → 利用 e 的定义或取对数
↓
0^0 或 ∞^0 型 → 取对数转化为乘积
```

#### ✏️ 第三步：执行计算

根据选定的方法进行计算，注意以下几点：

1. **洛必达法则**：每次使用前需验证是否满足条件
2. **等价无穷小**：只能用于乘除，不能用于加减
3. **泰勒展开**：确定展开的阶数，保证精度
4. **有理化**：分子或分母含有根号时的常用技巧

#### ✅ 第四步：验证结果

- 检查极限是否存在（左右极限是否相等）
- 验证结果是否合理
- 对于数值极限，可以用数值方法验证

### 💡 核心技巧与常用结论

#### 1. 常用等价无穷小（$x \to 0$ 时）

必须熟记，考试可直接使用：

| 原式 | 等价无穷小 |
|-----|----------|
| $\sin x$ | $x$ |
| $\tan x$ | $x$ |
| $\arcsin x$ | $x$ |
| $\arctan x$ | $x$ |
| $1 - \cos x$ | $\frac{x^2}{2}$ |
| $e^x - 1$ | $x$ |
| $\ln(1 + x)$ | $x$ |
| $(1 + x)^\alpha - 1$ | $\alpha x$ |
| $x - \ln(1 + x)$ | $\frac{x^2}{2}$ |
| $x - \sin x$ | $\frac{x^3}{6}$ |

**记忆技巧**：所有基本初等函数在原点附近都近似于一次函数。

**注意**：等价无穷小只能用于**乘除**，不能用于加减！

- ✅ 正确：$\lim_{x \to 0} \frac{\sin x \cdot \tan x}{x^2} = \lim_{x \to 0} \frac{x \cdot x}{x^2} = 1$
- ❌ 错误：$\lim_{x \to 0} \frac{\tan x - \sin x}{x^3} = \lim_{x \to 0} \frac{x - x}{x^3} = 0$（实际结果是 $\frac{1}{2}$）

#### 2. 重要极限公式

| 极限 | 值 | 应用场景 |
|-----|---|---------|
| $\lim_{x \to 0} \frac{\sin x}{x}$ | $1$ | 三角函数极限 |
| $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$ | $\frac{1}{2}$ | 三角函数极限 |
| $\lim_{x \to \infty} (1 + \frac{1}{x})^x$ | $e$ | 指数型极限 |
| $\lim_{x \to 0} (1 + x)^{\frac{1}{x}}$ | $e$ | 指数型极限 |
| $\lim_{x \to 0} \frac{e^x - 1}{x}$ | $1$ | 指数函数极限 |
| $\lim_{x \to 0} \frac{\ln(1 + x)}{x}$ | $1$ | 对数函数极限 |
| $\lim_{x \to 0} \frac{a^x - 1}{x}$ | $\ln a$ | 指数函数极限 |

#### 3. 洛必达法则使用要点

**适用条件**：
1. $\frac{0}{0}$ 型或 $\frac{\infty}{\infty}$ 型
2. $\lim \frac{f'(x)}{g'(x)}$ 存在或为 $\infty$

**注意事项**：
- 每次使用前验证条件
- 可连续使用，直到求得结果
- 若导数之比的极限不存在，不能说明原极限不存在

**常见陷阱**：
```python
# 错误示例：盲目使用洛必达
# lim(x→∞) (x + sin x) / x
# 洛必达后：lim(x→∞) (1 + cos x) / 1，极限不存在！
# 但原极限 = lim(x→∞) (1 + sin x / x) = 1 存在
```

#### 4. 泰勒展开法

当洛必达法则计算繁琐时，泰勒展开往往更高效：

**常用泰勒公式**（在 $x = 0$ 处）：
- $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + o(x^3)$
- $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} + o(x^5)$
- $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} + o(x^4)$
- $\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} + o(x^3)$
- $(1 + x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!}x^2 + o(x^2)$

**技巧**：展开到最低非零项即可。

#### 5. 夹逼准则的应用

**适用场景**：
- 函数形式复杂，直接求极限困难
- 有明显上下界的函数

**常见形式**：
- $\lim_{n \to \infty} \frac{1}{n^2 + n + 1} + \cdots + \frac{1}{n^2 + n + n}$（n项和的极限）
- $\lim_{n \to \infty} \sqrt[n]{a_1^n + a_2^n + \cdots + a_k^n}$（幂平均）

**操作步骤**：
1. 找到放大和缩小的函数 $g(x)$ 和 $h(x)$
2. 证明 $g(x) \leq f(x) \leq h(x)$
3. 计算 $\lim g(x) = \lim h(x) = L$
4. 得出 $\lim f(x) = L$

#### 6. $1^\infty$ 型极限的处理

**核心公式**：$\lim (1 + u)^v = e^{\lim u \cdot v}$（当 $u \to 0, v \to \infty$ 时）

**解题步骤**：
1. 将底数写成 $1 + \text{无穷小量}$ 的形式
2. 提取指数部分：$\lim (1 + u)^v = \lim e^{v \cdot \ln(1+u)}$
3. 利用等价无穷小 $\ln(1+u) \sim u$
4. 计算 $\lim v \cdot u$

**示例**：$\lim_{x \to \infty} (1 + \frac{2}{x})^{3x}$
$$= e^{\lim_{x \to \infty} 3x \cdot \frac{2}{x}} = e^6$$

#### 7. 左右极限的判断

当以下情况时，必须分别计算左右极限：
- 分段函数在分段点
- 含有 $|x|$、$\sqrt{x}$ 等函数
- $a^x$（$a > 0, a \neq 1$）在 $x \to \infty$ 时
- $\arctan x$ 在 $x \to \pm\infty$ 时

**极限存在的充要条件**：$\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x)$

### 🎯 题型分类与对策

| 题型 | 特点 | 推荐方法 |
|-----|------|---------|
| 分式极限 | 分子分母多项式 | 洛必达或比较最高次 |
| 根式极限 | 含有 $\sqrt{x}$ | 有理化或泰勒展开 |
| 三角极限 | 含 $\sin, \cos, \tan$ | 等价无穷小或洛必达 |
| 指数对数极限 | 含 $e^x, \ln x$ | 等价无穷小或泰勒 |
| 幂指极限 | $f(x)^{g(x)}$ 形式 | 取对数或 $e$ 的定义 |
| 数列极限 | $n \to \infty$ | 夹逼准则或单调有界 |

## 5. 证明

### 证明1：夹逼定理

**定理**：设 $f, g, h$ 是定义在 $U^\circ(a, \delta)$ 上的函数，满足 $g(x) \leq f(x) \leq h(x)$ 对所有 $x \in U^\circ(a, \delta)$ 成立。如果 $\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$，则 $\lim_{x \to a} f(x) = L$。

**证明**：
对于任意 $\varepsilon > 0$，由于 $\lim_{x \to a} g(x) = L$，存在 $\delta_1 > 0$，使得对于所有 $x \in U^\circ(a, \delta_1)$，有 $|g(x) - L| < \varepsilon$。

即 $L - \varepsilon < g(x) < L + \varepsilon$。

类似地，由于 $\lim_{x \to a} h(x) = L$，存在 $\delta_2 > 0$，使得对于所有 $x \in U^\circ(a, \delta_2)$，有 $|h(x) - L| < \varepsilon$。

即 $L - \varepsilon < h(x) < L + \varepsilon$。

令 $\delta' = \min\{\delta, \delta_1, \delta_2\}$，则对于所有 $x \in U^\circ(a, \delta')$，有：
$$L - \varepsilon < g(x) \leq f(x) \leq h(x) < L + \varepsilon$$

因此 $|f(x) - L| < \varepsilon$，故 $\lim_{x \to a} f(x) = L$。

### 证明2：极限的唯一性

**定理**：如果 $\lim_{x \to a} f(x)$ 存在，则极限值是唯一的。

**证明**：
假设 $\lim_{x \to a} f(x) = L_1$ 且 $\lim_{x \to a} f(x) = L_2$，其中 $L_1 \neq L_2$。

令 $\varepsilon = \frac{|L_1 - L_2|}{2} > 0$。

由于 $\lim_{x \to a} f(x) = L_1$，存在 $\delta_1 > 0$，使得对于所有 $x \in U^\circ(a, \delta_1)$，有 $|f(x) - L_1| < \varepsilon$。

由于 $\lim_{x \to a} f(x) = L_2$，存在 $\delta_2 > 0$，使得对于所有 $x \in U^\circ(a, \delta_2)$，有 $|f(x) - L_2| < \varepsilon$。

令 $\delta = \min\{\delta_1, \delta_2\}$，则对于所有 $x \in U^\circ(a, \delta)$，有：
$$|f(x) - L_1| < \varepsilon \text{ 且 } |f(x) - L_2| < \varepsilon$$

由三角不等式：
$$|L_1 - L_2| \leq |L_1 - f(x)| + |f(x) - L_2| < 2\varepsilon = |L_1 - L_2|$$

矛盾！因此假设不成立，极限值是唯一的。

### 证明3：极限的局部有界性

**定理**：如果 $\lim_{x \to a} f(x) = L$，则存在 $\delta > 0$ 和 $M > 0$，使得对于所有 $x \in U^\circ(a, \delta)$，有 $|f(x)| \leq M$。

**证明**：
对于 $\varepsilon = 1$，由于 $\lim_{x \to a} f(x) = L$，存在 $\delta > 0$，使得对于所有 $x \in U^\circ(a, \delta)$，有 $|f(x) - L| < 1$。

由三角不等式：
$$|f(x)| = |f(x) - L + L| \leq |f(x) - L| + |L| < 1 + |L|$$

令 $M = 1 + |L|$，则对于所有 $x \in U^\circ(a, \delta)$，有 $|f(x)| \leq M$。

### 证明4：极限的四则运算

**定理**：设 $\lim_{x \to a} f(x) = A$，$\lim_{x \to a} g(x) = B$，则：

1. $\lim_{x \to a} [f(x) + g(x)] = A + B$
2. $\lim_{x \to a} [f(x) - g(x)] = A - B$
3. $\lim_{x \to a} [f(x) \cdot g(x)] = A \cdot B$
4. 如果 $B \neq 0$，则 $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{A}{B}$

**证明（乘法）**：
对于任意 $\varepsilon > 0$，我们需要找到 $\delta > 0$，使得对于所有 $x \in U^\circ(a, \delta)$，有：
$$|f(x)g(x) - AB| < \varepsilon$$

注意到：
$$|f(x)g(x) - AB| = |f(x)g(x) - f(x)B + f(x)B - AB| \leq |f(x)| \cdot |g(x) - B| + |B| \cdot |f(x) - A|$$

由于 $\lim_{x \to a} f(x) = A$，存在 $\delta_1 > 0$，使得对于所有 $x \in U^\circ(a, \delta_1)$，有 $|f(x) - A| < 1$。

因此 $|f(x)| < |A| + 1$。

由于 $\lim_{x \to a} g(x) = B$，存在 $\delta_2 > 0$，使得对于所有 $x \in U^\circ(a, \delta_2)$，有 $|g(x) - B| < \frac{\varepsilon}{2(|A| + 1)}$。

由于 $\lim_{x \to a} f(x) = A$，存在 $\delta_3 > 0$，使得对于所有 $x \in U^\circ(a, \delta_3)$，有 $|f(x) - A| < \frac{\varepsilon}{2|B|}$（假设 $B \neq 0$，如果 $B = 0$ 则不需要第二项）。

令 $\delta = \min\{\delta_1, \delta_2, \delta_3\}$，则对于所有 $x \in U^\circ(a, \delta)$：
$$|f(x)g(x) - AB| \leq (|A| + 1) \cdot \frac{\varepsilon}{2(|A| + 1)} + |B| \cdot \frac{\varepsilon}{2|B|} = \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

因此 $\lim_{x \to a} [f(x) \cdot g(x)] = A \cdot B$。

## 6. 更多例题

### 例题4：计算 $\lim_{x \to 0} \frac{\sin x}{x} = 1$

**解**：
利用几何方法或泰勒展开：

**方法1（几何方法）**：
考虑单位圆，扇形面积公式：
$$\frac{1}{2}\sin x < \frac{1}{2}x < \frac{1}{2}\tan x$$

化简：
$$\cos x < \frac{\sin x}{x} < 1$$

由于 $\lim_{x \to 0} \cos x = 1$，由夹逼定理：
$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

**方法2（泰勒展开）**：
$$\sin x = x - \frac{x^3}{6} + o(x^3)$$

因此：
$$\frac{\sin x}{x} = 1 - \frac{x^2}{6} + o(x^2)$$

当 $x \to 0$ 时，$\frac{\sin x}{x} \to 1$。

### 例题5：计算 $\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$

**解**：
令 $n = \lfloor x \rfloor$，则 $n \leq x < n + 1$。

由于 $\left(1 + \frac{1}{x}\right)^x$ 关于 $x$ 单调递增，有：
$$\left(1 + \frac{1}{n + 1}\right)^n \leq \left(1 + \frac{1}{x}\right)^x \leq \left(1 + \frac{1}{n}\right)^{n + 1}$$

计算左右两端的极限：
$$\lim_{n \to \infty} \left(1 + \frac{1}{n + 1}\right)^n = \lim_{n \to \infty} \left(1 + \frac{1}{n + 1}\right)^{n + 1} \cdot \left(1 + \frac{1}{n + 1}\right)^{-1} = e \cdot 1 = e$$

$$\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^{n + 1} = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \cdot \left(1 + \frac{1}{n}\right) = e \cdot 1 = e$$

由夹逼定理，$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$。

### 例题6：计算 $\lim_{x \to 0} \frac{e^x - 1}{x}$

**解**：
利用泰勒展开或洛必达法则：

**方法1（泰勒展开）**：
$$e^x = 1 + x + \frac{x^2}{2} + o(x^2)$$

因此：
$$\frac{e^x - 1}{x} = \frac{x + \frac{x^2}{2} + o(x^2)}{x} = 1 + \frac{x}{2} + o(x)$$

当 $x \to 0$ 时，$\frac{e^x - 1}{x} \to 1$。

**方法2（洛必达法则）**：
这是 $\frac{0}{0}$ 型极限：
$$\lim_{x \to 0} \frac{e^x - 1}{x} = \lim_{x \to 0} \frac{(e^x - 1)'}{x'} = \lim_{x \to 0} e^x = 1$$

## 7. 更多习题

### 基础题

1. 计算 $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$

2. 计算 $\lim_{x \to 0} \frac{\ln(1 + x)}{x}$

3. 计算 $\lim_{x \to 0} \frac{a^x - 1}{x}$，其中 $a > 0$

### 进阶题

4. 计算 $\lim_{x \to 0} \frac{\tan x - \sin x}{x^3}$

5. 计算 $\lim_{x \to \infty} \left(1 + \frac{a}{x}\right)^{bx}$

6. 证明：如果 $\lim_{x \to a} f(x) = A$ 且 $A > 0$，则存在 $\delta > 0$，使得对于所有 $x \in U^\circ(a, \delta)$，有 $f(x) > 0$。

### 挑战题

7. 证明：$\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e$ 的严格定义（使用单调有界数列定理）。

8. 计算 $\lim_{x \to 0} \frac{\arcsin x - x}{x^3}$

9. 在深度学习中，为什么需要检查梯度的范数？这涉及什么极限概念？

## 8. 更多应用

### 应用3：梯度消失问题

梯度消失问题本质上是极限 $\lim_{n \to \infty} W^n = 0$ 的问题，其中 $|W| < 1$。

```python
import numpy as np
import matplotlib.pyplot as plt

def gradient_vanishing(weights, n_layers):
    """模拟梯度消失"""
    gradients = np.ones(weights.shape)
    
    for layer in range(n_layers):
        gradients = gradients * weights
        
    return gradients

# 示例：权重小于1时梯度消失
weights = np.array([0.9])
n_layers = 50

gradients_history = []
for layer in range(n_layers):
    grad = gradient_vanishing(weights, layer)
    gradients_history.append(grad[0])

plt.figure(figsize=(10, 6))
plt.plot(range(n_layers), gradients_history, 'b-', label='梯度')
plt.axhline(y=0, color='r', linestyle='--', label='零')
plt.title("梯度消失问题")
plt.xlabel("层数")
plt.ylabel("梯度值")
plt.legend()
plt.grid(True, alpha=0.3)
plt.yscale('log')
plt.show()

print(f"第1层梯度: {gradients_history[0]:.6f}")
print(f"第10层梯度: {gradients_history[9]:.6f}")
print(f"第50层梯度: {gradients_history[-1]:.10f}")
print(f"极限: lim(n→∞) 0.9^n = 0")
```

### 应用4：学习率衰减

学习率衰减策略基于极限 $\lim_{t \to \infty} \eta_t = 0$ 的思想。

```python
import numpy as np

def learning_rate_schedule(initial_lr, t, decay_type='exponential'):
    """学习率衰减策略"""
    if decay_type == 'exponential':
        return initial_lr * np.exp(-0.1 * t)
    elif decay_type == 'inverse':
        return initial_lr / (1 + 0.1 * t)
    elif decay_type == 'step':
        decay_rate = 0.5
        decay_steps = 10
        return initial_lr * (decay_rate ** (t // decay_steps))
    else:
        return initial_lr

# 可视化不同衰减策略
initial_lr = 0.1
epochs = 100

schedules = ['exponential', 'inverse', 'step']

plt.figure(figsize=(12, 4))
for i, schedule in enumerate(schedules, 1):
    plt.subplot(1, 3, i)
    lr_history = [learning_rate_schedule(initial_lr, t, schedule) for t in range(epochs)]
    plt.plot(range(epochs), lr_history, label=schedule)
    plt.title(f"{schedule} decay")
    plt.xlabel("Epoch")
    plt.ylabel("Learning Rate")
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("不同衰减策略的极限:")
print(f"exponential: lim(t→∞) 0.1 * exp(-0.1t) = 0")
print(f"inverse: lim(t→∞) 0.1 / (1 + 0.1t) = 0")
print(f"step: lim(t→∞) 0.1 * 0.5^(t//10) = 0")
```

### 应用5：数值精度与极限

浮点数的精度限制实际上是对极限的数值近似。

```python
import numpy as np

def numerical_limits():
    """演示数值精度对极限计算的影响"""
    
    # 极限：lim(x→0) sin(x)/x = 1
    x_values = np.logspace(-1, -16, 16)
    ratios = []
    
    for x in x_values:
        ratio = np.sin(x) / x
        ratios.append(ratio)
    
    print("x值 vs sin(x)/x:")
    for x, ratio in zip(x_values, ratios):
        print(f"x = {x:.2e}: sin(x)/x = {ratio:.15f}")
    
    # 找到最佳近似
    best_idx = np.argmax(ratios)
    print(f"\n最佳近似: x = {x_values[best_idx]:.2e}, sin(x)/x = {ratios[best_idx]:.15f}")
    
    # 过小导致数值不稳定
    print(f"\n过小的x值导致数值不稳定:")
    print(f"x = {x_values[-1]:.2e}: sin(x)/x = {ratios[-1]:.15f}")

numerical_limits()
```

## 6. 易错点

⚠️ **常见错误**

1. **忽略极限的存在性**
   - 不是所有函数在所有点都有极限
   - 需要检查左右极限是否相等

2. **滥用洛必达法则**
   - 只适用于 0/0 或 ∞/∞ 型
   - 需要验证条件

3. **混淆极限和函数值**
   - lim(x→a) f(x) ≠ f(a)
   - 函数在该点可能无定义

✅ **最佳实践**

1. **先观察，再计算**
   - 先判断极限类型
   - 选择合适的方法

2. **使用多种方法验证**
   - 数值方法
   - 符号计算
   - 图形分析

3. **注意特殊情况**
   - 无穷大
   - 不存在
   - 振荡

## 7. 相关概念

- [[01_Real_Numbers]] - 实数理论（极限的基础）
- [[03_Continuity]] - 连续性（极限的应用）
- [[05_Derivatives]] - 导数（极限的推广）

## 自测（3问速测）

1. 我能用 $\varepsilon$-$\delta$ 语言复述“极限存在”吗？
2. 碰到 $1^\infty$ 型，我是否能稳定地用“取对数”转化？
3. 我能给出一个“左右极限不等所以极限不存在”的反例吗？

## 10. 总结

### 10.1 重要定义
1. 函数极限：当x趋近a时，f(x)趋近L
2. 数列极限：当n趋近无穷时，数列项趋近某个值
3. 左极限和右极限：从左侧或右侧趋近时的极限
4. 无穷小量：极限为0的量
5. 无穷大量：绝对值无限增大的量

### 10.2 重要定理
1. 极限的唯一性：如果极限存在，则极限值唯一
2. 极限的保号性：极限为正（负）则函数在该点附近也为正（负）
3. 极限的局部有界性：如果极限存在，函数在该点附近有界
4. 夹逼准则：如果两个函数夹逼第三个函数，则极限相同
5. 单调有界准则：单调有界数列必收敛
6. 柯西收敛准则：数列收敛的充要条件

### 10.3 重要证明
1. 极限唯一性的证明：假设两个极限，证明它们必须相等
2. 夹逼准则的证明：利用不等式传递性
3. 单调有界准则的证明：利用确界原理

### 10.4 重要性质
1. 极限的四则运算：和、差、积、商的极限性质
2. 无穷小的比较：高阶、同阶、等价无穷小
3. 极限的保号性：极限符号决定函数值符号
4. 复合函数的极限：链式法则

本章为后续学习相关章节奠定了基础。

## 11. 练习（分层）

本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 计算：lim(x→0) sin(x)/x（参考《高等数学 上册 第八版》第1章习题1-5第1题）
2. 计算：lim(x→∞) (1+1/x)^x（参考《高等数学 上册 第八版》第1章习题1-6第2题）
3. 计算：lim(x→0) (1-cosx)/x²（参考《数学分析(第5版) 上》第2章习题2-1第3题）
4. 计算：lim(x→∞) (2x³+3x²+5)/(3x³-4x²+2)（参考《高等数学 上册 第八版》第1章习题1-6第4题）
5. 证明：lim(x→a) f(x)=L的唯一性（参考《数学分析(第5版) 上》第2章定理2.1）

### B档（进阶）
1. 利用夹逼准则计算：lim(n→∞) (√(n²+n)-n)（参考《高等数学 上册 第八版》第1章习题1-8第2题）
2. 利用洛必达法则计算：lim(x→0) (e^x-1)/sin(x)（参考《高等数学 上册 第八版》第3章习题3-2第1题）
3. 证明：单调有界数列必收敛（参考《数学分析(第5版) 上》第2章定理2.4）
4. 证明：柯西收敛准则（参考《数学分析(第5版) 上》第2章定理2.5）
5. 证明：数列收敛则其子列收敛（参考《数学分析(第5版) 上》第2章习题2-5第2题）

### C档（挑战）
1. 研究：讨论lim(x→0) sin(1/x)的极限（参考《高等数学 上册 第八版》第1章习题1-9第6题）
2. 研究：讨论lim(x→0) x·sin(1/x)的极限（参考《高等数学 上册 第八版》第1章习题1-9第7题）
3. 应用：极限在神经网络初始化中的应用（参考《高等数学 下册 第八版》第12章微分方程）
4. 应用：极限在优化算法收敛性分析中的应用（参考《高等数学 下册 第八版）第14章重积分）
5. 应用：利用极限计算概率分布的期望和方差（参考《高等数学 下册第八版》第9章多元函数微分法应用）



