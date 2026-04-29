---
type: concept
topic: basis_dimension
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[08_Vectors]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 10
---

# 基与维数 (Basis and Dimension)

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

## 1. 基的定义

### 1.1 线性无关

向量组 $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ 线性无关，如果：
$$\sum_{i=1}^n c_i \mathbf{v}_i = \mathbf{0} \implies c_1 = c_2 = \cdots = c_n = 0$$

### 1.2 生成空间

向量组 $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ 生成空间 $V$，如果：
$$V = \text{span}\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\} = \left\{\sum_{i=1}^n c_i \mathbf{v}_i \mid c_i \in \mathbb{R}\right\}$$

### 1.3 基的定义

向量空间 $V$ 的基 $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ 满足：
1. **线性无关**：基中的向量线性无关
2. **生成 $V$**：$V$ 中任意向量都可由基线性表示

### 1.4 维数的定义

向量空间 $V$ 的维数 $\dim(V)$ 是基中向量的个数。

**重要性质**：
- 基不唯一，但维数唯一
- $\dim(\mathbb{R}^n) = n$
- $\dim(P_n) = n + 1$（$P_n$ 是次数不超过 $n$ 的多项式空间）

## 2. 基的性质

### 2.1 唯一表示定理

**定理**：如果 $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ 是 $V$ 的基，则任意 $\mathbf{v} \in V$ 可以唯一表示为：
$$\mathbf{v} = c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_n \mathbf{v}_n$$

**证明**：

- 存在性：由于 $\mathcal{B}$ 生成 $V$，$\mathbf{v}$ 可以表示为 $\mathcal{B}$ 的线性组合
- 唯一性：假设 $\mathbf{v} = \sum_{i=1}^n c_i \mathbf{v}_i = \sum_{i=1}^n d_i \mathbf{v}_i$，则 $\sum_{i=1}^n (c_i - d_i)\mathbf{v}_i = \mathbf{0}$
  - 由于 $\mathcal{B}$ 线性无关，$c_i - d_i = 0$，即 $c_i = d_i$

### 2.2 坐标

给定基 $\mathcal{B} = \{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$，向量 $\mathbf{v}$ 的坐标为：
$$[\mathbf{v}]_{\mathcal{B}} = \begin{bmatrix}
c_1 \\
c_2 \\
\vdots \\
c_n
\end{bmatrix}$$

其中 $\mathbf{v} = c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_n \mathbf{v}_n$。

### 2.3 坐标映射

坐标映射 $[\cdot]_{\mathcal{B}}: V \to \mathbb{R}^n$ 是同构（线性双射）。

**性质**：
- $[\mathbf{u} + \mathbf{v}]_{\mathcal{B}} = [\mathbf{u}]_{\mathcal{B}} + [\mathbf{v}]_{\mathcal{B}}$
- $[c\mathbf{v}]_{\mathcal{B}} = c[\mathbf{v}]_{\mathcal{B}}$

### 2.4 基的性质总结

1. **极小生成集**：基是生成 $V$ 的最小向量组
2. **极大线性无关组**：基是 $V$ 中最大的线性无关向量组
3. **基变换**：任何两个基之间有可逆的基变换矩阵

## 3. 常见基

### 3.1 标准基

$\mathbb{R}^n$ 的标准基：
$$\mathcal{E} = \{\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n\}$$

其中 $\mathbf{e}_i = [0, \ldots, 0, 1, 0, \ldots, 0]^T$（第 $i$ 个分量为 1，其余为 0）。

例如，$\mathbb{R}^3$ 的标准基：
$$\mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad \mathbf{e}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \quad \mathbf{e}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

### 3.2 正交基

如果基中的向量两两正交，则称为正交基：

$$\mathbf{v}_i \cdot \mathbf{v}_j = 0 \quad (i \neq j)$$

**性质**：
- 正交基的向量必线性无关
- 坐标计算简单：$c_i = \frac{\mathbf{v} \cdot \mathbf{v}_i}{\mathbf{v}_i \cdot \mathbf{v}_i}$

### 3.3 标准正交基

如果基中的向量两两正交且长度为 1，则称为标准正交基：

$$\mathbf{v}_i \cdot \mathbf{v}_j = \begin{cases}
1 & i = j \\
0 & i \neq j
\end{cases}$$

**性质**：
- 坐标计算最简单：$c_i = \mathbf{v} \cdot \mathbf{v}_i$
- 坐标变换矩阵是正交矩阵

### 3.4 多项式空间的基

$P_n$（次数不超过 $n$ 的多项式空间）的常用基：

1. **标准基**：$\{1, x, x^2, \ldots, x^n\}$
2. **拉格朗日基**：$\{L_0(x), L_1(x), \ldots, L_n(x)\}$
3. **切比雪夫基**：$\{T_0(x), T_1(x), \ldots, T_n(x)\}$

### 3.5 矩阵空间的基

$M_{m \times n}$（$m \times n$ 矩阵空间）的基：

$$\{E_{ij} \mid 1 \leq i \leq m, 1 \leq j \leq n\}$$

其中 $E_{ij}$ 是第 $i$ 行第 $j$ 列为 1，其余为 0 的矩阵。

维数：$\dim(M_{m \times n}) = m \times n$。

## 4. 基变换

### 4.1 基变换矩阵

设 $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2, \ldots, \mathbf{b}_n\}$ 和 $\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2, \ldots, \mathbf{c}_n\}$ 是 $V$ 的两个基。

