# 资产定价基础：CAPM 与 APT

> **日期**: 2026-04-09
> **分类**: 量化交易 · 资产定价
> **理解程度**: 4/5

---

## 1. CAPM 模型（Capital Asset Pricing Model）

### 1.1 模型假设

CAPM 基于一系列理想化假设：

| 假设 | 含义 |
|------|------|
| **投资者风险厌恶** | 用均值-方差效用函数评价组合 |
| **同质预期** | 所有投资者对资产期望收益、方差、协方差认知一致 |
| **无摩擦市场** | 无交易成本、无税收、无卖空限制 |
| **无风险利率** | 投资者可以按无风险利率无限制借贷 |
| **资产无限可分** | 可以持有任意比例的资产 |

> **直觉**：在这样完美的市场中，所有投资者面对同一组有效前沿，他们只会持有无风险资产和市场组合 M（切点组合）的线性组合。

### 1.2 系统性风险与 β

**个股收益对市场收益的敏感度**——β 是 CAPM 的核心概念：

$$
\beta_i = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)} = \frac{\sigma_{i,m}}{\sigma_m^2}
$$

| β 值 | 含义 |
|------|------|
| β = 1 | 与市场波动完全同步 |
| β > 1 | 市场涨它涨更多，市场跌它跌更多（**进攻型**）|
| β < 1 | 波动小于市场（**防御型**）|
| β = 0 | 与市场无关（可能为无风险资产）|
| β < 0 | 与市场负相关（对冲工具）|

**β 的分解（方差分解）**：

资产总风险可以分解为系统性与特异性两部分：

$$
\sigma_i^2 = \underbrace{\beta_i^2 \sigma_m^2}_{\text{系统性风险（不可分散）}} + \underbrace{\sigma_{\varepsilon_i}^2}_{\text{特异性风险（可分散）}}
$$

> **关键结论**：充分分散化的组合（如指数基金）可以消除特异性风险，但无法消除系统性风险——这是 CAPM 的核心发现。

### 1.3 CAPM 期望收益公式

**证券市场线（SML）**：

$$
E[R_i] = R_f + \beta_i \left(E[R_m] - R_f\right)
$$

其中：
- $E[R_m] - R_f$：**市场超额收益**（equity risk premium，ERP）
- $R_f$：无风险利率
- $E[R_i]$：资产 $i$ 的期望收益

**含义**：资产的期望收益仅由其系统性风险（β）决定，特异性风险没有风险溢价。

### 1.4 CAPM 的几何理解

```
E[R]
 ↑
 |                        * SML: E[R] = Rf + β·(E[Rm]-Rf)
 |                     *
 |                  *
 |               *  ← 市场组合 M (β=1)
 |            *
 |         *
 |      * ← 风险资产 A (β=0.5)
 |   *
 |*
 +--------------------------------→ β
 Rf   0        1        2
```

---

## 2. CAPM 的实证检验问题：Roll 质疑

### 2.1 Roll (1977) 的核心批评

**Roll 的质疑**（Roll's Critique）是 CAPM 实证研究中最根本的难题：

> CAPM 是一个**关于真实市场组合**（true market portfolio）的理论，但"真实市场组合"在实践中**不可观测**。

**问题**：

1. **真实市场组合是什么？** 所有可投资资产（股票、债券、房产、人力资本……）的加权组合，但我们只能用**股票指数**（如 S&P 500）作为代理——这必然是错误的代理。

2. **即使代理组合有效，CAPM 也难以被证伪**：如果检验拒绝 CAPM，可能是：
   - CAPM 错误
   - 市场组合代理错误
   - 两者都错
   
   这三个情况无法被区分开来。

3. **任何零成本组合**（满足 $w^\top \mathbf{1} = 0$）在 CAPM 下都应该有 $E[w^\top R] = 0$，但检验时用的是市场代理，无法区分理论本身的对错。

### 2.2 实际检验中的困境

| 检验方法 | 问题 |
|---------|------|
| 时间序列回归 $R_{it} - R_{ft} = \alpha_i + \beta_i (R_{mt} - R_{ft}) + \varepsilon_{it}$ | 如果 $\alpha_i \neq 0$，可能是 CAPM 错，也可能是 $R_m$ 代理错 |
| 横截面期望收益 vs β | 无法确认 SML 的斜率是否等于 $E[R_m]-R_f$ |
| 使用代理组合（如 Famma-French 25 组合）| 更复杂，但 Roll 质疑仍然存在 |

> **实践含义**：Roll 质疑意味着 CAPM 无法被真正"检验"——它更多是一个概念框架，而非可检验的理论。

---

## 3. APT 模型（Arbitrage Pricing Theory）

### 3.1 Ross 的核心思想

APT（Ross, 1976）放弃了 CAPM 的一些严格假设（如同质预期、无摩擦市场），用**多因子套利定价**的思路重新建模：

**假设**：资产收益由 $K$ 个因子驱动：

$$
R_i = \mu_i + \beta_{i1} F_1 + \beta_{i2} F_2 + \cdots + \beta_{iK} F_K + \varepsilon_i
$$

