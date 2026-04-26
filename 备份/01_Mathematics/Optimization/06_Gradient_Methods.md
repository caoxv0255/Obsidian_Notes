---
type: note
subject: optimization
chapter: 06
created: 2026-04-03
status: complete
---

# 06 - 梯度下降法

## 📌 学习目标

- 理解为什么最速下降方向是 $-\nabla f(x)$
- 掌握常用步长策略（回溯/Armijo/Wolfe/固定步长）的使用场景
- 能读懂凸/强凸情形下的收敛结论与条件数 $\kappa$ 的影响

## 难度分层

- **基础**：算法形式 + 固定步长的直觉与基本收敛
- **进阶**：线搜索条件（Armijo/Wolfe）与强凸线性收敛
- **拓展**：动量/Nesterov/随机梯度的对比与适用边界

## 1. 梯度下降法的基本原理

### 1.1 直观理解

**核心思想**：沿着函数值下降最快的方向迭代。

**最速下降方向**：函数 f 在点 x 处**下降最快**的方向是 -∇f(x)。

**依据**：
$$f(x + td) \approx f(x) + t\nabla f(x)^T d + O(t^2)$$

当 d = -∇f(x)/‖∇f(x)‖ 时，∇f(x)ᵀd 最小，下降最快。

### 1.2 梯度下降算法

**算法**：
```
初始化 x_0
for k = 0, 1, 2, ...
    计算梯度 g_k = ∇f(x_k)
    确定步长 t_k（线搜索）
    更新 x_{k+1} = x_k - t_k * g_k
    判断收敛：‖g_k‖ < ε
```

**关键问题**：
1. 如何选择步长 t_k？
2. 收敛速度如何？
3. 如何加速收敛？

### 1.3 几何解释

**等高线视角**：
- 梯度方向垂直于等高线
- 梯度下降沿着等高线的法线方向
- 最优路径应该沿"山谷"方向

**条件数影响**：
- 条件数 κ = L/μ（Hessian 最大/最小特征值之比）
- κ 大：等高线呈狭长椭圆，收敛慢
- κ 小：等高线接近圆，收敛快

## 2. 步长选择策略

### 2.1 精确线搜索

**方法**：选择最优步长
$$t_k = \arg\min_{t > 0} f(x_k - t \nabla f(x_k))$$

**优点**：每步下降最多
**缺点**：计算代价高，需要解一维优化问题

**适用情况**：
- 一维优化问题容易求解
- 二次函数（有闭式解）

### 2.2 Armijo线搜索（回溯线搜索）

**Armijo条件**：
$$f(x_k + t d_k) \leq f(x_k) + \alpha t \nabla f(x_k)^T d_k$$

其中 α ∈ (0, 0.5)，通常取 α = 0.01 或 0.1。

**算法**：
```
给定 α ∈ (0, 0.5), β ∈ (0, 1), t = 1
while f(x_k + t d_k) > f(x_k) + α t ∇f(x_k)^T d_k:
    t = β * t
返回 t
```

**参数选择**：
- α 控制下降量
- β 控制步长缩减速度，通常取 β = 0.5 或 0.8

**保证**：对Lipschitz连续梯度，算法在有限步内终止。

### 2.3 Goldstein条件

**Goldstein条件**：
$$f(x_k) + (1-\alpha) t \nabla f(x_k)^T d_k \leq f(x_k + t d_k) \leq f(x_k) + \alpha t \nabla f(x_k)^T d_k$$

**优点**：避免步长过小
**缺点**：第一不等式可能将最优步长排除在外

### 2.4 Wolfe条件

**Wolfe条件**：
1. **充分下降条件**：
   $$f(x_k + t d_k) \leq f(x_k) + \alpha_1 t \nabla f(x_k)^T d_k$$

2. **曲率条件**：
   $$\nabla f(x_k + t d_k)^T d_k \geq \alpha_2 \nabla f(x_k)^T d_k$$

其中 0 < α₁ < α₂ < 1，通常 α₁ = 0.01, α₂ = 0.9。

**强Wolfe条件**（更常用）：
$$|\nabla f(x_k + t d_k)^T d_k| \leq \alpha_2 |\nabla f(x_k)^T d_k|$$

**保证**：对Lipschitz连续梯度，存在满足Wolfe条件的步长。

