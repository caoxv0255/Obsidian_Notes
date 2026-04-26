---
type: concept
topic: linear_relations
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[08_Vectors]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
---
# 向量组的线性相关性 (Linear Relations)

## 1. 定义

### 1.1 线性组合

向量 $\mathbf{b}$ 是向量组 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 的线性组合，如果存在标量 $c_1, c_2, \ldots, c_n$ 使得：
$$\mathbf{b} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n$$

**几何解释**：线性组合表示用已知向量的伸缩和叠加来构造新的向量。

### 1.2 线性相关

向量组 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 线性相关，如果存在不全为零的标量 $c_1, c_2, \ldots, c_n$ 使得：
$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n = \mathbf{0}$$

**几何解释**：
- 在 $\mathbb{R}^2$ 中：两个向量线性相关意味着它们共线（方向相同或相反）
- 在 $\mathbb{R}^3$ 中：三个向量线性相关意味着它们共面
- 一般情况：线性相关意味着向量组中存在"冗余"，某些向量可以由其他向量表示

### 1.3 线性无关

向量组 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 线性无关，如果方程 $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n = \mathbf{0}$ 只有零解 $c_1 = c_2 = \cdots = c_n = 0$。

**几何解释**：
- 在 $\mathbb{R}^2$ 中：两个向量线性无关意味着它们不共线
- 在 $\mathbb{R}^3$ 中：三个向量线性无关意味着它们不共面
- 一般情况：线性无关意味着每个向量都提供了"新"的方向信息

## 2. 判定定理

### 定理 1：基本判定

**向量组线性相关** $\iff$ $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n = \mathbf{0}$ 有非零解。

### 定理 2：行列式判定（方阵情形）

对于 $n$ 个 $n$ 维向量 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$：

**向量组线性无关** $\iff$ $\det[\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n] \neq 0$

**向量组线性相关** $\iff$ $\det[\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n] = 0$

### 定理 3：矩阵判定

将向量组 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 排列成矩阵 $A = [\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n]$：

**向量组线性无关** $\iff$ $\text{rank}(A) = n$（满秩）

**向量组线性相关** $\iff$ $\text{rank}(A) < n$（秩亏）

### 定理 4：分量个数关系

- $m$ 个 $n$ 维向量，若 $m > n$，则必线性相关
- $m$ 个 $n$ 维向量，若 $m \leq n$，可能线性相关或线性无关

## 3. 重要性质

### 性质 1：零向量的作用

- **包含零向量的向量组必线性相关**

**证明**：设向量组包含 $\mathbf{0}$，取 $c_0 = 1$，其余 $c_i = 0$，则 $1 \cdot \mathbf{0} + 0 \cdot \mathbf{v}_1 + \cdots + 0 \cdot \mathbf{v}_n = \mathbf{0}$，存在非零解。

### 性质 2：部分与整体

- **向量组的部分组线性相关，则整个向量组线性相关**
- **向量组线性无关，则其任意部分组也线性无关**

### 性质 3：延长与缩短

- **线性无关的向量组，在每个向量上添加相同个数的分量后仍线性无关**
- **线性相关的向量组，删去某些分量后仍线性相关**

### 性质 4：线性表示

**向量组线性相关** $\iff$ **某个向量可由其余向量线性表示**

**证明**：
- $\Rightarrow$ 若 $c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n = \mathbf{0}$ 有非零解，不妨设 $c_1 \neq 0$，则 $\mathbf{v}_1 = -\frac{c_2}{c_1}\mathbf{v}_2 - \cdots - \frac{c_n}{c_1}\mathbf{v}_n$
- $\Leftarrow$ 若 $\mathbf{v}_1 = c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n$，则 $\mathbf{v}_1 - c_2\mathbf{v}_2 - \cdots - c_n\mathbf{v}_n = \mathbf{0}$，有非零解

### 性质 5：替换定理

如果 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 线性无关，且 $\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_m$ 可由它们线性表示，则：
- 若 $m > n$，则 $\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_m$ 线性相关
- 若 $m \leq n$，则可以从 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 中选出 $m$ 个向量替换为 $\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_m$，使新向量组仍线性无关

## 4. 特殊情况的判定

### 4.1 单个向量

- **单个向量 $\mathbf{v}$ 线性无关** $\iff$ $\mathbf{v} \neq \mathbf{0}$

### 4.2 两个向量

- **两个向量 $\mathbf{u}, \mathbf{v}$ 线性相关** $\iff$ $\mathbf{u} = k\mathbf{v}$（成比例）
- **几何意义**：共线

