---
type: concept
topic: series
category: calculus
difficulty: intermediate
prerequisites:
  - [[02_Limits]]
acm_relevant: true
created: 2026-02-20
status: complete
subject: calculus
chapter: 14
updated: 2026-04-27
---

# 级数 (Series)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解数项级数、部分和与收敛的基本定义
- 掌握等比级数、p-级数、调和级数等典型级数的敛散性
- 会用比较判别法、比值判别法、根值判别法和积分判别法判断敛散性

## 先修
- [[02_Limits]] - 极限
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：级数定义、部分和、等比级数与p-级数
- B档（进阶）：比较判别法、比值判别法、根值判别法
- C档（挑战）：绝对收敛、条件收敛与交错级数综合判断

## 高数/数分附件补充

### 高数题型补充（同济/托马斯/吉米多维奇）
- **先看项型**：等比、p-级数、交错、望远镜、幂级数展开
- **先看极限**：必要条件先验算 $a_n\to0$
- **常见套路**：拆项、配凑、比较、构造望远镜

### 数分严谨补充（华师大/Rudin）
- **Cauchy 判别**：判断级数收敛的核心工具之一
- **绝对收敛优先**：先证绝对收敛再讨论性质最稳妥
- **反例意识**：项趋零不代表和收敛

### 完整例题（望远镜级数）
计算
$$
\sum_{n=1}^{\infty} \frac{1}{n(n+1)}
$$

解：
$$
\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}
$$
故部分和为
$$
S_N=\sum_{n=1}^{N}\left(\frac{1}{n}-\frac{1}{n+1}\right)=1-\frac{1}{N+1}
$$
于是
$$
\sum_{n=1}^{\infty} \frac{1}{n(n+1)}=1
$$

## 自测（3问速测）
1. 为什么级数收敛的必要条件是 $a_n\to 0$，但这并不足以保证收敛？
2. 等比级数 $\sum ar^{n-1}$ 什么时候收敛，和是多少？
3. 比值判别法在 $\rho=1$ 时为什么失效？

## 1. 定义

**直观理解**：
级数是将无限多个数项相加得到的和。级数的收敛性判断是微积分的重要内容。

想象你不断往杯子里倒水，每次倒的水量是前一次的一半。虽然你倒了无限次，但杯子里的水总量是有限的（等于第一次倒水量的两倍）。这就是一个收敛的级数。

## 2. 定理与性质

### 级数的定义

#### 部分和

给定数列 $\{a_n\}$，其部分和序列为：
$$S_n = \sum_{k=1}^{n} a_k = a_1 + a_2 + \cdots + a_n$$

#### 级数的和

如果部分和序列 $\{S_n\}$ 收敛，即存在 $S \in \mathbb{R}$ 使得 $\lim_{n \to \infty} S_n = S$，则称级数 $\sum_{n=1}^{\infty} a_n$ 收敛，其和为 $S$。

记作：
$$\sum_{n=1}^{\infty} a_n = S$$

如果部分和序列发散，则称级数发散。

#### 收敛的必要条件

**定理**：如果 $\sum_{n=1}^{\infty} a_n$ 收敛，则 $\lim_{n \to \infty} a_n = 0$。

**证明**：
设 $\sum_{n=1}^{\infty} a_n = S$，则 $\lim_{n \to \infty} S_n = S$ 且 $\lim_{n \to \infty} S_{n-1} = S$。

因此：
$$\lim_{n \to \infty} a_n = \lim_{n \to \infty} (S_n - S_{n-1}) = \lim_{n \to \infty} S_n - \lim_{n \to \infty} S_{n-1} = S - S = 0$$

**注意**：反之不成立！例如调和级数 $\sum_{n=1}^{\infty} \frac{1}{n}$ 满足 $\lim_{n \to \infty} \frac{1}{n} = 0$，但发散。

### 重要级数

#### 1. 等比级数

$$\sum_{n=1}^{\infty} ar^{n-1} = a + ar + ar^2 + \cdots$$

