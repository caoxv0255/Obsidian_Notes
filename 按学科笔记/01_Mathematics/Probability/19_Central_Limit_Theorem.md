---
type: note
subject: probability
chapter: 19
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 19 - 中心极限定理

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 📌 学习目标

- 说清楚 CLT 的“标准化”为什么是 $(\sum X_i-n\mu)/(\sqrt{n}\sigma)$
- 掌握 i.i.d. 情形（Lindeberg–Lévy）与独立不同分布情形（Lyapunov/Lindeberg–Feller）的差别
- 理解 Berry–Esseen 给出的误差界意味着什么（收敛速度）

## 难度分层

- **基础**：经典 CLT 的表述与应用（正态近似）
- **进阶**：特征函数法证明主线、Lindeberg 条件
- **拓展**：误差界（Berry–Esseen）、Edgeworth 展开与大偏差

## 1. 中心极限定理的意义

### 1.1 正态分布的普遍性

**经验观察**：许多自然现象呈现正态分布：
- 测量误差
- 人的身高、体重
- 考试成绩
- 产品尺寸

**问题**：为什么正态分布如此普遍？

**答案**：中心极限定理！

### 1.2 核心思想

**中心极限定理（CLT）**：大量独立随机变量之和（在适当标准化后）近似服从正态分布。

**数学表述**：
$$\frac{\sum_{i=1}^{n} X_i - n\mu}{\sqrt{n}\sigma} \xrightarrow{d} N(0, 1)$$

**意义**：
- 解释正态分布的普遍性
- 为统计推断提供理论基础
- 许多复杂问题可简化为正态分布

## 2. 特征函数预备

### 2.1 特征函数的定义

**定义**：随机变量 X 的**特征函数**定义为：
$$\varphi_X(t) = E[e^{itX}] = E[\cos(tX) + i\sin(tX)]$$

**性质**：
1. φ(0) = 1
2. |φ(t)| ≤ 1
3. φ(-t) = φ̄(t)（共轭）
4. φ 一致连续

### 2.2 特征函数的例子

**常用分布的特征函数**：

| 分布 | 特征函数 |
|------|----------|
| 点分布（X = a） | e^{ita} |
| Bernoulli(p) | q + pe^{it} |
| Binomial(n, p) | (q + pe^{it})^n |
| Poisson(λ) | exp(λ(e^{it} - 1)) |
| Uniform(a, b) | (e^{itb} - e^{ita})/(it(b-a)) |
| N(μ, σ²) | exp(iμt - σ²t²/2) |
| Exponential(λ) | λ/(λ - it) |
| Gamma(α, β) | (1 - it/β)^{-α} |

### 2.3 特征函数的重要性质

**性质1（唯一性）**：特征函数唯一确定分布。

**性质2（矩）**：若 E[|X|^n] < ∞，则：
$$E[X^k] = \frac{1}{i^k} \varphi^{(k)}(0), \quad k \leq n$$

**性质3（独立和）**：若 X, Y 独立，则：
$$\varphi_{X+Y}(t) = \varphi_X(t) \varphi_Y(t)$$

**性质4（线性变换）**：φ_{aX+b}(t) = e^{itb} φ_X(at)

### 2.4 连续性定理

**Lévy连续定理**：设随机变量序列 {Xₙ} 和 X 的特征函数分别为 φₙ 和 φ，则：
$$X_n \xrightarrow{d} X \iff \varphi_n(t) \to \varphi(t) \quad (\text{对每个} t \in \mathbb{R})$$

**意义**：特征函数收敛 ⟺ 分布收敛

## 3. 林德伯格-列维中心极限定理

### 3.1 经典CLT

**定理**（林德伯格-列维）：设 X₁, X₂, ... 为独立同分布随机变量，E[Xᵢ] = μ，Var(Xᵢ) = σ² > 0，则：
$$\frac{\sum_{i=1}^{n} X_i - n\mu}{\sqrt{n}\sigma} \xrightarrow{d} N(0, 1)$$

**等价形式**：
$$\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0, 1)$$

**意义**：样本均值经过标准化后渐近服从标准正态分布。

### 3.2 证明（特征函数法）

**步骤1**：设 Yᵢ = (Xᵢ - μ)/σ，则 E[Yᵢ] = 0，Var(Yᵢ) = 1。

**步骤2**：Yᵢ 的特征函数 φ(t) 在 t = 0 处展开：
$$\varphi(t) = E[e^{itY}] = 1 + itE[Y] + \frac{(it)^2}{2}E[Y^2] + o(t^2) = 1 - \frac{t^2}{2} + o(t^2)$$

**步骤3**：标准化和的特征函数：
$$\varphi_n(t) = E\left[\exp\left(it \frac{\sum_{i=1}^{n} Y_i}{\sqrt{n}}\right)\right] = \varphi\left(\frac{t}{\sqrt{n}}\right)^n$$

