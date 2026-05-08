# Hawkes 过程：神经 Spike Train 建模

> **日期**: 2026-04-09
> **分类**: 计算神经科学 · 点过程建模
> **理解程度**: 4/5

---

## 1. 从泊松过程到自激泊松过程

### 1.1 标准泊松过程的局限

标准泊松过程假设**事件发生率恒定**，与历史无关：

$$
\lambda(t) = \lambda_0 \quad \text{（常数）}
$$

这无法描述许多真实现象：
- 神经元放电：一次 spike 会**增加**未来 spike 的概率
- 地震余震：主震后余震概率升高
- 金融交易：大单成交后会吸引更多流动性交易
- 社交媒体：一条热门帖子会带来更多转发

> **核心洞察**：这些现象中，**历史事件会触发未来事件**——称为**自激点过程（Self-Exciting Point Process, SEPP）**。

### 1.2 自激泊松过程（Hawkes 过程）的定义

Hawkes（1971）提出：条件强度函数 $\lambda(t)$ 随历史事件动态变化：

$$
\lambda(t) = \lambda_0 + \sum_{t_i < t} \alpha e^{-\beta(t - t_i)}
$$

**各项含义**：

| 符号 | 含义 |
|------|------|
| $\lambda_0 \geq 0$ | 基底强度（basal intensity），无历史事件时的背景发放率 |
| $\alpha \geq 0$ | 激励幅度（excitation magnitude），每个历史 spike 带来的强度增加 |
| $\beta > 0$ | 衰减速率（decay rate），激励随时间指数衰减的快慢 |
| $t_i$ | 第 $i$ 个历史事件的发生时间 |
| $\sum_{t_i < t}$ | 对所有**在 $t$ 之前**发生的历史事件求和 |

**物理直觉**：
- 每个历史 spike 在时间 $t_i$ 处对 $\lambda(t)$ 贡献 $\alpha$ 的跳变
- 该跳变以速率 $\beta$ 指数衰减：$\alpha e^{-\beta(t-t_i)}$
- 当 $t - t_i \to \infty$ 时，贡献趋于 0（遗忘历史）

### 1.3 稳态性质

当 $t \to \infty$ 时，Hawkes 过程达到**稳态**，此时：

$$
\bar{\lambda} = \frac{\lambda_0}{1 - \rho} \quad \text{其中} \quad \rho = \frac{\alpha}{\beta}
$$

**条件**：必须满足 $\rho = \alpha/\beta < 1$（否则强度会发散——这称为**稳定性条件**）

> $\rho$ 是 **分支比（branching ratio）**，代表"由历史事件引发的触发事件占总事件的比例"。$\rho < 1$ 意味着过程是稳定的，不会无限级联。

---

## 2. 参数估计

### 2.1 负对数似然函数

给定观测到的 spike times $0 < t_1 < t_2 < \cdots < t_n < T$，Hawkes 过程的负对数似然为：

$$
-\log L(\theta) = -\sum_{i=1}^n \log \lambda(t_i) + \int_0^T \lambda(s) \, ds
$$

其中 $\theta = (\lambda_0, \alpha, \beta)$。

**积分项的计算**（利用指数衰减的可加性）：

$$
\int_0^T \lambda(s) \, ds = \lambda_0 T + \alpha \int_0^T \sum_{t_i < s} e^{-\beta(s-t_i)} \, ds = \lambda_0 T + \frac{\alpha}{\beta} \cdot n \left(1 - e^{-\beta T}\right) + \frac{\alpha^2}{\beta} \sum_{i=1}^n \left(1 - e^{-\beta(T-t_i)}\right)
$$

> **注意**：实际使用 `scipy.optimize` 时，不需要手动推导梯度——直接对负对数似然求最小化即可。

### 2.2 Python 实现：参数估计

