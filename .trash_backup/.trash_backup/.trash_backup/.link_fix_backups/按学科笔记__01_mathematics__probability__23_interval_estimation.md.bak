---
type: note
subject: probability
chapter: 23
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 23 - 区间估计

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

## 1. 区间估计的概念

### 1.1 定义

**置信区间**：对于参数 θ，若统计量 θ̂_L 和 θ̂_U 满足：
$$P(\hat{\theta}_L \leq \theta \leq \hat{\theta}_U) = 1 - \alpha$$

则称 [θ̂_L, θ̂_U] 为 θ 的置信水平 1-α 的置信区间。

**置信水平**：区间包含真值的概率，常用 0.90, 0.95, 0.99。

**置信限**：θ̂_L 为置信下限，θ̂_U 为置信上限。

### 1.2 与点估计的区别

| 点估计 | 区间估计 |
|--------|----------|
| 给出一个数值 | 给出一个范围 |
| 没有精度信息 | 反映估计精度 |
| 更简洁 | 更全面 |

### 1.3 置信区间的解释

**频率学派解释**：若重复抽样多次，约 (1-α)×100% 的置信区间会包含真值。

**注意**：不是"真值落在区间内的概率"，真值是固定的。

## 2. 正态总体均值的置信区间

### 2.1 σ已知

**枢轴量**：
$$Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$$

**置信区间**：
$$\bar{X} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

其中 z_{α/2} 是标准正态分布的上 α/2 分位数。

### 2.2 σ未知

**枢轴量**：
$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(n-1)$$

**置信区间**：
$$\bar{X} \pm t_{\alpha/2, n-1} \cdot \frac{S}{\sqrt{n}}$$

**完整例题**：
某批零件的寿命服从近似正态分布，抽取 12 个样本，得到
$$\bar{X} = 48.6, \qquad S = 4.2$$
求总体平均寿命的 95% 置信区间。

**解**：由于总体标准差未知，使用 t 区间。这里 n = 12，故自由度为 11，取
$$t_{0.025,11} \approx 2.201$$

于是误差限为
$$2.201 \cdot \frac{4.2}{\sqrt{12}} \approx 2.67$$

所以 95% 置信区间为
$$48.6 \pm 2.67$$
$$\Rightarrow [45.93,\ 51.27]$$

**直观理解**：σ 未知时，我们用样本标准差 S 代替 σ，因此区间会比“σ已知”的情形更保守一些；样本越小，t 分布尾部越厚，这种保守性越明显。

### 2.3 单侧置信区间

**置信上限**：
$$\mu < \bar{X} + t_{\alpha, n-1} \cdot \frac{S}{\sqrt{n}}$$

**置信下限**：
$$\mu > \bar{X} - t_{\alpha, n-1} \cdot \frac{S}{\sqrt{n}}$$

## 3. 正态总体方差的置信区间

### 3.1 枢轴量

$$\chi^2 = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$$

### 3.2 置信区间

$$\left(\frac{(n-1)S^2}{\chi^2_{\alpha/2, n-1}}, \frac{(n-1)S^2}{\chi^2_{1-\alpha/2, n-1}}\right)$$

### 3.3 标准差的置信区间

取置信区间端点的平方根。

## 4. 两个正态总体的比较

### 4.1 均值差的置信区间

**情况1：σ₁², σ₂² 已知**

$$\bar{X}_1 - \bar{X}_2 \pm z_{\alpha/2} \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$$

**情况2：σ₁² = σ₂² = σ² 未知**

**合并方差**：
$$S_p^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}$$

**置信区间**：
$$(\bar{X}_1 - \bar{X}_2) \pm t_{\alpha/2, n_1+n_2-2} \cdot S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$$

**情况3：σ₁² ≠ σ₂² 且未知（Welch）**

$$t' = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{S_1^2/n_1 + S_2^2/n_2}}$$

自由度近似为：
$$df \approx \frac{(S_1^2/n_1 + S_2^2/n_2)^2}{\frac{(S_1^2/n_1)^2}{n_1-1} + \frac{(S_2^2/n_2)^2}{n_2-1}}$$

### 4.2 方差比的置信区间

**枢轴量**：
$$F = \frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} \sim F(n_1-1, n_2-1)$$

**置信区间**：
$$\left(\frac{S_1^2}{S_2^2} \cdot \frac{1}{F_{\alpha/2, n_1-1, n_2-1}}, \frac{S_1^2}{S_2^2} \cdot F_{\alpha/2, n_2-1, n_1-1}\right)$$

## 5. 比例的置信区间

### 5.1 单个比例

**Wald区间**：
$$\hat{p} \pm z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

**Wilson区间**（更精确）：
$$\frac{\hat{p} + z_{\alpha/2}^2/(2n) \pm z_{\alpha/2}\sqrt{\hat{p}(1-\hat{p})/n + z_{\alpha/2}^2/(4n^2)}}{1 + z_{\alpha/2}^2/n}$$

### 5.2 比例差的置信区间

$$\hat{p}_1 - \hat{p}_2 \pm z_{\alpha/2}\sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$$

## 6. 非正态总体的置信区间

### 6.1 大样本方法

**中心极限定理**：当 n 足够大时：
$$\frac{\bar{X} - \mu}{S/\sqrt{n}} \approx N(0, 1)$$

**置信区间**：
$$\bar{X} \pm z_{\alpha/2} \cdot \frac{S}{\sqrt{n}}$$

### 6.2 Bootstrap方法

**步骤**：
1. 从样本中有放回抽样，得到Bootstrap样本
2. 计算统计量
3. 重复多次，得到统计量的经验分布
4. 取分位数作为置信区间

## 7. 样本量的确定

### 7.1 估计均值

给定置信水平 1-α 和允许误差 E：
$$n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2$$

