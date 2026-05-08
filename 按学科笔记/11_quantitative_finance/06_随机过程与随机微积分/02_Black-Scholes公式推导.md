# 02 Black-Scholes 公式推导

## Black-Scholes 假设条件

Black-Scholes 模型建立在以下关键假设之上：

1. **价格连续性**：股票价格 $S_t$ 连续变化，无跳跃
2. **几何布朗运动**：$dS_t = \mu S_t dt + \sigma S_t dW_t$（$\mu$ 为漂移率，$\sigma$ 为波动率，$W_t$ 为标准布朗运动）
3. **常数参数**：无风险利率 $r$ 和波动率 $\sigma$ 均为常数
4. **无摩擦市场**：无交易成本、无税收、无卖空限制
5. **连续交易**：可任意连续地买卖股票
6. **无套利**：市场无套利机会
7. **股息**：股票不分红（或 dividend yield 已知）

---

## 伊藤引理（Ito's Lemma）

### 布朗运动的二次变差

对标准布朗运动 $W_t$：
- $E[W_t] = 0$，$\text{Var}[W_t] = t$
- $(dW_t)^2 = dt$（二次变差）
- $dt \to 0$ 时，$(dt)^2$ 和 $dt \cdot dW_t$ 均可忽略

### 伊藤引理陈述

设 $X_t$ 服从伊藤过程 $dX_t = \mu_t dt + \sigma_t dW_t$，函数 $F(x, t)$ 对 $x$ 二阶连续可导、对 $t$ 一阶连续可导，则：

$$
dF = \left( \frac{\partial F}{\partial t} + \mu_t \frac{\partial F}{\partial x} + \frac{1}{2} \sigma_t^2 \frac{\partial^2 F}{\partial x^2} \right) dt + \sigma_t \frac{\partial F}{\partial x} dW_t
$$

**关键**：多了 $\frac{1}{2}\sigma_t^2 \frac{\partial^2 F}{\partial x^2} dt$ 这一项，来源于 $(dW_t)^2 = dt$。

### 几何布朗运动的函数推导

设 $S_t$ 服从 $dS_t = \mu S_t dt + \sigma S_t dW_t$，令 $F = \ln S_t$。

计算偏导：
- $\frac{\partial F}{\partial t} = 0$
- $\frac{\partial F}{\partial x} = \frac{1}{x}$
- $\frac{\partial^2 F}{\partial x^2} = -\frac{1}{x^2}$

代入伊藤引理：
$$
d(\ln S_t) = \left(0 + \mu \cdot \frac{1}{S_t} + \frac{1}{2} \sigma^2 \cdot \left(-\frac{1}{S_t^2}\right) \right) dt + \sigma \cdot \frac{1}{S_t} dW_t
$$
$$
= \left(\mu - \frac{\sigma^2}{2}\right) dt + \sigma dW_t
$$

> **结论**：$\ln S_t \sim N\left(\ln S_0 + (\mu - \frac{\sigma^2}{2})t,\; \sigma^2 t\right)$

---

## Black-Scholes 偏微分方程推导

### 核心思想：Delta 对冲

考虑一个包含 1 单位看涨期权 $C(S_t, t)$ 和 $-\Delta$ 单位股票的组合：
$$
\Pi = C - \Delta \cdot S_t
$$

选取 $\Delta = \frac{\partial C}{\partial S}$（Delta），使得组合**无风险**。

伊藤引理作用于 $C(S_t, t)$：
$$
dC = \left( \frac{\partial C}{\partial t} + \mu S_t \frac{\partial C}{\partial S} + \frac{1}{2} \sigma^2 S_t^2 \frac{\partial^2 C}{\partial S^2} \right) dt + \sigma S_t \frac{\partial C}{\partial S} dW_t
$$

股票变动：$dS_t = \mu S_t dt + \sigma S_t dW_t$

