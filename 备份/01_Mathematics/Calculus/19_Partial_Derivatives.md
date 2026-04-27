---
type: concept
topic: partial_derivatives
category: calculus
difficulty: intermediate
prerequisites:
    - [[02_Limits]]
    - [[05_Derivatives]]
    - [[18_Multivariable_Limits]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: false
created: 2026-03-09
updated: 2026-04-24
status: complete
subject: calculus
chapter: 19
---

# 偏导数与全微分 (Partial Derivatives and Total Differential)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解偏导数、全微分、方向导数和梯度的基本概念
- 掌握多元链式法则、隐函数求导和混合偏导数判别
- 会用二阶偏导和 Hessian 判别多元函数的极值

## 先修
- [[02_Limits]] - 极限
- [[05_Derivatives]] - 导数
- [[18_Multivariable_Limits]] - 多元函数极限
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：偏导数、全微分与梯度
- B档（进阶）：链式法则、方向导数与隐函数求导
- C档（挑战）：极值判别、Hessian 与综合应用

## 自测（3问速测）
1. 偏导数和全微分的区别是什么？
2. 为什么方向导数可以写成梯度与单位方向向量的点积？
3. 混合偏导数什么时候相等？

## 1. 定义

**直观理解**：
偏导数是多元函数的导数概念，描述函数在某个方向上的变化率。全微分则是函数的线性近似，是多元函数微分学的核心概念。

想象你在山上，高度是位置的函数（x, y）。偏导数就是：
- 对 x 的偏导数：如果你只向东走，高度会如何变化
- 对 y 的偏导数：如果你只向北走，高度会如何变化

全微分则是：如果你同时向东和北走一点，高度会如何变化（这是两个方向变化的叠加）。

## 2. 定理与性质

### 偏导数的定义

设函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 的某个邻域内有定义。

**对 x 的偏导数**：
$$\frac{\partial f}{\partial x}(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}$$

**对 y 的偏导数**：
$$\frac{\partial f}{\partial y}(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0, y_0 + h) - f(x_0, y_0)}{h}$$

**几何意义**：
- $\frac{\partial f}{\partial x}$ 是曲面 $z = f(x, y)$ 与平面 $y = y_0$ 的交线的切线斜率
- $\frac{\partial f}{\partial y}$ 是曲面 $z = f(x, y)$ 与平面 $x = x_0$ 的交线的切线斜率

### 高阶偏导数

**二阶偏导数**：
$$\frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right)$$
$$\frac{\partial^2 f}{\partial y^2} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right)$$
$$\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)$$
$$\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)$$

**混合偏导数的相等性**（Clairaut 定理）：
如果 $\frac{\partial^2 f}{\partial x \partial y}$ 和 $\frac{\partial^2 f}{\partial y \partial x}$ 都连续，则：
$$\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$$

### 全微分

**定义**：
函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 处的全微分为：
$$dz = \frac{\partial f}{\partial x}(x_0, y_0) dx + \frac{\partial f}{\partial y}(x_0, y_0) dy$$

其中 $dx$ 和 $dy$ 是自变量的增量。

**几何意义**：
全微分是函数在点 $(x_0, y_0)$ 处的切平面方程：
$$z - f(x_0, y_0) = \frac{\partial f}{\partial x}(x_0, y_0)(x - x_0) + \frac{\partial f}{\partial y}(x_0, y_0)(y - y_0)$$

### 可微性

**定义**：
函数 $f$ 在点 $(x_0, y_0)$ 处可微，如果：
$$\Delta f = f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0) = A \Delta x + B \Delta y + o(\sqrt{\Delta x^2 + \Delta y^2})$$
其中 $A = \frac{\partial f}{\partial x}(x_0, y_0)$，$B = \frac{\partial f}{\partial y}(x_0, y_0)$。

**可微的充分条件**：
如果 $f$ 的两个偏导数在 $(x_0, y_0)$ 的某个邻域内存在且在 $(x_0, y_0)$ 处连续，则 $f$ 在 $(x_0, y_0)$ 处可微。

### 方向导数与梯度

