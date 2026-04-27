---
type: concept

topic: derivatives

category: calculus

difficulty: intermediate

prerequisites:
    - [[02_Limits]]

acm_relevant: false

created: 2026-02-20

status: complete

subject: calculus
chapter: 05
updated: 2026-04-27
---

# 导数 (Derivatives)

## 📌 学习目标

- 理解导数定义（极限）与几何意义（切线斜率/瞬时变化率）
- 熟练选择并使用求导法则（和差积商、链式、对数求导、隐函数/参数方程）
- 能把导数与优化连接起来（梯度、方向导数、Hessian 的直觉用途）

## ✅ 先修

- [[02_Limits]]
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层

- **基础**：导数定义 + 常用求导公式 + 基本运算法则
- **进阶**：链式法则/隐函数/参数方程/高阶导数；可导必连续与应用
- **拓展**：多元微分（梯度/Jacobian/Hessian）与机器学习中的反向传播

## 1. 定义

**直观理解**：
导数是微积分的核心概念，描述函数在某一点处的瞬时变化率。几何上，导数表示函数曲线在该点的切线斜率。在机器学习中，导数是优化算法（如梯度下降）的基础。

想象你开车，速度表显示的是你的瞬时速度。这个瞬时速度就是你行驶距离对时间的导数。如果你在某时刻加速，你的加速度就是速度对时间的导数。在机器学习中，损失函数的导数告诉我们如何调整参数以最小化损失。

## 2. 定理与性质

### 3Blue1Brown 的几何直觉

**导数的本质：微小推动引起的微小变化**

3Blue1Brown (Grant Sanderson) 提供了一个非常直观的理解导数的方法：**把导数看作是"微小推动"（tiny nudge）引起的响应**。

不要只把导数看作是"曲线的斜率"，而要思考：**当输入发生一个极其微小的变化 dx 时，输出会发生多大的变化 dy？**

```
dy/dx = 当输入改变 dx 时，输出改变 dy 的比例
```

这个比例告诉我们变化的"速率"或"敏感度"。

#### 可视化：正方形面积的变化

考虑函数 f(x) = x²，代表边长为 x 的正方形的面积。

当我们把边长增加一个微小的量 dx 时，面积会如何变化？

```
新面积 = (x + dx)² = x² + 2x·dx + (dx)²
面积变化 = 新面积 - 旧面积 = 2x·dx + (dx)²
```

在几何上，这个变化由三部分组成：
1. **两个细长的矩形**：每个面积为 x·dx，总共 2x·dx
2. **一个微小的正方形**：面积为 (dx)²

**关键洞察**：当 dx 非常小（趋近于 0）时，(dx)² 是可以忽略的！例如，如果 dx = 0.0001，那么 (dx)² = 0.00000001，相比之下可以忽略不计。

因此，面积变化 ≈ 2x·dx

而导数就是：dy/dx ≈ 2x·dx / dx = 2x

这就是为什么 (x²)' = 2x！

```
┌─────────────┐
│  x²        │ 原面积
│  ┌─────┐   │
│  │dx   │   │ 新增面积
│  │  ├─┐   │ 两个细长矩形（2x·dx）
│  │  │ │   │ + 一个微小正方形（dx²）
└──┴──┴─┴───┘
  x   dx
```

#### 立方体积的变化

对于 f(x) = x³（边长为 x 的立方体的体积）：

当边长增加 dx 时，体积增加的部分主要是**三个正方形面**：
- 每个面的面积为 x²
- 厚度为 dx
- 总增加量 ≈ 3x²·dx

其他边缘和角落的体积与 $dx^2$ 或 $dx^3$ 成正比，当 $dx \to 0$ 时可以忽略。

因此，(x³)' = 3x²

#### 幂法则的几何直觉

通过观察模式：
- (x¹)' = 1·x⁰ = 1（一维长度，dx）
- (x²)' = 2·x¹ = 2x（二维面积，2个矩形）
- (x³)' = 3·x² = 3x²（三维体积，3个面）

**幂法则**：(xⁿ)' = n·xⁿ⁻¹

这个公式的几何含义是：n 维"超立方体"有 n 个 (n-1) 维的"面"，当边长增加 dx 时，每个面的增加量是 xⁿ⁻¹·dx。

#### 倒数函数的导数

对于 f(x) = 1/x，可以想象一个面积为 1 的矩形：
- 宽度为 x
- 高度为 1/x

当宽度增加 dx 时，为了保持面积不变，高度必须减少 dy。

