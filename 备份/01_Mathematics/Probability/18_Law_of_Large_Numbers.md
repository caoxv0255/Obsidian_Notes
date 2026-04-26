---
type: note
subject: probability
chapter: 18
created: 2026-04-03
status: complete
---

# 18 - 大数定律

## 1. 大数定律的意义

### 1.1 频率稳定性

**经验事实**：当试验次数很大时，事件发生的频率趋于稳定，接近某个常数。

**例**：抛硬币
- n = 10：频率波动大
- n = 100：频率接近 0.5
- n = 1000：频率稳定在 0.5 附近

**问题**：如何从数学上严格证明这种现象？

**答案**：大数定律！

### 1.2 大数定律的核心思想

**直观**：随机现象在大量重复试验中呈现出统计规律性。

**数学表述**：样本均值依概率收敛（或几乎必然收敛）到期望值。

$$\bar{X}_n = \frac{1}{n}\sum_{i=1}^{n} X_i \to \mu \quad (n \to \infty)$$

## 2. 切比雪夫不等式

### 2.1 切比雪夫不等式

**定理**：设随机变量 X 的期望为 μ，方差为 σ²，则对任意 ε > 0：
$$P(|X - \mu| \geq \varepsilon) \leq \frac{\sigma^2}{\varepsilon^2}$$

**等价形式**：
$$P(|X - \mu| < \varepsilon) \geq 1 - \frac{\sigma^2}{\varepsilon^2}$$

**证明**：
$$\sigma^2 = E[(X-\mu)^2] = \int_{-\infty}^{+\infty} (x-\mu)^2 f(x) dx$$
$$\geq \int_{|x-\mu| \geq \varepsilon} (x-\mu)^2 f(x) dx \geq \varepsilon^2 \int_{|x-\mu| \geq \varepsilon} f(x) dx = \varepsilon^2 P(|X-\mu| \geq \varepsilon)$$

### 2.2 切比雪夫不等式的意义

**作用**：
1. 仅需知道期望和方差，即可估计概率
2. 不需要知道具体分布
3. 提供概率的保守估计

**例**：某考试平均分 75，标准差 10，估计分数在 55-95 之间的概率。

**解**：P(|X-75| ≥ 20) ≤ 10²/20² = 0.25
P(55 < X < 95) = P(|X-75| < 20) ≥ 0.75

**注意**：切比雪夫不等式给出的是下界，实际概率可能更大。

### 2.3 马尔可夫不等式

**定理**：若 X ≥ 0，E[X] = μ，则对任意 a > 0：
$$P(X \geq a) \leq \frac{\mu}{a}$$

**证明**：
$$\mu = E[X] = \int_0^{+\infty} x f(x) dx \geq \int_a^{+\infty} x f(x) dx \geq a \int_a^{+\infty} f(x) dx = a P(X \geq a)$$

**应用**：切比雪夫不等式是马尔可夫不等式的推论（应用于 (X-μ)²）。

## 3. 弱大数定律

### 3.1 弱大数定律（切比雪夫形式）

**定理**：设 X₁, X₂, ... 为独立同分布随机变量，E[Xᵢ] = μ，Var(Xᵢ) = σ² < ∞，则对任意 ε > 0：
$$\lim_{n \to \infty} P\left(\left|\frac{1}{n}\sum_{i=1}^{n} X_i - \mu\right| \geq \varepsilon\right) = 0$$

即样本均值**依概率收敛**到期望值。

**证明**：设 Sₙ = X₁ + ... + Xₙ，则：
- E[Sₙ/n] = μ
- Var(Sₙ/n) = σ²/n

由切比雪夫不等式：
$$P\left(\left|\frac{S_n}{n} - \mu\right| \geq \varepsilon\right) \leq \frac{\sigma^2/n}{\varepsilon^2} \to 0 \quad (n \to \infty)$$

### 3.2 辛钦弱大数定律

**定理**：设 X₁, X₂, ... 为独立同分布随机变量，E[Xᵢ] = μ < ∞（方差可以不存在），则：
$$\frac{1}{n}\sum_{i=1}^{n} X_i \xrightarrow{P} \mu$$

**意义**：不需要方差存在，只要期望存在即可。

**证明**：使用特征函数方法（略）。

### 3.3 依概率收敛

**定义**：随机变量序列 {Xₙ} **依概率收敛**到 X，记作 Xₙ →ᴾ X，若对任意 ε > 0：
$$\lim_{n \to \infty} P(|X_n - X| \geq \varepsilon) = 0$$