**方向导数**：
函数 $f$ 在点 $(x_0, y_0)$ 处沿方向 $\mathbf{u} = (u_1, u_2)$（单位向量）的方向导数为：
$$D_{\mathbf{u}}f(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + hu_1, y_0 + hu_2) - f(x_0, y_0)}{h}$$

**梯度**：
函数 $f$ 在点 $(x_0, y_0)$ 处的梯度为：
$$\nabla f(x_0, y_0) = \left(\frac{\partial f}{\partial x}(x_0, y_0), \frac{\partial f}{\partial y}(x_0, y_0)\right)$$

**梯度与方向导数的关系**：
$$D_{\mathbf{u}}f(x_0, y_0) = \nabla f(x_0, y_0) \cdot \mathbf{u}$$

**梯度的性质**：
1. 梯度的方向是函数增长最快的方向
2. 梯度的模（长度）是最大增长率
3. 梯度方向垂直于等值线（等高线）

### 链式法则

**多元复合函数的链式法则**：
设 $z = f(u, v)$，而 $u = u(x, y)$，$v = v(x, y)$，则：
$$\frac{\partial z}{\partial x} = \frac{\partial f}{\partial u} \cdot \frac{\partial u}{\partial x} + \frac{\partial f}{\partial v} \cdot \frac{\partial v}{\partial x}$$
$$\frac{\partial z}{\partial y} = \frac{\partial f}{\partial u} \cdot \frac{\partial u}{\partial y} + \frac{\partial f}{\partial v} \cdot \frac{\partial v}{\partial y}$$

### 隐函数求导

**一个方程确定的隐函数**：
设 $F(x, y) = 0$ 确定 $y$ 为 $x$ 的函数 $y = y(x)$，则：
$$\frac{dy}{dx} = -\frac{\partial F}{\partial x} / \frac{\partial F}{\partial y}$$

**方程组确定的隐函数**：
设 $\begin{cases} F(x, y, u, v) = 0 \\ G(x, y, u, v) = 0 \end{cases}$ 确定 $u, v$ 为 $x, y$ 的函数，则可以通过求解方程组来得到 $\frac{\partial u}{\partial x}$, $\frac{\partial u}{\partial y}$ 等。

### 多元函数的极值

**极值的必要条件**：
如果 $f$ 在 $(x_0, y_0)$ 处有极值且偏导数存在，则：
$$\nabla f(x_0, y_0) = \mathbf{0}$$

即：
$$\frac{\partial f}{\partial x}(x_0, y_0) = 0, \quad \frac{\partial f}{\partial y}(x_0, y_0) = 0$$

**极值的充分条件（二阶判别法）**：
设 $(x_0, y_0)$ 是 $f$ 的驻点（$\nabla f(x_0, y_0) = \mathbf{0}$），记：
$$A = \frac{\partial^2 f}{\partial x^2}(x_0, y_0), \quad B = \frac{\partial^2 f}{\partial x \partial y}(x_0, y_0), \quad C = \frac{\partial^2 f}{\partial y^2}(x_0, y_0)$$

判别式：$\Delta = AC - B^2$

1. 如果 $\Delta > 0$ 且 $A > 0$，则 $(x_0, y_0)$ 是极小值点
2. 如果 $\Delta > 0$ 且 $A < 0$，则 $(x_0, y_0)$ 是极大值点
3. 如果 $\Delta < 0$，则 $(x_0, y_0)$ 是鞍点
4. 如果 $\Delta = 0$，需要更高阶的判别法

## 3. 代码示例

### 示例 1：计算偏导数