新增面积（右侧）≈ x·dy（负值，因为高度减少）
减少面积（顶部）≈ (1/x)·dx

为了保持面积不变：x·dy + (1/x)·dx = 0

因此：dy/dx = -1/x²

这就是为什么 (1/x)' = -1/x²！

### 导数的定义

函数 f(x) 在点 a 处的导数定义为：
$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

这个定义告诉我们：
- 计算函数在 a 点附近的变化率
- h 趋近于 0 时得到瞬时变化率
- 如果极限不存在，则函数在该点不可导

### 导数的几何意义

- **斜率**：f'(a) 是曲线 y = f(x) 在点 (a, f(a)) 处切线的斜率
- **切线方程**：y = f(a) + f'(a)(x - a)
- **单调性**：f'(a) > 0 时函数递增，f'(a) < 0 时函数递减
- **极值点**：f'(a) = 0 时，a 可能是极值点

### 常见导数公式

#### 基本函数的导数

1. **常数**：$(C)' = 0$
2. **幂函数**：$(x^n)' = n \cdot x^{n-1}$
3. **指数函数**：$(e^x)' = e^x$, $(a^x)' = a^x \cdot \ln(a)$
4. **对数函数**：$(\ln x)' = \frac{1}{x}$, $(\log_a x)' = \frac{1}{x \cdot \ln(a)}$
5. **三角函数**：
   - $(\sin x)' = \cos x$
   - $(\cos x)' = -\sin x$
   - $(\tan x)' = \sec^2 x$

#### 导数的运算法则

1. **常数倍法则**：$(C \cdot f(x))' = C \cdot f'(x)$
2. **和差法则**：$(f(x) \pm g(x))' = f'(x) \pm g'(x)$
3. **乘积法则**：$(f(x) \cdot g(x))' = f'(x) \cdot g(x) + f(x) \cdot g'(x)$
4. **商法则**：$(\frac{f(x)}{g(x)})' = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{g(x)^2}$
5. **链式法则**：$(f(g(x)))' = f'(g(x)) \cdot g'(x)$

### 高阶导数

- **二阶导数**：f''(x) = (f'(x))'，描述函数曲率
- **n 阶导数**：f^(n)(x)，表示连续求导 n 次
- **应用**：泰勒展开、凸性分析、牛顿法

### 偏导数

对于多元函数 $f(x_1, x_2, \ldots, x_n)$，对第 $i$ 个变量的偏导数为：
$$\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(x_1, \ldots, x_i+h, \ldots, x_n) - f(x_1, \ldots, x_i, \ldots, x_n)}{h}$$

偏导数描述函数在某个方向上的变化率，是梯度向量的分量。

### 梯度

函数 $f(\mathbf{x})$ 的梯度是偏导数组成的向量：
$$\nabla f(\mathbf{x}) = \left[\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n}\right]^T$$

梯度的性质：
- 指向函数增长最快的方向
- 梯度的大小表示增长的速率
- 在优化中，沿梯度反方向移动可以最小化函数

## 3. 代码示例

### 示例 1：数值求导

```python
import numpy as np

def forward_difference(f, x, h=1e-6):
    """前向差分法"""
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h=1e-6):
    """后向差分法"""
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h=1e-6):
    """中心差分法（更精确）"""
    return (f(x + h) - f(x - h)) / (2 * h)

# 测试函数
f = lambda x: x**3 - 2*x**2 + 3*x - 1
df_analytical = lambda x: 3*x**2 - 4*x + 3  # 解析导数

x = 2.0
h = 1e-6

print(f"解析解: f'({x}) = {df_analytical(x):.10f}")
print(f"前向差分: f'({x}) = {forward_difference(f, x, h):.10f}")
print(f"后向差分: f'({x}) = {backward_difference(f, x, h):.10f}")
print(f"中心差分: f'({x}) = {central_difference(f, x, h):.10f}")

# 比较误差
error_forward = abs(forward_difference(f, x, h) - df_analytical(x))
error_backward = abs(backward_difference(f, x, h) - df_analytical(x))
error_central = abs(central_difference(f, x, h) - df_analytical(x))

print(f"\n误差比较:")
print(f"前向差分误差: {error_forward:.2e}")
print(f"后向差分误差: {error_backward:.2e}")
print(f"中心差分误差: {error_central:.2e}")
```

### 示例 2：多元函数的梯度

