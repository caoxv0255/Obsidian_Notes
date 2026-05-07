---
type: note
subject: optimization
chapter: 19
created: 2026-04-03
status: complete
updated: 2026-04-27
---

# 19 - 分布式优化

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

## 1. 分布式优化的动机

### 1.1 大规模数据挑战

**问题**：
- 数据量太大，单机内存不足
- 计算任务繁重，单机计算能力有限
- 数据分布在多个地理位置

**解决方案**：多台机器协同优化。

### 1.2 分布式计算模型

**参数服务器架构**：
- 工作节点：存储数据，计算梯度
- 参数服务器：存储和更新模型参数

**通信模式**：
- 同步：所有节点完成后更新
- 异步：节点独立更新

## 2. 分布式梯度下降

### 2.1 同步SGD

**算法**：
```
for k = 0, 1, 2, ...:
    服务器广播参数 x_k 到所有工作节点
    每个工作节点 i 并行计算梯度 g_i
    等待所有节点完成
    聚合梯度：g = (1/n)∑g_i
    更新：x_{k+1} = x_k - α g
```

**特点**：
- 收敛稳定
- 等待最慢节点（同步瓶颈）

### 2.2 异步SGD（Hogwild!）

**算法**：
```
每个工作节点独立运行：
    while 未收敛:
        从服务器读取当前参数 x
        计算本地梯度 g
        异步更新服务器：x = x - α g
```

**特点**：
- 无等待，高吞吐
- 梯度可能过期（使用旧参数计算）
- 需要处理写入冲突

### 2.3 收敛性

**同步SGD**：与单机SGD相同的收敛性。

**异步SGD**：受梯度延迟影响，收敛速度下降，但总时间可能更短。

## 3. ADMM分布式优化

### 3.1 问题的分解

**原问题**：
$$\min \sum_{i=1}^{n} f_i(x_i) + g(z)$$
$$\text{s.t.} \quad A_i x_i = z, \quad i = 1, \ldots, n$$

### 3.2 分布式ADMM

**迭代公式**：
$$x_i^{k+1} = \arg\min_{x_i} \left\{ f_i(x_i) + \frac{\rho}{2}\|A_i x_i - z^k + u_i^k\|^2 \right\}$$
$$z^{k+1} = \arg\min_z \left\{ g(z) + \frac{\rho}{2}\sum_i \|A_i x_i^{k+1} - z + u_i^k\|^2 \right\}$$
$$u_i^{k+1} = u_i^k + A_i x_i^{k+1} - z^{k+1}$$

### 3.3 并行实现

- x_i 更新：各节点并行
- z 更新：聚合后计算
- u_i 更新：各节点本地

## 4. 去中心化优化

### 4.1 动机

**问题**：参数服务器可能成为瓶颈。

**解决方案**：节点间直接通信，无需中心服务器。

### 4.2 一致性约束

**问题**：各节点维护本地参数 x_i，要求最终一致：
$$x_1 = x_2 = \cdots = x_n$$

**等价约束**：
$$x_i = x_j, \quad \forall (i,j) \in E$$

其中 E 是通信图的边集。

### 4.3 分布式梯度下降（DGD）

**算法**：
$$x_i^{k+1} = \sum_{j} w_{ij} x_j^k - \alpha_k \nabla f_i(x_i^k)$$

其中 W = (w_{ij}) 是混合矩阵，满足：
- 双随机：W1 = 1, Wᵀ1 = 1
- 与通信图兼容：w_{ij} = 0 若 (i,j) ∉ E

### 4.4 收敛条件

**条件**：
- W 与通信图的谱隙相关
- 步长 α_k → 0（或固定步长+正则化）

**收敛性**：
$$\lim_{k \to \infty} x_i^k = x^*, \quad \forall i$$

## 5. 联邦学习

### 5.1 概念

**定义**：数据保留在本地，仅共享模型更新。

**特点**：
- 数据隐私保护
- 通信效率
- 数据异质性

### 5.2 FedAvg算法

**算法**：
```
服务器初始化全局模型 w_0
for t = 0, 1, 2, ...:
    服务器选择客户端子集 S_t
    for 每个客户端 i ∈ S_t 并行:
        本地训练：w_i^t = LocalTrain(w_t, D_i)
    聚合：w_{t+1} = (1/|S_t|)∑_{i∈S_t} w_i^t
```

### 5.3 数据异质性挑战

**问题**：各客户端数据分布不同（非IID）。

**解决方案**：
- FedProx：添加近端项
- SCAFFOLD：控制变量修正
- FedNova：归一化平均

## 6. 通信效率优化

### 6.1 通信压缩

**量化**：
$$\text{Quantize}(g) = \text{sign}(g) \cdot \|g\| \cdot \frac{\|g\|_0}{n}$$

**稀疏化**：仅发送最大的 k 个分量。

**Top-K稀疏化**：
$$\tilde{g} = \text{Top-K}(g)$$

### 6.2 本地多步更新

**思路**：减少通信频率，增加本地计算。

**本地SGD**：
```
for 每个工作节点:
    for t = 1 to τ:  # 本地迭代τ步
        x = x - α ∇f_i(x)
    发送 x 到服务器
```

