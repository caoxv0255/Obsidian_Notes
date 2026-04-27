---
type: concept
topic: vector_calculus
category: calculus
difficulty: advanced
prerequisites:
    - [[19_Partial_Derivatives]]
    - [[22_Curve_Integrals]]
    - [[23_Surface_Integrals]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-03-09
status: complete
subject: calculus
chapter: 24
updated: 2026-04-27
---

# 向量微积分 (Vector Calculus)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解梯度、散度、旋度与拉普拉斯算子的定义和几何意义
- 掌握格林公式、高斯公式和斯托克斯公式之间的联系
- 会用向量微积分分析保守场、通量和环量问题

## 先修
- [[19_Partial_Derivatives]] - 偏导数与全微分
- [[22_Curve_Integrals]] - 曲线积分
- [[23_Surface_Integrals]] - 曲面积分
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：梯度、散度、旋度与拉普拉斯算子
- B档（进阶）：保守场判定与三大定理关系
- C档（挑战）：通量、环量、图神经网络与综合应用

## 自测（3问速测）
1. 梯度、散度和旋度分别把什么对象映射成什么对象？
2. 为什么保守场的曲线积分与路径无关？
3. 高斯公式和斯托克斯公式分别对应什么几何对象？

## 1. 定义

向量微积分研究向量场的微分和积分，包括梯度、散度、旋度以及它们之间的关系。

## 2. 定理与性质

### 1. 梯度（Gradient）

#### 定义

标量场 $f(x, y, z)$ 的梯度是向量场：

$$\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)$$

#### 性质

1. 梯度方向是函数增长最快的方向
2. 梯度的模长是函数在该方向上的最大增长率
3. 梯度垂直于等值面

**示例**：计算 $f(x, y, z) = x^2 + y^2 + z^2$ 的梯度。

**解**：
$$\nabla f = (2x, 2y, 2z) = 2(x, y, z)$$

### 2. 散度（Divergence）

#### 定义

向量场 $\mathbf{F} = (P, Q, R)$ 的散度是标量场：

$$\nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

#### 物理意义

散度描述向量场在某点的"源头"或"汇"的强度：
- $\nabla \cdot \mathbf{F} > 0$：该点是源（发散）
- $\nabla \cdot \mathbf{F} < 0$：该点是汇（收敛）
- $\nabla \cdot \mathbf{F} = 0$：该点无源无汇（无源场）

**示例**：计算 $\mathbf{F} = (x, y, z)$ 的散度。

**解**：
$$\nabla \cdot \mathbf{F} = 1 + 1 + 1 = 3$$

### 3. 旋度（Curl）

#### 定义

向量场 $\mathbf{F} = (P, Q, R)$ 的旋度是向量场：

$$\nabla \times \mathbf{F} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
P & Q & R
\end{vmatrix} = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}, \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}, \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)$$

#### 物理意义

旋度描述向量场的旋转强度：
- $\nabla \times \mathbf{F} = \mathbf{0}$：向量场是无旋场（保守场）
- $\nabla \times \mathbf{F} \neq \mathbf{0}$：向量场有旋转

**示例**：计算 $\mathbf{F} = (-y, x, 0)$ 的旋度。

**解**：
$$\nabla \times \mathbf{F} = \left(\frac{\partial 0}{\partial y} - \frac{\partial x}{\partial z}, \frac{\partial (-y)}{\partial z} - \frac{\partial 0}{\partial x}, \frac{\partial x}{\partial x} - \frac{\partial (-y)}{\partial y}\right) = (0, 0, 2)$$

### 4. 梯度、散度、旋度的关系

#### 恒等式

1. $\nabla \times (\nabla f) = \mathbf{0}$（梯度的旋度为零）
2. $\nabla \cdot (\nabla \times \mathbf{F}) = 0$（旋度的散度为零）

#### 保守场

**定义**：如果 $\nabla \times \mathbf{F} = \mathbf{0}$，则 $\mathbf{F}$ 是保守场，存在势函数 $\phi$ 使得 $\mathbf{F} = \nabla \phi$。

**性质**：
- 保守场的曲线积分与路径无关
- $\int_A^B \mathbf{F} \cdot d\mathbf{r} = \phi(B) - \phi(A)$
- $\oint_C \mathbf{F} \cdot d\mathbf{r} = 0$（闭路径积分为零）

### 5. 拉普拉斯算子

#### 定义

$$\nabla^2 f = \nabla \cdot (\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$

#### 应用

- 泊松方程：$\nabla^2 f = \rho$
- 拉普拉斯方程：$\nabla^2 f = 0$
- 热传导方程：$\frac{\partial u}{\partial t} = \alpha \nabla^2 u$
- 波动方程：$\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u$

### 6. 三个重要定理

#### 高斯公式（散度定理）

$$\oiint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V (\nabla \cdot \mathbf{F}) dV$$

**物理意义**：通过封闭曲面的通量等于体积内的散度积分。

#### 斯托克斯公式

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}$$

**物理意义**：沿闭合曲线的环量等于穿过该曲面的旋度通量。

#### 格林公式

$$\oint_C P dx + Q dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dx dy$$

**物理意义**：平面上的斯托克斯公式。

## 机器学习中的应用

### 1. 梯度下降

梯度下降的核心思想是沿着负梯度方向迭代：

$$\theta_{t+1} = \theta_t - \eta \nabla L(\theta_t)$$

### 2. 图神经网络

在图神经网络中，拉普拉斯算子用于捕捉图的拓扑结构：

$$\mathbf{L} = \mathbf{D} - \mathbf{A}$$

其中 $\mathbf{D}$ 是度矩阵，$\mathbf{A}$ 是邻接矩阵。

### 3. 流形学习