```python
def numerical_gradient(f, x, h=1e-6):
    """
    计算多元函数的数值梯度
    
    参数:
        f: 多元函数
        x: 输入向量
        h: 步长
    """
    x = np.array(x, dtype=float)
    grad = np.zeros_like(x)
    
    for i in range(len(x)):
        # 前向差分
        x_plus = x.copy()
        x_plus[i] += h
        f_plus = f(x_plus)
        
        # 后向差分
        x_minus = x.copy()
        x_minus[i] -= h
        f_minus = f(x_minus)
        
        # 中心差分
        grad[i] = (f_plus - f_minus) / (2 * h)
    
    return grad

# 示例函数: f(x, y) = x² + y²
f = lambda x: x[0]**2 + x[1]**2
x = [1, 2]

grad = numerical_gradient(f, x)
print(f"函数 f(x,y) = x² + y² 在点 {x} 的梯度: {grad}")
print(f"解析解: ∇f = [2x, 2y] = {[2*x[0], 2*x[1]]}")

# 示例函数: f(x, y, z) = x*y*z + x² + y² + z²
f2 = lambda x: x[0]*x[1]*x[2] + x[0]**2 + x[1]**2 + x[2]**2
x2 = [1, 2, 3]

grad2 = numerical_gradient(f2, x2)
print(f"\n函数在点 {x2} 的梯度: {grad2}")
```

### 示例 3：激活函数及其导数

```python
import numpy as np

# Sigmoid 函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Sigmoid 导数: σ'(x) = σ(x)(1 - σ(x))"""
    s = sigmoid(x)
    return s * (1 - s)

# Tanh 函数
def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    """Tanh 导数: tanh'(x) = 1 - tanh²(x)"""
    return 1 - np.tanh(x)**2

# ReLU 函数
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    """ReLU 导数: ReLU'(x) = 1 if x > 0 else 0"""
    return (x > 0).astype(float)

# Leaky ReLU 函数
def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def leaky_relu_derivative(x, alpha=0.01):
    """Leaky ReLU 导数"""
    return np.where(x > 0, 1, alpha)

# 测试
x = np.array([-2, -1, 0, 1, 2])

print("Sigmoid:")
print(f"值: {sigmoid(x)}")
print(f"导数: {sigmoid_derivative(x)}")

print("\nTanh:")
print(f"值: {tanh(x)}")
print(f"导数: {tanh_derivative(x)}")

print("\nReLU:")
print(f"值: {relu(x)}")
print(f"导数: {relu_derivative(x)}")

print("\nLeaky ReLU:")
print(f"值: {leaky_relu(x)}")
print(f"导数: {leaky_relu_derivative(x)}")
```

### 示例 4：自动微分（使用 PyTorch）

```python
import torch

# 示例 1：标量函数的导数
x = torch.tensor(2.0, requires_grad=True)
y = x**3 - 2*x**2 + 3*x - 1

# 计算梯度
y.backward()

print(f"函数值: y = {y.item():.4f}")
print(f"导数: dy/dx = {x.grad.item():.4f}")
print(f"解析解: dy/dx = 3*2² - 4*2 + 3 = {3*2**2 - 4*2 + 3}")

# 示例 2：多元函数的梯度
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x[0]*x[1]*x[2] + x[0]**2 + x[1]**2 + x[2]**2

# 计算梯度
y.backward()

print(f"\n函数值: y = {y.item():.4f}")
print(f"梯度: ∇y = {x.grad.numpy()}")
print(f"解析解: ∇y = [yz+2x, xz+2y, xy+2z] = {[1*2*3+2*1, 1*2*3+2*2, 1*2*3+2*3]}")

# 示例 3：计算高阶导数
x = torch.tensor(2.0, requires_grad=True)
y = x**4

# 一阶导数
dy_dx = torch.autograd.grad(y, x, create_graph=True)[0]
print(f"\n一阶导数: dy/dx = {dy_dx.item():.4f}")

# 二阶导数
d2y_dx2 = torch.autograd.grad(dy_dx, x)[0]
print(f"二阶导数: d²y/dx² = {d2y_dx2.item():.4f}")

# 三阶导数
d3y_dx3 = torch.autograd.grad(d2y_dx2, x)[0]
print(f"三阶导数: d³y/dx³ = {d3y_dx3.item():.4f}")
```

### 示例 5：使用 SymPy 进行符号求导

