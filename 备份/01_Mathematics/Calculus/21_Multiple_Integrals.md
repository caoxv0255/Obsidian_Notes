---
type: concept
topic: multiple_integrals
category: calculus
difficulty: advanced
prerequisites:
    - [[10_Definite_Integrals]]
    - [[19_Partial_Derivatives]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-03-09
status: complete
---
# 重积分 (Multiple Integrals)

## 学习目标
- 理解二重积分、三重积分及其几何意义
- 掌握直角坐标、极坐标、柱坐标和球坐标下的积分计算
- 会用重积分求体积、质量、概率与物理量

## 先修
- [[10_Definite_Integrals]] - 定积分
- [[19_Partial_Derivatives]] - 偏导数与全微分
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：二重积分、三重积分与区域分解
- B档（进阶）：极坐标、柱坐标、球坐标与变量代换
- C档（挑战）：Jacobian、对称性与应用建模

## 自测（3问速测）
1. 二重积分和一重积分在几何意义上有什么区别？
2. 什么情况下应该改用极坐标或柱坐标？
3. 变量代换时为什么必须乘上 Jacobian？

## 1. 定义

重积分是定积分在多维空间的推广，用于计算多维区域的体积、质量、质心等。

## 2. 定理与性质

### 1. 二重积分

#### 定义

函数 $f(x, y)$ 在区域 $D$ 上的二重积分记作：

$$\iint_D f(x, y) dA$$

#### 计算方法

**直角坐标系**：
$$\iint_D f(x, y) dx dy = \int_a^b \left[\int_{g_1(x)}^{g_2(x)} f(x, y) dy\right] dx$$

或：
$$\iint_D f(x, y) dy dx = \int_c^d \left[\int_{h_1(y)}^{h_2(y)} f(x, y) dx\right] dy$$

**极坐标**：
$$\iint_D f(x, y) dA = \iint_{D'} f(r\cos\theta, r\sin\theta) r dr d\theta$$

**示例**：计算 $\iint_D (x + y) dA$，其中 $D = [0, 1] \times [0, 2]$。

**解**：
$$\iint_D (x + y) dx dy = \int_0^1 \int_0^2 (x + y) dy dx$$
$$= \int_0^1 \left[xy + \frac{y^2}{2}\right]_0^2 dx = \int_0^1 (2x + 2) dx$$
$$= \left[x^2 + 2x\right]_0^1 = 3$$

### 2. 三重积分

#### 定义

函数 $f(x, y, z)$ 在区域 $V$ 上的三重积分记作：

$$\iiint_V f(x, y, z) dV$$

#### 计算方法

**直角坐标系**：
$$\iiint_V f(x, y, z) dx dy dz = \int_a^b \int_{g_1(x)}^{g_2(x)} \int_{h_1(x,y)}^{h_2(x,y)} f(x, y, z) dz dy dx$$

**柱坐标**：
$$\iiint_V f(x, y, z) dV = \iiint_{V'} f(r\cos\theta, r\sin\theta, z) r dz dr d\theta$$

**球坐标**：
$$\iiint_V f(x, y, z) dV = \iiint_{V'} f(\rho\sin\phi\cos\theta, \rho\sin\phi\sin\theta, \rho\cos\phi) \rho^2 \sin\phi d\rho d\phi d\theta$$

### 3. 重积分的性质

1. **线性性**：$\iint_D [c f(x, y) + d g(x, y)] dA = c \iint_D f(x, y) dA + d \iint_D g(x, y) dA$
2. **可加性**：如果 $D = D_1 \cup D_2$ 且 $D_1 \cap D_2 = \emptyset$，则 $\iint_D f(x, y) dA = \iint_{D_1} f(x, y) dA + \iint_{D_2} f(x, y) dA$
3. **单调性**：如果 $f(x, y) \leq g(x, y)$ 对所有 $(x, y) \in D$，则 $\iint_D f(x, y) dA \leq \iint_D g(x, y) dA$

## 机器学习中的应用

### 1. 联合概率分布

对于随机向量 $(X, Y)$，其联合概率密度函数 $f_{X,Y}(x, y)$ 满足：

$$\iint_{\mathbb{R}^2} f_{X,Y}(x, y) dx dy = 1$$

联合概率：
$$P((X, Y) \in D) = \iint_D f_{X,Y}(x, y) dx dy$$

### 2. 边缘分布

边缘概率密度函数：
$$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) dy$$
$$f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) dx$$

### 3. 贝叶斯推断

后验分布的计算通常涉及多重积分：

$$P(\theta|D) = \frac{P(D|\theta) P(\theta)}{\int P(D|\theta') P(\theta') d\theta'}$$

## 3. 代码示例

```python
import numpy as np
from scipy.integrate import dblquad, tplquad

# 示例1：二重积分
def f2(x, y):
    """被积函数：x + y"""
    return x + y

result, error = dblquad(f2, 0, 1, lambda x: 0, lambda x: 2)
print(f"二重积分结果: {result:.6f} (理论值: 3)")

# 示例2：三重积分
def f3(x, y, z):
    """被积函数：x + y + z"""
    return x + y + z

result3, error3 = tplquad(
    f3,
    0, 1,  # x的范围
    lambda x: 0, lambda x: 2,  # y的范围（可能依赖于x）
    lambda x, y: 0, lambda x, y: 1  # z的范围（可能依赖于x和y）
)
print(f"三重积分结果: {result3:.6f}")

# 示例3：极坐标下的二重积分
def polar_integral():
    """计算单位圆的面积"""
    def integrand(r, theta):
        return r  # 极坐标下的面积元素

    result, error = dblquad(
        integrand,
        0, 2*np.pi,  # θ的范围
        lambda theta: 0, lambda theta: 1  # r的范围
    )
    return result

print(f"单位圆面积: {polar_integral():.6f} (理论值: π ≈ {np.pi:.6f})")
```

## 习题

### 基础题

1. 计算以下二重积分：
   - $\iint_D x^2 y dx dy$，其中 $D = [0, 1] \times [0, 2]$
   - $\iint_D e^{x+y} dx dy$，其中 $D = [0, 1] \times [0, 1]$

2. 计算以下区域在极坐标下的面积：
   - 半径为 $r$ 的圆
   - $0 \leq r \leq \cos\theta$，$0 \leq \theta \leq \pi/2$

### 进阶题

3. 证明：$\iint_{[0,1] \times [0,1]} f(x) g(y) dx dy = \int_0^1 f(x) dx \cdot \int_0^1 g(y) dy$

4. 在球坐标下计算半径为 $R$ 的球的体积。

## 根据题型整理的做题方法
### 重积分计算策略

**坐标系选择**：
- 区域是矩形/由直线围成 → 直角坐标
- 区域含圆弧/圆域 → 极坐标
- 区域含球面/圆柱 → 柱坐标/球坐标

**积分次序**：
- 分析被积函数和边界
- 选择先积的变量使计算简单

**变量代换**：
- Jacobian行列式：$dxdy = |J|dudv$
- 常用变换：极坐标、柱坐标、球坐标

### 核心公式

**极坐标**：$x=r\cos\theta, y=r\sin\theta, dA = r drd\theta$

**柱坐标**：$x=r\cos\theta, y=r\sin\theta, z=z, dV = rdzdrd\theta$

**球坐标**：$x=\rho\sin\phi\cos\theta, y=\rho\sin\phi\sin\theta, z=\rho\cos\phi, dV = \rho^2\sin\phi d\rho d\phi d\theta$

### 积分区域类型与判断

#### 二重积分区域类型

**X型区域（先y后x）**：
$$D = \{(x, y) : a \leq x \leq b, \varphi_1(x) \leq y \leq \varphi_2(x)\}$$

**特征**：用平行于y轴的直线穿过区域，入口和出口都是单值函数。

**Y型区域（先x后y）**：
$$D = \{(x, y) : c \leq y \leq d, \psi_1(y) \leq x \leq \psi_2(y)\}$$

**特征**：用平行于x轴的直线穿过区域，入口和出口都是单值函数。

**混合型区域**：需分割成若干X型或Y型区域。

**极坐标型区域**：
$$D = \{(r, \theta) : \alpha \leq \theta \leq \beta, r_1(\theta) \leq r \leq r_2(\theta)\}$$

**判断技巧**：
1. 画出积分区域
2. 用平行于坐标轴的直线试探
3. 选择穿入穿出点最少的方向作为内层积分

#### 典型区域示例

| 区域形状 | 最佳坐标系 | 积分次序建议 |
|---------|-----------|-------------|
| 矩形 $[a,b] \times [c,d]$ | 直角坐标 | 任意 |
| 三角形 $0 \leq y \leq x \leq 1$ | 直角坐标 | 先y后x |
| 圆域 $x^2+y^2 \leq R^2$ | 极坐标 | 先r后θ |
| 圆环 $a^2 \leq x^2+y^2 \leq b^2$ | 极坐标 | 先r后θ |
| 抛物线域 $y \geq x^2$ | 直角坐标 | 先y后x |
| 心形线 $r = a(1+\cos\theta)$ | 极坐标 | 先r后θ |
| 球体 $x^2+y^2+z^2 \leq R^2$ | 球坐标 | 先ρ后φ再θ |

### 详细计算实例

#### 实例1：直角坐标下的二重积分

**问题**：计算 $\iint_D xy \, dx dy$，其中 $D$ 由 $y = x^2$ 和 $y = \sqrt{x}$ 围成。

**步骤1：确定积分区域**
- 求交点：$x^2 = \sqrt{x} \Rightarrow x = 0$ 或 $x = 1$
- 区域：$0 \leq x \leq 1$，$x^2 \leq y \leq \sqrt{x}$

**步骤2：确定积分次序**
- X型：$\int_0^1 dx \int_{x^2}^{\sqrt{x}} xy \, dy$
- Y型：$\int_0^1 dy \int_{y^2}^{\sqrt{y}} xy \, dx$（相同）

**步骤3：计算**
$$\int_0^1 dx \int_{x^2}^{\sqrt{x}} xy \, dy = \int_0^1 x \cdot \frac{y^2}{2}\Big|_{x^2}^{\sqrt{x}} dx$$
$$= \int_0^1 x \cdot \frac{x - x^4}{2} dx = \frac{1}{2}\int_0^1 (x^2 - x^5) dx = \frac{1}{2}\left[\frac{x^3}{3} - \frac{x^6}{6}\right]_0^1 = \frac{1}{12}$$

#### 实例2：极坐标下的二重积分

**问题**：计算 $\iint_D e^{-(x^2+y^2)} dA$，其中 $D = \{(x,y) : x^2+y^2 \leq 1\}$。

**分析**：
- 区域是圆域，适合极坐标
- 被积函数 $e^{-(x^2+y^2)} = e^{-r^2}$

**计算**：
$$\iint_D e^{-(x^2+y^2)} dA = \int_0^{2\pi} d\theta \int_0^1 e^{-r^2} \cdot r \, dr$$

内层积分（换元 $u = r^2$）：
$$\int_0^1 e^{-r^2} \cdot r \, dr = \frac{1}{2}\int_0^1 e^{-u} du = \frac{1}{2}(1 - e^{-1})$$

外层积分：
$$\int_0^{2\pi} \frac{1}{2}(1 - e^{-1}) d\theta = \pi(1 - e^{-1})$$

**重要推广**：
$$\int_0^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$$

#### 实例3：利用对称性简化

**问题**：计算 $\iint_D (x^3 + y^3 + xy^2) dA$，其中 $D = \{(x,y) : |x| + |y| \leq 1\}$。

**分析**：
- $D$ 关于x轴和y轴都对称
- $x^3$ 关于x是奇函数，$\iint_D x^3 dA = 0$
- $y^3$ 关于y是奇函数，$\iint_D y^3 dA = 0$
- $xy^2$ 关于x是奇函数，$\iint_D xy^2 dA = 0$

**结论**：$\iint_D (x^3 + y^3 + xy^2) dA = 0$

**对称性原则**：
- 区域关于某轴对称 + 函数关于该变量是奇函数 → 积分值为0
- 区域关于某轴对称 + 函数关于该变量是偶函数 → 积分 = 2 × 半区域积分

#### 实例4：变量代换

**问题**：计算 $\iint_D e^{(x-y)/(x+y)} dA$，其中 $D$ 由 $x+y=1$，$x+y=2$，$x=0$，$y=0$ 围成。

**变换选择**：
令 $u = x - y$，$v = x + y$

**Jacobian计算**：
$$x = \frac{u+v}{2}, \quad y = \frac{v-u}{2}$$
$$J = \frac{\partial(x,y)}{\partial(u,v)} = \begin{vmatrix} \frac{1}{2} & \frac{1}{2} \\ -\frac{1}{2} & \frac{1}{2} \end{vmatrix} = \frac{1}{2}$$

**新区域**：
- $x+y=1 \Rightarrow v=1$
- $x+y=2 \Rightarrow v=2$
- $x=0 \Rightarrow u+v=0 \Rightarrow u=-v$
- $y=0 \Rightarrow v-u=0 \Rightarrow u=v$

**计算**：
$$\iint_D e^{(x-y)/(x+y)} dA = \int_1^2 dv \int_{-v}^v e^{u/v} \cdot \frac{1}{2} du$$

#### 实例5：三重积分的投影法

**问题**：计算 $\iiint_V z \, dV$，其中 $V$ 由 $z = x^2 + y^2$ 和 $z = 1$ 围成。

**方法：投影法**
1. 将V投影到xy平面：$D = \{(x,y) : x^2 + y^2 \leq 1\}$
2. z的范围：$x^2 + y^2 \leq z \leq 1$

$$\iiint_V z \, dV = \iint_D dA \int_{x^2+y^2}^1 z \, dz$$

计算内层积分：
$$\int_{x^2+y^2}^1 z \, dz = \frac{1}{2}(1 - (x^2+y^2)^2)$$

使用极坐标：
$$\iint_D \frac{1}{2}(1 - (x^2+y^2)^2) dA = \frac{1}{2}\int_0^{2\pi} d\theta \int_0^1 (1-r^4) \cdot r \, dr$$
$$= \pi \int_0^1 (r - r^5) dr = \pi\left[\frac{r^2}{2} - \frac{r^6}{6}\right]_0^1 = \frac{\pi}{3}$$

#### 实例6：球坐标的应用

**问题**：计算球体 $x^2+y^2+z^2 \leq R^2$ 的体积。

**球坐标**：
- $x = \rho\sin\phi\cos\theta$
- $y = \rho\sin\phi\sin\theta$
- $z = \rho\cos\phi$
- $dV = \rho^2\sin\phi \, d\rho \, d\phi \, d\theta$

**积分限**：
- $\rho: 0 \to R$
- $\phi: 0 \to \pi$
- $\theta: 0 \to 2\pi$

**计算**：
$$V = \int_0^{2\pi} d\theta \int_0^\pi d\phi \int_0^R \rho^2\sin\phi \, d\rho$$
$$= 2\pi \cdot \int_0^\pi \sin\phi \, d\phi \cdot \int_0^R \rho^2 d\rho$$
$$= 2\pi \cdot 2 \cdot \frac{R^3}{3} = \frac{4\pi R^3}{3}$$

### 雅可比行列式的几何意义

**定义**：对于变换 $x = x(u,v)$，$y = y(u,v)$：

$$J = \frac{\partial(x,y)}{\partial(u,v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix}$$

**几何意义**：$|J|$ 表示变换的"面积伸缩因子"。

**示例**：极坐标变换
$$x = r\cos\theta, \quad y = r\sin\theta$$
$$J = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r(\cos^2\theta + \sin^2\theta) = r$$

**物理意义**：极坐标下，$r dr d\theta$ 是"小扇环"的面积。

### 代码实现：多元积分计算器

```python
import numpy as np
from scipy.integrate import dblquad, tplquad, nquad
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ============================================
# 实例1：直角坐标二重积分
# ============================================
def example1_rectangular():
    """计算 ∬_D xy dxdy，D由 y=x² 和 y=√x 围成"""
    
    # 内层积分：对y积分
    def inner_y(y, x):
        return x * y
    
    # 外层积分：对x积分
    result, error = dblquad(
        inner_y,
        0, 1,  # x的范围
        lambda x: x**2,  # y的下界
        lambda x: np.sqrt(x)  # y的上界
    )
    
    print(f"实例1结果: {result:.10f}")
    print(f"理论值: 1/12 ≈ {1/12:.10f}")
    print(f"误差: {abs(result - 1/12):.2e}\n")

# ============================================
# 实例2：极坐标二重积分
# ============================================
def example2_polar():
    """计算 ∬_D e^(-(x²+y²)) dA，D是单位圆"""
    
    def integrand(r, theta):
        return np.exp(-r**2) * r  # 注意乘以r
    
    result, error = dblquad(
        integrand,
        0, 2*np.pi,  # θ的范围
        lambda theta: 0,  # r的下界
        lambda theta: 1   # r的上界
    )
    
    theoretical = np.pi * (1 - np.exp(-1))
    print(f"实例2结果: {result:.10f}")
    print(f"理论值: π(1-e^(-1)) ≈ {theoretical:.10f}")
    print(f"误差: {abs(result - theoretical):.2e}\n")

# ============================================
# 实例3：三重积分（投影法）
# ============================================
def example3_triple():
    """计算 ∭_V z dV，V由 z=x²+y² 和 z=1 围成"""
    
    def integrand(z, y, x):
        return z
    
    # 需要先对z积分，然后对y，最后对x
    # 使用极坐标更方便，这里演示直角坐标
    
    def inner_z(z, x, y):
        return z
    
    # 简化：使用对称性
    # 投影区域是单位圆，使用极坐标
    
    def polar_integrand(r, theta):
        z_max = 1
        z_min = r**2
        # 内层积分 ∫_{r²}^{1} z dz = (1-r⁴)/2
        return (1 - r**4) / 2 * r
    
    result, error = dblquad(
        polar_integrand,
        0, 2*np.pi,
        lambda theta: 0,
        lambda theta: 1
    )
    
    theoretical = np.pi / 3
    print(f"实例3结果: {result:.10f}")
    print(f"理论值: π/3 ≈ {theoretical:.10f}")
    print(f"误差: {abs(result - theoretical):.2e}\n")

# ============================================
# 实例4：球坐标
# ============================================
def example4_spherical():
    """计算球体体积"""
    
    def integrand(rho, phi, theta):
        return rho**2 * np.sin(phi)
    
    result, error = tplquad(
        integrand,
        0, 2*np.pi,  # θ
        lambda theta: 0, lambda theta: np.pi,  # φ
        lambda theta, phi: 0, lambda theta, phi: 1  # ρ
    )
    
    theoretical = 4 * np.pi / 3
    print(f"实例4结果: {result:.10f}")
    print(f"理论值: 4π/3 ≈ {theoretical:.10f}")
    print(f"误差: {abs(result - theoretical):.2e}\n")

# ============================================
# 实例5：变量代换
# ============================================
def example5_transform():
    """计算 ∬_D e^((x-y)/(x+y)) dA"""
    
    # 使用变换 u = x-y, v = x+y
    # 反解：x = (u+v)/2, y = (v-u)/2
    # Jacobian = 1/2
    
    def integrand(u, v):
        return np.exp(u/v) * 0.5  # 乘以Jacobian
    
    # 新区域：v从1到2，u从-v到v
    result, error = dblquad(
        integrand,
        1, 2,  # v的范围
        lambda v: -v,
        lambda v: v
    )
    
    print(f"实例5结果: {result:.10f}")
    print(f"理论值: (e - 1/e)/2 ≈ {(np.e - 1/np.e)/2:.10f}")
    print(f"误差: {abs(result - (np.e - 1/np.e)/2):.2e}\n")

# ============================================
# 实例6：区域可视化
# ============================================
def visualize_regions():
    """可视化不同类型的积分区域"""
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # 1. 矩形区域
    ax = axes[0, 0]
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 2, 100)
    X, Y = np.meshgrid(x, y)
    ax.fill_between(x, 0, 2, alpha=0.3)
    ax.set_title('矩形区域: [0,1]×[0,2]', fontsize=12)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, alpha=0.3)
    
    # 2. 三角形区域
    ax = axes[0, 1]
    x = np.linspace(0, 1, 100)
    ax.fill_between(x, 0, x, alpha=0.3)
    ax.plot(x, x, 'r-', linewidth=2)
    ax.set_title('三角形: 0≤y≤x≤1', fontsize=12)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, alpha=0.3)
    
    # 3. 圆域
    ax = axes[0, 2]
    theta = np.linspace(0, 2*np.pi, 100)
    r = 1
    ax.fill(r*np.cos(theta), r*np.sin(theta), alpha=0.3)
    ax.plot(r*np.cos(theta), r*np.sin(theta), 'r-', linewidth=2)
    ax.set_title('圆域: x²+y²≤1', fontsize=12)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    
    # 4. 抛物线区域
    ax = axes[1, 0]
    x = np.linspace(0, 1, 100)
    ax.fill_between(x, x**2, np.sqrt(x), alpha=0.3)
    ax.plot(x, x**2, 'r-', linewidth=2, label='y=x²')
    ax.plot(x, np.sqrt(x), 'b-', linewidth=2, label='y=√x')
    ax.set_title('抛物线区域', fontsize=12)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 5. 极坐标区域（心形线）
    ax = axes[1, 1]
    theta = np.linspace(0, 2*np.pi, 100)
    r = 1 + np.cos(theta)
    ax = plt.subplot(235, projection='polar')
    ax.plot(theta, r, 'r-', linewidth=2)
    ax.fill(theta, r, alpha=0.3)
    ax.set_title('心形线: r=1+cosθ', fontsize=12)
    
    # 6. 极坐标区域（玫瑰线）
    ax = axes[1, 2]
    ax = plt.subplot(236, projection='polar')
    theta = np.linspace(0, 2*np.pi, 100)
    r = np.sin(2*theta)
    ax.plot(theta, r, 'r-', linewidth=2)
    ax.fill(theta, r, alpha=0.3)
    ax.set_title('玫瑰线: r=sin(2θ)', fontsize=12)
    
    plt.tight_layout()
    plt.show()

# ============================================
# 运行所有实例
# ============================================
if __name__ == "__main__":
    print("="*50)
    print("多元积分计算实例")
    print("="*50 + "\n")
    
    example1_rectangular()
    example2_polar()
    example3_triple()
    example4_spherical()
    example5_transform()
    
    print("="*50)
    print("区域可视化")
    print("="*50 + "\n")
    
    visualize_regions()
```

### 积分顺序选择的决策树

```
开始
  │
  ├─ 区域是圆/圆环/扇形？
  │   └─ 是 → 极坐标
  │
  ├─ 区域含球面/椭球面？
  │   └─ 是 → 球坐标
  │
  ├─ 区域含圆柱面？
  │   └─ 是 → 柱坐标
  │
  └─ 其他情况
      │
      ├─ 被积函数含 e^(-(x²+y²))？
      │   └─ 是 → 极坐标
      │
      └─ 直角坐标
          │
          ├─ 边界函数简单？
          │   └─ 先对边界函数复杂的变量积分
          │
          └─ 被积函数简单？
              └─ 先对被积函数复杂的变量积分
```

### 常见错误警示

**错误1**：忘记极坐标的 $r$ 因子

❌ $\iint_D f(x,y) dxdy = \iint_{D'} f(r\cos\theta, r\sin\theta) drd\theta$

✅ $\iint_D f(x,y) dxdy = \iint_{D'} f(r\cos\theta, r\sin\theta) \cdot r \, drd\theta$

**错误2**：积分限搞反

❌ $\int_0^1 dx \int_0^x ...$（应该是 $y$ 从 $0$ 到 $x$）

✅ $\int_0^1 dx \int_0^x ...$ 表示 $0 \leq y \leq x$

**错误3**：忽略对称性

❌ 直接计算 $\iint_D x \, dA$，其中 $D$ 关于 $y$ 轴对称

✅ 利用对称性，$\iint_D x \, dA = 0$

**错误4**：雅可比行列式计算错误

❌ 忘记取绝对值

✅ $dxdy = |J| dudv$

## 相关链接

- [[10_Definite_Integrals]] - 定积分（重积分的基础）
- [[19_Partial_Derivatives]] - 偏导数（重积分的逆运算）
- [[../../01_Mathematics/Probability/03_Distributions]] - 概率分布（重积分的应用）
- [[06_Case_Finance]] - 金融案例（联合概率的应用）

## 总结
- 重积分是把一维积分推广到二维和三维区域上的累积量计算
- 选坐标系、选积分次序和拆分区域是求解的关键
- 对称性与变量代换可以显著简化计算

## 根据题型整理的做题方法
### 重积分四步法
1. 先画区域，确定积分边界。
2. 再选合适的坐标系和积分次序。
3. 若有对称性或可代换结构，优先化简。
4. 最后检查 Jacobian 与积分限是否一致。

## 易错点
- 极坐标下忘记 $r$ 因子
- 变量代换时 Jacobian 写错或漏绝对值
- 积分限和区域边界对应错误
- 看到对称区域却没有利用奇偶性

## 练习（分层）
### A档（基础）
1. 计算 $\iint_{[0,1]\times[0,2]} (x+y) \, dxdy$。
2. 计算由 $y=x^2$ 与 $y=\sqrt{x}$ 围成区域的面积。
3. 计算单位圆盘的面积。
4. 计算球体 $x^2+y^2+z^2\le R^2$ 的体积。

### B档（进阶）
1. 用极坐标计算 $\iint_D e^{-(x^2+y^2)} dA$，其中 $D$ 是单位圆盘。
2. 用变量代换 $u=x-y, v=x+y$ 计算一个给定区域上的二重积分。
3. 计算由抛物线和直线围成区域的质量中心。
4. 用柱坐标或球坐标计算给定旋转体或球体积分。

### C档（挑战）
1. 证明在适当条件下，重积分对变量代换满足 $dA = |J| dudv$。
2. 研究二重积分与联合概率密度函数的关系。
3. 证明对称区域上奇函数积分为零。
4. 结合一个优化或概率问题，建立并计算三重积分模型。