### 2.5 固定步长

**方法**：t_k = t（常数）

**收敛条件**：对 L-光滑凸函数，若 t < 2/L，则收敛。

**最优固定步长**：t = 1/L

**优点**：简单
**缺点**：需要知道Lipschitz常数，收敛慢

## 3. 收敛性分析

### 3.1 凸函数的收敛性

**定理**：设 f 为凸函数，∇f 为 L-Lipschitz 连续，使用固定步长 t = 1/L，则：
$$f(x_k) - f(x^*) \leq \frac{\|x_0 - x^*\|^2}{2 k} = O\left(\frac{1}{k}\right)$$

**证明**：
由 L-光滑性：
$$f(x_{k+1}) \leq f(x_k) + \nabla f(x_k)^T (x_{k+1} - x_k) + \frac{L}{2} \|x_{k+1} - x_k\|^2$$
$$= f(x_k) - t \|\nabla f(x_k)\|^2 + \frac{L t^2}{2} \|\nabla f(x_k)\|^2$$

取 t = 1/L：
$$f(x_{k+1}) \leq f(x_k) - \frac{1}{2L} \|\nabla f(x_k)\|^2$$

由凸性：
$$f(x_k) \leq f(x^*) + \nabla f(x_k)^T (x_k - x^*)$$

结合并求和，可得收敛速度 O(1/k)。

### 3.2 强凸函数的收敛性

**定理**：设 f 为 μ-强凸函数，∇f 为 L-Lipschitz 连续，使用固定步长 t = 1/L，则：
$$\|x_k - x^*\|^2 \leq \left(1 - \frac{\mu}{L}\right)^k \|x_0 - x^*\|^2$$

即**线性收敛**，收敛速度为：
$$O\left(\left(1 - \frac{1}{\kappa}\right)^k\right)$$

其中 κ = L/μ 为条件数。

**几何解释**：
- κ 小：条件好，收敛快
- κ 大：条件差，收敛慢
- 极端：κ → ∞（接近退化），收敛极慢

### 3.3 迭代次数估计

**定理**：为达到精度 ε，需要迭代次数：
- **凸函数**：k = O(1/ε)
- **强凸函数**：k = O(κ log(1/ε))

### 3.5 二次函数的完整例子

考虑二维二次函数
$$f(x,y)=\frac{1}{2}(x^2+4y^2)$$

则梯度为
$$\nabla f(x,y)=(x,4y)$$

使用固定步长 $t=\frac{1}{4}$ 时，更新式变为
$$x_{k+1}=(1-t)x_k=\frac{3}{4}x_k$$
$$y_{k+1}=(1-4t)y_k=0$$

所以只要第一步之后，$y$ 分量就被直接消掉，而 $x$ 分量按几何级数衰减。

如果把步长改成 $t=1$，则
$$x_{k+1}=0, \qquad y_{k+1}=-3y_k$$

这会导致 $y$ 方向发散，说明步长过大时梯度下降会失稳。

**启示**：步长不是“越大越快”，而是要落在稳定区间内。

### 3.4 下界与最优性

**定理**（Nesterov）：一阶方法的最优收敛速度：
- **凸函数**：O(1/k²)（可以改进！）
- **强凸函数**：O((1 - 1/√κ)^k)（可以改进！）

**启示**：梯度下降法在凸函数上不是最优的！

## 4. 加速方法

### 4.1 动量法（Momentum）

**思想**：利用历史梯度信息，增加"惯性"。

**算法**：
```
初始化 x_0, v_0 = 0
for k = 0, 1, 2, ...
    v_{k+1} = β v_k - α ∇f(x_k)
    x_{k+1} = x_k + v_{k+1}
```

**参数**：
- α：学习率
- β：动量系数，通常取 0.9

**物理类比**：小球滚下山坡，带有惯性。

**收敛速度**：对强凸函数，适当选择参数可加速到 O((1 - 1/√κ)^k)。

### 4.2 Nesterov加速梯度法

**思想**：在"预测位置"计算梯度。

**算法**：
```
初始化 x_0, y_0 = x_0
for k = 0, 1, 2, ...
    x_{k+1} = y_k - α ∇f(y_k)
    y_{k+1} = x_{k+1} + \frac{k}{k+3} (x_{k+1} - x_k)
```

