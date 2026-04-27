---
type: concept
topic: indefinite_integrals
category: calculus
difficulty: intermediate
prerequisites:
  - [[05_Derivatives]]
acm_relevant: true
created: 2026-03-09
status: complete
subject: calculus
chapter: 09
updated: 2026-04-27
---

# 不定积分 (Indefinite Integrals)

## 📌 学习目标

- 掌握不定积分与原函数的关系及其存在性
- 熟练选择换元、分部积分、部分分式、三角换元等方法
- 能检查积分结果并识别常见积分结构

## ✅ 先修

- [[05_Derivatives]]
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层

- **基础**：基本积分公式与直接积分
- **进阶**：换元积分、分部积分、部分分式分解
- **拓展**：三角换元、数值积分与积分建模

## 高数/数分附件补充

### 高数题型补充（同济/吉米多维奇）
- **换元识别**：看到“复合函数 × 导数”优先想换元
- **分部积分**：对数 × 幂函数、反三角 × 幂函数、指数 × 幂函数
- **部分分式**：有理函数先化为真分式再拆分

### 数分严谨补充（华师大/Rudin）
- **原函数观念**：不定积分不是“一个数”，而是原函数全体
- **回代检查**：每次算完都对结果求导验算，是最可靠的自检方式

### 完整例题（换元法）
计算
$$
\int \frac{2x+1}{x^2+x+1}\,dx
$$

解：令
$$
u=x^2+x+1,
\quad du=(2x+1)dx
$$
则
$$
\int \frac{2x+1}{x^2+x+1}\,dx
=\int \frac{1}{u}\,du
=\ln|u|+C
=\ln(x^2+x+1)+C
$$

**检验**：对结果求导，正好回到原 integrand。

## 1. 定义

**直观理解**：
不定积分是导数的逆运算。如果 $F'(x) = f(x)$，则称 $F(x)$ 是 $f(x)$ 的一个原函数，所有原函数的集合就是不定积分：

$$\int f(x) dx = F(x) + C$$

其中 $C$ 是任意常数。

不定积分就像"逆向工程"：给定变化率（导数），求原函数。

**类比**：
- 导数：知道位置，求速度
- 不定积分：知道速度，求位置

由于位置可以任意平移（加常数），所以不定积分包含一个常数项 $C$。

## 2. 定理与性质

### 原函数的存在性

#### 定理：原函数存在定理

如果 $f$ 在区间 $I$ 上连续，则 $f$ 在 $I$ 上存在原函数。

**证明**：
定义 $F(x) = \int_a^x f(t) dt$，其中 $a \in I$ 是固定点。

根据微积分基本定理：
$$F'(x) = \frac{d}{dx} \int_a^x f(t) dt = f(x)$$

因此 $F(x)$ 是 $f(x)$ 的原函数。

### 不定积分的基本性质

#### 性质1：线性性

$$\int [c \cdot f(x) + d \cdot g(x)] dx = c \int f(x) dx + d \int g(x) dx$$

#### 性质2：常数因子

$$\int c \cdot f(x) dx = c \int f(x) dx$$

#### 性质3：导数与积分互逆

$$\frac{d}{dx} \int f(x) dx = f(x)$$
$$\int f'(x) dx = f(x) + C$$

### 基本积分公式

#### 幂函数

$$\int x^n dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)$$
$$\int \frac{1}{x} dx = \ln|x| + C$$

#### 指数函数

$$\int e^x dx = e^x + C$$
$$\int a^x dx = \frac{a^x}{\ln a} + C \quad (a > 0, a \neq 1)$$

#### 三角函数

$$\int \sin x dx = -\cos x + C$$
$$\int \cos x dx = \sin x + C$$
$$\int \sec^2 x dx = \tan x + C$$
$$\int \csc^2 x dx = -\cot x + C$$
$$\int \sec x \tan x dx = \sec x + C$$
$$\int \csc x \cot x dx = -\csc x + C$$

#### 反三角函数

