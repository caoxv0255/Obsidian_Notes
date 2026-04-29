---
type: concept

topic: real_numbers

category: calculus

difficulty: advanced

prerequisites: []

acm_relevant: false

created: 2026-03-09

status: complete

subject: calculus
chapter: 01
updated: 2026-04-27
---

# 实数理论 (Real Numbers)

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

## 1. 定义

### 1.1 实数集的定义

实数集 $\mathbb{R}$ 是满足以下性质的集合：

1. **域公理**：$\mathbb{R}$ 是一个有序域
   - 加法和乘法满足交换律、结合律、分配律
   - 存在加法单位元 $0$ 和乘法单位元 $1$
   - 每个元素都有加法逆元，每个非零元素都有乘法逆元
   - 存在序关系 $<$，满足传递性、三歧性

2. **完备性公理**（确界原理）：
   - $\mathbb{R}$ 的任何非空有上界的子集都有最小上界（上确界）

### 1.2 上确界和下确界

设 $S \subset \mathbb{R}$ 是非空集合：

- **上确界**（supremum）：集合 $S$ 的最小上界
  - 记作 $\sup S$
  - 满足：$\forall x \in S, x \leq \sup S$ 且 $\forall \varepsilon > 0, \exists x \in S$ 使得 $x > \sup S - \varepsilon$

- **下确界**（infimum）：集合 $S$ 的最大下界
  - 记作 $\inf S$
  - 满足：$\forall x \in S, x \geq \inf S$ 且 $\forall \varepsilon > 0, \exists x \in S$ 使得 $x < \inf S + \varepsilon$

### 1.3 有理数与无理数

- **有理数**：可以表示为两个整数之比的数，即 $\frac{p}{q}$，其中 $p, q \in \mathbb{Z}$，$q \neq 0$
  - 有理数集记作 $\mathbb{Q}$
  - 有理数在实数中是稠密的，但不完备

- **无理数**：不能表示为两个整数之比的实数
  - 如 $\sqrt{2}, \pi, e$ 等
  - 无理数在实数中也是稠密的

### 1.4 邻域与开闭集

设 $a \in \mathbb{R}$，$\delta > 0$：

- **邻域**：$U(a, \delta) = \{x \in \mathbb{R} \mid |x - a| < \delta\}$
- **去心邻域**：$U^\circ(a, \delta) = \{x \in \mathbb{R} \mid 0 < |x - a| < \delta\}$

- **开集**：集合 $U$ 是开集，如果 $\forall x \in U$，$\exists \delta > 0$，使得 $U(x, \delta) \subset U$
- **闭集**：集合 $F$ 是闭集，如果其补集 $F^c = \mathbb{R} \setminus F$ 是开集

### 1.5 绝对值

对于 $x \in \mathbb{R}$，绝对值定义为：
$$|x| = \begin{cases}
x, & x \geq 0 \\
-x, & x < 0
\end{cases}$$

## 2. 代码示例

### 示例 1：计算确界

```python
import numpy as np

def supremum(S):
    """计算集合的上确界"""
    if not S:
        raise ValueError("集合不能为空")
    return max(S)

def infimum(S):
    """计算集合的下确界"""
    if not S:
        raise ValueError("集合不能为空")
    return min(S)

# 示例 1：有限集合
S1 = {1, 2, 3, 4, 5}
print(f"集合 S1 = {S1}")
print(f"sup S1 = {supremum(S1)}")
print(f"inf S1 = {infimum(S1)}")

# 示例 2：区间
S2 = set(np.linspace(0, 1, 1001))
print(f"\n集合 S2 = [0, 1] 的离散近似")
print(f"sup S2 = {supremum(S2)}")
print(f"inf S2 = {infimum(S2)}")

# 示例 3：有上界但无上确界的集合（在有限表示中）
# 在实数系中，{x | x^2 < 2} 的上确界是 √2
import math
S3 = {x/1000 for x in range(-1414, 1415) if x**2 < 2*1000**2}
print(f"\n集合 S3 = {{x | x² < 2}} 的近似")
print(f"sup S3 ≈ {supremum(S3):.6f}")
print(f"√2 = {math.sqrt(2):.6f}")
```

### 示例 2：验证三角不等式

