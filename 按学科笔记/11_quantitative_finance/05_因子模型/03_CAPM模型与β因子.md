---
type: chapter
subject: quantitative_finance
chapter: Q1.02
title: CAPM模型与β因子
created: 2026-04-07
updated: 2026-04-07
level: Level 1
area: 资产定价理论
---

# Q1.02 CAPM模型与β因子

> 将"系统性风险"量化为可交易因子的开山之作

## 学习目标

- [x] 理解CAPM模型的假设条件和推导逻辑
- [x] 掌握β因子的定义、计算方法和经济含义
- [x] 理解证券市场线（SML）和CML的区别
- [x] 了解CAPM的实证局限与批评论战
- [ ] 能够用Python对真实收益率数据进行β估计

---

## 1. CAPM模型的假设条件

### 1.1 Sharpe-Lintner-Mossin 三人组

CAPM（全称 Capital Asset Pricing Model）由以下三人独立提出：

| 年份 | 作者 | 贡献 |
|------|------|------|
| 1964 | William Sharpe | 均衡定价模型 |
| 1964 | John Lintner | 风险资产定价 |
| 1966 | Jan Mossin | 套利均衡条件 |

### 1.2 核心假设

CAPM的推导依赖于一系列理想化假设：

```
1. 投资者是风险厌恶的，追求均值-方差最优
2. 所有投资者有同质的预期（相同μ, Σ）
3. 所有资产可无限分割（连续交易）
4. 无摩擦市场：无税、无交易成本、无卖空限制
5. 借贷利率相等（无风险利率r_f统一）
6. 资本市场是均衡的（出清状态）
```

> **现实检验**：这些假设在真实市场中几乎都不成立，但这不影响CAPM作为**理论基准**的价值。金融学的很多模型都是"假设不真实但很有用"。

---

## 2. CAPM的推导

### 2.1 从分离定理到市场组合

**分离定理**（Fisher Separation Theorem）：

> 在无摩擦市场中，投资决策和消费决策可以分离。所有人选择相同的风险资产组合——**市场组合M**，只是借款/储蓄比例因人而异。

这意味着：
- 所有投资者持有相同的**风险资产组合**（切点组合）
- 这个切点组合就是**市场组合**（Market Portfolio）
- 市场组合包含所有可投资资产，权重与其市值成比例

### 2.2 资本市场线（CML）

在均值-方差平面上，**最优组合**一定落在**资本市场线**上：

```
期望收益 E(R)
    ↑
    |            CML（资本市场线）
    |           /
    |         /  r_f
    |       /  ● 可行集边界（最小方差前沿）
    |     /
    |   /  ● 市场组合 M（切点）
    | /
    +--------------------------------→ 标准差 σ
```

**CML方程**：

$$E(R_p) = r_f + \frac{E(R_M) - r_f}{\sigma_M} \cdot \sigma_p$$

或写成**夏普比率**形式：

$$\text{夏普比率} = \frac{E(R_p) - r_f}{\sigma_p} = \frac{E(R_M) - r_f}{\sigma_M} = \text{常数}$$

> CML上所有组合都是**完全分散化**的组合（只有系统性风险）。CML以下的组合没有充分利用分散化。

### 2.3 β因子的定义

**关键洞察**：CML描述的是**完全分散化组合**的风险-收益关系，但单个资产的收益不仅仅取决于总波动率，还取决于它与市场组合的**相关程度**。

**β因子**衡量资产收益率对市场收益率的**敏感度**：

$$\beta_i = \frac{\text{Cov}(R_i, R_M)}{\text{Var}(R_M)} = \rho_{i,M} \cdot \frac{\sigma_i}{\sigma_M}$$

**含义**：
- β = 1：资产与市场同涨同跌（市场组合本身）
- β > 1：放大市场波动（进攻型资产，如小市值股票）
- β < 1：削弱市场波动（防御型资产，如公用事业股）
- β < 0：与市场负相关（少数对冲基金策略）

### 2.4 证券市场线（SML）

**CAPM核心公式**——证券市场线（Security Market Line）：

