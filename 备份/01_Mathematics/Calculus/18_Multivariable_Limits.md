---
type: concept
topic: multivariable_limits
category: calculus
difficulty: advanced
prerequisites:
    - [[01_Real_Numbers]]
    - [[02_Limits]]
    - [[03_Continuity]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-03-09
status: complete
subject: calculus
chapter: 18
updated: 2026-04-27
---

# 多元函数极限与连续 (Multivariable Limits and Continuity)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 熟悉欧式空间、邻域与开闭集等点集概念
- 理解多元函数极限存在的判定思路与路径法
- 掌握多元函数连续性的定义和基本性质，并理解有界闭域上的最值性质
- 会用极坐标、夹逼和反例判断多元极限是否存在，并理解累次极限与二重极限的区别

## 先修
- [[01_Real_Numbers]] - 实数理论
- [[02_Limits]] - 极限
- [[03_Continuity]] - 连续性
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：多元极限定义、路径法与连续性
- B档（进阶）：极坐标法、夹逼定理与累次极限
- C档（挑战）：路径构造、连续性证明与综合反例

## 自测（3问速测）
1. 为什么多元函数极限要检查不同路径？
2. 二重极限存在时，所有方向极限都必须相同吗？
3. 什么时候可以直接用连续函数的复合性质判断极限？

## 1. 定义

多元函数的极限和连续是一元情况的推广，但更加复杂，因为趋近路径有无穷多条。

### 0. 欧式空间与点集

多元微积分通常在欧式空间 $\mathbb{R}^n$ 中讨论，采用欧式距离
$$
d(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|
$$
来描述“接近”。

对集合 $E \subset \mathbb{R}^n$：
- **内点**：某个邻域完全包含于 $E$
- **外点**：某个邻域与 $E$ 无交
- **聚点**：任意去心邻域都与 $E$ 有交
- **开集**：每个点都是内点的集合
- **闭集**：补集是开集的集合
- **开区域/闭区域**：多元微积分中常把开集/闭集视作区域时的称呼

在 $\mathbb{R}^n$ 中，闭有界集是紧集，因此连续函数在其上一定有界，并能取到最大值和最小值。

## 2. 定理与性质

### 1. 多元函数的极限

#### 定义

函数 $f: \mathbb{R}^n \to \mathbb{R}$ 在点 $\mathbf{a} = (a_1, a_2, \ldots, a_n)$ 处的极限为 $L$，记作：

$$\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = L$$

如果对于任意 $\varepsilon > 0$，存在 $\delta > 0$，使得当 $0 < \|\mathbf{x} - \mathbf{a}\| < \delta$ 时，有 $|f(\mathbf{x}) - L| < \varepsilon$。

#### 极限存在的条件

**重要**：多元函数极限存在的关键条件是：**无论以何种路径趋近 $\mathbf{a}$，函数值都必须趋近同一个值**。

**示例**：判断 $\lim_{(x,y) \to (0,0)} \frac{xy}{x^2 + y^2}$ 是否存在。

**解**：
- 沿 $x$ 轴趋近（$y = 0$）：$\lim_{x \to 0} \frac{x \cdot 0}{x^2 + 0} = 0$
- 沿 $y$ 轴趋近（$x = 0$）：$\lim_{y \to 0} \frac{0 \cdot y}{0 + y^2} = 0$
- 沿 $y = x$ 趋近：$\lim_{x \to 0} \frac{x \cdot x}{x^2 + x^2} = \lim_{x \to 0} \frac{x^2}{2x^2} = \frac{1}{2}$

由于沿不同路径趋近得到不同的值，极限不存在！

### 1.1 累次极限

**定义**：先固定一个变量取极限，再对另一个变量取极限，称为累次极限。

例如，若内层极限存在，则可写作
$$
\lim_{y \to b}\left(\lim_{x \to a} f(x,y)\right)
$$

**重要提醒**：累次极限存在，不代表二重极限一定存在。

**典型反例**：
$$
f(x,y)=\frac{xy}{x^2+y^2}
$$
沿 $x \to 0$ 先取极限，再令 $y \to 0$，以及反过来，累次极限都为 $0$；但二重极限不存在，因为沿 $y=x$ 的路径极限为 $\frac12$。

### 2. 多元函数的连续性

#### 定义

函数 $f: \mathbb{R}^n \to \mathbb{R}$ 在点 $\mathbf{a}$ 处连续，如果：

1. $f(\mathbf{a})$ 存在（$\mathbf{a}$ 在定义域内）
2. $\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x})$ 存在
3. $\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})$