```python
import numpy as np
import random

def verify_triangle_inequality(n_tests=1000, x_range=(-10, 10)):
    """验证三角不等式 |x + y| ≤ |x| + |y|"""
    for _ in range(n_tests):
        x = random.uniform(*x_range)
        y = random.uniform(*x_range)
        
        left = abs(x + y)
        right = abs(x) + abs(y)
        
        if left > right + 1e-10:  # 考虑浮点误差
            print(f"反例：x = {x}, y = {y}")
            print(f"|x + y| = {left}, |x| + |y| = {right}")
            return False
    
    print(f"三角不等式在 {n_tests} 次随机测试中成立")
    return True

verify_triangle_inequality()

# 验证反向三角不等式
def verify_reverse_triangle_inequality(n_tests=1000, x_range=(-10, 10)):
    """验证反向三角不等式 ||x| - |y|| ≤ |x - y|"""
    for _ in range(n_tests):
        x = random.uniform(*x_range)
        y = random.uniform(*x_range)
        
        left = abs(abs(x) - abs(y))
        right = abs(x - y)
        
        if left > right + 1e-10:
            print(f"反例：x = {x}, y = {y}")
            print(f"||x| - |y|| = {left}, |x - y| = {right}")
            return False
    
    print(f"反向三角不等式在 {n_tests} 次随机测试中成立")
    return True

verify_reverse_triangle_inequality()
```

### 示例 3：AM-GM 不等式

```python
import numpy as np

def am_gm_inequality(n=5, n_tests=1000):
    """验证 AM-GM 不等式"""
    violations = 0
    
    for _ in range(n_tests):
        # 生成 n 个正数
        numbers = np.random.uniform(0.1, 10, n)
        
        # 计算算术平均和几何平均
        am = np.mean(numbers)
        gm = np.prod(numbers) ** (1/n)
        
        # 验证不等式
        if am < gm - 1e-10:
            violations += 1
            print(f"违反：AM = {am:.6f}, GM = {gm:.6f}")
            print(f"数字：{numbers}")
    
    print(f"AM-GM 不等式在 {n_tests} 次测试中违反 {violations} 次")
    return violations == 0

# 验证不同 n 的情况
for n in [2, 3, 5, 10]:
    print(f"\nn = {n}:")
    am_gm_inequality(n)
```

### 示例 4：柯西-施瓦茨不等式

```python
import numpy as np

def cauchy_schwarz_inequality(dim=5, n_tests=1000):
    """验证柯西-施瓦茨不等式"""
    violations = 0
    
    for _ in range(n_tests):
        # 生成两个向量
        x = np.random.randn(dim)
        y = np.random.randn(dim)
        
        # 计算不等式两边
        left = np.dot(x, y) ** 2
        right = np.dot(x, x) * np.dot(y, y)
        
        # 验证不等式
        if left > right + 1e-10:
            violations += 1
            print(f"违反：(x·y)² = {left:.6f}, ||x||²·||y||² = {right:.6f}")
    
    print(f"柯西-施瓦茨不等式在 {n_tests} 次测试中违反 {violations} 次")
    return violations == 0

# 验证不同维度的情况
for dim in [2, 3, 5, 10]:
    print(f"\n维度 = {dim}:")
    cauchy_schwarz_inequality(dim)
```

### 示例 5：闭区间套定理

```python
import numpy as np

def nested_interval_theorem(n=10):
    """演示闭区间套定理"""
    a = 0  # 初始左端点
    b = 1  # 初始右端点
    
    intervals = []
    
    for i in range(n):
        intervals.append((a, b))
        
        # 构造新的嵌套区间
        mid = (a + b) / 2
        if i % 2 == 0:
            b = mid  # 保留左半部分
        else:
            a = mid  # 保留右半部分
    
    print("闭区间套序列：")
    for i, (ai, bi) in enumerate(intervals):
        print(f"[{i+1}] [{ai:.6f}, {bi:.6f}], 长度 = {bi - ai:.6f}")
    
    # 极限点
    c = (a + b) / 2
    print(f"\n极限点 c ≈ {c:.6f}")
    print(f"区间长度趋于 0: {b - a:.6f}")
    
    return c

nested_interval_theorem(10)
```

## 3. 机器学习应用

### 应用 1：损失函数的有界性

在机器学习中，损失函数必须有下界（通常为 0），否则优化过程无法收敛。

