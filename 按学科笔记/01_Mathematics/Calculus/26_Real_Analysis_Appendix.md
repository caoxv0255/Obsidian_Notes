---
type: appendix
topic: real_analysis
category: calculus
difficulty: advanced
prerequisites:
    - [[01_Real_Numbers]]
    - [[10_Definite_Integrals]]
    - [[12_Improper_Integrals]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-04-01
status: complete
subject: calculus
chapter: 26
updated: 2026-04-27
---

# 附录：实分析初步 (Introduction to Real Analysis)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解为什么需要 Lebesgue 积分以及它比 Riemann 积分更强的地方
- 掌握测度、可测函数和 Lebesgue 积分的基本概念
- 了解单调收敛定理、Fatou 引理和支配收敛定理的作用

## 先修
- [[01_Real_Numbers]] - 实数与完备性
- [[10_Definite_Integrals]] - 定积分
- [[12_Improper_Integrals]] - 反常积分
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：测度、可测函数与简单函数积分
- B档（进阶）：Lebesgue 积分、单调收敛和 Fatou 引理
- C档（挑战）：支配收敛定理、$L^p$ 空间与极限定理

## 自测（3问速测）
1. 为什么 Dirichlet 函数不是 Riemann 可积，但却是 Lebesgue 可积？
2. 单调收敛定理和支配收敛定理各适合什么场景？
3. 什么是零测集，它为什么重要？

## 高数/数分附件补充

### 高数到数分的过渡
- 高数关注“怎么算”，数分关注“为什么能算”
- Riemann 积分处理“规则图形”，Lebesgue 积分处理“更坏的集合与更强的极限交换”

### 典型例题（Dirichlet 函数）
定义
$$
D(x)=\chi_{\mathbb{Q}}(x)=
\begin{cases}
1, & x\in\mathbb{Q}\\
0, & x\notin\mathbb{Q}
\end{cases}
$$
在 $[0,1]$ 上，$D$ 不是 Riemann 可积的，因为它在每一点都不连续。

但从 Lebesgue 观点看，$\mathbb{Q}$ 是零测集，因此
$$
\int_{[0,1]} D(x)\,dx=0
$$

**意义**：这正是数分中“积分先看集合结构，再看函数值”的核心转折。

本附录为有志于深入学习数学分析或从事理论机器学习研究的读者准备，介绍实分析的核心概念，包括测度论基础和Lebesgue积分理论。

## 1. 为什么需要Lebesgue积分？

### 1.1 Riemann积分的局限性

**Riemann积分**虽然直观且实用，但在某些情况下存在不足：

**问题1：Dirichlet函数**

$$D(x) = \begin{cases} 1, & x \in \mathbb{Q} \\ 0, & x \notin \mathbb{Q} \end{cases}$$

这个函数在 $[0,1]$ 上处处不连续，Riemann积分不存在。但直观上，有理数集"很少"，函数"大部分"是0，积分"应该"是0。

**问题2：极限与积分交换**

对于函数列 $f_n(x)$，Riemann积分下：

$$\lim_{n \to \infty} \int_a^b f_n(x) dx = \int_a^b \lim_{n \to \infty} f_n(x) dx$$

不一定成立，需要很强的条件（如一致收敛）。

**问题3：完备性**

Riemann可积函数空间关于 $L^2$ 范数不完备，这在泛函分析中是个问题。

### 1.2 Lebesgue积分的优势

**优势1：更广泛的函数类**

Dirichlet函数是Lebesgue可积的，积分为0。

**优势2：更好的极限定理**

在更弱的条件下，极限与积分可以交换。

**优势3：函数空间完备性**

$L^p$ 空间是完备的Banach空间。

## 2. 测度论基础

### 2.1 集合的长度/面积/体积

**直观理解**：
- 区间 $[a, b]$ 的长度：$b - a$
- 矩形 $[a, b] \times [c, d]$ 的面积：$(b-a)(d-c)$
- 可数个不相交区间的并的长度：各区间长度之和

**目标**：将"长度/面积/体积"的概念推广到更一般的集合。

### 2.2 σ-代数

**定义**：设 $X$ 是一个集合，$\mathcal{A}$ 是 $X$ 的子集族。如果 $\mathcal{A}$ 满足：

1. $X \in \mathcal{A}$
2. 若 $A \in \mathcal{A}$，则 $A^c \in \mathcal{A}$（对补集封闭）
3. 若 $A_n \in \mathcal{A}$（$n=1,2,...$），则 $\bigcup_{n=1}^{\infty} A_n \in \mathcal{A}$（对可数并封闭）

则称 $\mathcal{A}$ 为 $X$ 上的一个 **σ-代数**。

**性质**：
- $\emptyset \in \mathcal{A}$
- 若 $A_n \in \mathcal{A}$，则 $\bigcap_{n=1}^{\infty} A_n \in \mathcal{A}$
- 若 $A, B \in \mathcal{A}$，则 $A \setminus B \in \mathcal{A}$

**Borel σ-代数**：由 $\mathbb{R}$ 上所有开集生成的最小σ-代数，记为 $\mathcal{B}(\mathbb{R})$。

### 2.3 测度

**定义**：设 $(X, \mathcal{A})$ 是可测空间。映射 $\mu: \mathcal{A} \to [0, \infty]$ 称为**测度**，如果：

1. $\mu(\emptyset) = 0$
2. **可数可加性**：若 $A_n \in \mathcal{A}$ 两两不相交，则：
   $$\mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mu(A_n)$$

**Lebesgue测度**：在 $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ 上，存在唯一的测度 $m$，使得 $m([a,b]) = b-a$，称为Lebesgue测度。

**性质**：
1. **单调性**：若 $A \subset B$，则 $m(A) \leq m(B)$
2. **次可加性**：$m\left(\bigcup_{n=1}^{\infty} A_n\right) \leq \sum_{n=1}^{\infty} m(A_n)$
3. **平移不变性**：$m(A + x) = m(A)$
4. **完备性**：零测集的子集也是可测的

**零测集**：测度为0的集合。例如：
- 可数集（如 $\mathbb{Q}$）是零测集
- Cantor集是不可数的零测集

### 2.4 可测函数

**定义**：设 $(X, \mathcal{A})$ 是可测空间。函数 $f: X \to \mathbb{R}$ 称为**可测函数**，如果对任意开集 $U \subset \mathbb{R}$：

$$f^{-1}(U) \in \mathcal{A}$$

**等价定义**：$f$ 是可测的，当且仅当对任意 $a \in \mathbb{R}$：

$$\{x \in X : f(x) > a\} \in \mathcal{A}$$

**重要例子**：
- 连续函数是可测的
- 可测函数的和、差、积、商（分母不为0）是可测的
- 可测函数列的极限是可测的

## 3. Lebesgue积分

### 3.1 简单函数的积分

**简单函数**：只取有限个值的可测函数，可表示为：

$$s(x) = \sum_{i=1}^{n} a_i \chi_{A_i}(x)$$

其中 $\chi_{A_i}$ 是集合 $A_i$ 的特征函数：

$$\chi_{A_i}(x) = \begin{cases} 1, & x \in A_i \\ 0, & x \notin A_i \end{cases}$$

**积分定义**：

$$\int_X s \, d\mu = \sum_{i=1}^{n} a_i \mu(A_i)$$

### 3.2 非负可测函数的积分

**定义**：设 $f \geq 0$ 是可测函数。定义：

$$\int_X f \, d\mu = \sup\left\{\int_X s \, d\mu : 0 \leq s \leq f, s \text{ 是简单函数}\right\}$$

**单调收敛定理**：若 $0 \leq f_n \uparrow f$，则：

$$\int_X f \, d\mu = \lim_{n \to \infty} \int_X f_n \, d\mu$$

### 3.3 一般可测函数的积分

**定义**：设 $f$ 是可测函数。将 $f$ 分解为正部和负部：

$$f^+(x) = \max(f(x), 0), \quad f^-(x) = \max(-f(x), 0)$$

则 $f = f^+ - f^-$，定义：

$$\int_X f \, d\mu = \int_X f^+ \, d\mu - \int_X f^- \, d\mu$$

**可积**：如果 $\int_X |f| \, d\mu < \infty$，则称 $f$ 是Lebesgue可积的。

### 3.4 核心定理

**定理1：Fatou引理**

设 $f_n \geq 0$ 是可测函数列，则：

$$\int_X \liminf_{n \to \infty} f_n \, d\mu \leq \liminf_{n \to \infty} \int_X f_n \, d\mu$$

**定理2：单调收敛定理（Monotone Convergence Theorem）**

设 $0 \leq f_n \uparrow f$，则：

$$\int_X f \, d\mu = \lim_{n \to \infty} \int_X f_n \, d\mu$$

**定理3：控制收敛定理（Dominated Convergence Theorem）**

设 $f_n \to f$ a.e.，且存在可积函数 $g$ 使得 $|f_n| \leq g$ 对所有 $n$ 成立。则：

$$\int_X f \, d\mu = \lim_{n \to \infty} \int_X f_n \, d\mu$$

**这一定理是Lebesgue积分理论的核心！**

**定理4：Fubini定理**

设 $f(x, y)$ 是可积的，则：

$$\int_{X \times Y} f \, d(\mu \times \nu) = \int_X \left[\int_Y f(x, y) \, d\nu(y)\right] d\mu(x)$$

积分顺序可以交换。

## 4. $L^p$ 空间

### 4.1 定义

对于 $1 \leq p < \infty$，定义：

$$L^p(\mu) = \left\{f : \int_X |f|^p \, d\mu < \infty\right\}$$

范数：

$$\|f\|_p = \left(\int_X |f|^p \, d\mu\right)^{1/p}$$

对于 $p = \infty$：

$$L^\infty(\mu) = \left\{f : \text{ess sup}|f| < \infty\right\}$$

其中 $\text{ess sup}|f| = \inf\{M : |f| \leq M \text{ a.e.}\}$。

### 4.2 重要不等式

**Hölder不等式**：设 $1 < p, q < \infty$ 且 $\frac{1}{p} + \frac{1}{q} = 1$，则：

$$\int_X |fg| \, d\mu \leq \|f\|_p \cdot \|g\|_q$$

**Minkowski不等式**：对于 $1 \leq p \leq \infty$：

$$\|f + g\|_p \leq \|f\|_p + \|g\|_p$$

### 4.3 完备性

**Riesz-Fischer定理**：$L^p(\mu)$ 是完备的Banach空间。

**意义**：Cauchy序列在 $L^p$ 中收敛。这使得 $L^p$ 空间成为泛函分析和偏微分方程研究的理想框架。

## 5. 与Riemann积分的关系

### 5.1 等价性定理

**定理**：如果 $f$ 在 $[a,b]$ 上Riemann可积，则 $f$ Lebesgue可积，且：

$$\int_a^b f(x) dx = \int_{[a,b]} f \, dm$$

### 5.2 Riemann可积的充要条件

**定理**：$f$ 在 $[a,b]$ 上Riemann可积，当且仅当 $f$ 有界且不连续点集是零测集。

### 5.3 Lebesgue积分的推广

Lebesgue积分推广了Riemann积分：
- Riemann可积 $\Rightarrow$ Lebesgue可积
- 反之不成立（如Dirichlet函数）

## 6. 在机器学习中的应用

### 6.1 概率论的严格基础

**概率空间**：$(\Omega, \mathcal{F}, P)$，其中：
- $\Omega$ 是样本空间
- $\mathcal{F}$ 是σ-代数（事件域）
- $P$ 是概率测度

**随机变量**：可测函数 $X: \Omega \to \mathbb{R}$

**期望**：$E[X] = \int_\Omega X \, dP$

### 6.2 信息论

**熵**：$H(X) = -\sum_x p(x) \log p(x)$（离散）

**微分熵**：$h(X) = -\int f(x) \log f(x) dx$（连续）

这需要Lebesgue积分理论来严格处理。

### 6.3 核方法与再生核Hilbert空间

RKHS（Reproducing Kernel Hilbert Space）的理论基础是 $L^2$ 空间的完备性。

### 6.4 深度学习中的泛化理论

Rademacher复杂度、VC维等概念需要测度论语言。

## 1. 代码示例

```python
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# ============================================
# 示例1：Dirichlet函数的Lebesgue积分
# ============================================
def dirichlet_function():
    """
    Dirichlet函数：
    D(x) = 1 if x ∈ Q (有理数)
    D(x) = 0 if x ∉ Q (无理数)
    
    Lebesgue积分 = 0（因为有理数集是零测集）
    """
    print("="*50)
    print("示例1：Dirichlet函数")
    print("="*50)
    
    # 无法直接数值计算，但可以理解：
    # 有理数集Q的测度 = 0
    # 无理数集的测度 = 1（在[0,1]上）
    # 因此 Lebesgue积分 = 1×m(Q) + 0×m([0,1]\Q) = 0
    
    print("有理数集是零测集（可数集）")
    print("无理数集的测度 = 1（在[0,1]区间）")
    print("D(x) = 1×χ_Q + 0×χ_{[0,1]\\Q}")
    print("Lebesgue积分 = 1×m(Q) + 0×1 = 0")
    print()

# ============================================
# 示例2：控制收敛定理示例
# ============================================
def dominated_convergence_example():
    """
    示例：f_n(x) = n·x·exp(-nx) 在 [0,1]
    
    点态极限：f_n(x) → 0（对所有x）
    
    Riemann积分：∫₀¹ f_n(x)dx = 1 - (1+n)e^(-n) → 1
    这与点态极限不符！
    
    原因：不存在可积的控制函数
    """
    print("="*50)
    print("示例2：控制收敛定理")
    print("="*50)
    
    from scipy.integrate import quad
    
    # 定义函数列
    def f_n(x, n):
        return n * x * np.exp(-n * x) if x > 0 else 0
    
    # 计算不同n的积分
    n_values = [1, 5, 10, 20, 50, 100]
    integrals = []
    
    for n in n_values:
        result, _ = quad(lambda x: f_n(x, n), 0, 1)
        integrals.append(result)
        print(f"n = {n:3d}: ∫f_n = {result:.6f}")
    
    print(f"\n点态极限：f_n(x) → 0（对所有x）")
    print(f"积分极限：∫f_n → {integrals[-1]:.6f}")
    print(f"极限不相等！原因：不存在可积的控制函数")
    print()

# ============================================
# 示例3：单调收敛定理示例
# ============================================
def monotone_convergence_example():
    """
    示例：f_n(x) = n·χ_{(0,1/n)}(x) 在 [0,1]
    
    f_n ↑ ∞·χ_{(0)}（不是函数！）
    但 ∫f_n = 1 对所有n
    
    这说明单调收敛定理要求函数列收敛到函数
    """
    print("="*50)
    print("示例3：单调收敛定理")
    print("="*50)
    
    print("f_n(x) = n·χ_{(0,1/n)}(x)")
    print("f_n(x) → 0（点态收敛，除了x=0）")
    print("∫₀¹ f_n(x)dx = 1（对所有n）")
    print("∫₀¹ lim f_n(x)dx = 0")
    print("lim ∫f_n ≠ ∫lim f_n")
    print("原因：f_n不是单调递增的函数列")
    print()

# ============================================
# 示例4：L^p空间范数计算
# ============================================
def lp_norm_example():
    """
    计算不同p值的L^p范数
    """
    print("="*50)
    print("示例4：L^p空间范数")
    print("="*50)
    
    # 在[0,1]上，计算f(x)=x的L^p范数
    def f(x):
        return x
    
    p_values = [1, 2, 3, 5, 10, np.inf]
    
    for p in p_values:
        if p == np.inf:
            # L^∞范数 = ess sup|f|
            norm = np.max(f(np.linspace(0, 1, 1000)))
            print(f"L^∞范数 = {norm:.6f}")
        else:
            # L^p范数
            integrand = lambda x: abs(f(x))**p
            result, _ = quad(integrand, 0, 1)
            norm = result**(1/p)
            theoretical = (1/(p+1))**(1/p)
            print(f"L^{p}范数 = {norm:.6f} (理论值: {theoretical:.6f})")
    print()

# ============================================
# 示例5：Hölder不等式验证
# ============================================
def holder_inequality():
    """
    验证Hölder不等式：∫|fg| ≤ ||f||_p · ||g||_q
    """
    print("="*50)
    print("示例5：Hölder不等式")
    print("="*50)
    
    # 在[0,1]上
    def f(x):
        return x**0.5
    
    def g(x):
        return (1-x)**0.5
    
    # 选择p=2, q=2（Cauchy-Schwarz不等式）
    p, q = 2, 2
    
    # 计算∫|fg|
    integrand_fg = lambda x: abs(f(x) * g(x))
    integral_fg, _ = quad(integrand_fg, 0, 1)
    
    # 计算||f||_p
    integrand_f = lambda x: abs(f(x))**p
    norm_f = quad(integrand_f, 0, 1)[0]**(1/p)
    
    # 计算||g||_q
    integrand_g = lambda x: abs(g(x))**q
    norm_g = quad(integrand_g, 0, 1)[0]**(1/q)
    
    print(f"∫|fg| = {integral_fg:.6f}")
    print(f"||f||_{p} = {norm_f:.6f}")
    print(f"||g||_{q} = {norm_g:.6f}")
    print(f"||f||_{p}·||g||_{q} = {norm_f * norm_g:.6f}")
    print(f"验证：{integral_fg:.6f} ≤ {norm_f * norm_g:.6f} ✓")
    print()

# ============================================
# 示例6：测度可视化
# ============================================
def visualize_measures():
    """
    可视化不同集合的测度
    """
    print("="*50)
    print("示例6：测度可视化")
    print("="*50)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. 区间的测度
    ax = axes[0, 0]
    a, b = 0.2, 0.8
    ax.fill_between([a, b], 0, 1, alpha=0.3, color='blue')
    ax.axhline(y=0.5, color='r', linestyle='--')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f'区间 [{a}, {b}] 的测度 = {b-a:.2f}', fontsize=12)
    ax.set_xlabel('x')
    ax.grid(True, alpha=0.3)
    
    # 2. 可数集的测度
    ax = axes[0, 1]
    # 可数个点
    points = np.array([1/n for n in range(1, 20)])
    ax.scatter(points, np.zeros_like(points), s=100, c='red', zorder=5)
    ax.set_xlim(0, 1.1)
    ax.set_ylim(-0.1, 0.1)
    ax.set_title('可数集的测度 = 0', fontsize=12)
    ax.set_xlabel('x')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.5)
    
    # 3. Cantor集（示意）
    ax = axes[1, 0]
    # 绘制Cantor集的前几步
    def cantor_set(levels=5):
        intervals = [(0, 1)]
        for _ in range(levels):
            new_intervals = []
            for (a, b) in intervals:
                new_intervals.append((a, a + (b-a)/3))
                new_intervals.append((a + 2*(b-a)/3, b))
            intervals = new_intervals
        return intervals
    
    intervals = cantor_set(4)
    for i, (a, b) in enumerate(intervals):
        ax.fill_between([a, b], 0, 1, alpha=0.5, color='blue')
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(0, 1)
    ax.set_title('Cantor集的测度 = 0（不可数）', fontsize=12)
    ax.set_xlabel('x')
    ax.grid(True, alpha=0.3)
    
    # 4. 区间并集的测度
    ax = axes[1, 1]
    intervals = [(0.1, 0.3), (0.4, 0.5), (0.6, 0.9)]
    total_measure = sum(b-a for (a, b) in intervals)
    
    for i, (a, b) in enumerate(intervals):
        ax.fill_between([a, b], 0, 1, alpha=0.5, color=f'C{i}')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f'不相交区间并的测度 = {total_measure:.2f}', fontsize=12)
    ax.set_xlabel('x')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    print()

# ============================================
# 运行所有示例
# ============================================
if __name__ == "__main__":
    dirichlet_function()
    dominated_convergence_example()
    monotone_convergence_example()
    lp_norm_example()
    holder_inequality()
    visualize_measures()
```

## 8. 推荐学习路径

### 8.1 入门阶段

1. **理解动机**：为什么需要Lebesgue积分？
2. **掌握概念**：测度、可测函数、Lebesgue积分
3. **对比学习**：Riemann积分 vs Lebesgue积分

### 8.2 进阶阶段

1. **证明定理**：单调收敛定理、控制收敛定理、Fubini定理
2. **应用练习**：计算具体例子
3. **理论深化**：$L^p$ 空间、泛函分析初步

### 8.3 推荐教材

| 教材 | 特点 | 适合人群 |
|------|------|----------|
| Rudin《实分析与复分析》 | 简洁深刻 | 数学专业研究生 |
| Folland《Real Analysis》 | 现代观点 | 研究生、研究者 |
| Royden《Real Analysis》 | 经典教材 | 数学系学生 |
| 周民强《实变函数论》 | 中文经典 | 国内学生 |
| 程士宏《测度论与概率论基础》 | 概率视角 | 统计学学生 |

### 8.4 与机器学习的联系

| 实分析概念 | 机器学习应用 |
|-----------|-------------|
| 测度 | 概率分布、损失函数 |
| $L^p$ 空间 | 正则化、泛化理论 |
| 收敛定理 | 优化理论、极限行为 |
| Fubini定理 | 边缘分布、条件期望 |

## 习题

### 基础题

1. 证明：可数集是零测集。

2. 证明：Cantor集是不可数的零测集。

3. 设 $f_n(x) = n^2 x e^{-nx}$ 在 $[0,1]$ 上，验证：
   - 点态极限 $f_n \to 0$
   - $\int_0^1 f_n(x) dx$ 是否收敛？为什么？

### 进阶题

4. 证明Hölder不等式。

5. 验证 $L^p$ 空间的完备性（Riesz-Fischer定理）。

6. 举例说明：不存在可积的控制函数时，控制收敛定理不成立。

### 挑战题

7. 证明：有界函数 $f$ 在 $[a,b]$ 上Riemann可积，当且仅当 $f$ 的不连续点集是零测集。

8. 研究Rademacher函数列的极限行为，说明几乎处处收敛与 $L^p$ 收敛的区别。

## 相关链接

- [[01_Real_Numbers]] - 实数理论（测度论的基础）
- [[10_Definite_Integrals]] - 定积分（Riemann积分）
- [[12_Improper_Integrals]] - 反常积分（推广的积分）
- [[../../02_programming/04_python/02_Autograd]] - 自动微分（$L^2$ 空间的应用）

## 总结

实分析是现代数学的基石，为概率论、泛函分析、偏微分方程提供了严格的理论框架。对于机器学习研究者，掌握测度论和Lebesgue积分有助于：

1. **严格理解概率论**：概率空间、随机变量、期望的数学基础
2. **泛化理论研究**：Rademacher复杂度、VC维等高级概念
3. **优化理论**：收敛性分析、稳定性研究
4. **深度学习理论**：神经网络的表达能力、泛化界

虽然Lebesgue积分在日常机器学习实践中不直接使用，但其背后的思想——用更严谨的框架处理极限和收敛——对于理解高级算法和理论至关重要。



