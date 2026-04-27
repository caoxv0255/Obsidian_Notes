---
type: concept

topic: continuity

category: calculus

difficulty: intermediate

prerequisites:
  - [[02_Limits]]

acm_relevant: false

created: 2026-03-09

status: complete

subject: calculus
chapter: 03
updated: 2026-04-27
---

# 连续性 (Continuity)

## 📌 学习目标

- 用三条件与 $\varepsilon$-$\delta$ 语言判断点连续
- 能找出间断点并完成分类（可去/跳跃/无穷/振荡）
- 熟练使用闭区间连续函数三大定理（介值/零点、最值、有界性）解决存在性问题

## ✅ 先修

- [[02_Limits]]
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层

- **基础**：连续定义与间断点分类；初等函数连续性
- **进阶**：介值/最值/有界性定理的使用与证明主线；一致连续的判断
- **拓展**：连续性在数值算法与机器学习（激活/损失）中的设计约束

## 高数/数分附件补充

### 高数题型补充（同济/托马斯）
- **拼接函数连续性**：先看分段点处左右极限，再核对函数值
- **零点存在题**：连续 + 端点异号，直接用零点定理
- **最值存在题**：闭区间连续函数先找区间内极值，再比端点

### 数分严谨补充（华师大/Rudin）
- **连续定义模板**：在点 $x_0$ 处连续等价于 $\varepsilon$-$\delta$ 语言下的极限与函数值相等
- **反例意识**：介值定理要求区间连续，若有跳跃间断则不能直接用

### 完整例题（可去间断点）
定义
$$
f(x)=
\begin{cases}
\frac{\sin x}{x}, & x\neq 0\\
1, & x=0
\end{cases}
$$
证明 $f$ 在 $x=0$ 连续。

解：
$$
\lim_{x\to 0}\frac{\sin x}{x}=1=f(0)
$$
故 $f$ 在 $0$ 连续。

**提示**：这类题在高数里常被当作“补定义使其连续”，在数分里则是标准的“极限-函数值一致性”练习。

## 1. 定义

**直观理解**：
连续性是函数的重要性质，描述了函数在某点附近没有"跳跃"或"断开"的现象。直观地说，如果函数图像可以一笔画成，那么这个函数就是连续的。

想象你在画一条曲线。如果你不需要抬起笔就能画出整条曲线，那么这条曲线就是连续的。如果你在某些点需要"跳过"一段，那么函数在这些点就不连续。

连续函数的图像是一个"完整的"图形，没有缺口或断裂。

## 2. 定理与性质

### 连续性的定义

#### 点连续性

函数 $f$ 在点 $x_0$ 处连续，如果满足以下条件：

1. $f(x_0)$ 存在（$x_0$ 在定义域内）
2. $\lim_{x \to x_0} f(x)$ 存在
3. $\lim_{x \to x_0} f(x) = f(x_0)$

用 $\varepsilon-\delta$ 语言表述：
$$\forall \varepsilon > 0, \exists \delta > 0, \text{使得 } |x - x_0| < \delta \implies |f(x) - f(x_0)| < \varepsilon$$

#### 区间连续性

函数 $f$ 在区间 $I$ 上连续，如果 $f$ 在 $I$ 内的每一点都连续。

### 连续性的类型

#### 1. 点连续

函数在某点 $x_0$ 处连续。

#### 2. 区间连续

函数在区间 $[a, b]$ 上连续：
- 在开区间 $(a, b)$ 内每点连续
- 在左端点 $a$ 右连续：$\lim_{x \to a^+} f(x) = f(a)$
- 在右端点 $b$ 左连续：$\lim_{x \to b^-} f(x) = f(b)$

### 连续函数的性质

#### 定理 1：连续函数的四则运算

如果 $f$ 和 $g$ 都在 $x_0$ 处连续，则：
1. $f \pm g$ 在 $x_0$ 处连续
2. $f \cdot g$ 在 $x_0$ 处连续
3. 如果 $g(x_0) \neq 0$，则 $\frac{f}{g}$ 在 $x_0$ 处连续

#### 定理 2：复合函数的连续性