```python
import numpy as np

def loss_function_boundedness(losses):
    """验证损失函数的有界性"""
    infimum = np.min(losses)
    print(f"损失函数的最小值（下确界）: {infimum:.6f}")
    
    # 检查是否有界
    if infimum >= 0:
        print("损失函数有下界（非负）")
    else:
        print(f"损失函数的下界为负数: {infimum:.6f}")
    
    return infimum

# 模拟训练过程中的损失值
epochs = 100
losses = np.exp(-np.linspace(0, 5, epochs)) + 0.1 * np.random.randn(epochs)
losses = np.maximum(losses, 0)  # 确保非负

print("训练损失值：")
loss_function_boundedness(losses)
```

### 应用 2：柯西-施瓦茨不等式在余弦相似度中的应用

余弦相似度本质上是向量的归一化点积，可以利用柯西-施瓦茨不等式证明其范围在 [-1, 1] 之间。

```python
import numpy as np

def cosine_similarity(x, y):
    """计算余弦相似度"""
    # 归一化
    x_norm = x / np.linalg.norm(x)
    y_norm = y / np.linalg.norm(y)
    
    # 点积
    similarity = np.dot(x_norm, y_norm)
    
    # 由于归一化，cosine similarity ∈ [-1, 1]
    similarity = np.clip(similarity, -1, 1)
    
    return similarity

# 示例
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([-1, -2, -3])

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")

print(f"\n余弦相似度(v1, v2) = {cosine_similarity(v1, v2):.6f}")
print(f"余弦相似度(v1, v3) = {cosine_similarity(v1, v3):.6f}")
print(f"余弦相似度(v2, v3) = {cosine_similarity(v2, v3):.6f}")
```

## 根据题型整理的做题方法
### 实数理论问题的分析方法

实数理论是数学分析的基础，其问题多为证明题和概念题。

#### 📋 第一步：识别问题类型

| 问题类型 | 特点 | 主要方法 |
|---------|------|---------|
| **确界计算** | 求集合的上/下确界 | 利用单调性、极限 |
| **存在性证明** | 证明某对象存在 | 构造法、反证法 |
| **不等式证明** | 证明不等式成立 | 放缩法、归纳法 |
| **收敛性证明** | 证明数列收敛 | 柯西准则、单调有界 |
| **稠密性证明** | 证明某集合在另一集合中稠密 | 构造有理数逼近 |

#### 🔧 第二步：选择证明策略

```
问题分析
    │
    ├── 涉及确界？
    │       ├── 计算确界 → 找最大/最小值，分析极限
    │       └── 证明存在 → 利用确界原理
    │
    ├── 证明不等式？
    │       ├── 绝对值不等式 → 三角不等式
    │       ├── 平均值不等式 → AM-GM
    │       └── 向量不等式 → 柯西-施瓦茨
    │
    ├── 证明收敛？
    │       ├── 单调有界 → 单调有界定理
    │       └── 柯西列 → 柯西收敛准则
    │
    └── 证明稠密性？
            └── 构造有理数逼近
```

### 💡 核心技巧与常用结论

#### 1. 确界的计算方法

**策略**：
1. 判断集合是否有界
2. 找出可能的确界值
3. 验证：① 是上/下界；② 是最小上界/最大下界

**常见集合的确界**：

| 集合 $A$ | $\sup A$ | $\inf A$ |
|---------|---------|---------|
| $\{x \mid x^2 < 2\}$ | $\sqrt{2}$ | $-\sqrt{2}$ |
| $\{\frac{1}{n} \mid n \in \mathbb{N}\}$ | $1$ | $0$（不在 $A$ 中） |
| $\{\frac{n}{n+1} \mid n \in \mathbb{N}\}$ | $1$（不在 $A$ 中） | $\frac{1}{2}$ |

**关键点**：确界可能不在集合内！

#### 2. 绝对值不等式

**三角不等式**：$|x + y| \leq |x| + |y|$

**反向三角不等式**：$||x| - |y|| \leq |x - y|$

#### 3. AM-GM 不等式

**公式**：$\frac{a_1 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 \cdots a_n}$

**等号条件**：$a_1 = a_2 = \cdots = a_n$

#### 4. 柯西-施瓦茨不等式

**代数形式**：$(\sum a_i b_i)^2 \leq (\sum a_i^2)(\sum b_i^2)$

**向量形式**：$|\vec{a} \cdot \vec{b}| \leq |\vec{a}| \cdot |\vec{b}|$

**等号条件**：$\vec{a}$ 与 $\vec{b}$ 线性相关

#### 5. 无理数证明（反证法模板）

