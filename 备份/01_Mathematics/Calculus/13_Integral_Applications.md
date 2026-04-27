---
type: concept
topic: integral_applications
category: calculus
difficulty: intermediate
prerequisites:
    - [[10_Definite_Integrals]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-03-09
status: complete
subject: calculus
chapter: 13
updated: 2026-04-27
---

# 积分的应用 (Applications of Integrals)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解面积、体积、弧长与物理量的积分模型
- 掌握圆盘法、垫圈法、圆柱壳法和弧长公式
- 能把概率、质心和转动惯量问题转为积分

## 先修
- [[10_Definite_Integrals]] - 定积分
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：面积、体积与弧长的基本公式
- B档（进阶）：极坐标面积、旋转体与物理量应用
- C档（挑战）：综合建模、帕普斯定理与概率联动

## 自测（3问速测）
1. 面积、旋转体体积、弧长分别对应什么基本公式？
2. 什么时候应该考虑圆盘法、垫圈法和圆柱壳法？
3. 如何判断题目是几何应用还是物理应用？

## 1. 定义

**直观理解**：
积分是计算"累积量"的强大工具。通过积分，我们可以计算面积、体积、弧长、物理量（功、质心、转动惯量）等。

积分就像"把无数个小量加起来"：

- **面积**：把无数个小矩形加起来
- **体积**：把无数个小薄板加起来
- **弧长**：把无数个小线段加起来
- **功**：把无数个小功加起来

## 2. 定理与性质

### 1. 面积计算

#### 1.1 曲边梯形面积

**公式**：曲线 $y = f(x)$ 与 $x$ 轴在 $[a, b]$ 之间的面积：

$$A = \int_a^b |f(x)| dx$$

**示例**：计算 $y = \sin x$ 与 $x$ 轴在 $[0, 2\pi]$ 之间的面积

**解**：
$$A = \int_0^{2\pi} |\sin x| dx = \int_0^{\pi} \sin x dx + \int_{\pi}^{2\pi} (-\sin x) dx$$
$$= [-\cos x]_0^{\pi} + [\cos x]_{\pi}^{2\pi} = 2 + 2 = 4$$

#### 1.2 两曲线之间的面积

**公式**：两曲线 $y = f(x)$ 和 $y = g(x)$ 在 $[a, b]$ 之间的面积：

$$A = \int_a^b |f(x) - g(x)| dx$$

**示例**：计算 $y = x^2$ 和 $y = x$ 之间的面积

**解**：
首先求交点：
$$x^2 = x \implies x = 0 \text{ 或 } x = 1$$

在 $[0, 1]$ 上，$x \geq x^2$，故：
$$A = \int_0^1 (x - x^2) dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$$

#### 1.3 极坐标下的面积

**公式**：极坐标曲线 $r = r(\theta)$ 在 $[\alpha, \beta]$ 之间的面积：

$$A = \frac{1}{2} \int_{\alpha}^{\beta} r^2(\theta) d\theta$$

**示例**：计算圆 $r = 2\cos\theta$ 的面积

**解**：
圆的范围是 $[-\frac{\pi}{2}, \frac{\pi}{2}]$，故：
$$A = \frac{1}{2} \int_{-\pi/2}^{\pi/2} (2\cos\theta)^2 d\theta$$
$$= 2 \int_{-\pi/2}^{\pi/2} \cos^2\theta d\theta = 2 \int_{-\pi/2}^{\pi/2} \frac{1 + \cos 2\theta}{2} d\theta$$
$$= \int_{-\pi/2}^{\pi/2} (1 + \cos 2\theta) d\theta = \pi$$

### 2. 体积计算

#### 2.1 圆盘法（旋转体体积）

**公式**：曲线 $y = f(x)$ 绕 $x$ 轴旋转一周形成的旋转体体积：

$$V = \pi \int_a^b f^2(x) dx$$

**示例**：计算 $y = \sqrt{x}$ 绕 $x$ 轴旋转一周在 $[0, 1]$ 上的体积

**解**：
$$V = \pi \int_0^1 (\sqrt{x})^2 dx = \pi \int_0^1 x dx = \pi \left[\frac{x^2}{2}\right]_0^1 = \frac{\pi}{2}$$

#### 2.2 垫圈法（空心旋转体）

**公式**：两曲线 $y = f(x)$（外曲线）和 $y = g(x)$（内曲线）绕 $x$ 轴旋转一周形成的旋转体体积：

$$V = \pi \int_a^b [f^2(x) - g^2(x)] dx$$

**示例**：计算 $y = x$ 和 $y = x^2$ 绕 $x$ 轴旋转一周在 $[0, 1]$ 上的体积

**解**：
$$V = \pi \int_0^1 [x^2 - (x^2)^2] dx = \pi \int_0^1 (x^2 - x^4) dx$$
$$= \pi \left[\frac{x^3}{3} - \frac{x^5}{5}\right]_0^1 = \pi \left(\frac{1}{3} - \frac{1}{5}\right) = \frac{2\pi}{15}$$

#### 2.3 圆柱壳法

**公式**：曲线 $y = f(x)$ 绕 $y$ 轴旋转一周形成的旋转体体积：

$$V = 2\pi \int_a^b x \cdot f(x) dx$$

**示例**：计算 $y = x^2$ 绕 $y$ 轴旋转一周在 $[0, 1]$ 上的体积

**解**：
$$V = 2\pi \int_0^1 x \cdot x^2 dx = 2\pi \int_0^1 x^3 dx = 2\pi \left[\frac{x^4}{4}\right]_0^1 = \frac{\pi}{2}$$

### 3. 弧长计算

#### 平面曲线的弧长

**参数方程**：$x = x(t), y = y(t), t \in [a, b]$

$$L = \int_a^b \sqrt{[x'(t)]^2 + [y'(t)]^2} dt$$

**显函数**：$y = f(x), x \in [a, b]$

$$L = \int_a^b \sqrt{1 + [f'(x)]^2} dx$$

**极坐标**：$r = r(\theta), \theta \in [\alpha, \beta]$

$$L = \int_{\alpha}^{\beta} \sqrt{r^2(\theta) + [r'(\theta)]^2} d\theta$$

**示例**：计算 $y = \frac{2}{3}x^{3/2}$ 在 $[0, 3]$ 上的弧长

**解**：
$$y' = x^{1/2}$$
$$L = \int_0^3 \sqrt{1 + x} dx = \int_0^3 (1 + x)^{1/2} dx$$
$$= \left[\frac{2}{3}(1 + x)^{3/2}\right]_0^3 = \frac{2}{3}(8 - 1) = \frac{14}{3}$$

### 4. 旋转面的面积

**公式**：曲线 $y = f(x)$ 绕 $x$ 轴旋转一周形成的旋转面面积：

$$S = 2\pi \int_a^b f(x) \sqrt{1 + [f'(x)]^2} dx$$

**示例**：计算 $y = \sqrt{x}$ 绕 $x$ 轴旋转一周在 $[0, 1]$ 上的表面积

**解**：
$$f'(x) = \frac{1}{2\sqrt{x}}$$
$$S = 2\pi \int_0^1 \sqrt{x} \sqrt{1 + \frac{1}{4x}} dx = 2\pi \int_0^1 \sqrt{x + \frac{1}{4}} dx$$
$$= 2\pi \left[\frac{2}{3}(x + \frac{1}{4})^{3/2}\right]_0^1 = \frac{4\pi}{3}\left(\frac{5}{4}\right)^{3/2} - \frac{\pi}{6}$$

### 5. 物理应用

#### 5.1 功

**公式**：力 $F(x)$ 沿 $x$ 轴从 $a$ 到 $b$ 做的功：

$$W = \int_a^b F(x) dx$$

**示例**：将一个质量为 $m$ 的物体从地球表面移到距离地球表面 $h$ 处，需要做多少功？

**解**：
万有引力：$F(x) = \frac{G M m}{(R + x)^2}$，其中 $R$ 是地球半径

$$W = \int_0^h \frac{G M m}{(R + x)^2} dx = G M m \left[-\frac{1}{R + x}\right]_0^h$$
$$= G M m \left(\frac{1}{R} - \frac{1}{R + h}\right)$$

#### 5.2 质心

**公式**：平面区域的质心 $(\bar{x}, \bar{y})$：

$$\bar{x} = \frac{1}{A} \int_a^b x \cdot f(x) dx$$
$$\bar{y} = \frac{1}{2A} \int_a^b f^2(x) dx$$

其中 $A = \int_a^b f(x) dx$ 是区域的面积。

**示例**：计算 $y = \sqrt{x}$ 与 $x$ 轴在 $[0, 1]$ 之间区域的质心

**解**：
$$A = \int_0^1 \sqrt{x} dx = \frac{2}{3}$$
$$\bar{x} = \frac{1}{A} \int_0^1 x \sqrt{x} dx = \frac{3}{2} \cdot \frac{2}{5} = \frac{3}{5}$$
$$\bar{y} = \frac{1}{2A} \int_0^1 x dx = \frac{3}{4} \cdot \frac{1}{2} = \frac{3}{8}$$

因此质心为 $(\frac{3}{5}, \frac{3}{8})$。

#### 5.3 转动惯量

**公式**：平面区域关于 $x$ 轴的转动惯量：

$$I_x = \int_a^b \int_0^{f(x)} y^2 dy dx = \frac{1}{3} \int_a^b f^3(x) dx$$

## 机器学习中的应用

### 1. 概率密度函数

#### 正态分布的累积分布函数

$$\Phi(x) = \int_{-\infty}^x \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(t-\mu)^2}{2\sigma^2}} dt$$

这个积分没有初等函数形式的解，需要数值计算。

#### 期望和方差

**期望**：$E[X] = \int_{-\infty}^{\infty} x f(x) dx$

**方差**：$\text{Var}(X) = \int_{-\infty}^{\infty} (x - \mu)^2 f(x) dx$

### 2. 信息论

#### 微分熵

$$h(X) = -\int f(x) \log f(x) dx$$

#### KL散度

$$D_{KL}(P \| Q) = \int p(x) \log \frac{p(x)}{q(x)} dx$$

### 3. 贝叶斯推断

#### 边缘似然

$$P(D) = \int P(D|\theta) P(\theta) d\theta$$

#### 后验分布

$$P(\theta|D) = \frac{P(D|\theta) P(\theta)}{P(D)}$$

## 3. 代码示例

### 1. 面积计算

```python
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def area_between_curves(f, g, a, b):
    """
    计算两曲线之间的面积

    参数:
        f: 上曲线函数
        g: 下曲线函数
        a: 积分下限
        b: 积分上限

    返回:
        area: 面积
    """
    integrand = lambda x: abs(f(x) - g(x))
    area, _ = quad(integrand, a, b)
    return area

# 示例：y = x 和 y = x^2 之间的面积
f = lambda x: x
g = lambda x: x**2

# 求交点
from scipy.optimize import fsolve
intersection1 = fsolve(lambda x: f(x) - g(x), 0)
intersection2 = fsolve(lambda x: f(x) - g(x), 1)

a, b = float(intersection1[0]), float(intersection2[0])
area = area_between_curves(f, g, a, b)

print(f"y = x 和 y = x² 在 [{a:.2f}, {b:.2f}] 之间的面积 = {area:.6f}")
print(f"理论值：1/6 ≈ {1/6:.6f}")

# 可视化
x = np.linspace(a - 0.5, b + 0.5, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, f(x), 'b-', label='y = x')
plt.plot(x, g(x), 'r-', label='y = x²')
plt.fill_between(x, g(x), f(x), where=(x >= a) & (x <= b),
                 alpha=0.3, label='面积')
plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)
plt.axvline(x=a, color='k', linestyle='--', alpha=0.5)
plt.axvline(x=b, color='k', linestyle='--', alpha=0.5)
plt.title(f"曲线之间的面积 = {area:.6f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### 2. 体积计算

```python
def volume_of_revolution_disk(f, a, b):
    """
    使用圆盘法计算旋转体体积

    参数:
        f: 曲线函数
        a: 积分下限
        b: 积分上限

    返回:
        volume: 体积
    """
    integrand = lambda x: np.pi * f(x)**2
    volume, _ = quad(integrand, a, b)
    return volume

def volume_of_revolution_shell(f, a, b):
    """
    使用圆柱壳法计算旋转体体积

    参数:
        f: 曲线函数
        a: 积分下限
        b: 积分上限

    返回:
        volume: 体积
    """
    integrand = lambda x: 2 * np.pi * x * f(x)
    volume, _ = quad(integrand, a, b)
    return volume

# 示例1：y = sqrt(x) 绕 x 轴旋转
f1 = lambda x: np.sqrt(x)
volume1_disk = volume_of_revolution_disk(f1, 0, 1)
print(f"y = √x 绕 x 轴旋转的体积（圆盘法）= {volume1_disk:.6f}")
print(f"理论值：π/2 ≈ {np.pi/2:.6f}")

# 示例2：y = x^2 绕 y 轴旋转
f2 = lambda x: x**2
volume2_shell = volume_of_revolution_shell(f2, 0, 1)
print(f"y = x² 绕 y 轴旋转的体积（圆柱壳法）= {volume2_shell:.6f}")
print(f"理论值：π/2 ≈ {np.pi/2:.6f}")
```

### 3. 弧长计算

```python
def arc_length_parametric(x_func, y_func, a, b):
    """
    计算参数方程的弧长

    参数:
        x_func: x(t) 函数
        y_func: y(t) 函数
        a: 参数下限
        b: 参数上限

    返回:
        length: 弧长
    """
    from scipy.misc import derivative

    # 定义导数函数
    dx_dt = lambda t: derivative(x_func, t, dx=1e-6)
    dy_dt = lambda t: derivative(y_func, t, dx=1e-6)

    integrand = lambda t: np.sqrt(dx_dt(t)**2 + dy_dt(t)**2)
    length, _ = quad(integrand, a, b)
    return length

# 示例：半圆 x = cos(t), y = sin(t), t ∈ [0, π]
x_func = lambda t: np.cos(t)
y_func = lambda t: np.sin(t)
length = arc_length_parametric(x_func, y_func, 0, np.pi)

print(f"半圆的弧长 = {length:.6f}")
print(f"理论值：π ≈ {np.pi:.6f}")
```

### 4. 概率分布的期望和方差

```python
def expected_value(f, pdf, x_range):
    """
    计算随机变量的期望

    参数:
        f: 函数 f(X)
        pdf: 概率密度函数
        x_range: x 的范围 [a, b]

    返回:
        expectation: 期望值
    """
    integrand = lambda x: f(x) * pdf(x)
    expectation, _ = quad(integrand, x_range[0], x_range[1])
    return expectation

def variance(f, pdf, x_range):
    """
    计算随机变量的方差

    参数:
        f: 函数 f(X)
        pdf: 概率密度函数
        x_range: x 的范围 [a, b]

    返回:
        var: 方差
    """
    E = expected_value(f, pdf, x_range)
    f_squared = lambda x: (f(x) - E)**2
    var = expected_value(f_squared, pdf, x_range)
    return var

# 示例：均匀分布 U(0, 1)
pdf_uniform = lambda x: 1 if 0 <= x <= 1 else 0

# 计算 E[X] 和 Var(X)
E_X = expected_value(lambda x: x, pdf_uniform, [0, 1])
Var_X = variance(lambda x: x, pdf_uniform, [0, 1])

print(f"均匀分布 U(0,1) 的 E[X] = {E_X:.6f} (理论值: 0.5)")
print(f"均匀分布 U(0,1) 的 Var(X) = {Var_X:.6f} (理论值: 1/12 ≈ {1/12:.6f})")

# 示例：正态分布 N(0, 1) 的绝对值的期望
from scipy.stats import norm
pdf_normal = lambda x: norm.pdf(x, 0, 1)

E_abs = expected_value(lambda x: abs(x), pdf_normal, [-np.inf, np.inf])
print(f"标准正态分布 |X| 的期望 = {E_abs:.6f}")
print(f"理论值：2/√(2π) ≈ {2/np.sqrt(2*np.pi):.6f}")
```

## 习题

### 基础题

1. 计算以下区域的面积：
   - $y = x^2$ 和 $y = x$ 之间的面积
   - $y = \cos x$ 和 $x$ 轴在 $[0, 2\pi]$ 之间的面积
   - 极坐标曲线 $r = 2\sin\theta$ 的面积

2. 计算以下旋转体的体积：
   - $y = \sqrt{4 - x^2}$ 绕 $x$ 轴旋转一周的体积
   - $y = x^2$ 和 $y = \sqrt{x}$ 绕 $x$ 轴旋转一周的体积

3. 计算以下曲线的弧长：
   - $y = \ln x$ 在 $[1, e]$ 上的弧长
   - $y = \cosh x$ 在 $[0, 1]$ 上的弧长

### 进阶题

4. 计算圆 $x^2 + y^2 = R^2$ 的面积、周长、绕 $x$ 轴旋转的体积和表面积。

5. 一个密度为 $\rho(x) = 1 + x$ 的细杆，$x \in [0, 1]$，计算：
   - 质量
   - 质心
   - 关于原点的转动惯量

6. 证明：对于均匀分布 U(a, b)，E[X] = (a + b)/2，Var(X) = (b - a)²/12。

### 挑战题

7. 研究"帕普斯定理"（Pappus's Centroid Theorems），并利用它计算复杂旋转体的体积。

8. 在机器学习中，为什么 KL 散度不能作为真正的"距离"？讨论对称性和三角不等式。

9. 计算 $E[X^2]$ 和 $E[X]^2$，并证明 $\text{Var}(X) = E[X^2] - E[X]^2$。

## 经典教材参考

- **Rudin《数学分析原理》**：第6章"黎曼-斯蒂尔杰斯积分"
- **华东师大《数学分析》**：第3章第4节"定积分的应用"
- **同济《高等数学》**：第6章"定积分的应用"
- **Thomas《托马斯微积分》**：第6章"积分的应用"

## 相关链接

- [[10_Definite_Integrals]] - 定积分（积分应用的基础）
- [[12_Improper_Integrals]] - 反常积分（面积和体积的推广）
- [[../../01_Mathematics/Probability/04_Expectation_Variance]] - 期望方差（积分在概率中的应用）
- [[05_Data_Visualization]] - 数据可视化（面积和曲线的应用）
- [[06_Case_Finance]] - 金融案例（期望和方差的应用）
## 总结
- 积分应用的关键是把几何、物理或概率问题转成“微元求和”
- 画图、分区、选微元、列积分是通用流程
- 面积、体积、弧长与物理量都围绕积分核与几何意义展开

## 易错点
- 忽略取绝对值或分区间处理
- 旋转轴判断错误导致公式选错
- 弧长公式漏掉导数平方项
- 物理题没有先建立微元

## 根据题型整理的做题方法
### 积分应用的分析框架

**核心思想**：积分是"微元求和"的工具

#### 常见应用类型

| 应用类型      | 基本公式                           | 关键技巧   |
| --------- | ------------------------------ | ------ |
| **平面面积**  | $\int\vert f(x)-g(x)\vert dx$  | 确定上下函数 |
| **旋转体体积** | $\pi\int f^2(x)dx$             | 绕x轴或y轴 |
| **曲线弧长**  | $\int\sqrt{1+f'^2}dx$          | 弧微分公式  |
| **旋转面面积** | $2\pi\int f(x)\sqrt{1+f'^2}dx$ | 侧面积公式  |
| **物理应用**  | 视具体问题而定                        | 建立微元   |

#### 解题步骤

1. **画图**：确定积分区域
2. **选变量**：确定积分变量和区间
3. **写微元**：表达被积函数
4. **计算积分**：求定积分

### 核心公式速查

**几何应用**：
- 面积：$A = \int_a^b |f(x)-g(x)|dx$
- 体积（圆盘法）：$V = \pi\int_a^b f^2(x)dx$
- 体积（圆柱壳法）：$V = 2\pi\int_a^b x|f(x)|dx$
- 弧长：$L = \int_a^b \sqrt{1+[f'(x)]^2}dx$

**物理应用**：
- 功：$W = \int_a^b F(x)dx$
- 质心：$\bar{x} = \frac{\int xf(x)dx}{\int f(x)dx}$
- 转动惯量：$I = \int r^2 dm$

## 10. 练习（分层）
本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 计算曲线 $$y=x$$ 与 $$x$$ 轴在区间 $$[0,1]$$ 上围成的面积。
2. 计算曲线 $$y=x$$ 与 $$y=x^2$$ 在区间 $$[0,1]$$ 上围成的面积。
3. 计算 $$y=\sqrt{x}$$ 绕 $$x$$ 轴在 $$[0,1]$$ 上旋转一周所得体积。
4. 计算直线 $$y=2x$$ 在 $$[0,1]$$ 上的弧长。

### B档（进阶）
1. 用圆柱壳法计算曲线 $$y=1-x$$ 绕 $$y$$ 轴旋转一周在 $$[0,1]$$ 上形成的体积。
2. 计算由 $$y=x$$ 与 $$y=x^2$$ 围成的区域绕 $$x$$ 轴旋转所得体积。
3. 计算极坐标曲线 $$r=1+\cos\theta$$ 在一个完整闭合区间内围成的面积。
4. 若平面薄板的密度为 $$\rho(x)=x$$，求区间 $$[0,1]$$ 上薄板的质心位置。

### C档（挑战）
1. 证明在适当光滑条件下，圆盘法与圆柱壳法给出的旋转体体积是一致的。
2. 用帕普斯定理计算一个由简单平面区域旋转得到的体积，并与直接积分结果核对。
3. 设力随位置变化为 $$F(x)=kx^2$$，求从 $$x=0$$ 到 $$x=a$$ 所做的功，并讨论它与线性力模型的区别。
4. 建立一个“质心 + 体积”联合建模题：先求一个旋转体体积，再求其质心或转动惯量的积分表达式。