**性质**：
1. 若 Xₙ →ᴾ X，Yₙ →ᴾ Y，则 Xₙ + Yₙ →ᴾ X + Y
2. 若 g 连续，Xₙ →ᴾ X，则 g(Xₙ) →ᴾ g(X)

### 3.4 弱大数定律的例子

**例1**（伯努利试验）：设 Xᵢ 为第 i 次伯努利试验的结果（0或1），p 为成功概率，则：
$$\frac{1}{n}\sum_{i=1}^{n} X_i \xrightarrow{P} p$$

即成功频率依概率收敛到成功概率。

**例2**（蒙特卡洛积分）：计算 I = ∫₀¹ f(x) dx
- 生成 U₁, U₂, ..., Uₙ ~ U(0,1)
- 计算 Īₙ = (1/n) Σf(Uᵢ)
- 由弱大数定律：Īₙ →ᴾ I

## 4. 强大数定律

### 4.1 强大数定律

**定理**（柯尔莫哥洛夫）：设 X₁, X₂, ... 为独立同分布随机变量，E[Xᵢ] = μ < ∞，则：
$$P\left(\lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^{n} X_i = \mu\right) = 1$$

即样本均值**几乎必然收敛**到期望值。

**意义**：
- 比弱大数定律更强
- 保证样本均值最终收敛到期望值（概率为1）
- 例外事件发生的概率为0

### 4.2 几乎必然收敛

**定义**：随机变量序列 {Xₙ} **几乎必然收敛**到 X，记作 Xₙ →ᵃˢ X，若：
$$P\left(\lim_{n \to \infty} X_n = X\right) = 1$$

**等价定义**：对任意 ε > 0：
$$P\left(\limsup_{n \to \infty} |X_n - X| \geq \varepsilon\right) = 0$$

或：
$$P\left(\bigcap_{m=1}^{\infty} \bigcup_{n=m}^{\infty} \{|X_n - X| \geq \varepsilon\}\right) = 0$$

### 4.3 收敛性的关系

**定理**：几乎必然收敛 ⟹ 依概率收敛（反之不成立）

**反例**：考虑 [0,1] 上独立随机变量序列：
$$X_n = \begin{cases} 1, & U_n \in [0, 1/n] \\ 0, & \text{其他} \end{cases}$$

其中 Uₙ ~ U(0,1) 独立。

- 依概率收敛：P(|Xₙ - 0| ≥ 1) = P(Xₙ = 1) = 1/n → 0
- 不几乎必然收敛：Xₙ = 1 无穷多次发生（Borel-Cantelli引理）

### 4.4 波莱尔强大数定律

**定理**（波莱尔）：设 Sₙ 为 n 次独立伯努利试验中成功的次数，p 为成功概率，则：
$$P\left(\lim_{n \to \infty} \frac{S_n}{n} = p\right) = 1$$

**意义**：频率几乎必然收敛到概率。

## 5. 大数定律的应用

### 5.1 统计推断

**参数估计**：
- 样本均值是总体均值的一致估计量
- 样本方差是总体方差的一致估计量

**依据**：弱大数定律保证估计量收敛到真实值。

### 5.2 蒙特卡洛方法

**计算积分**：I = ∫f(x) dx
- 从分布 p(x) 抽取样本 x₁, ..., xₙ
- 估计：Ī = (1/n) Σf(xᵢ)/p(xᵢ)
- 由强大数定律：Ī → I (a.s.)

**应用**：
- 高维积分
- 复杂概率计算
- 物理模拟

### 5.3 机器学习

**经验风险最小化**：
$$\hat{R}_n(\theta) = \frac{1}{n}\sum_{i=1}^{n} L(y_i, f_\theta(x_i))$$

由大数定律：
$$\hat{R}_n(\theta) \xrightarrow{P} R(\theta) = E[L(Y, f_\theta(X))]$$

**意义**：经验风险收敛到期望风险。

### 5.4 博弈论

**例**：重复博弈中，平均收益收敛到期望收益。

### 5.5 保险业

**风险池化**：大量独立风险的平均损失趋于稳定。

## 6. 证明方法简介

### 6.1 切比雪夫方法

**步骤**：
1. 计算样本均值的期望和方差
2. 应用切比雪夫不等式
3. 取极限

**优点**：简单直观
**缺点**：需要方差存在

### 6.2 特征函数方法

**思路**：
1. 计算样本均值的特征函数
2. 利用特征函数的性质证明收敛

**优点**：不需要方差存在
**应用**：证明辛钦弱大数定律

### 6.3 鞅方法