1. 假设为有理数 $\frac{p}{q}$（$p, q$ 互质）
2. 推出 $p, q$ 有公因子
3. 矛盾，故为无理数

### 🎯 题型分类与对策

| 题型 | 关键技巧 | 典型问题 |
|-----|---------|---------|
| 确界计算 | 分析单调性和极限 | 求 $\sup\{x^2 < 2\}$ |
| 不等式证明 | 放缩法、归纳法 | 证明 $|x+y| \leq |x|+|y|$ |
| 收敛性证明 | 柯西准则、单调有界 | 证明 $\{\frac{n}{n+1}\}$ 收敛 |
| 存在性证明 | 构造法、反证法 | 证明无理数存在 |
| 稠密性证明 | 构造逼近序列 | 证明 $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密 |

### ⚠️ 常见错误与陷阱

**错误一**：混淆上界和上确界
- 上确界是"最小上界"，不是"某个上界"

**错误二**：忽略确界不在集合内的情况
- $\inf\{\frac{1}{n}\} = 0$，但 $0 \notin \{\frac{1}{n}\}$

**错误三**：不等式放缩过度
- 放缩要保持方向，不能丢失关键信息

## 4. 易错点
⚠️ **常见错误**

1. **混淆有理数和实数**
   - 有理数集 $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密但不完备
   - 极限运算需要在实数系中进行

2. **忽略确界的存在性**
   - 不是所有集合都有确界（如无上界的集合）
   - 确界原理只保证有界集合的确界存在

3. **不等式的方向**
   - 不等式乘以负数时要改变方向
   - 绝对值不等式要注意三角不等式的应用

✅ **最佳实践**

1. **理解完备性的重要性**
   - 完备性是微积分的基础
   - 没有完备性，极限可能不存在

2. **掌握确界的概念**
   - 确界是极限理论的基础
   - 理解 sup 和 inf 的定义和性质

3. **熟练使用不等式**
   - AM-GM、柯西-施瓦茨等不等式是重要工具
   - 在证明和估计中经常用到

## 严格证明（Rudin风格）

### 证明1：确界原理的推论 - 阿基米德性质

**定理**：对于任意 $x, y \in \mathbb{R}$，且 $x > 0$，存在 $n \in \mathbb{N}$，使得 $nx > y$。

**证明**：
假设不存在这样的 $n$，即对所有 $n \in \mathbb{N}$，有 $nx \leq y$。

令 $A = \{nx \mid n \in \mathbb{N}\}$，则 $A$ 有上界 $y$。

由确界原理，$A$ 有上确界，记为 $\sup A = s$。

由于 $s - x < s$，故存在 $n_0 \in \mathbb{N}$，使得 $n_0 x > s - x$。

因此 $(n_0 + 1)x > s$，但 $(n_0 + 1)x \in A$，这与 $s = \sup A$ 矛盾！

因此假设不成立，定理得证。

### 证明2：有界单调序列定理

**定理**：单调递增且有上界的数列必收敛；单调递减且有下界的数列必收敛。

**证明**：
设 $\{x_n\}$ 是单调递增且有上界的数列。

令 $s = \sup\{x_n \mid n \in \mathbb{N}\}$（由确界原理，$s$ 存在）。

对于任意 $\varepsilon > 0$，由于 $s - \varepsilon$ 不是上界，存在 $N$，使得 $x_N > s - \varepsilon$。

由于 $\{x_n\}$ 单调递增，对于所有 $n \geq N$，有：
$$s - \varepsilon < x_N \leq x_n \leq s$$

因此 $|x_n - s| < \varepsilon$ 对所有 $n \geq N$ 成立，故 $\lim_{n \to \infty} x_n = s$。

单调递减的情况类似可证。

### 证明3：柯西收敛准则

**定理**：数列 $\{x_n\}$ 收敛的充要条件是：$\forall \varepsilon > 0$，$\exists N$，使得 $\forall m, n > N$，有 $|x_m - x_n| < \varepsilon$。

**证明**：

**必要性**：
设 $\lim_{n \to \infty} x_n = L$，则对于任意 $\varepsilon > 0$，存在 $N$，使得对于所有 $n > N$，有 $|x_n - L| < \varepsilon/2$。

因此对于所有 $m, n > N$：
$$|x_m - x_n| \leq |x_m - L| + |L - x_n| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

**充分性**：
假设柯西条件成立。首先证明 $\{x_n\}$ 有界。

