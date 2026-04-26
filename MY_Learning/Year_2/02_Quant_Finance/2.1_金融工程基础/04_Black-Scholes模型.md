# Q1.10 Black-Scholes模型

> Black-Scholes-Merton Model | 期权定价的解析方法

## 📋 基本信息

| 属性 | 值 |
|------|-----|
| 章节编号 | Q1.10 |
| 主题 | Black-Scholes模型 |
| 难度 | ⭐⭐⭐ |
| 类型 | 衍生品定价 |
| 前置知识 | 伊藤微积分、概率统计、正态分布 |

---

## 🎯 学习目标

1. 理解Black-Scholes模型的核心假设
2. 掌握BS公式的推导思路
3. 能够使用BS公式为期权定价
4. 理解Greeks的计算和应用

---

## 1. 模型假设

### 1.1 核心假设

1. **标的资产价格服从几何布朗运动**：
$$dS = \mu S dt + \sigma S dW$$

2. **无摩擦市场**：无交易成本、无税收、无保证金要求

3. **连续交易**：可以连续交易标的资产和期权

4. **无风险利率恒定**：对所有期限相同

5. **标的无分红**：在期权有效期内不分红

6. **期权为欧式**：仅在到期日可行权

### 1.2 几何布朗运动的性质

| 性质 | 公式 |
|------|------|
| 对数正态分布 | $\ln S_T \sim N(\ln S_0 + (\mu - \sigma^2/2)T, \sigma^2 T)$ |
| 期望 | $E[S_T] = S_0 e^{\mu T}$ |
| 瞬时收益率 | $dS/S \sim N(\mu, \sigma^2)$ |

---

## 2. Black-Scholes公式

### 2.1 微分方程推导

**构建无风险组合**：
$$\Pi = V - \Delta S$$

其中 $V$ 是期权价值，$\Delta$ 是对冲比率。

**伊藤引理**：
$$dV = \frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S}dS + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}(dS)^2$$

**组合变化**：
$$d\Pi = dV - \Delta dS$$

代入并消除随机项：
$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = rV - rS\frac{\partial V}{\partial S}$$

### 2.2 定价公式

**欧式Call期权**：
$$C(S, t) = S_0 N(d_1) - Ke^{-r(T-t)} N(d_2)$$

**欧式Put期权**（Put-Call Parity）：
$$P(S, t) = Ke^{-r(T-t)} N(-d_2) - S_0 N(-d_1)$$

其中：
$$d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}$$
$$d_2 = d_1 - \sigma\sqrt{T-t}$$

### 2.3 Python实现

```python
import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    """
    Black-Scholes 欧式Call期权定价
    
    Parameters:
    -----------
    S : float - 当前标的价格
    K : float - 行权价
    T : float - 到期时间（年）
    r : float - 无风险利率
    sigma : float - 波动率
    
    Returns:
    --------
    call_price : float - Call期权价格
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

def black_scholes_put(S, K, T, r, sigma):
    """Black-Scholes 欧式Put期权定价"""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

def bs_greeks(S, K, T, r, sigma):
    """
    计算Black-Scholes Greeks
    
    Returns:
    --------
    dict with delta, gamma, theta, vega, rho
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) 
             - r * K * np.exp(-r * T) * norm.cdf(d2))
    vega = S * norm.pdf(d1) * np.sqrt(T)
    rho = K * T * np.exp(-r * T) * norm.cdf(d2)
    
    return {
        'delta': delta,
        'gamma': gamma,
        'theta': theta,
        'vega': vega,
        'rho': rho
    }

# 示例
if __name__ == "__main__":
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    
    call = black_scholes_call(S, K, T, r, sigma)
    put = black_scholes_put(S, K, T, r, sigma)
    greeks = bs_greeks(S, K, T, r, sigma)
    
    print(f"Call价格: {call:.4f}")
    print(f"Put价格: {put:.4f}")
    print(f"验证Put-Call Parity: {call - put:.4f} vs {S - K*np.exp(-r*T):.4f}")
    print(f"Greeks: {greeks}")
```

---

## 3. Greeks详解

### 3.1 Delta (Δ)

**定义**：期权价格对标的资产价格的一阶导数

$$\Delta = \frac{\partial V}{\partial S} = N(d_1) \text{ (Call)}$$