**收敛性**：
- 当 $|r| < 1$ 时，级数收敛，和为 $\frac{a}{1 - r}$
- 当 $|r| \geq 1$ 时，级数发散

**证明**：
部分和：
$$S_n = a + ar + ar^2 + \cdots + ar^{n-1} = \frac{a(1 - r^n)}{1 - r}$$

当 $|r| < 1$ 时，$\lim_{n \to \infty} r^n = 0$，故：
$$\lim_{n \to \infty} S_n = \frac{a(1 - 0)}{1 - r} = \frac{a}{1 - r}$$

当 $|r| \geq 1$ 时，$\lim_{n \to \infty} r^n$ 不存在或为无穷大，故级数发散。

#### 2. 调和级数

$$\sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots$$

**发散性**：调和级数发散。

**证明（积分判别法）**：
考虑函数 $f(x) = \frac{1}{x}$，它在 $[1, \infty)$ 上正、连续、单调递减。

$$\int_1^{\infty} \frac{1}{x} dx = \lim_{b \to \infty} \ln b = \infty$$

由积分判别法，$\sum_{n=1}^{\infty} \frac{1}{n}$ 发散。

#### 3. p-级数

$$\sum_{n=1}^{\infty} \frac{1}{n^p} = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \cdots$$

**收敛性**：
- 当 $p > 1$ 时，级数收敛
- 当 $p \leq 1$ 时，级数发散

**证明（积分判别法）**：
考虑函数 $f(x) = \frac{1}{x^p}$，它在 $[1, \infty)$ 上正、连续、单调递减（$p > 0$）。

$$\int_1^{\infty} \frac{1}{x^p} dx = \lim_{b \to \infty} \int_1^b x^{-p} dx$$

如果 $p \neq 1$：
$$= \lim_{b \to \infty} \left[\frac{x^{1-p}}{1-p}\right]_1^b = \lim_{b \to \infty} \left(\frac{b^{1-p}}{1-p} - \frac{1}{1-p}\right)$$

- 当 $p > 1$ 时，$1 - p < 0$，故 $b^{1-p} \to 0$，积分收敛
- 当 $p < 1$ 时，$1 - p > 0$，故 $b^{1-p} \to \infty$，积分发散

如果 $p = 1$：
$$\int_1^{\infty} \frac{1}{x} dx = \lim_{b \to \infty} \ln b = \infty$$

发散！

### 收敛判别法

#### 1. 比较判别法

**定理**：设 $\sum_{n=1}^{\infty} a_n$ 和 $\sum_{n=1}^{\infty} b_n$ 是正项级数。

- 如果 $a_n \leq b_n$ 对所有 $n$ 成立，且 $\sum_{n=1}^{\infty} b_n$ 收敛，则 $\sum_{n=1}^{\infty} a_n$ 收敛
- 如果 $a_n \geq b_n$ 对所有 $n$ 成立，且 $\sum_{n=1}^{\infty} b_n$ 发散，则 $\sum_{n=1}^{\infty} a_n$ 发散

**极限形式**：如果 $\lim_{n \to \infty} \frac{a_n}{b_n} = L$（$0 < L < \infty$），则 $\sum_{n=1}^{\infty} a_n$ 和 $\sum_{n=1}^{\infty} b_n$ 同敛散。

#### 2. 比值判别法（达朗贝尔判别法）

**定理**：对于正项级数 $\sum_{n=1}^{\infty} a_n$，设 $\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = \rho$。

- 如果 $\rho < 1$，则级数收敛
- 如果 $\rho > 1$，则级数发散
- 如果 $\rho = 1$，判别法失效

#### 3. 根值判别法（柯西判别法）

**定理**：对于正项级数 $\sum_{n=1}^{\infty} a_n$，设 $\lim_{n \to \infty} \sqrt[n]{a_n} = \rho$。

- 如果 $\rho < 1$，则级数收敛
- 如果 $\rho > 1$，则级数发散
- 如果 $\rho = 1$，判别法失效

