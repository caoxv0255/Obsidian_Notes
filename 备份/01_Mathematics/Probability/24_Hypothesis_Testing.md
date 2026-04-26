---
type: note
subject: probability
chapter: 24
created: 2026-04-03
status: complete
---

# 24 - 假设检验

## 1. 假设检验的基本概念

### 1.1 基本思想

**假设检验**：根据样本信息判断关于总体的某个假设是否成立。

**基本步骤**：
1. 提出假设（原假设H₀和备择假设H₁）
2. 选择检验统计量
3. 确定显著性水平α
4. 计算检验统计量的值
5. 做出判断

### 1.2 两类假设

**原假设（H₀）**：待检验的假设，通常包含等号。

**备择假设（H₁）**：与原假设对立的假设。

**检验类型**：
- 双侧检验：H₀: θ = θ₀ vs H₁: θ ≠ θ₀
- 右侧检验：H₀: θ ≤ θ₀ vs H₁: θ > θ₀
- 左侧检验：H₀: θ ≥ θ₀ vs H₁: θ < θ₀

### 1.3 两类错误

|  | H₀为真 | H₀为假 |
|--|--------|--------|
| 接受H₀ | 正确 | 第二类错误(β) |
| 拒绝H₀ | 第一类错误(α) | 正确 |

**第一类错误**：弃真错误，P(拒绝H₀ | H₀为真) = α

**第二类错误**：取伪错误，P(接受H₀ | H₀为假) = β

**显著性水平**：α，通常取 0.05, 0.01。

**功效**：1 - β，正确拒绝错误原假设的概率。

## 2. 正态总体均值的检验

### 2.1 单个正态总体（σ已知）

**检验统计量**：
$$Z = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}} \sim N(0, 1)$$

**拒绝域**：
- 双侧：|Z| > z_{α/2}
- 右侧：Z > z_α
- 左侧：Z < -z_α

### 2.2 单个正态总体（σ未知）

**检验统计量**：
$$T = \frac{\bar{X} - \mu_0}{S/\sqrt{n}} \sim t(n-1)$$

**拒绝域**：
- 双侧：|T| > t_{α/2, n-1}
- 右侧：T > t_{α, n-1}
- 左侧：T < -t_{α, n-1}

**完整例题**：
某生产线随机抽取 16 个零件，测得平均长度为 10.3 mm，样本标准差为 0.8 mm。已知设计标准长度为 10 mm，试在显著性水平 0.05 下检验该生产线是否“平均长度大于标准值”。

**解**：提出假设
$$H_0: \mu \leq 10, \qquad H_1: \mu > 10$$

由于总体方差未知，使用单样本 t 检验：
$$T = \frac{10.3 - 10}{0.8/\sqrt{16}} = \frac{0.3}{0.2} = 1.5$$

查临界值：自由度为 15，右侧检验的临界值
$$t_{0.05,15} \approx 1.753$$

因为 $1.5 < 1.753$，所以在显著性水平 0.05 下**不拒绝** $H_0$。

若用 p 值判断，则
$$p = P(T > 1.5) \approx 0.077$$
也大于 0.05，因此结论一致。

**直观理解**：样本均值虽然高于 10，但这种偏高还不够“显著”；样本只有 16 个时，随机波动仍然比较大，所以不能轻易断言总体均值真的超过标准值。

### 2.3 两个正态总体均值比较

**情况1：σ₁² = σ₂² = σ² 未知**

$$T = \frac{\bar{X}_1 - \bar{X}_2}{S_p\sqrt{1/n_1 + 1/n_2}} \sim t(n_1 + n_2 - 2)$$

**情况2：σ₁² ≠ σ₂² 未知（Welch检验）**

$$T = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{S_1^2/n_1 + S_2^2/n_2}}$$

自由度由Welch-Satterthwaite公式确定。

### 2.4 配对样本检验

**检验统计量**：
$$T = \frac{\bar{D}}{S_D/\sqrt{n}} \sim t(n-1)$$

其中 Dᵢ = Xᵢ - Yᵢ 为配对差。

## 3. 正态总体方差的检验

### 3.1 单个正态总体

**检验统计量**：
$$\chi^2 = \frac{(n-1)S^2}{\sigma_0^2} \sim \chi^2(n-1)$$