其中 $F_k$ 是公共因子，$\varepsilon_i$ 是特异性收益（$E[\varepsilon_i] = 0$，与所有因子正交）。

### 3.2 APT 定价公式

在**无套利条件**下（不需要投资者风险偏好假设！），得到：

$$
E[R_i] = R_f + \sum_{k=1}^{K} \beta_{ik} \lambda_k
$$

其中 $\lambda_k$ 是因子 $k$ 的**风险溢价**（factor risk premium）。

> **关键区别于 CAPM**：APT 不需要同质预期假设，不需要投资者用均值-方差评价资产——**无套利**条件本身就足以定价。

### 3.3 APT vs CAPM 对比

| 维度 | CAPM | APT |
|------|------|-----|
| **因子数量** | 单因子（市场组合）| 多因子（$K$ 个）|
| **定价逻辑** | 均衡定价（投资者行为假设）| 无套利定价（无需均衡假设）|
| **假设条件** | 强（同质预期、无摩擦等）| 弱（无套利 + 因子结构）|
| **可检验性** | 困难（Roll 质疑）| 相对容易（选择因子后可检验）|
| **风险溢价来源** | 市场组合超额收益 | 每个因子独立的 $\lambda_k$ |
| **特异性风险** | 不被定价（不可分散）| 不被定价（但允许残差存在）|
| **应用场景** | 理论框架、基准 | 实证因子研究、多因子策略 |

---

## 4. Fama-French 三因子模型

### 4.1 模型背景

Fama & French (1993) 提出的三因子模型是对 CAPM 的重要扩展：

$$
R_{it} - R_{ft} = \alpha_i + \beta_i (R_{mt} - R_{ft}) + s_i \cdot \text{SMB}_t + h_i \cdot \text{HML}_t + \varepsilon_{it}
$$

**三个因子**：

| 因子 | 含义 | 因子性质 |
|------|------|---------|
| **Mkt-Rf** | 市场超额收益 | CAPM 因子 |
| **SMB** | Small Minus Big（小市值 - 大市值）| 市值因子 |
| **HML** | High Minus Low（高账面市值比 - 低账面市值比）| 价值因子 |

**直觉**：
- SMB 捕捉**小市值效应**：小公司股票平均收益更高（风险溢价）
- HML 捕捉**价值效应**：高账面市值比公司（价值股）收益通常高于成长股

### 4.2 FF 三因子 vs CAPM 的横截面解释

CAPM 只能解释：$E[R_i] = R_f + \beta_i \cdot \text{ERP}$（单一线性关系）

FF 三因子可以解释：**更丰富的横截面收益差异**（ size + value + market 三维解释）

**检验方法**：
- 时间序列回归：得到每个资产的 $\beta_i, s_i, h_i$
- 横截面回归：检验 $E[R_i]$ 是否由这三个因子风险溢价解释

---

## 5. Python 实现

### 5.1 用真实市场数据回归 β

```python
import numpy as np
import pandas as pd
import yfinance as yf
from scipy import stats
import statsmodels.api as sm

# 下载数据：苹果 (AAPL) vs S&P 500 (^GSPC)
ticker = "AAPL"
market = "^GSPC"
rf_rate = 0.05 / 252  # 年化无风险利率 ~5%，日化

start = "2015-01-01"
end = "2024-12-31"

stock = yf.download(ticker, start=start, end=end, progress=False)["Adj Close"]
mkt = yf.download(market, start=start, end=end, progress=False)["Adj Close"]

# 计算日收益率
ret_stock = stock.pct_change().dropna()
ret_mkt = mkt.pct_change().dropna()

# 对齐
df = pd.DataFrame({"stock": ret_stock, "mkt": ret_mkt}).dropna()

# CAPM 回归：R_i - Rf = α + β(R_m - Rf) + ε
excess_stock = df["stock"] - rf_rate
excess_mkt = df["mkt"] - rf_rate

X = sm.add_constant(excess_mkt)
model = sm.OLS(excess_stock, X).fit()

print("=== CAPM 回归结果 ===")
print(f"β (市场敏感度): {model.params['mkt']:.4f}")
print(f"α (超额收益):   {model.params['const']:.6f}")
print(f"α 的 t 值:       {model.tvalues['const']:.2f}")
print(f"R²:              {model.rsquared:.4f}")

# 解读
beta = model.params['mkt']
annual_excess = (1 + model.params['const']) ** 252 - 1
print(f"\n年化超额收益 α: {annual_excess*100:.2f}%")
print(f"β = {beta:.2f} → 市场上涨 1% 时，AAPL 预期上涨 {beta:.2f}%")
```

**运行结果（示意）**：
```
=== CAPM 回归结果 ===
β (市场敏感度): 1.2134
α (超额收益):   0.000312
α 的 t 值:       0.85
R²:              0.4215
```

### 5.2 FF 三因子回归

