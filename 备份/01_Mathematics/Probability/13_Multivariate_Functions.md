---
type: note
subject: probability
chapter: 13
created: 2026-04-03
status: complete
---

# 13 - 多维随机变量函数的分布

## 1. 问题的提出

**基本问题**：设 (X₁, X₂, ..., Xₙ) 的联合分布已知，求函数 Z = g(X₁, ..., Xₙ) 的分布。

**典型问题**：
- Z = X + Y（和的分布）
- Z = X - Y（差的分布）
- Z = XY（积的分布）
- Z = X/Y（商的分布）
- Z = max(X, Y), Z = min(X, Y)（极值的分布）

## 2. 分布函数法

### 2.1 基本方法

**步骤**：
1. 写出 Z 的分布函数：F_Z(z) = P(Z ≤ z) = P(g(X,Y) ≤ z)
2. 将事件 {g(X,Y) ≤ z} 转化为 (X,Y) 平面上的区域
3. 用联合密度在该区域积分
4. 对 F_Z(z) 求导得到 f_Z(z)

### 2.2 示例：Z = X + Y

设 (X, Y) 的联合密度为 f(x, y)，求 Z = X + Y 的分布。

**分布函数**：
$$F_Z(z) = P(X + Y \leq z) = \iint_{x+y \leq z} f(x, y) dx dy$$

**转化为累次积分**：
$$F_Z(z) = \int_{-\infty}^{+\infty} \int_{-\infty}^{z-x} f(x, y) dy dx$$

**求导得密度**：
$$f_Z(z) = \frac{d}{dz} F_Z(z) = \int_{-\infty}^{+\infty} f(x, z-x) dx$$

**独立情况下的卷积公式**：
$$f_Z(z) = \int_{-\infty}^{+\infty} f_X(x) f_Y(z-x) dx = f_X * f_Y$$

### 2.3 示例：Z = max(X, Y)

**分布函数**：
$$F_Z(z) = P(\max(X,Y) \leq z) = P(X \leq z, Y \leq z) = F(z, z)$$

**独立时**：
$$F_Z(z) = F_X(z) \cdot F_Y(z)$$
$$f_Z(z) = f_X(z) F_Y(z) + F_X(z) f_Y(z)$$

### 2.4 示例：Z = min(X, Y)

**分布函数**：
$$F_Z(z) = 1 - P(\min(X,Y) > z) = 1 - P(X > z, Y > z)$$

**独立时**：
$$F_Z(z) = 1 - (1 - F_X(z))(1 - F_Y(z)) = F_X(z) + F_Y(z) - F_X(z)F_Y(z)$$
$$f_Z(z) = f_X(z)(1 - F_Y(z)) + (1 - F_X(z))f_Y(z)$$

## 3. 变量变换法（雅可比法）

### 3.1 二元变换

**问题**：设 (X, Y) 有联合密度 f_{XY}(x, y)，作变换：
$$\begin{cases} U = g_1(X, Y) \\ V = g_2(X, Y) \end{cases}$$

求 (U, V) 的联合密度。

**条件**：变换一一对应，逆变换存在且可微：
$$\begin{cases} X = h_1(U, V) \\ Y = h_2(U, V) \end{cases}$$

### 3.2 雅可比行列式

**定义**：
$$J = \frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix}$$

### 3.3 变换公式

**(U, V) 的联合密度**：
$$f_{UV}(u, v) = f_{XY}(h_1(u, v), h_2(u, v)) \cdot |J|$$

**注意**：
- 取雅可比行列式的绝对值
- 需要确定新变量的取值范围

### 3.4 示例：和与商

设 X, Y 独立，求 U = X + Y, V = X/Y 的联合密度。

**逆变换**：
$$X = \frac{UV}{1+V}, \quad Y = \frac{U}{1+V}$$

**雅可比行列式**：
$$J = \begin{vmatrix} \frac{v}{1+v} & \frac{u}{(1+v)^2} \\ \frac{1}{1+v} & -\frac{u}{(1+v)^2} \end{vmatrix} = -\frac{u}{(1+v)^2}$$