基变换矩阵 $P_{\mathcal{C} \leftarrow \mathcal{B}}$ 满足：
$$[\mathbf{v}]_{\mathcal{C}} = P_{\mathcal{C} \leftarrow \mathcal{B}} [\mathbf{v}]_{\mathcal{B}}$$

### 4.2 基变换矩阵的计算

基变换矩阵 $P_{\mathcal{C} \leftarrow \mathcal{B}}$ 的列是 $\mathcal{B}$ 中的向量在 $\mathcal{C}$ 下的坐标：

$$P_{\mathcal{C} \leftarrow \mathcal{B}} = \begin{bmatrix} [\mathbf{b}_1]_{\mathcal{C}} & [\mathbf{b}_2]_{\mathcal{C}} & \cdots & [\mathbf{b}_n]_{\mathcal{C}} \end{bmatrix}$$

### 4.3 基变换矩阵的性质

1. **可逆性**：$P_{\mathcal{C} \leftarrow \mathcal{B}}$ 可逆，且 $P_{\mathcal{C} \leftarrow \mathcal{B}}^{-1} = P_{\mathcal{B} \leftarrow \mathcal{C}}$
2. **链式法则**：$P_{\mathcal{D} \leftarrow \mathcal{B}} = P_{\mathcal{D} \leftarrow \mathcal{C}} \cdot P_{\mathcal{C} \leftarrow \mathcal{B}}$
3. **标准基转换**：若 $\mathcal{E}$ 是标准基，则 $P_{\mathcal{E} \leftarrow \mathcal{B}} = [\mathbf{b}_1, \mathbf{b}_2, \ldots, \mathbf{b}_n]$

## 5. 子空间的基

### 5.1 子空间维数定理

**定理**：如果 $W$ 是 $n$ 维向量空间 $V$ 的子空间，则 $W$ 也是有限维的，且 $\dim(W) \leq \dim(V)$。

### 5.2 基的扩展定理

**定理**：$W$ 的任何基都可以扩展为 $V$ 的基。

### 5.3 维数公式

**定理**：对于 $V$ 的子空间 $W_1, W_2$：
$$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$

## 代码示例

### 示例 1：判断向量组是否为基

```python
import numpy as np

def is_basis(vectors, dim=None, tolerance=1e-10):
    """判断向量组是否为基"""
    vectors = np.array(vectors, dtype=float)
    
    if vectors.ndim != 2:
        return False, "向量组必须是一个矩阵"
    
    n_vectors, n_dims = vectors.shape
    
    # 检查向量个数是否等于空间维数
    if dim is not None and n_vectors != dim:
        return False, f"向量个数 {n_vectors} 不等于空间维数 {dim}"
    
    # 检查线性无关性
    rank = np.linalg.matrix_rank(vectors, tol=tolerance)
    
    if rank == n_vectors:
        return True, f"是基，维数为 {n_vectors}"
    else:
        return False, f"不是基，秩为 {rank}，需要 {rank} 个向量"

# 示例 1：标准基
basis1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).T
result, msg = is_basis(basis1, dim=3)
print(f"标准基: {msg}")

# 示例 2：线性相关的向量组
basis2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).T
result, msg = is_basis(basis2, dim=3)
print(f"线性相关组: {msg}")

# 示例 3：正交基
basis3 = np.array([[1, 1, 0], [1, -1, 0], [0, 0, 1]]).T
result, msg = is_basis(basis3, dim=3)
print(f"正交基: {msg}")
```

### 示例 2：计算向量在基下的坐标

```python
import numpy as np

def coordinates_in_basis(vector, basis, tolerance=1e-10):
    """计算向量在给定基下的坐标"""
    vector = np.array(vector, dtype=float).reshape(-1, 1)
    basis = np.array(basis, dtype=float)
    
    # 检查基是否有效
    if np.linalg.matrix_rank(basis, tol=tolerance) != basis.shape[1]:
        raise ValueError("给定的向量组不是基")
    
    # 求解 basis * x = vector
    coordinates = np.linalg.solve(basis, vector)
    
    # 验证
    reconstructed = basis @ coordinates
    if not np.allclose(reconstructed, vector, atol=tolerance):
        raise ValueError("无法精确表示该向量")
    
    return coordinates.flatten()

# 示例：向量 v = [5, 7, 9] 在不同基下的坐标
v = np.array([5, 7, 9])

# 基 1：标准基
B1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).T
coords1 = coordinates_in_basis(v, B1)
print(f"向量 {v} 在标准基下的坐标: {coords1}")

# 基 2：非标准基
B2 = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]]).T
coords2 = coordinates_in_basis(v, B2)
print(f"向量 {v} 在非标准基下的坐标: {coords2}")

# 验证：基 2 下的坐标重建原向量
v_reconstructed = B2 @ coords2
print(f"验证: {v_reconstructed} ≈ {v}")
```

