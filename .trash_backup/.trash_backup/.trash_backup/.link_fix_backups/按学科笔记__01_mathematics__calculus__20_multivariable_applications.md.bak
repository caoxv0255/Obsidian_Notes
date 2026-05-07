---
type: concept
topic: multivariable_applications
category: calculus
difficulty: advanced
prerequisites:
    - [[19_Partial_Derivatives]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-03-09
status: complete
subject: calculus
chapter: 20
updated: 2026-04-27
---

# 多元函数应用 (Multivariable Applications)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解多元函数极值、条件极值和约束优化的基本思路
- 掌握 Hessian 判别法、拉格朗日乘数法和反函数/隐函数定理的应用
- 会把几何、优化和机器学习中的问题转化为多元函数分析
- 会求有界闭域上的连续函数的最值点

## 先修
- [[19_Partial_Derivatives]] - 偏导数与全微分
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：驻点、Hessian 判别和无条件极值
- B档（进阶）：拉格朗日乘数法、条件极值与最值
- C档（挑战）：反函数定理、隐函数定理与优化综合题

## 自测（3问速测）
1. 多元函数极值点的必要条件是什么？
2. Hessian 正定、负定和不定分别对应什么结论？
3. 拉格朗日乘数法什么时候适合使用？

## 1. 定义

多元函数的应用广泛，包括极值问题、拉格朗日乘数法、条件极值、最优化等。

## 2. 定理与性质

### 1. 多元函数的极值

#### 极值的定义

函数 $f: \mathbb{R}^n \to \mathbb{R}$ 在点 $\mathbf{a}$ 处取得局部极大值（极小值），如果存在 $\delta > 0$，使得对所有 $\|\mathbf{x} - \mathbf{a}\| < \delta$，有 $f(\mathbf{x}) \leq f(\mathbf{a})$（或 $f(\mathbf{x}) \geq f(\mathbf{a})$）。

#### 极值的必要条件

**定理**：如果 $f$ 在 $\mathbf{a}$ 处可导且 $\mathbf{a}$ 是极值点，则 $\nabla f(\mathbf{a}) = \mathbf{0}$。

#### 极值的充分条件

设 $f$ 在 $\mathbf{a}$ 处二阶可导且 $\nabla f(\mathbf{a}) = \mathbf{0}$。令 $H(\mathbf{a})$ 为 Hessian 矩阵：

$$H(\mathbf{a}) = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}$$

**判断**：
- 如果 $H(\mathbf{a})$ 正定，则 $\mathbf{a}$ 是局部极小值点
- 如果 $H(\mathbf{a})$ 负定，则 $\mathbf{a}$ 是局部极大值点
- 如果 $H(\mathbf{a})$ 不定，则 $\mathbf{a}$ 是鞍点

**示例**：求 $f(x, y) = x^2 + y^2 - 4x - 6y$ 的极值。

**解**：
$$\frac{\partial f}{\partial x} = 2x - 4 = 0 \implies x = 2$$
$$\frac{\partial f}{\partial y} = 2y - 6 = 0 \implies y = 3$$

因此临界点为 $(2, 3)$。

Hessian 矩阵：
$$H = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$$

特征值为 $2, 2 > 0$，故 $H$ 正定，$(2, 3)$ 是局部极小值点。

$f(2, 3) = 4 + 9 - 8 - 18 = -13$

### 1.1 有界闭域上的最值点

若 $f$ 在有界闭域 $D$ 上连续，则 $f$ 在 $D$ 上必能取到最大值和最小值。

**求法**：
1. 先找域内驻点
2. 再检查边界上的候选点
3. 比较所有候选点的函数值

**典型思路**：
- 边界是光滑曲线时，常用参数化或拉格朗日乘数法
- 边界是线段或矩形时，常化为一元函数逐边检查

**示例**：对闭圆盘 $x^2 + y^2 \le 1$ 上的 $f(x,y)=x^2+y^2$，
- 内部驻点为 $(0,0)$，取到最小值 $0$
- 边界 $x^2+y^2=1$ 上取到最大值 $1$

因此最小值点为 $(0,0)$，最大值点为圆周上的任一点。

### 2. 拉格朗日乘数法

#### 问题陈述

在约束条件 $g(\mathbf{x}) = 0$ 下，求 $f(\mathbf{x})$ 的极值。

#### 方法

构造拉格朗日函数：
$$\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) - \lambda g(\mathbf{x})$$

求解方程组：
$$\nabla \mathcal{L} = \mathbf{0} \implies \begin{cases} \nabla f(\mathbf{x}) - \lambda \nabla g(\mathbf{x}) = \mathbf{0} \\ g(\mathbf{x}) = 0 \end{cases}$$