**联合密度**：
$$f_{UV}(u, v) = f_X\left(\frac{uv}{1+v}\right) f_Y\left(\frac{u}{1+v}\right) \cdot \frac{|u|}{(1+v)^2}$$

## 4. 和的分布

### 4.1 卷积公式

**独立随机变量的和**：
$$f_Z(z) = \int_{-\infty}^{+\infty} f_X(x) f_Y(z-x) dx$$

**对称形式**：
$$f_Z(z) = \int_{-\infty}^{+\infty} f_X(z-y) f_Y(y) dy$$

### 4.2 正态分布的和

**定理**：若 X ~ N(μ₁, σ₁²), Y ~ N(μ₂, σ₂²) 独立，则：
$$X + Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$$

**推广**：若 X₁, ..., Xₙ 独立正态，则：
$$\sum_{i=1}^{n} X_i \sim N\left(\sum_{i=1}^{n} \mu_i, \sum_{i=1}^{n} \sigma_i^2\right)$$

### 4.3 泊松分布的和

**定理**：若 X ~ Poisson(λ₁), Y ~ Poisson(λ₂) 独立，则：
$$X + Y \sim \text{Poisson}(\lambda_1 + \lambda_2)$$

### 4.4 指数分布的和

**定理**：若 X₁, ..., Xₙ i.i.d. Exp(λ)，则：
$$\sum_{i=1}^{n} X_i \sim \text{Gamma}(n, \lambda)$$

### 4.5 卡方分布的和

**定理**：若 X ~ χ²(n), Y ~ χ²(m) 独立，则：
$$X + Y \sim \chi^2(n + m)$$

## 5. 商的分布

### 5.1 商的密度公式

设 X, Y 独立，Z = X/Y，则：
$$f_Z(z) = \int_{-\infty}^{+\infty} |y| f_X(zy) f_Y(y) dy$$

### 5.2 正态变量的商（t分布）

**定理**：若 X ~ N(0,1), Y ~ χ²(n) 独立，则：
$$T = \frac{X}{\sqrt{Y/n}} \sim t(n)$$

这是学生t分布的定义。

### 5.3 卡方变量的商（F分布）

**定理**：若 X ~ χ²(n), Y ~ χ²(m) 独立，则：
$$F = \frac{X/n}{Y/m} \sim F(n, m)$$

这是F分布的定义。

## 6. 极值的分布

### 6.1 最大值分布

设 X₁, ..., Xₙ 独立同分布，分布函数为 F(x)，则：
$$M = \max(X_1, \ldots, X_n)$$

**分布函数**：
$$F_M(x) = P(M \leq x) = P(X_1 \leq x, \ldots, X_n \leq x) = [F(x)]^n$$

**密度函数**：
$$f_M(x) = n[F(x)]^{n-1} f(x)$$

### 6.2 最小值分布

设 X₁, ..., Xₙ 独立同分布，分布函数为 F(x)，则：
$$m = \min(X_1, \ldots, X_n)$$

**分布函数**：
$$F_m(x) = 1 - [1 - F(x)]^n$$

**密度函数**：
$$f_m(x) = n[1 - F(x)]^{n-1} f(x)$$

### 6.3 极值分布的渐近行为

**Gumbel分布**：指数型尾部的极值渐近分布
**Fréchet分布**：幂律尾部的极值渐近分布
**Weibull分布**：有限尾部的极值渐近分布

## 7. 顺序统计量

### 7.1 定义

设 X₁, ..., Xₙ 为样本，按从小到大排列：
$$X_{(1)} \leq X_{(2)} \leq \cdots \leq X_{(n)}$$

X_{(k)} 称为第 k 个顺序统计量。

### 7.2 顺序统计量的分布

**第 k 个顺序统计量的密度**：
$$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!(n-k)!}[F(x)]^{k-1}[1-F(x)]^{n-k}f(x)$$

