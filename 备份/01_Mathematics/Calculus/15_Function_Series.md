---
type: concept
topic: function_series
category: calculus
difficulty: advanced
prerequisites:
    - [[14_Series]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-03-09
updated: 2026-04-24
status: complete
---
# 函数项级数 (Function Series)

## 学习目标
- 理解函数项级数、收敛域与和函数的基本概念
- 掌握一致收敛与逐点收敛的区别及常用判别法
- 会用一致收敛处理逐项积分、逐项求导和函数逼近问题

## 先修
- [[14_Series]] - 级数
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：函数项级数、收敛域与点收敛
- B档（进阶）：一致收敛、M判别法与逐项积分
- C档（挑战）：逐项求导、幂级数性质与函数逼近

## 自测（3问速测）
1. 点收敛和一致收敛的区别是什么？
2. 为什么一致收敛能保证极限函数连续？
3. 逐项求导为什么需要比逐项积分更强的条件？

## 1. 定义

函数项级数是由函数序列构成的级数 $\sum_{n=1}^{\infty} u_n(x)$，其中每一项 $u_n(x)$ 都是定义在某个集合上的函数。

## 2. 定理与性质

### 1. 函数项级数的收敛性

#### 点收敛

**定义**：函数项级数 $\sum_{n=1}^{\infty} u_n(x)$ 在点 $x_0$ 处收敛，如果数项级数 $\sum_{n=1}^{\infty} u_n(x_0)$ 收敛。

#### 收敛域

函数项级数 $\sum_{n=1}^{\infty} u_n(x)$ 的收敛域是所有使级数收敛的点 $x$ 的集合。

### 2. 一致收敛

#### 定义

函数项级数 $\sum_{n=1}^{\infty} u_n(x)$ 在集合 $E$ 上一致收敛，如果其部分和序列 $S_n(x) = \sum_{k=1}^{n} u_k(x)$ 在 $E$ 上一致收敛。

**等价定义**：对于任意 $\varepsilon > 0$，存在 $N$，使得对所有 $n > N$ 和所有 $x \in E$，有：
$$|S(x) - S_n(x)| < \varepsilon$$

其中 $S(x) = \sum_{n=1}^{\infty} u_n(x)$ 是和函数。

#### 魏尔斯特拉斯判别法（M判别法）

**定理**：如果存在收敛的正项级数 $\sum_{n=1}^{\infty} M_n$，使得对所有 $x \in E$ 有 $|u_n(x)| \leq M_n$，则 $\sum_{n=1}^{\infty} u_n(x)$ 在 $E$ 上一致收敛。

**示例**：证明 $\sum_{n=1}^{\infty} \frac{\sin nx}{n^2}$ 在 $\mathbb{R}$ 上一致收敛。

**证明**：
由于 $|\sin nx| \leq 1$，故 $\left|\frac{\sin nx}{n^2}\right| \leq \frac{1}{n^2}$。

而 $\sum_{n=1}^{\infty} \frac{1}{n^2}$ 收敛（p-积分，$p = 2 > 1$），故由M判别法，$\sum_{n=1}^{\infty} \frac{\sin nx}{n^2}$ 在 $\mathbb{R}$ 上一致收敛。

### 3. 一致收敛的性质

#### 定理1：连续性

如果 $\sum_{n=1}^{\infty} u_n(x)$ 在 $E$ 上一致收敛，且每个 $u_n(x)$ 在 $E$ 上连续，则和函数 $S(x)$ 在 $E$ 上连续。

#### 定理2：逐项积分

如果 $\sum_{n=1}^{\infty} u_n(x)$ 在 $[a, b]$ 上一致收敛，且每个 $u_n(x)$ 在 $[a, b]$ 上可积，则：
$$\int_a^b \sum_{n=1}^{\infty} u_n(x) dx = \sum_{n=1}^{\infty} \int_a^b u_n(x) dx$$

#### 定理3：逐项微分

如果 $\sum_{n=1}^{\infty} u_n(x)$ 在 $[a, b]$ 上收敛，且 $\sum_{n=1}^{\infty} u_n'(x)$ 在 $[a, b]$ 上一致收敛，则：
$$\frac{d}{dx} \sum_{n=1}^{\infty} u_n(x) = \sum_{n=1}^{\infty} u_n'(x)$$

## 机器学习中的应用

### 1. 神经网络的通用逼近

**定理**：具有足够多神经元的单隐藏层神经网络可以一致逼近任何连续函数。

这实际上是在说：任何复杂的函数都可以用简单的函数（如sigmoid或ReLU）的级数来逼近。

### 2. 正则化

在深度学习中，L2正则化可以看作是对参数的"级数约束"，防止模型过拟合。

$$\mathcal{L}_{reg} = \mathcal{L}_{data} + \lambda \sum_{i=1}^{N} w_i^2$$

## 3. 代码示例

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_function_series(u_n_terms, x_range, n_values, title):
    """
    绘制函数项级数的部分和

    参数:
        u_n_terms: 返回第n项u_n(x)的函数列表
        x_range: x的范围 [a, b]
        n_values: 要绘制的n值列表
        title: 标题
    """
    x = np.linspace(x_range[0], x_range[1], 1000)

    plt.figure(figsize=(12, 6))

    # 绘制部分和
    for n in n_values:
        S_n = np.zeros_like(x)
        for k in range(1, n + 1):
            S_n += u_n_terms[k - 1](x)
        plt.plot(x, S_n, label=f'n = {n}')

    # 绘制极限函数（如果已知）
    # S_inf = ...
    # plt.plot(x, S_inf, 'k--', label='极限函数')

    plt.title(title, fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('S_n(x)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# 示例1：几何级数
u_n_terms = [lambda x: x**n for n in range(1, 6)]
plot_function_series(u_n_terms, [0, 0.9], [1, 3, 5], "几何级数 S_n(x) = 1 + x + x² + ...")

# 示例2：正弦级数
u_n_terms = [lambda x, n=n: ((-1)**(n-1) / n) * np.sin(n*x) for n in range(1, 6)]
plot_function_series(u_n_terms, [0, 2*np.pi], [1, 3, 5], "正弦级数")
```

## 习题

### 基础题

1. 判断以下函数项级数的收敛域：
   - $\sum_{n=1}^{\infty} \frac{x^n}{n}$
   - $\sum_{n=1}^{\infty} \frac{\cos nx}{n^2}$

2. 证明：$\sum_{n=1}^{\infty} \frac{x}{n^2 + x^2}$ 在 $\mathbb{R}$ 上一致收敛。

### 进阶题

3. 利用M判别法证明：$\sum_{n=1}^{\infty} \frac{\cos nx}{n^2}$ 在 $\mathbb{R}$ 上一致收敛。

4. 如果 $\sum_{n=1}^{\infty} u_n(x)$ 在 $[0, 1]$ 上一致收敛，且每个 $u_n(x)$ 连续，证明和函数 $S(x)$ 在 $[0, 1]$ 上连续。

## 相关链接

- [[13_Series]] - 数项级数（函数项级数的基础）
- [[15_Power_Series]] - 幂级数（特殊的函数项级数）
- [[16_Fourier_Series]] - 傅里叶级数（三角函数项级数）
- [[05_Data_Visualization]] - 数据可视化（级数的应用）
## 根据题型整理的做题方法
### 函数项级数收敛性判断

**逐点收敛**：固定$x$，判断$\sum u_n(x)$是否收敛

**一致收敛判别法**：
- **M判别法**：若$|u_n(x)| \leq M_n$且$\sum M_n$收敛，则一致收敛
- **Abel判别法**：$\sum a_n(x)$一致收敛，$b_n(x)$单调有界
- **Dirichlet判别法**：$\sum a_n(x)$部分和一致有界，$b_n(x)$单调趋于0

**一致收敛的性质**：
- 连续函数的一致收敛级数和连续
- 可逐项积分
- 可逐项求导（需附加条件）

## 10. 总结
### 10.1 重要定义
1. 函数项级数：各项为函数的级数 $\sum_{n=1}^\infty u_n(x)$
2. 部分和函数：$S_n(x) = \sum_{k=1}^n u_k(x)$
3. 收敛点：级数收敛的 $x$ 值
4. 一致收敛：收敛速度与 $x$ 无关

### 10.2 重要定理
1. Weierstrass M-判别法：利用收敛的数值级数控制
2. Abel定理：幂级数的收敛区间性质
3. 一致收敛的连续性：一致收敛保持连续性
4. 一致收敛的可积性：可以逐项积分

### 10.3 重要证明
1. Weierstrass M-判别法的证明：先找到一列可求和的常数上界，再用一致 Cauchy 准则说明收敛。
2. 一致收敛可积性的证明：对部分和逐项积分，再用一致收敛把极限和积分交换。

### 10.4 重要性质
1. 一致收敛比逐点收敛更强
2. 一致收敛保证极限函数连续
3. 一致收敛允许逐项积分
4. 一致收敛允许逐项求导（需导数一致收敛）

## 11. 练习（分层）
本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 判断函数项级数 $\sum_{n=1}^{\infty} x^n$ 在 $(-1,1)$ 上的收敛性，并写出和函数。
2. 判断 $\sum_{n=1}^{\infty} \frac{\sin(nx)}{n^2}$ 在 $\mathbb{R}$ 上是否一致收敛。
3. 证明：若 $u_n(x)$ 在 $E$ 上一致收敛于 $0$，则 $\sum u_n(x)$ 的每一项都必须逐点趋于 $0$。
4. 判断 $\sum_{n=1}^{\infty} \frac{x}{n^2+x^2}$ 在 $\mathbb{R}$ 上是否一致收敛。

### B档（进阶）
1. 用 Weierstrass M-判别法证明 $\sum_{n=1}^{\infty} \frac{x^n}{n^2}$ 在 $|x|\le 1$ 上的一致收敛性。
2. 设 $S(x)=\sum_{n=1}^{\infty} \frac{\cos(nx)}{n^2}$，证明 $S(x)$ 连续。
3. 证明：若 $\sum u_n(x)$ 在 $[a,b]$ 上一致收敛且每项可积，则可逐项积分。
4. 研究 $\sum_{n=1}^{\infty} \frac{x}{n(n+x)}$ 的收敛域，并讨论端点行为。

### C档（挑战）
1. 证明：若 $\sum u_n(x)$ 在 $[a,b]$ 上一致收敛且每项连续，则和函数连续。
2. 证明：若 $\sum u_n(x)$ 在 $[a,b]$ 上一致收敛且每项可积，则可逐项积分。
3. 研究级数 $\sum_{n=1}^{\infty} \frac{x^n}{n}$ 在 $[0,1)$ 上的和函数，并说明为什么在 $x\to 1^{-}$ 时会出现边界问题。
4. 构造一个在 $[0,1]$ 上逐点收敛但不一致收敛的函数项级数，并说明它为何不能随意交换极限与积分。