**示例**：在 $x^2 + y^2 = 1$ 的约束下，求 $f(x, y) = x + y$ 的极值。

**解**：
构造拉格朗日函数：
$$\mathcal{L}(x, y, \lambda) = x + y - \lambda(x^2 + y^2 - 1)$$

求解：
$$\frac{\partial \mathcal{L}}{\partial x} = 1 - 2\lambda x = 0 \implies x = \frac{1}{2\lambda}$$
$$\frac{\partial \mathcal{L}}{\partial y} = 1 - 2\lambda y = 0 \implies y = \frac{1}{2\lambda}$$
$$\frac{\partial \mathcal{L}}{\partial \lambda} = -(x^2 + y^2 - 1) = 0$$

代入约束条件：
$$\left(\frac{1}{2\lambda}\right)^2 + \left(\frac{1}{2\lambda}\right)^2 = 1 \implies \frac{2}{4\lambda^2} = 1 \implies \lambda = \pm \frac{1}{\sqrt{2}}$$

因此：
- 当 $\lambda = \frac{1}{\sqrt{2}}$ 时，$(x, y) = \left(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)$，$f = \sqrt{2}$（最大值）
- 当 $\lambda = -\frac{1}{\sqrt{2}}$ 时，$(x, y) = \left(-\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}\right)$，$f = -\sqrt{2}$（最小值）

### 3. 反函数定理 (Inverse Function Theorem)

#### 定理陈述

**定理**：设 $F: \mathbb{R}^n \to \mathbb{R}^n$ 在点 $\mathbf{a}$ 附近连续可微（$C^1$），且雅可比矩阵 $J_F(\mathbf{a})$ 可逆（即 $\det J_F(\mathbf{a}) \neq 0$），则：

1. 存在 $\mathbf{a}$ 的邻域 $U$ 和 $F(\mathbf{a})$ 的邻域 $V$，使得 $F: U \to V$ 是双射
2. 反函数 $F^{-1}: V \to U$ 存在且连续可微
3. 反函数的导数为：$J_{F^{-1}}(F(\mathbf{a})) = [J_F(\mathbf{a})]^{-1}$

**直观理解**：
- 可微函数在局部可逆，条件是导数矩阵可逆
- 反函数的导数是原函数导数的逆矩阵
- 这是将局部线性化推广到全局的桥梁

**证明思路**：
1. 利用压缩映射原理
2. 构造迭代序列逼近反函数
3. 证明反函数的存在性和可微性

#### 应用示例

**例1**：极坐标变换的可逆性

设 $F(r, \theta) = (r\cos\theta, r\sin\theta)$，雅可比矩阵为：