**步骤4**：取对数：
$$\ln \varphi_n(t) = n \ln \varphi\left(\frac{t}{\sqrt{n}}\right) = n \ln \left(1 - \frac{t^2}{2n} + o\left(\frac{1}{n}\right)\right)$$

**步骤5**：利用 ln(1 + x) ≈ x - x²/2：
$$\ln \varphi_n(t) = n \left(-\frac{t^2}{2n} + o\left(\frac{1}{n}\right)\right) = -\frac{t^2}{2} + o(1) \to -\frac{t^2}{2}$$

**步骤6**：因此：
$$\varphi_n(t) \to e^{-t^2/2}$$

这正是标准正态分布的特征函数。由 Lévy 连续定理，得证。

### 3.3 Lindeberg替换法

**思想**：用正态随机变量替换每个 Xᵢ，证明替换后误差很小。

**步骤**：
1. 设 {Xᵢ} 为目标序列，{Yᵢ} 为标准正态序列
2. 构造混合序列：Zᵢᵏ = Xᵢ（i ≤ k），Yᵢ（i > k）
3. 证明每步替换误差趋于 0
4. 应用三角不等式

**优点**：不依赖特征函数，更直观。

## 4. 李雅普诺夫中心极限定理

### 4.1 独立不同分布的情形

**定理**（李雅普诺夫）：设 X₁, X₂, ... 为独立随机变量（可不同分布），设：
$$s_n^2 = \sum_{i=1}^{n} \sigma_i^2 = \sum_{i=1}^{n} \text{Var}(X_i)$$

若存在 δ > 0 使得：
$$\lim_{n \to \infty} \frac{1}{s_n^{2+\delta}} \sum_{i=1}^{n} E[|X_i - \mu_i|^{2+\delta}] = 0$$

则：
$$\frac{\sum_{i=1}^{n} X_i - \sum_{i=1}^{n} \mu_i}{s_n} \xrightarrow{d} N(0, 1)$$

**意义**：
- 不要求同分布
- "李雅普诺夫条件"保证没有单项占主导地位

### 4.2 李雅普诺夫条件的验证

**例**：设 Xᵢ ~ Bernoulli(pᵢ)，pᵢ ∈ (0, 1)

取 δ = 1：
$$\frac{\sum_{i=1}^{n} E|X_i - p_i|^3}{(\sum_{i=1}^{n} p_i(1-p_i))^{3/2}}$$

若 pᵢ 一致远离 0 和 1，且 n → ∞，则条件成立。

## 5. 林德伯格-费勒中心极限定理

### 5.1 林德伯格条件

**林德伯格条件**：对任意 ε > 0：
$$\lim_{n \to \infty} \frac{1}{s_n^2} \sum_{i=1}^{n} E\left[(X_i - \mu_i)^2 \mathbf{1}_{\{|X_i - \mu_i| > \varepsilon s_n\}}\right] = 0$$

**直观理解**：
- 每个 Xᵢ 对总方差的贡献"均匀"
- 没有单个随机变量占主导地位
- 极端值的影响可以忽略

### 5.2 林德伯格-费勒定理

**定理**：设 {Xₙ} 为独立随机变量序列，则：
$$\frac{\sum_{i=1}^{n} (X_i - \mu_i)}{s_n} \xrightarrow{d} N(0, 1) \quad \text{且} \quad \max_{1 \leq i \leq n} \frac{\sigma_i^2}{s_n^2} \to 0$$

当且仅当林德伯格条件成立。

**意义**：
- 给出了独立不同分布情形的最一般形式
- 林德伯格条件是充分必要条件

### 5.3 Feller条件

**Feller条件**：
$$\max_{1 \leq i \leq n} \frac{\sigma_i^2}{s_n^2} \to 0$$

**意义**：每个随机变量的方差在总方差中的占比趋于 0。

**关系**：林德伯格条件 ⟹ Feller条件

## 6. 误差估计与收敛速度

### 6.1 Berry-Esseen定理

**定理**（Berry-Esseen）：设 X₁, X₂, ... 为 i.i.d.，E[|X - μ|³] < ∞，则：
$$\sup_x \left| P\left(\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \leq x\right) - \Phi(x) \right| \leq \frac{C \cdot E[|X - \mu|^3]}{\sigma^3 \sqrt{n}}$$

其中 C 是常数（最优值约为 0.4748），Φ 是标准正态分布函数。

**意义**：
- 给出一致误差估计
- 收敛速度为 O(1/√n)
- 需要三阶矩存在

### 6.2 收敛速度的改进

**Edgeworth展开**：
$$P\left(\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \leq x\right) = \Phi(x) + \frac{\gamma_1}{6\sqrt{n}}(1-x^2)\phi(x) + O\left(\frac{1}{n}\right)$$

