---
type: note
subject: probability
chapter: 08
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 08 - 随机变量函数的分布

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层

- **基础**：定义与直接计算
- **进阶**：性质证明与综合应用
- **拓展**：跨章节联系与建模

## 自测（3问速测）

1. 本章最核心的定义是什么？
2. 本章一个关键结论的适用条件是什么？
3. 如何把本章方法应用到一个具体问题？

## 1. 离散型随机变量的函数

### 1.1 基本方法

**定理**：设 X 为离散型随机变量，PMF 为 p_X(x)，Y = g(X)。

**方法**：
$$p_Y(y) = \sum_{x: g(x) = y} p_X(x)$$

### 1.2 单调函数

**定理**：若 g 严格单调，则：
$$p_Y(y) = p_X(g^{-1}(y))$$

**例**：X 的分布律为：

| X | -1 | 0 | 1 |
|---|----|----|---|
| P | 0.2 | 0.3 | 0.5 |

求 Y = X² 的分布。

**解**：
- Y = 0: P(Y=0) = P(X=0) = 0.3
- Y = 1: P(Y=1) = P(X=-1) + P(X=1) = 0.2 + 0.5 = 0.7

## 2. 连续型随机变量的函数

### 2.1 分布函数法

**步骤**：
1. 求 F_Y(y) = P(Y ≤ y) = P(g(X) ≤ y)
2. 对 y 求导得 f_Y(y) = F'_Y(y)

**例**：X ~ U(0, 1)，求 Y = -ln X 的分布。

**解**：
$$F_Y(y) = P(Y \leq y) = P(-\ln X \leq y) = P(X \geq e^{-y}) = 1 - e^{-y}, \quad y > 0$$
$$f_Y(y) = e^{-y}, \quad y > 0$$

故 Y ~ Exp(1)。

### 2.2 变量替换公式

**定理**：设 X 为连续型随机变量，PDF 为 f_X(x)，y = g(x) 严格单调可导，则：
$$f_Y(y) = f_X(g^{-1}(y)) \cdot \left|\frac{d g^{-1}(y)}{dy}\right|$$

**证明**：
设 g 递增，则：
$$F_Y(y) = P(Y \leq y) = P(g(X) \leq y) = P(X \leq g^{-1}(y)) = F_X(g^{-1}(y))$$
$$f_Y(y) = \frac{d}{dy} F_Y(y) = f_X(g^{-1}(y)) \cdot \frac{d g^{-1}(y)}{dy}$$

**例**：X ~ N(0, 1)，求 Y = σX + μ 的分布。

**解**：g(x) = σx + μ，g⁻¹(y) = (y-μ)/σ，|dg⁻¹/dy| = 1/|σ|
$$f_Y(y) = \phi\left(\frac{y-\mu}{\sigma}\right) \cdot \frac{1}{|\sigma|} = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(y-\mu)^2}{2\sigma^2}}$$

故 Y ~ N(μ, σ²)。

### 2.3 多个区间的情形

**定理**：若 y = g(x) 在区间 I₁, ..., Iₙ 上分别单调，反函数为 h₁(y), ..., hₙ(y)，则：
$$f_Y(y) = \sum_{i=1}^{n} f_X(h_i(y)) |h_i'(y)|$$

**例**：X ~ N(0, σ²)，求 Y = X² 的分布。

**解**：y = x² 在 (-∞, 0) 和 (0, +∞) 上分别单调，反函数为 x = -√y 和 x = √y。
$$f_Y(y) = f_X(-\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} + f_X(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}}$$
$$= \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{y}{2\sigma^2}} \cdot \frac{1}{\sqrt{y}} = \frac{1}{\sqrt{2\pi y}\sigma} e^{-\frac{y}{2\sigma^2}}, \quad y > 0$$

这是 Gamma(1/2, 1/(2σ²)) = χ²(1)/(2σ²)。

## 3. 常见变换

### 3.1 线性变换

**定理**：若 X 的 PDF 为 f_X(x)，则 Y = aX + b (a ≠ 0) 的 PDF 为：
$$f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y-b}{a}\right)$$

**例**：X ~ N(μ, σ²)，Y = (X-μ)/σ，则 Y ~ N(0, 1)。

### 3.2 幂变换

**例**：X ~ Exp(λ)，求 Y = X^α (α > 0) 的分布。

**解**：g(x) = x^α，g⁻¹(y) = y^{1/α}
$$f_Y(y) = f_X(y^{1/\alpha}) \cdot \frac{1}{\alpha} y^{1/\alpha - 1} = \lambda e^{-\lambda y^{1/\alpha}} \cdot \frac{1}{\alpha} y^{1/\alpha - 1}$$

### 3.3 指数变换

**例**：X ~ N(μ, σ²)，求 Y = e^X 的分布。

**解**：g(x) = e^x，g⁻¹(y) = ln y
$$f_Y(y) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(\ln y - \mu)^2}{2\sigma^2}} \cdot \frac{1}{y}, \quad y > 0$$

这是对数正态分布 LN(μ, σ²)。

### 3.4 对数变换