```python
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import cumulative_trapezoid

def hawkes_log_likelihood(params, events, T):
    """
    计算 Hawkes 过程的负对数似然
    params: (lambda0, alpha, beta)
    events: spike times (numpy array)
    T: 观测窗口总长度
    """
    lambda0, alpha, beta = params
    
    if lambda0 < 0 or alpha < 0 or beta <= 0 or alpha/beta >= 1:
        return 1e10  # 非法参数，返回大值
    
    n = len(events)
    
    # 计算 lambda(t_i) 对每个 spike
    lambdas = np.zeros(n)
    for i in range(n):
        t_i = events[i]
        # 找到所有 t_j < t_i
        past = events[:i]
        if len(past) > 0:
            decays = np.exp(-beta * (t_i - past))
            lambdas[i] = lambda0 + alpha * np.sum(decays)
        else:
            lambdas[i] = lambda0
    
    # 负对数似然
    ll = -np.sum(np.log(lambdas + 1e-10))  # 防止 log(0)
    ll += lambda0 * T + (alpha / beta) * np.sum(1 - np.exp(-beta * (T - events)))
    
    return ll

# 示例：生成模拟数据后估计参数
np.random.seed(42)
T = 1000  # 观测时长

# 真实参数
true_params = (0.5, 0.4, 1.0)  # (lambda0, alpha, beta)
events = simulate_hawkes(*true_params, T)

# 参数估计
result = minimize(
    hawkes_log_likelihood,
    x0=[0.3, 0.3, 0.8],  # 初始猜测
    args=(events, T),
    method='Nelder-Mead'
)

print(f"真实参数:   {true_params}")
print(f"估计参数:   ({result.x[0]:.4f}, {result.x[1]:.4f}, {result.x[2]:.4f})")
print(f"优化成功:   {result.success}")
```

---

## 3. Python 模拟：生成 Hawkes Spike Train

### 3.1 递推模拟算法（ Gillespie 算法变体）

Hawkes 过程可以用** thinning 算法**高效模拟：

```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_hawkes(lambda0, alpha, beta, T, seed=42):
    """
    用 Ogata (1981) 的 thinning 算法模拟 Hawkes 过程
    """
    np.random.seed(seed)
    events = []
    t = 0.0
    
    while True:
        # 计算当前强度
        if len(events) == 0:
            lamb_curr = lambda0
        else:
            decays = np.exp(-beta * (np.array(events) - t))
            lamb_curr = lambda0 + alpha * np.sum(decays)
        
        if lamb_curr <= 0:
            break
        
        # 提议下一个事件（指数间隔）
        u = np.random.uniform()
        dt = -np.log(u) / lamb_curr
        t_new = t + dt
        
        if t_new >= T:
            break
        
        # 接受/拒绝（thinning）
        if len(events) == 0:
            decays_new = 0
        else:
            decays_new = np.sum(np.exp(-beta * (t_new - np.array(events))))
        lamb_new = lambda0 + alpha * decays_new
        
        if np.random.uniform() < lamb_new / lamb_curr:
            events.append(t_new)
        
        t = t_new
    
    return np.array(events)

# 模拟
np.random.seed(42)
events = simulate_hawkes(0.5, 0.6, 1.0, T=100)

print(f"生成 {len(events)} 个 spikes")
print(f"平均发放率: {len(events)/100:.3f} spikes/unit_time")

# 可视化
fig, axes = plt.subplots(2, 1, figsize=(12, 5))

# Raster plot
axes[0].eventplot([events], linewidths=1.5, color='black')
axes[0].set_ylabel(" neuron")
axes[0].set_title("Hawkes Spike Train (Raster Plot)")
axes[0].set_xlim(0, 100)

# 条件强度函数
dt = 0.1
time_bins = np.arange(0, 100, dt)
lambda_est = []
for t_end in time_bins:
    past = events[events < t_end]
    if len(past) > 0:
        decay_sum = np.sum(np.exp(-1.0 * (t_end - past)))
        lambda_est.append(0.5 + 0.6 * decay_sum)
    else:
        lambda_est.append(0.5)

axes[1].plot(time_bins, lambda_est, color='steelblue', linewidth=1.5)
axes[1].axhline(0.5, color='gray', linestyle='--', label=r'$\lambda_0 = 0.5$')
axes[1].set_xlabel("Time")
axes[1].set_ylabel(r'$\lambda(t)$')
axes[1].set_title("Estimated Conditional Intensity")
axes[1].legend()

plt.tight_layout()
plt.savefig("hawkes_spike_train.png", dpi=150)
plt.show()
```