### 6.3 梯度累积

**思路**：累积多步梯度后发送。

**算法**：
```
累计梯度 G = 0
for t = 1 to τ:
    G = G + ∇f_i(x)
发送 G/τ
```

## 7. 理论分析

### 7.1 通信复杂度

**定义**：达到精度 ε 所需的通信轮数。

**结果**：
| 算法 | 通信复杂度（强凸） |
|------|-------------------|
| 分布式SGD | O(log(1/ε)) |
| 分布式加速梯度 | O(√(L/μ) log(1/ε)) |
| 本地SGD | O(log(1/ε)) + 本地迭代 |

### 7.2 计算通信权衡

**权衡**：
- 更多本地计算 → 更少通信
- 但可能降低收敛速度

**最优策略**：本地迭代次数 τ ≈ √(n/K)。

## 8. Python实现

```python
import numpy as np
from multiprocessing import Pool
import time

class DistributedOptimizer:
    """分布式优化器模拟"""
    
    def __init__(self, n_workers, model):
        self.n_workers = n_workers
        self.model = model
        self.params = model.get_params()
    
    def parallel_gradient(self, worker_data):
        """工作节点计算梯度"""
        X, y = worker_data
        return self.model.gradient(X, y)
    
    def sync_sgd(self, data_partitions, epochs=100, lr=0.01):
        """同步分布式SGD"""
        for epoch in range(epochs):
            # 广播参数
            self.model.set_params(self.params)
            
            # 并行计算梯度
            with Pool(self.n_workers) as pool:
                grads = pool.map(self.parallel_gradient, data_partitions)
            
            # 聚合梯度
            avg_grad = np.mean(grads, axis=0)
            
            # 更新参数
            self.params = self.params - lr * avg_grad
            
            if (epoch + 1) % 10 == 0:
                loss = sum(self.model.loss(X, y) for X, y in data_partitions) / self.n_workers
                print(f"Epoch {epoch+1}, Loss: {loss:.4f}")
        
        return self.params

class FedAvg:
    """联邦平均算法"""
    
    def __init__(self, n_clients, model_class):
        self.n_clients = n_clients
        self.model_class = model_class
        self.global_model = None
    
    def client_update(self, client_data):
        """客户端本地训练"""
        X, y, global_params, local_epochs, lr = client_data
        model = self.model_class()
        model.set_params(global_params.copy())
        
        for _ in range(local_epochs):
            grad = model.gradient(X, y)
            params = model.get_params()
            model.set_params(params - lr * grad)
        
        return model.get_params()
    
    def fit(self, client_datasets, n_rounds=50, local_epochs=5, lr=0.01):
        """训练过程"""
        # 初始化全局模型
        model = self.model_class()
        self.global_model = model.get_params()
        
        for round_idx in range(n_rounds):
            # 选择参与本轮的客户端
            selected_clients = np.random.choice(
                self.n_clients, 
                size=max(1, self.n_clients // 10),
                replace=False
            )
            
            # 收集客户端更新
            client_updates = []
            for i in selected_clients:
                X, y = client_datasets[i]
                client_updates.append((X, y, self.global_model, local_epochs, lr))
            
            # 并行执行本地训练
            with Pool(len(selected_clients)) as pool:
                local_params = pool.map(self.client_update, client_updates)
            
            # 聚合
            self.global_model = np.mean(local_params, axis=0)
            
            if (round_idx + 1) % 10 == 0:
                print(f"Round {round_idx+1} completed")
        
        return self.global_model

# 去中心化优化示例
def decentralized_sgd(grad_funcs, W, n_iters=1000, lr=0.01):
    """
    去中心化SGD
    grad_funcs: 各节点的梯度函数列表
    W: 混合矩阵（双随机）
    """
    n = len(grad_funcs)
    n_params = 10  # 参数维度
    X = np.random.randn(n, n_params)  # 各节点参数
    
    for k in range(n_iters):
        # 各节点计算梯度
        grads = np.array([grad_funcs[i](X[i]) for i in range(n)])
        
        # 混合 + 梯度更新
        X = W @ X - lr * grads
    
    return X.mean(axis=0)  # 返回平均值
```

## 9. 应用场景

| 场景 | 方法 | 特点 |
|------|------|------|
| 数据中心 | 参数服务器 | 高效，同步 |
| 边缘计算 | 联邦学习 | 隐私保护 |
| 传感器网络 | 去中心化 | 鲁棒性 |
| 分布式数据库 | ADMM | 约束优化 |

## 10. 总结

**分布式优化的关键问题**：
1. 通信效率：压缩、本地更新
2. 一致性：同步 vs 异步
3. 异质性：非IID数据
4. 隐私：联邦学习

**方法选择**：
- 数据中心：同步分布式SGD
- 边缘设备：联邦学习
- 无中心：去中心化优化
- 约束问题：分布式ADMM

---

**相关链接**：
- [[13_Augmented_Lagrangian]] - 增广拉格朗日法（ADMM）
- [[18_Stochastic_Optimization]] - 随机优化
- [[20_ML_Applications]] - 机器学习应用