```python
from sympy import symbols, diff, sin, cos, exp, log, sqrt

# 定义符号变量
x, y, z = symbols('x y z')

# 示例 1：基本函数的导数
f1 = x**3 - 2*x**2 + 3*x - 1
df1 = diff(f1, x)
print(f"f(x) = {f1}")
print(f"f'(x) = {df1}")

# 示例 2：复合函数的导数
f2 = sin(x**2)
df2 = diff(f2, x)
print(f"\nf(x) = sin(x²)")
print(f"f'(x) = {df2}")

# 示例 3：多元函数的偏导数
f3 = x*y*z + x**2 + y**2 + z**2
df3_dx = diff(f3, x)
df3_dy = diff(f3, y)
df3_dz = diff(f3, z)
print(f"\nf(x,y,z) = {f3}")
print(f"∂f/∂x = {df3_dx}")
print(f"∂f/∂y = {df3_dy}")
print(f"∂f/∂z = {df3_dz}")

# 示例 4：高阶导数
f4 = x**4
df4 = diff(f4, x, 2)  # 二阶导数
print(f"\nf(x) = {f4}")
print(f"f''(x) = {df4}")

# 示例 5：计算梯度
f5 = x**2 + y**2
grad_f5 = [diff(f5, x), diff(f5, y)]
print(f"\nf(x,y) = {f5}")
print(f"∇f = [{grad_f5[0]}, {grad_f5[1]}]")
```

### 示例 6：Jacobian 矩阵和 Hessian 矩阵

```python
import torch

def jacobian(f, x):
    """计算 Jacobian 矩阵"""
    return torch.autograd.functional.jacobian(f, x)

def hessian(f, x):
    """计算 Hessian 矩阵"""
    return torch.autograd.functional.hessian(f, x)

# 示例 1：向量值函数的 Jacobian
def f_vector(x):
    """向量值函数 f: R³ → R²"""
    return torch.tensor([x[0]**2 + x[1], x[1]*x[2]])

x = torch.tensor([1.0, 2.0, 3.0])
J = jacobian(f_vector, x)

print("向量值函数 f(x) = [x₁² + x₂, x₂·x₃]")
print(f"在点 {x} 的 Jacobian 矩阵:")
print(J)

# 示例 2：标量函数的 Hessian
def f_scalar(x):
    """标量函数 f: R² → R"""
    return x[0]**3 + x[1]**2 + x[0]*x[1]

x = torch.tensor([1.0, 2.0])
H = hessian(f_scalar, x)

print(f"\n标量函数 f(x) = x₁³ + x₂² + x₁·x₂")
print(f"在点 {x} 的 Hessian 矩阵:")
print(H)

# 示例 3：使用 Hessian 进行牛顿法
def newton_method(f, x0, max_iter=10, tol=1e-6):
    """使用 Hessian 的牛顿法优化"""
    x = x0.clone().detach().requires_grad_(True)
    
    for i in range(max_iter):
        # 计算梯度和 Hessian
        y = f(x)
        grad = torch.autograd.grad(y, x, create_graph=True)[0]
        hess = torch.autograd.functional.hessian(f, x)
        
        # 检查收敛
        if torch.norm(grad) < tol:
            print(f"在 {i} 次迭代后收敛")
            break
        
        # 更新: x = x - H⁻¹·∇f
        delta = torch.linalg.solve(hess, grad)
        x = x - delta
    
    return x.detach()

# 优化 f(x) = x₁² + 2*x₂²
f_quad = lambda x: x[0]**2 + 2*x[1]**2
x0 = torch.tensor([10.0, 10.0])
x_opt = newton_method(f_quad, x0)

print(f"\n优化 f(x) = x₁² + 2*x₂²")
print(f"初始点: {x0}")
print(f"最优解: {x_opt}")
print(f"最优值: {f_quad(x_opt):.6f}")
```

## 4. 机器学习应用

### 应用 1：梯度下降中的导数

```python
import numpy as np

def gradient_descent(f, df, x0, learning_rate=0.01, max_iter=100):
    """梯度下降算法"""
    x = np.array(x0, dtype=float)
    history = [x.copy()]
    
    for i in range(max_iter):
        # 计算梯度（导数）
        gradient = df(x)
        
        # 更新参数
        x = x - learning_rate * gradient
        history.append(x.copy())
    
    return x, history

# 示例：最小化二次函数 f(x) = x²
f = lambda x: x**2
df = lambda x: 2*x  # 导数

x0 = 10.0
x_opt, history = gradient_descent(f, df, x0, learning_rate=0.1, max_iter=50)

print(f"最小化 f(x) = x²")
print(f"初始值: {x0}")
print(f"最优解: {x_opt[-1]:.6f}")
print(f"最优值: {f(x_opt[-1]):.6f}")
```

### 应用 2：反向传播中的链式法则

