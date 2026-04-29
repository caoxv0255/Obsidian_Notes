---
type: concept
topic: inner_product
category: linear_algebra
difficulty: intermediate
prerequisites:
  - [[08_Vectors]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 18
---

# 内积空间 (Inner Product Spaces)

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

## 1. 内积的定义

### 1.1 定义

内积空间 $V$ 是配备了内积的向量空间。内积 $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{R}$ 满足以下公理：

1. **对称性**：$\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$
2. **线性性（第一变元）**：$\langle \lambda\mathbf{u} + \mu\mathbf{v}, \mathbf{w} \rangle = \lambda\langle \mathbf{u}, \mathbf{w} \rangle + \mu\langle \mathbf{v}, \mathbf{w} \rangle$
3. **正定性**：$\langle \mathbf{v}, \mathbf{v} \rangle \geq 0$，且 $\langle \mathbf{v}, \mathbf{v} \rangle = 0 \iff \mathbf{v} = \mathbf{0}$

### 1.2 标准内积

$\mathbb{R}^n$ 的标准内积（点积）：
$$\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i$$

### 1.3 其他内积

**加权内积**：
$$\langle \mathbf{u}, \mathbf{v} \rangle_W = \mathbf{u}^T W \mathbf{v}$$

其中 $W$ 是正定矩阵。

**函数空间的内积**：
$$\langle f, g \rangle = \int_a^b f(x)g(x) \, dx$$

**多项式空间的内积**：
$$\langle p, q \rangle = \int_{-1}^1 p(x)q(x) \, dx$$

## 2. 范数

### 2.1 由内积诱导的范数

$$\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$$

### 2.2 范数的性质

1. **非负性**：$\|\mathbf{v}\| \geq 0$
2. **齐次性**：$\|\lambda\mathbf{v}\| = |\lambda|\|\mathbf{v}\|$
3. **三角不等式**：$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$
4. **可分性**：$\|\mathbf{u} + \mathbf{v}\| = 0 \implies \mathbf{u} = \mathbf{v} = \mathbf{0}$

### 2.3 距离

由范数定义的距离：
$$d(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\|$$

## 3. 角度与正交

### 3.1 角度的定义

两个非零向量 $\mathbf{u}$ 和 $\mathbf{v}$ 之间的夹角 $\theta$ 定义为：
$$\cos\theta = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{u}\| \|\mathbf{v}\|}$$

其中 $0 \leq \theta \leq \pi$。

### 3.2 正交的定义

$\mathbf{u}$ 和 $\mathbf{v}$ 正交（记作 $\mathbf{u} \perp \mathbf{v}$），如果：
$$\langle \mathbf{u}, \mathbf{v} \rangle = 0$$

### 3.3 勾股定理

如果 $\mathbf{u} \perp \mathbf{v}$，则：
$$\|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$$

**推广**：如果 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ 两两正交，则：
$$\|\mathbf{v}_1 + \mathbf{v}_2 + \cdots + \mathbf{v}_n\|^2 = \|\mathbf{v}_1\|^2 + \|\mathbf{v}_2\|^2 + \cdots + \|\mathbf{v}_n\|^2$$

## 4. 格拉姆-施密特正交化

### 4.1 算法

给定线性无关向量组 $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$，构造正交基 $\{\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n\}$：

$$\mathbf{u}_1 = \mathbf{v}_1$$

$$\mathbf{u}_k = \mathbf{v}_k - \sum_{i=1}^{k-1} \frac{\langle \mathbf{v}_k, \mathbf{u}_i \rangle}{\langle \mathbf{u}_i, \mathbf{u}_i \rangle} \mathbf{u}_i, \quad k = 2, 3, \ldots, n$$

### 4.2 标准正交化

进一步归一化：
$$\mathbf{e}_k = \frac{\mathbf{u}_k}{\|\mathbf{u}_k\|}$$

### 4.3 几何解释

每一步都是减去当前向量在之前所有正交向量上的投影。

## 5. 正交投影

### 5.1 投影的定义

向量 $\mathbf{v}$ 在向量 $\mathbf{u}$ 上的投影：
$$\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\langle \mathbf{v}, \mathbf{u} \rangle}{\langle \mathbf{u}, \mathbf{u} \rangle} \mathbf{u}$$

### 5.2 子空间上的投影