**问题**：σ 未知。解决方法：
- 预调查估计 σ
- 使用历史数据

### 7.2 估计比例

$$n = \frac{z_{\alpha/2}^2 \cdot p(1-p)}{E^2}$$

**保守估计**：取 p = 0.5（最大方差）：
$$n = \frac{z_{\alpha/2}^2}{4E^2}$$

## 8. Python实现

```python
import numpy as np
from scipy import stats

class IntervalEstimation:
    """区间估计"""
    
    @staticmethod
    def mean_ci(data, confidence=0.95, sigma=None):
        """
        均值的置信区间
        sigma: 总体标准差（已知时）
        """
        n = len(data)
        x_bar = np.mean(data)
        s = np.std(data, ddof=1)
        alpha = 1 - confidence
        
        if sigma is not None:
            # σ已知
            z = stats.norm.ppf(1 - alpha/2)
            margin = z * sigma / np.sqrt(n)
        else:
            # σ未知
            t = stats.t.ppf(1 - alpha/2, n-1)
            margin = t * s / np.sqrt(n)
        
        return x_bar - margin, x_bar + margin
    
    @staticmethod
    def variance_ci(data, confidence=0.95):
        """方差的置信区间"""
        n = len(data)
        s2 = np.var(data, ddof=1)
        alpha = 1 - confidence
        
        chi2_lower = stats.chi2.ppf(alpha/2, n-1)
        chi2_upper = stats.chi2.ppf(1 - alpha/2, n-1)
        
        lower = (n-1) * s2 / chi2_upper
        upper = (n-1) * s2 / chi2_lower
        
        return lower, upper
    
    @staticmethod
    def proportion_ci(n_success, n, confidence=0.95):
        """比例的置信区间"""
        p_hat = n_success / n
        alpha = 1 - confidence
        z = stats.norm.ppf(1 - alpha/2)
        
        # Wald区间
        margin = z * np.sqrt(p_hat * (1 - p_hat) / n)
        return p_hat - margin, p_hat + margin
    
    @staticmethod
    def mean_diff_ci(data1, data2, confidence=0.95, equal_var=True):
        """均值差的置信区间"""
        n1, n2 = len(data1), len(data2)
        x1_bar, x2_bar = np.mean(data1), np.mean(data2)
        s1, s2 = np.std(data1, ddof=1), np.std(data2, ddof=1)
        alpha = 1 - confidence
        
        if equal_var:
            # 合并方差
            sp2 = ((n1-1)*s1**2 + (n2-1)*s2**2) / (n1 + n2 - 2)
            sp = np.sqrt(sp2)
            t = stats.t.ppf(1 - alpha/2, n1 + n2 - 2)
            margin = t * sp * np.sqrt(1/n1 + 1/n2)
        else:
            # Welch
            se = np.sqrt(s1**2/n1 + s2**2/n2)
            df = (s1**2/n1 + s2**2/n2)**2 / ((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1))
            t = stats.t.ppf(1 - alpha/2, df)
            margin = t * se
        
        diff = x1_bar - x2_bar
        return diff - margin, diff + margin

def bootstrap_ci(data, stat_func, n_bootstrap=10000, confidence=0.95):
    """Bootstrap置信区间"""
    n = len(data)
    stats = []
    
    for _ in range(n_bootstrap):
        sample = np.random.choice(data, size=n, replace=True)
        stats.append(stat_func(sample))
    
    alpha = 1 - confidence
    lower = np.percentile(stats, 100 * alpha/2)
    upper = np.percentile(stats, 100 * (1 - alpha/2))
    
    return lower, upper

# 示例
if __name__ == "__main__":
    np.random.seed(42)
    
    # 生成数据
    data = np.random.normal(100, 15, 50)
    
    # 均值置信区间
    ci = IntervalEstimation.mean_ci(data)
    print(f"均值95%置信区间: ({ci[0]:.2f}, {ci[1]:.2f})")
    
    # 方差置信区间
    ci_var = IntervalEstimation.variance_ci(data)
    print(f"方差95%置信区间: ({ci_var[0]:.2f}, {ci_var[1]:.2f})")
    
    # 比例置信区间
    ci_prop = IntervalEstimation.proportion_ci(30, 100)
    print(f"比例95%置信区间: ({ci_prop[0]:.4f}, {ci_prop[1]:.4f})")
    
    # Bootstrap
    ci_boot = bootstrap_ci(data, np.mean)
    print(f"Bootstrap均值置信区间: ({ci_boot[0]:.2f}, {ci_boot[1]:.2f})")
```

## 9. 置信区间公式汇总

| 参数 | 条件 | 置信区间 |
|------|------|----------|
| μ | σ已知 | X̄ ± z_{α/2}·σ/√n |
| μ | σ未知 | X̄ ± t_{α/2,n-1}·S/√n |
| σ² | - | ((n-1)S²/χ²_{α/2}, (n-1)S²/χ²_{1-α/2}) |
| μ₁-μ₂ | σ相等 | (X̄₁-X̄₂) ± t·Sₚ√(1/n₁+1/n₂) |
| p | 大样本 | p̂ ± z_{α/2}√(p̂(1-p̂)/n) |

## 10. 总结

**置信区间的核心要素**：
1. 点估计（中心）
2. 标准误（宽度）
3. 置信水平（概率保证）

**构造置信区间的方法**：
1. 枢轴量法
2. 大样本近似
3. Bootstrap

**应用注意事项**：
- 样本量要足够大
- 检查分布假设
- 理解置信区间的正确含义

---

**相关链接**：
- [[21_Sample_Statistics]] - 样本与统计量
- [[22_Point_Estimation]] - 点估计
- [[24_Hypothesis_Testing]] - 假设检验