**收敛速度**：对凸函数，f(x_k) - f(x*) = O(1/k²)，达到最优！

**证明思路**：构造"估计序列"，利用凸性。

### 4.3 NAG的另一种形式

**算法**：
```
v_{k+1} = β v_k + α ∇f(x_k - β v_k)
x_{k+1} = x_k - v_{k+1}
```

**解释**：先"预测"到 x_k - βv_k，再计算梯度。

### 4.4 加速收敛速度对比

| 方法 | 凸函数 | 强凸函数 |
|------|--------|----------|
| 梯度下降 | O(1/k) | O((1-1/κ)^k) |
| 动量法 | O(1/k) | O((1-1/√κ)^k) |
| Nesterov | O(1/k²) | O((1-1/√κ)^k) |

**结论**：Nesterov加速在凸函数上达到最优收敛速度！

## 5. 随机梯度下降

### 5.1 动机

**问题**：大规模数据集中，计算 ∇f(x) 需要遍历所有数据，代价高。

**解决**：用单个或少量样本估计梯度。

### 5.2 随机梯度下降（SGD）

**设定**：f(x) = (1/n) Σfᵢ(x)

**算法**：
```
for k = 0, 1, 2, ...
    随机选择 i_k ∈ {1, ..., n}
    x_{k+1} = x_k - α_k ∇f_{i_k}(x_k)
```

**性质**：E[∇fᵢₖ(x_k)] = ∇f(x_k)（无偏估计）

### 5.3 收敛性

**定理**：对强凸函数，若 α_k = O(1/k)，则：
$$E[\|x_k - x^*\|^2] = O\left(\frac{1}{k}\right)$$

**对比**：
- 全梯度下降：O((1-1/κ)^k)（线性收敛）
- SGD：O(1/k)（次线性收敛）

**为什么用SGD？**

## 练习（分层）

### A档（熟练）

1. 对二次函数 $f(x)=\frac{1}{2}x^TAx-b^Tx$（$A\succ 0$），写出梯度下降迭代式。
2. 证明/说明：当步长 $t<2/L$ 时（$L$-光滑），函数值单调下降的直觉。

### B档（辨析）

1. 给出一个例子说明：盲用“精确线搜索”不一定意味着最快整体收敛。
2. 解释：为什么条件数大时等高线狭长会导致“之”字形？

### C档（证明/推导）

1. 在强凸光滑条件下，推导 $\|x_k-x^*\|$ 的线性收敛率（写主线即可）。

## 自测（3问速测）

1. 我能说清 $L$（光滑）与 $\mu$（强凸）分别控制什么吗？
2. 我能稳定写出 Armijo 条件并解释每个参数的作用吗？
3. 我能解释 Nesterov 为什么能达到 $O(1/k^2)$ 的直觉吗？
- 每次迭代代价低（O(1) vs O(n)）
- 适合大规模数据
- 可以跳出局部最优（非凸情形）

### 5.4 Mini-batch SGD

**算法**：
```
for k = 0, 1, 2, ...
    随机选择小批量 B_k ⊂ {1, ..., n}, |B_k| = b
    x_{k+1} = x_k - α_k * (1/b) Σ_{i∈B_k} ∇f_i(x_k)
```

**优点**：
- 方差减小（batch size 大）
- 并行计算加速
- 平衡计算效率和收敛速度

### 5.5 学习率调度

**常用策略**：
1. **固定步长**：α_k = α
2. **步长衰减**：α_k = α₀/(1 + γk)
3. **指数衰减**：α_k = α₀ γ^k
4. **余弦退火**：α_k = α_min + (α_max - α_min)(1 + cos(πk/T))/2

**实践建议**：
- 开始用较大学习率快速下降
- 后期减小学习率精细调整
- 配合学习率预热（warmup）

## 6. 自适应学习率方法

### 6.1 AdaGrad

**思想**：对每个参数自适应调整学习率。

**算法**：
```
初始化 x_0, r_0 = 0
for k = 0, 1, 2, ...
    g_k = ∇f(x_k)
    r_{k+1} = r_k + g_k ⊙ g_k  (逐元素平方和)
    x_{k+1} = x_k - α / (ε + √r_{k+1}}) ⊙ g_k
```

**特点**：
- 频繁更新的参数：学习率减小
- 稀疏更新的参数：学习率保持较大