取 $\varepsilon = 1$，存在 $N$，使得对于所有 $m, n > N$，有 $|x_m - x_n| < 1$。

特别地，对于所有 $n > N$，有 $|x_n - x_{N+1}| < 1$，故 $|x_n| < |x_{N+1}| + 1$。

令 $M = \max\{|x_1|, |x_2|, \ldots, |x_N|, |x_{N+1}| + 1\}$，则 $|x_n| \leq M$ 对所有 $n \in \mathbb{N}$ 成立。

由 Bolzano-Weierstrass 定理，$\{x_n\}$ 有收敛子列 $\{x_{n_k}\}$，设其极限为 $L$。

对于任意 $\varepsilon > 0$，存在 $K$，使得对于所有 $k \geq K$，有 $|x_{n_k} - L| < \varepsilon/2$。

取 $N'$ 使得对于所有 $m, n > N'$，有 $|x_m - x_n| < \varepsilon/2$。

对于任意 $n > N'$，选择 $k$ 使得 $n_k > N'$，则：
$$|x_n - L| \leq |x_n - x_{n_k}| + |x_{n_k} - L| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$

因此 $\lim_{n \to \infty} x_n = L$。

## 6. 更多例题

### 例题1：计算集合的确界

**问题**：设 $A = \{\frac{n}{n+1} \mid n \in \mathbb{N}\}$，求 $\sup A$ 和 $\inf A$。

**解**：
首先观察数列 $a_n = \frac{n}{n+1} = 1 - \frac{1}{n+1}$。

由于 $\frac{1}{n+1}$ 单调递减，故 $a_n$ 单调递增。

因此 $a_1 = \frac{1}{2}$ 是最小值，$\inf A = \frac{1}{2}$。

对于上确界，显然 $a_n < 1$ 对所有 $n \in \mathbb{N}$ 成立，故 $1$ 是上界。

对于任意 $\varepsilon > 0$，选择 $N$ 使得 $\frac{1}{N+1} < \varepsilon$，则：
$$a_N = 1 - \frac{1}{N+1} > 1 - \varepsilon$$

因此 $\sup A = 1$。

### 例题2：证明无理数的存在

**问题**：证明 $\sqrt{2}$ 是无理数。

**证明**：
假设 $\sqrt{2}$ 是有理数，即 $\sqrt{2} = \frac{p}{q}$，其中 $p, q \in \mathbb{N}$ 互质。

两边平方：$2 = \frac{p^2}{q^2}$，故 $p^2 = 2q^2$。

因此 $p^2$ 是偶数，故 $p$ 是偶数，设 $p = 2k$。

代入得：$(2k)^2 = 2q^2$，即 $4k^2 = 2q^2$，故 $q^2 = 2k^2$。

因此 $q^2$ 是偶数，故 $q$ 是偶数。

这与 $p, q$ 互质矛盾！

因此假设不成立，$\sqrt{2}$ 是无理数。

### 例题3：证明稠密性

**问题**：证明 $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密，即对于任意 $x < y$，存在 $q \in \mathbb{Q}$，使得 $x < q < y$。

**证明**：
由于 $y - x > 0$，由阿基米德性质，存在 $n \in \mathbb{N}$，使得 $n(y - x) > 1$。

即 $ny - nx > 1$。

令 $m = \lceil nx \rceil$（大于或等于 $nx$ 的最小整数），则：
$$m - 1 < nx \leq m$$

因此：
$$nx \leq m < nx + 1 < ny$$

即 $x < \frac{m}{n} < y$。

令 $q = \frac{m}{n} \in \mathbb{Q}$，则 $x < q < y$，得证。

## 7. 更多习题

### 基础题

1. 设 $A = \{\frac{1}{n} \mid n \in \mathbb{N}\}$，求 $\sup A$ 和 $\inf A$。

2. 证明：$\sqrt{3}$ 是无理数。

3. 设 $x, y \in \mathbb{R}$，证明：$|x + y| \geq ||x| - |y||$。

### 进阶题

4. 证明：闭区间套定理与完备性公理等价。

5. 设 $\{x_n\}$ 和 $\{y_n\}$ 都是有界数列，证明：
   $$\sup\{x_n + y_n\} \leq \sup\{x_n\} + \sup\{y_n\}$$

6. 构造一个有界但无极限的数列。

### 挑战题

7. 证明：实数系 $\mathbb{R}$ 是不可数的（康托尔对角线法）。