**定义**：随机变量序列 {Mₙ} 称为鞅，若 E[Mₙ₊₁|M₁, ..., Mₙ] = Mₙ。

**定理**（鞅收敛定理）：有界鞅几乎必然收敛。

**应用**：证明强大数定律。

## 7. Borel-Cantelli引理

### 7.1 第一引理

**定理**：若 ΣP(Aₙ) < ∞，则：
$$P\left(\bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} A_k\right) = 0$$

即：若事件概率之和有限，则这些事件无穷多次发生的概率为0。

**意义**："坏事件"无穷多次发生的概率为0。

### 7.2 第二引理

**定理**：若 {Aₙ} 相互独立且 ΣP(Aₙ) = ∞，则：
$$P\left(\bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} A_k\right) = 1$$

即：若独立事件概率之和发散，则这些事件无穷多次发生的概率为1。

### 7.3 应用

**例**（强大数定律的证明）：证明 P(|Sₙ/n - μ| ≥ ε 无穷多次) = 0。

**思路**：
1. 证明 ΣP(|Sₙ²/n² - μ| ≥ ε) < ∞（需要更高阶矩）
2. 由第一引理，无穷多次偏离的概率为0
3. 对所有有理数 ε 应用，得几乎必然收敛

## 8. 大数定律的推广

### 8.1 非同分布情形

**定理**：设 X₁, X₂, ... 独立，E[Xᵢ] = μᵢ，Var(Xᵢ) = σᵢ²，若 Σσᵢ²/n² → 0，则：
$$\frac{1}{n}\sum_{i=1}^{n} (X_i - \mu_i) \xrightarrow{P} 0$$

### 8.2 依赖情形

**定理**（遍历定理）：对于平稳遍历序列：
$$\frac{1}{n}\sum_{i=1}^{n} X_i \to E[X_1] \quad \text{a.s.}$$

**应用**：时间序列分析、马尔可夫链。

### 8.3 加权情形

**定理**：设 {wₙ} 为权重序列，满足一定条件，则：
$$\frac{\sum_{i=1}^{n} w_i X_i}{\sum_{i=1}^{n} w_i} \xrightarrow{P} \mu$$

**应用**：加权平均、指数平滑。

## 9. 数值实验

### 9.1 抛硬币模拟

```python
import numpy as np
import matplotlib.pyplot as plt

# 模拟抛硬币
np.random.seed(42)
n = 10000
flips = np.random.binomial(1, 0.5, n)
frequencies = np.cumsum(flips) / np.arange(1, n+1)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(frequencies)
plt.axhline(y=0.5, color='r', linestyle='--')
plt.xlabel('n')
plt.ylabel('Frequency')
plt.title('Law of Large Numbers: Coin Flips')
plt.show()
```

**观察**：频率逐渐稳定在 0.5 附近。

### 9.2 不同分布的比较

```python
# 比较不同分布的收敛速度
distributions = {
    'Uniform(0,1)': lambda n: np.random.uniform(0, 1, n),
    'Normal(0,1)': lambda n: np.random.normal(0, 1, n),
    'Exponential(1)': lambda n: np.random.exponential(1, n)
}

for name, dist_func in distributions.items():
    samples = dist_func(10000)
    means = np.cumsum(samples) / np.arange(1, 10001)
    plt.plot(means, label=name)

plt.legend()
plt.xlabel('n')
plt.ylabel('Sample Mean')
plt.title('Convergence of Sample Means')
plt.show()
```

## 10. 小结

### 10.1 核心定理

| 定理 | 条件 | 结论 |
|------|------|------|
| 切比雪夫弱大数定律 | i.i.d., 期望和方差存在 | 依概率收敛 |
| 辛钦弱大数定律 | i.i.d., 期望存在 | 依概率收敛 |
| 强大数定律 | i.i.d., 期望存在 | 几乎必然收敛 |

### 10.2 关键概念

- **依概率收敛**：P(|Xₙ - X| ≥ ε) → 0
- **几乎必然收敛**：P(lim Xₙ = X) = 1
- **切比雪夫不等式**：概率估计的有力工具
- **频率稳定性**：大数定律的概率解释

### 10.3 应用领域

1. **统计推断**：估计量的一致性
2. **蒙特卡洛方法**：数值积分
3. **机器学习**：经验风险收敛
4. **金融**：风险分散
5. **物理**：统计力学

---

**参考文献**：
1. 《概率论基础》（第3版）- 李贤平
2. 《Probability: Theory and Examples》- Rick Durrett
3. 《A Probability Path》- Sidney Resnick

**下一章**：[[19_Central_Limit_Theorem]] - 中心极限定理
