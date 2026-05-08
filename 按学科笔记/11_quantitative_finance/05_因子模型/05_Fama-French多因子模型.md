---
type: chapter
subject: quantitative_finance
chapter: Q1.04
title: Fama-French多因子模型
created: 2026-04-07
updated: 2026-04-07
level: Level 1
area: 资产定价理论
---

# Q1.04 Fama-French多因子模型

> 从实证因子到因子投资——FF3/5/6模型的演进

## 学习目标

- [x] 掌握FF3因子模型的构建逻辑与实证证据
- [x] 理解SMB、HML因子的构造方法
- [x] 了解FF5、FF6模型的扩展方向
- [x] 能够用FF框架对投资组合进行因子归因
- [ ] 理解因子拥挤（Factor Crowding）现象

---

## 1. Fama-French的提出背景

### 1.1 CAPM的"死亡宣告"

1992年，Fama和French发表"The Cross-Section of Expected Stock Returns"，用实证方法证明：

> CAPM的β**不能**解释股票收益率的横截面差异。

他们发现：
- **规模**（Size）：小市值股票平均收益高于大市值
- **价值**（Value）：高账面市值比（BM）股票平均收益高于低BM

这两个变量在CAPM框架之外，但能显著提升对收益率的解释能力。

### 1.2 FF3因子模型（1993）

$$\mathbb{E}[R_i] - r_f = \beta_i^{MKT} \cdot \lambda_{MKT} + \beta_i^{SMB} \cdot \lambda_{SMB} + \beta_i^{HML} \cdot \lambda_{HML}$$

| 因子 | 名称 | 经济含义 | 实证溢价（美国）|
|------|------|----------|----------------|
| MKT | 市场超额收益 | 系统性风险 | ~5.5%/年 |
| SMB | Small Minus Big | 规模效应（小盘股溢价）| ~2-3%/年 |
| HML | High Minus Low | 价值效应（价值股溢价）| ~3-5%/年 |

---

## 2. 因子构造方法

### 2.1 规模因子（SMB）

**构造步骤**：

```
1. 将所有股票按市值（Size）分为 Small (S) 和 Big (B) 两组（前50%为S，后50%为B）
2. 按账面市值比（BM）分为 Low (L)、Medium (M)、High (H) 三组（30%/40%/30%）
3. 构成6个组合：SL、SM、SH、BL、BM、BH
4. SMB = (SL + SM + SH) / 3 - (BL + BM + BH) / 3
```

```python
def construct_smb_factor(stock_data, factor_data):
    """
    构造SMB因子
    stock_data: 包含市值、账面市值比的数据
    """
    # 分组
    size_median = stock_data['market_cap'].median()
    stock_data['size_group'] = np.where(stock_data['market_cap'] < size_median, 'S', 'B')
    
    # BM三分位
    stock_data['bm_quartile'] = pd.qcut(stock_data['bm'], q=3, labels=['L', 'M', 'H'])
    
    # 6个组合的等权收益率
    portfolios = stock_data.groupby(['size_group', 'bm_quartile']).apply(
        lambda x: (x['return'] * x['market_cap']).sum() / x['market_cap'].sum()
    )
    
    # SMB = 小市值组合平均 - 大市值组合平均
    small = portfolios.loc['S'].mean()
    big = portfolios.loc['B'].mean()
    smb = small - big
    
    return smb
```

### 2.2 价值因子（HML）

**构造步骤**：

```
1. 按BM分为 High (H)、Medium (M)、Low (L) 三组
2. HML = 高BM组平均收益 - 低BM组平均收益
```

> **经济直觉**：高账面市值比（价值股）意味着市场对公司的"悲观预期"较多。当市场情绪改善或公司基本面好转时，价值股反弹空间更大，因此要求更高的风险溢价。

### 2.3 因子溢价的实证估计

```python
import pandas as pd
import numpy as np

def estimate_ff3_premiums(portfolio_returns, factors):
    """
    用横截面回归估计FF3因子溢价
    E[R_i] - rf = λ_0 + β_MKT·λ_MKT + β_SMB·λ_SMB + β_HML·λ_HML + ε
    """
    from sklearn.linear_model import LinearRegression
    
    # 资产超额收益的横截面均值
    excess_mean = portfolio_returns.mean()
    
    # 因子载荷矩阵（β）
    # 这里简化处理，实际应用中需要先做时序回归
    betas = np.linalg.lstsq(factors.cov(), factors.mean(), rcond=None)[0]
    
    # 横截面回归
    lr = LinearRegression().fit(betas.reshape(-1, 1), excess_mean)
    
    return {
        'lambda_MKT': lr.coef_[0],
        'lambda_SMB': lr.coef_[1],
        'lambda_HML': lr.coef_[2]
    }
```

---

## 3. FF3的实证表现

### 3.1 解释能力

| 指标 | CAPM | FF3 |
|------|------|-----|
| 平均R²（横截面）| ~10-30% | ~70-90% |
| α（Jensen's alpha）| 显著非零 | 接近零 |
| 残余风险 | 高 | 低 |

FF3大幅提升了CAPM的解释能力，尤其是对**价值股**和**小市值股**的定价。

