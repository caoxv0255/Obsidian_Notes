---
type: chapter
subject: quantitative_finance
chapter: Q1.03
title: APT套利定价理论
created: 2026-04-07
updated: 2026-04-07
level: Level 1
area: 资产定价理论
---

# Q1.03 APT套利定价理论

> "没有免费的午餐"——从无套利原则推导普适定价公式

## 学习目标

- [x] 理解APT与CAPM的核心区别（多因子 vs 单因子）
- [x] 掌握APT的假设条件和推导逻辑
- [x] 理解因子、因子载荷、因子溢价的概念
- [x] 能够用APT框架识别资产的因子暴露
- [ ] 理解APT与Fama-French模型的关系

---

## 1. APT vs CAPM：两种定价哲学

```
         CAPM                          APT
     ───────────                   ─────────────
     单因子模型                       多因子模型
     需要市场组合                  不需要市场组合
     假设同质预期                   假设无套利
     适用范围：股票                 适用范围：所有资产
```

| 维度 | CAPM | APT |
|------|------|-----|
| **因子数量** | 单一（市场组合） | 多个（任意因子） |
| **理论基础** | 均值-方差均衡 | 无套利条件 |
| **市场组合** | 必须存在且可观测 | 不需要 |
| **假设强度** | 强（同质预期） | 弱（无套利） |
| **预测精度** | 较低（被FF打败） | 可扩展 |

> **核心思想**：APT认为资产的预期收益由**多个因子**共同决定，只要这些因子的风险溢价存在，就不可能有无风险套利机会。

---

## 2. APT的假设条件

APT的推导仅需两个温和的假设：

### 假设 1：因子模型描述资产收益

资产收益率由 $K$ 个因子驱动：

$$R_i = \alpha_i + \beta_{i,1} F_1 + \beta_{i,2} F_2 + \cdots + \beta_{i,K} F_K + \epsilon_i$$

- $F_k$：第 $k$ 个**公共因子**（所有资产共享）
- $\beta_{i,k}$：资产 $i$ 对因子 $k$ 的**敏感度**（因子载荷）
- $\epsilon_i$：资产特异性收益（期望为0，方差 $\sigma_{\epsilon_i}^2$）

> **假设2**：特异性风险 $\epsilon_i$ 可以通过组合**充分分散化**消除。

### 假设 2：无套利

若存在**充分分散化的组合**$p$ 满足：

$$\mathbb{E}[R_p] > r_f \quad \text{且} \quad \beta_{p,k} = 0, \forall k$$

则存在套利机会，市场未出清。

---

## 3. APT的推导

### 3.1 因子组合

考虑一个特殊组合 $z_k$，它对因子 $k$ 的载荷为1，对其他因子载荷为0：

$$\beta_{z_k, j} = \begin{cases} 1 & j = k \\ 0 & j \neq k \end{cases}$$

$z_k$ 被称为**纯因子组合**（Pure Factor Portfolio）。

### 3.2 无套利条件

对任何纯因子组合 $z_k$，如果它的期望收益为 $\lambda_k$，则：

$$E[R_{z_k}] = \lambda_k$$

由**无套利条件**，$z_k$ 的期望超额收益必须与其风险（因子载荷）成正比。

### 3.3 APT定价公式

**核心结论**：在无套利市场中，充分分散化的资产满足：

$$\mathbb{E}[R_i] = r_f + \beta_{i,1} \lambda_1 + \beta_{i,2} \lambda_2 + \cdots + \beta_{i,K} \lambda_K$$

其中 $\lambda_k$ 是**因子 $k$ 的风险溢价**（也叫**因子预期收益**）。

**或者写成风险溢价形式**：

$$\mathbb{E}[R_i] - r_f = \beta_{i,1} (E[R_{z_1}] - r_f) + \beta_{i,2} (E[R_{z_2}] - r_f) + \cdots + \beta_{i,K} (E[R_{z_K}] - r_f)$$

### 3.4 APT的直观理解

```
                    因子组合收益
                          ↑
            λ_2         λ_1     ← 因子溢价
           ↑         ↑
  E(R_i)  |       / 
    ↑     |     /  ← 线性定价
    |   /    
    | /   ← α_i（被定价理论忽略的残余收益）
  r_f +------------------→ β_i（因子载荷）
```

> **关键洞察**：APT说明资产的预期收益是**因子载荷的线性函数**。这比CAPM的一般化程度高得多——CAPM只是K=1时的特例。

---

## 4. 因子、因子载荷、因子溢价

### 4.1 三个核心概念

| 概念 | 符号 | 定义 | 角色 |
|------|------|------|------|
| **因子** | $F_k$ | 公共风险来源 | 解释资产的共同波动 |
| **因子载荷** | $\beta_{i,k}$ | 资产对因子的敏感度 | 资产对每个因子的暴露 |
| **因子溢价** | $\lambda_k$ | 每个因子要求的超额收益 | 因子的"价格" |