```python
# 简单的神经网络层
class LinearLayer:
    def __init__(self, input_dim, output_dim):
        self.W = np.random.randn(input_dim, output_dim) * 0.01
        self.b = np.zeros(output_dim)
        self.cache = None
    
    def forward(self, x):
        """前向传播"""
        self.cache = x
        return x @ self.W + self.b
    
    def backward(self, dout):
        """反向传播（使用链式法则）"""
        x = self.cache
        
        # 对输入的导数：∂L/∂x = ∂L/∂y · ∂y/∂x = dout · Wᵀ
        dx = dout @ self.W.T
        
        # 对权重的导数：∂L/∂W = ∂L/∂y · ∂y/∂W = xᵀ · dout
        dW = x.T @ dout
        
        # 对偏置的导数：∂L/∂b = ∂L/∂y · ∂y/∂b = dout
        db = np.sum(dout, axis=0)
        
        return dx, dW, db

# 激活函数层
class ReLU:
    def __init__(self):
        self.cache = None
    
    def forward(self, x):
        """前向传播"""
        self.cache = x
        return np.maximum(0, x)
    
    def backward(self, dout):
        """反向传播"""
        x = self.cache
        # ReLU 导数: 1 if x > 0 else 0
        drelu = (x > 0).astype(float)
        # 链式法则: ∂L/∂x = ∂L/∂y · ∂y/∂x
        return dout * drelu

# 测试网络
np.random.seed(42)
x = np.random.randn(1, 3)  # 输入
layer1 = LinearLayer(3, 4)
relu = ReLU()
layer2 = LinearLayer(4, 2)

# 前向传播
y1 = layer1.forward(x)
a1 = relu.forward(y1)
y2 = layer2.forward(a1)

print("前向传播:")
print(f"输入: {x}")
print(f"第一层输出: {y1}")
print(f"ReLU 输出: {a1}")
print(f"第二层输出: {y2}")

# 假设损失函数的导数（来自上一层）
dout = np.array([[1.0, -1.0]])

# 反向传播
d_relu, dW2, db2 = layer2.backward(dout)
d_y1 = relu.backward(d_relu)
d_x, dW1, db1 = layer1.backward(d_y1)

print("\n反向传播:")
print(f"∂L/∂W2:\n{dW2}")
print(f"∂L/∂b2: {db2}")
print(f"∂L/∂W1:\n{dW1}")
print(f"∂L/∂b1: {db1}")
```

### 应用 3：损失函数的导数

```python
import numpy as np

# 均方误差损失
def mse_loss(y_true, y_pred):
    """均方误差损失"""
    return np.mean((y_true - y_pred)**2)

def mse_loss_gradient(y_true, y_pred):
    """MSE 损失对预测值的导数"""
    n = len(y_true)
    return -2 * (y_true - y_pred) / n

# 交叉熵损失
def cross_entropy_loss(y_true, y_pred):
    """交叉熵损失（y_true 是 one-hot 编码）"""
    epsilon = 1e-15  # 避免对数为 0
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.sum(y_true * np.log(y_pred))

def cross_entropy_loss_gradient(y_true, y_pred):
    """交叉熵损失对预测值的导数"""
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -y_true / y_pred

# 测试
y_true = np.array([1, 0, 0])  # one-hot 编码
y_pred = np.array([0.7, 0.2, 0.1])  # softmax 输出

print("损失函数的导数:")
print(f"真实标签: {y_true}")
print(f"预测值: {y_pred}")
print(f"\n交叉熵损失: {cross_entropy_loss(y_true, y_pred):.4f}")
print(f"损失对预测值的导数: {cross_entropy_loss_gradient(y_true, y_pred)}")

# 更新预测值
learning_rate = 0.1
y_pred_new = y_pred - learning_rate * cross_entropy_loss_gradient(y_true, y_pred)
# 重新归一化（因为这是概率分布）
y_pred_new = np.maximum(y_pred_new, 0)
y_pred_new = y_pred_new / np.sum(y_pred_new)

print(f"\n更新后的预测值: {y_pred_new}")
print(f"更新后的损失: {cross_entropy_loss(y_true, y_pred_new):.4f}")
```

### 应用 4：自动微分在优化中的应用

