---
type: note
subject: optimization
chapter: 09
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 09 - KKT条件

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层

- **基础**：定义与直接计算
- **进阶**：性质证明与综合应用
- **拓展**：跨章节联系与建模

## 自测（3问速测）

1. 本章最核心的定义是什么？
2. 本章一个关键结论的适用条件是什么？
3. 如何把本章方法应用到一个具体问题？

## 1. 约束优化问题

### 1.1 标准形式

**一般约束优化问题**：
$$\min_{x \in \mathbb{R}^n} f(x)$$
$$\text{s.t.} \quad g_i(x) \leq 0, \quad i = 1, \ldots, m$$
$$\quad\quad\; h_j(x) = 0, \quad j = 1, \ldots, p$$

**术语**：
- **目标函数**：f(x)
- **不等式约束**：gᵢ(x) ≤ 0
- **等式约束**：hⱼ(x) = 0
- **可行域**：满足所有约束的点的集合
- **最优解**：x* 使得 f(x*) = min{f(x) : x ∈ 可行域}

### 1.2 可行性与约束类型

**可行点**：满足所有约束的点 x

**约束的激活**：
- **激活约束**：在点 x 处 gᵢ(x) = 0
- **非激活约束**：在点 x 处 gᵢ(x) < 0
- **激活集**：A(x) = {i : gᵢ(x) = 0}

**注意**：等式约束总是激活的。

### 1.3 几何理解

**可行域的边界**：
- 不等式约束定义区域
- 等式约束定义曲面
- 可行域是这些约束的交集

**最优点的位置**：
- 可能在可行域内部（无约束情形）
- 可能在边界上（约束激活）
- 可能是角点（多个约束激活）

## 2. 拉格朗日乘子法

### 2.1 等式约束问题

**问题**：
$$\min_x f(x)$$
$$\text{s.t.} \quad h(x) = 0$$

**拉格朗日函数**：
$$L(x, \nu) = f(x) + \nu^T h(x)$$

**一阶必要条件**：
$$\nabla_x L(x^*, \nu^*) = \nabla f(x^*) + \nabla h(x^*) \nu^* = 0$$
$$h(x^*) = 0$$

### 2.2 几何解释

**等值面**：f(x) = c 的曲面

**约束曲面**：h(x) = 0

**最优性条件**：在最优解处，目标函数的等值面与约束曲面相切。

**数学表达**：
$$\nabla f(x^*) \perp T_{x^*}\{h(x) = 0\}$$

其中 T 是约束曲面的切空间。

**拉格朗日乘子的意义**：
$$\nabla f(x^*) = -\nu^* \nabla h(x^*)$$

ν* 是目标函数梯度在约束曲面法方向的分量。

### 2.3 多个等式约束

**问题**：
$$\min_x f(x)$$
$$\text{s.t.} \quad h_j(x) = 0, \quad j = 1, \ldots, p$$

**拉格朗日函数**：
$$L(x, \nu) = f(x) + \sum_{j=1}^{p} \nu_j h_j(x)$$

**条件**：
$$\nabla f(x^*) + \sum_{j=1}^{p} \nu_j^* \nabla h_j(x^*) = 0$$
$$h_j(x^*) = 0, \quad j = 1, \ldots, p$$

## 3. 不等式约束与KKT条件

### 3.1 只有一个不等式约束

**问题**：
$$\min_x f(x)$$
$$\text{s.t.} \quad g(x) \leq 0$$

**两种情况**：

**情况1：约束不激活** g(x*) < 0
- 等价于无约束问题
- ∇f(x*) = 0
- λ* = 0

**情况2：约束激活** g(x*) = 0
- 类似等式约束
- ∇f(x*) + λ*∇g(x*) = 0
- λ* ≥ 0（为什么？见下文）

### 3.2 KKT条件的推导

**拉格朗日函数**：
$$L(x, \lambda) = f(x) + \lambda g(x)$$

**互补松弛条件**：
$$\lambda g(x) = 0$$

保证：
- 若约束不激活（g(x) < 0），则 λ = 0
- 若约束激活（g(x) = 0），则 λ 可非零

### 3.3 λ ≥ 0 的几何意义

**最优解在边界**：g(x*) = 0

**可行性要求**：可行方向 d 满足 ∇g(x*)ᵀd ≤ 0

**下降方向**：∇f(x*)ᵀd < 0

**最优性**：可行方向都不是下降方向

**条件**：∇f(x*) 必须指向可行域外部

