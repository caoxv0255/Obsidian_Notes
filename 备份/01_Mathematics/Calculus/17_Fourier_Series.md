---
type: concept
topic: fourier_series
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
chapter: 17
updated: 2026-04-27
---

# 傅里叶级数 (Fourier Series)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解傅里叶级数、傅里叶系数和正交性的基本概念
- 掌握偶函数、奇函数和分段函数的傅里叶展开方法
- 会用傅里叶级数处理积分恒等式、能量恒等式与信号分解

## 先修
- [[14_Series]] - 级数
- [[15_Function_Series]] - 函数项级数
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：傅里叶系数、偶奇函数与基本展开
- B档（进阶）：分段函数展开、收敛点与帕塞瓦尔等式
- C档（挑战）：积分恒等式、信号处理与综合应用

## 自测（3问速测）
1. 为什么傅里叶系数可以通过正交性直接计算？
2. 偶函数和奇函数的傅里叶级数分别有什么简化？
3. 傅里叶级数在间断点处收敛到什么值？

## 1. 定义

**直观理解**：
傅里叶级数是将周期函数表示为正弦和余弦函数的线性组合：

$$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[a_n \cos\left(\frac{n\pi x}{L}\right) + b_n \sin\left(\frac{n\pi x}{L}\right)\right]$$

其中 $2L$ 是函数的周期。

傅里叶级数的核心思想是：**任何周期函数都可以表示为不同频率的正弦波和余弦波的叠加**。

**类比**：
- 就像音乐可以分解为不同频率的音符
- 光可以分解为不同波长的颜色
- 任何声音都可以用正弦波的组合来表示

## 2. 定理与性质

### 1. 傅里叶系数

#### 系数公式

对于定义在 $[-L, L]$ 上的函数 $f(x)$，傅里叶系数为：

$$a_0 = \frac{1}{L} \int_{-L}^{L} f(x) dx$$

$$a_n = \frac{1}{L} \int_{-L}^{L} f(x) \cos\left(\frac{n\pi x}{L}\right) dx, \quad n = 1, 2, 3, \ldots$$

$$b_n = \frac{1}{L} \int_{-L}^{L} f(x) \sin\left(\frac{n\pi x}{L}\right) dx, \quad n = 1, 2, 3, \ldots$$

#### 正交性

这些公式基于三角函数的正交性：

$$\int_{-L}^{L} \cos\left(\frac{m\pi x}{L}\right) \cos\left(\frac{n\pi x}{L}\right) dx = \begin{cases}
0, & m \neq n \\
L, & m = n \neq 0 \\
2L, & m = n = 0
\end{cases}$$

$$\int_{-L}^{L} \sin\left(\frac{m\pi x}{L}\right) \sin\left(\frac{n\pi x}{L}\right) dx = \begin{cases}
0, & m \neq n \\
L, & m = n \neq 0
\end{cases}$$

$$\int_{-L}^{L} \cos\left(\frac{m\pi x}{L}\right) \sin\left(\frac{n\pi x}{L}\right) dx = 0$$

### 2. 傅里叶级数的收敛性

#### 狄利克雷条件

如果函数 $f(x)$ 满足以下条件，则其傅里叶级数收敛：
1. $f(x)$ 在 $[-L, L]$ 上分段连续
2. $f(x)$ 在 $[-L, L]$ 上分段单调
3. $f(x)$ 在 $[-L, L]$ 上只有有限个极值点

**结论**：在连续点，傅里叶级数收敛于 $f(x)$；在间断点，收敛于 $\frac{f(x^+) + f(x^-)}{2}$。

#### 帕塞瓦尔等式

$$\frac{a_0^2}{2} + \sum_{n=1}^{\infty} (a_n^2 + b_n^2) = \frac{1}{L} \int_{-L}^{L} f^2(x) dx$$

这个等式表示信号的能量在时域和频域是相等的。

### 3. 特殊情况

#### 偶函数的傅里叶级数

如果 $f(x)$ 是偶函数，则 $b_n = 0$，傅里叶级数只包含余弦项：

$$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos\left(\frac{n\pi x}{L}\right)$$

#### 奇函数的傅里叶级数

如果 $f(x)$ 是奇函数，则 $a_n = 0$，傅里叶级数只包含正弦项：

$$f(x) = \sum_{n=1}^{\infty} b_n \sin\left(\frac{n\pi x}{L}\right)$$

### 4. 复数形式的傅里叶级数