**例**：X ~ LN(μ, σ²)，求 Y = ln X 的分布。

**解**：Y = ln X ~ N(μ, σ²)。

## 4. 多个随机变量的函数

### 4.1 和的分布

**定理**：设 X, Y 独立，PDF 分别为 f_X, f_Y，则 Z = X + Y 的 PDF 为：
$$f_Z(z) = \int_{-\infty}^{+\infty} f_X(x) f_Y(z-x) dx = (f_X * f_Y)(z)$$

这是 f_X 和 f_Y 的**卷积**。

**例**：X₁, X₂ i.i.d. ~ Exp(λ)，求 Y = X₁ + X₂ 的分布。

**解**：
$$f_Y(y) = \int_0^y \lambda e^{-\lambda x} \cdot \lambda e^{-\lambda(y-x)} dx = \lambda^2 e^{-\lambda y} \int_0^y dx = \lambda^2 y e^{-\lambda y}$$

这是 Gamma(2, λ) 的 PDF。

### 4.2 差的分布

**定理**：Z = X - Y 的 PDF 为：
$$f_Z(z) = \int_{-\infty}^{+\infty} f_X(z+y) f_Y(y) dy$$

### 4.3 积的分布

**定理**：Z = XY 的 PDF 为：
$$f_Z(z) = \int_{-\infty}^{+\infty} f_X(x) f_Y\left(\frac{z}{x}\right) \frac{1}{|x|} dx$$

### 4.4 商的分布

**定理**：Z = X/Y 的 PDF 为：
$$f_Z(z) = \int_{-\infty}^{+\infty} f_X(zy) f_Y(y) |y| dy$$

**例**：X, Y i.i.d. ~ N(0, 1)，求 Z = X/Y 的分布。

**解**：
$$f_Z(z) = \int_{-\infty}^{+\infty} \frac{1}{2\pi} e^{-\frac{(zy)^2 + y^2}{2}} |y| dy = \frac{1}{\pi} \int_0^{\infty} y e^{-\frac{y^2(1+z^2)}{2}} dy = \frac{1}{\pi(1+z^2)}$$

这是 Cauchy 分布。

## 5. 极值分布

### 5.1 最大值

**定理**：设 X₁, ..., Xₙ i.i.d.，CDF 为 F(x)，则：
$$Y = \max(X_1, \ldots, X_n)$$
$$F_Y(y) = P(Y \leq y) = P(X_1 \leq y, \ldots, X_n \leq y) = F(y)^n$$
$$f_Y(y) = n F(y)^{n-1} f(y)$$

### 5.2 最小值

**定理**：
$$Z = \min(X_1, \ldots, X_n)$$
$$F_Z(z) = 1 - (1-F(z))^n$$
$$f_Z(z) = n (1-F(z))^{n-1} f(z)$$

### 5.3 例题

**例**：X₁, ..., Xₙ i.i.d. ~ Exp(λ)，求 Y = min(X₁, ..., Xₙ) 的分布。

**解**：
$$F_Y(y) = 1 - (1 - (1-e^{-\lambda y}))^n = 1 - e^{-n\lambda y}$$

故 Y ~ Exp(nλ)。

**意义**：n 个独立指数分布的最小值仍服从指数分布，参数为 nλ。

## 6. 次序统计量

### 6.1 定义

**定义**：设 X₁, ..., Xₙ 为样本，按从小到大排列：
$$X_{(1)} \leq X_{(2)} \leq \cdots \leq X_{(n)}$$

称 X_{(k)} 为第 k 个**次序统计量**。

### 6.2 分布

**定理**：设 X₁, ..., Xₙ i.i.d.，PDF 为 f(x)，CDF 为 F(x)，则：
$$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!(n-k)!} F(x)^{k-1} (1-F(x))^{n-k} f(x)$$

### 6.3 联合分布

**定理**：(X_{(1)}, ..., X_{(n)}) 的联合 PDF 为：
$$f(x_1, \ldots, x_n) = n! \prod_{i=1}^n f(x_i), \quad x_1 < x_2 < \cdots < x_n$$

### 6.4 应用

**例**：均匀分布 U(0,1) 的次序统计量。

X_{(k)} ~ Beta(k, n-k+1)。

## 7. 小结

### 7.1 核心方法

| 方法 | 适用情形 | 公式 |
|------|----------|------|
| 分布函数法 | 一般情形 | F_Y(y) → f_Y(y) |
| 变量替换 | 单调函数 | f_Y(y) = f_X(g⁻¹(y))\|dg⁻¹/dy\| |
| 卷积公式 | 独立和 | f_Z = f_X * f_Y |

### 7.2 重要结论

- X ~ N(μ,σ²) ⟹ aX+b ~ N(aμ+b, a²σ²)
- X ~ Exp(λ) ⟹ -ln(X/U(0,1)) ~ Exp(λ)
- X₁+X₂ ~ Gamma(α₁+α₂, β)（独立Gamma）

---

**参考文献**：
1. 《概率论与数理统计》- 浙江大学
2. 《Statistical Inference》- Casella & Berger

**下一章**：[[09_Common_Distributions]] - 常见概率分布族

