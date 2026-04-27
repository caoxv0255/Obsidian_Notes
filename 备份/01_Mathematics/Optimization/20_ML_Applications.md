---
type: note
subject: optimization
chapter: 20
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 20 - 机器学习应用

## 📌 学习目标

- 明确本章核心概念与关键结论
- 能将本章方法用于标准题型

## ✅ 先修

- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层

- **基础**：定义与直接计算
- **进阶**：性质证明与综合应用
- **拓展**：跨章节联系与建模

## 自测（3问速测）

1. 本章最核心的定义是什么？
2. 本章一个关键结论的适用条件是什么？
3. 如何把本章方法应用到一个具体问题？

## 1. 机器学习中的优化问题

### 1.1 经验风险最小化

**一般形式**：
$$\min_\theta \frac{1}{n}\sum_{i=1}^{n} \ell(y_i, f_\theta(x_i)) + \lambda R(\theta)$$

其中：
- ℓ 是损失函数
- f_θ 是模型
- R 是正则项
- λ 是正则化系数

### 1.2 常见优化问题

| 问题 | 损失函数 | 正则项 | 优化类型 |
|------|----------|--------|----------|
| 线性回归 | 均方误差 | L2 | 凸 |
| 逻辑回归 | 交叉熵 | L2 | 凸 |
| SVM | Hinge | L2 | 凸 |
| LASSO | 均方误差 | L1 | 凸（非光滑） |
| 神经网络 | 交叉熵 | L2 | 非凸 |

## 2. 线性模型

### 2.1 线性回归

**问题**：
$$\min_w \frac{1}{2n}\|Xw - y\|^2 + \frac{\lambda}{2}\|w\|^2$$

**闭式解**：
$$w^* = (X^TX + \lambda I)^{-1}X^Ty$$

**梯度**：
$$\nabla_w = \frac{1}{n}X^T(Xw - y) + \lambda w$$

### 2.2 逻辑回归

**问题**：
$$\min_w \frac{1}{n}\sum_{i=1}^{n} \log(1 + \exp(-y_i w^T x_i)) + \frac{\lambda}{2}\|w\|^2$$

**梯度**：
$$\nabla_w = \frac{1}{n}\sum_{i=1}^{n} \frac{-y_i x_i}{1 + \exp(y_i w^T x_i)} + \lambda w$$

### 2.3 支持向量机

**软间隔SVM**：
$$\min_{w,b,\xi} \frac{1}{2}\|w\|^2 + C\sum_{i=1}^{n}\xi_i$$
$$\text{s.t.} \quad y_i(w^T x_i + b) \geq 1 - \xi_i, \quad \xi_i \geq 0$$

**对偶形式**：
$$\max_\alpha \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j$$
$$\text{s.t.} \quad 0 \leq \alpha_i \leq C, \quad \sum_i \alpha_i y_i = 0$$

## 3. 正则化与优化

### 3.1 L1正则化（LASSO）

**问题**：
$$\min_w \frac{1}{2n}\|Xw - y\|^2 + \lambda\|w\|_1$$

**近端梯度法**：
$$w^{k+1} = \text{prox}_{\lambda\|\cdot\|_1}(w^k - \alpha \nabla f(w^k))$$

**软阈值算子**：
$$\text{prox}_{\lambda\|\cdot\|_1}(z) = \text{sign}(z) \odot \max(|z| - \lambda, 0)$$

### 3.2 弹性网络

**问题**：
$$\min_w \frac{1}{2n}\|Xw - y\|^2 + \lambda_1\|w\|_1 + \frac{\lambda_2}{2}\|w\|^2$$

**优点**：结合L1稀疏性和L2稳定性。

### 3.3 组LASSO

**问题**：
$$\min_w \frac{1}{2n}\|Xw - y\|^2 + \sum_g \lambda_g \|w_g\|_2$$

**特点**：变量按组选择。

## 4. 神经网络优化

### 4.1 反向传播

**链式法则**：
$$\frac{\partial L}{\partial W^{(l)}} = \frac{\partial L}{\partial a^{(L)}} \cdot \frac{\partial a^{(L)}}{\partial a^{(L-1)}} \cdots \frac{\partial a^{(l+1)}}{\partial W^{(l)}}$$

**计算图**：自动微分的基础。

### 4.2 常见问题

**梯度消失**：
- 原因：激活函数导数小于1
- 解决：ReLU、BatchNorm、残差连接

**梯度爆炸**：
- 原因：权重初始化不当
- 解决：梯度裁剪、合理初始化

**鞍点**：
- 高维优化中的常见问题
- 解决：动量、自适应方法

### 4.3 批归一化

