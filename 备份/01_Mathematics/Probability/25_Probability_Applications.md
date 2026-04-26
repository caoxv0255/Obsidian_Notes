---
type: note
subject: probability
chapter: 25
created: 2026-04-03
status: complete
---

# 25 - 概率论应用

## 1. 机器学习中的概率

### 1.1 贝叶斯分类

**贝叶斯定理**：
$$P(y|x) = \frac{P(x|y)P(y)}{P(x)}$$

**朴素贝叶斯分类器**：
$$\hat{y} = \arg\max_y P(y) \prod_{i=1}^{n} P(x_i|y)$$

**应用**：
- 垃圾邮件过滤
- 文本分类
- 情感分析

**完整例题：朴素贝叶斯邮件分类**

设要判断一封邮件是“垃圾邮件”还是“正常邮件”。已知：
- 先验概率：$P(\text{spam}) = 0.4$, $P(\text{ham}) = 0.6$
- 观测到两个二元特征：邮件中出现“free”，但没有出现“meeting”
- 条件概率：
    - $P(\text{free}|\text{spam}) = 0.7$, $P(\text{meeting}=0|\text{spam}) = 0.8$
    - $P(\text{free}|\text{ham}) = 0.1$, $P(\text{meeting}=0|\text{ham}) = 0.3$

**解**：朴素贝叶斯假设特征条件独立，因此只需比较后验的比例：
$$P(\text{spam}|x) \propto P(\text{spam})P(\text{free}|\text{spam})P(\text{meeting}=0|\text{spam})$$
$$= 0.4 \times 0.7 \times 0.8 = 0.224$$

$$P(\text{ham}|x) \propto P(\text{ham})P(\text{free}|\text{ham})P(\text{meeting}=0|\text{ham})$$
$$= 0.6 \times 0.1 \times 0.3 = 0.018$$

因为 $0.224 > 0.018$，所以判为**垃圾邮件**。

**直观理解**：朴素贝叶斯不是把特征“平均看待”，而是把“先验倾向”和“特征证据”连乘起来；像“free”这类强提示词会迅速把后验推向垃圾邮件一侧。

### 1.2 高斯混合模型

**模型**：
$$p(x) = \sum_{k=1}^{K} \pi_k N(x|\mu_k, \Sigma_k)$$

**参数估计**：EM算法

**应用**：
- 聚类
- 密度估计
- 异常检测

### 1.3 隐马尔可夫模型

**三要素**：
- 初始概率分布 π
- 转移概率矩阵 A
- 观测概率分布 B

**三个基本问题**：
1. 评估问题：前向-后向算法
2. 解码问题：Viterbi算法
3. 学习问题：Baum-Welch算法（EM）

## 2. 统计学习中的概率

### 2.1 最大似然估计

**原理**：选择使观测数据概率最大的参数。

**似然函数**：
$$L(\theta) = \prod_{i=1}^{n} p(x_i|\theta)$$

**对数似然**：
$$\ell(\theta) = \sum_{i=1}^{n} \log p(x_i|\theta)$$

### 2.2 最大后验估计

**原理**：选择使后验概率最大的参数。

$$\hat{\theta}_{MAP} = \arg\max_\theta P(\theta|X) = \arg\max_\theta P(X|\theta)P(\theta)$$

**正则化解释**：
- L2正则化 = 高斯先验
- L1正则化 = 拉普拉斯先验

### 2.3 贝叶斯推断

**核心思想**：参数也是随机变量。

**后验分布**：
$$P(\theta|X) \propto P(X|\theta)P(\theta)$$

**预测分布**：
$$P(x_{new}|X) = \int P(x_{new}|\theta)P(\theta|X)d\theta$$

## 3. 信息论中的概率

### 3.1 熵

**定义**：
$$H(X) = -\sum_{x} P(x)\log P(x)$$

**性质**：
- 非负性
- H(X) ≥ 0
- H(X) ≤ log|X|（均匀分布最大）

**含义**：随机变量的不确定性度量。

### 3.2 互信息

**定义**：
$$I(X;Y) = \sum_{x,y} P(x,y)\log\frac{P(x,y)}{P(x)P(y)}$$

**性质**：
- I(X;Y) = H(X) - H(X|Y)
- I(X;Y) ≥ 0
- I(X;Y) = I(Y;X)

**应用**：特征选择。

### 3.3 KL散度

**定义**：
$$D_{KL}(P||Q) = \sum_x P(x)\log\frac{P(x)}{Q(x)}$$

**性质**：
- 非负性
- 不对称性

**应用**：
- 变分推断
- 生成模型（VAE）

## 4. 金融工程中的概率

### 4.1 风险度量

**VaR（风险价值）**：
$$VaR_\alpha = \inf\{x : P(L > x) \leq \alpha\}$$

**CVaR（条件风险价值）**：
$$CVaR_\alpha = E[L|L > VaR_\alpha]$$

### 4.2 期权定价

**Black-Scholes模型**：
$$C = S_0 N(d_1) - Ke^{-rT}N(d_2)$$