```python
import torch

# 使用自动微分进行优化
def minimize_with_autograd(f, x0, learning_rate=0.1, max_iter=100):
    """使用自动微分最小化函数"""
    x = torch.tensor(x0, requires_grad=True)
    
    for i in range(max_iter):
        # 前向传播
        y = f(x)
        
        # 反向传播（自动计算导数）
        y.backward()
        
        # 更新参数
        with torch.no_grad():
            x -= learning_rate * x.grad
            x.grad.zero_()  # 清零梯度
    
    return x.detach().numpy()

# 示例：最小化 Rosenbrock 函数
def rosenbrock(x):
    """Rosenbrock 函数（优化测试函数）"""
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

x0 = [-1.5, 2.0]
x_opt = minimize_with_autograd(rosenbrock, x0, learning_rate=0.001, max_iter=5000)

print(f"最小化 Rosenbrock 函数")
print(f"初始点: {x0}")
print(f"最优解: {x_opt}")
print(f"最优值: {rosenbrock(torch.tensor(x_opt)):.6f}")
print(f"理论最优解: [1.0, 1.0]")
```

### 应用 5：二阶导数（Hessian）在优化中的应用

```python
import torch

def newton_method_autograd(f, x0, max_iter=10, tol=1e-6):
    """使用自动微分的牛顿法"""
    x = torch.tensor(x0, requires_grad=True)
    
    for i in range(max_iter):
        # 计算函数值
        y = f(x)
        
        # 计算梯度
        grad = torch.autograd.grad(y, x, create_graph=True)[0]
        
        # 计算梯度范数
        grad_norm = torch.norm(grad)
        
        if grad_norm < tol:
            print(f"在 {i} 次迭代后收敛")
            break
        
        # 计算 Hessian
        hess = torch.autograd.functional.hessian(f, x)
        
        # 更新: x = x - H⁻¹·∇f
        delta = torch.linalg.solve(hess, grad)
        
        with torch.no_grad():
            x -= delta
    
    return x.detach().numpy()

# 示例：最小化二次函数
def quadratic(x):
    return 2*x[0]**2 + x[1]**2 + x[0]*x[1]

x0 = [5.0, 5.0]
x_opt = newton_method_autograd(quadratic, x0)

print(f"最小化二次函数 f(x) = 2x₁² + x₂² + x₁x₂")
print(f"初始点: {x0}")
print(f"最优解: {x_opt}")
print(f"最优值: {quadratic(torch.tensor(x_opt)):.6f}")
```

## 根据题型整理的做题方法

### 求导的四步法

遇到求导题目，按以下步骤系统分析。

#### 📋 第一步：识别函数类型

首先判断函数属于哪种类型，选择对应的求导方法：

| 函数类型 | 特点 | 主要方法 |
|---------|------|---------|
| **基本初等函数** | 幂、指、对、三角、反三角 | 直接套用公式 |
| **四则运算** | 加减乘除组合 | 和差积商法则 |
| **复合函数** | 函数套函数 | 链式法则 |
| **隐函数** | $F(x,y)=0$ 形式 | 隐函数求导 |
| **参数方程** | $x=x(t), y=y(t)$ | 参数方程求导 |
| **反函数** | $y=f^{-1}(x)$ | 反函数求导公式 |

#### 🔧 第二步：选择求导方法

根据函数结构确定求导策略：

```
单一函数 → 基本公式
↓
函数组合 → 分析组合方式
    ├── 加减 → 分别求导
    ├── 乘法 → 乘积法则
    ├── 除法 → 商法则
    └── 复合 → 链式法则
↓
特殊形式 → 特殊方法
    ├── 隐函数 → 两边对x求导
    ├── 参数方程 → dy/dx = (dy/dt)/(dx/dt)
    ├── 对数求导 → 先取对数再求导
    └── 高阶导数 → 逐次求导找规律
```

#### ✏️ 第三步：执行求导

注意以下细节：
1. **链式法则**：从外到内，层层求导，相乘连接
2. **乘积法则**：$(uv)' = u'v + uv'$，不要漏项
3. **商法则**：$\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$，注意顺序和分母
4. **符号**：三角函数求导注意正负号变化

#### ✅ 第四步：验证与化简

- 化简结果，合并同类项
- 检查定义域，注意分母不为零
- 可用数值方法验证

### 💡 核心技巧与常用结论

#### 1. 基本导数公式速查表

**必须熟记**，考试可直接使用：

| 函数 $f(x)$ | 导数 $f'(x)$ |
|------------|-------------|
| $C$（常数） | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\log_a x$ | $\frac{1}{x \ln a}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\cot x$ | $-\csc^2 x$ |
| $\sec x$ | $\sec x \tan x$ |
| $\csc x$ | $-\csc x \cot x$ |
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ |
| $\arccos x$ | $-\frac{1}{\sqrt{1-x^2}}$ |
| $\arctan x$ | $\frac{1}{1+x^2}$ |
| $\text{arccot } x$ | $-\frac{1}{1+x^2}$ |