$$f(x) = \sum_{n=-\infty}^{\infty} c_n e^{i n \pi x / L}$$

其中：
$$c_n = \frac{1}{2L} \int_{-L}^{L} f(x) e^{-i n \pi x / L} dx$$

## 机器学习中的应用

### 1. 信号处理

傅里叶级数是傅里叶变换的基础，用于：
- 频域分析
- 滤波
- 压缩

### 2. 卷积神经网络

在CNN中，傅里叶变换可以加速卷积运算：

**定理**：时域的卷积等价于频域的乘法：

$$(f * g)(x) \xrightarrow{\mathcal{F}} \hat{f}(\omega) \cdot \hat{g}(\omega)$$

这意味着：
$$\mathcal{F}\{f * g\} = \mathcal{F}\{f\} \cdot \mathcal{F}\{g\}$$

### 3. 注意力机制

在Transformer中，注意力机制可以看作是一种频域操作。

## 3. 代码示例

### 1. 计算傅里叶系数

```python
import numpy as np
from scipy.integrate import quad

def fourier_coefficients(f, L, N):
    """
    计算傅里叶系数

    参数:
        f: 周期函数
        L: 半周期（周期为2L）
        N: 计算前N项系数

    返回:
        a0, a_list, b_list: 傅里叶系数
    """
    # 计算a0
    a0, _ = quad(lambda x: f(x), -L, L)
    a0 = a0 / L

    # 计算an和bn
    a_list = []
    b_list = []

    for n in range(1, N + 1):
        # 计算an
        integrand_an = lambda x: f(x) * np.cos(n * np.pi * x / L)
        an, _ = quad(integrand_an, -L, L)
        an = an / L
        a_list.append(an)

        # 计算bn
        integrand_bn = lambda x: f(x) * np.sin(n * np.pi * x / L)
        bn, _ = quad(integrand_bn, -L, L)
        bn = bn / L
        b_list.append(bn)

    return a0, a_list, b_list

def fourier_series(x, a0, a_list, b_list, L):
    """
    计算傅里叶级数的值

    参数:
        x: 自变量
        a0: a0系数
        a_list: an系数列表
        b_list: bn系数列表
        L: 半周期

    返回:
        y: 傅里叶级数的值
    """
    y = a0 / 2
    for n, (an, bn) in enumerate(zip(a_list, b_list), 1):
        y += an * np.cos(n * np.pi * x / L) + bn * np.sin(n * np.pi * x / L)
    return y

# 示例：方波函数
def square_wave(x):
    """方波函数，周期2"""
    if x < 0:
        x = x + 2 * np.ceil(-x / 2)
    return 1 if (x % 2) < 1 else -1

# 计算系数
L = 1
N = 50
a0, a_list, b_list = fourier_coefficients(square_wave, L, N)

# 绘制
x = np.linspace(-2, 2, 1000)
y_true = np.array([square_wave(xi) for xi in x])

plt.figure(figsize=(12, 8))

for i, n_terms in enumerate([1, 5, 10, 20], 1):
    plt.subplot(2, 2, i)
    y_approx = np.array([fourier_series(xi, a0, a_list[:n_terms], b_list[:n_terms], L) for xi in x])
    plt.plot(x, y_true, 'b-', label='方波')
    plt.plot(x, y_approx, 'r--', label=f'傅里叶级数（{n_terms}项）')
    plt.title(f"项数 = {n_terms}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### 2. 傅里叶变换

```python
from scipy.fft import fft, fftfreq

# 生成信号
T = 2.0  # 信号持续时间
N = 1000  # 采样点数
t = np.linspace(-T/2, T/2, N)

# 复合信号：包含多个频率成分
signal = 3 * np.sin(2 * np.pi * 2 * t) + \
         2 * np.cos(2 * np.pi * 5 * t) + \
         1.5 * np.sin(2 * np.pi * 10 * t)

# 计算FFT
fft_values = fft(signal)
fft_freq = fftfreq(N, t[1] - t[0])