$$\int \frac{1}{\sqrt{1 - x^2}} dx = \arcsin x + C$$
$$\int \frac{1}{1 + x^2} dx = \arctan x + C$$
$$\int \frac{1}{|x|\sqrt{x^2 - 1}} dx = \text{arcsec}|x| + C$$

### 积分方法

#### 方法1：换元积分法（第一类换元法）

**公式**：$\int f(g(x)) \cdot g'(x) dx = \int f(u) du$，其中 $u = g(x)$

**步骤**：
1. 选择合适的换元 $u = g(x)$
2. 计算 $du = g'(x) dx$
3. 将积分转换为 $\int f(u) du$
4. 计算积分
5. 将 $u$ 换回 $g(x)$

**示例1**：$\int 2x \cos(x^2) dx$

**解**：
设 $u = x^2$，则 $du = 2x dx$

$$\int 2x \cos(x^2) dx = \int \cos u du = \sin u + C = \sin(x^2) + C$$

**示例2**：$\int \tan x dx$

**解**：
$$\int \tan x dx = \int \frac{\sin x}{\cos x} dx$$

设 $u = \cos x$，则 $du = -\sin x dx$

$$\int \frac{\sin x}{\cos x} dx = -\int \frac{1}{u} du = -\ln|u| + C = -\ln|\cos x| + C$$

#### 方法2：分部积分法

**公式**：$\int u dv = uv - \int v du$

**步骤**：
1. 选择 $u$ 和 $dv$
2. 计算 $du = u' dx$ 和 $v = \int dv$
3. 应用分部积分公式
4. 计算剩余积分

**示例1**：$\int x e^x dx$

**解**：
设 $u = x$，$dv = e^x dx$
则 $du = dx$，$v = e^x$

$$\int x e^x dx = x e^x - \int e^x dx = x e^x - e^x + C = e^x(x - 1) + C$$

**示例2**：$\int x^2 \ln x dx$

**解**：
设 $u = \ln x$，$dv = x^2 dx$
则 $du = \frac{1}{x} dx$，$v = \frac{x^3}{3}$

$$\int x^2 \ln x dx = \frac{x^3}{3} \ln x - \int \frac{x^3}{3} \cdot \frac{1}{x} dx$$
$$= \frac{x^3}{3} \ln x - \frac{1}{3} \int x^2 dx$$
$$= \frac{x^3}{3} \ln x - \frac{1}{3} \cdot \frac{x^3}{3} + C$$
$$= \frac{x^3}{3} \ln x - \frac{x^3}{9} + C$$

#### 方法3：三角换元法

**三种标准形式**：

1. **$\sqrt{a^2 - x^2}$ 形式**：设 $x = a \sin \theta$

**示例**：$\int \sqrt{a^2 - x^2} dx$

**解**：
设 $x = a \sin \theta$，则 $dx = a \cos \theta d\theta$

$$\int \sqrt{a^2 - x^2} dx = \int \sqrt{a^2 - a^2 \sin^2 \theta} \cdot a \cos \theta d\theta$$
$$= \int a \cos \theta \cdot a \cos \theta d\theta = a^2 \int \cos^2 \theta d\theta$$
$$= a^2 \int \frac{1 + \cos 2\theta}{2} d\theta$$
$$= \frac{a^2}{2} \left(\theta + \frac{\sin 2\theta}{2}\right) + C$$

换回 $x$：
$$\theta = \arcsin\left(\frac{x}{a}\right)$$
$$\sin 2\theta = 2 \sin \theta \cos \theta = 2 \cdot \frac{x}{a} \cdot \frac{\sqrt{a^2 - x^2}}{a} = \frac{2x\sqrt{a^2 - x^2}}{a^2}$$

因此：
$$\int \sqrt{a^2 - x^2} dx = \frac{a^2}{2} \arcsin\left(\frac{x}{a}\right) + \frac{x\sqrt{a^2 - x^2}}{2} + C$$

2. **$\sqrt{a^2 + x^2}$ 形式**：设 $x = a \tan \theta$

3. **$\sqrt{x^2 - a^2}$ 形式**：设 $x = a \sec \theta$

#### 方法4：部分分式分解

