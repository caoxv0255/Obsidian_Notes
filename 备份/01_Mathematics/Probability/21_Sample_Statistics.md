---
type: note
subject: probability
chapter: 21
created: 2026-04-03
status: complete
---

# 21 - 样本与统计量

## 1. 基本概念

### 1.1 总体与样本

**总体**：研究对象的全体，用分布函数 F(x) 或密度函数 f(x) 描述。

**样本**：从总体中抽取的部分个体，是随机变量 X₁, X₂, ..., Xₙ 的观测值。

**简单随机样本**：
1. 独立性：X₁, X₂, ..., Xₙ 相互独立
2. 同分布：X₁, X₂, ..., Xₙ 与总体同分布

### 1.2 样本的表示

**样本观测值**：x₁, x₂, ..., xₙ（小写，具体数值）

**样本作为随机变量**：X₁, X₂, ..., Xₙ（大写，随机变量）

**样本空间**：所有可能的样本观测值集合。

## 2. 统计量

### 2.1 定义

**统计量**：样本的函数，不依赖于未知参数。

$$T = T(X_1, X_2, \ldots, X_n)$$

**特点**：
- 是随机变量
- 不含未知参数
- 用于推断总体特征

### 2.2 常用统计量

**样本均值**：
$$\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i$$

**样本方差**：
$$S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2$$

**样本标准差**：
$$S = \sqrt{S^2}$$

**样本k阶原点矩**：
$$A_k = \frac{1}{n}\sum_{i=1}^{n} X_i^k$$

**样本k阶中心矩**：
$$B_k = \frac{1}{n}\sum_{i=1}^{n}(X_i - \bar{X})^k$$

### 2.3 顺序统计量

**定义**：将样本按大小排列：
$$X_{(1)} \leq X_{(2)} \leq \cdots \leq X_{(n)}$$

**样本中位数**：
$$M_e = \begin{cases} X_{((n+1)/2)} & n \text{为奇数} \\ \frac{1}{2}(X_{(n/2)} + X_{(n/2+1)}) & n \text{为偶数} \end{cases}$$

**样本极差**：
$$R = X_{(n)} - X_{(1)}$$

## 3. 样本均值和方差的性质

### 3.1 样本均值的性质

**期望**：
$$E[\bar{X}] = \mu$$

**方差**：
$$\text{Var}(\bar{X}) = \frac{\sigma^2}{n}$$

**分布**：
- 若总体正态：X̄ ~ N(μ, σ²/n)
- 大样本：X̄ ≈ N(μ, σ²/n)（CLT）

### 3.2 样本方差的性质

**期望**：
$$E[S^2] = \sigma^2$$

**方差**：
$$\text{Var}(S^2) = \frac{2\sigma^4}{n-1}$$（正态总体）

**与均值的关系**：
$$\sum_{i=1}^{n}(X_i - \bar{X})^2 = \sum_{i=1}^{n}X_i^2 - n\bar{X}^2$$

### 3.3 均值与方差的独立性

**定理**：若总体服从正态分布 N(μ, σ²)，则：
- X̄ 与 S² 独立
- (n-1)S²/σ² ~ χ²(n-1)

## 4. 抽样分布

### 4.1 χ²分布

**定义**：若 X₁, ..., Xₙ i.i.d. N(0,1)，则：
$$\chi^2 = \sum_{i=1}^{n} X_i^2 \sim \chi^2(n)$$

**性质**：
- E[χ²] = n
- Var(χ²) = 2n
- 可加性：χ²(m) + χ²(n) ~ χ²(m+n)

**应用**：样本方差的分布。

### 4.2 t分布

**定义**：若 X ~ N(0,1)，Y ~ χ²(n)，且独立，则：
$$T = \frac{X}{\sqrt{Y/n}} \sim t(n)$$

**性质**：
- 对称分布
- E[T] = 0（n > 1）
- Var(T) = n/(n-2)（n > 2）
- n → ∞ 时趋于标准正态

**应用**：σ未知时均值推断。

### 4.3 F分布

**定义**：若 X ~ χ²(m)，Y ~ χ²(n)，且独立，则：
$$F = \frac{X/m}{Y/n} \sim F(m, n)$$

**性质**：
- F ~ F(m,n) ⟹ 1/F ~ F(n,m)
- F₁₋α(m,n) = 1/Fα(n,m)

**应用**：两方差比较，方差分析。

## 5. 正态总体的抽样分布

### 5.1 单个正态总体

设 X₁, ..., Xₙ i.i.d. N(μ, σ²)：

**样本均值**：
$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

**标准化**：
$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$$

**σ未知时**：
$$\frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(n-1)$$

**样本方差**：
$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$$

### 5.2 两个正态总体

设 X₁, ..., Xₙ₁ i.i.d. N(μ₁, σ₁²)，Y₁, ..., Yₙ₂ i.i.d. N(μ₂, σ₂²)：

**均值差**：
$$\bar{X} - \bar{Y} \sim N\left(\mu_1 - \mu_2, \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}\right)$$

**方差比（σ₁² = σ₂² = σ²）**：
$$\frac{S_1^2}{S_2^2} \sim F(n_1-1, n_2-1)$$

**均值差的t分布（σ₁ = σ₂）**：
$$\frac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{S_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t(n_1 + n_2 - 2)$$

其中 $S_p^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}$。

## 6. 大样本性质

### 6.1 样本均值

