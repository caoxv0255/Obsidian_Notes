---
type: concept
topic: surface_integrals
category: calculus
difficulty: advanced
prerequisites:
    - [[19_Partial_Derivatives]]
    - [[21_Multiple_Integrals]]
    - [[22_Curve_Integrals]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-03-09
status: complete
subject: calculus
chapter: 23
updated: 2026-04-27
---

# 曲面积分 (Surface Integrals)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解第一类和第二类曲面积分的定义与几何意义
- 掌握曲面参数化、法向量与高斯公式
- 会用曲面积分处理面积、通量和散度定理问题

## 先修
- [[19_Partial_Derivatives]] - 偏导数与全微分
- [[21_Multiple_Integrals]] - 重积分
- [[22_Curve_Integrals]] - 曲线积分
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：第一类曲面积分、第二类曲面积分的定义与计算
- B档（进阶）：参数化曲面、高斯公式与通量
- C档（挑战）：斯托克斯公式、散度定理与综合应用

## 自测（3问速测）
1. 第一类和第二类曲面积分的区别是什么？
2. 高斯公式适用于什么类型的曲面？
3. 什么时候应该用参数化来计算曲面积分？

## 1. 定义

曲面积分是二重积分的推广，积分区域是一个曲面而不是平面区域。

## 2. 定理与性质

### 1. 第一类曲面积分（对面积的积分）

#### 定义

函数 $f(x, y, z)$ 沿曲面 $S$ 的第一类曲面积分：

$$\iint_S f(x, y, z) dS$$

其中 $dS$ 是面积元素。

#### 计算方法

如果曲面 $S$ 的参数方程为 $\mathbf{r}(u, v) = (x(u, v), y(u, v), z(u, v))$，$(u, v) \in D$，则：

$$\iint_S f(x, y, z) dS = \iint_D f(x(u, v), y(u, v), z(u, v)) \|\mathbf{r}_u \times \mathbf{r}_v\| du dv$$

其中 $\mathbf{r}_u = \frac{\partial \mathbf{r}}{\partial u}$，$\mathbf{r}_v = \frac{\partial \mathbf{r}}{\partial v}$。

**示例**：计算 $\iint_S (x + y + z) dS$，其中 $S$ 是平面 $x + y + z = 1$ 在第一象限的部分。

**解**：
曲面参数方程：$z = 1 - x - y$，$(x, y) \in D$，其中 $D = \{(x, y) | x \geq 0, y \geq 0, x + y \leq 1\}$

$$dS = \sqrt{1 + \left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2} dx dy = \sqrt{3} dx dy$$

$$\iint_S (x + y + z) dS = \iint_D (x + y + 1 - x - y) \sqrt{3} dx dy = \sqrt{3} \iint_D 1 dx dy$$

由于 $D$ 是直角三角形，面积为 $\frac{1}{2}$，故：
$$\iint_S (x + y + z) dS = \frac{\sqrt{3}}{2}$$

### 2. 第二类曲面积分（对坐标的积分）

#### 定义

向量场 $\mathbf{F} = (P, Q, R)$ 沿曲面 $S$ 的第二类曲面积分：

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_S P dy dz + Q dz dx + R dx dy$$

#### 计算方法

如果曲面 $S$ 的参数方程为 $\mathbf{r}(u, v) = (x(u, v), y(u, v), z(u, v))$，$(u, v) \in D$，则：

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_D \mathbf{F}(\mathbf{r}(u, v)) \cdot (\mathbf{r}_u \times \mathbf{r}_v) du dv$$

### 3. 高斯公式（散度定理）

#### 定理

设 $V$ 是空间中的有界闭区域，边界 $S$ 是分段光滑的封闭曲面，$\mathbf{F}$ 在 $V$ 上有连续的一阶偏导数，则：

$$\oiint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V (\nabla \cdot \mathbf{F}) dV$$

其中 $\nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$ 是散度。

**示例**：计算 $\oiint_S x dy dz + y dz dx + z dx dy$，其中 $S$ 是单位球面的外侧。

**解**：
设 $\mathbf{F} = (x, y, z)$，则：
$$\nabla \cdot \mathbf{F} = 1 + 1 + 1 = 3$$

由高斯公式：
$$\oiint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V 3 dV = 3 \cdot \frac{4\pi}{3} = 4\pi$$

### 4. 斯托克斯公式

#### 定理

设 $S$ 是有向光滑曲面，边界 $C$ 是分段光滑的闭曲线，$\mathbf{F}$ 在 $S$ 上有连续的一阶偏导数，则：

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}$$

其中 $\nabla \times \mathbf{F}$ 是旋度。

## 机器学习中的应用

### 1. 流形学习