# 绘制
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.title("时域信号")
plt.xlabel("时间")
plt.ylabel("幅值")
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(fft_freq[:N//2], np.abs(fft_values[:N//2]))
plt.title("频域表示")
plt.xlabel("频率")
plt.ylabel("幅值")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

## 习题

### 基础题

1. 计算以下函数在 $[-\pi, \pi]$ 上的傅里叶级数：
   - $f(x) = x$
   - $f(x) = x^2$

2. 判断以下函数的傅里叶级数只包含余弦项还是正弦项：
   - $f(x) = |x|$，$x \in [-1, 1]$
   - $f(x) = x^3$，$x \in [-\pi, \pi]$

### 进阶题

3. 证明：如果 $f(x)$ 是偶函数，则其傅里叶级数只包含余弦项。

4. 利用傅里叶级数计算 $\sum_{n=1}^{\infty} \frac{1}{n^2}$。

### 挑战题

5. 研究傅里叶变换与傅里叶级数的关系，以及它们在信号处理中的应用。

6. 在深度学习中，傅里叶变换如何加速卷积运算？讨论其优缺点。

## 相关链接

- [[13_Series]] - 数项级数（傅里叶级数的基础）
- [[14_Function_Series]] - 函数项级数（傅里叶级数的推广）
- [[08_Case_NLP]] - NLP案例（傅里叶变换在语音处理中的应用）
## 根据题型整理的做题方法
### 傅里叶级数核心公式

**傅里叶系数**（周期$2\pi$）：
- $a_0 = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)dx$
- $a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos nx\,dx$
- $b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin nx\,dx$

**奇偶函数简化**：
- 偶函数：$b_n=0$，只有余弦项
- 奇函数：$a_n=0$，只有正弦项

**收敛定理**（Dirichlet条件）：
若$f$在$[-\pi,\pi]$上分段连续、分段可导，则傅里叶级数收敛于$\frac{f(x^+)+f(x^-)}{2}$

**周期$2L$的函数**：将$x$换成$\frac{\pi x}{L}$即可

## 10. 总结
### 10.1 重要定义
1. 傅里叶级数：周期函数用三角函数表示 $\frac{a_0}{2} + \sum_{n=1}^\infty (a_n \cos nx + b_n \sin nx)$
2. 傅里叶系数：$a_n = \frac{1}{\pi} \int_{-\pi}^\pi f(x) \cos nx \, dx$
3. 周期延拓：将非周期函数延拓为周期函数
4. 正弦级数与余弦级数：奇偶函数的特殊形式

### 10.2 重要定理
1. 狄利克雷收敛定理：满足一定条件的函数可以展开为傅里叶级数
2. 帕塞瓦尔恒等式：傅里叶系数与函数能量的关系
3. 正交性：三角函数系的正交性
4. 收敛判别法：Dirichlet判别法和Abel判别法

### 10.3 重要证明
1. 三角函数系正交性的证明：利用三角函数的积分性质
2. 傅里叶系数公式的证明：利用正交性

### 10.4 重要性质
1. 周期函数的傅里叶展开唯一
2. 收敛性与函数的光滑性相关
3. 可以处理非正弦周期信号
4. 在信号处理、物理中有广泛应用

## 根据题型整理的做题方法
### 傅里叶展开四步法
1. 先确认函数所在区间和周期 $2L$。
2. 利用奇偶性先判断是否能去掉一类系数。
3. 用正交性公式计算 $a_n$ 和 $b_n$。
4. 若是分段函数，再检查收敛点与端点值。

## 易错点
- 忘记周期 $2L$ 与区间 $[-L,L]$ 的对应关系
- 偶函数、奇函数的系数简化方向写反
- 间断点处误以为级数收敛到原函数值
- 计算系数时漏掉积分常数因子

## 11. 练习（分层）
本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 求 $f(x)=x$ 在 $[-\pi,\pi]$ 上的傅里叶级数。
2. 求 $f(x)=x^2$ 在 $[-\pi,\pi]$ 上的傅里叶级数。
3. 判断 $f(x)=|x|$ 在 $[-1,1]$ 上的傅里叶级数只包含哪类项。
4. 判断 $f(x)=x^3$ 在 $[-\pi,\pi]$ 上的傅里叶级数只包含哪类项。

### B档（进阶）
1. 证明偶函数的傅里叶级数只包含余弦项。
2. 利用傅里叶级数计算 $\sum_{n=1}^{\infty} \frac{1}{n^2}$。
3. 求分段函数在 $[-\pi,\pi]$ 上的傅里叶级数，并判断间断点处的收敛值。
4. 证明帕塞瓦尔等式在一个具体函数上的形式。

### C档（挑战）
1. 研究傅里叶级数与傅里叶变换的联系，并说明前者如何导向后者。
2. 用傅里叶级数处理一个热传导或振动模型的初始边值问题。
3. 证明方波级数出现 Gibbs 现象，并说明其极限含义。
4. 讨论傅里叶级数在信号分解中的作用，以及它与卷积的联系。