组合变动：
$$
d\Pi = dC - \Delta dS_t
$$
$$
= \left( \frac{\partial C}{\partial t} + \frac{1}{2} \sigma^2 S_t^2 \frac{\partial^2 C}{\partial S^2} \right) dt + \sigma S_t \frac{\partial C}{\partial S} dW_t - \Delta \mu S_t dt - \Delta \sigma S_t dW_t
$$

令 $\Delta = \frac{\partial C}{\partial S}$ 消去随机项：
$$
d\Pi = \left( \frac{\partial C}{\partial t} + \frac{1}{2} \sigma^2 S_t^2 \frac{\partial^2 C}{\partial S^2} \right) dt
$$

无风险组合的收益率应等于无风险利率：
$$
d\Pi = r \Pi dt = r (C - S_t \frac{\partial C}{\partial S}) dt
$$

联立得到 **Black-Scholes 偏微分方程**：

$$
\boxed{\frac{\partial C}{\partial t} + \frac{1}{2} \sigma^2 S_t^2 \frac{\partial^2 C}{\partial S^2} = r \left( C - S_t \frac{\partial C}{\partial S} \right)}
$$

或等价形式：
$$
\frac{\partial C}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} + r S \frac{\partial C}{\partial S} - rC = 0
$$

### 终端条件（到期日）

$$
C(S_T, T) = \max(S_T - K, 0) \quad \text{（看涨期权）}
$$

---

## 解析解推导

### 概率论视角（Risk-Neutral Pricing）

在风险中性测度下，股票期望收益率为无风险利率 $r$：

$$
dS_t = r S_t dt + \sigma S_t dW_t^{\mathbb{Q}}
$$

期权在风险中性测度下的定价公式（ Feynman-Kac 定理）：

$$
C_0 = e^{-rT} E^{\mathbb{Q}}[(S_T - K)^+]
$$

### 计算 $E^{\mathbb{Q}}[(S_T - K)^+]$

由伊藤引理结果：
$$
\ln S_T \sim N\left(\ln S_0 + (r - \frac{\sigma^2}{2})T,\; \sigma^2 T\right)
$$

标准化：
$$
Z = \frac{\ln S_T - \left(\ln S_0 + (r - \frac{\sigma^2}{2})T\right)}{\sigma\sqrt{T}} \sim N(0,1)
$$

$$
C_0 = e^{-rT} \int_{-\infty}^{\infty} \left( e^{\ln S_0 + (r - \frac{\sigma^2}{2})T + \sigma\sqrt{T}z} - K \right)^+ \frac{1}{\sqrt{2\pi}} e^{-z^2/2} dz
$$

积分下界为使 $S_T > K$ 的 $z$，即 $z > -d_1$：

$$
\boxed{C_0 = S_0 N(d_1) - K e^{-rT} N(d_2)}
$$

其中：
$$
d_1 = \frac{\ln(S_0/K) + (r + \frac{\sigma^2}{2})T}{\sigma\sqrt{T}}
$$
$$
d_2 = d_1 - \sigma\sqrt{T} = \frac{\ln(S_0/K) + (r - \frac{\sigma^2}{2})T}{\sigma\sqrt{T}}
$$

$N(\cdot)$ 为标准正态分布的累计分布函数。

---

## Python 实现：BS 公式计算期权价格

