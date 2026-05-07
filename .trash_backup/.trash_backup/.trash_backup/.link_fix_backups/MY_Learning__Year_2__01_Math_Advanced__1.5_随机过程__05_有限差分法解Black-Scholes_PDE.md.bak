# 有限差分法解 Black-Scholes PDE

> **日期**: 2026-04-09
> **分类**: 高等数学 · 随机过程 · 数值方法
> **前置知识**: [[02_Black-Scholes公式推导]], [[04_伊藤引理与二次变差]]
> **理解程度**: 4/5

---

## 1. 为什么需要有限差分法？

### 1.1 解析解的局限性

Black-Scholes 解析公式 $C(S,t) = SN(d_1) - Ke^{-r(T-t)}N(d_2)$ 依赖一个关键假设：**标的资产波动率 $\sigma$ 为常数**。

当这个假设被打破时，解析解不存在或不适用：

| 场景 | 解析解可用？ | 有限差分法优势 |
|------|------------|--------------|
| **美式期权**（可提前行权） | ❌ 否，存在自由边界问题 | ✅ 直接处理停时条件 |
| **局部波动率模型** $dv = \sigma(S,t)\,dW$ | ❌ 否，$\sigma$ 是 $S$ 的函数 | ✅ 网格随 $S$ 适应 |
| **随机波动率模型**（Heston 等）| ❌ 否，需解 2D PDE | ✅ 可扩展到高维 |
| **路径依赖期权**（亚式、障碍）| ⚠️ 部分有解析近似 | ✅ 自然处理路径积分 |
| **跳扩散模型**（Merton）| ❌ 否 | ⚠️ 需与蒙特卡洛结合 |

**美式期权的自由边界**：最优行权边界 $S^*(t)$ 未知，必须满足 **Snell 包络条件**，PDE 多了一个不等式约束：

$$
\max\!\left(\frac{\partial V}{\partial t} + \mathcal{L}V,\; V - \phi(S)\right) = 0
$$

### 1.2 有限差分法的核心思想

将 B-S PDE 在 $(S_i, t_j)$ 网格上离散化：

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - rV = 0
$$

空间导数近似：
$$
\frac{\partial V}{\partial S} \approx \frac{V_{i+1,j} - V_{i-1,j}}{2\Delta S}, \quad \frac{\partial^2 V}{\partial S^2} \approx \frac{V_{i+1,j} - 2V_{i,j} + V_{i-1,j}}{\Delta S^2}
$$

将 PDE 转化为线性代数问题求解。

---

## 2. 三种差分格式

### 2.1 显式格式（Explicit）

**核心思想**：用已知时刻 $j$ 的值直接计算 $j+1$ 时刻。

$$
V_{i,j+1} = \alpha_i V_{i-1,j} + \beta_i V_{i,j} + \gamma_i V_{i+1,j}
$$

**优点**：计算简单，$O(N)$ 每步
**致命缺陷**：**条件稳定**，要求 CFL 条件：
$$
\Delta t \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
$$

### 2.2 隐式格式（Implicit）

$$
-\alpha_i V_{i-1,j+1} + (1+\beta_i)V_{i,j+1} - \gamma_i V_{i+1,j+1} = V_{i,j}
$$

矩阵形式：**三对角矩阵**，用追赶法求解 $\mathbf{A}\,\mathbf{V}_{j+1} = \mathbf{V}_j$

**优点**：**无条件稳定**
**缺点**：每步需解线性方程组 $O(N)$

### 2.3 Crank-Nicolson 格式（CN）—— 业界首选

**核心思想**：显式和隐式的**算术平均**——在时间 $j+\tfrac{1}{2}$ 处离散化：

$$
\frac{V_i^{j+1} - V_i^j}{\Delta t} = \frac{1}{2}\left[\mathcal{L}_h V_i^{j+1} + \mathcal{L}_h V_i^j\right]
$$

整理得：

$$
-\frac{\alpha_i}{2}V_{i-1,j+1} + \left(1+\frac{\beta_i}{2}\right)V_{i,j+1} - \frac{\gamma_i}{2}V_{i+1,j+1} = \frac{\alpha_i}{2}V_{i-1,j} + \left(1-\frac{\beta_i}{2}\right)V_{i,j} + \frac{\gamma_i}{2}V_{i+1,j}
$$

矩阵形式：$\mathbf{A}\,\mathbf{V}_{j+1} = \mathbf{B}\,\mathbf{V}_j$

**优点**：
- **无条件稳定**
- **二阶精度** $O((\Delta t)^2 + (\Delta S)^2)$
- 实践中收敛最快

---

## 3. 稳定性分析：von Neumann 方法

### 3.1 方法原理