**拒绝域**（双侧）：
$$\chi^2 < \chi^2_{1-\alpha/2, n-1} \quad \text{或} \quad \chi^2 > \chi^2_{\alpha/2, n-1}$$

### 3.2 两个正态总体

**检验统计量**：
$$F = \frac{S_1^2}{S_2^2} \sim F(n_1-1, n_2-1)$$

**拒绝域**（双侧）：
$$F < F_{1-\alpha/2, n_1-1, n_2-1} \quad \text{或} \quad F > F_{\alpha/2, n_1-1, n_2-1}$$

## 4. 比例的检验

### 4.1 单个比例

**大样本检验**：
$$Z = \frac{\hat{p} - p_0}{\sqrt{p_0(1-p_0)/n}} \approx N(0, 1)$$

**条件**：np₀ ≥ 5 且 n(1-p₀) ≥ 5。

### 4.2 两个比例比较

**检验统计量**：
$$Z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})(1/n_1 + 1/n_2)}}$$

其中 p̂ = (X₁ + X₂)/(n₁ + n₂) 为合并比例估计。

## 5. p值与决策

### 5.1 p值的定义

**p值**：在H₀为真时，观测到当前或更极端结果的概率。

### 5.2 p值的计算

**双侧检验**：
$$p = 2P(Z > |z_{obs}|)$$

**右侧检验**：
$$p = P(Z > z_{obs})$$

**左侧检验**：
$$p = P(Z < z_{obs})$$

### 5.3 决策规则

- p < α：拒绝H₀
- p ≥ α：不拒绝H₀

**优势**：p值提供比简单的"接受/拒绝"更多的信息。

## 6. 非参数检验

### 6.1 符号检验

**适用**：中位数检验，无需正态假设。

**统计量**：正号（或负号）的个数 S ~ B(n, 0.5)。

### 6.2 符号秩检验（Wilcoxon）

**适用**：配对样本比较。

**统计量**：W = Σ Rᵢ，其中 Rᵢ 是 |Dᵢ| 的秩。

### 6.3 秩和检验（Mann-Whitney U）

**适用**：两独立样本比较。

**统计量**：U = n₁n₂ + n₁(n₁+1)/2 - R₁

### 6.4 卡方检验

**拟合优度检验**：
$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i} \sim \chi^2(k-1)$$

**独立性检验**：
$$\chi^2 = \sum_{i,j} \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \sim \chi^2((r-1)(c-1))$$

## 7. 多重检验与校正

### 7.1 多重比较问题

**问题**：同时进行多次检验时，总体第一类错误率上升。

**总体错误率**：
$$\alpha_{family} = 1 - (1-\alpha)^m$$

### 7.2 校正方法

**Bonferroni校正**：
$$\alpha' = \alpha / m$$

**优点**：简单，保守。
**缺点**：检验次数多时过于保守。

**FDR控制（Benjamini-Hochberg）**：
控制错误发现率，更适用于大规模检验。

## 8. Python实现