### 4.3 三个向量

- **三个向量 $\mathbf{u}, \mathbf{v}, \mathbf{w}$ 线性相关** $\iff$ $\det[\mathbf{u}, \mathbf{v}, \mathbf{w}] = 0$
- **几何意义**：共面

## 5. 正交向量的线性无关性

### 定理：正交向量组

**非零的正交向量组必线性无关。**

**证明**：
设 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 两两正交，且 $\mathbf{v}_i \neq \mathbf{0}$。

假设 $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n = \mathbf{0}$。

两边与 $\mathbf{v}_1$ 作内积：
$$\mathbf{v}_1 \cdot (c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n) = \mathbf{v}_1 \cdot \mathbf{0}$$

$$c_1(\mathbf{v}_1 \cdot \mathbf{v}_1) + c_2(\mathbf{v}_1 \cdot \mathbf{v}_2) + \cdots + c_n(\mathbf{v}_1 \cdot \mathbf{v}_n) = 0$$

由于正交性，$\mathbf{v}_1 \cdot \mathbf{v}_j = 0$（$j \neq 1$），因此：
$$c_1\|\mathbf{v}_1\|^2 = 0$$

由于 $\mathbf{v}_1 \neq \mathbf{0}$，$\|\mathbf{v}_1\|^2 \neq 0$，故 $c_1 = 0$。

同理可得 $c_2 = c_3 = \cdots = c_n = 0$。

因此向量组线性无关。

## 代码示例

### 示例 1：判断向量组的线性相关性

```python
import numpy as np

def check_linear_independence(vectors):
    """判断向量组是否线性无关"""
    A = np.column_stack(vectors)
    rank = np.linalg.matrix_rank(A)
    n_vectors = len(vectors)
    
    if rank == n_vectors:
        return True, rank
    else:
        return False, rank

# 示例 1：线性无关的向量组
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([0, 0, 1])

is_independent, rank = check_linear_independence([v1, v2, v3])
print(f"向量组 {[v1, v2, v3]} 线性无关: {is_independent}, 秩: {rank}")

# 示例 2：线性相关的向量组
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])

is_independent, rank = check_linear_independence([v1, v2, v3])
print(f"向量组 {[v1, v2, v3]} 线性无关: {is_independent}, 秩: {rank}")

# 示例 3：两个向量成比例
v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])

is_independent, rank = check_linear_independence([v1, v2])
print(f"向量组 {[v1, v2]} 线性无关: {is_independent}, 秩: {rank}")
```

### 示例 2：求解线性相关关系

```python
import numpy as np

def find_linear_relation(vectors):
    """寻找线性相关关系（如果存在）"""
    A = np.column_stack(vectors)
    
    # 使用 SVD 找到零空间
    _, _, Vh = np.linalg.svd(A)
    null_space = Vh.T[:, -1]  # 对应最小奇异值的向量
    
    # 验证是否为零空间向量
    if np.allclose(A @ null_space, np.zeros(A.shape[0])):
        return null_space
    else:
        return None

# 线性相关的向量组
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])

relation = find_linear_relation([v1, v2, v3])
if relation is not None:
    print(f"线性相关关系: {relation}")
    print(f"验证: {relation[0]} * v1 + {relation[1]} * v2 + {relation[2]} * v3 = {relation[0] * v1 + relation[1] * v2 + relation[2] * v3}")
else:
    print("向量组线性无关")
```

### 示例 3：Gram-Schmidt 正交化

```python
import numpy as np

def gram_schmidt(vectors):
    """Gram-Schmidt 正交化"""
    orthogonal = []
    
    for v in vectors:
        w = v.copy()
        for u in orthogonal:
            w = w - np.dot(v, u) / np.dot(u, u) * u
        if np.linalg.norm(w) > 1e-10:
            orthogonal.append(w)
    
    return orthogonal

# 原始向量组
v1 = np.array([1, 1, 1])
v2 = np.array([1, 0, 1])
v3 = np.array([0, 1, 0])

vectors = [v1, v2, v3]
orthogonal = gram_schmidt(vectors)

print("原始向量组:")
for i, v in enumerate(vectors):
    print(f"v{i+1}: {v}")

print("\n正交化后的向量组:")
for i, v in enumerate(orthogonal):
    print(f"u{i+1}: {v}")

# 验证正交性
print("\n验证正交性:")
for i in range(len(orthogonal)):
    for j in range(i+1, len(orthogonal)):
        dot = np.dot(orthogonal[i], orthogonal[j])
        print(f"u{i+1} · u{j+1} = {dot:.10f}")
```

