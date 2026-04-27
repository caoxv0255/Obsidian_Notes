---
type: concept
topic: power_series
category: calculus
difficulty: advanced
prerequisites:
    - [[14_Series]]
    - [[15_Function_Series]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-03-09
status: complete
subject: calculus
chapter: 16
updated: 2026-04-27
---

# 幂级数 (Power Series)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解幂级数、收敛半径和收敛区间的基本概念
- 掌握幂级数的逐项求导、逐项积分与端点判断
- 会用幂级数和泰勒展开处理函数近似与恒等式证明

## 先修
- [[14_Series]] - 级数
- [[15_Function_Series]] - 函数项级数
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：幂级数定义、收敛半径与常见展开
- B档（进阶）：端点判定、逐项运算与泰勒展开
- C档（挑战）：函数逼近、唯一性与综合证明

## 高数/数分附件补充

### 高数题型补充（同济/托马斯）
- **展开求和**：由已知几何级数或泰勒展开出发，再逐项求导/积分
- **函数逼近**：用低阶泰勒多项式近似指数、对数、三角函数
- **常见目标**：求 $\sum n x^n$、$\sum n^2 x^n$、$\arctan x$、$\ln(1+x)$ 的展开

### 数分严谨补充（华师大/Rudin）
- **收敛区间内的逐项运算**：靠一致收敛或幂级数定理保证
- **端点必须单独判断**：这是幂级数题的标准“漏项点”

### 完整例题（从几何级数导出加权和）
由
$$
\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n\qquad (|x|<1)
$$
两边求导得
$$
\frac{1}{(1-x)^2}=\sum_{n=1}^{\infty} n x^{n-1}
$$
故
$$
\sum_{n=1}^{\infty} n x^n = \frac{x}{(1-x)^2},\qquad |x|<1
$$

取 $x=\frac12$，得到
$$
\sum_{n=1}^{\infty} \frac{n}{2^n}=2
$$

## 自测（3问速测）
1. 幂级数的收敛半径如何求，为什么端点要单独判断？
2. 为什么幂级数在收敛区间内可以逐项求导和积分？
3. 常见初等函数的麦克劳林展开各是什么？

## 1. 定义

幂级数是形如 $\sum_{n=0}^{\infty} a_n (x - x_0)^n$ 的函数项级数，其中 $a_n$ 是系数，$x_0$ 是中心点。

## 2. 定理与性质

### 1. 幂级数的收敛性

#### 收敛半径

**定理**：对于幂级数 $\sum_{n=0}^{\infty} a_n (x - x_0)^n$，存在收敛半径 $R$ ($0 \leq R \leq \infty$)，使得：
- 当 $|x - x_0| < R$ 时，级数绝对收敛
- 当 $|x - x_0| > R$ 时，级数发散
- 当 $|x - x_0| = R$ 时，需要单独判断

#### 收敛半径的计算

**比值法**：
$$R = \lim_{n \to \infty} \left|\frac{a_n}{a_{n+1}}\right|$$

**根值法**：
$$R = \frac{1}{\limsup_{n \to \infty} \sqrt[n]{|a_n|}}$$

**示例**：求 $\sum_{n=0}^{\infty} \frac{x^n}{n!}$ 的收敛半径。

**解**：
使用比值法：
$$\lim_{n \to \infty} \left|\frac{a_n}{a_{n+1}}\right| = \lim_{n \to \infty} \left|\frac{1/n!}{1/(n+1)!}\right| = \lim_{n \to \infty} \frac{(n+1)!}{n!} = \lim_{n \to \infty} (n+1) = \infty$$

因此 $R = \infty$，级数对所有 $x \in \mathbb{R}$ 收敛。

### 2. 幂级数的性质

#### 定理1：一致收敛

幂级数在收敛区间内的任何闭区间上一致收敛。

#### 定理2：逐项积分

幂级数在收敛区间内可以逐项积分：
$$\int_{x_0}^{x} \sum_{n=0}^{\infty} a_n (t - x_0)^n dt = \sum_{n=0}^{\infty} \frac{a_n}{n+1} (x - x_0)^{n+1}$$

#### 定理3：逐项微分

幂级数在收敛区间内可以逐项微分：
$$\frac{d}{dx} \sum_{n=0}^{\infty} a_n (x - x_0)^n = \sum_{n=1}^{\infty} n a_n (x - x_0)^{n-1}$$

#### 定理4：唯一性

如果两个幂级数在某区间内相等，则对应项的系数相等。

### 3. 泰勒级数

#### 泰勒级数的定义

函数 $f(x)$ 在 $x_0$ 处的泰勒级数为：
$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!} (x - x_0)^n$$