如果 $f$ 在 $x_0$ 处连续，$g$ 在 $f(x_0)$ 处连续，则 $g \circ f$ 在 $x_0$ 处连续。

#### 定理 3：反函数的连续性

如果 $f$ 是严格单调的连续函数，则其反函数 $f^{-1}$ 也是连续的。

#### 定理 4：闭区间上连续函数的性质

**介值定理（中间值定理）**：
设 $f$ 在 $[a, b]$ 上连续，且 $f(a) \neq f(b)$。对于 $f(a)$ 和 $f(b)$ 之间的任何值 $\eta$，存在 $c \in (a, b)$，使得 $f(c) = \eta$。

**推论（零点定理）**：
设 $f$ 在 $[a, b]$ 上连续，且 $f(a) \cdot f(b) < 0$，则存在 $c \in (a, b)$，使得 $f(c) = 0$。

**最值定理**：
设 $f$ 在 $[a, b]$ 上连续，则 $f$ 在 $[a, b]$ 上必有最大值和最小值。

**有界性定理**：
设 $f$ 在 $[a, b]$ 上连续，则 $f$ 在 $[a, b]$ 上有界。

#### 定理 5：一致连续性

**定义**：函数 $f$ 在区间 $I$ 上一致连续，如果：
$$\forall \varepsilon > 0, \exists \delta > 0, \text{使得 } \forall x_1, x_2 \in I, |x_1 - x_2| < \delta \implies |f(x_1) - f(x_2)| < \varepsilon$$

**康托尔定理**：如果 $f$ 在闭区间 $[a, b]$ 上连续，则 $f$ 在 $[a, b]$ 上一致连续。

### 间断点

#### 第一类间断点（可去间断点）

$\lim_{x \to x_0} f(x)$ 存在，但 $\lim_{x \to x_0} f(x) \neq f(x_0)$ 或 $f(x_0)$ 无定义。

#### 第二类间断点（跳跃间断点）

$\lim_{x \to x_0^-} f(x)$ 和 $\lim_{x \to x_0^+} f(x)$ 都存在，但不相等。

#### 第三类间断点（无穷间断点、振荡间断点）

至少有一个单侧极限不存在（包括极限为无穷）。

### 基本初等函数的连续性

1. **常数函数**：$f(x) = c$ 在 $\mathbb{R}$ 上连续
2. **幂函数**：$f(x) = x^\alpha$ 在定义域内连续
3. **指数函数**：$f(x) = a^x$（$a > 0, a \neq 1$）在 $\mathbb{R}$ 上连续
4. **对数函数**：$f(x) = \log_a x$（$a > 0, a \neq 1$）在 $(0, +\infty)$ 上连续
5. **三角函数**：$\sin x, \cos x$ 在 $\mathbb{R}$ 上连续
6. **反三角函数**：$\arcsin x, \arccos x$ 在 $[-1, 1]$ 上连续，$\arctan x, \text{arccot } x$ 在 $\mathbb{R}$ 上连续

**初等函数**：由基本初等函数经过有限次四则运算和复合运算得到的函数，在其定义域内连续。

## 3. 代码示例

### 示例 1：验证连续性