**问题**：r 单调递增，学习率持续减小，可能过早停止。

### 6.2 RMSprop

**思想**：用指数移动平均代替累积和。

**算法**：
```
r_{k+1} = ρ r_k + (1-ρ) g_k ⊙ g_k
x_{k+1} = x_k - α / (ε + √r_{k+1}}) ⊙ g_k
```

**参数**：ρ 通常取 0.9 或 0.99

**优点**：避免学习率单调递减。

### 6.3 Adam

**结合动量和自适应学习率**。

**算法**：
```
初始化 x_0, m_0 = 0, v_0 = 0
for k = 0, 1, 2, ...
    g_k = ∇f(x_k)
    m_{k+1} = β_1 m_k + (1-β_1) g_k          # 一阶矩估计
    v_{k+1} = β_2 v_k + (1-β_2) g_k ⊙ g_k   # 二阶矩估计
    
    # 偏差修正
    m̂_{k+1} = m_{k+1} / (1 - β_1^{k+1})
    v̂_{k+1} = v_{k+1} / (1 - β_2^{k+1})
    
    x_{k+1} = x_k - α m̂_{k+1} / (ε + √v̂_{k+1}})
```

**参数**：
- α = 0.001（学习率）
- β₁ = 0.9（一阶矩衰减率）
- β₂ = 0.999（二阶矩衰减率）
- ε = 10⁻⁸（数值稳定）

**优点**：
- 结合动量和自适应学习率
- 偏差修正使初始迭代更稳定
- 适合稀疏梯度
- 深度学习中最常用

### 6.4 AdamW

**问题**：Adam 的权重衰减实现有误。

**修正**：将权重衰减与梯度更新分离：
$$x_{k+1} = x_k - α m̂_{k+1} / (ε + √v̂_{k+1}}) - α λ x_k$$

其中 λ 为权重衰减系数。

**实践**：AdamW 在训练 Transformer 等大模型时效果更好。

## 7. 收敛加速技巧

### 7.1 特征缩放

**问题**：不同特征尺度差异大时，条件数 κ 大，收敛慢。

**解决**：
- 标准化：x' = (x - μ)/σ
- 归一化：x' = (x - min)/(max - min)

**效果**：减小条件数，加速收敛。

### 7.2 预处理

**思想**：用预条件矩阵代替单位矩阵。

**算法**：
$$x_{k+1} = x_k - α_k P^{-1} \nabla f(x_k)$$

**选择 P**：
- P ≈ ∇²f(x)（近似Hessian）
- 对角预处理：P = diag(∇²f(x))
- 牛顿法：P = ∇²f(x)

**效果**：相当于在变换后的坐标系中做梯度下降。

### 7.3 批量归一化（Batch Normalization）

**方法**：在神经网络的每层输出进行归一化。

$$\hat{x} = \frac{x - \mu_B}{\sqrt{\sigma_B^2 + ε}}, \quad y = γ \hat{x} + β$$

**效果**：
- 减小内部协变量偏移
- 允许使用更大学习率
- 加速收敛

### 7.4 梯度裁剪

**问题**：梯度爆炸导致训练不稳定。

**方法**：
$$\nabla f(x) \leftarrow \begin{cases}
\nabla f(x), & \|\nabla f(x)\| \leq c \\
\frac{c \nabla f(x)}{\|\nabla f(x)\|}, & \|\nabla f(x)\| > c
\end{cases}$$

**应用**：RNN、Transformer 训练中常用。

## 8. 实践指南

### 8.1 学习率选择

**经验规则**：
1. 从小学习率开始，逐步增大
2. 观察损失曲线：
   - 损失震荡：学习率过大
   - 损失下降缓慢：学习率过小
3. 使用学习率调度

**推荐范围**：
- SGD：0.01 ~ 0.1
- Adam：0.0001 ~ 0.001
- 带动量的SGD：0.01 ~ 0.1

### 8.2 超参数调试顺序

1. **学习率**：最重要
2. **动量系数**：通常 0.9
3. **批量大小**：权衡计算效率和收敛
4. **权重衰减**：防止过拟合
5. **其他超参数**

### 8.3 调试技巧

**诊断工具**：
1. **损失曲线**：监控训练过程
2. **梯度范数**：检测梯度消失/爆炸
3. **参数统计**：检查参数分布
4. **可视化**：理解优化过程