$$J_F = \begin{bmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{bmatrix}$$

行列式：$\det J_F = r(\cos^2\theta + \sin^2\theta) = r$

因此，当 $r \neq 0$ 时，极坐标变换局部可逆。

**例2**：神经网络中的坐标变换

在深度学习中，网络层可以看作 $\mathbf{y} = F(\mathbf{x})$。如果雅可比矩阵可逆，则信息在局部可逆，这对流模型（Normalizing Flows）至关重要。

### 4. 隐函数定理 (Implicit Function Theorem)

#### 定理陈述

**定理**：设 $F: \mathbb{R}^{n+m} \to \mathbb{R}^m$ 在点 $(\mathbf{a}, \mathbf{b})$ 附近连续可微，其中 $F(\mathbf{a}, \mathbf{b}) = \mathbf{0}$。如果 $m \times m$ 矩阵 $\frac{\partial F}{\partial \mathbf{y}}$ 在 $(\mathbf{a}, \mathbf{b})$ 处可逆，则：

1. 存在 $\mathbf{a}$ 的邻域 $U \subset \mathbb{R}^n$ 和 $\mathbf{b}$ 的邻域 $V \subset \mathbb{R}^m$
2. 存在唯一的函数 $\mathbf{g}: U \to V$，使得对任意 $\mathbf{x} \in U$，有 $F(\mathbf{x}, \mathbf{g}(\mathbf{x})) = \mathbf{0}$
3. $\mathbf{g}$ 在 $U$ 上连续可微
4. 隐函数的导数为：$\frac{\partial \mathbf{g}}{\partial \mathbf{x}} = -\left[\frac{\partial F}{\partial \mathbf{y}}\right]^{-1} \frac{\partial F}{\partial \mathbf{x}}$

**特例（二元函数）**：设 $F(x, y) = 0$，且 $\frac{\partial F}{\partial y} \neq 0$，则局部存在 $y = g(x)$，且：

$$\frac{dy}{dx} = -\frac{\frac{\partial F}{\partial x}}{\frac{\partial F}{\partial y}}$$

#### 证明思路

1. 构造辅助函数 $G(x, y) = (x, F(x, y))$
2. 应用反函数定理证明 $G$ 局部可逆
3. 从 $G^{-1}$ 构造隐函数 $g$

#### 应用示例

**例1**：圆的方程

设 $F(x, y) = x^2 + y^2 - 1 = 0$，则：

$$\frac{\partial F}{\partial x} = 2x, \quad \frac{\partial F}{\partial y} = 2y$$

当 $y \neq 0$ 时，$\frac{\partial F}{\partial y} \neq 0$，因此局部可以解出：

$$y = g(x) = \pm\sqrt{1-x^2}$$

隐函数导数：
$$\frac{dy}{dx} = -\frac{2x}{2y} = -\frac{x}{y}$$

**例2**：约束优化

在约束优化中，约束条件 $g(x, y) = 0$ 可以通过隐函数定理在局部表示为 $y = y(x)$，从而将约束优化转化为无约束优化。

**例3**：机器学习中的流形学习

高维数据通常位于低维流形上。隐函数定理保证了流形的局部参数化，即局部可以用更少的坐标表示。

#### 机器学习中的应用

**1. 正规化流（Normalizing Flows）**

在生成模型中，需要将简单分布变换为复杂分布。反函数定理保证了变换的可逆性：

```python
import torch
import torch.nn as nn

class InvertibleLayer(nn.Module):
    """可逆层，基于反函数定理"""
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
    
    def forward(self, x):
        # 前向变换
        y = self._transform(x)
        # 计算雅可比行列式
        log_det = self._log_det_jacobian(x)
        return y, log_det
    
    def inverse(self, y):
        # 反向变换（需要雅可比可逆）
        x = self._inverse_transform(y)
        return x
    
    def _transform(self, x):
        # 实现具体的可逆变换
        pass
    
    def _inverse_transform(self, y):
        # 实现逆变换
        pass
    
    def _log_det_jacobian(self, x):
        # 计算 log|det(J)|
        pass
```

**2. 隐式神经表示**

在神经网络的隐式层中，隐函数定理用于求解平衡点：

```python
import torch
from torch.autograd import grad

def implicit_layer(z, theta, max_iter=50):
    """
    隐式层：求解不动点 z* = f(z*, theta)
    使用隐函数定理计算梯度
    """
    # 前向：找到平衡点
    for _ in range(max_iter):
        z = f(z, theta)
    
    # 反向：利用隐函数定理
    # dz*/dθ = -(I - ∂f/∂z*)^{-1} ∂f/∂θ
    return z
```

**3. 约束优化中的灵敏度分析**

在约束优化问题中，隐函数定理用于分析最优解对参数的敏感度：

$$\min_x f(x, \theta) \quad \text{s.t.} \quad g(x, \theta) = 0$$

当参数 $\theta$ 变化时，最优解 $x^*(\theta)$ 的变化率可由隐函数定理计算。

## 机器学习中的应用

### 1. 支持向量机（SVM）

SVM 的目标是找到最大间隔超平面，这可以表述为优化问题：

$$\min_{\mathbf{w}, b} \frac{1}{2}\|\mathbf{w}\|^2$$

约束条件：
$$y_i(\mathbf{w}^T \mathbf{x}_i + b) \geq 1, \quad i = 1, \ldots, n$$

这是一个典型的约束优化问题，可以使用拉格朗日乘数法求解。

### 2. 主成分分析（PCA）

PCA 的目标是找到最大方差的方向，这可以通过求解特征值问题得到。

### 3. 神经网络的损失函数

神经网络的损失函数通常是多元函数，其优化涉及梯度、Hessian 矩阵等概念。

## 3. 代码示例

```python
import numpy as np
from scipy.optimize import minimize

# 示例1：无约束优化
def f(x):
    """目标函数：f(x, y) = x² + y² - 4x - 6y"""
    return x[0]**2 + x[1]**2 - 4*x[0] - 6*x[1]

def grad_f(x):
    """梯度"""
    return np.array([2*x[0] - 4, 2*x[1] - 6])

# 使用梯度下降
x0 = np.array([0.0, 0.0])
result = minimize(f, x0, method='BFGS', jac=grad_f)

print(f"最小值点: {result.x}")
print(f"最小值: {result.fun:.6f}")

# 示例2：约束优化（拉格朗日乘数法）
def constraint(x):
    """约束条件：x² + y² = 1"""
    return x[0]**2 + x[1]**2 - 1

# 使用SLSQP方法求解约束优化
cons = {'type': 'eq', 'fun': constraint}
x0 = np.array([0.5, 0.5])

result_max = minimize(lambda x: -f(x), x0, method='SLSQP', constraints=cons)
result_min = minimize(f, x0, method='SLSQP', constraints=cons)

print(f"\n最大值点: {result_max.x}")
print(f"最大值: {-result_max.fun:.6f}")
print(f"最小值点: {result_min.x}")
print(f"最小值: {result_min.fun:.6f}")
```

## 习题

### 基础题

1. 求以下函数的极值：
   - $f(x, y) = x^2 + 2xy + 2y^2$
   - $f(x, y, z) = x^2 + y^2 + z^2 - 4x - 6y - 8z$

2. 在 $x^2 + y^2 = 4$ 的约束下，求 $f(x, y) = x^2 + y^2 + xy$ 的极值。

### 进阶题

3. 证明：如果 $H(\mathbf{a})$ 正定，则 $\mathbf{a}$ 是局部极小值点。

4. 在 $x + y + z = 1$ 的约束下，求 $f(x, y, z) = x^2 + y^2 + z^2$ 的最小值。

## 相关链接

- [[19_Partial_Derivatives]] - 偏导数（多元函数应用的基础）
- [[../../01_Mathematics/Optimization/01_Gradient_Descent]] - 梯度下降（极值问题的应用）
- [[03_NN_Module]] - 神经网络（损失函数的优化）
## 根据题型整理的做题方法
### 多元函数极值判断

**无条件极值**：
1. 求驻点：$\nabla f = 0$
2. 判断Hessian矩阵$H$：
   - $H$正定 $\Rightarrow$ 极小值
   - $H$负定 $\Rightarrow$ 极大值
   - $H$不定 $\Rightarrow$ 鞍点

**条件极值（Lagrange乘数法）**：
- 目标：$f(x,y)$，约束$g(x,y)=0$
- 构造：$L(x,y,\lambda) = f(x,y) + \lambda g(x,y)$
- 解方程组：$\frac{\partial L}{\partial x}=0, \frac{\partial L}{\partial y}=0, g(x,y)=0$

**最值求法**：
- 比较内部极值点和边界上的极值
- 比较所有候选点的函数值

## 10. 总结
### 10.1 重要定义
1. 多元函数极值：局部最大或最小值点
2. 临界点：梯度为零或偏导数不存在的点
3. 鞍点：既非极大也非极小的临界点
4. Hessian矩阵：二阶偏导数组成的矩阵
5. 条件极值：在约束条件下的极值

### 10.2 重要定理
1. 极值必要条件：可微极值点处梯度为零
2. 极值充分条件：Hessian矩阵正定（极小）或负定（极大）
3. 拉格朗日乘数法：求解条件极值
4. 最小二乘法：数据拟合的最小化方法

### 10.3 重要证明
1. 极值必要条件的证明：利用一元极值定理
2. 拉格朗日乘数法的证明：利用梯度与约束曲线的切线垂直

### 10.4 重要性质
1. Hessian矩阵判断极值类型
2. 条件极值通过拉格朗日函数求解
3. 最小二乘法是线性回归的核心
4. 多元极值在优化问题中广泛应用
## 11. 练习（分层）
## 根据题型整理的做题方法
### 多元函数极值判断
1. 先求所有驻点，解出 $\nabla f = 0$。
2. 计算 Hessian 矩阵并判断正定、负定或不定。
3. 若有约束条件，改用拉格朗日乘数法。
4. 对边界和候选点分别比较函数值。

## 易错点
- 只看驻点，不看 Hessian 的符号
- 条件极值里忘记把约束方程一并求解
- 误把“临界点”与“极值点”混为一谈
- 多元问题中忽略边界和可行域

本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 求 $f(x,y)=x^2+2xy+2y^2$ 的极值点。
2. 求 $f(x,y,z)=x^2+y^2+z^2-4x-6y-8z$ 的极值点。
3. 计算 $f(x,y)=x^2+y^2-4x-6y$ 的临界点并分类。
4. 判断 Hessian 矩阵正定时函数的极值类型。

### B档（进阶）
1. 在约束 $x^2+y^2=4$ 下，求 $f(x,y)=x^2+y^2+xy$ 的极值。
2. 在约束 $x+y+z=1$ 下，求 $f(x,y,z)=x^2+y^2+z^2$ 的最小值。
3. 用拉格朗日乘数法求椭球面上的最值问题。
4. 证明：若 $H(\mathbf{a})$ 正定，则 $\mathbf{a}$ 为局部极小值点。

### C档（挑战）
1. 证明反函数定理在局部可逆性中的作用，并举极坐标变换为例。
2. 结合隐函数定理，分析约束方程组的局部解结构。
3. 研究最小二乘法与多元极值之间的联系。
4. 设计一个机器学习损失函数的优化问题，并写出梯度与 Hessian。