**适用**：有理函数积分 $\int \frac{P(x)}{Q(x)} dx$

**步骤**：
1. 如果 $\deg(P) \geq \deg(Q)$，先做多项式除法
2. 分解 $Q(x)$ 为不可约因式
3. 将 $\frac{P(x)}{Q(x)}$ 分解为部分分式
4. 逐项积分

**示例**：$\int \frac{x + 3}{x^2 - 5x + 6} dx$

**解**：
分解分母：$x^2 - 5x + 6 = (x - 2)(x - 3)$

设 $\frac{x + 3}{(x - 2)(x - 3)} = \frac{A}{x - 2} + \frac{B}{x - 3}$

$$x + 3 = A(x - 3) + B(x - 2) = (A + B)x - (3A + 2B)$$

比较系数：
$$A + B = 1$$
$$-3A - 2B = 3$$

解得：$A = -5$，$B = 6$

因此：
$$\int \frac{x + 3}{x^2 - 5x + 6} dx = \int \left(\frac{-5}{x - 2} + \frac{6}{x - 3}\right) dx$$
$$= -5 \ln|x - 2| + 6 \ln|x - 3| + C$$

## 机器学习中的应用

### 1. 损失函数的推导

#### 对数损失（Log Loss）

对于二分类问题，预测概率为 $\hat{y}$，真实标签为 $y \in \{0, 1\}$：

$$\text{Log Loss} = -[y \ln \hat{y} + (1 - y) \ln(1 - \hat{y})]$$

通过求导（使用链式法则）得到梯度：
$$\frac{\partial \text{Loss}}{\partial \hat{y}} = -\left[\frac{y}{\hat{y}} - \frac{1 - y}{1 - \hat{y}}\right] = \frac{\hat{y} - y}{\hat{y}(1 - \hat{y})}$$

#### 交叉熵损失

对于多分类问题：
$$\text{Cross Entropy} = -\sum_{i=1}^n y_i \ln \hat{y}_i$$

### 2. 概率分布的归一化

#### Softmax函数

$$\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}$$

**Softmax的性质**：
- 所有输出值都在 $(0, 1)$ 之间
- 输出值之和为 1（归一化）
- 是指数函数的积分形式

#### Softmax的导数

$$\frac{\partial \text{softmax}(z_i)}{\partial z_j} = \begin{cases}
\text{softmax}(z_i)(1 - \text{softmax}(z_i)), & i = j \\
-\text{softmax}(z_i)\text{softmax}(z_j), & i \neq j
\end{cases}$$

### 3. 梯度的计算

#### 简单神经网络的梯度

```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

# 前向传播
def forward(X, W1, b1, W2, b2):
    z1 = X @ W1 + b1
    a1 = sigmoid(z1)
    z2 = a1 @ W2 + b2
    a2 = sigmoid(z2)
    return a2, a1, z1, z2

# 反向传播（使用链式法则）
def backward(X, y, a2, a1, z1, W1, W2):
    m = X.shape[0]

    # 输出层梯度
    dz2 = a2 - y
    dW2 = (a1.T @ dz2) / m
    db2 = np.sum(dz2, axis=0, keepdims=True) / m

    # 隐藏层梯度（链式法则）
    da1 = dz2 @ W2.T
    dz1 = da1 * sigmoid_derivative(z1)
    dW1 = (X.T @ dz1) / m
    db1 = np.sum(dz1, axis=0, keepdims=True) / m

    return dW1, db1, dW2, db2

# 示例
np.random.seed(42)
X = np.random.randn(100, 2)
y = np.random.randint(0, 2, (100, 1))

# 初始化参数
W1 = np.random.randn(2, 3)
b1 = np.zeros((1, 3))
W2 = np.random.randn(3, 1)
b2 = np.zeros((1, 1))

# 前向和反向传播
a2, a1, z1, z2 = forward(X, W1, b1, W2, b2)
dW1, db1, dW2, db2 = backward(X, y, a2, a1, z1, W1, W2)

print("输出层梯度 dW2:", dW2.T)
print("隐藏层梯度 dW1:", dW1.T)
```

