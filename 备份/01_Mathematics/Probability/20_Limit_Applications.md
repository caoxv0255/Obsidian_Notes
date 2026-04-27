---
type: note
subject: probability
chapter: 20
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 20 - 极限定理的应用

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

## 1. 大数定律的应用

### 1.1 蒙特卡洛方法

**理论基础**：大数定律保证样本均值收敛于期望。

**积分估计**：
$$\int_a^b g(x) dx \approx \frac{b-a}{n}\sum_{i=1}^{n} g(X_i)$$

其中 Xᵢ ~ Uniform(a, b)。

**期望估计**：
$$E[g(X)] \approx \frac{1}{n}\sum_{i=1}^{n} g(X_i)$$

**误差分析**：由中心极限定理，估计的标准误为 σ/√n。

### 1.2 频率学派解释

**概率的频率解释**：
$$P(A) = \lim_{n \to \infty} \frac{n_A}{n}$$

其中 n_A 是事件 A 在 n 次试验中发生的次数。

**应用**：
- 概率的经验估计
- 统计推断的基础

### 1.3 样本均值的性质

**无偏性**：E[X̄] = μ

**一致性**：X̄ → μ（概率收敛）

**大样本性质**：
- X̄ 依分布收敛于 N(μ, σ²/n)
- |X̄ - μ| 的误差界可用切比雪夫不等式估计

## 2. 中心极限定理的应用

### 2.1 置信区间

**总体均值μ的置信区间**：
$$\bar{X} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

**推导**：由CLT，(X̄ - μ)/(σ/√n) ≈ N(0,1)。

**样本方差未知时**：使用t分布：
$$\bar{X} \pm t_{\alpha/2, n-1} \cdot \frac{S}{\sqrt{n}}$$

### 2.2 比例的推断

**样本比例**：p̂ = X/n，其中 X ~ B(n, p)。

**大样本近似**：
$$\frac{\hat{p} - p}{\sqrt{p(1-p)/n}} \approx N(0,1)$$

**置信区间**：
$$\hat{p} \pm z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

### 2.3 正态近似

**二项分布的正态近似**：
若 X ~ B(n, p)，当 np 和 n(1-p) 都较大时：
$$X \approx N(np, np(1-p))$$

**连续性修正**：
$$P(X \leq k) \approx \Phi\left(\frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right)$$

**泊松分布的正态近似**：
若 X ~ Poisson(λ)，当 λ 较大时：
$$X \approx N(\lambda, \lambda)$$

### 2.4 完整例题：样本比例的置信区间

**例**：某民调随机调查 400 人，其中 258 人支持某提案，求该提案支持率的 95% 置信区间。

**解**：样本比例为
$$\hat{p} = \frac{258}{400} = 0.645$$

由样本比例的正态近似，标准误为
$$\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} = \sqrt{\frac{0.645 \cdot 0.355}{400}} \approx 0.0239$$

取 $z_{0.025} \approx 1.96$，得到置信区间
$$0.645 \pm 1.96 \times 0.0239 \approx 0.645 \pm 0.0469$$
$$\Rightarrow [0.598,\ 0.692]$$

**直观理解**：样本量越大，区间越窄；样本比例越接近 0.5，波动越大。CLT 的作用就是把这种“样本平均的波动”统一地转成正态分布来处理。

## 3. 统计推断中的应用

### 3.1 假设检验

**Z检验**：检验均值是否等于某值

**检验统计量**：
$$Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}$$

**p值计算**：由标准正态分布计算。

### 3.2 样本量确定

**给定置信水平和误差限**：
$$n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2$$

其中 E 是允许的最大误差。

**示例**：估计均值，要求95%置信水平，误差不超过E：
$$n = \left(\frac{1.96 \cdot \sigma}{E}\right)^2$$

### 3.3 功效分析

**检验功效**：正确拒绝错误原假设的概率。

**样本量与功效的关系**：更大的样本量 → 更高的功效。

## 4. 蒙特卡洛积分

### 4.1 基本方法

**估计积分**：
$$I = \int_a^b g(x) dx$$

**步骤**：
1. 从 Uniform(a, b) 抽取 n 个样本 x₁, ..., xₙ
2. 计算估计值：
$$\hat{I} = \frac{b-a}{n}\sum_{i=1}^{n} g(x_i)$$

### 4.2 重要性采样

**问题**：直接采样效率低。

**方法**：从提议分布 q(x) 采样：
$$E[g(X)] = \int g(x) \frac{p(x)}{q(x)} q(x) dx$$

**估计**：
$$\hat{I} = \frac{1}{n}\sum_{i=1}^{n} g(x_i) \frac{p(x_i)}{q(x_i)}$$

**选择 q(x)**：使 g(x)p(x)/q(x) 方差最小。

### 4.3 方差缩减技术

**对偶变量**：
$$\hat{I} = \frac{1}{2}\left[\frac{1}{n}\sum g(U_i) + \frac{1}{n}\sum g(1-U_i)\right]$$

**控制变量**：利用相关变量减少方差。

**分层采样**：将积分区域分层，各层独立采样。

## 5. 误差分析

### 5.1 蒙特卡洛误差

**标准误**：
$$SE = \frac{\sigma}{\sqrt{n}}$$

**置信区间**：
$$\hat{I} \pm z_{\alpha/2} \cdot SE$$

### 5.2 收敛速度

**蒙特卡洛方法**：O(1/√n)，与维度无关。

**数值积分**：高维时维度灾难。

**优势**：高维积分蒙特卡洛更高效。

## 6. 实际应用案例

### 6.1 圆周率估计