$$\mathbb{E}[R_i] = r_f + \beta_i \cdot \underbrace{(E[R_M] - r_f)}_{\text{市场风险溢价}}$$

```
E(R_i)
  ↑
  |                        SML（证券市场线）
  |                    /
  |                 / β=1.5
  |              /  ● 高β资产
  |           /
  |        / β=1
  |     / ● 市场组合 M
  |  /
  |/
  +------------------------------------→ β
  0    0.5    1.0    1.5    2.0
```

**预期超额收益只取决于β**（CAPM的核心结论）：

$$\mathbb{E}[R_i] - r_f = \beta_i \cdot (E[R_M] - r_f)$$

> 非系统性风险没有**风险溢价**——这是CAPM最革命性的结论。因为可以通过分散化消除的非系统性风险，不值得额外补偿。

---

## 3. β的计算与估计

### 3.1 简单线性回归法（SLR）

最常用的β估计方法是对资产收益率与市场收益率做OLS回归：

$$R_{i,t} - r_f = \alpha_i + \beta_i (R_{M,t} - r_f) + \epsilon_t$$

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm

# 假设：rf = 0.03（年化无风险利率），R_M是市场收益率序列
def estimate_beta(asset_returns, market_returns, rf=0.0):
    """
    用OLS回归估计β
    asset_returns: 资产收益率序列
    market_returns: 市场收益率序列
    """
    # 超额收益
    excess_asset = asset_returns - rf
    excess_market = market_returns - rf
    
    # OLS: R_i - r_f = α + β(R_M - r_f) + ε
    X = sm.add_constant(excess_market)  # 加截距项
    model = sm.OLS(excess_asset, X).fit()
    
    return {
        'beta': model.params.iloc[1],      # β
        'alpha': model.params.iloc[0],     # α（Jensen's alpha）
        'r_squared': model.rsquared,        # R²
        'std_error': model.bse.iloc[1],    # β的标准误
        't_stat': model.tvalues.iloc[1],   # t统计量
        'p_value': model.pvalues.iloc[1]   # p值
    }

# 示例：估计苹果公司（AAPL）的β
# import yfinance as yf
# aapl = yf.download('AAPL', start='2015-01-01', end='2024-12-31')['Adj Close'].pct_change().dropna()
# sp500 = yf.download('^GSPC', start='2015-01-01', end='2024-12-31')['Adj Close'].pct_change().dropna()
# result = estimate_beta(aapl, sp500, rf=0.05/252)  # 日化无风险利率
# print(f"β = {result['beta']:.2f}, α = {result['alpha']:.4f}, R² = {result['r_squared']:.3f}")
```

### 3.2 β估计的细节问题

**滚动窗口β**（时变β）：

```python
def rolling_beta(asset, market, window=252, rf=0.0):
    """计算滚动β（过去252个交易日）"""
    excess_asset = asset - rf
    excess_market = market - rf
    
    # 滚动协方差/方差
    rolling_cov = excess_asset.rolling(window).cov(excess_market)
    rolling_var = excess_market.rolling(window).var()
    rolling_beta = rolling_cov / rolling_var
    
    return rolling_beta