即：∇f(x*) 和 ∇g(x*) 方向相同，故 λ ≥ 0。

### 3.4 一般KKT条件

**问题**：
$$\min_x f(x)$$
$$\text{s.t.} \quad g_i(x) \leq 0, \quad i = 1, \ldots, m$$
$$\quad\quad\; h_j(x) = 0, \quad j = 1, \ldots, p$$

**拉格朗日函数**：
$$L(x, \lambda, \nu) = f(x) + \sum_{i=1}^{m} \lambda_i g_i(x) + \sum_{j=1}^{p} \nu_j h_j(x)$$

**KKT条件**：

1. **站点条件**（Stationarity）：
   $$\nabla f(x^*) + \sum_{i=1}^{m} \lambda_i^* \nabla g_i(x^*) + \sum_{j=1}^{p} \nu_j^* \nabla h_j(x^*) = 0$$

2. **原始可行性**（Primal feasibility）：
   $$g_i(x^*) \leq 0, \quad i = 1, \ldots, m$$
   $$h_j(x^*) = 0, \quad j = 1, \ldots, p$$

3. **对偶可行性**（Dual feasibility）：
   $$\lambda_i^* \geq 0, \quad i = 1, \ldots, m$$

4. **互补松弛条件**（Complementary slackness）：
   $$\lambda_i^* g_i(x^*) = 0, \quad i = 1, \ldots, m$$

## 4. KKT条件的性质

### 4.1 必要性与充分性

**定理**（一阶必要条件）：
若 x* 是局部最优解，且满足适当的约束规范条件，则存在 λ*, ν* 使得 KKT 条件成立。

**定理**（凸优化的充分性）：
若 f(x) 凸，gᵢ(x) 凸，hⱼ(x) 仿射，且 (x*, λ*, ν*) 满足 KKT 条件，则 x* 是全局最优解。

### 4.2 约束规范条件

**为什么需要约束规范？**

KKT 条件不是自动成立的，需要保证约束"足够规则"。

**常见约束规范**：

1. **线性独立约束规范（LICQ）**：
   激活约束的梯度线性独立。

2. **Slater条件**（凸优化）：
   存在严格可行点 x̃ 使得 gᵢ(x̃) < 0, hⱼ(x̃) = 0。

3. **Mangasarian-Fromovitz约束规范（MFCQ）**：
   存在方向 d 使得：
   - ∇gᵢ(x*)ᵀd < 0 对所有激活约束 i
   - ∇hⱼ(x*)ᵀd = 0 对所有等式约束 j

### 4.3 KKT条件的唯一性

**问题**：KKT 点唯一吗？

**答案**：不一定。

- 若约束规范成立，KKT 乘子唯一
- 若约束规范不成立，可能存在多个 KKT 点，或者没有 KKT 点

## 5. 实例分析

### 5.1 简单二次规划

**问题**：
$$\min_x \frac{1}{2} x^T Q x + c^T x$$
$$\text{s.t.} \quad Ax = b$$

**拉格朗日函数**：
$$L(x, \nu) = \frac{1}{2} x^T Q x + c^T x + \nu^T (Ax - b)$$

**KKT条件**：
$$\nabla_x L = Qx + c + A^T \nu = 0$$
$$Ax = b$$

**解**：
$$\begin{bmatrix} Q & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x \\ \nu \end{bmatrix} = \begin{bmatrix} -c \\ b \end{bmatrix}$$

### 5.2 带不等式约束的二次规划

**问题**：
$$\min_x \frac{1}{2} x^T Q x + c^T x$$
$$\text{s.t.} \quad Gx \preceq h$$

**KKT条件**：
$$Qx + c + G^T \lambda = 0$$
$$Gx \preceq h$$
$$\lambda \succeq 0$$
$$\lambda_i (Gx - h)_i = 0$$

**求解**：需要确定激活集，然后用等式约束方法求解。

### 5.3 支持向量机（SVM）

**原始问题**：
$$\min_{w,b} \frac{1}{2}\|w\|^2 + C \sum_{i=1}^{m} \xi_i$$
$$\text{s.t.} \quad y_i(w^T x_i + b) \geq 1 - \xi_i, \quad \xi_i \geq 0$$

**KKT条件**：
$$w = \sum_{i=1}^{m} \alpha_i y_i x_i$$
$$\sum_{i=1}^{m} \alpha_i y_i = 0$$
$$\alpha_i (y_i(w^T x_i + b) - 1 + \xi_i) = 0$$
$$(C - \alpha_i) \xi_i = 0$$
$$0 \leq \alpha_i \leq C$$

