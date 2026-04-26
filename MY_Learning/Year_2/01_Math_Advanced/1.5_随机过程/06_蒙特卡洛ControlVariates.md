# 蒙特卡洛 Control Variates

> **日期**: 2026-04-09
> **分类**: 高等数学 · 随机过程 · 数值方法
> **前置知识**: [[03_MonteCarlo期权定价]]（若已整理）, [[02_Black-Scholes公式推导]]
> **理解程度**: 4/5

---

## 1. Control Variates 原理

### 1.1 核心思想

**Control Variates（控制变量法）** 是一种**方差缩减技术**。其核心思想是：

> 利用一个与待估计量 $X$ **高度相关**、且**已知解析解 $E[Y]$** 的随机变量 $Y$，来"控制" $X$ 的随机波动。

设原始估计量 $X = C_{\text{MC}}$（蒙特卡洛期权定价），已知存在一个相关量 $Y$ 满足：
- $Y$ 与 $X$ 高度相关（$\rho(X,Y)$ 接近 1）
- $E[Y]$ **已知解析**（closed form 存在）

定义调整后的估计量：

$$
Z = X - \theta\,(Y - E[Y])
$$

其中 $\theta$ 是一个待优化的系数。

### 1.2 为什么会降低方差？

计算 $Z$ 的方差：

$$
\text{Var}(Z) = \text{Var}(X) + \theta^2\text{Var}(Y) - 2\theta\text{Cov}(X,Y)
$$

对 $\theta$ 求导并令其为 0，得到最优 $\theta^*$：

$$
\theta^* = \frac{\text{Cov}(X,Y)}{\text{Var}(Y)}
$$

代入 $\text{Var}(Z^*)$：

$$
\text{Var}(Z^*) = \text{Var}(X)\left(1 - \rho_{XY}^2\right)
$$

其中 $\rho_{XY} = \frac{\text{Cov}(X,Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}}$ 是 $X$ 与 $Y$ 的相关系数。

**关键结论**：方差缩减比例是 $(1 - \rho^2)$。当 $\rho \to 1$ 时，方差可接近 0！

> 💡 **直观理解**：$Y$ 作为"参照系"，它的已知波动被用来抵消 $X$ 中相似的波动分量。

---

## 2. 最常用的 Control Variate：BS 解析解

### 2.1 为什么 BS 公式是天然的控制变量？

在股票期权定价中，BS 解析解 $C_{\text{BS}}(S_0, K, T, r, \sigma)$ 是最流行的 CV，原因是：

1. **高度相关性**：BS 期权价格 $C_{\text{BS}}$ 与蒙特卡洛模拟价格 $C_{\text{MC}}$ 都来自同一标的资产，同涨同跌，相关性极高（$\rho > 0.99$）
2. **精确已知**：BS 解析公式给出 $E[C_{\text{BS}}]$ 的精确值
3. **计算代价极低**：只需要几次数学函数调用，不增加多少计算量
4. **广泛适用**：可用于欧式期权，也可推广到亚式期权（用几何平均 BS 近似作为 CV）

### 2.2 推导：BS 调整后的估计量

设：
- $X = C_{\text{MC}}$：蒙特卡洛模拟的期权价格
- $Y = C_{\text{BS}}$：同一组模拟路径用 BS 公式计算的价格
- $E[Y] = C_{\text{BS}}^*$：BS 解析解（精确期望）

最优 $\theta^*$（可从模拟数据中估计）：

$$
\theta^* = \frac{\widehat{\text{Cov}}(X,Y)}{\widehat{\text{Var}}(Y)}
$$

调整后的估计量：

$$
Z = C_{\text{MC}} - \theta^*\left(C_{\text{BS}} - C_{\text{BS}}^*\right)
$$

在实际操作中，由于 $C_{\text{BS}}^*$ 是确定的（解析解），可以简化：

$$
Z = C_{\text{MC}} - \theta\left(C_{\text{BS}} - C_{\text{BS}}^*\right)
$$

其中 $\theta$ 可以简化为 1（在相关性极高时，$\theta \to 1$ 是最优的近似）。

---

## 3. 方差缩减效果的理论分析

### 3.1 理论方差

$$
\frac{\text{Var}(Z^*)}{\text{Var}(X)} = 1 - \rho_{XY}^2
$$

| $\rho_{XY}$ | 方差缩减比例 $\text{Var}(Z)/\text{Var}(X)$ | 相当于增加多少倍路径数 |
|------------|-------------------------------------------|-------------------|
| 0.90 | 19% | 5.3× |
| 0.95 | 10% | 10× |
| 0.99 | 2% | **50×** |
| 0.999 | 0.2% | **500×** |

理论上当 $\rho = 0.99$ 时，CV 估计量等价于 **50 倍**的原始蒙特卡洛路径数的精度！