假设数值解可分离变量 $V_i^j = \xi^k e^{ik\theta}$，代入差分格式，求解**放大因子** $G(\theta)$：

$$
V_i^{j+1} = G(\theta)\,V_i^j
$$

**稳定条件**：$|G(\theta)| \leq 1,\quad \forall\,\theta \in [0,2\pi]$

### 3.2 显式格式

$$
G_{\text{explicit}} = 1 - 4\lambda\sin^2\!\left(\frac{\theta}{2}\right), \quad \lambda = \frac{\sigma^2 S^2 \Delta t}{(\Delta S)^2}
$$

$|G| \leq 1$ 要求 $\lambda \leq \tfrac{1}{2}$，即 **条件稳定**。

### 3.3 隐式格式

$$
G_{\text{implicit}} = \frac{1}{1 + 4\lambda\sin^2(\theta/2)}
$$

恒有 $|G| \leq 1$（分母 $\geq 1$），故 **无条件稳定**。

### 3.4 CN 格式

$$
G_{\text{CN}} = \frac{1 - 2\lambda\sin^2(\theta/2)}{1 + 2\lambda\sin^2(\theta/2)}
$$

恒有 $|G_{\text{CN}}| \leq 1$（中性发散 $|G| \to 1$），故 **无条件稳定 + 二阶精度**。

| 格式 | 稳定性 | 时间精度 | 每步计算量 |
|------|--------|---------|-----------|
| 显式 | 条件稳定 | 一阶 $O(\Delta t)$ | $O(N)$ |
| 隐式 | **无条件稳定** | 一阶 $O(\Delta t)$ | $O(N)$（三对角）|
| CN | **无条件稳定** | **二阶 $O((\Delta t)^2)$** | $O(N)$（三对角×2）|

---

## 4. 边界条件

### 4.1 到期条件（Terminal Condition）

期权在 $t=T$ 时价值已知，从 $t=T$ 向 $t=0$ **倒向迭代**：

$$
V(S_i, T) = \max(S_i - K,\; 0) \quad \text{（欧式看涨）}
$$

### 4.2 股价下界 $S \to 0$

- **看涨期权**：$V(0,t) = 0$
- **看跌期权**：$V(0,t) = Ke^{-r(T-t)}$

### 4.3 股价上界 $S \to S_{\max}$

取 $S_{\max} = 4K$，精确边界：

$$
V(N,j) = S_N - K e^{-r\tau_j}, \quad \tau_j = T - t_j
$$

### 4.4 美式期权的额外边界（投影步骤）

每步迭代后执行投影：

$$
V_i^j = \max\!\left(V_i^j,\; \phi(S_i)\right), \quad \phi(S) = \max(S-K, 0)
$$

结合 CN 格式即为 **CN + PSOR** 方法。

---

## 5. Python 实现：CN 格式