其中：
$$d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$$
$$d_2 = d_1 - \sigma\sqrt{T}$$

### 4.3 投资组合理论

**均值-方差模型**：
$$\min_w w^T\Sigma w \quad \text{s.t.} \quad w^T\mu \geq r, \quad 1^Tw = 1$$

## 5. 通信系统中的概率

### 5.1 信道容量

**香农公式**：
$$C = B\log_2\left(1 + \frac{S}{N}\right)$$

### 5.2 误码率分析

**BPSK调制**：
$$P_e = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)$$

其中 Q(x) 是标准正态分布的尾概率。

## 6. 质量控制中的概率

### 6.1 控制图

**X̄控制图**：
- 中心线：μ
- 控制限：μ ± 3σ/√n

**原理**：3σ原则，正常情况下99.73%的点在控制限内。

### 6.2 抽样检验

**OC曲线**：接受概率与质量水平的关系。

**AQL**：可接受质量水平
**LTPD**：批容忍不合格品率

## 7. Python实现示例

### 7.1 朴素贝叶斯分类器

```python
import numpy as np
from collections import defaultdict

class NaiveBayes:
    def __init__(self):
        self.class_priors = {}
        self.feature_probs = defaultdict(dict)
    
    def fit(self, X, y):
        """训练"""
        classes = np.unique(y)
        n_samples = len(y)
        
        for c in classes:
            # 类先验概率
            self.class_priors[c] = np.sum(y == c) / n_samples
            
            # 条件概率（假设特征为二元）
            X_c = X[y == c]
            for j in range(X.shape[1]):
                self.feature_probs[c][j] = {
                    0: np.sum(X_c[:, j] == 0) / len(X_c) + 1e-10,
                    1: np.sum(X_c[:, j] == 1) / len(X_c) + 1e-10
                }
    
    def predict(self, X):
        """预测"""
        predictions = []
        for x in X:
            posteriors = {}
            for c in self.class_priors:
                log_prob = np.log(self.class_priors[c])
                for j, val in enumerate(x):
                    log_prob += np.log(self.feature_probs[c][j].get(val, 1e-10))
                posteriors[c] = log_prob
            predictions.append(max(posteriors, key=posteriors.get))
        return np.array(predictions)
```

### 7.2 高斯混合模型

```python
from sklearn.mixture import GaussianMixture
import numpy as np

def gmm_clustering(X, n_components=3):
    """GMM聚类"""
    gmm = GaussianMixture(n_components=n_components, random_state=42)
    gmm.fit(X)
    
    labels = gmm.predict(X)
    probs = gmm.predict_proba(X)
    
    return labels, probs, gmm
```

### 7.3 风险计算

```python
import numpy as np
from scipy import stats

def calculate_var(returns, confidence=0.95):
    """计算VaR"""
    return np.percentile(returns, (1 - confidence) * 100)

def calculate_cvar(returns, confidence=0.95):
    """计算CVaR"""
    var = calculate_var(returns, confidence)
    return np.mean(returns[returns <= var])

def black_scholes_call(S, K, T, r, sigma):
    """Black-Scholes期权定价"""
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    call = S * stats.norm.cdf(d1) - K * np.exp(-r*T) * stats.norm.cdf(d2)
    return call
```

## 8. 应用领域汇总

| 领域 | 概率方法 | 应用 |
|------|----------|------|
| 机器学习 | 贝叶斯推断 | 分类、聚类 |
| 信息论 | 熵、互信息 | 特征选择、压缩 |
| 金融 | 随机过程 | 风险管理、定价 |
| 通信 | 随机分析 | 信道设计 |
| 质量控制 | 统计推断 | 过程监控 |

## 9. 概率思维的重要性

### 9.1 不确定性建模

**确定性方法**：输出固定的预测值
**概率方法**：输出预测值及其不确定性

**优势**：
- 风险评估
- 决策支持
- 模型校准

### 9.2 数据驱动决策

**贝叶斯更新**：
$$P(\theta|data) \propto P(data|\theta)P(\theta)$$

**应用**：
- A/B测试
- 在线学习
- 增量更新

### 9.3 因果推断

**贝叶斯网络**：表示变量间的因果关系

**潜在结果框架**：处理效应的估计

## 10. 总结

**概率论的核心价值**：
1. 建模不确定性
2. 支持理性决策
3. 提供理论保证

**学习建议**：
1. 理解概率思维
2. 掌握常用分布
3. 练习实际应用
4. 结合编程实践

**延伸方向**：
- 贝叶斯统计
- 随机过程
- 统计学习理论
- 因果推断

---

**相关链接**：
- [[01_Probability_Axioms]] - 概率公理
- [[02_Conditional_Probability]] - 条件概率
- [[14_Expectation]] - 数学期望
- [[18_Law_of_Large_Numbers]] - 大数定律
- [[19_Central_Limit_Theorem]] - 中心极限定理
- [[22_Point_Estimation]] - 点估计
- [[24_Hypothesis_Testing]] - 假设检验