**记忆技巧**：
- 反三角函数的导数分母都是 $1 \pm x^2$ 的某种形式
- 余函数的导数都有负号（$\cos, \cot, \csc, \arccos, \text{arccot}$）

#### 2. 链式法则的口诀

**"外导内不导，乘以内导"**

$$\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$$

**操作步骤**：
1. 识别外层函数 $f$ 和内层函数 $g$
2. 对外层函数求导，内层不变
3. 乘以内层函数的导数

**示例**：求 $(\sin x^2)'$
- 外层：$\sin u$，导数 $\cos u$
- 内层：$x^2$，导数 $2x$
- 结果：$\cos x^2 \cdot 2x = 2x \cos x^2$

**多层复合**：从外到内，逐层求导相乘
$$(f(g(h(x))))' = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x)$$

#### 3. 对数求导法

**适用场景**：
- 幂指函数 $y = u(x)^{v(x)}$
- 多个因子的乘除运算

**方法步骤**：
1. 两边取自然对数：$\ln y = \ln f(x)$
2. 对 $x$ 求导：$\frac{y'}{y} = \frac{d}{dx}\ln f(x)$
3. 解出 $y'$：$y' = y \cdot \frac{d}{dx}\ln f(x)$

**示例**：求 $y = x^x$ 的导数
$$\ln y = x \ln x$$
$$\frac{y'}{y} = \ln x + x \cdot \frac{1}{x} = \ln x + 1$$
$$y' = x^x (\ln x + 1)$$

#### 4. 隐函数求导法

**核心思想**：将 $y$ 视为 $x$ 的函数，方程两边对 $x$ 求导

**操作步骤**：
1. 方程两边对 $x$ 求导
2. 遇到 $y$ 时用链式法则：$\frac{d}{dx}f(y) = f'(y) \cdot y'$
3. 解出 $y'$

**示例**：求 $x^2 + y^2 = 1$ 的 $\frac{dy}{dx}$
$$2x + 2y \cdot y' = 0$$
$$y' = -\frac{x}{y}$$

#### 5. 参数方程求导

**公式**：
$$\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} = \frac{y'(t)}{x'(t)}$$

**二阶导数**：
$$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}}$$

**示例**：$\begin{cases} x = t^2 \\ y = t^3 \end{cases}$
$$\frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2}$$
$$\frac{d^2y}{dx^2} = \frac{\frac{3}{2}}{2t} = \frac{3}{4t}$$

#### 6. 高阶导数求法

**常用公式**：
- $(x^n)^{(n)} = n!$
- $(e^x)^{(n)} = e^x$
- $(\sin x)^{(n)} = \sin(x + \frac{n\pi}{2})$
- $(\cos x)^{(n)} = \cos(x + \frac{n\pi}{2})$
- $(\frac{1}{x})^{(n)} = \frac{(-1)^n n!}{x^{n+1}}$

**莱布尼茨公式**：
$$(uv)^{(n)} = \sum_{k=0}^{n} C_n^k u^{(k)} v^{(n-k)}$$

#### 7. 求导中的常见陷阱

**陷阱一：乘积法则应用错误**
- ❌ $(uv)' = u'v'$
- ✅ $(uv)' = u'v + uv'$

**陷阱二：复合函数漏项**
- ❌ $(\sin x^2)' = \cos x^2$
- ✅ $(\sin x^2)' = 2x \cos x^2$

**陷阱三：商法则顺序错误**
- ❌ $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v}$ 或 $\frac{uv' - u'v}{v^2}$
- ✅ $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$

**陷阱四：三角函数符号错误**
- ❌ $(\cos x)' = \sin x$
- ✅ $(\cos x)' = -\sin x$

### 🎯 题型分类与对策

| 题型 | 特点 | 推荐方法 |
|-----|------|---------|
| 显函数求导 | $y = f(x)$ 形式 | 直接应用公式和法则 |
| 复合函数求导 | 函数嵌套 | 链式法则，逐层求导 |
| 隐函数求导 | $F(x,y) = 0$ | 两边求导法 |
| 参数方程求导 | $\begin{cases}x=x(t)\\y=y(t)\end{cases}$ | 公式 $\frac{y'(t)}{x'(t)}$ |
| 对数求导 | 幂指函数或多因子乘除 | 取对数后求导 |
| 高阶导数 | 求 $y^{(n)}$ | 找规律或莱布尼茨公式 |
| 反函数求导 | 已知 $y=f(x)$ 求 $(f^{-1})'(y)$ | 公式 $\frac{1}{f'(x)}$ |