### 示例 3：基变换

```python
import numpy as np

def basis_change_matrix(B_old, B_new):
    """计算基变换矩阵 P_new <- old"""
    B_old = np.array(B_old, dtype=float)
    B_new = np.array(B_new, dtype=float)
    
    # 基变换矩阵的列是旧基在新基下的坐标
    P = np.linalg.solve(B_new, B_old)
    
    return P

# 示例：从标准基到非标准基的变换
E = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).T  # 标准基
B = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]]).T  # 非标准基

# 计算基变换矩阵 P_B <- E
P = basis_change_matrix(E, B)
print(f"基变换矩阵 P_B <- E:\n{P}")

# 验证：v 在 E 下的坐标是 v 本身
v = np.array([5, 7, 9])
coords_E = v
coords_B = P @ coords_E
print(f"\n向量 {v} 在标准基下的坐标: {coords_E}")
print(f"向量 {v} 在基 B 下的坐标: {coords_B}")

# 验证逆变换
P_inv = np.linalg.inv(P)
coords_E_recovered = P_inv @ coords_B
print(f"验证逆变换: {coords_E_recovered} ≈ {coords_E}")
```

### 示例 4：Gram-Schmidt 正交化

```python
import numpy as np

def gram_schmidt(vectors, normalize=True):
    """Gram-Schmidt 正交化"""
    vectors = np.array(vectors, dtype=float)
    n = vectors.shape[1]
    
    orthogonal = []
    
    for i in range(n):
        v = vectors[:, i].copy()
        
        # 减去在前面所有向量上的投影
        for u in orthogonal:
            v = v - np.dot(v, u) / np.dot(u, u) * u
        
        # 如果向量非零，添加到正交基
        if np.linalg.norm(v) > 1e-10:
            if normalize:
                v = v / np.linalg.norm(v)
            orthogonal.append(v)
    
    return np.column_stack(orthogonal)

# 原始向量组
vectors = np.array([[1, 1, 1], [1, 0, 1], [0, 1, 1]]).T
print("原始向量组:")
print(vectors)

# Gram-Schmidt 正交化
orthogonal_basis = gram_schmidt(vectors, normalize=True)
print("\n正交基（归一化）:")
print(orthogonal_basis)

# 验证正交性
print("\n验证正交性:")
for i in range(orthogonal_basis.shape[1]):
    for j in range(i+1, orthogonal_basis.shape[1]):
        dot = np.dot(orthogonal_basis[:, i], orthogonal_basis[:, j])
        print(f"u{i+1} · u{j+1} = {dot:.10f}")

# 验证单位长度
print("\n验证单位长度:")
for i in range(orthogonal_basis.shape[1]):
    norm = np.linalg.norm(orthogonal_basis[:, i])
    print(f"||u{i+1}|| = {norm:.10f}")
```

### 示例 5：从向量组中提取基

```python
import numpy as np

def extract_basis(vectors, tolerance=1e-10):
    """从向量组中提取基"""
    vectors = np.array(vectors, dtype=float)
    
    # 使用 SVD 提取线性无关的向量
    U, s, Vt = np.linalg.svd(vectors)
    rank = np.linalg.matrix_rank(vectors, tol=tolerance)
    
    # 提取前 rank 个向量作为基
    basis_indices = []
    for i in range(rank):
        # 找到最大的主成分对应的原向量
        max_idx = np.argmax(np.abs(Vt[i, :]))
        if max_idx not in basis_indices:
            basis_indices.append(max_idx)
    
    basis = vectors[:, basis_indices]
    
    return basis, basis_indices

# 示例：从相关向量组中提取基
vectors = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
    [1, 0, 1]
]).T

print(f"原始向量组（{vectors.shape[1]}个向量）:")
print(vectors)

basis, indices = extract_basis(vectors)
print(f"\n提取的基（{basis.shape[1]}个向量）:")
print(basis)
print(f"基的索引: {indices}")

# 验证
rank_original = np.linalg.matrix_rank(vectors)
rank_basis = np.linalg.matrix_rank(basis)
print(f"\n原始向量组的秩: {rank_original}")
print(f"提取的基的秩: {rank_basis}")
```

## 机器学习应用

### 应用 1：PCA（主成分分析）

PCA 找到数据的最优基，使数据在该基下的表示具有最大方差。

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# 加载数据
iris = load_iris()
X = iris.data
y = iris.target

# 使用 PCA 找到最优基
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print(f"原始特征维数: {X.shape[1]}")
print(f"PCA 后特征维数: {X_pca.shape[1]}")
print(f"解释方差比: {pca.explained_variance_ratio_}")
print(f"累计解释方差: {sum(pca.explained_variance_ratio_):.4f}")

# PCA 的基向量是主成分
print(f"\nPCA 基向量的形状: {pca.components_.shape}")
print("PCA 基向量（主成分）:")
for i, component in enumerate(pca.components_):
    print(f"PC{i+1}: {component}")