其中 γ₁ = E[(X-μ)³]/σ³ 是偏度。

**意义**：
- 比CLT更精确
- 考虑分布的偏度
- 小样本时更准确

### 6.3 大偏差理论

**问题**：当 x 很大时，P(Sₙ/√n > x) 的渐进行为？

**Cramér定理**：
$$\lim_{n \to \infty} \frac{1}{n} \ln P\left(\frac{S_n}{n} > a\right) = -I(a)$$

其中 I(a) 是率函数（大偏差速率函数）。

## 7. 应用实例

### 7.1 二项分布的正态近似

**德莫弗-拉普拉斯定理**（CLT的最早形式）：
设 X ~ B(n, p)，则当 n → ∞：
$$P(a < X \leq b) \approx \Phi\left(\frac{b-np}{\sqrt{np(1-p)}}\right) - \Phi\left(\frac{a-np}{\sqrt{np(1-p)}}\right)$$

**连续性修正**：
$$P(X \leq k) \approx \Phi\left(\frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right)$$

**例**：抛硬币 100 次，求正面次数在 45-55 之间的概率。

**解**：
$$P(45 \leq X \leq 55) \approx \Phi\left(\frac{55.5 - 50}{5}\right) - \Phi\left(\frac{44.5 - 50}{5}\right)$$
$$= \Phi(1.1) - \Phi(-1.1) = 2\Phi(1.1) - 1 \approx 0.7286$$

### 7.2 泊松分布的正态近似

**定理**：若 X ~ P(λ)，则当 λ → ∞：
$$\frac{X - \lambda}{\sqrt{\lambda}} \xrightarrow{d} N(0, 1)$$

**例**：某路口一年内发生 100 次事故，求明年事故次数在 80-120 之间的概率。

**解**：λ = 100，X ~ P(100)
$$P(80 \leq X \leq 120) \approx \Phi\left(\frac{120.5 - 100}{\sqrt{100}}\right) - \Phi\left(\frac{79.5 - 100}{\sqrt{100}}\right)$$
$$= \Phi(2.05) - \Phi(-2.05) = 2\Phi(2.05) - 1 \approx 0.9596$$

### 7.3 抽样调查

**问题**：估计总体比例 p，需要多大样本量？

**置信区间**：
$$P\left(\left|\hat{p} - p\right| < z_{\alpha/2} \sqrt{\frac{p(1-p)}{n}}\right) \approx 1 - \alpha$$

**样本量确定**：
$$n \geq \frac{z_{\alpha/2}^2 p(1-p)}{\varepsilon^2}$$

其中 ε 是允许误差。

## 练习（分层）

### A档（熟练）

1. 用 CLT 近似 $\mathrm{Binomial}(n,p)$ 的区间概率，并说明连续性修正。
2. 给定样本均值 $\bar X_n$，写出其标准化形式并解释每一项的意义。

### B档（辨析）

1. 举例说明：独立但不同分布时，为什么需要 Lindeberg/Lyapunov 条件。
2. 解释：Berry–Esseen 的 $O(1/\sqrt{n})$ 在小样本下意味着什么。

### C档（证明/推导）

1. 按特征函数法，把“i.i.d. + 二阶矩存在”推到 $\varphi_n(t)\to e^{-t^2/2}$ 的主线写出来。

## 自测（3问速测）

1. 我能解释为什么要除以 $\sqrt{n}\sigma$ 吗？
2. 我能区分“依分布收敛”和“依概率收敛”吗？
3. 我能说清 Berry–Esseen 界中的三阶矩在做什么吗？

**例**：估计支持率，要求误差不超过 3%，置信度 95%。

**解**：z₀.₀₂₅ ≈ 1.96，最保守估计 p = 0.5：
$$n \geq \frac{1.96^2 \times 0.25}{0.03^2} \approx 1067$$

### 7.4 蒙特卡洛方法

**估计积分**：I = ∫f(x) dx

**方法**：
1. 生成 U₁, ..., Uₙ ~ U(0,1)
2. 计算估计量 Îₙ = (1/n) Σf(Uᵢ)
3. 构建置信区间：
   $$\hat{I}_n \pm z_{\alpha/2} \frac{s}{\sqrt{n}}$$

其中 s 是样本标准差。

### 7.5 样本均值的直接近似

**例**：设 $X_1, \ldots, X_{25}$ 独立同分布，且 $X_i \sim \mathrm{Exp}(1)$。
则
$$\mu = E[X_i] = 1, \qquad \sigma^2 = \mathrm{Var}(X_i) = 1$$

由 CLT，样本均值
$$\bar{X}_{25} = \frac{1}{25}\sum_{i=1}^{25} X_i$$
近似服从
$$\bar{X}_{25} \approx N\left(1, \frac{1}{25}\right)$$