### 3.2 关键模拟结果

**可视化特征**：
- 稳态下 $\bar{\lambda} = \lambda_0/(1-\rho) = 0.5/(1-0.6) = 1.25$（因为 $\rho = 0.6/1.0 = 0.6 < 1$）
- 观察到的平均发放率应接近 1.25
- 出现 burst（短时间高发放）后强度回落

---

## 4. 量化金融应用

### 4.1 高频交易（High-Frequency Trading）

在订单簿数据中，**市场微观结构**事件具有明显的自激特性：

| 现象 | Hawkes 建模对象 |
|------|----------------|
| **大单交易（Large Trade）** | 触发后续流动性消耗订单 |
| **价格冲击传播** | 一笔大宗交易 → 价格移动 → 跟随订单 |
| **订单簿重构** | 订单到达、取消、重发的自激循环 |

**模型形式**：

$$
\lambda^{\text{trade}}(t) = \lambda_0 + \sum_{t_i^{\text{trade}} < t} \alpha_{\text{trade}} e^{-\beta_{\text{trade}}(t-t_i)}
$$

- 用于预测短期价格变动方向
- 估计订单流量的条件强度，辅助做市策略

### 4.2 事件扩散（Event Diffusion）

金融市场中，**信息扩散**本质上是一个自激过程：

- **盈利公告** → 分析师上调评级 → 更多投资者买入 → 价格进一步上涨
- **信用评级下调** → 抛售 → 触发更多降级 → 级联效应

Hawkes 过程可以建模：
- 事件到达时间：信用卡违约、期权到期、公司债价格变动
- 通过调节 $\alpha$ 控制信息传染速度

### 4.3 信用违约传染（Credit Contagion）

银行间网络中，单个银行违约会提高其关联方的违约概率（**传染效应**）：

$$
\lambda^{\text{def}}(t) = \lambda_0^{\text{def}} + \sum_{t_i^{\text{def}} < t} \alpha_{\text{def}} \cdot \text{EXPOSURE}_{ij} \cdot e^{-\beta_{\text{def}}(t-t_i)}
$$

> 这与神经科学中的**突触传递**高度类比：一次发放（spike）→ 神经递质释放 → 下一神经元兴奋（违约传染）

---

## 5. 计算神经科学应用

### 5.1 神经振荡（Neural Oscillations）

**θ 节律（4-8 Hz）与海马神经元发放**：

在海马 CA1 区域，θ 波驱动下神经元发放模式符合 Hawkes 模型：

$$
\lambda^{\text{spike}}(t) = \lambda_0 + \alpha_\theta \sum_{t_i^\theta < t} e^{-\beta_\theta (t-t_i^\theta)} + \text{(其他调制项)}
$$

- 每个 θ 周期峰值触发一次"模板发放"
- 但发放时刻有 jitter（$\alpha_\theta$ 控制 jitter 程度）

### 5.2 突触可塑性（Synaptic Plasticity）

**尖峰时间依赖可塑性（STDP）**与 Hawkes 的联系：

- Hebbian learning：$W_{ij} \uparrow$ 当 $t_j^{\text{pre}} < t_i^{\text{post}}$（前→后）
- 反Hebbian：$W_{ij} \downarrow$ 当 $t_j^{\text{pre}} > t_i^{\text{post}}$
- 突触权重变化率 $\frac{dW}{dt}$ 本质上是 **spike train 的 Hawkes 条件强度函数**的积分