### 示例 4：从相关向量组中提取基

```python
import numpy as np

def extract_basis(vectors):
    """从向量组中提取基（删除线性相关的向量）"""
    basis = []
    
    for v in vectors:
        # 检查当前向量是否可由基向量组线性表示
        if len(basis) == 0:
            basis.append(v)
        else:
            A = np.column_stack(basis)
            # 检查 v 是否在 span(basis) 中
            try:
                coefficients = np.linalg.lstsq(A, v, rcond=None)[0]
                if not np.allclose(A @ coefficients, v):
                    basis.append(v)
            except:
                basis.append(v)
    
    return basis

# 线性相关的向量组
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([1, 1, 0])
v4 = np.array([0, 0, 1])

vectors = [v1, v2, v3, v4]
basis = extract_basis(vectors)

print(f"原始向量组（{len(vectors)}个向量）:")
for i, v in enumerate(vectors):
    print(f"v{i+1}: {v}")

print(f"\n提取的基（{len(basis)}个向量）:")
for i, v in enumerate(basis):
    print(f"b{i+1}: {v}")

print(f"\n原始向量组的秩: {np.linalg.matrix_rank(np.column_stack(vectors))}")
print(f"提取的基的秩: {np.linalg.matrix_rank(np.column_stack(basis))}")
```

## 机器学习应用

### 应用 1：特征选择与降维

在机器学习中，特征之间可能存在线性相关性，导致：
- 信息冗余
- 模型过拟合
- 计算效率低下

通过检测和去除线性相关的特征，可以提高模型性能。

```python
import numpy as np

def remove_correlated_features(X, threshold=0.99):
    """去除高度相关的特征"""
    n_features = X.shape[1]
    to_remove = set()
    
    for i in range(n_features):
        if i in to_remove:
            continue
        for j in range(i+1, n_features):
            if j in to_remove:
                continue
            
            # 计算相关性
            corr = np.abs(np.corrcoef(X[:, i], X[:, j])[0, 1])
            
            if corr > threshold:
                to_remove.add(j)
                print(f"特征 {i} 和 {j} 高度相关（相关性: {corr:.4f}），移除特征 {j}")
    
    keep = [i for i in range(n_features) if i not in to_remove]
    return X[:, keep], keep

# 示例数据
np.random.seed(42)
n_samples = 100
X = np.random.randn(n_samples, 5)

# 添加一些线性相关的特征
X[:, 2] = X[:, 0] * 2 + X[:, 1] * 3  # 特征2是特征0和1的线性组合
X[:, 4] = X[:, 3] * 0.95 + np.random.randn(n_samples) * 0.1  # 特征4与特征3高度相关

print(f"原始特征数: {X.shape[1]}")
X_reduced, keep = remove_correlated_features(X)
print(f"降维后特征数: {X_reduced.shape[1]}")
print(f"保留的特征索引: {keep}")
```

### 应用 2：线性模型的可解释性

在线性回归中，如果特征之间存在线性相关性，会导致系数估计不稳定。

```python
import numpy as np
from sklearn.linear_model import LinearRegression

def analyze_feature_importance(X, y):
    """分析特征重要性"""
    model = LinearRegression()
    model.fit(X, y)
    
    coefficients = model.coef_
    feature_names = [f"特征{i}" for i in range(X.shape[1])]
    
    print("特征系数:")
    for name, coef in zip(feature_names, coefficients):
        print(f"{name}: {coef:.4f}")
    
    # 检查特征相关性
    corr_matrix = np.corrcoef(X.T)
    print("\n特征相关性矩阵:")
    print(np.round(corr_matrix, 3))
    
    return model

# 示例：有线性相关特征的数据
np.random.seed(42)
n_samples = 100
X = np.random.randn(n_samples, 3)

# 真实关系：y = 2*x0 + 3*x1 + 噪声
y = 2 * X[:, 0] + 3 * X[:, 1] + np.random.randn(n_samples) * 0.1

# 添加相关特征
X_with_corr = np.column_stack([X, X[:, 0] + X[:, 1]])  # 特征3是特征0和1的和

print("原始数据（无相关特征）:")
model1 = analyze_feature_importance(X, y)

print("\n添加相关特征后的数据:")
model2 = analyze_feature_importance(X_with_corr, y)
```

