---
type: index
subject: optimization
created: 2026-04-03
updated: 2026-04-24
status: complete
---

# 优化理论 (Optimization Theory)

## 速查

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习进度

### 第一部分：凸集与凸函数（4章）
- [x] 01_Convex_Sets - 凸集
- [x] 02_Convex_Functions - 凸函数
- [x] 03_Conjugate_Functions - 共轭函数
- [x] 04_Convex_Optimization_Basics - 凸优化基础

### 第二部分：无约束优化（4章）
- [x] 05_Optimality_Conditions - 最优性条件
- [x] 06_Gradient_Methods - 梯度下降法
- [x] 07_Newton_Method - 牛顿法与拟牛顿法
- [x] 08_Conjugate_Gradient - 共轭梯度法

### 第三部分：约束优化（6章）
- [x] 09_KKT_Conditions - KKT条件
- [x] 10_Linear_Programming - 线性规划
- [x] 11_Duality_Theory - 对偶理论
- [x] 12_Penalty_Methods - 罚函数法
- [x] 13_Augmented_Lagrangian - 增广拉格朗日法
- [x] 14_Sequential_Quadratic - 序列二次规划

### 第四部分：凸优化专题（3章）
- [x] 15_Simplex_Method - 单纯形法
- [x] 16_Interior_Point - 内点法
- [x] 17_Semidefinite_Programming - 半定规划

### 第五部分：现代优化方法（3章）
- [x] 18_Stochastic_Optimization - 随机优化
- [x] 19_Distributed_Optimization - 分布式优化
- [x] 20_ML_Applications - 机器学习应用

## 模块概览

优化理论研究如何在可行域中寻找目标函数的最优值，是应用数学的重要分支，在工程、经济、机器学习等领域有广泛应用。本笔记基于以下经典教材编写：

- **《Convex Optimization》** - Stephen Boyd & Lieven Vandenberghe
- **《Numerical Optimization》** - Jorge Nocedal & Stephen Wright
- **《凸分析》** - 史树中
- **《Convex Analysis》** - R. Tyrrell Rockafellar

## 学习路径

1. **凸集与凸函数** - 理解凸优化的几何与代数基础
2. **无约束优化** - 掌握梯度法和牛顿法
3. **约束优化** - 理解KKT条件和对偶理论
4. **凸优化专题** - 深入学习经典凸优化算法
5. **现代优化方法** - 了解随机优化和分布式优化
6. **机器学习应用** - 将理论应用于实际问题

## 已完成笔记

### 第一部分：凸集与凸函数
- [[01_Convex_Sets]] - 凸集（仿射集、凸集定义、凸锥、分离超平面定理、对偶锥）
- [[02_Convex_Functions]] - 凸函数（一阶条件、二阶条件、Jensen不等式、保凸运算、共轭函数）
- [x] [[03_Conjugate_Functions]] - 共轭函数
- [x] [[04_Convex_Optimization_Basics]] - 凸优化基础

### 第二部分：无约束优化
- [[05_Optimality_Conditions]] - 最优性条件（一阶必要条件、二阶条件、凸函数最优性）
- [[06_Gradient_Methods]] - 梯度下降法（步长策略、收敛性分析、SGD、Adam）
- [x] [[07_Newton_Method]] - 牛顿法与拟牛顿法
- [x] [[08_Conjugate_Gradient]] - 共轭梯度法

### 第三部分：约束优化
- [[09_KKT_Conditions]] - KKT条件（拉格朗日乘子法、互补松弛条件、敏感性分析）
- [[10_Linear_Programming]] - 线性规划（单纯形法、对偶理论、敏感性分析）
- [x] [[11_Duality_Theory]] - 对偶理论
- [x] [[12_Penalty_Methods]] - 罚函数法
- [x] [[13_Augmented_Lagrangian]] - 增广拉格朗日法
- [x] [[14_Sequential_Quadratic]] - 序列二次规划

### 第四部分：凸优化专题
- [x] [[15_Simplex_Method]] - 单纯形法
- [[16_Interior_Point]] - 内点法（中心路径、原始-对偶方法、Mehrotra方法）
- [x] [[17_Semidefinite_Programming]] - 半定规划

### 第五部分：现代优化方法
- [x] [[18_Stochastic_Optimization]] - 随机优化
- [x] [[19_Distributed_Optimization]] - 分布式优化
- [x] [[20_ML_Applications]] - 机器学习应用

## 核心知识图谱

```
凸集 → 分离超平面定理
    ↓
凸函数 → 一阶条件、二阶条件
    ↓
凸优化问题 → 强对偶性
    ↓
最优性条件（KKT）
    ↓
    ├─ 无约束优化：梯度法、牛顿法
    │       ↓
    │   共轭梯度法、拟牛顿法
    │
    └─ 约束优化：线性规划、对偶理论
            ↓
        罚函数法、增广拉格朗日法
            ↓
        内点法、半定规划
            ↓
        随机优化、分布式优化
```