#### 4. 积分判别法

**定理**：设 $f(x)$ 在 $[1, \infty)$ 上正、连续、单调递减，则 $\sum_{n=1}^{\infty} f(n)$ 和 $\int_1^{\infty} f(x) dx$ 同敛散。

### 绝对收敛与条件收敛

#### 定义

- **绝对收敛**：如果 $\sum_{n=1}^{\infty} |a_n|$ 收敛，则称 $\sum_{n=1}^{\infty} a_n$ 绝对收敛
- **条件收敛**：如果 $\sum_{n=1}^{\infty} a_n$ 收敛，但 $\sum_{n=1}^{\infty} |a_n|$ 发散，则称 $\sum_{n=1}^{\infty} a_n$ 条件收敛

#### 定理

如果 $\sum_{n=1}^{\infty} |a_n|$ 收敛，则 $\sum_{n=1}^{\infty} a_n$ 收敛。

**证明**：
由于 $-|a_n| \leq a_n \leq |a_n|$，且 $\sum_{n=1}^{\infty} |a_n|$ 收敛，由比较判别法，$\sum_{n=1}^{\infty} a_n$ 收敛。

**示例**：交错调和级数 $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n}$ 条件收敛。

## 3. 证明

### 证明1：Cauchy收敛准则

**定理**：级数 $\sum_{n=1}^{\infty} a_n$ 收敛的充要条件是：对于任意 $\varepsilon > 0$，存在 $N$，使得对于所有 $n > m \geq N$，有 $|a_{m+1} + a_{m+2} + \cdots + a_n| < \varepsilon$。

**证明**：
**必要性**：
设 $\sum_{n=1}^{\infty} a_n = S$，则对于任意 $\varepsilon > 0$，存在 $N$，使得对于所有 $n > N$，有 $|S_n - S| < \varepsilon/2$。

因此对于所有 $n > m \geq N$：
$$|a_{m+1} + a_{m+2} + \cdots + a_n| = |S_n - S_m| = |(S_n - S) + (S - S_m)| \leq |S_n - S| + |S - S_m| < \varepsilon$$

**充分性**：
由条件，$\{S_n\}$ 是柯西数列，故收敛。

### 证明2：莱布尼茨判别法

**定理**：如果交错级数 $\sum_{n=1}^{\infty} (-1)^{n-1} a_n$ 满足：
1. $a_n$ 单调递减
2. $\lim_{n \to \infty} a_n = 0$

则级数收敛。

**证明**：
考虑部分和序列 $\{S_n\}$。

对于奇数项部分和 $S_{2m+1} = S_{2m-1} + a_{2m} - a_{2m+1}$，由于 $a_{2m} \geq a_{2m+1}$，故 $S_{2m+1} \geq S_{2m-1}$。

对于偶数项部分和 $S_{2m} = S_{2m-2} - a_{2m-1} + a_{2m}$，由于 $a_{2m-1} \geq a_{2m}$，故 $S_{2m} \leq S_{2m-2}$。

因此：
$$S_1 \leq S_3 \leq S_5 \leq \cdots \leq S_6 \leq S_4 \leq S_2$$

由于 $0 \leq S_{2m} - S_{2m-1} = a_{2m} \to 0$，故 $\{S_{2m-1}\}$ 和 $\{S_{2m}\}$ 收敛到同一极限。

因此 $\{S_n\}$ 收敛。

## 4. 代码示例