## 5. 易错点

⚠️ **常见错误**

1. **数值不稳定**
   - 步长 h 太小导致舍入误差
   - 步长 h 太大导致截断误差
   - 使用中心差分提高精度

2. **导数不存在**
   - 函数在某些点不可导（如 |x| 在 x=0）
   - 需要检查函数的光滑性

3. **梯度消失/爆炸**
   - 深度网络中的导数问题
   - 使用合适的激活函数和初始化

✅ **最佳实践**

1. **使用自动微分**
   - PyTorch、TensorFlow 等框架
   - 避免手动计算导数

2. **验证导数**
   - 使用数值导数验证解析导数
   - 确保实现正确

3. **理解链式法则**
   - 反向传播的核心
   - 复杂函数的求导

## 6. 相关概念

- [[02_Limits]] - 极限
- [[03_Continuity]] - 连续性（可导必连续）
- [[09_Indefinite_Integrals]] - 不定积分（导数的逆运算）
- [[10_Definite_Integrals]] - 定积分（微积分基本定理）
- [[../../03_Machine_Learning]] - 机器学习

## 自测（3问速测）

1. 我能从导数定义式出发，解释“为什么可导必连续”吗？
2. 面对 $u(x)^{v(x)}$ 这类幂指函数，我是否会优先考虑对数求导？
3. 我能在 10 秒内判断该用链式/乘积/商法则还是隐函数求导吗？

## 10. 总结

### 10.1 重要定义
1. 导数：f'(x)=lim(h→0)[f(x+h)-f(x)]/h
2. 偏导数：多元函数对某个变量的导数
3. 全微分：函数的线性近似
4. 方向导数：沿某个方向的导数
5. 梯度：偏导数组成的向量

### 10.2 重要定理
1. 可导必连续：函数在某点可导则必在该点连续
2. 链式法则：复合函数的导数等于导数的乘积
3. 乘积法则：(uv)'=u'v+uv'
4. 商法则：(u/v)'=(u'v-uv')/v²
5. Clairaut定理：混合偏导数连续则相等

### 10.3 重要证明
1. 可导必连续的证明：利用导数定义和极限性质
2. 链式法则的证明：利用复合函数的极限和导数定义
3. Clairaut定理的证明：利用混合偏导数的连续性

### 10.4 重要性质
1. 导数的几何意义：切线斜率
2. 高阶导数的定义：导数的导数
3. 隐函数求导法则：对隐式方程两边求导
4. 多元函数的极值条件：梯度为零

本章为后续学习相关章节奠定了基础。

## 11. 练习（分层）

本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第一章 函数与极限
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第一章 实数集
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 计算：f(x)=x³的导数（参考《高等数学 上册 第八版》第2章习题2-1第1题）
2. 计算：f(x)=eˣ的导数（参考《高等数学 上册 第八版》第2章习题2-1第3题）
3. 计算：f(x)=ln(x)的导数（参考《高等数学 上册 第八版》第2章习题2-1第4题）
4. 计算：f(x)=sin(x)的导数（参考《高等数学 上册 第八版》第2章习题2-1第5题）
5. 计算：f(x)=cos(x)的导数（参考《高等数学 上册 第八版》第2章习题2-1第6题）

### B档（进阶）
1. 计算：f(x)=x³·eˣ的导数（参考《高等数学 上册 第八版》第2章习题2-2第3题）
2. 计算：f(x)=x·ln(x)的导数（参考《高等数学 上册 第八版》第2章习题2-2第4题）
3. 证明：可导必连续（参考《数学分析(第5版) 上》第4章定理4.1）
4. 证明：链式法则（参考《数学分析(第5版) 上》第4章定理4.3）
5. 证明：乘积法则（参考《数学分析(第5版) 上》第4章定理4.4）

### C档（挑战）
1. 计算：f(x)=sin(x²)的导数（参考《高等数学 上册 第八版》第2章习题2-2第5题）
2. 计算：f(x)=ln(1+x)的导数（参考《高等数学 上册 第八版》第2章习题2-2第6题）
3. 应用：导数在神经网络反向传播中的应用（参考《高等数学 下册 第八版》第1章第10节）
4. 应用：导数在梯度下降算法中的应用（参考《高等数学 下册》第9章多元函数微分法应用）
5. 应用：导数在优化算法收敛性分析中的应用（参考《高等数学 下册》第14章重积分）