### 应用 3：神经网络中的权重初始化

在神经网络中，如果同一层的权重向量线性相关，会导致网络表达能力下降。

```python
import numpy as np

def check_weight_diversity(W):
    """检查权重向量的多样性（线性相关性）"""
    n_neurons = W.shape[1]
    rank = np.linalg.matrix_rank(W)
    
    print(f"权重矩阵形状: {W.shape}")
    print(f"权重矩阵的秩: {rank}")
    print(f"神经元数量: {n_neurons}")
    print(f"线性无关的神经元: {rank}")
    
    if rank < n_neurons:
        print(f"⚠️  警告: 存在 {n_neurons - rank} 个线性相关的神经元!")
        print("   建议: 使用正交初始化")
    else:
        print("✓ 所有神经元权重向量线性无关")
    
    return rank == n_neurons

# 示例 1: 随机初始化
np.random.seed(42)
W_random = np.random.randn(10, 5)

print("=" * 50)
print("示例 1: 随机初始化")
print("=" * 50)
check_weight_diversity(W_random)

# 示例 2: 使用相同的初始化
W_same = np.zeros((10, 5))
W_same[:, :] = W_random[:, 0:1]  # 所有列相同

print("\n" + "=" * 50)
print("示例 2: 所有神经元使用相同的初始化")
print("=" * 50)
check_weight_diversity(W_same)

# 示例 3: 正交初始化
def orthogonal_init(shape):
    """正交初始化"""
    flat_shape = (shape[0], np.prod(shape[1:]))
    Q = np.linalg.qr(np.random.randn(*flat_shape))[0]
    Q = Q.reshape(shape)
    return Q

W_orthogonal = orthogonal_init((10, 5))

print("\n" + "=" * 50)
print("示例 3: 正交初始化")
print("=" * 50)
check_weight_diversity(W_orthogonal)
```

## 严格证明

### 证明 1：$n+1$ 个 $n$ 维向量必线性相关

**定理**：$n+1$ 个 $n$ 维向量必线性相关。

**证明**：

设 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_{n+1}$ 是 $n$ 维向量。

考虑齐次线性方程组：
$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_{n+1}\mathbf{v}_{n+1} = \mathbf{0}$$

这可以写成矩阵形式 $A\mathbf{c} = \mathbf{0}$，其中：
- $A$ 是 $n \times (n+1)$ 矩阵，列向量是 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_{n+1}$
- $\mathbf{c} = [c_1, c_2, \ldots, c_{n+1}]^T$

由于 $A$ 的行数 $n$ 小于列数 $n+1$，根据线性代数理论，齐次方程组 $A\mathbf{c} = \mathbf{0}$ 必有非零解。

因此存在不全为零的 $c_1, c_2, \ldots, c_{n+1}$ 使得上述方程成立，即向量组线性相关。

### 证明 2：线性无关向量组的子集线性无关

**定理**：如果向量组 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 线性无关，则其任意子集也线性无关。

**证明**（反证法）：

假设 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 线性无关，但存在子集 $\mathbf{v}_{i_1}, \mathbf{v}_{i_2}, \ldots, \mathbf{v}_{i_k}$（$k \leq n$）线性相关。

则存在不全为零的标量 $c_{i_1}, c_{i_2}, \ldots, c_{i_k}$ 使得：
$$c_{i_1}\mathbf{v}_{i_1} + c_{i_2}\mathbf{v}_{i_2} + \cdots + c_{i_k}\mathbf{v}_{i_k} = \mathbf{0}$$

现在构造一个包含原向量组所有向量的线性组合：
- 对于子集中的向量，使用系数 $c_{i_j}$
- 对于不在子集中的向量，使用系数 $0$

这样得到的线性组合 $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n = \mathbf{0}$ 有非零解（因为 $c_{i_1}, c_{i_2}, \ldots, c_{i_k}$ 不全为零）。

这与 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 线性无关矛盾。

因此假设不成立，任意子集必线性无关。

### 证明 3：线性相关组的超集线性相关

**定理**：如果向量组的部分组线性相关，则整个向量组线性相关。

**证明**：

设向量组 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 的子组 $\mathbf{v}_{i_1}, \mathbf{v}_{i_2}, \ldots, \mathbf{v}_{i_k}$ 线性相关。

则存在不全为零的标量 $c_{i_1}, c_{i_2}, \ldots, c_{i_k}$ 使得：
$$c_{i_1}\mathbf{v}_{i_1} + c_{i_2}\mathbf{v}_{i_2} + \cdots + c_{i_k}\mathbf{v}_{i_k} = \mathbf{0}$$