### 3.2 著名的FF因子收益历史

| 年份 | MKT | SMB | HML |
|------|-----|-----|-----|
| 1927-2023 平均 | 5.5% | 2.5% | 3.5% |
| 2000-2010（互联网泡沫后）| 低 | 高 | 极高 |
| 2011-2023 | 中等 | 下降 | 下降 |

> **关键观察**：2010年后，HML和SMB的溢价显著萎缩，这被称为"**价值因子失效**"和"**规模因子失效**"，催生了后续的FF5、FF6模型。

---

## 4. FF5因子模型（2015）

### 4.1 新增两个因子

Fama和French在2015年将模型扩展为5因子：

$$\mathbb{E}[R_i] - r_f = \beta_i^{MKT} \lambda_{MKT} + \beta_i^{SMB} \lambda_{SMB} + \beta_i^{HML} \lambda_{HML} + \beta_i^{RMW} \lambda_{RMW} + \beta_i^{CMA} \lambda_{CMA}$$

| 因子 | 全称 | 含义 | 经济直觉 |
|------|------|------|----------|
| RMW | Robust Minus Weak | 盈利能力强-弱 | 优质公司溢价 |
| CMA | Conservative Minus Aggressive | 投资少-多 | 低投资溢价 |

### 4.2 因子相关性

```
           MKT    SMB    HML    RMW    CMA
MKT        1.00  -0.25  -0.35   0.15  -0.15
SMB       -0.25   1.00   0.20  -0.30   0.15
HML       -0.35   0.20   1.00  -0.50  -0.05
RMW        0.15  -0.30  -0.50   1.00   0.05
CMA       -0.15   0.15  -0.05   0.05   1.00
```

> HML与RMW高度负相关（-0.50），这导致FF5中HML因子的解释力大幅下降——**冗余因子**问题。

---

## 5. FF6因子模型（2018）

### 5.1 包含的因子

| # | 因子 | 描述 |
|---|------|------|
| 1 | MKT | 市场超额收益 |
| 2 | SMB | 规模因子 |
| 3 | HML | 价值因子 |
| 4 | RMW | 盈利因子 |
| 5 | CMA | 投资因子 |
| 6 | UMD | Up Minus Down（动量因子）|

UMD = 过去6个月收益高的股票组合 - 过去6个月收益低的股票组合

### 5.2 各因子的风险溢价（美国市场，1927-2023）

```python
ff_factor_returns = {
    'MKT': 0.055,    # ~5.5%/年
    'SMB': 0.025,    # ~2.5%/年
    'HML': 0.035,    # ~3.5%/年（2010年后失效）
    'RMW': 0.030,    # ~3.0%/年
    'CMA': 0.025,    # ~2.5%/年
    'UMD': 0.060     # ~6.0%/年（最强但不稳定）
}
```

---

## 6. 因子投资实践

### 6.1 Barra风险模型

MSCI Barra模型是机构投资者最常用的多因子风险模型：

$$R_i = \sum_{k=1}^{K} \beta_{i,k} F_k + \omega_i$$

其中 $F_k$ 是**共同因子**（市场、行业、风格），$\omega_i$ 是**特异性风险**。

```python
def barra_risk_attribution(portfolio_weights, factor_betas, factor_cov, residual_var):
    """
    Barra风格因子归因
    """
    # 因子收益方差
    factor_risk = np.sqrt(portfolio_weights @ factor_betas @ factor_cov @ factor_betas.T @ portfolio_weights)
    
    # 特异性风险
    residual_risk = np.sqrt(portfolio_weights @ np.diag(residual_var) @ portfolio_weights)
    
    # 总风险
    total_risk = np.sqrt(factor_risk**2 + residual_risk**2)
    
    return {
        'factor_risk': factor_risk,
        'residual_risk': residual_risk,
        'total_risk': total_risk,
        'diversification_ratio': total_risk / factor_risk
    }
```

### 6.2 因子择股框架

```
步骤1: 计算每只股票的因子暴露（β_SMB, β_HML, β_RMW, β_CMA）
步骤2: 估计因子溢价（λ_k）
步骤3: 计算预期超额收益 = Σ β_k · λ_k
步骤4: 选预期收益最高的N只股票
步骤5: 等权配置，定期再平衡
```

---

## 7. 章节小结

### FF模型演进

| 模型 | 因子数 | 年份 | 核心贡献 |
|------|--------|------|----------|
| FF1 (CAPM) | 1 | 1964 | 市场β |
| FF3 | 3 | 1993 | 规模+价值 |
| FF5 | 5 | 2015 | 盈利+投资 |
| FF6 | 6 | 2018 | +动量 |

### FF3核心公式

$$\mathbb{E}[R_i] - r_f = \beta_i^{MKT} \cdot 0.055 + \beta_i^{SMB} \cdot 0.025 + \beta_i^{HML} \cdot 0.035$$

### 因子择股流程

```
识别因子 → 构造因子 → 估计溢价 → 计算暴露 → 选择证券
```

---

**下一步** → [[Q2.01_量化策略基础|量化策略基础]]

---

*本笔记适用于 MY_Learning 量化金融路径 · Level 1 资产定价理论 · 第4章（共4章）*