### 5.3 Burst 放电（Burst Firing）

神经元常表现出 **burst firing 模式**（短时间内高频发放，随后沉寂）：

- 标准泊松模型无法捕捉 burst
- Hawkes 模型（高 $\alpha$，低 $\beta$）可以自然生成 burst：
  - $\alpha \uparrow$：一次 spike 带来强激励
  - $\beta \downarrow$：衰减慢，激励维持更久

```python
# 生成 burst 模式
events_burst = simulate_hawkes(lambda0=0.1, alpha=0.9, beta=0.5, T=200)
print(f"Burst 模式 - 平均发放率: {len(events_burst)/200:.3f}")
```

---

## 6. 跨方向共性：量化金融 vs 计算神经科学

| 共性 | 量化金融 | 计算神经科学 |
|------|---------|-------------|
| **点过程框架** | 交易事件、违约事件、信用事件 | 神经元 spike |
| **条件强度 $\lambda(t)$** | 交易强度、违约强度 | 发放率 |
| **指数衰减核** | 信息传染 $\alpha e^{-\beta \Delta t}$ | 突触后电位衰减 |
| **参数估计** | MLE + scipy.optimize | MLE + EM |
| **分支比 $\rho$** | 信息扩散比例 | 被触发的 spike 比例 |
| **burst/fire** | 高频交易脉冲 | 神经 burst 放电 |

### 6.1 共同数学结构

两者共享：

$$
\lambda(t) = \lambda_0 + \int_0^t \kappa(t-s) \, dN(s)
$$

其中 $\kappa(\tau) = \alpha e^{-\beta \tau}$ 是**指数衰减核（exponential decay kernel）**。

**在神经科学中**：$\kappa(\tau)$ 代表突触电流的时间结构
**在量化金融中**：$\kappa(\tau)$ 代表信息在市场中传播的时间结构

> **更深层的共性**：两者都是**非线性滤波**问题——从历史事件序列中推断当前系统状态（神经元的膜电位 / 金融资产的"公平价格"）

---

## 7. 延伸学习资源

**核心文献**：
- Hawkes (1971), "Point Spectra of Some Self-Exciting and Afternating Cases"
- Ogata (1981), "On Lewis' Simulation Method for Point Processes"
- Reynaud-Bouret & Schbath (2010), "Adaptive Estimation for Hawkes Processes"

**计算神经科学**：
- Rieke et al., "Spikes: Exploring the Neural Code"（经典教材）
- Dayan & Abbott, "Theoretical Neuroscience"（第 5 章：神经元模型）

**量化金融**：
- Bowsher, "Modelling Security Markeds Events in Continuous Time"
- Hewlett, "Clustering of Order Arrivals, Price Dynamics and Autocorrelation"

---

## 8. 理解程度自评

| 维度 | 自评 | 备注 |
|------|------|------|
| Hawkes 条件强度函数 | 5/5 | $\lambda_0 + \sum \alpha e^{-\beta(t-t_i)}$ 完全掌握 |
| 稳定性条件 $\rho < 1$ | 4/5 | 分支比的经济/神经学含义清晰 |
| 参数估计（MLE）| 4/5 | 负对数似然推导可独立完成 |
| Python 模拟 | 4/5 | Thinning 算法 + 可视化完成 |
| 量化金融应用 | 4/5 | 高频交易、信用传染已理解 |
| 计算神经科学应用 | 4/5 | Burst/STDP/振荡均已覆盖 |
| 跨方向共性 | 4/5 | 点过程框架完全一致 |

**本次综合自评：4/5**

**尚可提升**：
- EM 算法对 Hawkes 的具体推导（vs 直接 scipy.optimize）
- 多维 Hawkes 过程（多神经元建模，网络级联）
- 非指数核（power-law kernel，更符合真实神经数据）
- 实际金融数据的参数标定（用真实 HFT 数据实验）