```python
import numpy as np

def is_continuous_at(f, x0, epsilon=1e-6, delta_max=1.0):
    """
    数值验证函数在某点的连续性
    
    参数:
        f: 函数
        x0: 要验证的点
        epsilon: 允许的误差
        delta_max: 搜索的最大 delta
    """
    # 检查函数值是否存在
    try:
        f_x0 = f(x0)
    except:
        return False, "函数值不存在"
    
    # 检查极限是否存在
    h_values = np.logspace(-10, 0, 100)
    left_limits = [f(x0 - h) for h in h_values if x0 - h in np.linspace(-100, 100, 10001)]
    right_limits = [f(x0 + h) for h in h_values if x0 + h in np.linspace(-100, 100, 10001)]
    
    if len(left_limits) == 0 or len(right_limits) == 0:
        return False, "无法计算极限"
    
    left_limit = np.mean(left_limits)
    right_limit = np.mean(right_limits)
    
    # 检查极限是否相等
    if abs(left_limit - right_limit) > epsilon:
        return False, f"左极限({left_limit:.6f}) ≠ 右极限({right_limit:.6f})"
    
    # 检查极限是否等于函数值
    if abs(left_limit - f_x0) > epsilon:
        return False, f"极限({left_limit:.6f}) ≠ 函数值({f_x0:.6f})"
    
    return True, "连续"

# 测试函数
f1 = lambda x: x**2
f2 = lambda x: 1/x if x != 0 else 0
f3 = lambda x: np.sin(1/x) if x != 0 else 0
f4 = lambda x: np.sign(x) if x != 0 else 0

print("测试连续性：")
print(f"f(x) = x² 在 x=0: {is_continuous_at(f1, 0)}")
print(f"f(x) = 1/x (f(0)=0) 在 x=0: {is_continuous_at(f2, 0)}")
print(f"f(x) = sin(1/x) (f(0)=0) 在 x=0: {is_continuous_at(f3, 0)}")
print(f"f(x) = sign(x) (f(0)=0) 在 x=0: {is_continuous_at(f4, 0)}")
```

### 示例 2：介值定理

```python
import numpy as np

def intermediate_value_theorem(f, a, b, tolerance=1e-6, max_iter=1000):
    """
    使用介值定理寻找 f(x) = 0 的根
    
    参数:
        f: 函数
        a, b: 区间端点，满足 f(a)·f(b) < 0
        tolerance: 容差
        max_iter: 最大迭代次数
    """
    fa = f(a)
    fb = f(b)
    
    # 检查条件
    if fa * fb > 0:
        return None, "不满足 f(a)·f(b) < 0"
    
    # 二分法
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        
        if abs(fc) < tolerance or (b - a) / 2 < tolerance:
            return c, f"在 {i+1} 次迭代后收敛"
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    return c, "达到最大迭代次数"

# 示例 1：求解 x² - 2 = 0（即 √2）
f1 = lambda x: x**2 - 2
root1, msg1 = intermediate_value_theorem(f1, 0, 2)
print(f"√2 ≈ {root1:.6f} ({msg1})")

# 示例 2：求解 x³ - x - 1 = 0
f2 = lambda x: x**3 - x - 1
root2, msg2 = intermediate_value_theorem(f2, 1, 2)
print(f"x³ - x - 1 = 0 的根 ≈ {root2:.6f} ({msg2})")

# 示例 3：求解 cos(x) = x
f3 = lambda x: np.cos(x) - x
root3, msg3 = intermediate_value_theorem(f3, 0, np.pi/2)
print(f"cos(x) = x 的根 ≈ {root3:.6f} ({msg3})")
```

### 示例 3：最值定理

```python
import numpy as np

def find_extrema(f, a, b, n=10000):
    """
    寻找函数在闭区间上的最大值和最小值
    
    参数:
        f: 函数
        a, b: 区间端点
        n: 采样点数
    """
    x = np.linspace(a, b, n)
    y = f(x)
    
    max_val = np.max(y)
    min_val = np.min(y)
    
    max_x = x[np.argmax(y)]
    min_x = x[np.argmin(y)]
    
    return (max_x, max_val), (min_x, min_val)

# 示例 1：f(x) = x² - 4x + 3
f1 = lambda x: x**2 - 4*x + 3
max1, min1 = find_extrema(f1, 0, 4)
print(f"f(x) = x² - 4x + 3 在 [0, 4] 上：")
print(f"最大值：{max1[1]:.6f} 在 x = {max1[0]:.6f}")
print(f"最小值：{min1[1]:.6f} 在 x = {min1[0]:.6f}")

# 示例 2：f(x) = sin(x) + cos(x)
f2 = lambda x: np.sin(x) + np.cos(x)
max2, min2 = find_extrema(f2, 0, 2*np.pi)
print(f"\nf(x) = sin(x) + cos(x) 在 [0, 2π] 上：")
print(f"最大值：{max2[1]:.6f} 在 x = {max2[0]:.6f}")
print(f"最小值：{min2[1]:.6f} 在 x = {min2[0]:.6f}")

# 示例 3：f(x) = x³ - 3x
f3 = lambda x: x**3 - 3*x
max3, min3 = find_extrema(f3, -2, 2)
print(f"\nf(x) = x³ - 3x 在 [-2, 2] 上：")
print(f"最大值：{max3[1]:.6f} 在 x = {max3[0]:.6f}")
print(f"最小值：{min3[1]:.6f} 在 x = {min3[0]:.6f}")
```