```python
import numpy as np
import sympy as sp

def partial_derivative(f_sym, variables, var_index, point):
    """
    计算偏导数
    
    参数:
        f_sym: 符号函数
        variables: 变量列表
        var_index: 要求偏导数的变量索引
        point: 求导点
    """
    var = variables[var_index]
    partial = sp.diff(f_sym, var)
    
    # 代入具体点
    point_dict = {variables[i]: point[i] for i in range(len(variables))}
    result = partial.subs(point_dict)
    
    return result

# 示例：计算 f(x, y) = x² + y² + xy 的偏导数
x, y = sp.symbols('x y')
f = x**2 + y**2 + x*y

point = (1, 2)

print("计算 f(x, y) = x² + y² + xy 在点 (1, 2) 处的偏导数：")

# 对 x 的偏导数
partial_x = partial_derivative(f, [x, y], 0, point)
print(f"∂f/∂x(1, 2) = {partial_x}")

# 对 y 的偏导数
partial_y = partial_derivative(f, [x, y], 1, point)
print(f"∂f/∂y(1, 2) = {partial_y}")

# 验证：手动计算
# ∂f/∂x = 2x + y, ∂f/∂x(1, 2) = 2*1 + 2 = 4
# ∂f/∂y = 2y + x, ∂f/∂y(1, 2) = 2*2 + 1 = 5
```

### 示例 2：高阶偏导数

```python
import numpy as np
import sympy as sp

def higher_order_partial(f_sym, variables, orders, point):
    """
    计算高阶偏导数
    
    参数:
        f_sym: 符号函数
        variables: 变量列表
        orders: 求导阶数（如 [1, 2] 表示先对 x 求一次，再对 y 求两次）
        point: 求导点
    """
    # 按顺序求导
    result = f_sym
    for i, order in enumerate(orders):
        for _ in range(order):
            result = sp.diff(result, variables[i])
    
    # 代入具体点
    point_dict = {variables[i]: point[i] for i in range(len(variables))}
    value = result.subs(point_dict)
    
    return result, value

# 示例：计算 f(x, y) = x³y² + xy + 1 的高阶偏导数
x, y = sp.symbols('x y')
f = x**3 * y**2 + x*y + 1

point = (1, 1)

print("计算 f(x, y) = x³y² + xy + 1 的高阶偏导数：")

# ∂²f/∂x²
partial_xx, val_xx = higher_order_partial(f, [x, y], [2, 0], point)
print(f"∂²f/∂x²(1, 1) = {val_xx} (解析: {partial_xx})")

# ∂²f/∂y²
partial_yy, val_yy = higher_order_partial(f, [x, y], [0, 2], point)
print(f"∂²f/∂y²(1, 1) = {val_yy} (解析: {partial_yy})")

# ∂²f/∂x∂y
partial_xy, val_xy = higher_order_partial(f, [x, y], [1, 1], point)
print(f"∂²f/∂x∂y(1, 1) = {val_xy} (解析: {partial_xy})")

# ∂²f/∂y∂x（应该等于 ∂²f/∂x∂y）
partial_yx, val_yx = higher_order_partial(f, [x, y], [1, 1], point)
print(f"∂²f/∂y∂x(1, 1) = {val_yx} (解析: {partial_yx})")

# 验证混合偏导数相等
print(f"\n混合偏导数相等性验证：{val_xy == val_yx}")
```

### 示例 3：梯度和方向导数

