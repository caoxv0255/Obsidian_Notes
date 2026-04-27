---
type: concept
topic: applications
category: calculus
difficulty: intermediate
prerequisites:
    - [[02_Limits]]
    - [[05_Derivatives]]
    - [[10_Definite_Integrals]]
    - [[19_Partial_Derivatives]]
    - [[24_Vector_Calculus]]
    - [[../00_Symbols_Conventions|符号与约定总表]]
acm_relevant: true
created: 2026-02-20
status: complete
subject: calculus
chapter: 25
updated: 2026-04-27
---

# 微积分应用 (Applications)

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习目标
- 理解微积分在优化、物理、经济、概率和机器学习中的典型用途
- 掌握导数和积分在建模、求极值和累积量计算中的作用
- 会把文字题转成函数、约束和积分表达式

## 先修
- [[02_Limits]] - 极限
- [[05_Derivatives]] - 导数
- [[10_Definite_Integrals]] - 定积分
- [[19_Partial_Derivatives]] - 偏导数与全微分
- [[24_Vector_Calculus]] - 向量微积分
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层
- A档（基础）：一元极值、边际分析与基本积分模型
- B档（进阶）：拉格朗日乘数法、概率期望方差与梯度下降
- C档（挑战）：多目标建模、正则化与跨学科综合题

## 自测（3问速测）
1. 优化题通常先找什么，再判断什么？
2. 为什么概率统计中的期望和方差可以写成积分？
3. 梯度下降和正则化分别在机器学习中扮演什么角色？

## 1. 定义

**直观理解**：
微积分在科学、工程、经济学、机器学习等领域有广泛的应用，包括优化、物理建模、概率统计、信号处理等。

微积分就像一个强大的工具箱，可以帮助你解决各种实际问题：
- **优化**：找到函数的最大值或最小值
- **物理**：描述运动、力、能量等
- **经济**：分析边际成本、收益等
- **机器学习**：训练神经网络、优化模型参数

## 2. 定理与性质

### 1. 优化问题

#### 极值理论

**定理**（费马定理）：如果 $f$ 在 $x_0$ 处可导且在 $x_0$ 处取得极值，则 $f'(x_0) = 0$。

**证明**：
假设 $f$ 在 $x_0$ 处取得极大值。

对于 $h > 0$ 且充分小：
$$\frac{f(x_0 + h) - f(x_0)}{h} \leq 0$$

取极限 $h \to 0^+$：
$$f'(x_0) \leq 0$$

对于 $h < 0$ 且 $|h|$ 充分小：
$$\frac{f(x_0 + h) - f(x_0)}{h} \geq 0$$

取极限 $h \to 0^-$：
$$f'(x_0) \geq 0$$

因此 $f'(x_0) = 0$。

**极值判定定理**：
1. **一阶导数判别法**：
   - 如果 $f'(x)$ 在 $x_0$ 处由正变负，则 $x_0$ 是极大值点
   - 如果 $f'(x)$ 在 $x_0$ 处由负变正，则 $x_0$ 是极小值点

2. **二阶导数判别法**：
   - 如果 $f''(x_0) > 0$，则 $x_0$ 是极小值点
   - 如果 $f''(x_0) < 0$，则 $x_0$ 是极大值点
   - 如果 $f''(x_0) = 0$，判别法失效

#### 最优化算法

**梯度下降法**：
$$x_{k+1} = x_k - \eta \nabla f(x_k)$$

其中 $\eta$ 是学习率，$\nabla f(x_k)$ 是梯度。

**牛顿法**：
$$x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$$

牛顿法利用二阶导数信息，收敛速度更快。

### 2. 物理应用

#### 运动学

- **速度**：$v(t) = \frac{ds}{dt}$，其中 $s(t)$ 是位移
- **加速度**：$a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2}$
- **位移**：$s(t) = \int v(t) dt$

#### 功和能

- **功**：$W = \int_{a}^{b} F(x) dx$
- **动能**：$K = \frac{1}{2}mv^2$
- **势能**：$U = \int F(x) dx$

### 3. 经济学应用

#### 边际分析

- **边际成本**：$MC = \frac{dC}{dq}$，其中 $C(q)$ 是成本函数
- **边际收益**：$MR = \frac{dR}{dq}$，其中 $R(q)$ 是收益函数
- **边际利润**：$MP = MR - MC$

#### 弹性

- **需求弹性**：$\varepsilon = \frac{dq}{dp} \cdot \frac{p}{q}$

### 4. 概率统计应用

#### 期望

对于连续随机变量 $X$：
$$\mathbb{E}[X] = \int_{-\infty}^{\infty} x f_X(x) dx$$

其中 $f_X(x)$ 是概率密度函数。

#### 方差

$$\text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = \int_{-\infty}^{\infty} (x - \mu)^2 f_X(x) dx$$