于是
$$P(0.8 \leq \bar{X}_{25} \leq 1.2) \approx \Phi\left(\frac{1.2-1}{1/5}\right) - \Phi\left(\frac{0.8-1}{1/5}\right)$$
$$= \Phi(1) - \Phi(-1) \approx 0.6826$$

**解释**：这说明即使原始分布是偏斜的指数分布，只要样本量足够大，样本均值仍会接近正态分布。

## 8. 数值实验

### 8.1 验证CLT

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 验证不同分布的CLT
np.random.seed(42)
n_samples = 10000
n_sum = 100  # 求和的项数

# 指数分布
exp_samples = np.random.exponential(1, (n_samples, n_sum))
exp_means = exp_samples.mean(axis=1)

# 均匀分布
uniform_samples = np.random.uniform(0, 1, (n_samples, n_sum))
uniform_means = uniform_samples.mean(axis=1)

# 绘图
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 指数分布
axes[0].hist(exp_means, bins=50, density=True, alpha=0.7)
x = np.linspace(exp_means.min(), exp_means.max(), 100)
axes[0].plot(x, stats.norm.pdf(x, exp_means.mean(), exp_means.std()), 'r-', lw=2)
axes[0].set_title('Exponential Distribution -> Normal')

# 均匀分布
axes[1].hist(uniform_means, bins=50, density=True, alpha=0.7)
x = np.linspace(uniform_means.min(), uniform_means.max(), 100)
axes[1].plot(x, stats.norm.pdf(x, uniform_means.mean(), uniform_means.std()), 'r-', lw=2)
axes[1].set_title('Uniform Distribution -> Normal')

plt.tight_layout()
plt.show()
```

### 8.2 收敛速度

```python
# 比较不同 n 的收敛速度
n_values = [10, 50, 100, 500]
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

for idx, n in enumerate(n_values):
    ax = axes[idx // 2, idx % 2]
    
    # 生成样本
    samples = np.random.exponential(1, (n_samples, n))
    standardized = (samples.mean(axis=1) - 1) / (1 / np.sqrt(n))
    
    # 绘制直方图和理论分布
    ax.hist(standardized, bins=50, density=True, alpha=0.7)
    x = np.linspace(-4, 4, 100)
    ax.plot(x, stats.norm.pdf(x), 'r-', lw=2)
    ax.set_title(f'n = {n}')
    
    # 计算KS统计量
    ks_stat = stats.kstest(standardized, 'norm').statistic
    ax.text(0.05, 0.95, f'KS = {ks_stat:.4f}', transform=ax.transAxes)

plt.tight_layout()
plt.show()
```

## 9. CLT的推广

### 9.1 多维CLT

**定理**：设 X₁, X₂, ... 为 i.i.d. 随机向量，E[Xᵢ] = μ，Cov(Xᵢ) = Σ，则：
$$\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} N(0, \Sigma)$$

### 9.2 依赖序列的CLT

**定理**（依赖情形）：对于某些依赖序列（如马尔可夫链、混合序列），在适当条件下CLT仍成立。

**应用**：时间序列分析、马尔可夫链蒙特卡洛（MCMC）。

### 9.3 函数的CLT

**Delta方法**：若 √n(X̄ₙ - μ) → N(0, Σ)，g 在 μ 处可微，则：
$$\sqrt{n}(g(\bar{X}_n) - g(\mu)) \xrightarrow{d} N(0, \nabla g(\mu)^T \Sigma \nabla g(\mu))$$

**应用**：参数函数的渐近分布。

## 10. 小结

### 10.1 核心定理

| 定理 | 条件 | 结论 |
|------|------|------|
| 林德伯格-列维 | i.i.d., 方差存在 | 标准化和 → N(0,1) |
| 李雅普诺夫 | 独立, 李雅普诺夫条件 | 标准化和 → N(0,1) |
| 林德伯格-费勒 | 独立, 林德伯格条件 | 标准化和 → N(0,1) |

### 10.2 关键概念

- **特征函数**：分析收敛的强大工具
- **林德伯格条件**：保证没有单项占主导
- **收敛速度**：Berry-Esseen 界为 O(1/√n)
- **正态近似**：二项分布、泊松分布等

### 10.3 应用

1. **统计推断**：置信区间、假设检验
2. **抽样调查**：样本量确定
3. **蒙特卡洛**：误差估计
4. **大偏差理论**：极端事件概率

---

**参考文献**：
1. 《概率论基础》（第3版）- 李贤平
2. 《Probability: Theory and Examples》- Rick Durrett
3. 《Asymptotic Statistics》- A.W. van der Vaart

**下一章**：[[20_Limit_Applications]] - 极限定理的应用