```python
import numpy as np

def gradient(f, point, h=1e-6):
    """
    计算函数的梯度（数值方法）
    
    参数:
        f: 多元函数
        point: 求梯度点
        h: 数值微分步长
    """
    point = np.array(point, dtype=float)
    grad = np.zeros_like(point)
    
    for i in range(len(point)):
        # 前向差分
        point_plus = point.copy()
        point_plus[i] += h
        f_plus = f(*point_plus)
        
        # 后向差分
        point_minus = point.copy()
        point_minus[i] -= h
        f_minus = f(*point_minus)
        
        # 中心差分
        grad[i] = (f_plus - f_minus) / (2 * h)
    
    return grad

def directional_derivative(f, point, direction, h=1e-6):
    """
    计算方向导数
    
    参数:
        f: 多元函数
        point: 求导点
        direction: 方向向量（会自动归一化）
        h: 数值微分步长
    """
    # 归一化方向向量
    direction = np.array(direction, dtype=float)
    direction = direction / np.linalg.norm(direction)
    
    # 计算梯度
    grad = gradient(f, point, h)
    
    # 方向导数 = 梯度 · 方向
    d_derivative = np.dot(grad, direction)
    
    return d_derivative, grad

# 示例：计算 f(x, y) = x² + y² + xy 的梯度和方向导数
f = lambda x, y: x**2 + y**2 + x*y
point = (1, 2)
direction = (1, 1)  # 45° 方向

print("计算 f(x, y) = x² + y² + xy 的梯度和方向导数：")

# 计算梯度
grad = gradient(f, point)
print(f"梯度在点 {point} 处: ∇f = {grad}")

# 计算方向导数
d_deriv, _ = directional_derivative(f, point, direction)
print(f"沿方向 {direction} 的方向导数: D_uf = {d_deriv}")

# 验证：手动计算
# ∂f/∂x = 2x + y, ∂f/∂y = 2y + x
# ∇f(1, 2) = (2*1 + 2, 2*2 + 1) = (4, 5)
# 方向 (1, 1) 归一化后为 (1/√2, 1/√2)
# D_uf = 4*(1/√2) + 5*(1/√2) = 9/√2 ≈ 6.364
print(f"手动计算: 9/√2 ≈ {9/np.sqrt(2):.6f}")

# 梯度方向（增长最快的方向）
grad_norm = grad / np.linalg.norm(grad)
print(f"\n梯度方向（归一化）: {grad_norm}")
grad_direction_deriv, _ = directional_derivative(f, point, grad_norm)
print(f"沿梯度方向的方向导数: {grad_direction_deriv}")

# 最大增长率 = 梯度的模
max_rate = np.linalg.norm(grad)
print(f"最大增长率: {max_rate:.6f}")
```

### 示例 4：全微分和切平面

```python
import numpy as np
import sympy as sp

def total_differential(f_sym, variables, point):
    """
    计算全微分
    
    参数:
        f_sym: 符号函数
        variables: 变量列表
        point: 求全微分的点
    """
    # 计算偏导数
    partials = [sp.diff(f_sym, var) for var in variables]
    
    # 代入具体点
    point_dict = {variables[i]: point[i] for i in range(len(variables))}
    partial_values = [partial.subs(point_dict) for partial in partials]
    
    # 构造全微分表达式
    dx, dy = sp.symbols('dx dy')
    df = sum(partial_values[i] * (variables[i] - point[i]) for i in range(len(variables)))
    
    # 切平面方程
    f_value = f_sym.subs(point_dict)
    tangent_plane = f_value + df
    
    return partial_values, tangent_plane

# 示例：计算 f(x, y) = x² + y² 的全微分和切平面
x, y = sp.symbols('x y')
f = x**2 + y**2

point = (1, 2)

print("计算 f(x, y) = x² + y² 的全微分和切平面：")

# 计算全微分
partials, tangent = total_differential(f, [x, y], point)
print(f"在点 {point} 处：")
print(f"∂f/∂x = {partials[0]}")
print(f"∂f/∂y = {partials[1]}")

# 切平面方程
f_value = 1**2 + 2**2 = 5
print(f"\n切平面方程:")
print(f"z - {f_value} = {partials[0]}(x - {point[0]}) + {partials[1]}(y - {point[1]})")
print(f"z = {tangent}")

# 验证近似效果
def f_num(x, y):
    return x**2 + y**2

def tangent_approx(x, y):
    return f_value + partials[0] * (x - point[0]) + partials[1] * (y - point[1])

# 在点附近比较
test_points = [(1.1, 2.1), (1.2, 2.0), (0.9, 1.8)]
print("\n切平面近似效果：")
for test_x, test_y in test_points:
    true_val = f_num(test_x, test_y)
    approx_val = tangent_approx(test_x, test_y)
    error = abs(true_val - approx_val)
    print(f"({test_x}, {test_y}): 真实={true_val:.6f}, 近似={approx_val:.6f}, 误差={error:.6f}")
```

### 示例 5：多元函数的极值