向量 $\mathbf{v}$ 在子空间 $W = \text{span}\{\mathbf{w}_1, \mathbf{w}_2, \ldots, \mathbf{w}_k\}$ 上的投影：
$$\text{proj}_W(\mathbf{v}) = \sum_{i=1}^k \frac{\langle \mathbf{v}, \mathbf{w}_i \rangle}{\langle \mathbf{w}_i, \mathbf{w}_i \rangle} \mathbf{w}_i$$

如果是标准正交基，则：
$$\text{proj}_W(\mathbf{v}) = \sum_{i=1}^k \langle \mathbf{v}, \mathbf{e}_i \rangle \mathbf{e}_i$$

## 6. 重要不等式

### 6.1 柯西-施瓦茨不等式

**定理**：对于任意 $\mathbf{u}, \mathbf{v} \in V$：
$$|\langle \mathbf{u}, \mathbf{v} \rangle| \leq \|\mathbf{u}\| \|\mathbf{v}\|$$

等号成立当且仅当 $\mathbf{u}$ 和 $\mathbf{v}$ 线性相关。

### 6.2 三角不等式

**定理**：对于任意 $\mathbf{u}, \mathbf{v} \in V$：
$$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$$

等号成立当且仅当 $\mathbf{u}$ 和 $\mathbf{v}$ 同向（一个为另一个的非负倍数）。

### 6.3 闵可夫斯基不等式

**定理**：$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$（与三角不等式相同）

### 6.4 平行四边形定律

**定理**：对于任意 $\mathbf{u}, \mathbf{v} \in V$：
$$\|\mathbf{u} + \mathbf{v}\|^2 + \|\mathbf{u} - \mathbf{v}\|^2 = 2\|\mathbf{u}\|^2 + 2\|\mathbf{v}\|^2$$

### 6.5 极化恒等式

**定理**：
$$\langle \mathbf{u}, \mathbf{v} \rangle = \frac{1}{4}(\|\mathbf{u} + \mathbf{v}\|^2 - \|\mathbf{u} - \mathbf{v}\|^2)$$

## 7. 正交补

### 7.1 定义

子空间 $W$ 的正交补：
$$W^\perp = \{\mathbf{v} \in V \mid \langle \mathbf{v}, \mathbf{w} \rangle = 0, \forall \mathbf{w} \in W\}$$

### 7.2 性质

1. $W^\perp$ 是子空间
2. $V = W \oplus W^\perp$
3. $(W^\perp)^\perp = W$
4. $\dim(W) + \dim(W^\perp) = \dim(V)$

## 代码示例

### 示例 1：格拉姆-施密特正交化

```python
import numpy as np

def gram_schmidt(vectors, tolerance=1e-10):
    """格拉姆-施密特正交化"""
    vectors = np.array(vectors, dtype=float)
    m, n = vectors.shape

    orthogonal = np.zeros_like(vectors)

    for i in range(n):
        # 从原始向量开始
        orthogonal[:, i] = vectors[:, i].copy()

        # 减去在之前所有正交向量上的投影
        for j in range(i):
            projection = (np.dot(vectors[:, i], orthogonal[:, j]) /
                         np.dot(orthogonal[:, j], orthogonal[:, j])) * orthogonal[:, j]
            orthogonal[:, i] -= projection

        # 如果向量几乎为零，跳过
        if np.linalg.norm(orthogonal[:, i]) < tolerance:
            orthogonal[:, i] = np.zeros(m)

    return orthogonal

def orthonormalize(vectors):
    """标准正交化"""
    orthogonal = gram_schmidt(vectors)

    # 归一化非零向量
    orthonormal = np.zeros_like(orthogonal)
    for i in range(orthogonal.shape[1]):
        norm = np.linalg.norm(orthogonal[:, i])
        if norm > 1e-10:
            orthonormal[:, i] = orthogonal[:, i] / norm

    return orthonormal

# 示例
vectors = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [0, 1, 1]]).T

orthogonal = gram_schmidt(vectors)
orthonormal = orthonormalize(vectors)

print(f"原始向量:\n{vectors}")
print(f"\n正交化后的向量:\n{orthogonal}")
print(f"\n标准正交化后的向量:\n{orthonormal}")

# 验证正交性
print(f"\n验证正交性:")
for i in range(orthonormal.shape[1]):
    for j in range(i+1, orthonormal.shape[1]):
        dot = np.dot(orthonormal[:, i], orthonormal[:, j])
        print(f"<e_{i+1}, e_{j+1}> = {dot:.6f}")

# 验证单位长度
print(f"\n验证单位长度:")
for i in range(orthonormal.shape[1]):
    norm = np.linalg.norm(orthonormal[:, i])
    print(f"||e_{i+1}|| = {norm:.6f}")
```