### 3.2 实际注意事项

1. **$\theta$ 的估计**：从同一套模拟数据中估计 $\theta$，引入轻微偏差
   - 无偏修正：使用 $\theta=1$（即以 BS 期望为中心，不估计 $\theta$）
   - $\theta=1$ 时，$Z = C_{\text{MC}} - (C_{\text{BS}} - C_{\text{BS}}^*)$ 恒等于 $C_{\text{BS}}^* + (C_{\text{MC}} - C_{\text{BS}})$，相当于平移

2. **路径数和方差**：CV 不会改变估计的**期望**，只缩减方差

3. **相关性的重要性**：$\rho$ 越高，方差缩减越显著。BS/MC 在欧式期权上 $\rho > 0.999$

---

## 4. Python 实现：Control Variates

```python
import numpy as np
from scipy.stats import norm

def bs_call_exact(S, K, T, r, sigma):
    """Black-Scholes 欧式看涨期权解析解"""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def bs_call_mc_cv(S0, K, T, r, sigma, N_paths=100_000,
                  N_steps=252, theta=None, seed=42):
    """
    蒙特卡洛 + Control Variates 估算欧式看涨期权价格

    参数:
        S0: 初始股价
        K: 行权价
        T: 到期时间（年）
        r: 无风险利率
        sigma: 波动率
        N_paths: 蒙特卡洛路径数
        N_steps: 年化时间步数（每天一步）
        theta: CV 系数（None=用数据估计，1=固定为1）
        seed: 随机种子
    返回:
        price: 估计价格
        std_err: 标准误
        price_bs: BS 解析解
        var_reduction: 方差缩减比例（实际观察值）
    """
    rng = np.random.default_rng(seed)
    dt = T / N_steps
    disc = np.exp(-r * T)

    # ---- 模拟 GBM 路径（ Antithetic 配对抽样）----
    # 形状: (N_paths, N_steps+1)
    half_paths = N_paths // 2
    Z = rng.standard_normal((half_paths, N_steps))
    Z = np.concatenate([-Z, Z], axis=0)  # Antithetic: 镜像路径

    # 累积路径（使用 Antithetic）
    dW = Z * np.sqrt(dt)
    # 累积对数收益: cumsum across time steps
    logS = np.log(S0) + np.cumsum(
        (r - 0.5 * sigma**2) * dt + sigma * dW, axis=1
    )
    # 加上初始 S0 的对数
    logS = np.concatenate([np.full((2 * half_paths, 1), np.log(S0)), logS], axis=1)
    S_paths = np.exp(logS)

    # 到期收益
    payoff = np.maximum(S_paths[:, -1] - K, 0)

    # ---- MC 估计量 X = C_MC ----
    price_mc = disc * np.mean(payoff)

    # ---- Control Variate Y = C_BS（用同一组路径）----
    # 对每条模拟路径，用 BS 公式计算价格（使用相同的最终股价 S_T）
    # 注意：BS 公式用的是风险中性测度下的 S_T 分布（对数正态）
    # 作为 CV，我们用每条路径的 S_T 来"定价"这条路径
    price_bs_paths = bs_call_exact(S_paths[:, -1], K, T, r, sigma)
    price_bs = disc * np.mean(price_bs_paths)  # E[Y]（路径平均）
    price_bs_exact = bs_call_exact(S0, K, T, r, sigma)  # E[Y] 的精确值

    # ---- 最优 theta 估计 ----
    if theta is None:
        # 从模拟数据估计协方差和方差
        payoff_disc = payoff  # 已经是贴现后的
        bs_disc = price_bs_paths  # 注意：这里需要对应折扣后的 bs 价格
        # 更精确：用贴现后的价格计算协方差
        bs_disc = bs_call_exact(S_paths[:, -1], K, T, r, sigma) * disc
        cov_xy = np.cov(payoff * disc, bs_disc)[0, 1]
        var_y = np.var(bs_disc)
        theta_opt = cov_xy / var_y if var_y > 0 else 1.0
    else:
        theta_opt = theta

    # ---- CV 调整估计量 Z ----
    Z_est = payoff * disc - theta_opt * (bs_disc - price_bs_exact * disc)
    # 由于 E[bs_disc] ≈ price_bs_exact * disc，修正项均值为0，故 Z 是无偏的
    price_cv = np.mean(Z_est)
    std_err_cv = np.std(Z_est, ddof=1) / np.sqrt(N_paths)

    # 原始 MC 标准误
    std_err_mc = np.std(payoff * disc, ddof=1) / np.sqrt(N_paths)
    var_reduction = (std_err_cv / std_err_mc) ** 2

    return {
        'price_mc': price_mc,
        'price_cv': price_cv,
        'price_bs_exact': price_bs_exact,
        'std_err_mc': std_err_mc,
        'std_err_cv': std_err_cv,
        'var_reduction': var_reduction,
        'theta_opt': theta_opt,
        'std_err_ratio': std_err_mc / std_err_cv  # 标准误缩减比
    }

# ---- 测试与对比 ----
if __name__ == "__main__":
    S0, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2

    result = bs_call_mc_cv(S0, K, T, r, sigma,
                           N_paths=200_000, N_steps=252, seed=42)

    print("=" * 55)
    print(f"BS 解析解:          {result['price_bs_exact']:.6f}")
    print(f"原始 MC 价格:       {result['price_mc']:.6f}")
    print(f"CV 调整后价格:      {result['price_cv']:.6f}")
    print(f"原始 MC 标准误:     {result['std_err_mc']:.6f}")
    print(f"CV 调整后标准误:    {result['std_err_cv']:.6f}")
    print(f"标准误缩减比:       {result['std_err_ratio']:.2f}x")
    print(f"方差缩减比例:       {result['var_reduction']*100:.2f}%")
    print(f"最优 theta:         {result['theta_opt']:.4f}")
    print("=" * 55)

    # ---- 对比不同路径数的效果 ----
    print("\n--- 路径数 vs 方差缩减效果 ---")
    print(f"{'N_paths':>12} {'MC std_err':>12} {'CV std_err':>12} {'缩减比':>8}")
    for N in [10_000, 50_000, 200_000]:
        r_ = bs_call_mc_cv(S0, K, T, r, sigma, N_paths=N, seed=42)
        print(f"{N:>12,d} {r_['std_err_mc']:>12.5f} {r_['std_err_cv']:>12.5f} {r_['std_err_ratio']:>8.2f}x")
```