```python
import numpy as np
import sympy as sp

def find_critical_points(f_sym, variables):
    """
    寻找函数的临界点（驻点）
    
    参数:
        f_sym: 符号函数
        variables: 变量列表
    """
    # 计算偏导数
    gradients = [sp.diff(f_sym, var) for var in variables]
    
    # 解方程组 ∇f = 0
    solutions = sp.solve(gradients, variables, dict=True)
    
    return solutions

def classify_critical_point(f_sym, variables, point):
    """
    分类临界点（极大值、极小值、鞍点）
    
    参数:
        f_sym: 符号函数
        variables: 变量列表
        point: 临界点
    """
    # 计算二阶偏导数
    n = len(variables)
    hessian = sp.zeros(n, n)
    
    for i in range(n):
        for j in range(n):
            # 先对变量 i 求导，再对变量 j 求导
            hessian[i, j] = sp.diff(f_sym, variables[i], variables[j])
    
    # 代入临界点
    point_dict = {variables[i]: point[i] for i in range(n)}
    hessian_at_point = hessian.subs(point_dict)
    
    # 对于二元函数，使用判别式
    if n == 2:
        A = hessian_at_point[0, 0]
        B = hessian_at_point[0, 1]
        C = hessian_at_point[1, 1]
        
        Delta = A * C - B**2
        
        if Delta > 0:
            if A > 0:
                return "局部极小值"
            else:
                return "局部极大值"
        elif Delta < 0:
            return "鞍点"
        else:
            return "无法判断（需要更高阶判别法）"
    else:
        # 对于一般情况，使用 Hessian 的特征值
        eigenvalues = np.linalg.eigvals(np.array(hessian_at_point, dtype=float))
        
        if all(ev > 0 for ev in eigenvalues):
            return "局部极小值"
        elif all(ev < 0 for ev in eigenvalues):
            return "局部极大值"
        else:
            return "鞍点"

# 示例 1：f(x, y) = x² + y² + xy + x + y
x, y = sp.symbols('x y')
f1 = x**2 + y**2 + x*y + x + y

print("示例 1：f(x, y) = x² + y² + xy + x + y")

# 寻找临界点
critical_points1 = find_critical_points(f1, [x, y])
print(f"临界点: {critical_points1}")

# 分类临界点
for point_dict in critical_points1:
    point = (point_dict[x], point_dict[y])
    classification = classify_critical_point(f1, [x, y], point)
    f_value = f1.subs(point_dict)
    print(f"点 {point}: {classification}, f = {f_value}")

# 示例 2：f(x, y) = x³ - 3xy + y³
f2 = x**3 - 3*x*y + y**3

print("\n示例 2：f(x, y) = x³ - 3xy + y³")

# 寻找临界点
critical_points2 = find_critical_points(f2, [x, y])
print(f"临界点: {critical_points2}")

# 分类临界点
for point_dict in critical_points2:
    point = (point_dict[x], point_dict[y])
    classification = classify_critical_point(f2, [x, y], point)
    f_value = f2.subs(point_dict)
    print(f"点 {point}: {classification}, f = {f_value}")
```

## 4. 机器学习应用

### 应用 1：损失函数的梯度下降

在机器学习中，我们需要计算损失函数对参数的梯度来更新参数。

```python
import numpy as np

def mse_loss(y_true, y_pred):
    """均方误差损失"""
    return np.mean((y_true - y_pred)**2)

def mse_gradient(y_true, y_pred, X):
    """
    MSE 对参数的梯度（线性回归）
    
    参数:
        y_true: 真实值
        y_pred: 预测值
        X: 特征矩阵
    """
    n = len(y_true)
    gradient = -2 * X.T @ (y_true - y_pred) / n
    return gradient

# 示例：线性回归的梯度下降
np.random.seed(42)
n_samples = 100
n_features = 2

# 生成数据
X = np.random.randn(n_samples, n_features)
true_weights = np.array([2.0, -1.0])
y = X @ true_weights + 0.1 * np.random.randn(n_samples)

# 添加偏置项
X = np.column_stack([np.ones(n_samples), X])

# 初始化参数
weights = np.random.randn(n_features + 1)

# 梯度下降
learning_rate = 0.01
n_iterations = 1000

for i in range(n_iterations):
    y_pred = X @ weights
    gradient = mse_gradient(y, y_pred, X)
    weights = weights - learning_rate * gradient
    
    if i % 100 == 0:
        loss = mse_loss(y, y_pred)
        print(f"迭代 {i}: 损失 = {loss:.6f}")

print(f"\n最终权重: {weights}")
print(f"真实权重: {np.append([0], true_weights)}")  # 偏置项的真实权重是 0
```