#### 连续函数的性质

1. 连续函数的和、差、积、商（分母不为零）是连续的
2. 连续函数的复合函数是连续的
3. 多项式函数、有理函数、指数函数、对数函数、三角函数在其定义域内连续

### 3. 有界闭域上的性质

若 $f$ 在有界闭域 $D \subset \mathbb{R}^n$ 上连续，则：
- $f$ 在 $D$ 上有界
- $f$ 在 $D$ 上能取到最大值与最小值

**用法**：先确认定义域是闭且有界，再利用连续性得到最值存在；随后再找极值点或边界值。

## 机器学习中的应用

### 1. 损失函数的连续性

在机器学习中，损失函数的连续性对优化算法至关重要。

**例子**：Huber损失函数

$$L_{\delta}(y, \hat{y}) = \begin{cases}
\frac{1}{2}(y - \hat{y})^2, & |y - \hat{y}| \leq \delta \\
\delta(|y - \hat{y}| - \frac{1}{2}\delta), & |y - \hat{y}| > \delta
\end{cases}$$

这个函数处处连续，且在 $|y - \hat{y}| = \delta$ 处可导。

### 2. 激活函数的连续性

激活函数的连续性保证了梯度下降的稳定性。

## 3. 代码示例

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def check_multivariable_limit(f, paths, target_point):
    """
    检查多元函数沿不同路径的极限

    参数:
        f: 多元函数
        paths: 路径列表
        target_point: 目标点

    返回:
        results: 每条路径的极限值
    """
    results = []
    for path_func in paths:
        # 沿路径趋近
        t_values = np.logspace(-6, -1, 10)
        values = []
        for t in t_values:
            x, y = path_func(t)
            values.append(f(x, y))
        results.append(values[-1])  # 取最后一个值作为近似极限
    return results

# 示例：检查 f(x,y) = xy/(x² + y²) 在 (0,0) 处的极限
f = lambda x, y: (x * y) / (x**2 + y**2) if (x, y) != (0, 0) else 0

# 定义不同路径
paths = [
    lambda t: (t, 0),           # 沿x轴
    lambda t: (0, t),           # 沿y轴
    lambda t: (t, t),           # 沿y = x
    lambda t: (t, t**2),        # 沿y = x²
    lambda t: (t, np.sin(t)),   # 沿y = sin(x)
]

results = check_multivariable_limit(f, paths, (0, 0))

print("沿不同路径的极限值:")
for i, result in enumerate(results):
    print(f"路径{i+1}: {result:.6f}")