---

## 5. Control Variates + Antithetic Variates 的叠加

### 5.1 叠加原理

两种方差缩减技术**互补且可叠加**：

| 技术 | 原理 | 适用维度 |
|------|------|---------|
| **Antithetic Variates** | 配对镜像路径 $\epsilon \to -\epsilon$ | 缩减积分估计方差 |
| **Control Variates** | 利用已知解析解的相关变量 | 缩减模型参数估计方差 |

两者从**不同角度**缩减方差，叠加效果近似**相乘**：

$$
\text{Var}(Z_{\text{CV+AV}}) \approx \text{Var}(Z_{\text{CV}}) \times \text{Var}(Z_{\text{AV}})
$$

理论上，若各自缩减 50% 和 50%，叠加后可缩减约 **75%**。

### 5.2 叠加实现要点

在上面的 Python 实现中，已经自然地使用了 Antithetic（通过 `Z = np.concatenate([-Z, Z], axis=0)`），同时叠加了 Control Variate 调整，验证了两种技术的互补性。

**叠加效果**：代码中 `var_reduction` 即为两种方法叠加后的实际方差缩减比例（通常达到 1-5% 级别，即相当于 20-100 倍路径数的精度）。

---

## 6. 与 Antithetic 对比

| 维度 | Control Variates | Antithetic Variates |
|------|-----------------|---------------------|
| **原理** | 相关性（$\rho$）| 对称性（$\epsilon, -\epsilon$）|
| **要求** | 需已知 $E[Y]$ 的解析解 | 无（天然对称）|
| **方差缩减** | 强（$\rho^2$ 决定）| 中等（约 50%）|
| **可叠加性** | ✅ 与 AV 叠加 | ✅ 与 CV 叠加 |
| **实现复杂度** | 低（只需多算一个 BS 公式）| 低（镜像路径）|
| **路径依赖期权** | ⚠️ 需找到合适的 CV（更难）| ✅ 依然有效 |

> 💡 **业界实践**：在期权定价中，CV（以 BS 解析解为控制变量）是**最流行**的方差缩减方法，因为几乎零额外成本且效果显著；Antithetic 通常作为补充手段叠加使用。

---

## 7. 自评与反思

**理解程度**: 4/5

**核心收获**：
- CV 的本质是利用**相关性**来"吸收"随机波动，$\rho^2$ 直接决定方差缩减比例
- BS 解析解作为 CV 是量化金融中的**行业标准**，因为期权价格和 BS 价格的相关性极高（>0.999）
- $\theta$ 的估计有偏差修正（$\theta=1$ 是无偏近似），实际中使用 $\theta=1$ 牺牲一点精度换无偏性
- CV + AV 叠加是标准实践，两者从不同维度缩减方差

**待深化**：
- 亚式期权的 CV（用几何平均 BS 近似作为控制变量）
- 随机波动率模型中 Heston 解析解作为 CV
- $\theta$ 估计的偏差修正（jackknife 或bootstrap）