### 应用 2：神经网络的反向传播

反向传播使用链式法则计算损失函数对每个权重的梯度。

```python
import numpy as np

def sigmoid(x):
    """Sigmoid 激活函数"""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Sigmoid 导数"""
    s = sigmoid(x)
    return s * (1 - s)

class SimpleNN:
    """简单的神经网络"""
    def __init__(self, input_size, hidden_size, output_size):
        # 初始化权重
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros(hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros(output_size)
    
    def forward(self, X):
        """前向传播"""
        self.z1 = X @ self.W1 + self.b1
        self.a1 = sigmoid(self.z1)
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2
    
    def backward(self, X, y):
        """反向传播"""
        m = X.shape[0]
        
        # 输出层的梯度
        dz2 = self.a2 - y
        dW2 = self.a1.T @ dz2 / m
        db2 = np.sum(dz2, axis=0) / m
        
        # 隐藏层的梯度
        da1 = dz2 @ self.W2.T
        dz1 = da1 * sigmoid_derivative(self.z1)
        dW1 = X.T @ dz1 / m
        db1 = np.sum(dz1, axis=0) / m
        
        return dW1, db1, dW2, db2

# 示例：训练一个简单的神经网络
np.random.seed(42)
input_size = 2
hidden_size = 3
output_size = 1

# 生成数据
X = np.random.randn(100, input_size)
y = (X[:, 0] > 0).astype(float).reshape(-1, 1)

# 创建神经网络
nn = SimpleNN(input_size, hidden_size, output_size)

# 训练
learning_rate = 0.1
n_epochs = 1000

for epoch in range(n_epochs):
    # 前向传播
    y_pred = nn.forward(X)
    
    # 计算损失
    loss = np.mean((y_pred - y)**2)
    
    # 反向传播
    dW1, db1, dW2, db2 = nn.backward(X, y)
    
    # 更新权重
    nn.W1 -= learning_rate * dW1
    nn.b1 -= learning_rate * db1
    nn.W2 -= learning_rate * dW2
    nn.b2 -= learning_rate * db2
    
    if epoch % 100 == 0:
        print(f"Epoch {epoch}: Loss = {loss:.6f}")

# 测试
y_pred = nn.forward(X)
accuracy = np.mean((y_pred > 0.5) == y)
print(f"\n准确率: {accuracy:.2%}")
```

## 根据题型整理的做题方法
### 偏导数核心要点

**偏导数计算**：将其他变量视为常数，对目标变量求导

**全微分**：$dz = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$

**方向导数**：$\frac{\partial f}{\partial \vec{l}} = \nabla f \cdot \vec{l_0}$

**梯度**：$\nabla f = (\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z})$

**链式法则**：
- $z = f(x,y), x=x(t), y=y(t)$：$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$
- 树形图法确定依赖关系

**隐函数求导**：$F(x,y,z)=0$，则$\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}$

**高阶偏导数**：混合偏导数连续则相等（Clairaut定理）

## 5. 易错点
⚠️ **常见错误**

1. **混淆偏导数和全微分**
   - 偏导数是单个方向的变化率
   - 全微分是所有方向变化的线性组合

2. **忽略可微性条件**
   - 偏导数存在不一定可微
   - 需要验证偏导数的连续性

3. **方向导数的计算**
   - 方向向量必须归一化
   - 方向导数 = 梯度 · 方向

✅ **最佳实践**

1. **理解梯度的几何意义**
   - 梯度指向增长最快的方向
   - 在优化中沿梯度反方向移动

2. **掌握链式法则**
   - 多元复合函数的求导
   - 在神经网络中非常重要

3. **熟练使用数值方法**
   - 数值梯度用于验证解析梯度
   - 在实际应用中经常用到

## 6. 相关概念

- [[02_Limits]] - 极限
- [[05_Derivatives]] - 导数
- [[18_Multivariable_Limits]] - 多元函数极限
- [[20_Multiple_Integrals]] - 重积分

## 练习（分层）