## 根据题型整理的做题方法
### 积分方法选择的决策树

遇到不定积分，按以下流程选择方法。

#### 🔍 第一步：观察被积函数结构

首先分析被积函数 $f(x)$ 的结构特点：

| 函数类型 | 特点 | 首选方法 |
|---------|------|---------|
| **基本函数** | 可直接套公式 | 直接积分 |
| **复合函数** | 外层函数可积 | 凑微分法 |
| **乘积形式** | 两类函数相乘 | 分部积分法 |
| **有理函数** | $\frac{P(x)}{Q(x)}$ | 部分分式分解 |
| **含根式** | $\sqrt{a^2 \pm x^2}$ 等 | 三角换元 |
| **三角有理式** | $\sin x, \cos x$ 的有理式 | 万能公式或恒等变形 |

#### 📊 第二步：选择积分策略

```
被积函数分析
    │
    ├── 能直接套公式？
    │       └── 是 → 直接积分
    │
    ├── 含复合结构？
    │       └── 是 → 尝试凑微分法
    │           └── 设 u = 内层函数
    │
    ├── 是乘积形式？
    │       └── 是 → 分部积分法
    │           └── u 和 dv 的选择很关键
    │
    ├── 含根式？
    │       └── 是 → 三角换元
    │           ├── √(a²-x²) → x = a sinθ
    │           ├── √(a²+x²) → x = a tanθ
    │           └── √(x²-a²) → x = a secθ
    │
    └── 有理函数？
            └── 是 → 部分分式分解
```

#### ✏️ 第三步：执行计算

注意事项：
1. **凑微分法**：要凑成 $\int f(g(x))g'(x)dx$ 的形式
2. **分部积分**：$u$ 的选择遵循"反、对、幂、指、三"优先顺序
3. **三角换元**：注意换回原变量时画辅助三角形
4. **部分分式**：注意分母因式分解要完全

#### ✅ 第四步：验证结果

- 对结果求导，应等于被积函数
- 化简结果，避免繁琐形式

### 💡 核心技巧与常用结论

#### 1. 基本积分公式速查表

**必须熟记**，是所有积分方法的基础：

| 被积函数 $f(x)$ | 积分结果 $F(x) + C$ |
|----------------|-------------------|
| $x^n$ $(n \neq -1)$ | $\frac{x^{n+1}}{n+1}$ |
| $\frac{1}{x}$ | $\ln\|x\|$ |
| $e^x$ | $e^x$ |
| $a^x$ | $\frac{a^x}{\ln a}$ |
| $\sin x$ | $-\cos x$ |
| $\cos x$ | $\sin x$ |
| $\sec^2 x$ | $\tan x$ |
| $\csc^2 x$ | $-\cot x$ |
| $\frac{1}{\sqrt{1-x^2}}$ | $\arcsin x$ |
| $\frac{1}{1+x^2}$ | $\arctan x$ |
| $\frac{1}{\sqrt{x^2+a^2}}$ | $\ln(x + \sqrt{x^2+a^2})$ |
| $\frac{1}{\sqrt{x^2-a^2}}$ | $\ln\|x + \sqrt{x^2-a^2}\|$ |

#### 2. 凑微分法（第一类换元法）常用模式

**核心思想**：将被积表达式凑成 $f(g(x)) \cdot g'(x) dx$ 的形式

| 被积函数特征 | 凑微分方式 | 设 $u = $ |
|-------------|-----------|----------|
| $f(ax+b)$ | $dx = \frac{1}{a}d(ax+b)$ | $ax+b$ |
| $f(x^n) \cdot x^{n-1}$ | $x^{n-1}dx = \frac{1}{n}d(x^n)$ | $x^n$ |
| $f(e^x) \cdot e^x$ | $e^x dx = d(e^x)$ | $e^x$ |
| $f(\ln x) \cdot \frac{1}{x}$ | $\frac{1}{x}dx = d(\ln x)$ | $\ln x$ |
| $f(\sin x) \cdot \cos x$ | $\cos x dx = d(\sin x)$ | $\sin x$ |
| $f(\cos x) \cdot \sin x$ | $\sin x dx = -d(\cos x)$ | $\cos x$ |
| $f(\tan x) \cdot \sec^2 x$ | $\sec^2 x dx = d(\tan x)$ | $\tan x$ |
| $f(\arcsin x) \cdot \frac{1}{\sqrt{1-x^2}}$ | $\frac{dx}{\sqrt{1-x^2}} = d(\arcsin x)$ | $\arcsin x$ |
| $f(\arctan x) \cdot \frac{1}{1+x^2}$ | $\frac{dx}{1+x^2} = d(\arctan x)$ | $\arctan x$ |