8. 证明：对于任意 $x \in \mathbb{R}$，存在有理数序列 $\{q_n\}$，使得 $\lim_{n \to \infty} q_n = x$。

## 8. 更多应用

### 应用3：梯度下降的收敛性

梯度下降算法的收敛性依赖于损失函数的下确界和单调性。

```python
import numpy as np

def gradient_descent_with_convergence_analysis(f, grad_f, x0, learning_rate=0.1, max_iter=1000, tol=1e-6):
    """
    带收敛性分析的梯度下降算法

    参数:
        f: 目标函数
        grad_f: 梯度函数
        x0: 初始点
        learning_rate: 学习率
        max_iter: 最大迭代次数
        tol: 容差

    返回:
        x: 优化后的点
        loss_history: 损失历史
    """
    x = x0
    loss_history = []

    for i in range(max_iter):
        loss = f(x)
        loss_history.append(loss)

        # 计算梯度
        grad = grad_f(x)

        # 检查收敛
        if np.linalg.norm(grad) < tol:
            print(f"在 {i} 次迭代后收敛")
            break

        # 更新参数
        x = x - learning_rate * grad

    # 验证单调性（损失函数应该单调递减）
    is_monotonic = all(loss_history[i] >= loss_history[i+1] 
                       for i in range(len(loss_history)-1))
    
    print(f"损失函数单调递减: {is_monotonic}")
    print(f"初始损失: {loss_history[0]:.6f}")
    print(f"最终损失: {loss_history[-1]:.6f}")
    
    return x, loss_history

# 示例：最小化 f(x) = x² + 2x + 1
f = lambda x: x**2 + 2*x + 1
grad_f = lambda x: 2*x + 2

x0 = np.array([5.0])
x_opt, losses = gradient_descent_with_convergence_analysis(f, grad_f, x0)

print(f"\n最优解: x = {x_opt[0]:.6f}")
print(f"理论值: x = -1")
```

### 应用4：正则化中的不等式

L2正则化利用了柯西-施瓦茨不等式来约束参数范数。

```python
import numpy as np

def l2_regularization_loss(weights, lambda_reg):
    """L2正则化损失"""
    return 0.5 * lambda_reg * np.sum(weights**2)

def l2_regularization_gradient(weights, lambda_reg):
    """L2正则化梯度"""
    return lambda_reg * weights

# 示例：在训练过程中应用L2正则化
def train_with_regularization(X, y, learning_rate=0.01, lambda_reg=0.1, epochs=100):
    """带L2正则化的线性回归训练"""
    n_samples, n_features = X.shape
    weights = np.random.randn(n_features)
    bias = 0.0
    
    loss_history = []
    
    for epoch in range(epochs):
        # 前向传播
        y_pred = X @ weights + bias
        
        # 计算损失（MSE + L2正则化）
        mse_loss = np.mean((y_pred - y)**2)
        reg_loss = l2_regularization_loss(weights, lambda_reg)
        total_loss = mse_loss + reg_loss
        loss_history.append(total_loss)
        
        # 反向传播
        grad_weights = (2/n_samples) * X.T @ (y_pred - y) + l2_regularization_gradient(weights, lambda_reg)
        grad_bias = (2/n_samples) * np.sum(y_pred - y)
        
        # 更新参数
        weights -= learning_rate * grad_weights
        bias -= learning_rate * grad_bias
    
    return weights, bias, loss_history

# 生成示例数据
np.random.seed(42)
X = np.random.randn(100, 3)
y = X @ np.array([1.0, 2.0, 3.0]) + 0.1 * np.random.randn(100)

# 训练
weights, bias, losses = train_with_regularization(X, y)

print(f"训练后的权重: {weights}")
print(f"训练后的偏置: {bias:.6f}")
print(f"最终损失: {losses[-1]:.6f}")
```

### 应用5：数值稳定性中的确界原理

在深度学习中，数值稳定性问题经常涉及确界原理的应用。