| 期权状态 | Delta范围 | 含义 |
|---------|-----------|------|
| Deep ITM | 接近 1 | 几乎等同于持有标的 |
| ATM | 约 0.5 | 对标的价格变动敏感 |
| Deep OTM | 接近 0 | 几乎不受标的价格影响 |

**对冲应用**：卖出 $\Delta$ 份标的资产可对冲期权风险

### 3.2 Gamma (Γ)

**定义**：Delta对标的价格的二阶导数

$$\Gamma = \frac{\partial^2 V}{\partial S^2} = \frac{N'(d_1)}{S\sigma\sqrt{T}}$$

**特点**：
- ATM期权的Gamma最大
- 接近到期时，ATM期权Gamma急剧增加
- 是期权买方的"朋友"，卖方的"敌人"

### 3.3 Theta (Θ)

**定义**：期权价格对时间的一阶导数

$$\Theta = \frac{\partial V}{\partial t}$$

**规律**：
- 期权是"消耗性资产"，随时间流逝价值减少
- 越接近到期，Theta绝对值越大（加速衰减）
- OTM期权的Theta通常比ITM更大

### 3.4 Vega (ν)

**定义**：期权价格对波动率的一阶导数

$$\nu = \frac{\partial V}{\partial \sigma} = S\sqrt{T}N'(d_1)$$

**特点**：
- Vega总是正的（波动率增加对期权有利）
- ATM期权对波动率最敏感
- 长期期权的Vega大于短期期权

### 3.5 Rho (ρ)

**定义**：期权价格对利率的一阶导数

$$\rho = \frac{\partial V}{\partial r}$$

---

## 4. Put-Call Parity

### 4.1 基本公式

$$C - P = S - Ke^{-rT}$$

或等价形式：
$$C = P + S - Ke^{-rT}$$

### 4.2 含义

```
看涨期权 - 看跌期权 = 标的资产 - 行权价折现
     ↓           ↓         ↓           ↓
  收益差异     收益差异   持有成本   资金成本
```

### 4.3 风险中性定价视角

在风险中性世界中：
$$C = e^{-rT} E^Q[\max(S_T - K, 0)]$$

其中 $Q$ 是风险中性测度，$S_T$ 服从：
$$S_T = S_0 e^{(r - \sigma^2/2)T + \sigma W_T^Q}$$

---

## 5. 隐含波动率

### 5.1 定义

**隐含波动率 (IV)**：将市场价格代入BS公式反解出的波动率

```python
from scipy.optimize import brentq

def implied_vol_call(market_price, S, K, T, r):
    """
    使用二分法求解隐含波动率
    """
    def objective(sigma):
        return black_scholes_call(S, K, T, r, sigma) - market_price
    
    # 设置搜索边界
    low = 0.01
    high = 2.0
    
    try:
        iv = brentq(objective, low, high)
        return iv
    except:
        return np.nan
```

### 5.2 波动率微笑

```
        隐含波动率
              │
        高    │         ╭──╮
              │       ╭─    ─╮
              │      ╭        ╮
        低    │──────╯        ╲──────
              └────────────────────────→ 行权价
                   OTM  ATM  ITM
                     ←  微笑  →
```

**波动率微笑的成因**：
1. 波动率聚集 (Volatility clustering)
2. 杠杠效应 (Leverage effect)
3. 供需不平衡 (Supply/demand imbalance)

---

## 6. 模型局限性

| 局限 | 改进方向 |
|------|----------|
| 恒定波动率假设 | 局部波动率模型、Heston模型 |
| 对数正态分布假设 | 跳跃扩散模型、分数布朗运动 |
| 连续交易假设 | 离散时间模型、交易成本模型 |
| 无分红假设 | 加入分红收益率的BS模型 |

---

## 📝 练习题

1. **计算题**：S=100, K=105, T=0.5, r=5%, σ=20%，计算Call价格和Greeks
2. **推导题**：证明Put-Call Parity
3. **编程题**：绘制期权价格对各参数的敏感性曲线

---

## → 下一章节

[[Q1.11_Greeks与风险对冲|Greeks与风险对冲]]

---

**创建时间**: 2026-04-07
**难度评级**: ⭐⭐⭐