```python
import numpy as np
from scipy.integrate import quad

def geometric_series_sum(a, r, n_terms=1000):
    """计算等比级数和"""
    if abs(r) >= 1:
        return float('inf')
    return a / (1 - r)

# 示例
print(f"Σ(1/2^n) = {geometric_series_sum(1, 0.5)}")

# 泰勒级数展开
def taylor_sin(x, n_terms=10):
    """sin(x) 的泰勒级数展开"""
    result = 0
    for n in range(n_terms):
        term = ((-1)**n * x**(2*n + 1)) / np.math.factorial(2*n + 1)
        result += term
    return result

x = np.pi / 2
print(f"sin(π/2) ≈ {taylor_sin(x, 10)}")
print(f"真实值: {np.sin(x):.10f}")

# 级数收敛性测试
def test_series_convergence(a_n_func, n_max=10000):
    """测试级数的收敛性"""
    partial_sums = []
    current_sum = 0
    
    for n in range(1, n_max + 1):
        current_sum += a_n_func(n)
        partial_sums.append(current_sum)
    
    # 检查是否收敛
    if abs(partial_sums[-1] - partial_sums[-100]) < 1e-6:
        return True, partial_sums[-1]
    else:
        return False, partial_sums[-1]

# 测试调和级数
def harmonic_term(n):
    return 1 / n

converges, value = test_series_convergence(harmonic_term)
print(f"\n调和级数收敛: {converges}")

# 测试p-级数 (p=2)
def p_series_term(n, p=2):
    return 1 / (n ** p)

converges, value = test_series_convergence(lambda n: p_series_term(n, 2))
print(f"p-级数(p=2)收敛: {converges}, 值 ≈ {value:.6f}")
print(f"理论值: π²/6 ≈ {np.pi**2/6:.6f}")
```

## 5. 机器学习应用

### 1. 损失函数的期望

在机器学习中，期望损失本质上是无限级数的求和：

$$\mathbb{E}[L] = \sum_{x \in \mathcal{X}} L(x) P(x)$$

其中 $\mathcal{X}$ 可能是无限集。

### 2. 正则化中的级数

L2正则化可以看作是无限级数的和：

$$\sum_{i=1}^{\infty} w_i^2$$

为了使这个级数收敛，必须要求 $\lim_{i \to \infty} w_i = 0$。

### 3. 泰勒级数逼近

泰勒级数用于函数逼近和误差分析：

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x - a)^n$$

## 习题

### 基础题

1. 判断以下级数的收敛性：
   - $\sum_{n=1}^{\infty} \frac{1}{2^n}$
   - $\sum_{n=1}^{\infty} \frac{1}{n^2}$
   - $\sum_{n=1}^{\infty} \frac{n}{n+1}$

2. 利用比值判别法判断 $\sum_{n=1}^{\infty} \frac{n!}{n^n}$ 的收敛性。

3. 判断 $\sum_{n=1}^{\infty} \frac{(-1)^n}{n}$ 是绝对收敛还是条件收敛。

### 进阶题

4. 证明：如果 $\sum_{n=1}^{\infty} a_n$ 收敛，则 $\lim_{n \to \infty} a_n = 0$。

5. 利用积分判别法证明：$\sum_{n=1}^{\infty} \frac{1}{n \ln n}$ 发散。

6. 证明：如果 $\sum_{n=1}^{\infty} a_n$ 绝对收敛，则 $\sum_{n=1}^{\infty} a_n$ 收敛。

### 挑战题

7. 证明：$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$（巴塞尔问题）。

8. 在深度学习中，为什么需要控制参数范数？这与级数收敛有什么关系？

## 相关链接

- [[02_Limits]] - 极限（级数的基础）
- [[14_Function_Series]] - 函数项级数（级数的推广）
- [[15_Power_Series]] - 幂级数（特殊的函数项级数）
- [[06_Case_Finance]] - 金融案例（级数在时间序列中的应用）

## 参考资料

- 数学分析原理 - Walter Rudin
- 数学分析（第5版）- 华东师范大学数学系
- 高等数学（第八版）- 同济大学数学科学学院
- 托马斯微积分（第十版）- Thomas
## 根据题型整理的做题方法
### 级数收敛性判断流程

```
级数收敛性判断
    │
    ├── 通项不趋于0？
    │       └── 是 → 发散（必要条件）
    │
    ├── 正项级数？
    │       ├── 比较判别法
    │       ├── 比值判别法（d'Alembert）
    │       ├── 根值判别法（Cauchy）
    │       └── 积分判别法
    │
    ├── 交错级数？
    │       └── Leibniz判别法
    │
    └── 一般级数？
            └── 绝对收敛判别
```

