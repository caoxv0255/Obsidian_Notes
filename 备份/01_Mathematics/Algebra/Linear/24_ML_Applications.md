---
type: concept
topic: ml_applications
category: linear_algebra
difficulty: advanced
prerequisites:
  - [[21_SVD]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
---
# 机器学习应用 (Machine Learning Applications)

## 1. 线性代数在 ML 中的应用

### 1.1 数据表示

- **向量**：特征向量、词嵌入、注意力权重
- **矩阵**：数据集、权重矩阵、注意力矩阵
- **张量**：图像、视频、批量数据

### 1.2 核心算法

- **线性回归**：最小二乘法
- **PCA**：特征值分解
- **SVD**：降维、推荐系统
- **神经网络**：矩阵乘法

## 2. 深度学习

### 2.1 前向传播

$$\mathbf{y} = \sigma(W\mathbf{x} + \mathbf{b})$$

### 2.2 反向传播

使用链式法则计算梯度。

## 3. 实际案例

### 3.1 图像识别

卷积使用矩阵运算。

### 3.2 自然语言处理

词嵌入使用向量空间。

### 3.3 推荐系统

矩阵分解用于协同过滤。

## 代码示例

```python
import numpy as np

# 简单神经网络
W1 = np.random.randn(784, 128)
b1 = np.zeros(128)
W2 = np.random.randn(128, 10)
b2 = np.zeros(10)

def forward(x):
    h = np.maximum(0, x @ W1 + b1)
    y = h @ W2 + b2
    return y
```

## 严格证明

### 证明：线性回归的解

**定理**：线性回归的最小二乘解为 $\mathbf{w} = (X^T X)^{-1} X^T \mathbf{y}$。

**证明**：

最小化目标函数：
$$J(\mathbf{w}) = \|X\mathbf{w} - \mathbf{y}\|^2 = (X\mathbf{w} - \mathbf{y})^T (X\mathbf{w} - \mathbf{y})$$

展开：
$$J(\mathbf{w}) = \mathbf{w}^T X^T X \mathbf{w} - 2\mathbf{y}^T X \mathbf{w} + \mathbf{y}^T \mathbf{y}$$

求梯度并令为零：
$$\nabla J(\mathbf{w}) = 2X^T X \mathbf{w} - 2X^T \mathbf{y} = \mathbf{0}$$

解得：
$$\mathbf{w} = (X^T X)^{-1} X^T \mathbf{y}$$

## 例题

### 例题 1：线性回归

**问题**：给定数据点 $(1, 2)$，$(2, 3)$，$(3, 5)$，用线性回归拟合 $y = ax + b$。

**解**：

构造矩阵：
$$X = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}, \quad \mathbf{y} = \begin{bmatrix} 2 \\ 3 \\ 5 \end{bmatrix}$$

计算 $X^T X = \begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}$，$(X^T X)^{-1} = \frac{1}{6}\begin{bmatrix} 14 & -6 \\ -6 & 3 \end{bmatrix}$

$X^T \mathbf{y} = \begin{bmatrix} 10 \\ 23 \end{bmatrix}$

解：$\mathbf{w} = (X^T X)^{-1} X^T \mathbf{y} = \frac{1}{6}\begin{bmatrix} 14 & -6 \\ -6 & 3 \end{bmatrix}\begin{bmatrix} 10 \\ 23 \end{bmatrix} = \frac{1}{6}\begin{bmatrix} 2 \\ 9 \end{bmatrix} = \begin{bmatrix} 1/3 \\ 3/2 \end{bmatrix}$

因此 $y = \frac{3}{2}x + \frac{1}{3}$。

### 例题 2：PCA

**问题**：对数据 $[1, 1]^T$，$[2, 2]^T$，$[3, 1]^T$ 进行 PCA。

**解**：

中心化数据：$[0, 0]^T$，$[1, 1]^T$，$[2, 0]^T$

计算协方差矩阵：
$$\Sigma = \frac{1}{3}\begin{bmatrix} 0 & 0 & 2 \\ 0 & 0 & 0 \end{bmatrix} + \frac{1}{3}\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} + \frac{1}{3}\begin{bmatrix} 4 & 0 \\ 0 & 0 \end{bmatrix} = \frac{1}{3}\begin{bmatrix} 5 & 0 \\ 0 & 0 \end{bmatrix}$$

特征值：$\lambda_1 = 5/3$，$\lambda_2 = 0$

主成分：$[1, 0]^T$

### 例题 3：SVD降维

**问题**：用 SVD 对矩阵 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$ 进行 1 秩近似。

**解**：

计算 $A^T A = \begin{bmatrix} 35 & 44 \\ 44 & 56 \end{bmatrix}$

特征值：$\lambda_1 \approx 90.5$，$\lambda_2 \approx 0.5$

奇异值：$\sigma_1 \approx 9.5$

1 秩近似：$A_1 = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^T \approx \begin{bmatrix} 1.25 & 1.79 \\ 2.82 & 4.05 \\ 4.39 & 6.30 \end{bmatrix}$

## 习题

### 基础题