# 可视化
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', alpha=0.7)
plt.xlabel(f'PC1 (方差比: {pca.explained_variance_ratio_[0]:.2%})')
plt.ylabel(f'PC2 (方差比: {pca.explained_variance_ratio_[1]:.2%})')
plt.title('PCA 降维可视化')
plt.colorbar(scatter, label='类别')
plt.grid(True, alpha=0.3)
plt.show()
```

### 应用 2：特征空间的基选择

不同的基选择对机器学习模型的性能有重要影响。

```python
import numpy as np
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 加载数据
digits = load_digits()
X = digits.data
y = digits.target

# 基 1：原始像素空间（标准基）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model1 = LogisticRegression(max_iter=1000)
model1.fit(X_train, y_train)
score1 = model1.score(X_test, y_test)
print(f"使用标准基（原始像素）的准确率: {score1:.4f}")

# 基 2：PCA 基
from sklearn.decomposition import PCA

pca = PCA(n_components=32)
X_pca = pca.fit_transform(X)
X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split(X_pca, y, test_size=0.2, random_state=42)

model2 = LogisticRegression(max_iter=1000)
model2.fit(X_train_pca, y_train_pca)
score2 = model2.score(X_test_pca, y_test_pca)
print(f"使用 PCA 基的准确率: {score2:.4f}")

# 基 3：随机投影基
from sklearn.random_projection import GaussianRandomProjection

rp = GaussianRandomProjection(n_components=32)
X_rp = rp.fit_transform(X)
X_train_rp, X_test_rp, y_train_rp, y_test_rp = train_test_split(X_rp, y, test_size=0.2, random_state=42)

model3 = LogisticRegression(max_iter=1000)
model3.fit(X_train_rp, y_train_rp)
score3 = model3.score(X_test_rp, y_test_rp)
print(f"使用随机投影基的准确率: {score3:.4f}")

print(f"\n压缩比: 64 -> 32 ({50.0}%)")
```

### 应用 3：字典学习

字典学习学习数据的稀疏表示基，用于信号处理和图像压缩。

```python
import numpy as np
from sklearn.decomposition import DictionaryLearning
from sklearn.feature_extraction.image import extract_patches_2d
import matplotlib.pyplot as plt

# 生成合成数据
np.random.seed(42)
n_samples = 200
n_features = 64
n_components = 16

# 创建稀疏信号
X = np.zeros((n_samples, n_features))
for i in range(n_samples):
    # 随机选择 3-5 个基向量
    n_active = np.random.randint(3, 6)
    active_indices = np.random.choice(n_components, n_active, replace=False)
    coefficients = np.random.randn(n_active)
    
    # 合成信号
    for idx, coeff in zip(active_indices, coefficients):
        X[i, idx*4:(idx+1)*4] += coeff * np.random.randn(4)

# 添加噪声
X += np.random.randn(*X.shape) * 0.1

# 字典学习
dict_learner = DictionaryLearning(n_components=n_components, 
                                   transform_algorithm='lasso_lars',
                                   random_state=42)
X_transformed = dict_learner.fit_transform(X)
dictionary = dict_learner.components_

print(f"原始数据形状: {X.shape}")
print(f"字典形状: {dictionary.shape}")
print(f"稀疏表示形状: {X_transformed.shape}")
print(f"稀疏度: {np.mean(X_transformed == 0):.2%}")

# 可视化字典
fig, axes = plt.subplots(4, 4, figsize=(10, 10))
for i, ax in enumerate(axes.flat):
    ax.imshow(dictionary[i].reshape(8, 8), cmap='gray')
    ax.set_title(f'原子 {i+1}')
    ax.axis('off')