在流形学习中，需要计算流形上的积分，如测地线距离、曲率等。

### 2. 计算机视觉

在计算机视觉中，曲面积分用于计算表面积、法向量等。

## 3. 代码示例

```python
import numpy as np
from scipy.integrate import dblquad

# 示例1：第一类曲面积分
def first_type_surface_integral(f, r_func, ru_func, rv_func, u_range, v_range):
    """
    计算第一类曲面积分

    参数:
        f: 被积函数 f(x, y, z)
        r_func: 曲面参数方程 r(u, v) = (x(u, v), y(u, v), z(u, v))
        ru_func: 偏导数 ∂r/∂u
        rv_func: 偏导数 ∂r/∂v
        u_range: u的范围 [a, b]
        v_range: v的范围 [c, d]

    返回:
        integral: 曲面积分值
    """
    def integrand(u, v):
        x, y, z = r_func(u, v)
        ru = ru_func(u, v)
        rv = rv_func(u, v)

        # 计算叉积的范长
        cross = np.cross(ru, rv)
        dS = np.linalg.norm(cross)

        return f(x, y, z) * dS

    integral, _ = dblquad(integrand, u_range[0], u_range[1],
                          lambda u: v_range[0], lambda u: v_range[1])
    return integral

# 示例：计算单位上半球的面积
def hemisphere_r(u, v):
    """上半球面的参数方程"""
    r = 1
    x = r * np.sin(u) * np.cos(v)
    y = r * np.sin(u) * np.sin(v)
    z = r * np.cos(u)
    return (x, y, z)

def hemisphere_ru(u, v):
    """∂r/∂u"""
    r = 1
    dx = r * np.cos(u) * np.cos(v)
    dy = r * np.cos(u) * np.sin(v)
    dz = -r * np.sin(u)
    return (dx, dy, dz)

def hemisphere_rv(u, v):
    """∂r/∂v"""
    r = 1
    dx = -r * np.sin(u) * np.sin(v)
    dy = r * np.sin(u) * np.cos(v)
    dz = 0
    return (dx, dy, dz)

f = lambda x, y, z: 1  # 计算面积，被积函数为1

# 上半球：u ∈ [0, π/2], v ∈ [0, 2π]
area = first_type_surface_integral(f, hemisphere_r, hemisphere_ru, hemisphere_rv,
                                     [0, np.pi/2], [0, 2*np.pi])

print(f"上半球面积: {area:.6f}")
print(f"理论值: 2π ≈ {2*np.pi:.6f}")
```

## 习题

### 基础题

1. 计算以下第一类曲面积分：
   - $\iint_S (x + y + z) dS$，其中 $S$ 是平面 $x + y + z = 1$ 在第一象限的部分
   - $\iint_S z dS$，其中 $S$ 是上半球面 $x^2 + y^2 + z^2 = R^2$, $z \geq 0$

2. 计算以下第二类曲面积分：
   - $\oiint_S x dy dz + y dz dx + z dx dy$，其中 $S$ 是单位球面的外侧

### 进阶题

3. 利用高斯公式计算 $\oiint_S x^2 dy dz + y^2 dz dx + z^2 dx dy$，其中 $S$ 是单位球面的外侧。

4. 证明：如果 $\nabla \cdot \mathbf{F} = 0$，则 $\oiint_S \mathbf{F} \cdot d\mathbf{S} = 0$（无源场）。

## 根据题型整理的做题方法
### 曲面积分核心要点

**第一类曲面积分（对面积）**：
- 无方向性
- 公式：$\iint_S f dS = \iint_D f(x,y,z)\|\mathbf{r}_u\times\mathbf{r}_v\|dudv$

**第二类曲面积分（对坐标）**：
- 有方向性（指定侧）
- 公式：$\iint_S \mathbf{F}\cdot d\mathbf{S} = \iint_D \mathbf{F}\cdot(\mathbf{r}_u\times\mathbf{r}_v)dudv$

**高斯公式**：
$$\oiint_S \mathbf{F}\cdot d\mathbf{S} = \iiint_V (\nabla\cdot\mathbf{F})dV$$

**斯托克斯公式**：
$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S (\nabla\times\mathbf{F})\cdot d\mathbf{S}$$

### 常用技巧
- 封闭曲面：优先考虑高斯公式
- 曲线积分与曲面积分关系：斯托克斯公式
- 计算面积：被积函数取1

## 相关链接

- [[21_Multiple_Integrals]] - 重积分（曲面积分的基础）
- [[22_Curve_Integrals]] - 曲线积分（曲面积分的特例）
- [[23_Vector_Calculus]] - 向量微积分（曲面积分的应用）
- [[07_Case_Image]] - 图像案例（曲面积分的应用）