**技巧**：观察被积函数中是否有某部分的导数作为因子出现。

#### 3. 分部积分法 —— u 的选择口诀

**口诀："反、对、幂、指、三"**

选择 $u$ 的优先级从高到低：

| 优先级 | 函数类型 | 说明 |
|-------|---------|------|
| 1 | **反三角函数** | $\arcsin x, \arctan x$ 等 |
| 2 | **对数函数** | $\ln x, \log_a x$ |
| 3 | **幂函数** | $x^n$ |
| 4 | **指数函数** | $e^x, a^x$ |
| 5 | **三角函数** | $\sin x, \cos x$ |

**原则**：选 $u$ 优先级高的，剩余部分作为 $dv$

**示例**：
- $\int x e^x dx$：$u = x$（幂），$dv = e^x dx$
- $\int x \ln x dx$：$u = \ln x$（对），$dv = x dx$
- $\int e^x \sin x dx$：$u = \sin x$ 或 $e^x$ 均可，需两次分部积分

#### 4. 三角换元的标准形式

| 根式形式 | 换元方式 | 恒等式 |
|---------|---------|-------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $1 - \sin^2\theta = \cos^2\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $1 + \tan^2\theta = \sec^2\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\sec^2\theta - 1 = \tan^2\theta$ |

**注意事项**：
- 换元后注意 $dx$ 也要变换
- 积分完成后要用辅助三角形换回原变量
- 定义域和角度范围要一致

#### 5. 部分分式分解的标准形式

**分母的因式与分解形式**：

| 分母因式 | 分解形式 |
|---------|---------|
| $(x-a)$ | $\frac{A}{x-a}$ |
| $(x-a)^n$ | $\frac{A_1}{x-a} + \frac{A_2}{(x-a)^2} + \cdots + \frac{A_n}{(x-a)^n}$ |
| $(x^2+px+q)$（不可约） | $\frac{Ax+B}{x^2+px+q}$ |
| $(x^2+px+q)^n$ | $\frac{A_1x+B_1}{x^2+px+q} + \cdots + \frac{A_nx+B_n}{(x^2+px+q)^n}$ |

**待定系数法步骤**：
1. 设分解式（含待定系数）
2. 通分后比较分子系数
3. 解方程组确定系数
4. 逐项积分

#### 6. 几个重要的积分公式

**考试常用，可以记住结果**：

$$\int \frac{1}{x^2 + a^2} dx = \frac{1}{a} \arctan\frac{x}{a} + C$$

$$\int \frac{1}{x^2 - a^2} dx = \frac{1}{2a} \ln\left|\frac{x-a}{x+a}\right| + C$$

$$\int \frac{1}{\sqrt{a^2 - x^2}} dx = \arcsin\frac{x}{a} + C$$

$$\int \frac{1}{\sqrt{x^2 \pm a^2}} dx = \ln|x + \sqrt{x^2 \pm a^2}| + C$$

$$\int \sec x dx = \ln|\sec x + \tan x| + C$$

$$\int \csc x dx = \ln|\csc x - \cot x| + C$$

#### 7. 三角函数积分技巧

**$I_n = \int \sin^n x dx$ 或 $\int \cos^n x dx$ 的递推**：
- $n$ 为偶数：使用 $\sin^2 x = \frac{1-\cos 2x}{2}$ 降幂
- $n$ 为奇数：分离一个因子后用换元法