### 5. 机器学习应用

#### 损失函数优化

**均方误差（MSE）**：
$$L = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

梯度：
$$\frac{\partial L}{\partial w} = -\frac{2}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i) x_i$$

**交叉熵损失**：
$$L = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log \hat{y}_i + (1 - y_i) \log(1 - \hat{y}_i)]$$

#### 正则化

**L2正则化**：
$$L_{\text{reg}} = L + \lambda \sum_{j=1}^{m} w_j^2$$

导数：
$$\frac{\partial L_{\text{reg}}}{\partial w_j} = \frac{\partial L}{\partial w_j} + 2\lambda w_j$$

**L1正则化**：
$$L_{\text{reg}} = L + \lambda \sum_{j=1}^{m} |w_j|$$

导数（次梯度）：
$$\frac{\partial L_{\text{reg}}}{\partial w_j} = \frac{\partial L}{\partial w_j} + \lambda \cdot \text{sign}(w_j)$$

## 3. 证明

### 证明1：拉格朗日乘数法

**定理**：设 $f$ 和 $g$ 在 $\mathbb{R}^n$ 上可微，要在约束 $g(x) = c$ 下优化 $f(x)$，如果 $x^*$ 是极值点且 $\nabla g(x^*) \neq 0$，则存在 $\lambda$ 使得：
$$\nabla f(x^*) = \lambda \nabla g(x^*)$$

**证明**：
设 $x^*$ 是约束极值点，考虑约束曲线 $g(x) = c$。

在 $x^*$ 附近，约束曲线可以参数化为 $x = \gamma(t)$，其中 $\gamma(0) = x^*$。

由于 $x^*$ 是极值点，$\frac{d}{dt} f(\gamma(t))|_{t=0} = 0$。

由链式法则：
$$\nabla f(x^*) \cdot \gamma'(0) = 0$$

即 $\nabla f(x^*)$ 与约束曲线的切向量 $\gamma'(0)$ 正交。

由于 $\nabla g(x^*)$ 也与约束曲线的切向量正交（因为 $g(\gamma(t)) = c$ 对所有 $t$ 成立），故 $\nabla f(x^*)$ 与 $\nabla g(x^*)$ 平行。

因此存在 $\lambda$ 使得 $\nabla f(x^*) = \lambda \nabla g(x^*)$。

### 证明2：凸函数的极值唯一性

**定理**：设 $f$ 是严格凸函数，则 $f$ 至多有一个全局最小值。

**证明**：
反证法。假设 $x_1$ 和 $x_2$ 都是全局最小值，且 $x_1 \neq x_2$。

由于 $f$ 是严格凸的，对于任意 $\lambda \in (0, 1)$：
$$f(\lambda x_1 + (1-\lambda)x_2) < \lambda f(x_1) + (1-\lambda)f(x_2) = \lambda \min f + (1-\lambda)\min f = \min f$$

这与 $\min f$ 是最小值矛盾。因此 $x_1 = x_2$。

## 4. 代码示例