### 示例 2：计算内积和角度

```python
import numpy as np

def inner_product(u, v):
    """标准内积"""
    return np.dot(u, v)

def angle_between(u, v):
    """计算两个向量之间的夹角"""
    dot = inner_product(u, v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)

    cos_theta = dot / (norm_u * norm_v)
    # 防止数值误差导致 cos_theta 超出 [-1, 1]
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    theta = np.arccos(cos_theta)
    return theta

# 示例
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

dot = inner_product(u, v)
theta = angle_between(u, v)

print(f"向量 u: {u}")
print(f"向量 v: {v}")
print(f"内积: {dot}")
print(f"夹角（弧度）: {theta:.6f}")
print(f"夹角（度数）: {np.degrees(theta):.6f}")

# 验证柯西-施瓦茨不等式
left = abs(dot)
right = np.linalg.norm(u) * np.linalg.norm(v)
print(f"\n柯西-施瓦茨不等式:")
print(f"|<u, v>| = {left:.6f}")
print(f"||u|| · ||v|| = {right:.6f}")
print(f"不等式成立: {left <= right}")
```

### 示例 3：投影计算

```python
import numpy as np

def projection(v, u):
    """计算向量 v 在向量 u 上的投影"""
    return (np.dot(v, u) / np.dot(u, u)) * u

def projection_onto_subspace(v, basis):
    """计算向量 v 在子空间上的投影"""
    # 先正交化
    from scipy.linalg import qr
    Q, _ = qr(basis, mode='economic')
    
    # 投影
    proj = np.zeros_like(v)
    for i in range(Q.shape[1]):
        proj += np.dot(v, Q[:, i]) * Q[:, i]
    
    return proj

# 示例
v = np.array([3, 4, 5])
u = np.array([1, 0, 0])

proj_v_on_u = projection(v, u)
print(f"向量 v: {v}")
print(f"向量 u: {u}")
print(f"v 在 u 上的投影: {proj_v_on_u}")

# 验证分解
orthogonal_component = v - proj_v_on_u
print(f"正交分量: {orthogonal_component}")
print(f"验证正交性: {np.dot(proj_v_on_u, orthogonal_component):.6f}")

# 子空间投影
W_basis = np.array([[1, 0, 0],
                   [0, 1, 0]]).T
proj_v_on_W = projection_onto_subspace(v, W_basis)
print(f"\nv 在子空间 W 上的投影: {proj_v_on_W}")
print(f"验证投影在 W 中: {np.allclose(proj_v_on_W[2], 0)}")
```

### 示例 4：加权内积

```python
import numpy as np

def weighted_inner_product(u, v, W):
    """加权内积"""
    return u.T @ W @ v

def weighted_norm(v, W):
    """由加权内积诱导的范数"""
    return np.sqrt(weighted_inner_product(v, v, W))

# 示例
u = np.array([1, 2])
v = np.array([3, 4])
W = np.array([[2, 0], [0, 1]])  # 对第一个分量权重更大

dot_standard = np.dot(u, v)
dot_weighted = weighted_inner_product(u, v, W)

norm_u_standard = np.linalg.norm(u)
norm_u_weighted = weighted_norm(u, W)

print(f"向量 u: {u}")
print(f"向量 v: {v}")
print(f"权重矩阵 W:\n{W}")
print(f"\n标准内积: {dot_standard}")
print(f"加权内积: {dot_weighted}")
print(f"\n标准范数 ||u||: {norm_u_standard:.6f}")
print(f"加权范数 ||u||_W: {norm_u_weighted:.6f}")

# 验证柯西-施瓦茨不等式（加权）
cos_theta = dot_weighted / (weighted_norm(u, W) * weighted_norm(v, W))
print(f"\n加权角度余弦: {cos_theta:.6f}")
```

### 示例 5：函数空间的内积