现在考虑整个向量组的线性组合：
- 对于子组中的向量，使用系数 $c_{i_j}$
- 对于其他向量，使用系数 $0$

这样得到的线性组合：
$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n = \mathbf{0}$$

由于 $c_{i_1}, c_{i_2}, \ldots, c_{i_k}$ 不全为零，整个向量组存在非零解，因此线性相关。

### 证明 4：延长定理

**定理**：如果 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 线性无关，则在每个向量上添加相同个数的分量后，新向量组仍线性无关。

**证明**：

设 $\mathbf{v}_i = [v_{i1}, v_{i2}, \ldots, v_{ik}]^T$（$i = 1, 2, \ldots, n$）线性无关。

在每个向量上添加 $m$ 个分量，得到新向量 $\mathbf{w}_i = [v_{i1}, v_{i2}, \ldots, v_{ik}, w_{i1}, w_{i2}, \ldots, w_{im}]^T$。

假设新向量组线性相关，则存在不全为零的标量 $c_1, c_2, \ldots, c_n$ 使得：
$$c_1\mathbf{w}_1 + c_2\mathbf{w}_2 + \cdots + c_n\mathbf{w}_n = \mathbf{0}$$

这意味着：
$$\begin{cases}
c_1v_{11} + c_2v_{21} + \cdots + c_nv_{n1} = 0 \\
c_1v_{12} + c_2v_{22} + \cdots + c_nv_{n2} = 0 \\
\vdots \\
c_1v_{1k} + c_2v_{2k} + \cdots + c_nv_{nk} = 0 \\
c_1w_{11} + c_2w_{21} + \cdots + c_nw_{n1} = 0 \\
\vdots \\
c_1w_{1m} + c_2w_{2m} + \cdots + c_nw_{nm} = 0
\end{cases}$$

前 $k$ 个方程说明：
$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n = \mathbf{0}$$

由于 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 线性无关，必有 $c_1 = c_2 = \cdots = c_n = 0$。

这与假设矛盾，因此新向量组线性无关。

## 例题

### 例题 1：判断向量组的线性相关性

**问题**：判断向量组 $\mathbf{v}_1 = [1, 2, 3]^T$，$\mathbf{v}_2 = [4, 5, 6]^T$，$\mathbf{v}_3 = [7, 8, 9]^T$ 是否线性相关。

**解法 1：利用行列式**

构造矩阵 $A = [\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3]$：
$$A = \begin{bmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{bmatrix}$$

计算行列式：
$$\det(A) = 1 \cdot \begin{vmatrix} 5 & 8 \\ 6 & 9 \end{vmatrix} - 4 \cdot \begin{vmatrix} 2 & 8 \\ 3 & 9 \end{vmatrix} + 7 \cdot \begin{vmatrix} 2 & 5 \\ 3 & 6 \end{vmatrix}$$

$$= 1 \cdot (45 - 48) - 4 \cdot (18 - 24) + 7 \cdot (12 - 15)$$

$$= 1 \cdot (-3) - 4 \cdot (-6) + 7 \cdot (-3)$$

$$= -3 + 24 - 21 = 0$$

由于 $\det(A) = 0$，向量组线性相关。

**解法 2：利用秩**

构造矩阵 $A$ 并求秩：
$$A = \begin{bmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{bmatrix}$$

进行初等行变换：
$$A \xrightarrow{R_2-2R_1} \begin{bmatrix} 1 & 4 & 7 \\ 0 & -3 & -6 \\ 3 & 6 & 9 \end{bmatrix} \xrightarrow{R_3-3R_1} \begin{bmatrix} 1 & 4 & 7 \\ 0 & -3 & -6 \\ 0 & -6 & -12 \end{bmatrix} \xrightarrow{R_3-2R_2} \begin{bmatrix} 1 & 4 & 7 \\ 0 & -3 & -6 \\ 0 & 0 & 0 \end{bmatrix}$$

秩 $\text{rank}(A) = 2 < 3$，因此向量组线性相关。

**解法 3：观察法**

注意到 $\mathbf{v}_3 - 2\mathbf{v}_2 + \mathbf{v}_1 = [7, 8, 9]^T - 2[4, 5, 6]^T + [1, 2, 3]^T = [7-8+1, 8-10+2, 9-12+3]^T = [0, 0, 0]^T$

因此存在非零解（$1, -2, 1$），向量组线性相关。

### 例题 2：求解线性相关关系

**问题**：已知向量组 $\mathbf{v}_1 = [1, 1, 1]^T$，$\mathbf{v}_2 = [1, 2, 3]^T$，$\mathbf{v}_3 = [2, 3, 4]^T$ 线性相关，求线性相关关系。

**解**：

设 $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0}$，即：
$$c_1\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} + c_2\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + c_3\begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$

