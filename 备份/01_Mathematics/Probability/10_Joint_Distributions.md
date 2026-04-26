---
type: note
subject: probability
chapter: 10
created: 2026-04-03
status: complete
---

# 10 - 多维随机变量与联合分布

## 1. 多维随机变量的概念

### 1.1 定义

**定义**：设 X₁, X₂, ..., Xₙ 为 n 个随机变量，则 X = (X₁, X₂, ..., Xₙ) 称为 **n 维随机变量**（随机向量）。

### 1.2 联合分布函数

**定义**：n 维随机变量的**联合分布函数**为：
$$F(x_1, x_2, \ldots, x_n) = P(X_1 \leq x_1, X_2 \leq x_2, \ldots, X_n \leq x_n)$$

**性质**：
1. 单调不减
2. 右连续
3. $\lim_{x_i \to -\infty} F(x_1, \ldots, x_n) = 0$
4. $\lim_{x_i \to +\infty} F(x_1, \ldots, x_n) = 1$

## 2. 二维离散型随机变量

### 2.1 联合分布律

**定义**：设 (X, Y) 为二维离散型随机变量，联合分布律为：
$$p_{ij} = P(X = x_i, Y = y_j)$$

**性质**：
1. pᵢⱼ ≥ 0
2. $\sum_{i,j} p_{ij} = 1$

**表格形式**：

| X\Y | y₁ | y₂ | ... | yₘ |
|-----|----|----|-----|-----|
| x₁ | p₁₁ | p₁₂ | ... | p₁ₘ |
| x₂ | p₂₁ | p₂₂ | ... | p₂ₘ |
| ... | ... | ... | ... | ... |
| xₙ | pₙ₁ | pₙ₂ | ... | pₙₘ |

### 2.2 边缘分布

**定义**：
- X 的边缘分布：$p_{i\cdot} = \sum_j p_{ij}$
- Y 的边缘分布：$p_{\cdot j} = \sum_i p_{ij}$

### 2.3 条件分布

**定义**：给定 Y = yⱼ 下 X 的条件分布律：
$$P(X = x_i | Y = y_j) = \frac{p_{ij}}{p_{\cdot j}}$$

## 3. 二维连续型随机变量

### 3.1 联合概率密度

**定义**：若存在非负函数 f(x, y) 使得：
$$F(x, y) = \int_{-\infty}^x \int_{-\infty}^y f(u, v) du dv$$

则称 (X, Y) 为**二维连续型随机变量**，f(x, y) 为**联合概率密度**。

**性质**：
1. f(x, y) ≥ 0
2. $\iint_{\mathbb{R}^2} f(x, y) dx dy = 1$
3. $P((X,Y) \in D) = \iint_D f(x, y) dx dy$
4. $f(x, y) = \frac{\partial^2 F}{\partial x \partial y}$（在连续点处）

### 3.2 边缘概率密度

**定理**：
- X 的边缘密度：$f_X(x) = \int_{-\infty}^{+\infty} f(x, y) dy$
- Y 的边缘密度：$f_Y(y) = \int_{-\infty}^{+\infty} f(x, y) dx$

### 3.3 条件概率密度

**定义**：给定 Y = y 下 X 的条件密度：
$$f_{X|Y}(x|y) = \frac{f(x, y)}{f_Y(y)}, \quad f_Y(y) > 0$$

## 4. 二元正态分布

### 4.1 定义

**定义**：(X, Y) 服从二元正态分布 N(μₓ, μᵧ, σₓ², σᵧ², ρ)，联合密度为：
$$f(x, y) = \frac{1}{2\pi\sigma_x\sigma_y\sqrt{1-\rho^2}} \exp\left(-\frac{1}{2(1-\rho^2)}\left[\frac{(x-\mu_x)^2}{\sigma_x^2} - \frac{2\rho(x-\mu_x)(y-\mu_y)}{\sigma_x\sigma_y} + \frac{(y-\mu_y)^2}{\sigma_y^2}\right]\right)$$

### 4.2 性质

**定理**：
1. X ~ N(μₓ, σₓ²)，Y ~ N(μᵧ, σᵧ²)
2. Cov(X, Y) = ρσₓσᵧ
3. X, Y 独立 ⟺ ρ = 0

### 4.3 条件分布

**定理**：给定 Y = y，X 的条件分布：
$$X|Y=y \sim N\left(\mu_x + \rho\frac{\sigma_x}{\sigma_y}(y-\mu_y), \sigma_x^2(1-\rho^2)\right)$$

## 5. 多维随机变量的数字特征

### 5.1 联合期望

**定义**：
$$E[g(X_1, \ldots, X_n)] = \int \cdots \int g(x_1, \ldots, x_n) f(x_1, \ldots, x_n) dx_1 \cdots dx_n$$

### 5.2 协方差矩阵

**定义**：随机向量 X = (X₁, ..., Xₙ)ᵀ 的协方差矩阵：
$$\Sigma = (\sigma_{ij}), \quad \sigma_{ij} = \text{Cov}(X_i, X_j)$$

**矩阵形式**：
$$\Sigma = E[(X - \mu)(X - \mu)^T]$$

### 5.3 相关矩阵

**定义**：相关矩阵 R = (ρᵢⱼ)，其中：
$$\rho_{ij} = \frac{\text{Cov}(X_i, X_j)}{\sqrt{\text{Var}(X_i)\text{Var}(X_j)}}$$

## 6. 独立性

### 6.1 定义

**定义**：X₁, X₂, ..., Xₙ 相互独立 ⟺ 对任意 Borel 集 B₁, ..., Bₙ：
$$P(X_1 \in B_1, \ldots, X_n \in B_n) = \prod_{i=1}^{n} P(X_i \in B_i)$$

### 6.2 等价条件

**定理**：以下条件等价：
1. X₁, ..., Xₙ 相互独立
2. F(x₁, ..., xₙ) = F₁(x₁)···Fₙ(xₙ)
3. f(x₁, ..., xₙ) = f₁(x₁)···fₙ(xₙ)（连续型）

### 6.3 独立的性质

**定理**：若 X₁, ..., Xₙ 相互独立，则：
1. E[∏Xᵢ] = ∏E[Xᵢ]
2. Var(∑Xᵢ) = ∑Var(Xᵢ)
3. g₁(X₁), ..., gₙ(Xₙ) 相互独立

## 7. 小结

### 7.1 核心概念

| 概念 | 定义 | 公式 |
|------|------|------|
| 联合分布 | F(x,y) = P(X≤x, Y≤y) | 二元函数 |
| 边缘分布 | 联合分布的边缘积分 | f_X(x) = ∫f(x,y)dy |
| 条件分布 | f(x\|y) = f(x,y)/f_Y(y) | 比值形式 |

### 7.2 重要结论

- 二元正态：独立 ⟺ ρ = 0
- 独立 ⟹ 不相关（反之不成立）
- 协方差矩阵半正定

---

**下一章**：[[11_Marginal_Conditional]] - 边缘分布与条件分布