### A档（基础）
1. 计算 $f(x,y)=x^2y+xy^2$ 在点 $(1,2)$ 处的偏导数。
2. 验证 $f(x,y)=x^3y^2+xy$ 的混合偏导数相等性。
3. 求 $f(x,y)=e^{x+y}$ 的梯度和切平面方程。
4. 求 $f(x,y)=x^2+y^2$ 的偏导数并写出全微分。

### B档（进阶）
1. 利用链式法则求 $z=f(u,v)$ 的偏导数，其中 $u=x^2+y^2, v=xy$。
2. 证明：若偏导数在邻域内连续，则函数可微。
3. 计算函数 $f(x,y)=\ln(x^2+y^2)$ 的方向导数。
4. 求隐函数 $F(x,y)=0$ 给出的 $\frac{dy}{dx}$。

### C档（挑战）
1. 寻找函数 $f(x,y)=x^2-2xy+y^2+2x+2y$ 的极值点并分类。
2. 用 Hessian 矩阵分析 $f(x,y)=x^3-3xy+y^3$ 的临界点。
3. 证明混合偏导数连续时它们相等，并说明这一定理的边界条件。
4. 研究多元函数在神经网络损失函数中的梯度下降含义。

## 更多严格证明（Rudin风格）

### 证明1：混合偏导数相等

**定理**（克莱罗定理）：设 f 在开集 U ⊆ ℝ² 上定义，且混合偏导数 ∂²f/∂x∂y 和 ∂²f/∂y∂x 在 U 上连续，则：
∂²f/∂x∂y = ∂²f/∂y∂x

**证明**：
设 (x₀, y₀) ∈ U，考虑：
Δ(x, y) = [f(x₀ + h, y₀ + k) - f(x₀, y₀ + k)] - [f(x₀ + h, y₀) - f(x₀, y₀)]

令 g₁(x) = f(x, y₀ + k) - f(x, y₀)，则：
Δ(h, k) = g₁(x₀ + h) - g₁(x₀)

由中值定理，存在 θ₁ ∈ (0, 1)，使得：
Δ(h, k) = h g₁'(x₀ + θ₁h) = h[∂f/∂x(x₀ + θ₁h, y₀ + k) - ∂f/∂x(x₀ + θ₁h, y₀)]

令 g₂(y) = ∂f/∂x(x₀ + θ₁h, y)，则：
Δ(h, k) = h[g₂(y₀ + k) - g₂(y₀)]

由中值定理，存在 θ₂ ∈ (0, 1)，使得：
Δ(h, k) = h k g₂'(y₀ + θ₂k) = h k ∂²f/∂y∂x(x₀ + θ₁h, y₀ + θ₂k)

类似地，交换顺序可得：
Δ(h, k) = h k ∂²f/∂x∂y(x₀ + θ₁'h, y₀ + θ₂'k)

因此：
∂²f/∂y∂x(x₀ + θ₁h, y₀ + θ₂k) = ∂²f/∂x∂y(x₀ + θ₁'h, y₀ + θ₂'k)

令 h, k → 0，由连续性得：
∂²f/∂y∂x(x₀, y₀) = ∂²f/∂x∂y(x₀, y₀)

### 证明2：链式法则（多元）

**定理**（多元链式法则）：设 z = f(x, y) 和 x = g(t)，y = h(t) 都可导，则：
dz/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt)

**证明**：
设 Δt ≠ 0，Δx = g(t + Δt) - g(t)，Δy = h(t + Δt) - h(t)，Δz = f(x + Δx, y + Δy) - f(x, y)。

由于 f 可微：
Δz = (∂f/∂x)Δx + (∂f/∂y)Δy + ε₁Δx + ε₂Δy

其中 ε₁, ε₂ → 0 当 (Δx, Δy) → (0, 0)。

因此：
Δz/Δt = (∂f/∂x)(Δx/Δt) + (∂f/∂y)(Δy/Δt) + ε₁(Δx/Δt) + ε₂(Δy/Δt)

令 Δt → 0，得：
dz/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt)

## 6. 更多例题

### 例题1：计算偏导数

**问题**：设 f(x, y) = x²y + xy²，计算 ∂f/∂x 和 ∂f/∂y。

