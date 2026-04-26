---
type: note
subject: optimization
chapter: 17
created: 2026-04-03
status: complete
---

# 17 - 半定规划

## 1. 半定规划的定义

### 1.1 标准形式

**半定规划（Semidefinite Programming, SDP）**：
$$\min_X \langle C, X \rangle$$
$$\text{s.t.} \quad \langle A_i, X \rangle = b_i, \quad i = 1, \ldots, m$$
$$\quad\quad X \succeq 0$$

其中：
- X 是 n×n 对称矩阵变量
- C, Aᵢ 是 n×n 对称矩阵
- ⟨A, B⟩ = tr(AᵀB) = Σᵢⱼ AᵢⱼBᵢⱼ 是矩阵内积
- X ⪰ 0 表示 X 半正定

### 1.2 与线性规划的关系

**线性规划是SDP的特例**：当 X 限制为对角矩阵时，SDP退化为LP。

**SDP是锥规划的特例**：半定锥是凸锥的一种。

### 1.3 向量化形式

将矩阵 X 按列堆叠为向量 vec(X)，SDP可写为：
$$\min c^T x$$
$$\text{s.t.} \quad Ax = b, \quad x \in \mathcal{S}_+^n$$

其中 S₊ⁿ 是 n×n 半正定矩阵构成的锥。

## 2. 半正定锥

### 2.1 定义

**半正定锥**：
$$\mathcal{S}_+^n = \{X \in \mathcal{S}^n : X \succeq 0\}$$

其中 Sⁿ 是 n×n 对称矩阵空间。

### 2.2 性质

1. **凸性**：S₊ⁿ 是凸锥
2. **闭性**：S₊ⁿ 是闭集
3. **自对偶**：S₊ⁿ 的对偶锥是其自身
4. ** pointed**：S₊ⁿ ∩ (-S₊ⁿ) = {0}

### 2.3 半正定判别

**等价条件**：
- 所有特征值非负
- 所有主子式非负
- 存在分解 X = LLᵀ

## 3. 对偶问题

### 3.1 拉格朗日对偶

**原问题**：
$$\min_X \langle C, X \rangle \quad \text{s.t.} \quad \mathcal{A}(X) = b, X \succeq 0$$

**对偶问题**：
$$\max_y b^T y$$
$$\text{s.t.} \quad C - \sum_{i=1}^{m} y_i A_i \succeq 0$$

### 3.2 强对偶性

**定理**：若原问题严格可行（存在 X ≻ 0 满足约束），则强对偶性成立。

### 3.3 互补松弛条件

**最优性条件**：
$$X \succeq 0, \quad S = C - \sum_i y_i A_i \succeq 0$$
$$\mathcal{A}(X) = b, \quad X S = 0$$

## 4. 常见SDP模型

### 4.1 最大特征值最小化

$$\min t \quad \text{s.t.} \quad tI - A(x) \succeq 0$$

其中 A(x) = A₀ + ΣxᵢAᵢ。

### 4.2 矩阵范数最小化

$$\min \|A(x)\| \quad \Leftrightarrow \quad \min t \quad \text{s.t.} \quad \begin{pmatrix} tI & A(x) \\ A(x)^T & tI \end{pmatrix} \succeq 0$$

### 4.3 和范数最小化（核范数）

矩阵 M 的核范数（奇异值之和）最小化：
$$\min \|M\|_* \quad \Leftrightarrow \quad \min \frac{1}{2}(\text{tr}(W_1) + \text{tr}(W_2)) \quad \text{s.t.} \quad \begin{pmatrix} W_1 & M \\ M^T & W_2 \end{pmatrix} \succeq 0$$

### 4.4 Goemans-Williamson MAX-CUT近似

**SDP松弛**：
$$\max \frac{1}{4}\sum_{(i,j) \in E} w_{ij}(1 - v_i^T v_j)$$
$$\text{s.t.} \quad \|v_i\| = 1, \quad v_i \in \mathbb{R}^n$$

转化为矩阵形式：
$$\max \frac{1}{4}\sum_{(i,j) \in E} w_{ij}(1 - X_{ij})$$
$$\text{s.t.} \quad X \succeq 0, \quad X_{ii} = 1$$

## 5. 求解方法

### 5.1 内点法

**障碍函数**：
$$\phi(X) = -\log\det(X)$$

**中心路径**：
$$C - \sum_i y_i A_i = \mu X^{-1}$$
$$\mathcal{A}(X) = b$$

### 5.2 原始-对偶内点法

**搜索方向**：
$$\Delta X, \Delta y, \Delta S$$

满足：
$$\mathcal{A}(\Delta X) = r_b$$
$$\Delta S + \sum_i \Delta y_i A_i = r_C$$
$$\Delta X S + X \Delta S = r_{XS}$$

### 5.3 迭代复杂度

**定理**：内点法求解SDP的迭代复杂度为 O(√n log(1/ε))。

每步计算量主要来自求解线性系统，规模为 O(m³ + mn² + n³)。