## 重要定理与条件

### 凸性判定
- **一阶条件**：f(y) ≥ f(x) + ∇f(x)ᵀ(y-x)
- **二阶条件**：∇²f(x) ≽ 0（半正定）

### 最优性条件
- **无约束**：∇f(x*) = 0
- **约束优化（KKT）**：
  - 可行性：g(x*) ≤ 0, h(x*) = 0
  - 站点条件：∇f(x*) + λ∇g(x*) + ν∇h(x*) = 0
  - 互补松弛：λᵢgᵢ(x*) = 0, λ ≥ 0

### 对偶理论
- **弱对偶**：d* ≤ p*
- **强对偶**：d* = p*（Slater条件下）
- **对偶间隙**：p* - d*

## 经典算法收敛性

| 算法 | 收敛速度 | 适用问题 |
|------|----------|----------|
| 梯度下降 | O(1/k) | 凸函数 |
| 牛顿法 | 二次收敛 | 强凸函数 |
| 共轭梯度 | O(1/k²) | 二次函数 |
| 内点法 | 多项式时间 | 线性规划、凸优化 |

## 应用领域

### 机器学习
- **线性回归**：min ‖Ax - b‖²
- **逻辑回归**：min -Σ[yᵢlog(pᵢ) + (1-yᵢ)log(1-pᵢ)]
- **SVM**：min ‖w‖² + CΣξᵢ, s.t. yᵢ(wᵀxᵢ+b) ≥ 1-ξᵢ
- **神经网络**：min L(θ)（非凸优化）

### 信号处理
- **压缩感知**：min ‖x‖₁, s.t. Ax = b
- **去噪**：min ‖x - y‖² + λ‖x‖₁

### 金融工程
- **投资组合**：min wᵀΣw, s.t. wᵀμ ≥ r, 1ᵀw = 1
- **风险对冲**：min VaR, CVaR

### 控制理论
- **模型预测控制**：滚动优化
- **最优控制**：Pontryagin最大值原理

## 凸优化标准形式

**原问题**：
$$\min_x f_0(x)$$
$$\text{s.t.} \quad f_i(x) \leq 0, \quad i = 1, \ldots, m$$
$$\quad\quad\quad h_j(x) = 0, \quad j = 1, \ldots, p$$

**对偶问题**：
$$\max_{\lambda, \nu} g(\lambda, \nu)$$
$$\text{s.t.} \quad \lambda \geq 0$$

其中拉格朗日函数：
$$L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^{m} \lambda_i f_i(x) + \sum_{j=1}^{p} \nu_j h_j(x)$$

对偶函数：
$$g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$$

## 学习建议

### 理论学习
1. **先理解几何直观**：凸集、凸函数的几何意义
2. **掌握判定条件**：学会判断凸集和凸函数
3. **理解对偶理论**：对偶是优化理论的核心
4. **重视最优性条件**：KKT条件是约束优化的基础

### 算法实现
1. **从简单问题开始**：先实现一维优化
2. **理解收敛性**：知道算法何时收敛、收敛速度
3. **调试技巧**：学习如何调试优化算法
4. **实际应用**：在真实问题上验证算法

### 工具使用
- **CVX（MATLAB）**：凸优化建模工具
- **CVXPY（Python）**：Python凸优化库
- **Gurobi/CPLEX**：商业求解器
- **SCS**：分裂锥求解器

## 与其他数学分支的关系

```
线性代数
    ↓
凸分析 ←→ 实分析
    ↓         ↓
优化理论 ←→ 变分法
    ↓
数值分析
    ↓
机器学习、控制论、运筹学
```

## 经典问题分类

| 问题类型 | 目标函数 | 约束 | 求解方法 |
|----------|----------|------|----------|
| 无约束优化 | 一般 | 无 | 梯度法、牛顿法 |
| 线性规划 | 线性 | 线性 | 单纯形法、内点法 |
| 二次规划 | 二次 | 线性 | 有效集法、内点法 |
| 凸优化 | 凸 | 凸 | 内点法、梯度法 |
| 非凸优化 | 一般 | 一般 | 全局优化、启发式 |

## 相关链接

- [[00_Calculus_Index|微积分]] - 导数和梯度计算
- [[00_Linear_Algebra_Index|线性代数]] - 矩阵运算和特征值
- [[00_Probability_Index|概率统计]] - 随机优化和统计学习
- [[../00_Index|主索引]]

---

**创建时间：2026年4月3日**
**最后更新：2026年4月24日**
**总笔记数：20章（已完成）**
**完成状态：20/20（100%）**

**已完成章节**：
- 凸集与凸函数：4章
- 无约束优化：4章
- 约束优化：6章
- 凸优化专题：3章
- 现代优化方法：3章
