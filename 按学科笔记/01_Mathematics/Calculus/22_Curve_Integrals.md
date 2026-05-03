---
type: concept
topic: curve_integrals
category: calculus
difficulty: advanced
prerequisites:
    - [[19_Partial_Derivatives]]
    - [[21_Multiple_Integrals]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-03-09
status: complete
subject: calculus
chapter: 22
updated: 2026-04-27
---

# 曲线积分 (Curve Integrals)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解第一类和第二类曲线积分的定义与几何意义
- 掌握曲线参数化、格林公式和保守场判断
- 会用曲线积分解决功、路径无关和环量问题

## 先修
- [[19_Partial_Derivatives]] - 偏导数与全微分
- [[21_Multiple_Integrals]] - 重积分
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：第一类曲线积分、第二类曲线积分的定义与计算
- B档（进阶）：参数化、格林公式与路径无关
- C档（挑战）：保守场、环量与综合建模

## 自测（3问速测）
1. 第一类和第二类曲线积分的区别是什么？
2. 什么时候可以用格林公式代替直接计算？
3. 如何判断一个向量场是否保守？

## 1. 定义

曲线积分是定积分的推广，积分路径是一条曲线而不是直线段。

## 2. 定理与性质

### 1. 第一类曲线积分（对弧长的积分）

#### 定义

函数 $f(x, y, z)$ 沿曲线 $C$ 的第一类曲线积分：

$$\int_C f(x, y, z) ds$$

其中 $ds$ 是弧长元素。

#### 计算方法

如果曲线 $C$ 的参数方程为 $\mathbf{r}(t) = (x(t), y(t), z(t))$，$t \in [a, b]$，则：

$$\int_C f(x, y, z) ds = \int_a^b f(x(t), y(t), z(t)) \sqrt{[x'(t)]^2 + [y'(t)]^2 + [z'(t)]^2} dt$$

**示例**：计算 $\int_C (x + y) ds$，其中 $C$ 是从 $(0, 0)$ 到 $(1, 1)$ 的直线段。

**解**：
曲线参数方程：$x = t$, $y = t$, $t \in [0, 1]$

$$ds = \sqrt{1^2 + 1^2} dt = \sqrt{2} dt$$

$$\int_C (x + y) ds = \int_0^1 (t + t) \sqrt{2} dt = 2\sqrt{2} \int_0^1 t dt = 2\sqrt{2} \cdot \frac{1}{2} = \sqrt{2}$$

### 2. 第二类曲线积分（对坐标的积分）

#### 定义

向量场 $\mathbf{F} = (P, Q, R)$ 沿曲线 $C$ 的第二类曲线积分：

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C P dx + Q dy + R dz$$

#### 计算方法

如果曲线 $C$ 的参数方程为 $\mathbf{r}(t) = (x(t), y(t), z(t))$，$t \in [a, b]$，则：

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b [P(x(t), y(t), z(t)) x'(t) + Q(x(t), y(t), z(t)) y'(t) + R(x(t), y(t), z(t)) z'(t)] dt$$

**示例**：计算 $\int_C y dx + x dy$，其中 $C$ 是从 $(0, 0)$ 到 $(1, 1)$ 的直线段。

**解**：
曲线参数方程：$x = t$, $y = t$, $t \in [0, 1]$

$$\int_C y dx + x dy = \int_0^1 [t \cdot 1 + t \cdot 1] dt = \int_0^1 2t dt = 1$$

### 3. 格林公式

#### 定理

设 $D$ 是平面上的有界闭区域，边界 $C$ 是分段光滑的正向曲线，$P$ 和 $Q$ 在 $D$ 上有连续的一阶偏导数，则：

$$\oint_C P dx + Q dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dx dy$$

**示例**：利用格林公式计算 $\oint_C (x^2 + y) dx + (x - y^2) dy$，其中 $C$ 是单位圆的正向。

**解**：
$$\frac{\partial Q}{\partial x} = 1$$
$$\frac{\partial P}{\partial y} = 1$$

因此：
$$\oint_C (x^2 + y) dx + (x - y^2) dy = \iint_D (1 - 1) dx dy = 0$$

## 机器学习中的应用

### 1. 路径规划

在机器人路径规划中，需要计算路径上的积分，如能量消耗、时间等。

### 2. 梯度下降

梯度下降可以看作是沿着负梯度方向的曲线积分。

## 3. 代码示例

```python
import numpy as np
from scipy.integrate import quad

# 示例1：第一类曲线积分
def first_type_curve_integral(f, r_func, dr_func, a, b):
    """
    计算第一类曲线积分

    参数:
        f: 被积函数 f(x, y, z)
        r_func: 曲线参数方程 r(t) = (x(t), y(t), z(t))
        dr_func: 导数 r'(t) = (x'(t), y'(t), z'(t))
        a: 参数下限
        b: 参数上限

    返回:
        integral: 曲线积分值
    """
    def integrand(t):
        x, y, z = r_func(t)
        dx, dy, dz = dr_func(t)
        ds = np.sqrt(dx**2 + dy**2 + dz**2)
        return f(x, y, z) * ds

    integral, _ = quad(integrand, a, b)
    return integral

# 示例2：第二类曲线积分
def second_type_curve_integral(F, r_func, dr_func, a, b):
    """
    计算第二类曲线积分

    参数:
        F: 向量场 F = (P, Q, R)
        r_func: 曲线参数方程 r(t) = (x(t), y(t), z(t))
        dr_func: 导数 r'(t) = (x'(t), y'(t), z'(t))
        a: 参数下限
        b: 参数上限

    返回:
        integral: 曲线积分值
    """
    def integrand(t):
        x, y, z = r_func(t)
        dx, dy, dz = dr_func(t)
        P, Q, R = F(x, y, z)
        return P * dx + Q * dy + R * dz

    integral, _ = quad(integrand, a, b)
    return integral

# 使用示例
# f(x, y) = x + y
f = lambda x, y, z: x + y

# 曲线：从(0,0)到(1,1)的直线段
r_func = lambda t: (t, t, 0)
dr_func = lambda t: (1, 1, 0)

result1 = first_type_curve_integral(f, r_func, dr_func, 0, 1)
print(f"第一类曲线积分: {result1:.6f} (理论值: √2 ≈ {np.sqrt(2):.6f})")

# 向量场 F = (y, x, 0)
F = lambda x, y, z: (y, x, 0)

result2 = second_type_curve_integral(F, r_func, dr_func, 0, 1)
print(f"第二类曲线积分: {result2:.6f} (理论值: 1)")
```

## 习题

### 基础题

1. 计算以下第一类曲线积分：
   - $\int_C x ds$，其中 $C$ 是圆 $x^2 + y^2 = R^2$
   - $\int_C (x + y^2) ds$，其中 $C$ 是从 $(0, 0)$ 到 $(1, 1)$ 的直线段

2. 计算以下第二类曲线积分：
   - $\int_C y dx + x dy$，其中 $C$ 是椭圆 $x = a\cos t$, $y = b\sin t$，$t \in [0, 2\pi]$

### 进阶题

3. 利用格林公式计算 $\oint_C (x^2 - y) dx + (x + y^2) dy$，其中 $C$ 是单位圆的正向。

4. 证明：如果 $\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}$，则 $\oint_C P dx + Q dy = 0$（保守场）。

## 根据题型整理的做题方法
### 曲线积分核心要点

**第一类曲线积分（对弧长）**：
- 无方向性
- 公式：$\int_C f ds = \int_a^b f(x(t),y(t),z(t))\sqrt{x'^2+y'^2+z'^2}dt$

**第二类曲线积分（对坐标）**：
- 有方向性，方向相反变号
- 公式：$\int_C Pdx+Qdy+Rdz = \int_a^b [Px'+Qy'+Rz']dt$

**格林公式**：
$$\oint_C Pdx+Qdy = \iint_D (\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})dxdy$$

**保守场判断**：
$\frac{\partial Q}{\partial x}=\frac{\partial P}{\partial y}$ ⟹ 积分与路径无关

### 常用技巧
- 第一类积分：参数化曲线，代入弧长公式
- 第二类积分：参数化或用格林公式
- 封闭曲线：优先考虑格林公式

## 相关链接

- [[21_Multiple_Integrals]] - 重积分（曲线积分的基础）
- [[23_Surface_Integrals]] - 曲面积分（曲线积分的推广）
- [[23_Vector_Calculus]] - 向量微积分（曲线积分的应用）
- [[06_Case_Finance]] - 金融案例（路径规划的应用）