### 示例 4：一致连续性

```python
import numpy as np

def check_uniform_continuity(f, a, b, epsilon=1e-6):
    """
    数值检查函数在区间上的一致连续性
    
    参数:
        f: 函数
        a, b: 区间端点
        epsilon: 误差容限
    """
    # 生成采样点
    n = 1000
    x = np.linspace(a, b, n)
    
    # 寻找满足条件的 delta
    delta = b - a
    
    for d in np.logspace(-10, 0, 100):
        satisfied = True
        
        for i in range(n):
            for j in range(i+1, n):
                if abs(x[i] - x[j]) < d and abs(f(x[i]) - f(x[j])) >= epsilon:
                    satisfied = False
                    break
            if not satisfied:
                break
        
        if satisfied:
            delta = d
            break
    
    return delta

# 测试函数
f1 = lambda x: x**2  # 在闭区间上一致连续
f2 = lambda x: 1/x if x != 0 else 0  # 在包含 0 的区间上不一致连续
f3 = lambda x: np.sin(1/x) if x != 0 else 0  # 在包含 0 的区间上不一致连续

print("测试一致连续性：")
delta1 = check_uniform_continuity(f1, 0, 1)
print(f"f(x) = x² 在 [0, 1] 上，delta ≈ {delta1:.2e}")

delta2 = check_uniform_continuity(f1, 0, 10)
print(f"f(x) = x² 在 [0, 10] 上，delta ≈ {delta2:.2e}")

# 注意：数值方法难以准确检测不一致连续性
```

### 示例 5：间断点分析

```python
import numpy as np

def classify_discontinuity(f, x0):
    """
    分类函数的间断点
    
    参数:
        f: 函数
        x0: 要分析的点
    """
    # 计算左右极限
    h_values = np.logspace(-10, -1, 100)
    
    try:
        left_limits = [f(x0 - h) for h in h_values]
        left_limit = np.mean(left_limits)
    except:
        left_limit = None
    
    try:
        right_limits = [f(x0 + h) for h in h_values]
        right_limit = np.mean(right_limits)
    except:
        right_limit = None
    
    # 检查函数值
    try:
        f_x0 = f(x0)
    except:
        f_x0 = None
    
    # 分类
    if left_limit is None or right_limit is None:
        return "第三类间断点（至少一个单侧极限不存在）"
    
    if abs(left_limit - right_limit) < 1e-6:
        if f_x0 is None or abs(left_limit - f_x0) > 1e-6:
            return "第一类间断点（可去间断点）"
        else:
            return "连续"
    else:
        return "第二类间断点（跳跃间断点）"

# 测试函数
f1 = lambda x: x**2
f2 = lambda x: (x**2 - 1) / (x - 1) if x != 1 else 0  # 可去间断点
f3 = lambda x: np.sign(x) if x != 0 else 0  # 跳跃间断点
f4 = lambda x: 1/x if x != 0 else 0  # 无穷间断点

print("间断点分类：")
print(f"f(x) = x² 在 x=1: {classify_discontinuity(f1, 1)}")
print(f"f(x) = (x²-1)/(x-1) (f(1)=0) 在 x=1: {classify_discontinuity(f2, 1)}")
print(f"f(x) = sign(x) (f(0)=0) 在 x=0: {classify_discontinuity(f3, 0)}")
print(f"f(x) = 1/x (f(0)=0) 在 x=0: {classify_discontinuity(f4, 0)}")
```

## 4. 机器学习应用

### 应用 1：激活函数的连续性

神经网络的激活函数通常是连续的，这保证了网络的可微性和梯度下降的有效性。