```python
import numpy as np
from scipy.integrate import quad

def inner_product_functions(f, g, a=-1, b=1):
    """函数空间 [-1, 1] 上的内积"""
    integrand = lambda x: f(x) * g(x)
    result, _ = quad(integrand, a, b)
    return result

def norm_function(f, a=-1, b=1):
    """函数范数"""
    return np.sqrt(inner_product_functions(f, f, a, b))

def angle_functions(f, g, a=-1, b=1):
    """函数之间的夹角"""
    dot = inner_product_functions(f, g, a, b)
    norm_f = norm_function(f, a, b)
    norm_g = norm_function(g, a, b)

    if norm_f * norm_g == 0:
        return 0

    cos_theta = dot / (norm_f * norm_g)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    theta = np.arccos(cos_theta)

    return theta

# 示例：多项式函数
f = lambda x: x  # 线性函数
g = lambda x: x**2  # 二次函数
h = lambda x: x**3  # 三次函数

dot_fg = inner_product_functions(f, g)
dot_fh = inner_product_functions(f, h)
dot_gh = inner_product_functions(g, h)

theta_fg = angle_functions(f, g)
theta_fh = angle_functions(f, h)
theta_gh = angle_functions(g, h)

print(f"函数内积:")
print(f"<f, g> = {dot_fg:.6f}")
print(f"<f, h> = {dot_fh:.6f}")
print(f"<g, h> = {dot_gh:.6f}")

print(f"\n函数夹角（度数）:")
print(f"f(x) = x 和 g(x) = x²: {np.degrees(theta_fg):.6f}°")
print(f"f(x) = x 和 h(x) = x³: {np.degrees(theta_fh):.6f}°")
print(f"g(x) = x² 和 h(x) = x³: {np.degrees(theta_gh):.6f}°")
```

## 机器学习应用

### 应用 1：余弦相似度

余弦相似度用于比较文本、图像等特征向量。

### 应用 2：注意力机制

注意力机制使用内积计算注意力权重。

### 应用 3：词嵌入

词嵌入通过内积计算词之间的相似度。

```python
import numpy as np

# 简化的词嵌入示例
word_embeddings = {
    'king': np.array([0.9, 0.3, 0.8]),
    'queen': np.array([0.8, 0.2, 0.9]),
    'man': np.array([0.95, 0.4, 0.7]),
    'woman': np.array([0.85, 0.3, 0.8]),
}

def cosine_similarity(u, v):
    """余弦相似度"""
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

# 计算词之间的相似度
words = list(word_embeddings.keys())
for i, word1 in enumerate(words):
    for word2 in words[i+1:]:
        sim = cosine_similarity(word_embeddings[word1], word_embeddings[word2])
        print(f"{word1} - {word2}: {sim:.4f}")

# 词类比
analogy = word_embeddings['king'] - word_embeddings['man'] + word_embeddings['woman']

closest_word = None
max_sim = -1
for word, embedding in word_embeddings.items():
    if word not in ['king', 'man', 'woman']:
        sim = cosine_similarity(analogy, embedding)
        if sim > max_sim:
            max_sim = sim
            closest_word = word

print(f"\n词类比：king - man + woman ≈ {closest_word}")
```

## 严格证明

### 证明 1：柯西-施瓦茨不等式

**定理**：对于任意 $\mathbf{u}, \mathbf{v} \in V$：
$$|\langle \mathbf{u}, \mathbf{v} \rangle| \leq \|\mathbf{u}\| \|\mathbf{v}\|$$

**证明**：

对于任意 $\lambda \in \mathbb{R}$，考虑：
$$\|\mathbf{u} + \lambda\mathbf{v}\|^2 \geq 0$$

展开：
$$\langle \mathbf{u} + \lambda\mathbf{v}, \mathbf{u} + \lambda\mathbf{v} \rangle \geq 0$$

$$\langle \mathbf{u}, \mathbf{u} \rangle + 2\lambda\langle \mathbf{u}, \mathbf{v} \rangle + \lambda^2\langle \mathbf{v}, \mathbf{v} \rangle \geq 0$$

这是关于 $\lambda$ 的二次函数，对所有 $\lambda$ 非负，因此判别式非正：
$$(2\langle \mathbf{u}, \mathbf{v} \rangle)^2 - 4\|\mathbf{u}\|^2 \|\mathbf{v}\|^2 \leq 0$$