#### 麦克劳林级数

当 $x_0 = 0$ 时，泰勒级数称为麦克劳林级数：
$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n$$

#### 常见函数的麦克劳林级数

- $e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$，$R = \infty$
- $\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$，$R = \infty$
- $\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$，$R = \infty$
- $\ln(1 + x) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1} x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$，$R = 1$
- $(1 + x)^\alpha = \sum_{n=0}^{\infty} \binom{\alpha}{n} x^n$，$R = 1$（二项式级数）

## 机器学习中的应用

### 1. 激活函数的近似

在深度学习中，有时需要用多项式近似非线性函数（如sigmoid、tanh），这可以使用泰勒级数。

**示例**：用泰勒级数近似sigmoid函数

```python
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def taylor_approximation(x, order):
    """sigmoid函数的泰勒近似（在x=0处展开）"""
    # sigmoid在0处的导数：
    # f(0) = 0.5
    # f'(0) = 0.25
    # f''(0) = 0
    # f'''(0) = -0.125
    # f''''(0) = 0
    # f'''''(0) = 0.3125

    coeffs = {
        0: 0.5,
        1: 0.25,
        2: 0,
        3: -0.125 / 6,  # -1/48
        4: 0,
        5: 0.3125 / 120  # 1/384
    }

    result = 0
    for n in range(order + 1):
        result += coeffs[n] * x**n
    return result

x = np.linspace(-3, 3, 100)
y_true = sigmoid(x)

plt.figure(figsize=(12, 4))

for i, order in enumerate([1, 3, 5], 1):
    plt.subplot(1, 3, i)
    y_approx = taylor_approximation(x, order)
    plt.plot(x, y_true, 'b-', label='sigmoid')
    plt.plot(x, y_approx, 'r--', label=f'泰勒近似（阶数={order}）')
    plt.title(f"阶数 = {order}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### 2. 优化算法的收敛分析

在优化算法的收敛分析中，经常使用泰勒展开来近似目标函数：

$$f(x + \Delta x) \approx f(x) + \nabla f(x)^T \Delta x + \frac{1}{2} \Delta x^T \nabla^2 f(x) \Delta x$$

这是牛顿法的基础。

## 习题

### 基础题

1. 求以下幂级数的收敛半径：
   - $\sum_{n=0}^{\infty} n! x^n$
   - $\sum_{n=0}^{\infty} \frac{x^n}{2^n}$

2. 写出以下函数的麦克劳林级数：
   - $e^{-x}$
   - $\sin(2x)$

### 进阶题

3. 证明：$\sum_{n=0}^{\infty} \frac{x^n}{n!} = e^x$ 对所有 $x \in \mathbb{R}$ 成立。

4. 利用幂级数展开计算 $\int_0^1 e^{-x^2} dx$ 的近似值。

## 相关链接

- [[07_Taylor_Series]] - 泰勒级数（幂级数的特例）
- [[13_Series]] - 数项级数（幂级数的基础）
- [[14_Function_Series]] - 函数项级数（幂级数的推广）
- [[../../01_Mathematics/Optimization/01_Gradient_Descent]] - 梯度下降（泰勒展开的应用）
## 根据题型整理的做题方法
### 幂级数核心要点

**收敛半径公式**：$R = \lim_{n\to\infty} |\frac{a_n}{a_{n+1}}|$ 或 $R = \frac{1}{\lim_{n\to\infty}\sqrt[n]{|a_n|}}$

**收敛区间**：$(-R, R)$，端点需单独判断

**幂级数运算**：
- 加减：收敛半径取较小者
- 乘法：柯西乘积
- 逐项积分/求导：收敛半径不变

**常用展开式**：
- $e^x = \sum \frac{x^n}{n!}$，$R=\infty$
- $\sin x = \sum \frac{(-1)^n x^{2n+1}}{(2n+1)!}$，$R=\infty$
- $\frac{1}{1-x} = \sum x^n$，$R=1$

## 10. 总结
### 10.1 重要定义
1. 幂级数：$\sum_{n=0}^\infty a_n(x-c)^n$ 形式的函数项级数
2. 收敛半径：幂级数收敛的区间长度的一半
3. 收敛区间：$(c-R, c+R)$ 或类似区间
4. 阿贝尔定理：幂级数在收敛区间内连续

### 10.2 重要定理
1. 收敛半径公式：$R = \lim_{n \to \infty} \frac{|a_n|}{|a_{n+1}|}$ 或 $R = \frac{1}{\limsup \sqrt[n]{|a_n|}}$
2. 幂级数的性质：在收敛区间内可以逐项求导和积分
3. 唯一性定理：函数的幂级数展开唯一
4. 和函数的性质：和函数在收敛区间内无限次可微

### 10.3 重要证明
1. 收敛半径公式的证明：利用比值判别法或根值判别法
2. 逐项求导定理的证明：利用一致收敛性

### 10.4 重要性质
1. 收敛区间是以 $c$ 为中心的区间
2. 收敛半径内一致收敛
3. 可以逐项求导和积分
4. 和函数等于原函数（在收敛区间内）

## 根据题型整理的做题方法
### 幂级数四步法
1. 先写出通项，识别中心 $c$ 与系数 $a_n$。
2. 用比值法或根值法求收敛半径 $R$。
3. 在 $|x-c|<R$ 内进行逐项求导、逐项积分或函数变换。
4. 对端点 $x=c\pm R$ 单独判断敛散性。

## 易错点
- 只求收敛半径，不单独判断端点
- 把收敛区间误写成收敛半径
- 逐项求导后忘记更新幂次和系数
- 泰勒展开时漏掉阶乘因子

## 11. 练习（分层）
本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 求幂级数 $\sum_{n=0}^{\infty} \frac{x^n}{n!}$ 的收敛半径，并写出和函数。
2. 判断幂级数 $\sum_{n=0}^{\infty} x^n$ 的收敛区间。
3. 写出 $e^x$、$\sin x$、$\cos x$ 在 $x=0$ 处的麦克劳林展开前四项。
4. 求幂级数 $\sum_{n=0}^{\infty} \left(\frac{x-1}{2}\right)^n$ 的收敛半径。

### B档（进阶）
1. 判定幂级数 $\sum_{n=1}^{\infty} \frac{n}{2^n}(x-1)^n$ 的收敛半径与收敛区间。
2. 利用幂级数证明 $\ln(1+x)=\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n}x^n$（$|x|<1$）。
3. 证明幂级数在收敛区间内逐项积分后仍是幂级数，并写出新的系数。
4. 研究 $\sum_{n=1}^{\infty} \frac{x^n}{n}$ 的收敛区间，并讨论端点。

### C档（挑战）
1. 证明幂级数在收敛区间内可以逐项求导任意次，并说明其和函数无限次可微。
2. 研究 $\sum_{n=0}^{\infty} a_n(x-c)^n$ 的唯一性：若它在某区间上恒等于零，则所有系数都为零。
3. 用泰勒级数证明 $e^x\ge 1+x$，并讨论其推广。
4. 研究一个函数在某点是否解析：例如 $f(x)=\frac{1}{1+x^2}$ 的展开和收敛区间。



