---
type: note
subject: optimization
chapter: 18
created: 2026-04-03
status: complete
---

# 18 - 随机优化

## 1. 随机优化的动机

### 1.1 大规模优化问题

**问题**：传统优化方法每步需要计算完整梯度：
$$\nabla f(x) = \frac{1}{n}\sum_{i=1}^{n} \nabla f_i(x)$$

当 n 很大（如数百万样本）时，每步计算代价太高。

### 1.2 随机优化思想

**核心思想**：用小批量样本估计梯度，降低每步计算量。

**期望目标**：
$$\min_x f(x) = \mathbb{E}_{\xi}[F(x, \xi)]$$

其中 ξ 是随机变量（如数据样本）。

## 2. 随机梯度下降

### 2.1 算法

**随机梯度下降（SGD）**：
$$x_{k+1} = x_k - \alpha_k g_k$$

其中 g_k 是 ∇f(x_k) 的无偏估计：
$$\mathbb{E}[g_k] = \nabla f(x_k)$$

### 2.2 小批量梯度估计

**Mini-batch SGD**：
$$g_k = \frac{1}{m}\sum_{i \in B_k} \nabla f_i(x_k)$$

其中 B_k 是大小为 m 的随机小批量。

**方差**：
$$\text{Var}(g_k) = \frac{1}{m}\text{Var}(\nabla f_i(x_k))$$

### 2.3 收敛性分析

**假设**：
1. f 凸，L-光滑
2. 𝔼[‖g_k‖²] ≤ σ² + M‖∇f(x_k)‖²

**定理（凸情况）**：取 α_k = O(1/√k)，则：
$$\mathbb{E}[f(\bar{x}_K) - f(x^*)] = O\left(\frac{1}{\sqrt{K}}\right)$$

**定理（强凸情况）**：取 α_k = O(1/k)，则：
$$\mathbb{E}[\|x_k - x^*\|^2] = O\left(\frac{1}{k}\right)$$

### 2.4 与GD的对比

| 方法 | 每步复杂度 | 收敛速度 | 总复杂度（强凸） |
|------|------------|----------|------------------|
| GD | O(n) | O((1-μ/L)^k) | O(n log(1/ε)) |
| SGD | O(m) | O(1/k) | O(n/ε) |

当 n 大、精度要求不高时，SGD更高效。

## 3. 方差缩减方法

### 3.1 动机

SGD的方差限制了收敛速度。方差缩减方法通过控制估计方差加速收敛。

### 3.2 SVRG（Stochastic Variance Reduced Gradient）

**算法**：
```
初始化 x̃ = x₀
for s = 1, 2, ...:
    计算 x̃ 处的完整梯度 ∇f(x̃)
    x_0 = x̃
    for k = 0, 1, ..., m-1:
        随机选取 i_k
        v_k = ∇f_{i_k}(x_k) - ∇f_{i_k}(x̃) + ∇f(x̃)
        x_{k+1} = x_k - η v_k
    x̃ = x_m（或随机选取）
```

**收敛性**：线性收敛（强凸情况），无需减小步长。

### 3.3 SAGA

**算法**：
```
存储每个样本的梯度历史 g_i^old
for k = 0, 1, 2, ...:
    随机选取 i_k
    v_k = ∇f_{i_k}(x_k) - g_{i_k}^{old} + (1/n)∑g_j^{old}
    更新 g_{i_k}^{old} = ∇f_{i_k}(x_k)
    x_{k+1} = x_k - η v_k
```

**特点**：无需完整梯度计算，内存开销O(n)。

### 3.4 SARAH

**算法**：
```
for s = 1, 2, ...:
    x_0 = x̃
    v_0 = ∇f(x_0)
    for k = 0, 1, ..., m-1:
        随机选取 i_k
        v_{k+1} = v_k + ∇f_{i_k}(x_k) - ∇f_{i_k}(x_{k+1})
        x_{k+1} = x_k - η v_{k+1}
    x̃ = x_m
```

**特点**：递归更新，方差自动减小。

## 4. 动量方法