**大数定律**：X̄ → μ（概率收敛）

**中心极限定理**：
$$\sqrt{n}\frac{\bar{X} - \mu}{\sigma} \xrightarrow{d} N(0,1)$$

### 6.2 样本方差

**一致性**：S² → σ²（概率收敛）

**渐近分布**：
$$\sqrt{n}(S^2 - \sigma^2) \xrightarrow{d} N(0, 2\sigma^4)$$

### 6.3 样本比例

设 X ~ B(n, p)，p̂ = X/n。

**期望和方差**：
- E[p̂] = p
- Var(p̂) = p(1-p)/n

**渐近分布**：
$$\sqrt{n}\frac{\hat{p} - p}{\sqrt{p(1-p)}} \xrightarrow{d} N(0,1)$$

## 7. 充分统计量

### 7.1 定义

**充分统计量**：统计量 T(X) 对于参数 θ 是充分的，如果给定 T = t 时样本的条件分布不依赖于 θ。

### 7.2 因子分解定理

**定理**：T 是 θ 的充分统计量 ⟺ 存在函数 g 和 h 使得：
$$f(x; \theta) = g(T(x), \theta) \cdot h(x)$$

### 7.3 例子

**伯努利分布**：$\sum X_i$ 是 p 的充分统计量

**正态分布（μ未知，σ已知）**：$\sum X_i$ 是 μ 的充分统计量

**正态分布（μ已知，σ未知）**：$\sum(X_i - \mu)^2$ 是 σ² 的充分统计量

## 8. Python实现

```python
import numpy as np
from scipy import stats

class SampleStatistics:
    """样本统计量计算"""
    
    def __init__(self, data):
        self.data = np.array(data)
        self.n = len(data)
    
    def mean(self):
        """样本均值"""
        return np.mean(self.data)
    
    def variance(self, ddof=1):
        """样本方差（默认无偏）"""
        return np.var(self.data, ddof=ddof)
    
    def std(self, ddof=1):
        """样本标准差"""
        return np.std(self.data, ddof=ddof)
    
    def median(self):
        """样本中位数"""
        return np.median(self.data)
    
    def range(self):
        """极差"""
        return np.max(self.data) - np.min(self.data)
    
    def quartiles(self):
        """四分位数"""
        return np.percentile(self.data, [25, 50, 75])
    
    def skewness(self):
        """偏度"""
        return stats.skew(self.data)
    
    def kurtosis(self):
        """峰度"""
        return stats.kurtosis(self.data)
    
    def summary(self):
        """统计摘要"""
        return {
            'n': self.n,
            'mean': self.mean(),
            'std': self.std(),
            'var': self.variance(),
            'min': np.min(self.data),
            'Q1': np.percentile(self.data, 25),
            'median': self.median(),
            'Q3': np.percentile(self.data, 75),
            'max': np.max(self.data),
            'skewness': self.skewness(),
            'kurtosis': self.kurtosis()
        }

# 抽样分布模拟
def sampling_distribution_demo():
    """演示抽样分布"""
    np.random.seed(42)
    mu, sigma = 100, 15
    n_samples = 10000
    sample_size = 30
    
    # 生成样本均值
    sample_means = [np.mean(np.random.normal(mu, sigma, sample_size)) 
                    for _ in range(n_samples)]
    
    # 理论值
    theoretical_mean = mu
    theoretical_std = sigma / np.sqrt(sample_size)
    
    print("样本均值的抽样分布:")
    print(f"  理论均值: {theoretical_mean:.4f}")
    print(f"  模拟均值: {np.mean(sample_means):.4f}")
    print(f"  理论标准误: {theoretical_std:.4f}")
    print(f"  模拟标准误: {np.std(sample_means):.4f}")
    
    # 正态性检验
    stat, p = stats.normaltest(sample_means)
    print(f"  正态性检验 p值: {p:.4f}")
    
    return sample_means

# 示例
if __name__ == "__main__":
    # 生成样本数据
    data = np.random.normal(100, 15, 50)
    stats_obj = SampleStatistics(data)
    
    print("样本统计量:")
    for key, value in stats_obj.summary().items():
        print(f"  {key}: {value:.4f}")
    
    print("\n抽样分布演示:")
    sampling_distribution_demo()
```

## 9. 总结

**关键统计量**：

| 统计量 | 公式 | 性质 |
|--------|------|------|
| 样本均值 | X̄ = (1/n)ΣXᵢ | E[X̄]=μ, Var(X̄)=σ²/n |
| 样本方差 | S² = (1/(n-1))Σ(Xᵢ-X̄)² | E[S²]=σ² |
| 样本中位数 | M_e | 抗异常值 |

**抽样分布**：

| 统计量 | 总体 | 分布 |
|--------|------|------|
| X̄ | N(μ, σ²) | N(μ, σ²/n) |
| (n-1)S²/σ² | N(μ, σ²) | χ²(n-1) |
| √n(X̄-μ)/S | N(μ, σ²) | t(n-1) |

**重要定理**：
- 大数定律：保证一致性
- 中心极限定理：提供渐近分布
- 因子分解定理：识别充分统计量

---

**相关链接**：
- [[14_Expectation]] - 数学期望
- [[15_Variance]] - 方差与标准差
- [[18_Law_of_Large_Numbers]] - 大数定律
- [[19_Central_Limit_Theorem]] - 中心极限定理
- [[22_Point_Estimation]] - 点估计