### 核心判别法速查

| 判别法 | 适用类型 | 关键条件 |
|-------|---------|---------|
| **比值判别法** | 正项级数 | $\lim \frac{a_{n+1}}{a_n}$ 与1比较 |
| **根值判别法** | 正项级数 | $\lim \sqrt[n]{a_n}$ 与1比较 |
| **比较判别法** | 正项级数 | 与已知级数比较 |
| **Leibniz判别法** | 交错级数 | 单调递减趋于0 |
| **绝对收敛** | 一般级数 | $\sum|a_n|$ 收敛 |

### 重要级数结论

- 几何级数：$\sum r^n$ 收敛当且仅当 $|r|<1$
- p-级数：$\sum \frac{1}{n^p}$ 收敛当且仅当 $p>1$
- 调和级数：$\sum \frac{1}{n}$ 发散

## 10. 总结
### 10.1 重要定义
1. 数项级数：数列各项之和 $S = \sum_{n=1}^\infty a_n$
2. 部分和：$S_n = a_1 + a_2 + \cdots + a_n$
3. 级数收敛：部分和序列有极限
4. 正项级数：各项非负的级数
5. 交错级数：各项正负相间的级数

### 10.2 重要定理
1. 级数收敛的必要条件：$\lim_{n \to \infty} a_n = 0$
2. 正项级数比较判别法：与已知敛散性的级数比较
3. 比值判别法（d'Alembert）：$\lim \frac{a_{n+1}}{a_n} = \rho$
4. 根值判别法（Cauchy）：$\lim \sqrt[n]{a_n} = \rho$
5. 莱布尼茨判别法：交错级数单调递减且极限为0则收敛

### 10.3 重要证明
1. 级数收敛必要条件的证明：利用部分和极限
2. 比较判别法的证明：利用正项级数的单调性
3. 莱布尼茨判别法的证明：利用交错级数的部分和性质

### 10.4 重要性质
1. 线性性：收敛级数的线性组合仍收敛
2. 添加或删除有限项不改变敛散性
3. 收敛级数必满足 $\lim_{n \to \infty} a_n = 0$
4. 条件收敛与绝对收敛的区别
## 11. 练习（分层）
本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 判断级数 $\sum_{n=1}^{\infty} \frac{1}{2^n}$ 的收敛性并求和。
2. 判断级数 $\sum_{n=1}^{\infty} \frac{1}{n^2}$ 的敛散性。
3. 判断级数 $\sum_{n=1}^{\infty} \frac{1}{n}$ 的敛散性，并说明它为何是经典反例。
4. 判断级数 $\sum_{n=1}^{\infty} \left(\frac{3}{4}\right)^n$ 的收敛性并求和。

### B档（进阶）
1. 用比较判别法判断 $\sum_{n=1}^{\infty} \frac{1}{n^2+n}$ 的敛散性。
2. 用比值判别法判断 $\sum_{n=1}^{\infty} \frac{n!}{n^n}$ 的敛散性。
3. 用根值判别法判断 $\sum_{n=1}^{\infty} \left(\frac{2n+1}{3n+2}\right)^n$ 的敛散性。
4. 判断交错级数 $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n}$ 是否收敛，并说明它属于哪类收敛。

### C档（挑战）
1. 证明：如果 $\sum a_n$ 绝对收敛，则它一定收敛。
2. 证明 Leibniz 判别法，并用它分析 $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^p}$ 在不同 $p$ 下的敛散性。
3. 研究级数 $\sum_{n=1}^{\infty} \frac{x^n}{n}$ 的收敛域，并讨论边界点的敛散性。
4. 尝试用积分判别法证明调和级数发散，并与积分 $\int_1^{\infty} \frac{1}{x}dx$ 对照。