```python
import numpy as np

def estimate_pi(n):
    """用蒙特卡洛方法估计π"""
    # 在单位正方形内随机采样
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    
    # 计算落入单位圆内的比例
    inside = (x**2 + y**2) <= 1
    pi_estimate = 4 * np.sum(inside) / n
    
    # 标准误
    se = 4 * np.sqrt(np.var(inside) / n)
    
    return pi_estimate, se

# 不同样本量的估计
for n in [1000, 10000, 100000, 1000000]:
    pi_est, se = estimate_pi(n)
    print(f"n={n:8d}, π≈{pi_est:.6f}±{se:.6f}")
```

### 6.2 期权定价

**欧式看涨期权**：
$$C = e^{-rT} E[\max(S_T - K, 0)]$$

```python
def monte_carlo_option_pricing(S0, K, T, r, sigma, n=100000):
    """
    蒙特卡洛期权定价
    S0: 当前股价
    K: 行权价
    T: 到期时间
    r: 无风险利率
    sigma: 波动率
    """
    # 模拟到期股价
    Z = np.random.standard_normal(n)
    ST = S0 * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
    
    # 计算期权收益
    payoffs = np.maximum(ST - K, 0)
    
    # 折现到当前
    option_price = np.exp(-r*T) * np.mean(payoffs)
    
    # 标准误
    se = np.exp(-r*T) * np.std(payoffs) / np.sqrt(n)
    
    return option_price, se
```

### 6.3 置信区间计算

```python
import numpy as np
from scipy import stats

def confidence_interval(data, confidence=0.95):
    """计算均值的置信区间"""
    n = len(data)
    mean = np.mean(data)
    se = stats.sem(data)
    
    # 使用t分布
    t_value = stats.t.ppf((1 + confidence) / 2, n - 1)
    margin = t_value * se
    
    return mean, mean - margin, mean + margin

# 示例
data = np.random.normal(100, 15, 50)
mean, lower, upper = confidence_interval(data)
print(f"样本均值: {mean:.2f}")
print(f"95%置信区间: ({lower:.2f}, {upper:.2f})")
```

## 7. 贝叶斯推断中的应用

### 7.1 后验分布采样

**MCMC方法**：利用大数定律估计后验量。

**后验均值估计**：
$$E[\theta|data] \approx \frac{1}{n}\sum_{i=1}^{n} \theta^{(i)}$$

其中 θ^{(i)} 是来自后验分布的样本。

### 7.2 可信区间

**后验分位数**：
- 95%可信区间：第2.5百分位到第97.5百分位
- 由样本分位数估计

## 8. 质量控制中的应用

### 8.1 控制图

**X̄控制图**：
- 中心线：μ
- 控制限：μ ± 3σ/√n

**理论依据**：中心极限定理。

### 8.2 抽样检验

**接受概率**：使用二项分布或正态近似。

**OC曲线**：操作特性曲线，描述接受概率与质量水平的关系。

## 9. Python实现示例

```python
import numpy as np
from scipy import stats

class MonteCarloEstimator:
    """蒙特卡洛估计器"""
    
    def __init__(self, n_samples=10000):
        self.n = n_samples
    
    def integrate(self, func, a, b):
        """积分估计"""
        x = np.random.uniform(a, b, self.n)
        values = func(x)
        estimate = (b - a) * np.mean(values)
        std_error = (b - a) * np.std(values) / np.sqrt(self.n)
        return estimate, std_error
    
    def expectation(self, func, sampler, n_samples=None):
        """期望估计"""
        n = n_samples or self.n
        samples = sampler(n)
        values = func(samples)
        estimate = np.mean(values)
        std_error = np.std(values) / np.sqrt(n)
        return estimate, std_error
    
    def probability(self, condition, sampler, n_samples=None):
        """概率估计"""
        n = n_samples or self.n
        samples = sampler(n)
        success = condition(samples)
        estimate = np.mean(success)
        std_error = np.std(success) / np.sqrt(n)
        return estimate, std_error

# 使用示例
mc = MonteCarloEstimator(100000)

# 估计 E[X^2] where X ~ N(0,1)
result, se = mc.expectation(
    func=lambda x: x**2,
    sampler=lambda n: np.random.standard_normal(n)
)
print(f"E[X²] ≈ {result:.4f} ± {se:.4f} (理论值 = 1)")

# 估计积分 ∫₀¹ x² dx
result, se = mc.integrate(func=lambda x: x**2, a=0, b=1)
print(f"∫₀¹ x² dx ≈ {result:.4f} ± {se:.4f} (理论值 = 1/3)")
```

## 10. 总结

**极限定理的核心应用**：

| 应用 | 使用定理 | 说明 |
|------|----------|------|
| 蒙特卡洛积分 | 大数定律 | 样本均值→期望 |
| 置信区间 | 中心极限定理 | 正态近似 |
| 假设检验 | 中心极限定理 | 检验统计量分布 |
| 正态近似 | 中心极限定理 | 离散分布近似 |
| 样本量确定 | 中心极限定理 | 精度控制 |

**关键公式**：
- 大数定律：X̄ → μ
- 中心极限定理：√n(X̄ - μ)/σ → N(0,1)
- 置信区间：X̄ ± z_{α/2}·σ/√n
- 蒙特卡洛误差：SE = σ/√n

---

**相关链接**：
- [[18_Law_of_Large_Numbers]] - 大数定律
- [[19_Central_Limit_Theorem]] - 中心极限定理
- [[21_Sample_Statistics]] - 样本与统计量
- [[23_Interval_Estimation]] - 区间估计