plt.suptitle('学习到的字典原子')
plt.tight_layout()
plt.show()
```

## 严格证明

### 证明 1：基的维数唯一性

**定理**：有限维向量空间的所有基有相同数量的向量。

**证明**：

设 $\mathcal{B}_1 = \{\mathbf{b}_1, \mathbf{b}_2, \ldots, \mathbf{b}_m\}$ 和 $\mathcal{B}_2 = \{\mathbf{c}_1, \mathbf{c}_2, \ldots, \mathbf{c}_n\}$ 是 $V$ 的两个基。

假设 $m > n$。

由于 $\mathcal{B}_2$ 是基，$\mathbf{b}_1$ 可以表示为 $\mathcal{B}_2$ 的线性组合：
$$\mathbf{b}_1 = \sum_{j=1}^n a_{1j} \mathbf{c}_j$$

同理：
$$\mathbf{b}_i = \sum_{j=1}^n a_{ij} \mathbf{c}_j, \quad i = 1, 2, \ldots, m$$

考虑齐次线性方程组 $\sum_{i=1}^m x_i \mathbf{b}_i = \mathbf{0}$：

$$\sum_{i=1}^m x_i \left(\sum_{j=1}^n a_{ij} \mathbf{c}_j\right) = \sum_{j=1}^n \left(\sum_{i=1}^m a_{ij} x_i\right) \mathbf{c}_j = \mathbf{0}$$

由于 $\mathcal{B}_2$ 线性无关，有：
$$\sum_{i=1}^m a_{ij} x_i = 0, \quad j = 1, 2, \ldots, n$$

这是一个 $n$ 个方程、$m$ 个未知数的齐次线性方程组。由于 $m > n$，存在非零解。

因此存在不全为零的 $x_1, x_2, \ldots, x_m$ 使得 $\sum_{i=1}^m x_i \mathbf{b}_i = \mathbf{0}$，与 $\mathcal{B}_1$ 线性无关矛盾！

因此 $m \leq n$。同理可证 $n \leq m$，故 $m = n$。

### 证明 2：坐标映射是同构

**定理**：坐标映射 $[\cdot]_{\mathcal{B}}: V \to \mathbb{R}^n$ 是同构（线性双射）。

**证明**：

**线性性**：
- 设 $\mathbf{u}, \mathbf{v} \in V$，$\mathbf{u} = \sum_{i=1}^n u_i \mathbf{b}_i$，$\mathbf{v} = \sum_{i=1}^n v_i \mathbf{b}_i$
- 则 $\mathbf{u} + \mathbf{v} = \sum_{i=1}^n (u_i + v_i) \mathbf{b}_i$
- 所以 $[\mathbf{u} + \mathbf{v}]_{\mathcal{B}} = [u_1 + v_1, u_2 + v_2, \ldots, u_n + v_n]^T = [\mathbf{u}]_{\mathcal{B}} + [\mathbf{v}]_{\mathcal{B}}$
- 同理可证 $[c\mathbf{v}]_{\mathcal{B}} = c[\mathbf{v}]_{\mathcal{B}}$

**单射**：
- 设 $[\mathbf{u}]_{\mathcal{B}} = [\mathbf{v}]_{\mathcal{B}}$
- 则 $\mathbf{u} = \sum_{i=1}^n u_i \mathbf{b}_i = \sum_{i=1}^n v_i \mathbf{b}_i = \mathbf{v}$
- 所以 $\mathbf{u} = \mathbf{v}$

**满射**：
- 对于任意 $[c_1, c_2, \ldots, c_n]^T \in \mathbb{R}^n$
- 令 $\mathbf{v} = \sum_{i=1}^n c_i \mathbf{b}_i$
- 则 $[\mathbf{v}]_{\mathcal{B}} = [c_1, c_2, \ldots, c_n]^T$

因此坐标映射是同构。

### 证明 3：维数公式

**定理**：对于 $V$ 的子空间 $W_1, W_2$：
$$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$

**证明**：

设 $\{\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_k\}$ 是 $W_1 \cap W_2$ 的基，其中 $k = \dim(W_1 \cap W_2)$。

将此基扩展为：
- $W_1$ 的基：$\{\mathbf{u}_1, \ldots, \mathbf{u}_k, \mathbf{v}_1, \ldots, \mathbf{v}_m\}$，其中 $m = \dim(W_1) - k$
- $W_2$ 的基：$\{\mathbf{u}_1, \ldots, \mathbf{u}_k, \mathbf{w}_1, \ldots, \mathbf{w}_n\}$，其中 $n = \dim(W_2) - k$

**步骤 1**：证明 $\{\mathbf{u}_1, \ldots, \mathbf{u}_k, \mathbf{v}_1, \ldots, \mathbf{v}_m, \mathbf{w}_1, \ldots, \mathbf{w}_n\}$ 是 $W_1 + W_2$ 的基。

- 生成性：任意 $\mathbf{x} \in W_1 + W_2$ 可以表示为 $\mathbf{x} = \mathbf{y} + \mathbf{z}$，其中 $\mathbf{y} \in W_1, \mathbf{z} \in W_2$
  - $\mathbf{y} = \sum_{i=1}^k a_i \mathbf{u}_i + \sum_{j=1}^m b_j \mathbf{v}_j$
  - $\mathbf{z} = \sum_{i=1}^k c_i \mathbf{u}_i + \sum_{l=1}^n d_l \mathbf{w}_l$
  - 所以 $\mathbf{x} = \sum_{i=1}^k (a_i + c_i) \mathbf{u}_i + \sum_{j=1}^m b_j \mathbf{v}_j + \sum_{l=1}^n d_l \mathbf{w}_l$

- 线性无关性：假设
  $$\sum_{i=1}^k a_i \mathbf{u}_i + \sum_{j=1}^m b_j \mathbf{v}_j + \sum_{l=1}^n c_l \mathbf{w}_l = \mathbf{0}$$
  - 令 $\mathbf{y} = \sum_{i=1}^k a_i \mathbf{u}_i + \sum_{j=1}^m b_j \mathbf{v}_j \in W_1$
  - 令 $\mathbf{z} = \sum_{l=1}^n c_l \mathbf{w}_l \in W_2$
  - 则 $\mathbf{y} = -\mathbf{z} \in W_1 \cap W_2$
  - 所以 $\mathbf{z} = \sum_{l=1}^n c_l \mathbf{w}_l$ 可以用 $\{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$ 表示
  - 由于 $\{\mathbf{u}_1, \ldots, \mathbf{u}_k, \mathbf{w}_1, \ldots, \mathbf{w}_n\}$ 线性无关，$c_l = 0$
  - 同理 $b_j = 0$，然后 $a_i = 0$

**步骤 2**：计算维数。

$$\dim(W_1 + W_2) = k + m + n = \dim(W_1 \cap W_2) + (\dim(W_1) - k) + (\dim(W_2) - k)$$

$$= \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$

## 例题

### 例题 1：判断向量组是否为基

**问题**：判断 $\mathcal{B} = \{[1, 1, 0]^T, [1, 0, 1]^T, [0, 1, 1]^T\}$ 是否为 $\mathbb{R}^3$ 的基。

**解**：

构造矩阵 $A = [\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3]$：
$$A = \begin{bmatrix}
1 & 1 & 0 \\
1 & 0 & 1 \\
0 & 1 & 1
\end{bmatrix}$$

计算行列式：
$$\det(A) = 1 \cdot (0 \cdot 1 - 1 \cdot 1) - 1 \cdot (1 \cdot 1 - 0 \cdot 1) + 0 \cdot (1 \cdot 1 - 0 \cdot 0)$$

$$= 1 \cdot (-1) - 1 \cdot 1 + 0 = -1 - 1 = -2 \neq 0$$

因此 $A$ 可逆，$\mathcal{B}$ 线性无关且生成 $\mathbb{R}^3$，是基。

### 例题 2：计算向量在基下的坐标

**问题**：设 $\mathcal{B} = \{[1, 1]^T, [1, -1]^T\}$ 是 $\mathbb{R}^2$ 的基，求 $\mathbf{v} = [5, 7]^T$ 在 $\mathcal{B}$ 下的坐标。

**解**：

设 $\mathbf{v} = c_1[1, 1]^T + c_2[1, -1]^T$，即：
$$\begin{cases} c_1 + c_2 = 5 \\ c_1 - c_2 = 7 \end{cases}$$

解得：
$$c_1 = \frac{5 + 7}{2} = 6$$
$$c_2 = \frac{5 - 7}{2} = -1$$

因此 $[\mathbf{v}]_{\mathcal{B}} = [6, -1]^T$。

验证：$6[1, 1]^T + (-1)[1, -1]^T = [6-1, 6+1]^T = [5, 7]^T$。

### 例题 3：基变换

**问题**：设 $\mathcal{B} = \{[1, 1, 0]^T, [1, 0, 1]^T, [0, 1, 1]^T\}$ 和 $\mathcal{C} = \{[1, 0, 0]^T, [0, 1, 0]^T, [0, 0, 1]^T\}$ 是 $\mathbb{R}^3$ 的两个基。
1. 求基变换矩阵 $P_{\mathcal{C} \leftarrow \mathcal{B}}$
2. 求向量 $\mathbf{v} = [3, 4, 5]^T$ 在 $\mathcal{B}$ 下的坐标

**解**：

1. **求基变换矩阵 $P_{\mathcal{C} \leftarrow \mathcal{B}}$**

$\mathcal{C}$ 是标准基，所以 $P_{\mathcal{C} \leftarrow \mathcal{B}}$ 的列就是 $\mathcal{B}$ 中的向量：
$$P_{\mathcal{C} \leftarrow \mathcal{B}} = \begin{bmatrix}
1 & 1 & 0 \\
1 & 0 & 1 \\
0 & 1 & 1
\end{bmatrix}$$

2. **求 $\mathbf{v}$ 在 $\mathcal{B}$ 下的坐标**

由于 $\mathbf{v}$ 在标准基下的坐标是 $[\mathbf{v}]_{\mathcal{C}} = [3, 4, 5]^T$，我们有：
$$[\mathbf{v}]_{\mathcal{C}} = P_{\mathcal{C} \leftarrow \mathcal{B}} [\mathbf{v}]_{\mathcal{B}}$$

因此：
$$[\mathbf{v}]_{\mathcal{B}} = P_{\mathcal{C} \leftarrow \mathcal{B}}^{-1} [\mathbf{v}]_{\mathcal{C}}$$

先求逆矩阵：
$$P_{\mathcal{C} \leftarrow \mathcal{B}}^{-1} = \frac{1}{\det(P)} \text{adj}(P) = \frac{1}{-2} \begin{bmatrix}
-1 & -1 & 1 \\
-1 & 1 & -1 \\
1 & -1 & -1
\end{bmatrix} = \begin{bmatrix}
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
-\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{bmatrix}$$

计算坐标：
$$[\mathbf{v}]_{\mathcal{B}} = \begin{bmatrix}
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
-\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{bmatrix} \begin{bmatrix} 3 \\ 4 \\ 5 \end{bmatrix} = \begin{bmatrix}
\frac{3+4-5}{2} \\
\frac{3-4+5}{2} \\
\frac{-3+4+5}{2}
\end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$$

验证：$1[1, 1, 0]^T + 2[1, 0, 1]^T + 3[0, 1, 1]^T = [3, 4, 5]^T$。

### 例题 4：从相关向量组中提取基

**问题**：从向量组 $\mathbf{v}_1 = [1, 0, 0]^T$，$\mathbf{v}_2 = [0, 1, 0]^T$，$\mathbf{v}_3 = [1, 1, 0]^T$，$\mathbf{v}_4 = [0, 0, 1]^T$ 中提取一组基。

**解**：

方法 1：观察法

注意到 $\mathbf{v}_3 = \mathbf{v}_1 + \mathbf{v}_2$，所以 $\mathbf{v}_3$ 可以删除。

剩余的向量 $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_4\}$ 线性无关，是 $\mathbb{R}^3$ 的基。

方法 2：矩阵法

构造矩阵 $A = [\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3, \mathbf{v}_4]$：
$$A = \begin{bmatrix}
1 & 0 & 1 & 0 \\
0 & 1 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}$$

进行初等行变换得到行阶梯形：
$$A = \begin{bmatrix}
1 & 0 & 1 & 0 \\
0 & 1 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}$$

主元所在的列是第 1、2、4 列，对应的向量是 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_4$。

因此基为 $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_4\}$。

### 例题 5：维数公式的应用

**问题**：设 $W_1 = \{(x, y, z) \mid x + y + z = 0\}$ 和 $W_2 = \{(x, y, z) \mid x - y = 0\}$ 是 $\mathbb{R}^3$ 的两个子空间，求 $\dim(W_1 + W_2)$ 和 $\dim(W_1 \cap W_2)$。

**解**：

1. **求 $\dim(W_1)$**

$W_1$ 由方程 $x + y + z = 0$ 定义，是 $\mathbb{R}^3$ 的一个平面，维数为 2。

基：$\mathbf{v}_1 = [1, -1, 0]^T$，$\mathbf{v}_2 = [1, 0, -1]^T$

2. **求 $\dim(W_2)$**

$W_2$ 由方程 $x - y = 0$ 定义，是 $\mathbb{R}^3$ 的一个平面，维数为 2。

基：$\mathbf{w}_1 = [1, 1, 0]^T$，$\mathbf{w}_2 = [0, 0, 1]^T$

3. **求 $W_1 \cap W_2$**

$W_1 \cap W_2$ 满足：
$$\begin{cases} x + y + z = 0 \\ x - y = 0 \end{cases}$$

由第二个方程得 $x = y$，代入第一个方程：
$$2x + z = 0 \implies z = -2x$$

所以 $W_1 \cap W_2 = \{(x, x, -2x) \mid x \in \mathbb{R}\}$，是一条直线，维数为 1。

基：$\mathbf{u} = [1, 1, -2]^T$

4. **求 $\dim(W_1 + W_2)$**

根据维数公式：
$$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2) = 2 + 2 - 1 = 3$$

因此 $W_1 + W_2 = \mathbb{R}^3$。

## 习题

### 基础题

1. 判断 $\mathcal{B} = \{[1, 2]^T, [3, 4]^T\}$ 是否为 $\mathbb{R}^2$ 的基。

2. 求 $\mathbf{v} = [5, 7]^T$ 在基 $\mathcal{B} = \{[1, 1]^T, [1, -1]^T\}$ 下的坐标。

3. 找出向量组 $\mathbf{v}_1 = [1, 2, 3]^T$，$\mathbf{v}_2 = [4, 5, 6]^T$，$\mathbf{v}_3 = [7, 8, 9]^T$ 的基。

4. 构造 $\mathbb{R}^3$ 的一个正交基。

5. 证明：标准基 $\{\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n\}$ 是 $\mathbb{R}^n$ 的基。

### 进阶题

6. 设 $\mathcal{B} = \{[1, 1, 0]^T, [1, 0, 1]^T, [0, 1, 1]^T\}$ 和 $\mathcal{C}$ 是标准基，求基变换矩阵 $P_{\mathcal{B} \leftarrow \mathcal{C}}$。

7. 证明：基变换矩阵是可逆的，且 $P_{\mathcal{C} \leftarrow \mathcal{B}}^{-1} = P_{\mathcal{B} \leftarrow \mathcal{C}}$。

8. 设 $W_1 = \text{span}\{[1, 1, 0]^T, [0, 1, 1]^T\}$，$W_2 = \text{span}\{[1, 0, 1]^T, [1, 1, 1]^T\}$，求 $\dim(W_1 + W_2)$ 和 $\dim(W_1 \cap W_2)$。

9. 证明：有限维子空间的任何子空间都是有限维的。

10. 证明：$\dim(M_{m \times n}) = m \times n$，其中 $M_{m \times n}$ 是所有 $m \times n$ 矩阵构成的向量空间。

### 挑战题

11. 研究无限维向量空间的基（Hamel 基）的概念和性质。

12. 证明：任何线性无关向量组都可以扩展为基（基扩展定理）。

13. 在深度学习中，为什么稀疏基（如字典学习）比标准基有优势？从表示能力和计算效率两个角度分析。

14. 研究 K-SVD 算法及其在图像处理中的应用，并给出简单的 Python 实现。

15. 证明：Gram-Schmidt 正交化过程的正确性，并证明它总是产生正交基。

## 注意事项

⚠️ **常见错误**

1. **混淆基和生成集**
   - 基必须同时满足线性无关和生成空间
   - 生成集不一定线性无关
   - 线性无关组不一定生成整个空间

2. **错误计算基变换矩阵**
   - $P_{\mathcal{C} \leftarrow \mathcal{B}}$ 的列是 $\mathcal{B}$ 在 $\mathcal{C}$ 下的坐标
   - 不要混淆变换方向

3. **忽略基的不唯一性**
   - 基不唯一，但维数唯一
   - 同一向量在不同基下有不同的坐标

✅ **最佳实践**

1. **灵活运用判定方法**
   - 行列式法（方阵情形）
   - 秩法（一般情形）
   - 定义法（理论证明）

2. **理解基的几何意义**
   - 基定义了坐标系统
   - 基变换是坐标系统的转换

3. **掌握标准正交基的优势**
   - 坐标计算简单
   - 保持长度和角度
   - 变换矩阵是正交矩阵

## 题型总结与思路技巧

### 基与维数核心方法

#### 📋 关键概念

| 概念 | 定义 | 判定方法 |
|-----|------|---------|
| **基** | 线性无关的生成集 | 线性无关 + 生成全空间 |
| **维数** | 基中向量个数 | 所有基向量数相同 |
| **坐标** | 在基下的表示 | 解线性方程组 |

### 💡 核心技巧与常用结论

#### 1. 基的等价条件

向量组 $\mathbf{v}_1, \ldots, \mathbf{v}_n$ 是 $V$ 的基，当且仅当：
- 线性无关
- 生成 $V$（$\text{span}(\mathbf{v}_1, \ldots, \mathbf{v}_n) = V$）

**等价表述**：
- 任意 $v \in V$ 可唯一表示为 $v = \sum c_i \mathbf{v}_i$
- 矩阵 $[\mathbf{v}_1 \cdots \mathbf{v}_n]$ 可逆（对$n$维空间）

#### 2. 维数公式

**和空间维数公式**：
$$\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$$

**直和**：$U \cap W = \{0\}$ 时
$$\dim(U \oplus W) = \dim U + \dim W$$

#### 3. 标准正交基

**Gram-Schmidt正交化**：
1. $\mathbf{u}_1 = \mathbf{v}_1$
2. $\mathbf{u}_2 = \mathbf{v}_2 - \frac{\langle \mathbf{v}_2, \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1, \mathbf{u}_1 \rangle} \mathbf{u}_1$
3. 继续正交化...

**单位化**：$\mathbf{e}_i = \frac{\mathbf{u}_i}{\|\mathbf{u}_i\|}$

#### 4. 基变换

**坐标变换公式**：
$$[\mathbf{v}]_{\mathcal{B}'} = P^{-1} [\mathbf{v}]_{\mathcal{B}}$$

其中 $P$ 是从基 $\mathcal{B}'$ 到基 $\mathcal{B}$ 的过渡矩阵。

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 判断是否为基 | 验证线性无关+生成 | 检查向量个数=维数 |
| 求维数 | 找极大线性无关组 | 秩即为维数 |
| 求坐标 | 解方程组 | 在基下的唯一表示 |
| 基变换 | 过渡矩阵 | $[\mathbf{v}]_{new} = P^{-1}[\mathbf{v}]_{old}$ |
| 正交化 | Gram-Schmidt | 逐个正交化 |

### ⚠️ 常见错误

**错误一**：基不唯一
- 基不是唯一的，但维数唯一
- 同一空间可以有很多不同的基

**错误二**：坐标变换方向
- 注意是从哪个基到哪个基
- 过渡矩阵的逆表示反向变换

**错误三**：Gram-Schmidt顺序
- 正交化顺序影响结果
- 但最终都是正交基

## 本章小结

### 重要定义
1. 基：线性无关的生成集
2. 维数：基中向量的个数
3. 坐标：向量在基下的表示

### 重要定理
1. 基的维数唯一性
2. 坐标映射是同构
3. 维数公式
4. 基扩展定理

### 重要性质
1. 基不唯一，但维数唯一
2. 任何线性无关组都可扩展为基
3. 基变换矩阵是可逆的

### 重要应用
1. PCA 降维
2. 特征空间基选择
3. 字典学习和稀疏表示

本章为学习线性方程组、线性变换等后续内容奠定了基础。

## 相关概念

- [[08_Vectors]] - 向量基础
- [[09_Linear_Relations]] - 线性相关性
- [[11_Linear_Equations]] - 线性方程组
- [[02_Matrix_Basics]] - 矩阵基础

## 参考教材

- 《线性代数》（第6版），同济大学数学系，第四章
- 《Introduction to Linear Algebra》（第5版），Gilbert Strang, Chapter 3
- 《高等代数简明教程》（第2版），北京大学数学系，第三章