即：
$$\langle \mathbf{u}, \mathbf{v} \rangle^2 \leq \|\mathbf{u}\|^2 \|\mathbf{v}\|^2$$

开方得证。

等号成立当且仅当 $\mathbf{u}$ 和 $\mathbf{v}$ 线性相关。

### 证明 2：三角不等式

**定理**：对于任意 $\mathbf{u}, \mathbf{v} \in V$：
$$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$$

**证明**：

$$\|\mathbf{u} + \mathbf{v}\|^2 = \langle \mathbf{u} + \mathbf{v}, \mathbf{u} + \mathbf{v} \rangle$$

$$= \langle \mathbf{u}, \mathbf{u} \rangle + 2\langle \mathbf{u}, \mathbf{v} \rangle + \langle \mathbf{v}, \mathbf{v} \rangle$$

$$= \|\mathbf{u}\|^2 + 2\langle \mathbf{u}, \mathbf{v} \rangle + \|\mathbf{v}\|^2$$

由柯西-施瓦茨不等式：
$$\langle \mathbf{u}, \mathbf{v} \rangle \leq |\langle \mathbf{u}, \mathbf{v} \rangle| \leq \|\mathbf{u}\| \|\mathbf{v}\|$$

因此：
$$\|\mathbf{u} + \mathbf{v}\|^2 \leq \|\mathbf{u}\|^2 + 2\|\mathbf{u}\| \|\mathbf{v}\| + \|\mathbf{v}\|^2 = (\|\mathbf{u}\| + \|\mathbf{v}\|)^2$$

开方得证。

### 证明 3：格拉姆-施密特正交化算法的正确性