```python
import numpy as np

def activation_continuity(activation, x_range=(-5, 5), n=1000):
    """检查激活函数的连续性"""
    x = np.linspace(x_range[0], x_range[1], n)
    y = activation(x)
    
    # 检查是否有跳跃
    jumps = []
    for i in range(1, n):
        if abs(y[i] - y[i-1]) > 0.5:  # 较大的跳跃
            jumps.append((x[i-1], x[i], y[i-1], y[i]))
    
    return jumps

# 测试常用激活函数
sigmoid = lambda x: 1 / (1 + np.exp(-x))
relu = lambda x: np.maximum(0, x)
tanh = lambda x: np.tanh(x)
leaky_relu = lambda x: np.where(x > 0, x, 0.01 * x)

print("激活函数连续性检查：")

for name, func in [("Sigmoid", sigmoid), ("ReLU", relu), ("Tanh", tanh), ("Leaky ReLU", leaky_relu)]:
    jumps = activation_continuity(func)
    if len(jumps) == 0:
        print(f"{name}: 连续")
    else:
        print(f"{name}: 发现 {len(jumps)} 个跳跃点")
```

### 应用 2：损失函数的连续性

损失函数应该是连续的，以便能够使用梯度下降等优化算法。

```python
import numpy as np

def loss_function_continuity(loss_func, y_true, y_pred_range):
    """检查损失函数的连续性"""
    y_pred = np.linspace(y_pred_range[0], y_pred_range[1], 1000)
    losses = [loss_func(y_true, yp) for yp in y_pred]
    
    # 检查损失函数的变化
    changes = [abs(losses[i+1] - losses[i]) for i in range(len(losses)-1)]
    max_change = max(changes)
    
    return max_change

# 测试损失函数
mse_loss = lambda yt, yp: (yt - yp)**2
mae_loss = lambda yt, yp: abs(yt - yp)
huber_loss = lambda yt, yp: np.where(abs(yt-yp) <= 1, 0.5*(yt-yp)**2, abs(yt-yp)-0.5)

print("损失函数连续性检查：")

for name, func in [("MSE", mse_loss), ("MAE", mae_loss), ("Huber", huber_loss)]:
    max_change = loss_function_continuity(func, 0.5, (-2, 2))
    print(f"{name}: 最大变化 = {max_change:.6f}")
```

## 根据题型整理的做题方法

### 连续性问题的分析框架

#### 📋 第一步：识别问题类型

| 问题类型 | 特点 | 主要方法 |
|---------|------|---------|
| **连续性判断** | 判断函数在某点/区间是否连续 | 定义法、极限法 |
| **间断点分类** | 找出并分类间断点 | 分析左右极限 |
| **证明题** | 证明存在性、介值性等 | 闭区间连续函数性质 |
| **方程根的存在性** | 证明方程有解 | 零点定理 |

#### 🔧 第二步：选择分析方法

```
连续性问题
    │
    ├── 判断点连续？
    │       ├── 定义法 → 验证三条件
    │       └── 极限法 → lim f(x) = f(x₀)
    │
    ├── 判断区间连续？
    │       └── 初等函数 → 定义域内连续
    │
    ├── 找间断点？
    │       └── 分析无定义点、分段点
    │           ├── 左右极限相等 → 可去间断点
    │           ├── 左右极限存在但不等 → 跳跃间断点
    │           └── 至少一个极限不存在 → 其他间断点
    │
    └── 证明存在性问题？
            ├── 根的存在 → 零点定理
            ├── 中间值 → 介值定理
            └── 最值 → 最值定理
```

### 💡 核心技巧与常用结论

#### 1. 连续性判断的三个条件

函数 $f$ 在 $x_0$ 处连续 $\Leftrightarrow$ 以下三条件同时满足：
1. $f(x_0)$ 存在
2. $\lim_{x \to x_0} f(x)$ 存在
3. $\lim_{x \to x_0} f(x) = f(x_0)$

**判断流程**：
```
x₀ 是否在定义域内？
    ↓ 是
lim(x→x₀) f(x) 是否存在？
    ↓ 是
极限值是否等于函数值？
    ↓ 是
→ 连续
```

#### 2. 间断点分类速查表