**解**：
∂f/∂x = 2xy + y²
∂f/∂y = x² + 2xy

### 例题2：计算方向导数

**问题**：设 f(x, y) = x² + y²，计算 f 在点 (1, 1) 处沿方向 v = (1, 1)/√2 的方向导数。

**解**：
∇f(x, y) = (2x, 2y)
∇f(1, 1) = (2, 2)

方向导数 Dᵥf(1, 1) = ∇f(1, 1) · v = (2, 2) · (1/√2, 1/√2) = 2√2

### 例题3：隐函数求导

**问题**：设 x² + y² = 1，求 dy/dx。

**解**：对等式两边对 x 求导：
2x + 2y(dy/dx) = 0

解得：
dy/dx = -x/y

## 8. 更多应用

### 1. 梯度下降算法

梯度 ∇f(x) 指示函数 f 增长最快的方向，因此梯度下降使用 -∇f(x)。

### 2. 反向传播

链式法则用于计算神经网络中损失函数对各参数的梯度。

## 7. 更多习题

### 基础题

1. 设 f(x, y) = x³y + xy³，计算 ∂f/∂x 和 ∂f/∂y。

2. 计算函数 f(x, y) = eˣ⁺ʸ 在点 (0, 0) 处的梯度。

3. 设 x² + y² + z² = 1，求 ∂z/∂x。

### 进阶题

4. 证明混合偏导数相等定理（克莱罗定理）。

5. 设 f(x, y) = x² + y²，验证克莱罗定理。

6. 计算函数 f(x, y) = x²y + xy² 的所有二阶偏导数。

### 挑战题

7. 在深度学习中，为什么需要计算二阶导数？

8. 证明：如果 f 是凸函数，则其 Hessian 矩阵是半正定的。

##参考资料

- 数学分析（第5版）- 华东师范大学数学系
- 高等数学（第八版）- 同济大学数学科学学院
- 托马斯微积分（第十版）- Thomas
## 10. 总结
### 10.1 重要定义
1. 偏导数：保持其他变量不变，对一个变量求导
2. 全微分：$dz = f_x dx + f_y dy$
3. 方向导数：沿任意方向的导数
4. 梯度：$\nabla f = (f_x, f_y)$，函数增长最快的方向

### 10.2 重要定理
1. 可微必连续：全微分存在则函数连续
2. 可微必偏导存在：全微分存在则偏导数存在
3. Clairaut定理：混合偏导数连续则相等
4. 梯度与方向导数关系：方向导数等于梯度与方向单位向量的点积

### 10.3 重要证明
1. 可微必连续的证明：利用全微分定义
2. Clairaut定理的证明：利用偏导数的定义

### 10.4 重要性质
1. 偏导数描述函数沿坐标轴方向的变化率
2. 全微分是函数增量的线性近似
3. 梯度指向函数增长最快的方向
4. 方向导数是梯度在该方向的分量

## 11. 练习（分层）
本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 计算 $f(x,y)=x^2y+xy^2$ 在点 $(1,2)$ 处的偏导数。
2. 计算 $f(x,y)=e^{x+y}$ 在点 $(0,0)$ 处的梯度。
3. 设 $x^2+y^2+z^2=1$，求 $\partial z/\partial x$。
4. 求函数 $f(x,y)=x^2+y^2$ 的全微分，并写出在 $(1,1)$ 处的线性近似。

### B档（进阶）
1. 证明混合偏导数相等定理（Clairaut 定理）。
2. 设 $f(x,y)=x^2+y^2$，验证 Clairaut 定理。
3. 计算函数 $f(x,y)=x^2y+xy^2$ 的所有二阶偏导数。
4. 计算函数 $z=f(u,v)$ 的链式法则，其中 $u=x^2+y^2,\ v=xy$。

### C档（挑战）
1. 证明：如果 $f$ 在某点可微，则它在该点连续。
2. 构造一个在原点偏导数都存在但不可微的二维函数，并说明原因。
3. 用 Hessian 矩阵分析 $f(x,y)=x^2-2xy+y^2+2x+2y$ 的极值点。
4. 说明偏导数和梯度在神经网络反向传播中的作用。



