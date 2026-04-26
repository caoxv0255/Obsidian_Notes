---
type: note
subject: probability
chapter: 22
created: 2026-04-03
status: complete
---

# 22 - 点估计

## 1. 点估计的基本概念

### 1.1 定义

**点估计**：用样本统计量的一个具体数值来估计总体参数。

**估计量**：用于估计参数的统计量，记为 θ̂。

**估计值**：估计量的具体取值。

### 1.2 评价标准

**无偏性**：E[θ̂] = θ

**有效性**：在无偏估计量中，方差最小。

**一致性**：θ̂ → θ（概率收敛）。

**均方误差**：
$$MSE(\hat{\theta}) = E[(\hat{\theta} - \theta)^2] = \text{Var}(\hat{\theta}) + [E(\hat{\theta}) - \theta]^2$$

## 2. 矩估计法

### 2.1 基本思想

**原理**：用样本矩估计总体矩。

**理论依据**：大数定律保证样本矩收敛于总体矩。

### 2.2 方法步骤

1. 写出总体k阶矩（用参数表示）
2. 写出样本k阶矩
3. 令二者相等，解方程组

### 2.3 例子

**例1：正态分布**

设 X ~ N(μ, σ²)，求 μ, σ² 的矩估计。

总体矩：
- E[X] = μ
- E[X²] = μ² + σ²

样本矩：
- A₁ = X̄
- A₂ = (1/n)ΣXᵢ²

令：
- μ̂ = X̄
- μ̂² + σ̂² = (1/n)ΣXᵢ²

解得：
- μ̂ = X̄
- σ̂² = (1/n)ΣXᵢ² - X̄²

**例2：均匀分布**

设 X ~ U(a, b)，求 a, b 的矩估计。

总体矩：
- E[X] = (a + b)/2
- Var(X) = (b - a)²/12

样本矩：
- X̄
- S²

解得：
- â = X̄ - √(3S²)
- b̂ = X̄ + √(3S²)

## 3. 最大似然估计

### 3.1 基本思想

**原理**：选择使样本出现概率最大的参数值。

**似然函数**：
$$L(\theta) = L(\theta; x_1, \ldots, x_n) = \prod_{i=1}^{n} f(x_i; \theta)$$

**对数似然函数**：
$$\ell(\theta) = \log L(\theta) = \sum_{i=1}^{n} \log f(x_i; \theta)$$

### 3.2 求解方法

**求导法**：
$$\frac{d\ell(\theta)}{d\theta} = 0$$

**迭代法**：当没有解析解时，使用数值优化。

### 3.3 例子

**例1：正态分布**

似然函数：
$$L(\mu, \sigma^2) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right)$$

对数似然：
$$\ell = -\frac{n}{2}\log(2\pi) - \frac{n}{2}\log\sigma^2 - \frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i - \mu)^2$$

求偏导，得：
- μ̂ = X̄
- σ̂² = (1/n)Σ(Xᵢ - X̄)²

**例2：泊松分布**

似然函数：
$$L(\lambda) = \prod_{i=1}^{n} \frac{\lambda^{x_i} e^{-\lambda}}{x_i!}$$

对数似然：
$$\ell = \sum_{i=1}^{n} x_i \log\lambda - n\lambda - \sum_{i=1}^{n} \log(x_i!)$$

求导：
$$\frac{d\ell}{d\lambda} = \frac{\sum x_i}{\lambda} - n = 0$$

得：λ̂ = X̄

**例3：均匀分布 U(0, θ)**

似然函数：
$$L(\theta) = \prod_{i=1}^{n} \frac{1}{\theta} = \theta^{-n}, \quad 0 \leq x_i \leq \theta$$

L(θ) 是 θ 的减函数，故取 θ 的最小可能值：
$$\hat{\theta} = \max(X_1, \ldots, X_n) = X_{(n)}$$

## 4. 估计量的性质

### 4.1 无偏性

**定义**：E[θ̂] = θ

**例子**：
- X̄ 是 μ 的无偏估计
- S² 是 σ² 的无偏估计
- (1/n)Σ(Xᵢ - X̄)² 是 σ² 的有偏估计

### 4.2 有效性

**定义**：在无偏估计量中，方差最小。

**Cramer-Rao下界**：
$$\text{Var}(\hat{\theta}) \geq \frac{1}{I(\theta)}$$

其中 I(θ) 是Fisher信息量：
$$I(\theta) = -E\left[\frac{\partial^2 \log f(X;\theta)}{\partial \theta^2}\right]$$

**有效估计量**：达到Cramer-Rao下界的无偏估计量。

### 4.3 一致性

**定义**：θ̂ₙ → θ（概率收敛）

**条件**：
- 无偏性 + Var(θ̂ₙ) → 0
- 或MSE → 0

### 4.4 渐近正态性

**定理**：在正则条件下，MLE满足：
$$\sqrt{n}(\hat{\theta} - \theta) \xrightarrow{d} N(0, I(\theta)^{-1})$$

## 5. Fisher信息量

### 5.1 定义

**Fisher信息量**：
$$I(\theta) = E\left[\left(\frac{\partial \log f(X;\theta)}{\partial \theta}\right)^2\right] = -E\left[\frac{\partial^2 \log f(X;\theta)}{\partial \theta^2}\right]$$

### 5.2 性质