**$\int \sin^m x \cos^n x dx$ 类型**：
- $m, n$ 均为偶数：用倍角公式降幂
- $m, n$ 一奇一偶：换元法（设奇数次方的函数为新变量）

**$\int \tan^n x dx$ 递推公式**：
$$\int \tan^n x dx = \frac{\tan^{n-1} x}{n-1} - \int \tan^{n-2} x dx$$

### 🎯 题型分类与对策

| 题型 | 特点 | 推荐方法 |
|-----|------|---------|
| 幂函数积分 | $\int x^n dx$ | 直接公式或凑微分 |
| 指数函数积分 | $\int e^x f(x) dx$ | 分部积分或凑微分 |
| 对数函数积分 | $\int \ln x \cdot g(x) dx$ | 分部积分 |
| 三角函数积分 | 含 $\sin, \cos$ | 恒等变形或换元 |
| 有理函数积分 | $\frac{P(x)}{Q(x)}$ | 部分分式分解 |
| 根式积分 | 含 $\sqrt{...}$ | 三角换元或根式换元 |
| 混合型 | 多种函数组合 | 综合运用多种方法 |

## 3. 代码示例

### 1. 符号积分

```python
import sympy as sp

# 定义符号变量
x = sp.Symbol('x')

# 示例1：幂函数积分
expr1 = x**3
result1 = sp.integrate(expr1, x)
print(f"∫x³ dx = {result1}")

# 示例2：三角函数积分
expr2 = sp.sin(x) * sp.cos(x)
result2 = sp.integrate(expr2, x)
print(f"∫sin(x)cos(x) dx = {result2}")

# 示例3：分部积分
expr3 = x * sp.exp(x)
result3 = sp.integrate(expr3, x)
print(f"∫x·eˣ dx = {result3}")

# 示例4：三角换元
expr4 = sp.sqrt(1 - x**2)
result4 = sp.integrate(expr4, x)
print(f"∫√(1-x²) dx = {result4}")

# 示例5：部分分式
expr5 = (x + 3) / (x**2 - 5*x + 6)
result5 = sp.integrate(expr5, x)
print(f"∫(x+3)/(x²-5x+6) dx = {result5}")
```

### 2. 数值积分

```python
import numpy as np
from scipy.integrate import quad, trapz, simpson

# 定义函数
f = lambda x: np.exp(-x**2)

# 使用 quad（自适应积分）
result_quad, error_quad = quad(f, 0, 1)
print(f"quad 结果: ∫₀¹ e^(-x²) dx ≈ {result_quad:.10f} (误差: {error_quad:.2e})")

# 使用梯形法则
x = np.linspace(0, 1, 1000)
y = f(x)
result_trapz = trapz(y, x)
print(f"梯形法则: ∫₀¹ e^(-x²) dx ≈ {result_trapz:.10f}")

# 使用辛普森法则
result_simpson = simpson(y, x)
print(f"辛普森法则: ∫₀¹ e^(-x²) dx ≈ {result_simpson:.10f}")

# 精确值（误差函数）
result_exact = np.sqrt(np.pi) / 2 * sp.erf(1)
print(f"精确值: ∫₀¹ e^(-x²) dx ≈ {float(result_exact):.10f}")
```

### 3. 不定积分可视化

```python
import matplotlib.pyplot as plt

def plot_integrand_and_integral(f, F, x_range, title):
    """
    绘制被积函数和原函数

    参数:
        f: 被积函数
        F: 原函数
        x_range: x的范围 [a, b]
        title: 标题
    """
    x = np.linspace(x_range[0], x_range[1], 100)
    y_f = f(x)
    y_F = F(x)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    # 被积函数
    ax1.plot(x, y_f)
    ax1.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    ax1.fill_between(x, 0, y_f, alpha=0.3)
    ax1.set_title(f"{title}: f(x)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)")

    # 原函数
    ax2.plot(x, y_F)
    ax2.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    ax2.set_title(f"{title}: F(x) = ∫f(x)dx")
    ax2.set_xlabel("x")
    ax2.set_ylabel("F(x)")

    plt.tight_layout()
    plt.show()

# 示例1：多项式
f1 = lambda x: x**2
F1 = lambda x: x**3 / 3
plot_integrand_and_integral(f1, F1, [0, 2], "∫x² dx")

# 示例2：三角函数
f2 = lambda x: np.sin(x)
F2 = lambda x: -np.cos(x)
plot_integrand_and_integral(f2, F2, [0, 2*np.pi], "∫sin(x) dx")

# 示例3：指数函数
f3 = lambda x: np.exp(-x)
F3 = lambda x: -np.exp(-x)
plot_integrand_and_integral(f3, F3, [0, 3], "∫e^(-x) dx")
```