这给出方程组：
$$\begin{cases} c_1 + c_2 + 2c_3 = 0 \\ c_1 + 2c_2 + 3c_3 = 0 \\ c_1 + 3c_2 + 4c_3 = 0 \end{cases}$$

写成增广矩阵：
$$\begin{bmatrix} 1 & 1 & 2 & 0 \\ 1 & 2 & 3 & 0 \\ 1 & 3 & 4 & 0 \end{bmatrix} \xrightarrow{R_2-R_1} \begin{bmatrix} 1 & 1 & 2 & 0 \\ 0 & 1 & 1 & 0 \\ 1 & 3 & 4 & 0 \end{bmatrix} \xrightarrow{R_3-R_1} \begin{bmatrix} 1 & 1 & 2 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 2 & 2 & 0 \end{bmatrix} \xrightarrow{R_3-2R_2} \begin{bmatrix} 1 & 1 & 2 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

得到：
$$\begin{cases} c_1 + c_2 + 2c_3 = 0 \\ c_2 + c_3 = 0 \end{cases}$$

设 $c_3 = t$（$t$ 为自由参数），则 $c_2 = -t$，$c_1 = -c_2 - 2c_3 = t - 2t = -t$。

取 $t = 1$，得到非零解 $c_1 = -1, c_2 = -1, c_3 = 1$。

验证：$-\mathbf{v}_1 - \mathbf{v}_2 + \mathbf{v}_3 = -[1, 1, 1]^T - [1, 2, 3]^T + [2, 3, 4]^T = [0, 0, 0]^T$

线性相关关系为：$\mathbf{v}_3 = \mathbf{v}_1 + \mathbf{v}_2$。

### 例题 3：判断参数取值

**问题**：设 $\mathbf{v}_1 = [1, 2, 1]^T$，$\mathbf{v}_2 = [1, 3, 2]^T$，$\mathbf{v}_3 = [1, a, 3]^T$，问 $a$ 为何值时向量组线性相关？

**解**：

构造行列式：
$$\det(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3) = \begin{vmatrix} 1 & 1 & 1 \\ 2 & 3 & a \\ 1 & 2 & 3 \end{vmatrix}$$

$$= 1 \cdot \begin{vmatrix} 3 & a \\ 2 & 3 \end{vmatrix} - 1 \cdot \begin{vmatrix} 2 & a \\ 1 & 3 \end{vmatrix} + 1 \cdot \begin{vmatrix} 2 & 3 \\ 1 & 2 \end{vmatrix}$$

$$= 1 \cdot (9 - 2a) - 1 \cdot (6 - a) + 1 \cdot (4 - 3)$$

$$= 9 - 2a - 6 + a + 1$$

$$= 4 - a$$

向量组线性相关当且仅当行列式为零：
$$4 - a = 0$$

因此 $a = 4$ 时向量组线性相关。

### 例题 4：证明线性无关

**问题**：证明向量组 $\mathbf{v}_1 = [1, 0, 0]^T$，$\mathbf{v}_2 = [1, 1, 0]^T$，$\mathbf{v}_3 = [1, 1, 1]^T$ 线性无关。

**证明**：

设 $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0}$，即：
$$c_1\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} + c_3\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$

这给出方程组：
$$\begin{cases} c_1 + c_2 + c_3 = 0 \\ c_2 + c_3 = 0 \\ c_3 = 0 \end{cases}$$

从第三个方程得 $c_3 = 0$。

代入第二个方程得 $c_2 = 0$。

代入第一个方程得 $c_1 = 0$。

因此只有零解，向量组线性无关。

### 例题 5：利用线性相关性判断能否表示

**问题**：已知 $\mathbf{v}_1 = [1, 0, 1]^T$，$\mathbf{v}_2 = [0, 1, 1]^T$，$\mathbf{v}_3 = [1, 1, 2]^T$，
1. 判断 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ 是否线性相关
2. 判断 $\mathbf{b} = [2, 3, 5]^T$ 能否由 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ 线性表示

**解**：

1. **判断线性相关性**