1. **非负性**：I(θ) ≥ 0
2. **可加性**：独立样本的信息量相加
3. **变换法则**：若 φ = g(θ)，则 I(φ) = I(θ)/(g'(θ))²

### 5.3 例子

**正态分布 N(μ, σ²)（μ未知，σ已知）**：
$$I(\mu) = \frac{n}{\sigma^2}$$

**泊松分布 Poisson(λ)**：
$$I(\lambda) = \frac{n}{\lambda}$$

## 6. 贝叶斯估计

### 6.1 基本思想

**贝叶斯观点**：参数 θ 也是随机变量，有先验分布 π(θ)。

**后验分布**：
$$\pi(\theta|x) = \frac{f(x|\theta)\pi(\theta)}{f(x)} \propto f(x|\theta)\pi(\theta)$$

### 6.2 点估计

**后验均值**：
$$\hat{\theta}_B = E[\theta|X] = \int \theta \pi(\theta|X) d\theta$$

**后验中位数**：后验分布的中位数。

**后验众数（MAP）**：最大后验概率估计。

### 6.3 共轭先验

| 分布 | 先验 | 后验 |
|------|------|------|
| Bernoulli | Beta | Beta |
| Poisson | Gamma | Gamma |
| Normal(μ) | Normal | Normal |
| Normal(σ²) | Inverse-Gamma | Inverse-Gamma |

## 7. Python实现

```python
import numpy as np
from scipy import stats
from scipy.optimize import minimize

class PointEstimation:
    """点估计方法"""
    
    @staticmethod
    def moment_estimate(data, moments_func, n_params):
        """矩估计"""
        from scipy.optimize import fsolve
        
        # 计算样本矩
        sample_moments = [
            np.mean(data),
            np.mean(data**2),
            np.mean(data**3)
        ][:n_params]
        
        # 解方程组
        def equations(params):
            return [moments_func(params)[i] - sample_moments[i] 
                    for i in range(n_params)]
        
        initial = [1] * n_params
        return fsolve(equations, initial)
    
    @staticmethod
    def mle_normal(data):
        """正态分布MLE"""
        mu = np.mean(data)
        sigma2 = np.mean((data - mu)**2)
        return mu, np.sqrt(sigma2)
    
    @staticmethod
    def mle_poisson(data):
        """泊松分布MLE"""
        return np.mean(data)
    
    @staticmethod
    def mle_exponential(data):
        """指数分布MLE"""
        return np.mean(data)
    
    @staticmethod
    def mle_uniform(data):
        """均匀分布U(0,θ)的MLE"""
        return np.max(data)
    
    @staticmethod
    def mle_custom(data, log_likelihood, initial_params):
        """自定义MLE"""
        def neg_log_likelihood(params):
            return -log_likelihood(params, data)
        
        result = minimize(neg_log_likelihood, initial_params, method='BFGS')
        return result.x

# 贝叶斯估计
class BayesianEstimation:
    """贝叶斯估计"""
    
    @staticmethod
    def normal_normal(data, mu0, sigma0, sigma):
        """
        正态分布均值的后验（已知方差）
        先验: mu ~ N(mu0, sigma0^2)
        似然: X|mu ~ N(mu, sigma^2)
        """
        n = len(data)
        x_bar = np.mean(data)
        
        # 后验参数
        sigma0_sq = sigma0**2
        sigma_sq = sigma**2
        
        mu_n = (sigma0_sq * x_bar + (sigma_sq/n) * mu0) / (sigma0_sq + sigma_sq/n)
        sigma_n = np.sqrt(1 / (1/sigma0_sq + n/sigma_sq))
        
        return mu_n, sigma_n
    
    @staticmethod
    def bernoulli_beta(data, a, b):
        """
        伯努利分布参数的后验
        先验: p ~ Beta(a, b)
        似然: X|p ~ Bernoulli(p)
        """
        n = len(data)
        n_success = np.sum(data)
        
        # 后验参数
        a_post = a + n_success
        b_post = b + (n - n_success)
        
        return a_post, b_post

# 示例
if __name__ == "__main__":
    np.random.seed(42)
    
    # 生成正态数据
    true_mu, true_sigma = 100, 15
    data = np.random.normal(true_mu, true_sigma, 100)
    
    # MLE
    mu_mle, sigma_mle = PointEstimation.mle_normal(data)
    print(f"MLE: μ̂={mu_mle:.2f}, σ̂={sigma_mle:.2f}")
    print(f"真实值: μ={true_mu}, σ={true_sigma}")
    
    # 贝叶斯估计
    mu_post, sigma_post = BayesianEstimation.normal_normal(
        data, mu0=0, sigma0=100, sigma=true_sigma
    )
    print(f"后验均值: {mu_post:.2f}")
    
    # 泊松分布MLE
    poisson_data = np.random.poisson(5, 100)
    lambda_mle = PointEstimation.mle_poisson(poisson_data)
    print(f"\n泊松MLE: λ̂={lambda_mle:.2f}")
```

## 8. 估计方法比较

| 方法 | 优点 | 缺点 |
|------|------|------|
| 矩估计 | 简单直观 | 可能不如MLE有效 |
| MLE | 渐近最优 | 需要分布假设 |
| 贝叶斯 | 利用先验信息 | 先验选择主观 |

## 9. 总结

**点估计的核心**：
- 选择估计量
- 评价估计量
- 理解估计量的性质

**关键概念**：
- 无偏性：期望等于真值
- 有效性：方差最小
- 一致性：大样本收敛
- 渐近正态性：大样本近似

**方法选择**：
- 有先验信息：贝叶斯方法
- 无先验信息：MLE
- 简单快速：矩估计

---

**相关链接**：
- [[21_Sample_Statistics]] - 样本与统计量
- [[14_Expectation]] - 数学期望
- [[23_Interval_Estimation]] - 区间估计