```python
import numpy as np

def stable_sigmoid(x):
    """数值稳定的sigmoid函数"""
    # 使用确界原理避免数值溢出
    x_clipped = np.clip(x, -500, 500)  # 限制在合理的范围内
    return 1.0 / (1.0 + np.exp(-x_clipped))

def stable_softmax(x):
    """数值稳定的softmax函数"""
    # 减去最大值以避免数值溢出
    x_max = np.max(x)
    exp_x = np.exp(x - x_max)
    return exp_x / np.sum(exp_x)

# 测试数值稳定性
x_large = np.array([1000, 2000, 3000])

print("大数值输入:")
print(f"x = {x_large}")

print(f"\n标准sigmoid: {1 / (1 + np.exp(-x_large))}")
print(f"稳定sigmoid: {stable_sigmoid(x_large)}")

print(f"\n标准softmax: {np.exp(x_large) / np.sum(np.exp(x_large))}")
print(f"稳定softmax: {stable_softmax(x_large)}")
```

## 5. 相关概念

- [[02_Limits]] - 极限
- [[03_Continuity]] - 连续性
- [[05_Derivatives]] - 导数
- [[../../01_Mathematics/Linear_Algebra/04_Eigenvalues_Eigenvectors]] - 特征值特征向量

## 10. 总结
### 10.1 重要定义
1. 实数集：满足域公理和完备性公理的有序域
2. 上确界和下确界：集合的最小上界和最大下界
3. 有理数与无理数：可表示和不可表示为整数之比的数
4. 邻域与开闭集：点的邻域、开集和闭集的定义
5. 绝对值：实数的绝对值及其性质

### 10.2 重要定理
1. 确界原理（完备性公理）：实数集的任何非空有上界的子集都有最小上界
2. 阿基米德性质：对于任意x>0，存在n使得nx>y
3. 有界单调序列定理：单调有界数列必收敛
4. 闭区间套定理：嵌套闭区间的交集非空且唯一
5. 致密性定理（Bolzano-Weierstrass）：有界数列必有收敛子列
6. 柯西收敛准则：数列收敛的充要条件
7. 有理数稠密性：有理数在实数中稠密

### 10.3 重要证明
1. 阿基米德性质的证明：使用反证法和确界原理
2. 有界单调序列定理的证明：利用确界原理构造极限值
3. 有理数稠密性的证明：利用阿基米德性质和取整函数

### 10.4 重要性质
1. 绝对值性质：非负性、齐次性、三角不等式、反向三角不等式
2. 重要不等式：AM-GM不等式、柯西-施瓦茨不等式、伯努利不等式
3. 开集与闭集性质：有限交、任意并等运算的保持性质
4. 确界性质：集合运算的确界关系

本章为后续学习相关章节奠定了基础。

## 11. 练习（分层）
本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 证明：Q在R中是稠密的（参考《数学分析(第5版) 上》第1章习题1-2第3题）
2. 计算：sup{x∈R|x²<2}和inf{x∈R|x²>2}（参考《高等数学 上册 第八版》第1章习题1-1第5题）
3. 证明：三角不等式：|x+y|≤|x|+|y|（参考《数学分析(第5版) 上》第1章习题1-3第1题）
4. 验证：柯西-施瓦茨不等式在二维情况下的等号成立条件（参考《高等数学 上册 第八版》第1章习题1-3第4题）
5. 构造：构造一个闭区间套序列，并计算其极限点（参考《数学分析(第5版) 上》第1章习题1-4第2题）

### B档（进阶）
1. 证明：单调递增且有上界的数列必收敛（参考《数学分析(第5版) 上》第1章定理1.5）
2. 证明：阿基米德性质（参考《数学分析(第5版) 上》第1章定理1.3）
3. 证明：√2是无理数（参考《数学分析(第1版) 上》第1章例1.2）
4. 利用确界原理证明闭区间套定理（参考《数学分析(第5版) 上》第1章习题1-4第5题）
5. 设{xn}和{yn}都是有界数列，证明：sup{xn+yn}≤sup{xn}+sup{yn}（参考《数学分析(第5版) 上》第1章习题1-2第8题）

### C档（挑战）
1. 证明：实数系R是不可数的（康托尔对角线法）（参考《数学分析(第5版) 上》第1章第6节）
2. 证明：对于任意x∈R，存在有理数序列{qn}，使得lim(qn)=x（参考《数学分析(第5版) 上》第1章定理1.6）
3. 证明：柯西收敛准则（参考《数学分析(第5版) 上》第1章定理1.8）
4. 研究康托尔集的性质，证明其是不可数的且测度为零（参考《数学分析(第5版) 下》第15章习题15-3第10题）
5. 在机器学习中，为什么需要数值稳定的函数？给出具体例子和解决方案（参考《高等数学 下册 第八版》第11章级数收敛性）