| 类型 | 左极限 | 右极限 | 特点 | 例子 |
|-----|-------|-------|------|-----|
| **可去间断点** | 存在且相等 | 存在且相等 | 极限存在但≠函数值 | $f(x)=\frac{x^2-1}{x-1}, x=1$ |
| **跳跃间断点** | 存在 | 存在 | 左右极限不相等 | $f(x)=\text{sgn}(x), x=0$ |
| **无穷间断点** | ∞ 或 -∞ | - | 至少一侧为无穷 | $f(x)=\frac{1}{x}, x=0$ |
| **振荡间断点** | 不存在 | - | 极限振荡 | $f(x)=\sin\frac{1}{x}, x=0$ |

**第一类间断点**：左右极限都存在
**第二类间断点**：至少一个单侧极限不存在

#### 3. 闭区间连续函数三大定理

**零点定理**：$f(a) \cdot f(b) < 0 \Rightarrow \exists c \in (a,b), f(c) = 0$

**介值定理**：$f$ 连续，$\eta$ 介于 $f(a), f(b)$ 之间 $\Rightarrow \exists c, f(c) = \eta$

**最值定理**：$f$ 在 $[a,b]$ 上连续 $\Rightarrow f$ 在 $[a,b]$ 上有最大值和最小值

#### 4. 一致连续的判断

**定义**：$\forall \varepsilon > 0, \exists \delta > 0$，对任意 $x_1, x_2 \in I$，若 $|x_1 - x_2| < \delta$，则 $|f(x_1) - f(x_2)| < \varepsilon$

**重要结论**：
- 闭区间上连续 $\Rightarrow$ 一致连续（康托尔定理）
- 开区间上连续 $\not\Rightarrow$ 一致连续

**例子**：
- $f(x) = x^2$ 在 $[0,1]$ 上一致连续，在 $[0,+\infty)$ 上不一致连续
- $f(x) = \frac{1}{x}$ 在 $(0,1)$ 上不一致连续

#### 5. 方程根存在性的证明方法

**步骤**：
1. 构造函数 $f(x)$（将方程移项）
2. 找区间 $[a,b]$
3. 验证 $f$ 在 $[a,b]$ 上连续
4. 验证 $f(a) \cdot f(b) < 0$
5. 由零点定理，存在 $c \in (a,b)$ 使 $f(c) = 0$

**经典例子**：证明 $x^3 + x - 1 = 0$ 在 $(0,1)$ 内有根
- 设 $f(x) = x^3 + x - 1$
- $f(0) = -1 < 0$，$f(1) = 1 > 0$
- $f$ 在 $[0,1]$ 上连续
- 由零点定理，存在 $c \in (0,1)$ 使 $f(c) = 0$

### 🎯 题型分类与对策

| 题型 | 关键技巧 | 典型问题 |
|-----|---------|---------|
| 连续性判断 | 验证三条件 | 判断分段函数在分界点的连续性 |
| 间断点分类 | 分析左右极限 | 求 $f(x) = \frac{\sin x}{x}$ 的间断点 |
| 证明根存在 | 零点定理 | 证明方程有解 |
| 证明中间值 | 介值定理 | 证明 $f$ 取到某值 |
| 证明有界/有最值 | 最值定理 | 证明函数在闭区间上有界 |

### ⚠️ 常见错误与陷阱

**错误一**：混淆连续与可导
- 连续不一定可导，如 $|x|$ 在 $x=0$ 处连续但不可导
- 可导必连续

**错误二**：忽略函数定义域
- 判断连续性前必须确认点在定义域内
- 如 $\ln x$ 在 $x=0$ 处不讨论连续性（不在定义域内）

**错误三**：零点定理使用不当
- 必须验证 $f(a) \cdot f(b) < 0$
- 必须确认函数在闭区间上连续

## 5. 易错点

⚠️ **常见错误**

1. **混淆连续与可导**
   - 连续不一定可导（如 $|x|$ 在 $x=0$）
   - 可导必连续

2. **忽略端点连续性**
   - 在闭区间端点只需要单侧连续
   - 左端点右连续，右端点左连续