**常见问题**：
- 损失不下降：检查学习率、梯度
- 损失震荡：减小学习率
- 过拟合：增加正则化
- 欠拟合：增加模型容量

## 9. 数值实验

### 9.1 二次函数优化

```python
import numpy as np
import matplotlib.pyplot as plt

# 定义二次函数 f(x) = 0.5 * x^T A x - b^T x
A = np.array([[10, 3], [3, 1]])  # 条件数较大
b = np.array([0, 0])
x_star = np.linalg.solve(A, b)  # 最优解

def f(x):
    return 0.5 * x @ A @ x - b @ x

def grad_f(x):
    return A @ x - b

# 梯度下降
def gradient_descent(x0, lr=0.01, n_iter=100):
    x = x0.copy()
    trajectory = [x.copy()]
    for _ in range(n_iter):
        x = x - lr * grad_f(x)
        trajectory.append(x.copy())
    return np.array(trajectory)

# 实验
x0 = np.array([2.0, 2.0])
traj = gradient_descent(x0, lr=0.04, n_iter=50)

# 绘制等高线和轨迹
x1, x2 = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
Z = np.array([[f(np.array([x1[i,j], x2[i,j]])) for j in range(100)] for i in range(100)])

plt.contour(x1, x2, Z, levels=20)
plt.plot(traj[:, 0], traj[:, 1], 'r.-', linewidth=2)
plt.plot(x_star[0], x_star[1], 'g*', markersize=15)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Gradient Descent Trajectory')
plt.show()
```

### 9.2 收敛速度比较

```python
# 比较梯度下降、动量法、Nesterov加速
def momentum(x0, lr=0.01, beta=0.9, n_iter=100):
    x = x0.copy()
    v = np.zeros_like(x)
    trajectory = [x.copy()]
    for _ in range(n_iter):
        v = beta * v - lr * grad_f(x)
        x = x + v
        trajectory.append(x.copy())
    return np.array(trajectory)

def nesterov(x0, lr=0.01, beta=0.9, n_iter=100):
    x = x0.copy()
    v = np.zeros_like(x)
    trajectory = [x.copy()]
    for _ in range(n_iter):
        y = x + beta * v
        v = beta * v - lr * grad_f(y)
        x = x + v
        trajectory.append(x.copy())
    return np.array(trajectory)

# 实验
traj_gd = gradient_descent(x0, lr=0.04, n_iter=100)
traj_momentum = momentum(x0, lr=0.04, beta=0.9, n_iter=100)
traj_nesterov = nesterov(x0, lr=0.04, beta=0.9, n_iter=100)

# 绘制收敛曲线
plt.figure(figsize=(10, 6))
plt.plot([f(x) for x in traj_gd], label='GD')
plt.plot([f(x) for x in traj_momentum], label='Momentum')
plt.plot([f(x) for x in traj_nesterov], label='Nesterov')
plt.yscale('log')
plt.xlabel('Iteration')
plt.ylabel('Function Value (log scale)')
plt.legend()
plt.title('Convergence Comparison')
plt.show()
```

## 10. 小结

### 10.1 核心算法

| 算法 | 步长选择 | 收敛速度 | 适用场景 |
|------|----------|----------|----------|
| GD | 精确/回溯 | O(1/k) | 小规模凸优化 |
| SGD | 衰减 | O(1/k) | 大规模机器学习 |
| Momentum | 固定/自适应 | 加速 | 深度学习 |
| Adam | 自适应 | O(1/√k) | 深度学习首选 |

### 10.2 关键技术

- **线搜索**：Armijo、Wolfe条件
- **加速**：动量、Nesterov
- **自适应**：AdaGrad、Adam
- **预处理**：特征缩放、BatchNorm

### 10.3 实践要点

1. **学习率**：最重要的超参数
2. **批量大小**：权衡效率与收敛
3. **监控**：损失曲线、梯度范数
4. **正则化**：防止过拟合

---

**参考文献**：
1. 《Convex Optimization》- Stephen Boyd
2. 《Numerical Optimization》- Nocedal & Wright
3. 《Optimization for Machine Learning》- Sra, Nowozin, Wright

**下一章**：[[07_Newton_Method]] - 牛顿法与拟牛顿法