```python
import numpy as np
from scipy import stats

class HypothesisTesting:
    """假设检验"""
    
    @staticmethod
    def one_sample_t_test(data, mu0, alternative='two-sided'):
        """单样本t检验"""
        n = len(data)
        x_bar = np.mean(data)
        s = np.std(data, ddof=1)
        
        t_stat = (x_bar - mu0) / (s / np.sqrt(n))
        df = n - 1
        
        if alternative == 'two-sided':
            p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
        elif alternative == 'greater':
            p_value = 1 - stats.t.cdf(t_stat, df)
        else:  # less
            p_value = stats.t.cdf(t_stat, df)
        
        return t_stat, p_value, df
    
    @staticmethod
    def two_sample_t_test(data1, data2, equal_var=True, alternative='two-sided'):
        """两样本t检验"""
        if equal_var:
            t_stat, p_value = stats.ttest_ind(data1, data2)
        else:
            t_stat, p_value = stats.ttest_ind(data1, data2, equal_var=False)
        
        return t_stat, p_value
    
    @staticmethod
    def paired_t_test(data1, data2, alternative='two-sided'):
        """配对t检验"""
        t_stat, p_value = stats.ttest_rel(data1, data2)
        return t_stat, p_value
    
    @staticmethod
    def proportion_test(n_success, n, p0, alternative='two-sided'):
        """比例检验"""
        p_hat = n_success / n
        se = np.sqrt(p0 * (1 - p0) / n)
        z_stat = (p_hat - p0) / se
        
        if alternative == 'two-sided':
            p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        elif alternative == 'greater':
            p_value = 1 - stats.norm.cdf(z_stat)
        else:
            p_value = stats.norm.cdf(z_stat)
        
        return z_stat, p_value
    
    @staticmethod
    def chi2_variance_test(data, sigma2_0):
        """方差检验"""
        n = len(data)
        s2 = np.var(data, ddof=1)
        
        chi2_stat = (n - 1) * s2 / sigma2_0
        p_value = 2 * min(stats.chi2.cdf(chi2_stat, n-1), 
                          1 - stats.chi2.cdf(chi2_stat, n-1))
        
        return chi2_stat, p_value
    
    @staticmethod
    def f_variance_test(data1, data2):
        """两方差比较检验"""
        s1, s2 = np.var(data1, ddof=1), np.var(data2, ddof=1)
        n1, n2 = len(data1), len(data2)
        
        f_stat = s1 / s2
        p_value = 2 * min(stats.f.cdf(f_stat, n1-1, n2-1),
                          1 - stats.f.cdf(f_stat, n1-1, n2-1))
        
        return f_stat, p_value

def chi2_independence_test(observed):
    """卡方独立性检验"""
    observed = np.array(observed)
    row_totals = observed.sum(axis=1, keepdims=True)
    col_totals = observed.sum(axis=0, keepdims=True)
    total = observed.sum()
    
    expected = row_totals * col_totals / total
    
    chi2_stat = ((observed - expected)**2 / expected).sum()
    df = (observed.shape[0] - 1) * (observed.shape[1] - 1)
    p_value = 1 - stats.chi2.cdf(chi2_stat, df)
    
    return chi2_stat, p_value, df

# 示例
if __name__ == "__main__":
    np.random.seed(42)
    
    # 单样本t检验
    data = np.random.normal(102, 15, 50)
    t_stat, p_value, df = HypothesisTesting.one_sample_t_test(data, mu0=100)
    print(f"单样本t检验: t={t_stat:.3f}, p={p_value:.4f}")
    
    # 两样本t检验
    data1 = np.random.normal(100, 15, 30)
    data2 = np.random.normal(105, 15, 30)
    t_stat, p_value = HypothesisTesting.two_sample_t_test(data1, data2)
    print(f"两样本t检验: t={t_stat:.3f}, p={p_value:.4f}")
    
    # 比例检验
    z_stat, p_value = HypothesisTesting.proportion_test(55, 100, p0=0.5)
    print(f"比例检验: z={z_stat:.3f}, p={p_value:.4f}")
    
    # 卡方独立性检验
    observed = [[20, 30], [40, 10]]
    chi2, p_value, df = chi2_independence_test(observed)
    print(f"卡方检验: χ²={chi2:.3f}, p={p_value:.4f}, df={df}")
```

## 9. 假设检验汇总表

| 检验类型 | 条件 | 统计量 | 分布 |
|----------|------|--------|------|
| 单均值 | σ已知 | Z | N(0,1) |
| 单均值 | σ未知 | T | t(n-1) |
| 均值差 | σ相等 | T | t(n₁+n₂-2) |
| 单方差 | - | χ² | χ²(n-1) |
| 方差比 | - | F | F(n₁-1,n₂-1) |
| 单比例 | 大样本 | Z | N(0,1) |

## 10. 总结

**假设检验的核心步骤**：
1. 建立假设
2. 选择统计量
3. 确定拒绝域
4. 计算并判断

**注意事项**：
- 第一类错误与第二类错误的权衡
- p值的正确理解
- 检验的前提条件
- 多重检验校正

**检验选择**：
- 正态总体：参数检验
- 非正态/小样本：非参数检验
- 大样本：渐近检验

---

**相关链接**：
- [[21_Sample_Statistics]] - 样本与统计量
- [[23_Interval_Estimation]] - 区间估计
- [[25_Probability_Applications]] - 概率论应用