# 可视化时变β
# rolling_b = rolling_beta(aapl, sp500)
# rolling_b.plot(figsize=(12, 5), title='Rolling 252-day Beta of AAPL')
```

**β的贝叶斯收缩**（防止极端β的 shrinkage 现象）：

$$\hat{\beta}_{\text{shrink}} = w \cdot \hat{\beta}_{\text{OLS}} + (1-w) \cdot \bar{\beta}$$

其中 $\bar{\beta} = 1$，权重 $w = \frac{1}{1 + \frac{\lambda}{n}}$，$\lambda$ 是行业因子调节参数。

> **实践洞察**：实证发现，个股β倾向于向1**回归**（Mean Reversion）。这是因为公司本身会调整其业务结构，使系统性风险趋于市场平均水平。

---

## 4. CAPM的实证检验与论战

### 4.1 早期检验

Fama-MacBeth (1973) 两步法：

1. **第一步**：时序回归，估计每只股票的β
2. **第二步**：截面回归，检验 $\mathbb{E}[R_i] = r_f + \lambda_i \hat{\beta}_i$

$$\mathbb{E}[R_{i}] = \gamma_0 + \gamma_1 \hat{\beta}_i + \epsilon_i$$

Fama-MacBeth的结果：$\hat{\gamma}_1$ 接近 CAPM 预测的风险溢价，但略低。

### 4.2 CAPM的"死亡"

Black, Jensen, Scholes (1972) 发现：

- **低β股票的实际收益高于CAPM预测**（被低估）
- **高β股票的实际收益低于CAPM预测**（被高估）

> 这是CAPM的第一个重大裂痕——"**截距异常**"。

Fama-French (1992) 的棺材最后一钉：

$$\mathbb{E}[R_i] - r_f = \beta_i^{市场} \cdot \lambda_{MKT} + \beta_i^{SMB} \cdot \lambda_{SMB} + \beta_i^{HML} \cdot \lambda_{HML}$$

加入**规模因子**（SMB）和**价值因子**（HML）后，β的市场溢价消失了。

> **教训**：CAPM的假设（单因子、完全分散化）在真实市场中不成立。规模效应和价值效应是真实存在的"异象"，推动了多因子模型的革命。

---

## 5. CAPM的应用场景

### 5.1 权益成本（WACC）

CAPM最重要的应用之一：**估算权益资本成本**

$$r_{\text{equity}} = r_f + \beta_{\text{levered}} \cdot (E[R_M] - r_f)$$

```python
def wacc(equity_value, debt_value, r_equity, r_debt, tax_rate=0.25):
    """计算加权平均资本成本 WACC"""
    total_value = equity_value + debt_value
    equity_weight = equity_value / total_value
    debt_weight = debt_value / total_value
    
    # 税后债务成本（利息抵税效应）
    aftertax_rdebt = r_debt * (1 - tax_rate)
    
    wacc = equity_weight * r_equity + debt_weight * aftertax_rdebt
    return wacc

# 示例：苹果公司
# equity = 3_000_000_000_000  # 市值3万亿美元
# debt = 100_000_000_000       # 债务1000亿
# beta = 1.2
# rf = 0.045                   # 10年美债收益率
# market_premium = 0.055       # 历史市场溢价约5.5%
# r_equity = rf + beta * market_premium
# print(f"权益成本: {r_equity:.2%}")
# print(f"WACC: {wacc(equity, debt, r_equity, r_debt=0.05):.2%}")
```

### 5.2 项目估值（折现率）

CAPM给单个项目/投资决策提供折现率：

$$NPV = \sum_{t=1}^{T} \frac{CF_t}{(1 + r_f + \beta_{\text{项目}}(E[R_M] - r_f))^t} - I_0$$

---

## 6. 章节小结

### 核心公式

| 公式 | 名称 | 含义 |
|------|------|------|
| $\beta_i = \frac{\text{Cov}(R_i,R_M)}{\text{Var}(R_M)}$ | β定义 | 资产对市场风险的敏感度 |
| $E[R_i] = r_f + \beta_i(E[R_M] - r_f)$ | SML | CAPM核心定价公式 |
| $E[R_p] = r_f + \frac{E[R_M]-r_f}{\sigma_M}\sigma_p$ | CML | 有效组合的风险-收益线 |
| $R_i - r_f = \alpha_i + \beta_i(R_M - r_f) + \epsilon_i$ | β回归 | 估计β的统计模型 |

### CAPM的贡献与局限

| 贡献 | 局限 |
|------|------|
| 将风险量化、可交易化 | 只能解释市场风险溢价 |
| 提供了权益成本的基准 | β不能解释规模、价值效应 |
| 奠定了多因子模型基础 | 假设过于理想化 |

---

**下一步** → [[Q1.03_APT套利定价理论|APT套利定价理论]]

---

*本笔记适用于 MY_Learning 量化金融路径 · Level 1 资产定价理论 · 第2章（共4章）*