1. 用线性回归拟合数据点 $(0, 1)$，$(1, 3)$，$(2, 5)$。

2. 计算矩阵 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ 的特征值和特征向量。

3. 对数据 $[1, 2]^T$，$[2, 4]^T$，$[3, 1]^T$ 进行 PCA。

4. 用 SVD 对矩阵 $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ 进行降维。

5. 证明：线性回归的目标函数是凸函数。

### 进阶题

6. 证明：线性回归的最小二乘解。

7. 证明：PCA 的主成分方向是最大方差方向。

8. 证明：SVD 的低秩近似是最优的。

9. 推导反向传播的梯度公式。

10. 证明：交叉熵损失函数的凸性。

### 挑战题

11. 研究 Transformer 中的注意力机制的线性代数基础。

12. 证明：Batch Normalization 的数学原理。

13. 研究 GNN（图神经网络）中的拉普拉斯矩阵。

14. 证明：ResNet 的梯度流动性质。

15. 研究 Autoencoder 的数学原理。

## 注意事项

⚠️ **常见错误**

1. **混淆转置和共轭转置**
   - 实数矩阵：相同
   - 复数矩阵：不同

2. **忽略数值稳定性**
   - 直接求逆可能不稳定
   - 应使用 SVD 或 QR 分解

3. **错误理解维度**
   - 特征向量是列向量
   - 数据矩阵的行是样本

✅ **最佳实践**

1. **使用矩阵运算**
   - 避免循环
   - 利用向量化

2. **理解几何意义**
   - 特征值：伸缩因子
   - 特征向量：不变方向

3. **选择合适算法**
   - 大数据：随机化算法
   - 稀疏数据：稀疏矩阵运算

## 题型总结与思路技巧

### 线性代数在机器学习中的应用

#### 📋 核心应用领域

| 应用 | 核心数学 | 关键技术 |
|-----|---------|---------|
| **线性回归** | 最小二乘法 | $(X^TX)^{-1}X^T\mathbf{y}$ |
| **PCA降维** | 特征值分解 | 协方差矩阵对角化 |
| **推荐系统** | SVD分解 | 矩阵分解、低秩近似 |
| **神经网络** | 矩阵乘法 | 前向传播、反向传播 |
| **图像处理** | 正交变换 | DCT、小波变换 |

### 💡 核心技巧与常用结论

#### 1. 线性回归

**问题**：$\min_{\mathbf{w}} \|X\mathbf{w} - \mathbf{y}\|^2$

**解**：$\mathbf{w}^* = (X^TX)^{-1}X^T\mathbf{y}$（或伪逆）

**正则化**：
- Ridge：$\mathbf{w} = (X^TX + \lambda I)^{-1}X^T\mathbf{y}$
- Lasso：需要迭代求解

#### 2. PCA主成分分析

**步骤**：
1. 中心化数据
2. 计算协方差矩阵$C = X^TX/n$
3. 特征值分解
4. 选择前$k$个主成分

**方差解释**：第$i$个主成分解释的方差比例 = $\lambda_i / \sum \lambda_j$

#### 3. 神经网络中的矩阵运算

- **前向传播**：$\mathbf{h} = \sigma(W\mathbf{x} + \mathbf{b})$
- **反向传播**：链式法则，梯度计算
- **参数更新**：$\theta \leftarrow \theta - \eta \nabla L$

#### 4. 降维技术比较

| 方法 | 原理 | 适用场景 |
|-----|------|---------|
| PCA | 线性投影，最大化方差 | 线性数据 |
| SVD | 矩阵分解 | 稀疏矩阵、推荐 |
| t-SNE | 非线性嵌入 | 可视化 |
| UMAP | 流形学习 | 高维数据 |

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 线性回归求解 | 正规方程或梯度下降 | 矩阵求逆或迭代 |
| PCA实现 | 协方差矩阵特征分解 | 特征值排序 |
| 降维效果评估 | 方差解释率 | 选择合适维度 |
| 推荐系统 | SVD或矩阵分解 | 处理稀疏性 |
| 神经网络计算 | 矩阵乘法链 | 维数匹配 |

### ⚠️ 常见错误

**错误一**：PCA前未中心化
- 必须先减去均值
- 否则第一主成分方向会偏离

**错误二**：混淆SVD与特征值分解
- SVD适用于任意矩阵
- 特征值分解仅适用于方阵

**错误三**：正则化参数选择
- 需要交叉验证
- 不是越大越好或越小越好

## 本章小结

### 重要应用
1. 线性回归：最小二乘法
2. PCA：特征值分解
3. SVD：降维、推荐系统
4. 神经网络：矩阵乘法

### 重要概念
1. 特征值分解
2. 奇异值分解
3. 最小二乘法
4. 正则化

## 相关概念

- [[21_SVD]] - 奇异值分解
- [[22_Pseudoinverse]] - 伪逆
- [[12_Least_Squares]] - 最小二乘法

## 参考教材

- 《深度学习》，Goodfellow 等，第二章
- 《Introduction to Linear Algebra》（第5版），Gilbert Strang, Chapter 7