```python
import numpy as np
from scipy.linalg import solve_banded
from scipy.stats import norm

def bs_call_exact(S, K, T, r, sigma):
    """Black-Scholes 解析解（用于验证）"""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def crank_nicolson_bs(S0, K, T, r, sigma, M=200, N=200, Smax_factor=4):
    """
    Crank-Nicolson 格式求解 B-S PDE（欧式看涨期权）

    参数:
        S0: 标的价格
        K: 行权价
        T: 到期时间（年）
        r: 无风险利率
        sigma: 波动率
        M: 时间步数
        N: 空间步数
        Smax_factor: S_max = Smax_factor * K
    返回:
        V0: 期权估值
        S_grid: 股价网格
        V: 最终数值解向量
    """
    Smax = Smax_factor * K
    dt = T / M

    # 股价网格（等距，共 N+1 个点）
    S_grid = np.linspace(0, Smax, N + 1)

    # 内部节点索引 1:N（共 N-1 个）
    j = np.arange(1, N)

    # 离散化系数（与空间网格和时间步长相关）
    a = 0.25 * dt * (sigma**2 * j**2 - r * j)      # V_{i-1} 系数
    b = -0.5 * dt * (sigma**2 * j**2 + r)           # V_i 系数
    c = 0.25 * dt * (sigma**2 * j**2 + r * j)      # V_{i+1} 系数

    # ---- 左端矩阵 A（隐式部分，三对角）----
    # scipy solve_banded 格式：(l, u) = (1, 1)
    # ab[0, 1:] = 上对角, ab[1, :] = 对角, ab[2, :-1] = 下对角
    A = np.zeros((3, N - 1))
    A[0, 1:]  = -c[:-1]      # 上对角
    A[1, :]   = 1 - b         # 对角
    A[2, :-1] = -a[:-1]       # 下对角

    # ---- 右端矩阵 B（显式部分，三对角）----
    B = np.zeros((3, N - 1))
    B[0, 1:]  = c[:-1]
    B[1, :]   = 1 + b
    B[2, :-1] = a[:-1]

    # 终止条件 V(S, T) = max(S - K, 0)
    V = np.maximum(S_grid - K, 0.0)

    # ---- 时间倒向迭代（从 T 到 0）----
    for m in range(M - 1, -1, -1):
        tau = m * dt  # 剩余时间

        # 右端项 rhs = B @ V_internal + 边界修正
        rhs = (B[2, 0] * V[0]
             + B[2, 1:] * V[1:N-1]
             + B[1, :]  * V[1:N]
             + B[0, :-1] * V[2:N+1]
             + B[0, -1] * V[N])

        # 追赶法解线性方程组 A @ V_new = rhs
        V[1:N] = solve_banded((1, 1), A, rhs)

        # 更新边界条件（欧式看涨）
        V[0] = 0.0
        V[N] = Smax - K * np.exp(-r * tau)

    # ---- 插值得到 S0 ----
    idx = np.searchsorted(S_grid, S0)
    if idx == 0:
        return float(V[0]), S_grid, V
    elif idx >= N:
        return float(V[N]), S_grid, V
    else:
        w = (S0 - S_grid[idx-1]) / (S_grid[idx] - S_grid[idx-1])
        return float((1 - w) * V[idx-1] + w * V[idx]), S_grid, V

# ---- 验证测试 ----
if __name__ == "__main__":
    S0, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2

    V_cn, S_g, V_g = crank_nicolson_bs(S0, K, T, r, sigma, M=400, N=400)
    V_exact = bs_call_exact(S0, K, T, r, sigma)

    print(f"CN 数值解: {V_cn:.6f}")
    print(f"BS 解析解: {V_exact:.6f}")
    print(f"绝对误差:  {abs(V_cn - V_exact):.2e}")

    # 收敛阶测试
    print("\n--- 收敛阶测试 ---")
    for M in [50, 100, 200, 400]:
        V_m, _, _ = crank_nicolson_bs(S0, K, T, r, sigma, M=M, N=M)
        print(f"M=N={M:3d}: 误差 = {abs(V_m - V_exact):.2e}")
```

> **说明**：使用 `scipy.linalg.solve_banded` 处理三对角系统，时间复杂度 $O(N)$；边界处理为 $O(\Delta S)$，整体在细网格下为 CN 的二阶精度。

---

## 6. 与蒙特卡洛的对比

### 6.1 优缺点对比

| 维度 | 有限差分法（CN） | 蒙特卡洛 |
|------|----------------|---------|
| **计算速度** | 快（$O(MN)$，通常秒级）| 慢（大量路径，秒到分钟）|
| **精度** | 高（确定性，误差二阶收敛）| 低（随机误差 $\sim 1/\sqrt{N_{\text{paths}}}$）|
| **美式期权** | ✅ 自然处理（投影步骤）| ✅ 可行（LSM 算法）|
| **高维问题** | ❌ 维度灾难（网格数指数增长）| ✅ 自然扩展到高维 |
| **路径依赖** | ⚠️ 需额外处理（亚式困难）| ✅ 天然适合 |
| **波动率模型** | ✅ 局部波动率等复杂 PDE | ✅ 只需模拟 $S_t$ 路径 |
| **实现难度** | 中等（矩阵求解）| 简单（路径模拟）|

### 6.2 适用场景总结

**用有限差分法（CN）当**：
- 标的资产数量少（1-2个），波动率模型复杂
- 需要高精度、快速求解
- 美式期权（自由边界问题）

**用蒙特卡洛当**：
- 高维问题（多个标的资产）
- 路径依赖期权（亚式、障碍）
- 波动率模型复杂但可模拟（如 Heston 随机波动率）

> 💡 **实践中**：大多数量化交易台会同时使用两种方法，用 PDE/CN 做日常定价（速度优先），用 MC 做模型验证和新产品开发（灵活性优先）。

---

## 7. 自评与反思

**理解程度**: 4/5

**核心收获**：
- CN 格式的**无条件稳定性 + 二阶精度**是它的根本优势，在量化实践中几乎总是优于显式和纯隐式格式
- von Neumann 分析揭示了"中性发散"（$|G| \to 1$）和"绝对稳定"（$|G| < 1$）的区别
- 有限差分法和蒙特卡洛是互补的，前者适合低维精确求解，后者适合高维和路径依赖

**待深化**：
- 美式期权的 PSOR/罚函数方法实现
- 高维 PDE（随机波动率模型的 2D 解法）
- 与蒙特卡洛在实际定价中的具体取舍策略