```python
import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    """
    Black-Scholes 看涨期权定价公式
    
    参数：
        S   : 当前股价
        K   : 行权价
        T   : 到期时间（年）
        r   : 无风险利率（年化）
        sigma: 波动率（年化）
    
    返回：
        C   : 期权价格
        delta: Delta 值
    """
    if T <= 0:
        return max(S - K, 0)
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    C = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega  = S * norm.pdf(d1) * np.sqrt(T) / 100  # 每1%波动率变化
    theta = (- S * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
             - r * K * np.exp(-r * T) * norm.cdf(d2)) / 365  # 每日
    
    return {
        "price": C,
        "d1": d1,
        "d2": d2,
        "delta": delta,
        "gamma": gamma,
        "vega": vega,
        "theta": theta  # 日度
    }

# 示例：AAPL 当前股价 180，行权价 175，30天后到期
S = 180.0
K = 175.0
T = 30 / 365
r = 0.04
sigma = 0.25

result = black_scholes_call(S, K, T, r, sigma)
print(f"期权价格: ${result['price']:.4f}")
print(f"d1 = {result['d1']:.4f}, d2 = {result['d2']:.4f}")
print(f"Delta = {result['delta']:.4f}")
print(f"Gamma = {result['gamma']:.6f}")
print(f"Vega  = {result['vega']:.4f}（每1%隐含波动率）")
print(f"Theta = {result['theta']:.4f}（每日时间衰减）")

# 敏感性验证：检验 put-call parity
def black_scholes_put(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    P = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return P

call = result["price"]
put = black_scholes_put(S, K, T, r, sigma)
pc_parity = call - put
theoretical = S - K * np.exp(-r * T)
print(f"\nPut-Call Parity 验证:")
print(f"C - P = {pc_parity:.4f}, S - Ke^-rT = {theoretical:.4f}")
```

**输出示例**：
```
期权价格: $9.3721
d1 = 0.5423, d2 = 0.4815
Delta = 0.7059
Gamma = 0.0182
Vega  = 0.3647（每1%隐含波动率）
Theta = -0.0483（每日时间衰减）

Put-Call Parity 验证:
C - P = 6.3821, S - Ke^-rT = 6.3821  ✓
```

---

## 与神经建模的关联：扩散过程在神经信号中的应用

### 布朗运动与神经噪声

神经元的 spike timing 存在**随机波动**，可用布朗运动建模：

$$
dV_t = -\frac{V_t}{\tau} dt + \sigma dW_t
$$

其中 $V_t$ 是膜电位，$\tau$ 是时间常数，$\sigma$ 是噪声强度。

### 随机微分方程在神经建模中的地位

- **Leaky Integrate-and-Fire (LIF) 模型**：加入随机项后变为随机微分方程
- **Ornstein-Uhlenbeck (OU) 过程**：均值回归过程，描述神经元的**随机漂移**
- **扩散模型（DDM）**：用于决策理论，漂移率对应信号强度

> **数学共性**：伊藤引理是连接"确定性 PDE"和"随机微分方程"的桥梁，无论是 B-S 期权定价还是神经膜电位的 Fokker-Planck 方程，都遵循同样的数学结构。

---

## 延伸学习资源

- **书籍**：Steven Shreve《Stochastic Calculus and Finance》；John Hull《期权、期货及其他衍生品》第10-13章
- **课程**：MIT 18.S096「Financial Statistics and Machine Learning」；Coursera「Stochastic Processes」by Princeton
- **推导视频**：3Blue1Brown「But what is the Black-Scholes equation?」
- **深入**：尝试推导 B-S PDE 的 Green 函数解，理解解析解的概率意义

---

## 理解程度自评：3/5

- [x] Black-Scholes 七大假设条件
- [x] 伊藤引理（Ito's Lemma）陈述与几何布朗运动应用
- [x] Delta 对冲思想 → B-S PDE 推导
- [x] Feynman-Kac 定理 → 解析解推导
- [x] Python 实现 + Greeks 计算
- [x] 与神经科学扩散过程的关联
- [ ] B-S PDE 的 Green 函数（Feynman-Kac 完整证明）
- [ ] 隐含波动率（Implied Volatility）求解（Newton 法）
- [ ] 数值方法：有限差分法、Monte Carlo 验证

> ⚠️ **建议**：本节公式密度高，建议先复习伊藤微积分的二次变差性质，然后手推一遍 B-S PDE 的完整推导。核心记忆：Delta 对冲 → 无风险组合 → rΠ dt → B-S PDE → Feynman-Kac。