## 10. 总结
### 10.1 重要定义
1. 不定积分：所有原函数的集合
2. 原函数：F'(x)=f(x)的函数F(x)
3. 积分常数：C（因为常数的导数为0）
4. 部分积分：∫udv=uv-∫vdu

### 10.2 重要定理
1. 基本积分公式：幂函数、指数函数、三角函数、反三角函数
2. 换元积分法（第一类）：∫f(g(x))g'(x)dx=∫f(u)du
3. 分部积分法：∫udv=uv-∫vdu
4. 部分分式分解：有理函数分解为简单分式之和

### 10.3 重要证明
1. 换元法的证明：利用复合函数的链式法则
2. 分部积分法的证明：利用乘积法则的逆运算

### 10.4 重要性质
1. 线性性：∫[αf+βg]=α∫f+β∫g
2. 积分与微分互逆：(∫f)'=f，∫f'=f+C
3. 常见函数的积分公式：exp、ln、三角、反三角

本章为后续学习相关章节奠定了基础。

## 易错点

- 换元后要把 $du$ 和积分变量一起替换，必要时再换回原变量
- 分部积分时先选好 $u$ 和 $dv$，避免把最麻烦的部分留在最后
- 不定积分的结果必须带 $C$，否则答案不完整
- 结果写出来以后要习惯性求导回验

## 自测（3问速测）

1. 面对 $f(g(x))g'(x)$ 形式时，我是否会优先想到换元？
2. 面对 $x e^x$ 或 $x\ln x$ 这类乘积时，我是否会先考虑分部积分？
3. 我能说明“原函数相差一个常数”为什么是不定积分的本质吗？

## 11. 练习（分层）
本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 计算：∫x³dx（参考《高等数学 上册 第八版》第4章习题4-1第1题）
2. 计算：∫eˣdx（参考《高等数学 上册 第八版》第4章习题4-1第2题）
3. 计算：∫1/xdx（参考《高等数学 上册 第八版》第4章习题4-1第3题）
4. 计算：∫sin(x)dx（参考《高等数学 上册 第八版》第4章习题4-1第4题）
5. 计算：∫cos(x)dx（参考《高等数学 上册 第八版》第4章习题4-1第5题）

### B档（进阶）
1. 应用换元法计算：∫x·eˣ²dx（参考《数学分析(第5版) 上》第8章习题8-2第3题）
2. 应用分部积分法计算：∫x·ln(x)dx（参考《数学分析(第5版) 上》第8章习题8-3第2题）
3. 计算：∫sin(2x)dx（参考《数学分析(第5版) 上》第8章习题8-2第4题）
4. 计算：∫xeˣ²dx（参考《数学分析(第5版) 上》第8章习题8-2第5题）
5. 计算：∫1/(1+x²)dx（参考《数学分析(第5版) 上》第8章习题8-2第6题）

### C档（挑战）
1. 应用：不定积分在神经网络反向传播中的应用（参考《数学分析(第5版) 上）第8章）
2. 应用：积分在概率密度函数归一化中的应用（参考《数学分析(第5版) 下》第15章）
3. 应用：积分在期望和方差计算中的应用（参考《数学分析(第5版) 下》第15章）
4. 应用：部分分式分解在控制理论中的应用（参考《高等数学 上册 第八版》第4章）
5. 应用：不定积分在数值积分中的应用（参考《高等数学 上册 第八版》第4章）