计算行列式：
$$\det(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3) = \begin{vmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 2 \end{vmatrix} = 1 \cdot \begin{vmatrix} 1 & 1 \\ 1 & 2 \end{vmatrix} - 0 + 1 \cdot \begin{vmatrix} 0 & 1 \\ 1 & 1 \end{vmatrix} = (2-1) + (0-1) = 0$$

因此 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ 线性相关。

实际上，$\mathbf{v}_3 = \mathbf{v}_1 + \mathbf{v}_2$。

2. **判断能否表示**

由于 $\mathbf{v}_3 = \mathbf{v}_1 + \mathbf{v}_2$，$\text{span}(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3) = \text{span}(\mathbf{v}_1, \mathbf{v}_2)$。

判断 $\mathbf{b}$ 能否由 $\mathbf{v}_1, \mathbf{v}_2$ 线性表示：
设 $x\mathbf{v}_1 + y\mathbf{v}_2 = \mathbf{b}$，即：
$$x\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} + y\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 3 \\ 5 \end{bmatrix}$$

这给出方程组：
$$\begin{cases} x = 2 \\ y = 3 \\ x + y = 5 \end{cases}$$

解得 $x = 2, y = 3$，满足所有方程。

因此 $\mathbf{b} = 2\mathbf{v}_1 + 3\mathbf{v}_2$ 可以由 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ 线性表示。

## 习题

### 基础题

1. 判断向量组 $\mathbf{v}_1 = [1, 1, 1]^T$，$\mathbf{v}_2 = [0, 1, 1]^T$，$\mathbf{v}_3 = [0, 0, 1]^T$ 是否线性无关。

2. 设 $\mathbf{v}_1 = [1, 2]^T$，$\mathbf{v}_2 = [3, 6]^T$，判断它们是否线性相关。

3. 求参数 $a$ 使得向量组 $\mathbf{v}_1 = [1, 1, a]^T$，$\mathbf{v}_2 = [1, a, 1]^T$，$\mathbf{v}_3 = [a, 1, 1]^T$ 线性相关。

4. 已知 $\mathbf{v}_1 = [1, 0, 0]^T$，$\mathbf{v}_2 = [1, 1, 0]^T$ 线性无关，求 $\mathbf{v}_3 = [1, 1, 1]^T$ 使 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ 线性无关。

5. 证明：包含零向量的向量组必线性相关。

### 进阶题

6. 设 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ 线性无关，证明 $\mathbf{v}_1 + \mathbf{v}_2, \mathbf{v}_2 + \mathbf{v}_3, \mathbf{v}_3 + \mathbf{v}_1$ 也线性无关。

7. 设 $A$ 是 $n$ 阶方阵，证明：$A$ 的列向量线性无关 $\iff$ $A$ 的行向量线性无关 $\iff$ $\det(A) \neq 0$。

8. 设 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ 线性相关，$\mathbf{v}_2, \mathbf{v}_3, \mathbf{v}_4$ 线性无关，证明：
   (1) $\mathbf{v}_1$ 可由 $\mathbf{v}_2, \mathbf{v}_3$ 线性表示
   (2) $\mathbf{v}_4$ 不能由 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ 线性表示

9. 设 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 线性无关，而 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n, \mathbf{w}$ 线性相关，证明 $\mathbf{w}$ 可由 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 唯一地线性表示。

10. 证明：若 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 两两正交且都不为零，则它们线性无关。

### 挑战题

11. 设 $V$ 是所有 $2 \times 2$ 实矩阵构成的向量空间，判断以下矩阵是否线性相关：
    $A_1 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$, $A_2 = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$, $A_3 = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}$, $A_4 = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$, $A_5 = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$

12. 设 $P_n$ 是所有次数不超过 $n$ 的多项式构成的向量空间，判断 $1, x, x^2, \ldots, x^n$ 是否线性无关。

13. 在机器学习中，为什么线性相关的特征会导致模型性能下降？举例说明如何检测和去除线性相关的特征。

14. 证明替换定理：如果 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 线性无关，且 $\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_m$ 可由它们线性表示，若 $m \leq n$，则可以从 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 中选出 $m$ 个向量替换为 $\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_m$，使新向量组仍线性无关。

15. 研究函数空间 $C[0, 1]$ 中函数的线性无关性，判断以下函数组是否线性无关：
    $f_1(x) = 1$, $f_2(x) = x$, $f_3(x) = x^2$, $f_4(x) = e^x$

## 注意事项

⚠️ **常见错误**