3. **混淆点连续与一致连续**
   - 点连续是局部性质
   - 一致连续是全局性质
   - 在闭区间上连续必一致连续

✅ **最佳实践**

1. **理解连续性的直观意义**
   - 图像没有断开
   - 可以一笔画成

2. **掌握重要定理**
   - 介值定理、最值定理、有界性定理
   - 这些定理在证明和应用中非常重要

3. **注意间断点的分类**
   - 不同类型的间断点有不同的处理方法
   - 可去间断点可以通过重新定义函数值来消除

## 6. 相关概念

- [[01_Real_Numbers]] - 实数理论
- [[02_Limits]] - 极限
- [[05_Derivatives]] - 导数
- [[04_Uniform_Continuity]] - 一致连续性

## 自测（3问速测）

1. 点连续的“三条件”分别是什么？我能用一句话把它们串起来吗？
2. 给定一个分段函数，我能系统地算左右极限并完成间断点分类吗？
3. 使用零点定理时，我是否每次都检查“闭区间连续 + 端点异号”？

## 10. 总结

### 10.1 重要定义
1. 函数连续：lim(x→a)f(x)=f(a)
2. 间断点：函数不连续的点
3. 一致连续：在整个区间上连续程度一致
4. 连续函数的性质：有界性、介值性、最值性

### 10.2 重要定理
1. 连续函数的四则运算：连续函数的和、差、积、商（分母不为零）仍是连续的
2. 复合函数的连续性：连续函数的复合函数是连续的
3. 介值定理：连续函数在区间上取遍所有中间值
4. 最值定理：连续函数在闭区间上必有最大值和最小值
5. Cantor定理：闭区间上的连续函数一定一致连续

### 10.3 重要证明
1. 复合函数连续性的证明：利用极限的链式法则
2. 介值定理的证明：利用确界原理和中间值性质
3. 最值定理的证明：利用有界性和确界原理

### 10.4 重要性质
1. 连续函数的有界性：闭区间上的连续函数有界
2. 连续函数的介值性：取遍所有中间值
3. 连续函数的最值性：必有最大最小值
4. 连续函数的运算性质：和、差、积、商保持连续性

本章为后续学习相关章节奠定了基础。

## 11. 练习（分层）

本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 判断：下列函数在指定点的连续性（参考《高等数学 上册 第八版》第1章习题1-8第1题）
2. 求：函数f(x)=x²+1的间断点（参考《高等数学 上册 第八版》第1章习题1-9第2题）
3. 证明：若f在[a,b]上连续且f(a)<0<f(b)，则存在c使得f(c)=0（参考《数学分析(第5版) 上》第3章定理3.7介值定理）
4. 证明：初等函数在其定义域内连续（参考《高等数学 上册 第八版》第1章习题1-10）
5. 求：函数f(x)=sin(x)/x在x=0处的连续性（参考《高等数学 上册 第八版》第1章习题1-8第3题）

### B档（进阶）
1. 证明：闭区间上的连续函数必有最大值和最小值（参考《数学分析(第5版) 上》第3章定理3.8最值定理）
2. 证明：连续函数的复合函数是连续的（参考《数学分析(第5版) 上》第3章定理3.5）
3. 证明：一致连续的函数必连续（参考《数学分析(第5版) 上》第3章习题3-4第4题）
4. 证明：连续函数的和、差、积、商（分母不为零）是连续的（参考《高等数学 上册 第八版》第1章第8节）
5. 应用：连续性在神经网络激活函数中的应用（参考《高等数学 下册 第八版》第1章第10节）

### C档（挑战）
1. 研究：分段函数的连续性判断方法（参考《高等数学 上册 第八版》第1章习题1-9第5题）
2. 研究：一致连续与连续的区别和联系（参考《数学分析(第5版) 上》第3章习题3-5第6题）
3. 应用：连续性在损失函数设计中的应用（参考《高等数学 下册 第八版》第9章多元函数微分法应用）
4. 应用：利用介值定理证明方程根的存在性（参考《高等数学 上册 第八版》第1章习题1-11第3题）
5. 应用：连续性在数值分析中的应用（参考《高等数学 下册 第八版》第3章微分方程数值解）