```python
import numpy as np
from scipy.optimize import minimize, fsolve
import matplotlib.pyplot as plt

# ==================== 优化问题 ====================

# 梯度下降优化
def gradient_descent(f, df, x0, learning_rate=0.01, max_iter=1000, tol=1e-6):
    """梯度下降算法"""
    x = x0
    for i in range(max_iter):
        gradient = df(x)
        x_new = x - learning_rate * gradient
        
        # 收敛判断
        if abs(x_new - x) < tol:
            break
            
        x = x_new
    
    return x, f(x), i + 1

# 示例1：最小化 f(x) = x²
f1 = lambda x: x**2
df1 = lambda x: 2*x

x_opt, f_opt, iterations = gradient_descent(f1, df1, 10)
print(f"示例1: f(x) = x²")
print(f"梯度下降结果: x = {x_opt:.6f}, f(x) = {f_opt:.6f}")
print(f"迭代次数: {iterations}")

# 示例2：最小化 f(x) = x⁴ - 2x² + x
f2 = lambda x: x**4 - 2*x**2 + x
df2 = lambda x: 4*x**3 - 4*x + 1

x_opt, f_opt, iterations = gradient_descent(f2, df2, 2)
print(f"\n示例2: f(x) = x⁴ - 2x² + x")
print(f"梯度下降结果: x = {x_opt:.6f}, f(x) = {f_opt:.6f}")
print(f"迭代次数: {iterations}")

# ==================== 神经网络中的反向传播 ====================

def sigmoid(x):
    """Sigmoid激活函数"""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Sigmoid导数"""
    s = sigmoid(x)
    return s * (1 - s)

def simple_neural_network(x, w1, w2, b1, b2):
    """简单的神经网络"""
    # 第一层
    z1 = w1 * x + b1
    a1 = sigmoid(z1)
    
    # 第二层
    z2 = w2 * a1 + b2
    a2 = sigmoid(z2)
    
    return a2, z1, a1, z2

def mse_loss(y_true, y_pred):
    """均方误差损失"""
    return np.mean((y_true - y_pred)**2)

def backpropagation(x, y, w1, w2, b1, b2, learning_rate):
    """反向传播算法"""
    # 前向传播
    y_pred, z1, a1, z2 = simple_neural_network(x, w1, w2, b1, b2)
    
    # 计算损失
    loss = mse_loss(y, y_pred)
    
    # 反向传播
    # 输出层梯度
    dL_da2 = -2 * (y - y_pred)
    da2_dz2 = sigmoid_derivative(z2)
    dL_dz2 = dL_da2 * da2_dz2
    
    # 隐藏层梯度
    dL_da1 = dL_dz2 * w2
    da1_dz1 = sigmoid_derivative(z1)
    dL_dz1 = dL_da1 * da1_dz1
    
    # 参数梯度
    dL_dw2 = dL_dz2 * a1
    dL_db2 = dL_dz2
    dL_dw1 = dL_dz1 * x
    dL_db1 = dL_dz1
    
    # 更新参数
    w1 -= learning_rate * dL_dw1
    w2 -= learning_rate * dL_dw2
    b1 -= learning_rate * dL_db1
    b2 -= learning_rate * dL_db2
    
    return w1, w2, b1, b2, loss

# 训练神经网络
np.random.seed(42)
w1, w2 = np.random.randn(), np.random.randn()
b1, b2 = np.random.randn(), np.random.randn()

# 简单的训练数据
x_train = np.array([0, 1, 2, 3])
y_train = np.array([0, 1, 0, 1])

learning_rate = 0.1
epochs = 1000

print(f"\n神经网络训练：")
for epoch in range(epochs):
    total_loss = 0
    for i in range(len(x_train)):
        w1, w2, b1, b2, loss = backpropagation(
            x_train[i], y_train[i], w1, w2, b1, b2, learning_rate
        )
        total_loss += loss
    
    if (epoch + 1) % 100 == 0:
        avg_loss = total_loss / len(x_train)
        print(f"Epoch {epoch + 1}, Loss: {avg_loss:.6f}")

# 测试
x_test = np.array([0.5, 1.5, 2.5])
predictions = [simple_neural_network(x, w1, w2, b1, b2)[0] for x in x_test]
print(f"\n测试结果：")
for x, pred in zip(x_test, predictions):
    print(f"x = {x:.1f}, 预测值 = {pred:.6f}")

# ==================== 经济学应用：边际分析 ====================

def cost_function(q):
    """成本函数: C(q) = 100 + 10q + q²"""
    return 100 + 10*q + q**2

def marginal_cost(q):
    """边际成本: MC = dC/dq"""
    return 10 + 2*q

def revenue_function(q, p):
    """收益函数: R(q) = p·q"""
    return p * q

def marginal_revenue(q, p):
    """边际收益: MR = dR/dq = p"""
    return p

def profit_function(q, p):
    """利润函数: π(q) = R(q) - C(q)"""
    return revenue_function(q, p) - cost_function(q)

# 找到最优产量（利润最大化）
p = 50  # 价格

# 利润最大化的条件：MR = MC
# p = 10 + 2q → q* = (p - 10)/2
optimal_q = (p - 10) / 2

print(f"\n经济学应用：")
print(f"价格 p = {p}")
print(f"最优产量 q* = {optimal_q}")
print(f"边际收益 MR = {marginal_revenue(optimal_q, p)}")
print(f"边际成本 MC = {marginal_cost(optimal_q)}")
print(f"最大利润 π = {profit_function(optimal_q, p):.2f}")

# ==================== 概率应用：期望和方差 ====================

def normal_pdf(x, mu=0, sigma=1):
    """正态分布概率密度函数"""
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

def calculate_expectation(pdf_func, a=-np.inf, b=np.inf, mu=0, sigma=1):
    """计算期望 E[X]"""
    from scipy.integrate import quad
    
    def integrand(x):
        return x * pdf_func(x, mu, sigma)
    
    result, _ = quad(integrand, a, b)
    return result

def calculate_variance(pdf_func, mu_x, a=-np.inf, b=np.inf, mu=0, sigma=1):
    """计算方差 Var(X) = E[(X-μ)²]"""
    from scipy.integrate import quad
    
    def integrand(x):
        return (x - mu_x)**2 * pdf_func(x, mu, sigma)
    
    result, _ = quad(integrand, a, b)
    return result

print(f"\n概率统计应用（正态分布 N(0,1)）：")
mu_exp = calculate_expectation(normal_pdf, -10, 10, 0, 1)
var_exp = calculate_variance(normal_pdf, mu_exp, -10, 10, 0, 1)
print(f"期望 E[X] = {mu_exp:.6f} (理论值: 0)")
print(f"方差 Var(X) = {var_exp:.6f} (理论值: 1)")

# ==================== 正则化效果演示 ====================

def loss_with_regularization(y_true, y_pred, weights, lambda_reg=0.01):
    """带正则化的损失函数"""
    mse = np.mean((y_true - y_pred)**2)
    l2_reg = lambda_reg * np.sum(weights**2)
    return mse + l2_reg

def gradient_with_regularization(y_true, y_pred, x, weights, lambda_reg=0.01):
    """带正则化的梯度"""
    n = len(y_true)
    mse_grad = (2/n) * np.sum((y_pred - y_true) * x)
    reg_grad = 2 * lambda_reg * weights
    return mse_grad + reg_grad

# 对比有无正则化
weights_without_reg = []
weights_with_reg = []

for epoch in range(100):
    # 无正则化
    grad = gradient_with_regularization(y_train, np.dot(x_train, weights_without_reg[-1]) if weights_without_reg else np.zeros_like(x_train), x_train, weights_without_reg[-1] if weights_without_reg else 0, lambda_reg=0)
    
    if not weights_without_reg:
        weights_without_reg.append(grad * 0.01)
    else:
        weights_without_reg.append(weights_without_reg[-1] - grad * 0.01)
    
    # 有正则化
    grad = gradient_with_regularization(y_train, np.dot(x_train, weights_with_reg[-1]) if weights_with_reg else np.zeros_like(x_train), x_train, weights_with_reg[-1] if weights_with_reg else 0, lambda_reg=0.01)
    
    if not weights_with_reg:
        weights_with_reg.append(grad * 0.01)
    else:
        weights_with_reg.append(weights_with_reg[-1] - grad * 0.01)

print(f"\n正则化效果：")
print(f"无正则化，最终权重: {weights_without_reg[-1]:.6f}")
print(f"有正则化，最终权重: {weights_with_reg[-1]:.6f}")
print(f"正则化使权重更接近0，防止过拟合")
```