### 4.1 动量SGD

**算法**：
$$v_{k+1} = \beta v_k + (1-\beta)g_k$$
$$x_{k+1} = x_k - \alpha v_{k+1}$$

**参数**：β ∈ [0,1)，通常取 0.9。

**作用**：
- 加速收敛
- 抑制震荡
- 帮助跳出局部极小

### 4.2 Nesterov加速梯度

**算法**：
$$v_{k+1} = \beta v_k + \alpha \nabla f(x_k - \beta v_k)$$
$$x_{k+1} = x_k - v_{k+1}$$

**特点**：在动量基础上加入"前瞻"性质。

## 5. 自适应学习率方法

### 5.1 AdaGrad

**算法**：
$$G_k = G_{k-1} + g_k^2$$
$$x_{k+1} = x_k - \frac{\alpha}{\sqrt{G_k + \epsilon}} \odot g_k$$

**特点**：自适应调整每个参数的学习率。

**问题**：G_k 单调递增，学习率持续减小。

### 5.2 RMSprop

**算法**：
$$G_k = \beta G_{k-1} + (1-\beta)g_k^2$$
$$x_{k+1} = x_k - \frac{\alpha}{\sqrt{G_k + \epsilon}} \odot g_k$$

**改进**：使用指数移动平均，学习率不会单调减小。

### 5.3 Adam

**算法**：
$$m_k = \beta_1 m_{k-1} + (1-\beta_1) g_k$$
$$v_k = \beta_2 v_{k-1} + (1-\beta_2) g_k^2$$
$$\hat{m}_k = \frac{m_k}{1-\beta_1^k}, \quad \hat{v}_k = \frac{v_k}{1-\beta_2^k}$$
$$x_{k+1} = x_k - \frac{\alpha \hat{m}_k}{\sqrt{\hat{v}_k} + \epsilon}$$

**默认参数**：β₁ = 0.9, β₂ = 0.999, ε = 10⁻⁸。

**特点**：结合动量和自适应学习率。

### 5.4 方法对比

| 方法 | 动量 | 自适应学习率 | 适用场景 |
|------|------|--------------|----------|
| SGD | 无 | 无 | 简单问题，精细调参 |
| Momentum | 有 | 无 | 需要加速收敛 |
| AdaGrad | 无 | 有 | 稀疏特征 |
| RMSprop | 无 | 有 | 非平稳目标 |
| Adam | 有 | 有 | 通用，默认选择 |

## 6. 学习率调度

### 6.1 衰减策略

**步衰减**：
$$\alpha_k = \alpha_0 \cdot \gamma^{\lfloor k/s \rfloor}$$

**指数衰减**：
$$\alpha_k = \alpha_0 \cdot \gamma^k$$

**余弦退火**：
$$\alpha_k = \alpha_{min} + \frac{1}{2}(\alpha_0 - \alpha_{min})(1 + \cos(\pi k/T))$$

### 6.2 周期性策略

**SGDR（带重启的SGD）**：
周期性重置学习率，帮助跳出局部极小。

**Warm Restart**：每个周期从较大的学习率重新开始。

### 6.3 学习率预热

**Warmup**：训练初期使用较小学习率，逐渐增大到目标值。

**原因**：
- 初期参数随机，梯度不稳定
- 避免早期梯度过大导致参数偏移

## 7. 收敛性理论

### 7.1 凸情况

**假设**：f 凸，L-光滑，𝔼[‖g‖²] ≤ G²。

**定理**：取 α_k = α/√k，则：
$$\mathbb{E}[f(\bar{x}_K) - f^*] \leq \frac{\|x_0 - x^*\|^2}{2\alpha\sqrt{K}} + \frac{\alpha G^2}{\sqrt{K}}$$

### 7.2 强凸情况

**假设**：f μ-强凸，L-光滑。

**定理**：取 α_k = 1/(μk)，则：
$$\mathbb{E}[\|x_k - x^*\|^2] \leq \frac{C}{k}$$

### 7.3 非凸情况