print("\n由于极限值不相等，极限不存在！")
```

## 习题

### 基础题

1. 判断以下极限是否存在：
   - $\lim_{(x,y) \to (0,0)} \frac{x^2 y}{x^2 + y^2}$
   - $\lim_{(x,y) \to (0,0)} \frac{x y^2}{x^2 + y^4}$

2. 证明：$\lim_{(x,y) \to (0,0)} \frac{x^3 + y^3}{x + y} = 0$。

### 进阶题

3. 证明：如果 $f: \mathbb{R}^2 \to \mathbb{R}$ 在 $(a, b)$ 处连续，则对于任意路径 $\gamma(t)$，$\lim_{t \to 0} f(\gamma(t)) = f(a, b)$。

4. 构造一个在 $\mathbb{R}^2$ 上处处不连续的函数。

## 相关链接

- [[02_Limits]] - 极限（多元极限的基础）
- [[03_Continuity]] - 连续性（多元连续的基础）
- [[18_Partial_Derivatives]] - 偏导数（多元微分的开始）
- [[../../01_Mathematics/Optimization/01_Gradient_Descent]] - 梯度下降（连续性的应用）
## 根据题型整理的做题方法
### 多元极限判断方法

**证明极限存在**：
- 用定义（$\varepsilon$-$\delta$）
- 用夹逼准则
- 用极坐标变换（注意需对所有方向成立）

**证明极限不存在**：
- 找两条不同路径使极限值不同
- 常用路径：$y=kx$，$y=x^2$，$y=mx^n$等

**连续性判断**：
- 分段函数在分界点需单独讨论
- 初等函数在其定义域内连续

**关键技巧**：
- 二元极限要求"任意方式"趋近
- 常用$|x|, |y| \leq \sqrt{x^2+y^2}$放缩

## 10. 总结
### 10.1 重要定义
1. 二元函数：$z = f(x, y)$ 定义的从 $\mathbb{R}^2$ 到 $\mathbb{R}$ 的映射
2. 多元极限：$\lim_{(x,y) \to (a,b)} f(x,y) = L$
3. 累次极限：先 $x \to a$ 再 $y \to b$ 或反之的极限
4. 方向极限：沿特定方向的极限

### 10.2 重要定理
1. 极限的唯一性：多元极限若存在则唯一
2. 夹逼定理：多元函数的夹逼准则
3. 极坐标极限：利用极坐标判断二元极限
4. 累次极限与二重极限的关系

### 10.3 重要证明
1. 极限唯一性的证明：类似一元函数
2. 极坐标方法的证明：利用坐标变换

### 10.4 重要性质
1. 多元极限比一元极限更复杂
2. 路径相关性：不同路径可能得到不同极限
3. 累次极限存在不一定二重极限存在
4. 二元极限存在则所有方向极限相同

## 根据题型整理的做题方法
### 多元极限四步法
1. 先检查代入是否直接得到确定值。
2. 若形式不定，优先尝试不同路径或极坐标。
3. 若能夹住，则用夹逼定理。
4. 若极限不存在，尽量构造两条给出不同值的路径。

## 易错点
- 只检查一条路径就下结论
- 把累次极限存在误当成二重极限存在
- 极坐标替换后忘记同步处理 $r$ 与 $\theta$
- 代入得到 $0/0$ 时不继续分析

## 11. 练习（分层）
本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 判断极限 $\lim_{(x,y)\to(0,0)} \frac{x^2y}{x^2+y^2}$ 是否存在。
2. 判断极限 $\lim_{(x,y)\to(0,0)} \frac{xy^2}{x^2+y^4}$ 是否存在。
3. 证明 $\lim_{(x,y)\to(0,0)} \frac{x^3+y^3}{x+y}=0$。
4. 证明函数 $f(x,y)=x^2+y^2$ 在 $(0,0)$ 处连续。

### B档（进阶）
1. 用极坐标法判断 $\lim_{(x,y)\to(0,0)} \frac{x^2y}{x^2+y^2}$ 是否存在。
2. 比较沿 $y=mx$、$y=x^2$ 和 $x=0$ 三条路径的极限值。
3. 证明：若 $f$ 连续且 $g$ 连续，则 $f\circ g$ 连续。
4. 研究 $\lim_{(x,y)\to(0,0)} \frac{x^2-y^2}{x^2+y^2}$ 的路径依赖性。

### C档（挑战）
1. 构造一个多元函数，使其在原点沿所有直线路径的极限都存在，但二重极限不存在。
2. 证明：若 $f(x,y)$ 在 $(0,0)$ 附近可表示为 $r^k\phi(\theta)$，则可据此判断极限。
3. 研究极坐标法在判断 $\lim_{(x,y)\to(0,0)} \frac{x^m y^n}{x^2+y^2}$ 时的普适性。
4. 证明多元极限存在时，函数在该点的连续性与一元情形完全一致。