## 总结
- 微积分应用的核心是建模，而不是机械套公式。
- 导数负责变化率和极值，积分负责累积量和总量。
- 不同领域的问题，常常共享同一套数学结构。

## 易错点
- 没先定义变量和约束就直接求导
- 只算局部极值，不检查实际问题的边界条件
- 经济学里的边际量和总量混淆
- 概率题里忘记密度函数的归一化条件

## 根据题型整理的做题方法
### 微积分应用的核心思想

**优化问题**：
- 一元函数：求导找极值
- 多元函数：梯度=0，Hessian矩阵判断

**建模问题**：
1. 理解问题，确定变量
2. 建立函数关系
3. 求极值
4. 验证结果

**物理应用**：
- 速度、加速度：导数
- 路程、功：积分
- 质心、转动惯量：积分

**经济学应用**：
- 边际成本/收益：导数
- 总成本/收益：积分
- 利润最大化：求极值

### 机器学习中的数学

| 概念 | 数学基础 |
|-----|---------|
| 梯度下降 | 导数、偏导数 |
| 损失函数 | 函数极值 |
| 正则化 | 范数、不等式 |
| 反向传播 | 链式法则 |
| 概率模型 | 积分、期望 |

## 习题

### 基础题

1. 找到函数 $f(x) = x^3 - 3x^2 + 2$ 的极值点并判断极值类型。

2. 使用梯度下降法最小化 $f(x, y) = x^2 + y^2$。

3. 计算成本函数 $C(q) = 50 + 2q + 0.1q^2$ 的边际成本。

### 进阶题

4. 证明：如果 $f$ 是凸函数，则其任意局部最小值都是全局最小值。

5. 在机器学习中，为什么需要正则化？L1正则化和L2正则化有什么区别？

6. 给定正态分布 $N(\mu, \sigma^2)$，计算其期望和方差。

### 挑战题

7. 证明拉格朗日乘数法，并给出一个实际应用例子。

8. 在深度学习中，如何选择学习率？过大或过小会有什么问题？

## 相关链接

- [[05_Derivatives]] - 导数（优化的基础）
- [[06_Mean_Value_Theorem]] - 中值定理（极值理论的基础）
- [[19_Partial_Derivatives]] - 偏导数（多元优化）
- [[24_Vector_Calculus]] - 向量微积分（多元优化与梯度）
- [[06_Case_Finance]] - 金融案例（边际分析的应用）
- [[04_Training_Loop]] - 训练循环（梯度下降的实现）

## 参考资料

- 数学分析原理 - Walter Rudin
- 数学分析（第5版）- 华东师范大学数学系
- 高等数学（第八版）- 同济大学数学科学学院
- 深度学习 - Ian Goodfellow