**定理**：设 f 下有界，L-光滑，则：
$$\min_{k=0,\ldots,K-1} \mathbb{E}[\|\nabla f(x_k)\|^2] \leq O\left(\frac{1}{\sqrt{K}}\right)$$

## 8. Python实现

```python
import numpy as np

class Optimizers:
    """随机优化器集合"""
    
    @staticmethod
    def sgd(grad, x, lr=0.01):
        """标准SGD"""
        return x - lr * grad
    
    @staticmethod
    def momentum(grad, x, v, lr=0.01, beta=0.9):
        """带动量的SGD"""
        v = beta * v + grad
        x = x - lr * v
        return x, v
    
    @staticmethod
    def adam(grad, x, m, v, t, lr=0.001, beta1=0.9, beta2=0.999, eps=1e-8):
        """Adam优化器"""
        m = beta1 * m + (1 - beta1) * grad
        v = beta2 * v + (1 - beta2) * grad**2
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        x = x - lr * m_hat / (np.sqrt(v_hat) + eps)
        return x, m, v

def train_sgd(X, y, model, optimizer='adam', epochs=100, batch_size=32, lr=0.01):
    """
    使用随机优化方法训练模型
    """
    n_samples = X.shape[0]
    n_batches = n_samples // batch_size
    
    # 初始化优化器状态
    params = model.get_params()
    m = np.zeros_like(params)
    v = np.zeros_like(params)
    velocity = np.zeros_like(params)
    
    for epoch in range(epochs):
        # 打乱数据
        indices = np.random.permutation(n_samples)
        X_shuffled = X[indices]
        y_shuffled = y[indices]
        
        for i in range(n_batches):
            # 获取小批量
            start = i * batch_size
            end = start + batch_size
            X_batch = X_shuffled[start:end]
            y_batch = y_shuffled[start:end]
            
            # 计算梯度
            grad = model.gradient(X_batch, y_batch)
            
            # 更新参数
            t = epoch * n_batches + i + 1
            if optimizer == 'sgd':
                params = Optimizers.sgd(grad, params, lr)
            elif optimizer == 'momentum':
                params, velocity = Optimizers.momentum(grad, params, velocity, lr)
            elif optimizer == 'adam':
                params, m, v = Optimizers.adam(grad, params, m, v, t, lr)
            
            model.set_params(params)
        
        # 打印损失
        if (epoch + 1) % 10 == 0:
            loss = model.loss(X, y)
            print(f"Epoch {epoch+1}, Loss: {loss:.4f}")
    
    return model

# 示例：逻辑回归
class LogisticRegression:
    def __init__(self, n_features):
        self.w = np.zeros(n_features)
        self.b = 0
    
    def get_params(self):
        return np.concatenate([self.w, [self.b]])
    
    def set_params(self, params):
        self.w = params[:-1]
        self.b = params[-1]
    
    def predict(self, X):
        return 1 / (1 + np.exp(-(X @ self.w + self.b)))
    
    def loss(self, X, y):
        p = self.predict(X)
        return -np.mean(y * np.log(p + 1e-10) + (1-y) * np.log(1-p + 1e-10))
    
    def gradient(self, X, y):
        m = X.shape[0]
        p = self.predict(X)
        dw = X.T @ (p - y) / m
        db = np.mean(p - y)
        return np.concatenate([dw, [db]])
```

## 9. 总结

**随机优化的优势**：
- 每步计算量小
- 适合大规模问题
- 可处理数据流

**方法选择指南**：

| 场景 | 推荐方法 |
|------|----------|
| 简单凸问题 | SGD + 衰减 |
| 深度学习 | Adam |
| 精细调参 | SGD + Momentum |
| 稀疏数据 | AdaGrad/FTRL |
| 快速原型 | Adam |

**未来方向**：
- 自适应批量大小
- 二阶随机方法
- 分布式随机优化

---

**相关链接**：
- [[06_Gradient_Methods]] - 梯度下降法
- [[07_Newton_Method]] - 牛顿法
- [[19_Distributed_Optimization]] - 分布式优化