**特殊情形**：
- X_{(1)} = min(X₁, ..., Xₙ)：最小值
- X_{(n)} = max(X₁, ..., Xₙ)：最大值
- X_{((n+1)/2)}：样本中位数（n为奇数）

### 7.3 均匀分布的顺序统计量

**定理**：若 X₁, ..., Xₙ i.i.d. U(0,1)，则：
$$X_{(k)} \sim \text{Beta}(k, n-k+1)$$

## 8. 常用变换技巧

### 8.1 线性变换

若 Y = aX + b，则：
$$F_Y(y) = F_X\left(\frac{y-b}{a}\right)$$
$$f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y-b}{a}\right)$$

### 8.2 单调函数变换

若 Y = g(X)，g 严格单调，则：
$$f_Y(y) = f_X(g^{-1}(y)) \cdot \left|\frac{d}{dy}g^{-1}(y)\right|$$

### 8.3 极坐标变换

设 X, Y 独立 N(0,1)，令：
$$R = \sqrt{X^2 + Y^2}, \quad \Theta = \arctan(Y/X)$$

则：
- R ~ Rayleigh 分布
- Θ ~ U(0, 2π)
- R, Θ 独立

## 9. Python实现

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 卷积法求和的分布
def sum_distribution(f_x, f_y, z_range):
    """
    数值计算独立随机变量和的密度
    """
    dz = z_range[1] - z_range[0]
    f_z = np.zeros_like(z_range)
    
    for i, z in enumerate(z_range):
        # 数值积分
        x = z_range
        f_z[i] = np.trapz(f_x(x) * f_y(z - x), x)
    
    return f_z

# 示例：两个独立指数分布的和
lambda1, lambda2 = 1, 2
z = np.linspace(0, 10, 1000)

# 方法1：卷积（数值）
f_z_conv = sum_distribution(
    lambda x: stats.expon.pdf(x, scale=1/lambda1),
    lambda x: stats.expon.pdf(x, scale=1/lambda2),
    z
)

# 方法2：直接采样
n_samples = 100000
X = np.random.exponential(1/lambda1, n_samples)
Y = np.random.exponential(1/lambda2, n_samples)
Z = X + Y

# 绘图比较
plt.figure(figsize=(10, 6))
plt.hist(Z, bins=100, density=True, alpha=0.5, label='采样')
plt.plot(z, f_z_conv, 'r-', label='卷积')
plt.xlabel('z')
plt.ylabel('密度')
plt.legend()
plt.title('独立指数分布随机变量之和的分布')
plt.show()

# 顺序统计量
n = 10
k = 5
x = np.linspace(0, 1, 100)

# U(0,1) 的第k个顺序统计量服从 Beta(k, n-k+1)
y_theory = stats.beta.pdf(x, k, n-k+1)

# 采样验证
n_sim = 100000
samples = np.random.uniform(0, 1, (n_sim, n))
order_stats = np.sort(samples, axis=1)
x_k_samples = order_stats[:, k-1]

print(f"理论均值: {stats.beta.mean(k, n-k+1):.4f}")
print(f"样本均值: {x_k_samples.mean():.4f}")
```

## 10. 总结

| 方法 | 适用情况 | 关键公式 |
|------|----------|----------|
| 分布函数法 | 一般情况 | F_Z(z) = P(g(X,Y) ≤ z) |
| 卷积公式 | 独立变量的和 | f_Z = f_X * f_Y |
| 雅可比法 | 多元变换 | f_UV = f_XY · \|J\| |
| 极值公式 | max/min | F_max = Fⁿ, F_min = 1-(1-F)ⁿ |

**重要结论**：
- 正态分布对加法封闭
- 泊松分布对加法封闭
- 卡方分布对加法封闭
- 伽马分布对加法封闭（相同尺度参数）

---

**相关链接**：
- [[08_Functions_of_RV]] - 随机变量函数的分布
- [[10_Joint_Distributions]] - 多维随机变量与联合分布
- [[12_Independence]] - 随机变量的独立性