**定理**：格拉姆-施密特算法生成的向量组 $\{\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n\}$ 是正交的，且 $\text{span}\{\mathbf{u}_1, \ldots, \mathbf{u}_k\} = \text{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ 对所有 $k$ 成立。

**证明**：

**归纳法**：

**基础情况**：$k = 1$
$\mathbf{u}_1 = \mathbf{v}_1$，显然 $\text{span}\{\mathbf{u}_1\} = \text{span}\{\mathbf{v}_1\}$。

**归纳假设**：假设对 $k-1$ 成立，即 $\{\mathbf{u}_1, \ldots, \mathbf{u}_{k-1}\}$ 正交，且 $\text{span}\{\mathbf{u}_1, \ldots, \mathbf{u}_{k-1}\} = \text{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_{k-1}\}$。

**归纳步骤**：
$$\mathbf{u}_k = \mathbf{v}_k - \sum_{i=1}^{k-1} \frac{\langle \mathbf{v}_k, \mathbf{u}_i \rangle}{\langle \mathbf{u}_i, \mathbf{u}_i \rangle} \mathbf{u}_i$$

1. **正交性**：对于 $j < k$，
$$\langle \mathbf{u}_k, \mathbf{u}_j \rangle = \langle \mathbf{v}_k, \mathbf{u}_j \rangle - \sum_{i=1}^{k-1} \frac{\langle \mathbf{v}_k, \mathbf{u}_i \rangle}{\langle \mathbf{u}_i, \mathbf{u}_i \rangle} \langle \mathbf{u}_i, \mathbf{u}_j \rangle$$

由于 $\{\mathbf{u}_1, \ldots, \mathbf{u}_{k-1}\}$ 正交，$\langle \mathbf{u}_i, \mathbf{u}_j \rangle = 0$（$i \neq j$），所以：
$$\langle \mathbf{u}_k, \mathbf{u}_j \rangle = \langle \mathbf{v}_k, \mathbf{u}_j \rangle - \frac{\langle \mathbf{v}_k, \mathbf{u}_j \rangle}{\langle \mathbf{u}_j, \mathbf{u}_j \rangle} \langle \mathbf{u}_j, \mathbf{u}_j \rangle = 0$$

2. **生成空间**：$\mathbf{u}_k$ 是 $\mathbf{v}_k$ 减去 $\mathbf{v}_k$ 在 $\text{span}\{\mathbf{u}_1, \ldots, \mathbf{u}_{k-1}\} = \text{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_{k-1}\}$ 上的投影，所以 $\mathbf{u}_k \in \text{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$。

反之，$\mathbf{v}_k = \mathbf{u}_k + \sum_{i=1}^{k-1} \frac{\langle \mathbf{v}_k, \mathbf{u}_i \rangle}{\langle \mathbf{u}_i, \mathbf{u}_i \rangle} \mathbf{u}_i \in \text{span}\{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$。

因此 $\text{span}\{\mathbf{u}_1, \ldots, \mathbf{u}_k\} = \text{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$。

## 例题

### 例题 1：计算内积和角度

**问题**：计算 $\mathbf{u} = [1, 2, 3]^T$ 和 $\mathbf{v} = [4, 5, 6]^T$ 的内积和夹角。

**解**：

内积：
$$\langle \mathbf{u}, \mathbf{v} \rangle = 1 \times 4 + 2 \times 5 + 3 \times 6 = 4 + 10 + 18 = 32$$

范数：
$$\|\mathbf{u}\| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14}$$
$$\|\mathbf{v}\| = \sqrt{4^2 + 5^2 + 6^2} = \sqrt{77}$$

夹角：
$$\cos\theta = \frac{32}{\sqrt{14} \times \sqrt{77}} = \frac{32}{\sqrt{1078}}$$

$$\theta = \arccos\left(\frac{32}{\sqrt{1078}}\right) \approx 0.384 \text{ 弧度} \approx 22.0°$$

### 例题 2：格拉姆-施密特正交化

**问题**：将 $\{[1, 1, 0]^T, [1, 0, 1]^T, [0, 1, 1]^T\}$ 正交化。

**解**：

$\mathbf{u}_1 = \mathbf{v}_1 = [1, 1, 0]^T$

$\mathbf{u}_2 = \mathbf{v}_2 - \frac{\langle \mathbf{v}_2, \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1, \mathbf{u}_1 \rangle} \mathbf{u}_1$

计算：
$\langle \mathbf{v}_2, \mathbf{u}_1 \rangle = 1 \times 1 + 0 \times 1 + 1 \times 0 = 1$
$\langle \mathbf{u}_1, \mathbf{u}_1 \rangle = 1^2 + 1^2 + 0^2 = 2$

$\mathbf{u}_2 = [1, 0, 1]^T - \frac{1}{2}[1, 1, 0]^T = [1/2, -1/2, 1]^T$

$\mathbf{u}_3 = \mathbf{v}_3 - \frac{\langle \mathbf{v}_3, \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1, \mathbf{u}_1 \rangle} \mathbf{u}_1 - \frac{\langle \mathbf{v}_3, \mathbf{u}_2 \rangle}{\langle \mathbf{u}_2, \mathbf{u}_2 \rangle} \mathbf{u}_2$

计算：
$\langle \mathbf{v}_3, \mathbf{u}_1 \rangle = 0 \times 1 + 1 \times 1 + 1 \times 0 = 1$
$\langle \mathbf{v}_3, \mathbf{u}_2 \rangle = 0 \times \frac{1}{2} + 1 \times (-\frac{1}{2}) + 1 \times 1 = \frac{1}{2}$
$\langle \mathbf{u}_2, \mathbf{u}_2 \rangle = (\frac{1}{2})^2 + (-\frac{1}{2})^2 + 1^2 = \frac{3}{2}$

$\mathbf{u}_3 = [0, 1, 1]^T - \frac{1}{2}[1, 1, 0]^T - \frac{1/2}{3/2}[1/2, -1/2, 1]^T = [-2/3, 2/3, 2/3]^T$

### 例题 3：投影计算

**问题**：计算 $\mathbf{v} = [3, 4]^T$ 在 $\mathbf{u} = [1, 0]^T$ 上的投影。

**解**：

投影公式：
$$\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\langle \mathbf{v}, \mathbf{u} \rangle}{\langle \mathbf{u}, \mathbf{u} \rangle} \mathbf{u}$$

计算：
$\langle \mathbf{v}, \mathbf{u} \rangle = 3 \times 1 + 4 \times 0 = 3$
$\langle \mathbf{u}, \mathbf{u} \rangle = 1^2 + 0^2 = 1$

$\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{3}{1}[1, 0]^T = [3, 0]^T$

验证正交性：$\mathbf{v} - \text{proj}_{\mathbf{u}}(\mathbf{v}) = [0, 4]^T$，与 $\mathbf{u}$ 的内积为 $0 \times 1 + 4 \times 0 = 0$。

### 例题 4：验证柯西-施瓦茨不等式

**问题**：验证柯西-施瓦茨不等式对于 $\mathbf{u} = [1, 1]^T$ 和 $\mathbf{v} = [1, -1]^T$。

**解**：

左边：$|\langle \mathbf{u}, \mathbf{v} \rangle| = |1 \times 1 + 1 \times (-1)| = 0$

右边：$\|\mathbf{u}\| \|\mathbf{v}\| = \sqrt{1^2 + 1^2} \times \sqrt{1^2 + (-1)^2} = \sqrt{2} \times \sqrt{2} = 2$

$0 \leq 2$，不等式成立。

由于内积为 0，$\mathbf{u}$ 和 $\mathbf{v}$ 正交。

### 例题 5：勾股定理

**问题**：设 $\mathbf{u} = [1, 0]^T$，$\mathbf{v} = [0, 1]^T$，验证勾股定理。

**解**：

验证正交性：$\langle \mathbf{u}, \mathbf{v} \rangle = 1 \times 0 + 0 \times 1 = 0$，所以 $\mathbf{u} \perp \mathbf{v}$。

计算：
$\|\mathbf{u} + \mathbf{v}\|^2 = \|[1, 1]^T\|^2 = 1^2 + 1^2 = 2$
$\|\mathbf{u}\|^2 = 1^2 + 0^2 = 1$
$\|\mathbf{v}\|^2 = 0^2 + 1^2 = 1$

验证：$\|\mathbf{u} + \mathbf{v}\|^2 = 2 = 1 + 1 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$

勾股定理成立。

## 习题

### 基础题

1. 计算 $\mathbf{u} = [1, 2, 3]^T$ 和 $\mathbf{v} = [4, 5, 6]^T$ 的内积和夹角。

2. 验证柯西-施瓦茨不等式对于 $\mathbf{u} = [1, 1]^T$ 和 $\mathbf{v} = [1, -1]^T$。

3. 将 $\{[1, 1]^T, [1, 2]^T\}$ 正交化。

4. 证明：$\|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 + 2\langle \mathbf{u}, \mathbf{v} \rangle$。

5. 证明：勾股定理的逆命题。

### 进阶题

6. 证明：柯西-施瓦茨不等式。

7. 证明：三角不等式 $\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$。

8. 证明：格拉姆-施密特正交化算法的正确性。

9. 证明：平行四边形定律 $\|\mathbf{u} + \mathbf{v}\|^2 + \|\mathbf{u} - \mathbf{v}\|^2 = 2\|\mathbf{u}\|^2 + 2\|\mathbf{v}\|^2$。

10. 证明：极化恒等式 $\langle \mathbf{u}, \mathbf{v} \rangle = \frac{1}{4}(\|\mathbf{u} + \mathbf{v}\|^2 - \|\mathbf{u} - \mathbf{v}\|^2)$。

### 挑战题

11. 研究希尔伯特空间的定义和性质。

12. 证明：有限维内积空间都完备。

13. 在深度学习中，为什么自注意力机制使用内积？

14. 研究核方法与内积空间的关系。

15. 证明：贝塞尔不等式 $\sum_{i=1}^n |\langle \mathbf{v}, \mathbf{e}_i \rangle|^2 \leq \|\mathbf{v}\|^2$，其中 $\{\mathbf{e}_i\}$ 是标准正交基。

## 注意事项

⚠️ **常见错误**

1. **混淆内积和点积**
   - 点积是标准内积
   - 内积可以有多种定义

2. **忽略角度的定义域**
   - 角度 $\theta \in [0, \pi]$
   - $\cos\theta$ 的值必须在 $[-1, 1]$ 之间

3. **错误使用投影公式**
   - 投影是向量，不是标量
   - 要除以的是 $\|\mathbf{u}\|^2$，不是 $\|\mathbf{u}\|$

✅ **最佳实践**

1. **理解几何意义**
   - 内积表示投影
   - 范数表示长度
   - 角度表示方向差异

2. **掌握格拉姆-施密特算法**
   - 每步减去投影
   - 保持线性无关性
   - 可以用于构造标准正交基

3. **应用柯西-施瓦茨不等式**
   - 用于估计
   - 用于证明
   - 用于优化

## 题型总结与思路技巧

### 内积空间核心要点

#### 📋 内积的性质

| 性质 | 公式 |
|-----|------|
| 对称性 | $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$ |
| 线性性 | $\langle a\mathbf{u}+b\mathbf{v}, \mathbf{w} \rangle = a\langle \mathbf{u}, \mathbf{w} \rangle + b\langle \mathbf{v}, \mathbf{w} \rangle$ |
| 正定性 | $\langle \mathbf{v}, \mathbf{v} \rangle \geq 0$，等号当且仅当$\mathbf{v}=\mathbf{0}$ |

### 💡 核心技巧与常用结论

#### 1. 柯西-施瓦茨不等式

$$|\langle \mathbf{u}, \mathbf{v} \rangle| \leq \|\mathbf{u}\| \cdot \|\mathbf{v}\|$$

**应用**：
- 证明向量夹角存在
- 估计内积范围
- 证明三角不等式

#### 2. 正交分解

任意向量$\mathbf{v}$可分解为：
$$\mathbf{v} = \text{proj}_W \mathbf{v} + \text{proj}_{W^\perp} \mathbf{v}$$

**投影公式**：
$$\text{proj}_{\mathbf{u}} \mathbf{v} = \frac{\langle \mathbf{v}, \mathbf{u} \rangle}{\langle \mathbf{u}, \mathbf{u} \rangle} \mathbf{u}$$

#### 3. Gram-Schmidt正交化

**步骤**：
1. $\mathbf{u}_1 = \mathbf{v}_1$
2. $\mathbf{u}_k = \mathbf{v}_k - \sum_{i=1}^{k-1} \frac{\langle \mathbf{v}_k, \mathbf{u}_i \rangle}{\langle \mathbf{u}_i, \mathbf{u}_i \rangle} \mathbf{u}_i$
3. 单位化：$\mathbf{e}_k = \frac{\mathbf{u}_k}{\|\mathbf{u}_k\|}$

#### 4. 正交补

**性质**：
- $(W^\perp)^\perp = W$
- $\dim W + \dim W^\perp = n$
- $\mathbf{v} \in W^\perp \Leftrightarrow \langle \mathbf{v}, \mathbf{w} \rangle = 0, \forall \mathbf{w} \in W$

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 验证内积 | 检验三条性质 | 对称性、线性性、正定性 |
| 求正交投影 | 投影公式 | 减去投影向量 |
| 正交化 | Gram-Schmidt | 逐个正交化 |
| 求正交补 | 解方程组 | 与所有基正交 |
| 证明不等式 | 柯西-施瓦茨 | 内积与范数关系 |

### ⚠️ 常见错误

**错误一**：混淆正交与垂直
- 正交是内积为零
- 垂直是几何概念，正交是代数定义

**错误二**：Gram-Schmidt顺序
- 必须按顺序处理
- 后面的向量要减去前面所有方向的投影

**错误三**：投影公式记忆
- 投影向量 = $\frac{\langle \mathbf{v}, \mathbf{u} \rangle}{\langle \mathbf{u}, \mathbf{u} \rangle} \mathbf{u}$
- 分母是$\mathbf{u}$的范数平方

## 本章小结

### 重要定义
1. 内积：满足对称性、线性性、正定性的二元运算
2. 范数：由内积诱导的长度
3. 正交：内积为零

### 重要定理
1. 柯西-施瓦茨不等式
2. 三角不等式
3. 平行四边形定律
4. 格拉姆-施密特算法的正确性

### 重要方法
1. 格拉姆-施密特正交化
2. 投影计算
3. 角度计算

### 重要应用
1. 余弦相似度
2. 注意力机制
3. 词嵌入
4. 核方法

本章为后续学习正交性、SVD分解等奠定了基础。

## 相关概念

- [[08_Vectors]] - 向量基础
- [[09_Linear_Relations]] - 线性相关性
- [[19_Orthogonality]] - 正交性
- [[21_SVD]] - 奇异值分解

## 参考教材

- 《线性代数》（第6版），同济大学数学系，第四章
- 《Introduction to Linear Algebra》（第5版），Gilbert Strang, Chapter 4
- 《高等代数简明教程》（第2版），北京大学数学系，第六章