## 6. SDP的应用

### 6.1 组合优化

**MAX-CUT问题**：0.878近似算法
**图着色**：χ(G) 的下界
**最大独立集**：α(G) 的上界

### 6.2 控制理论

**Lyapunov稳定性**：找 Lyapunov 函数
**鲁棒控制**：H∞ 范数优化
**系统辨识**：结构化矩阵逼近

### 6.3 机器学习

**核学习**：学习核矩阵
**降维**：半定嵌入
**聚类**：松弛方法

### 6.4 信号处理

**传感器网络定位**：距离约束
**压缩感知**：矩阵补全
**相位恢复**：PhaseLift方法

## 7. 例子：矩阵补全

### 7.1 问题

给定部分观测到的矩阵元素 Mᵢⱼ (i,j) ∈ Ω，恢复完整矩阵。

**核范数最小化**：
$$\min_X \|X\|_* \quad \text{s.t.} \quad X_{ij} = M_{ij}, \quad (i,j) \in \Omega$$

### 7.2 SDP形式

$$\min \frac{1}{2}(\text{tr}(W_1) + \text{tr}(W_2))$$
$$\text{s.t.} \quad \begin{pmatrix} W_1 & X \\ X^T & W_2 \end{pmatrix} \succeq 0$$
$$\quad\quad X_{ij} = M_{ij}, \quad (i,j) \in \Omega$$

## 8. Python实现

```python
import numpy as np
import cvxpy as cp

# SDP示例：最大特征值最小化
n = 5
m = 3

# 定义变量
X = cp.Variable((n, n), symmetric=True)

# 定义问题参数
C = np.random.randn(n, n)
C = (C + C.T) / 2  # 对称化

A = []
b = []
for i in range(m):
    Ai = np.random.randn(n, n)
    Ai = (Ai + Ai.T) / 2
    A.append(Ai)
    b.append(np.random.randn())

# 约束：A_i•X = b_i
constraints = [X >> 0]  # 半正定约束
for i in range(m):
    constraints.append(cp.trace(A[i] @ X) == b[i])

# 目标：min C•X
problem = cp.Problem(cp.Minimize(cp.trace(C @ X)), constraints)
problem.solve()

print(f"最优值: {problem.value}")
print(f"最优矩阵X是否半正定: {np.all(np.linalg.eigvals(X.value) >= -1e-8)}")

# MAX-CUT SDP松弛示例
def max_cut_sdp(W):
    """
    W: 图的邻接矩阵/权重矩阵
    返回: 近似最大割值
    """
    n = W.shape[0]
    X = cp.Variable((n, n), symmetric=True)
    
    constraints = [X >> 0]
    for i in range(n):
        constraints.append(X[i, i] == 1)
    
    # 目标：max (1/4) * sum_{i<j} W[i,j] * (1 - X[i,j])
    objective = cp.Maximize(0.25 * cp.sum(cp.multiply(W, 1 - X)))
    
    problem = cp.Problem(objective, constraints)
    problem.solve()
    
    # 随机舍入
    x = np.random.randn(n)
    X_val = X.value
    # Cholesky分解（需添加小扰动保证正定）
    X_val = X_val + 1e-6 * np.eye(n)
    L = np.linalg.cholesky(X_val)
    v = L @ np.random.randn(n)
    
    # 割
    cut = 0
    for i in range(n):
        for j in range(i+1, n):
            if np.sign(v[i]) != np.sign(v[j]):
                cut += W[i, j]
    
    return cut, problem.value

# 测试MAX-CUT
W = np.array([[0, 1, 1, 0],
              [1, 0, 1, 1],
              [1, 1, 0, 1],
              [0, 1, 1, 0]], dtype=float)

cut, sdp_bound = max_cut_sdp(W)
print(f"SDP上界: {sdp_bound}")
print(f"随机舍入割值: {cut}")
```

## 9. 与其他凸优化问题的关系

| 问题类型 | 约束类型 | 关系 |
|----------|----------|------|
| LP | 非负约束 | SDP的特例（对角矩阵） |
| SOCP | 二阶锥约束 | SDP的特例（分块对角） |
| SDP | 半正定约束 | 最一般的凸锥规划之一 |

**包含关系**：LP ⊂ SOCP ⊂ SDP ⊂ 凸优化

## 10. 总结

**SDP的特点**：
- 表达能力强，可建模多种问题
- 多项式时间可解
- 提供组合优化问题的紧密松弛
- 每步计算量大，适合中小规模问题

**关键应用**：
- 组合优化（近似算法）
- 控制理论（稳定性分析）
- 机器学习（核学习、降维）
- 信号处理（矩阵补全）

**求解工具**：
- CVX/CVXPY（建模）
- SDPT3, SeDuMi（求解器）
- MOSEK, CPLEX（商业求解器）

---

**相关链接**：
- [[16_Interior_Point]] - 内点法
- [[09_KKT_Conditions]] - KKT条件
- [[11_Duality_Theory]] - 对偶理论