**支持向量**：αᵢ > 0 的样本点

### 5.4 拉格朗日对偶

**原始问题**：
$$p^* = \min_x \max_{\lambda \succeq 0, \nu} L(x, \lambda, \nu)$$

**对偶问题**：
$$d^* = \max_{\lambda \succeq 0, \nu} \min_x L(x, \lambda, \nu)$$

**弱对偶**：d* ≤ p*

**强对偶**：d* = p*（Slater条件下成立）

**对偶间隙**：p* - d*

## 6. 二阶条件

### 6.1 二阶必要条件

**定理**：若 x* 是局部最优解，且 LICQ 成立，则存在 λ*, ν* 满足 KKT 条件，且：
$$d^T \nabla^2_{xx} L(x^*, \lambda^*, \nu^*) d \geq 0$$

对所有满足以下条件的 d：
$$\nabla g_i(x^*)^T d = 0 \quad (\text{若} \lambda_i^* > 0)$$
$$\nabla g_i(x^*)^T d \leq 0 \quad (\text{若} \lambda_i^* = 0, g_i(x^*) = 0)$$
$$\nabla h_j(x^*)^T d = 0 \quad (\text{所有} j)$$

### 6.2 二阶充分条件

**定理**：若 (x*, λ*, ν*) 满足 KKT 条件，且：
$$d^T \nabla^2_{xx} L(x^*, \lambda^*, \nu^*) d > 0$$

对所有满足以下条件的非零 d：
$$\nabla g_i(x^*)^T d = 0 \quad (\text{若} g_i(x^*) = 0)$$
$$\nabla h_j(x^*)^T d = 0 \quad (\text{所有} j)$$

则 x* 是严格局部最优解。

## 7. 敏感性分析

### 7.1 扰动问题

**原始问题**：
$$\min_x f(x)$$
$$\text{s.t.} \quad g_i(x) \leq u_i$$
$$\quad\quad\; h_j(x) = v_j$$

**最优值函数**：p*(u, v) = min f(x) s.t. g(x) ≤ u, h(x) = v

### 7.2 拉格朗日乘子的意义

**定理**：若强对偶成立，且 (u, v) = (0, 0) 时对偶最优解唯一，则：
$$\frac{\partial p^*}{\partial u_i} = -\lambda_i^*$$
$$\frac{\partial p^*}{\partial v_j} = -\nu_j^*$$

**解释**：
- λᵢ* 是第 i 个不等式约束的"价格"
- νⱼ* 是第 j 个等式约束的"价格"
- 放松约束可以降低最优值

### 7.3 应用

**资源分配**：
- 约束代表资源限制
- 拉格朗日乘子是资源的影子价格
- 决定哪些资源值得增加

## 8. 计算方法

### 8.1 求解KKT系统

**直接法**：
1. 确定激活集（需要枚举或迭代）
2. 求解等式约束问题

**迭代法**：
- 内点法
- 罚函数法
- 增广拉格朗日法

### 8.2 激活集方法

**思想**：猜测激活集，求解等式约束问题，验证并更新。

**算法**：
```
初始化激活集 W
while 未收敛:
    求解等式约束问题（用 W 中的约束）
    计算拉格朗日乘子
    if 所有乘子非负:
        收敛
    else:
        移除负乘子对应的约束
    检查是否有违反的约束:
        添加到激活集
```

## 9. 小结

### 9.1 核心内容

| 条件 | 内容 |
|------|------|
| 站点条件 | ∇L = 0 |
| 原始可行性 | g ≤ 0, h = 0 |
| 对偶可行性 | λ ≥ 0 |
| 互补松弛 | λᵢgᵢ = 0 |

### 9.2 关键定理

1. **必要性**：局部最优 + 约束规范 ⟹ KKT条件
2. **充分性**：凸优化 + KKT条件 ⟹ 全局最优
3. **强对偶**：Slater条件 ⟹ 强对偶成立

### 9.3 应用

- 约束优化求解
- 敏感性分析
- 对偶问题推导
- 机器学习模型（SVM、对数障碍法）

---

**参考文献**：
1. 《Convex Optimization》- Stephen Boyd
2. 《Numerical Optimization》- Nocedal & Wright
3. 《Nonlinear Programming》- Dimitri Bertsekas

**下一章**：[[10_Linear_Programming]] - 线性规划