1. **混淆线性相关和线性表示**
   - 线性相关是向量组的性质
   - 线性表示是一个向量能否由其他向量表示
   - 两者有关联但不等价

2. **错误使用行列式判定**
   - 行列式判定只适用于向量个数等于向量维数的情况
   - 对于 $m \neq n$ 的情况，应该使用秩的方法

3. **忽略特殊情况**
   - 单个向量的情况
   - 包含零向量的情况
   - 向量个数大于维数的情况

✅ **最佳实践**

1. **灵活运用多种判定方法**
   - 行列式法（方阵情形）
   - 秩法（一般情形）
   - 定义法（理论证明）

2. **掌握几何直观**
   - 理解线性相关的几何意义
   - 二维：共线
   - 三维：共面

3. **理解线性相关性的应用**
   - 特征选择和降维
   - 基的提取
   - 模型可解释性

## 题型总结与思路技巧

### 线性相关性判断方法

#### 📋 判断方法选择

| 向量个数 | 推荐方法 |
|---------|---------|
| 2个 | 看是否成比例 |
| 3个 | 看是否共面 |
| 多个 | 行列式法或秩法 |

### 💡 核心技巧与常用结论

#### 1. 线性相关的等价条件

对于向量组 $\mathbf{v}_1, \ldots, \mathbf{v}_n$，以下等价：
- 存在不全为零的 $c_1, \ldots, c_n$ 使 $\sum c_i \mathbf{v}_i = \mathbf{0}$
- 某个向量可由其余向量线性表示
- 矩阵 $[\mathbf{v}_1 \cdots \mathbf{v}_n]$ 的秩 $< n$

#### 2. 线性无关的等价条件

- 只有零解使 $\sum c_i \mathbf{v}_i = \mathbf{0}$
- 没有向量可由其余向量表示
- 矩阵 $[\mathbf{v}_1 \cdots \mathbf{v}_n]$ 的秩 $= n$

#### 3. 重要结论

- $n$个$n$维向量线性相关 $\Leftrightarrow$ 行列式为0
- $n+1$个$n$维向量必线性相关
- 线性无关组的部分组仍线性无关
- 线性相关组添加向量仍线性相关

#### 4. 几何意义

| 维度 | 线性相关 | 线性无关 |
|-----|---------|---------|
| 2D | 共线 | 不共线 |
| 3D | 共面 | 不共面 |
| nD | 落在低维空间 | 张成全空间 |

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 判断线性相关 | 行列式/秩法 | $|A| = 0$ 则相关 |
| 证明线性无关 | 定义法或反证法 | 设$k_1v_1+\cdots+k_nv_n=0$ |
| 求线性表示系数 | 解方程组 | 高斯消元 |
| 证明向量组等价 | 互相线性表示 | 秩相等 |

### ⚠️ 常见错误

**错误一**：混淆"存在"与"任意"
- 线性相关：**存在**非零组合为零
- 不是任意组合都为零

**错误二**：部分与整体
- 线性无关组的部分组：仍无关
- 线性相关组添加向量：仍相关

**错误三**：判断方法选择
- 少量向量：直接判断
- 多个向量：用秩或行列式

## 本章小结

### 重要定义
1. 线性组合：用已知向量的伸缩和叠加构造新向量
2. 线性相关：存在非零的线性组合为零向量
3. 线性无关：只有零解能使线性组合为零向量

### 重要定理
1. 行列式判定定理
2. 矩阵秩判定定理
3. 正交向量组必线性无关
4. $n+1$ 个 $n$ 维向量必线性相关

### 重要性质
1. 包含零向量的向量组必线性相关
2. 部分组线性相关则整体线性相关
3. 线性无关组的任意子组线性无关
4. 延长线性无关组仍线性无关

### 重要应用
1. 机器学习中的特征选择
2. 线性模型的可解释性分析
3. 神经网络权重初始化

本章为学习基与维数、线性方程组等后续内容奠定了基础。

## 相关概念

- [[08_Vectors]] - 向量基础
- [[10_Basis_Dimension]] - 基与维数
- [[02_Matrix_Basics]] - 矩阵基础
- [[07_Matrix_Rank]] - 矩阵的秩
- [[11_Linear_Equations]] - 线性方程组

## 参考教材

- 《线性代数》（第6版），同济大学数学系，第三章
- 《Introduction to Linear Algebra》（第5版），Gilbert Strang, Chapter 3
- 《高等代数简明教程》（第2版），北京大学数学系，第二章