**前向传播**：
$$\hat{x} = \frac{x - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$$
$$y = \gamma \hat{x} + \beta$$

**梯度计算**：需要考虑均值和方差的依赖。

## 5. 凸优化在ML中的应用

### 5.1 对偶理论的应用

**SVM**：对偶形式引入核方法
**对偶上升**：分布式优化基础
**KKT条件**：最优性验证

### 5.2 约束优化

**半正定规划**：
- 核学习
- 降维

**二阶锥规划**：
- 鲁棒优化
- 机会约束

## 6. 加速技术

### 6.1 动量法

**应用**：深度学习训练

**效果**：
- 加速收敛
- 抑制震荡
- 帮助跳出局部极小

### 6.2 自适应学习率

**Adam**：
- 默认选择
- 快速收敛
- 鲁棒性强

**学习率调度**：
- 余弦退火
- 周期性重启
- Warmup

### 6.3 批量大小调整

**小批量**：
- 更好的泛化
- 正则化效果

**大批量**：
- 更快的训练
- 需要调整学习率

## 7. 实践案例

### 7.1 逻辑回归完整实现

```python
import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, n_iters=1000, reg_lambda=0.01):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.reg_lambda = reg_lambda
        self.w = None
        self.b = None
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0
        
        for i in range(self.n_iters):
            # 前向传播
            linear = np.dot(X, self.w) + self.b
            predictions = self.sigmoid(linear)
            
            # 计算梯度
            dw = (1/n_samples) * np.dot(X.T, (predictions - y)) + self.reg_lambda * self.w
            db = (1/n_samples) * np.sum(predictions - y)
            
            # 更新参数
            self.w -= self.lr * dw
            self.b -= self.lr * db
            
            if (i + 1) % 100 == 0:
                loss = self.compute_loss(X, y)
                print(f"Iteration {i+1}, Loss: {loss:.4f}")
    
    def compute_loss(self, X, y):
        linear = np.dot(X, self.w) + self.b
        predictions = self.sigmoid(linear)
        loss = -np.mean(y * np.log(predictions + 1e-10) + (1-y) * np.log(1-predictions + 1e-10))
        loss += (self.reg_lambda/2) * np.sum(self.w**2)
        return loss
    
    def predict_proba(self, X):
        linear = np.dot(X, self.w) + self.b
        return self.sigmoid(linear)
    
    def predict(self, X):
        return (self.predict_proba(X) >= 0.5).astype(int)
```

### 7.2 LASSO回归（近端梯度法）

```python
class LassoRegression:
    def __init__(self, alpha=0.1, n_iters=1000, learning_rate=0.01):
        self.alpha = alpha
        self.n_iters = n_iters
        self.lr = learning_rate
        self.w = None
    
    def soft_threshold(self, z, threshold):
        return np.sign(z) * np.maximum(np.abs(z) - threshold, 0)
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        
        # 预计算 X^T X 和 X^T y
        XtX = X.T @ X / n_samples
        Xty = X.T @ y / n_samples
        
        # Lipschitz常数
        L = np.linalg.eigvalsh(XtX).max()
        step = 1 / L
        
        for i in range(self.n_iters):
            # 梯度步
            grad = XtX @ self.w - Xty
            z = self.w - step * grad
            
            # 近端算子（软阈值）
            self.w = self.soft_threshold(z, self.alpha * step)
            
            if (i + 1) % 100 == 0:
                loss = self.compute_loss(X, y)
                print(f"Iteration {i+1}, Loss: {loss:.4f}, Non-zero: {np.sum(self.w != 0)}")
    
    def compute_loss(self, X, y):
        predictions = X @ self.w
        mse = np.mean((predictions - y)**2)
        l1 = self.alpha * np.sum(np.abs(self.w))
        return mse + l1
    
    def predict(self, X):
        return X @ self.w
```

### 7.3 神经网络训练

```python
import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        self.softmax = nn.Softmax(dim=1)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return self.softmax(x)

def train_neural_network(X_train, y_train, X_val, y_val, config):
    # 初始化模型
    model = SimpleNN(config['input_dim'], config['hidden_dim'], config['output_dim'])
    
    # 损失函数和优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config['lr'])
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=config['epochs'])
    
    history = {'train_loss': [], 'val_acc': []}
    
    for epoch in range(config['epochs']):
        # 训练阶段
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        scheduler.step()
        
        # 验证阶段
        model.eval()
        with torch.no_grad():
            val_outputs = model(X_val)
            val_preds = torch.argmax(val_outputs, dim=1)
            val_acc = (val_preds == y_val).float().mean()
        
        history['train_loss'].append(loss.item())
        history['val_acc'].append(val_acc.item())
        
        if (epoch + 1) % 10 == 0:
            print(f"Epoch {epoch+1}/{config['epochs']}, Loss: {loss:.4f}, Val Acc: {val_acc:.4f}")
    
    return model, history
```

## 8. 优化技巧总结

### 8.1 初始化

- **Xavier初始化**：适用于sigmoid/tanh
- **He初始化**：适用于ReLU
- **预训练**：迁移学习

### 8.2 正则化

| 方法 | 作用 | 适用场景 |
|------|------|----------|
| L1 | 稀疏性 | 特征选择 |
| L2 | 权重衰减 | 防止过拟合 |
| Dropout | 随机失活 | 深度网络 |
| BatchNorm | 归一化 | 训练加速 |

### 8.3 调参策略

1. **学习率**：从0.01开始，网格搜索或学习率调度
2. **批量大小**：32-256，与学习率联动
3. **正则化系数**：交叉验证选择
4. **优化器**：Adam默认，SGD+Momentum精细调参

## 9. 总结

**机器学习优化的核心**：
- 问题建模：选择合适的损失和正则
- 算法选择：凸问题用凸优化，非凸用启发式方法
- 工程实现：数值稳定性、计算效率

**最佳实践**：
1. 从简单模型开始
2. 使用标准化/归一化
3. 监控训练和验证损失
4. 早停防止过拟合
5. 使用预训练模型

---

**相关链接**：
- [[06_Gradient_Methods]] - 梯度下降法
- [[18_Stochastic_Optimization]] - 随机优化
- [[01_Convex_Sets]] - 凸集
- [[09_KKT_Conditions]] - KKT条件