### 4.2 因子溢价的估计

从历史数据中，用**横截面回归**估计因子溢价：

$$\mathbb{E}[R_i] - r_f = \lambda_0 + \beta_{i,1}\lambda_1 + \beta_{i,2}\lambda_2 + \cdots + \beta_{i,K}\lambda_K + \eta_i$$

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm

def estimate_factor_premiums(factor_returns, asset_returns, rf=0.0):
    """
    估计APT因子溢价（横截面回归）
    
    factor_returns: DataFrame (T × K) 因子收益率
    asset_returns: DataFrame (T × N) 资产收益率
    """
    # 资产超额收益（时序平均）
    excess_returns = (asset_returns - rf).mean()
    
    # 资产对因子的载荷（时序回归）
    betas = pd.DataFrame(index=asset_returns.columns, columns=factor_returns.columns)
    for asset in asset_returns.columns:
        y = asset_returns[asset] - rf
        X = sm.add_constant(factor_returns)
        model = sm.OLS(y, X).fit()
        betas.loc[asset] = model.params.iloc[1:]
    
    # 横截面回归：E[R_i] - rf = λ_0 + β_i'λ + ε
    X_cs = sm.add_constant(betas)
    model_cs = sm.OLS(excess_returns, X_cs).fit()
    
    lambdas = model_cs.params.iloc[1:]  # 因子溢价
    alpha = model_cs.params.iloc[0]     # 截距（CAPM的α）
    
    return {'lambdas': lambdas, 'alpha': alpha, 'r_squared': model_cs.rsquared}
```

---

## 5. APT vs 多因子模型（Fama-French）

APT是一个**框架**，Fama-French是**具体实现**：

| | APT框架 | Fama-French (1993) |
|--|---------|-------------------|
| 因子数 | 任意K | K=3 |
| 因子选择 | 未指定 | 市场因子+MKT、SMB、HML |
| 因子溢价 | 从数据估计 | 从数据估计 |
| 理论基础 | 无套利 | 无套利+实证因子 |

**Fama-French三因子模型**（可以看作APT的具体化）：

$$\mathbb{E}[R_i] - r_f = \beta_i^{MKT} \cdot \lambda_{MKT} + \beta_i^{SMB} \cdot \lambda_{SMB} + \beta_i^{HML} \cdot \lambda_{HML}$$

| 因子 | 含义 | 风险溢价实证结果 |
|------|------|----------------|
| MKT | 市场超额收益 | ~5.5%/年 |
| SMB | 小市值-大市值 | ~2-3%/年 |
| HML | 高账面市值比-低账面市值比 | ~3-5%/年 |

---

## 6. APT的实践应用

### 6.1 因子择股

利用APT框架，选择**高因子暴露 + 低特异性风险**的股票：

```python
def factor_portfolio_score(betas, lambdas, rf, asset_returns, risk_aversion=3.0):
    """
    基于APT的因子暴露打分
    score = Σ β_k · λ_k - 特异性风险溢价
    """
    # 预期超额收益（APT）
    expected_excess = betas @ lambdas
    
    # 特异性风险调整
    residual_var = (asset_returns - expected_excess).var()
    risk_penalty = risk_aversion * residual_var
    
    # 最终打分
    score = expected_excess - risk_penalty
    return score.sort_values(ascending=False)

# 示例：
# top_stocks = factor_portfolio_score(stock_betas, factor_premiums, rf).head(20)
```

### 6.2 事件研究：因子归因

当某股票因事件（如财报）大涨，分析有多少来自因子暴露、多少来自特异性：

$$\Delta R_i = \beta_{i,1}\Delta F_1 + \beta_{i,2}\Delta F_2 + \underbrace{\Delta \epsilon_i}_{\text{特异性贡献}}$$

---

## 7. 章节小结

### 核心公式

$$E[R_i] = r_f + \beta_{i,1}\lambda_1 + \beta_{i,2}\lambda_2 + \cdots + \beta_{i,K}\lambda_K$$

### APT的核心逻辑链

```
假设1: 收益由因子模型驱动
         ↓
假设2: 无套利机会
         ↓
结论: 预期收益是因子载荷的线性函数
         ↓
推论: 因子溢价（λ_k）可以被估计
```

### APT vs CAPM

| | CAPM | APT |
|--|------|-----|
| 本质 | 单因子均衡模型 | 多因子套利定价 |
| 假设 | 同质预期、借贷同利 | 无套利（更弱） |
| 市场组合 | 必须（不可测） | 不需要 |
| 因子溢价 | 唯一（市场溢价） | 多个 |

---

**下一步** → [[Q1.04_Fama-French多因子模型|Fama-French多因子模型]]

---

*本笔记适用于 MY_Learning 量化金融路径 · Level 1 资产定价理论 · 第3章（共4章）*