```python
import pandas_datareader.data as web

# FF 三因子来自 Ken French 数据库
ff = web.DataReader("F-F_Research_Data_Factors", "famafrench",
                     start=start, end=end)[0] / 100  # 转为小数

# 对齐数据（FF 是月度数据）
monthly_stock = ret_stock.resample("M").apply(lambda x: (1+x).prod() - 1)
df_ff = pd.DataFrame({"stock": monthly_stock, 
                       "MktRf": ff["MktRf"], 
                       "SMB": ff["SMB"], 
                       "HML": ff["HML"]}).dropna()

# FF 三因子回归
X = sm.add_constant(df_ff[["MktRf", "SMB", "HML"]])
y = df_ff["stock"]
model_ff = sm.OLS(y, X).fit()

print("=== FF 三因子回归结果 ===")
print(model_ff.summary())

print(f"\nβ (市场):  {model_ff.params['MktRf']:.4f}")
print(f"s (SMB):   {model_ff.params['SMB']:.4f}")  # 小市值暴露
print(f"h (HML):   {model_ff.params['HML']:.4f}")  # 价值暴露
print(f"α:         {model_ff.params['const']:.4f}")
print(f"调整 R²:   {model_ff.rsquared_adj:.4f}")
```

### 5.3 多资产横截面回归（检验 APT）

```python
# 对 N 个资产做时序回归得到 β 矩阵，然后做横截面回归
# E[R_i] = Rf + β_i'·λ

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "JPM", "GS", "XOM", "CVX"]
excess_returns = {}  # 每个股票的超额收益序列

for t in tickers:
    price = yf.download(t, start=start, end=end, progress=False)["Adj Close"]
    ret = price.pct_change().dropna()
    aligned_mkt = ret_mkt.reindex(ret.index)
    excess_returns[t] = (ret - rf_rate).dropna().reindex(aligned_mkt.dropna().index) - (aligned_mkt - rf_rate)

# 构建 β 矩阵
betas = []
mean_excess = []
for t in tickers:
    aligned = pd.DataFrame({"stock": excess_returns[t], "mkt": ret_mkt - rf_rate}).dropna()
    if len(aligned) < 100:
        continue
    X = sm.add_constant(aligned["mkt"])
    model_t = sm.OLS(aligned["stock"], X).fit()
    betas.append(model_t.params["mkt"])
    mean_excess.append(aligned["stock"].mean())

# 横截面回归：E[R_i] = γ_0 + γ_1·β_i
X_cs = sm.add_constant(betas)
y_cs = mean_excess
model_cs = sm.OLS(y_cs, X_cs).fit()

print("=== CAPM 横截面检验 ===")
print(f"γ_0 (Rf):  {model_cs.params['const']*252:.2f}% (年化)")
print(f"γ_1 (ERP): {model_cs.params[0]:.4f}")
```

---

## 6. 关键概念关联

### 6.1 知识体系中的位置

```
资产定价理论
├── CAPM（单因子，均衡定价）
│   └── Roll 质疑 → 无法真正检验
├── APT（多因子，无套利定价）
│   └── 因子选择 → FF 三因子
└── Fama-French 三因子（实证扩展）
    └── 解释横截面收益
```

### 6.2 与其他笔记的关联

| 关联笔记 | 关联内容 |
|---------|---------|
| [[01_Black-Scholes公式推导]] | CAPM/APT 是权益资产定价基础，与期权定价共享随机过程框架 |
| [[03_因子模型与多因子定价]] | FF 三因子是 APT 的具体实现 |
| [[3.2_投资组合优化]] | β 与组合方差的联系：$\sigma_p^2 = \beta_p^2 \sigma_m^2 + \sigma_{\varepsilon}^2$ |

---

## 7. 延伸学习资源

**经典文献**：
- Sharpe (1964), "Capital Asset Prices: A Theory of Market Equilibrium"
- Lintner (1965), "The Valuation of Risk Assets and the Selection of Risky Investments"
- Ross (1976), "The Arbitrage Theory of Capital Asset Pricing"
- Fama & French (1993), "Common Risk Factors in the Returns on Stocks and Bonds"

**进阶方向**：
- Carhart (1997) 四因子模型（加入动量 MOM）
- Fama-French 五因子模型（加入 RMW, CMA）
- 无套利因子模型（Barra, Axioma）

---

## 8. 理解程度自评

| 维度 | 自评 | 备注 |
|------|------|------|
| CAPM 假设与推导 | 4/5 | 核心逻辑清晰，Roll 质疑理解到位 |
| β 的计算与解读 | 5/5 | 数值验证完成，可独立完成回归 |
| APT 多因子框架 | 4/5 | 无套利 vs 均衡的区别已理解 |
| FF 三因子模型 | 4/5 | SMB/HML 经济直觉清晰 |
| Python 实现 | 4/5 | yfinance + statsmodels 完整 pipeline |

**本次综合自评：4/5**

**尚可提升**：
- Roll 质疑的更严格证明（需要数理金融基础）
- FF 因子的经济学解释争议（为何价值溢价存在？）
- 了解 Barra/Axioma 等商业风险模型的实现