在流形学习中，需要计算流形的切空间、法向量等，这涉及梯度、Hessian矩阵等概念。

## 3. 代码示例

```python
import numpy as np

def gradient(f, point, h=1e-6):
    """数值计算梯度"""
    point = np.array(point, dtype=float)
    grad = np.zeros_like(point)

    for i in range(len(point)):
        point_plus = point.copy()
        point_plus[i] += h
        f_plus = f(*point_plus)

        point_minus = point.copy()
        point_minus[i] -= h
        f_minus = f(*point_minus)

        grad[i] = (f_plus - f_minus) / (2 * h)

    return grad

def divergence(F, point, h=1e-6):
    """数值计算散度"""
    point = np.array(point, dtype=float)
    n = len(point)
    div = 0

    for i in range(n):
        point_plus = point.copy()
        point_plus[i] += h
        F_plus = F(*point_plus)

        point_minus = point.copy()
        point_minus[i] -= h
        F_minus = F(*point_minus)

        div += (F_plus[i] - F_minus[i]) / (2 * h)

    return div

def curl(F, point, h=1e-6):
    """数值计算旋度（三维）"""
    point = np.array(point, dtype=float)
    x, y, z = point

    # 计算偏导数
    dR_dy = (F(x, y + h, z)[2] - F(x, y - h, z)[2]) / (2 * h)
    dQ_dz = (F(x, y, z + h)[1] - F(x, y, z - h)[1]) / (2 * h)
    dP_dz = (F(x, y, z + h)[0] - F(x, y, z - h)[0]) / (2 * h)
    dR_dx = (F(x + h, y, z)[2] - F(x - h, y, z)[2]) / (2 * h)
    dQ_dx = (F(x + h, y, z)[1] - F(x - h, y, z)[1]) / (2 * h)
    dP_dy = (F(x, y + h, z)[0] - F(x, y - h, z)[0]) / (2 * h)

    curl_x = dR_dy - dQ_dz
    curl_y = dP_dz - dR_dx
    curl_z = dQ_dx - dP_dy

    return np.array([curl_x, curl_y, curl_z])

# 示例
# 标量场 f(x, y, z) = x² + y² + z²
f = lambda x, y, z: x**2 + y**2 + z**2

# 向量场 F(x, y, z) = (x, y, z)
F = lambda x, y, z: np.array([x, y, z])

# 向量场 F(x, y, z) = (-y, x, 0)
F_rot = lambda x, y, z: np.array([-y, x, 0])

point = (1, 2, 3)

# 计算梯度
grad = gradient(f, point)
print(f"梯度 ∇f 在 {point}: {grad}")

# 计算散度
div = divergence(F, point)
print(f"散度 ∇·F 在 {point}: {div:.6f}")

# 计算旋度
curl = curl(F_rot, point)
print(f"旋度 ∇×F 在 {point}: {curl}")
```

## 总结
- 梯度描述标量场的最陡上升方向。
- 散度描述向量场的源汇强度，旋度描述局部旋转。
- 三大公式把曲线积分、曲面积分和体积分统一起来。

## 易错点
- 把梯度、散度和旋度的输出类型混淆
- 误把“旋度为零”直接当作“处处保守”而不检查区域条件
- 高斯公式和斯托克斯公式的曲面/边界对象搞反
- 忘记拉普拉斯算子是散度的梯度，不是旋度

## 根据题型整理的做题方法
### 向量微积分核心公式

**梯度**：$\nabla f = (\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z})$
- 标量场 → 向量场
- 指向增长最快的方向

**散度**：$\nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$
- 向量场 → 标量场
- 表示"源"或"汇"

**旋度**：$\nabla \times \mathbf{F} = (\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z}, \frac{\partial P}{\partial z}-\frac{\partial R}{\partial x}, \frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})$
- 向量场 → 向量场
- 表示旋转程度

**重要恒等式**：
- $\nabla \times (\nabla f) = \mathbf{0}$
- $\nabla \cdot (\nabla \times \mathbf{F}) = 0$
- $\nabla \cdot (\nabla f) = \Delta f$（拉普拉斯算子）

### 三大定理关系

| 定理 | 联系 |
|-----|------|
| 格林公式 | 平面上的斯托克斯公式 |
| 高斯公式 | 散度定理 |
| 斯托克斯公式 | 旋度定理 |

## 习题

### 基础题

1. 计算以下标量场的梯度：
   - $f(x, y, z) = x^2 y + y^2 z + z^2 x$
   - $f(x, y, z) = \sin(xy) + e^{yz}$

2. 计算以下向量场的散度和旋度：
   - $\mathbf{F} = (x^2, y^2, z^2)$
   - $\mathbf{F} = (yz, zx, xy)$

### 进阶题

3. 证明：$\nabla \times (\nabla f) = \mathbf{0}$

4. 证明：$\nabla \cdot (\nabla \times \mathbf{F}) = 0$

5. 利用高斯公式计算 $\oiint_S x dy dz + y dz dx + z dx dy$，其中 $S$ 是单位球面的外侧。

### 挑战题

6. 在机器学习中，为什么梯度下降算法收敛到局部极小值点？讨论鞍点、局部极小值点和全局极小值点的区别。

7. 研究图神经网络中的拉普拉斯矩阵，并说明它如何捕捉图的拓扑结构。

## 相关链接

- [[19_Partial_Derivatives]] - 偏导数（向量微积分的基础）
- [[22_Curve_Integrals]] - 曲线积分（向量微积分的应用）
- [[23_Surface_Integrals]] - 曲面积分（向量微积分的应用）
- [[../../01_Mathematics/Linear_Algebra/04_Eigenvalues_Eigenvectors]] - 特征值特征向量（拉普拉斯算子）
- [[02_Autograd]] - 自动微分（梯度的计算）



