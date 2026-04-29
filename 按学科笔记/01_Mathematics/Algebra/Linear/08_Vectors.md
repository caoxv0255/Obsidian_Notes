---
type: concept
topic: vectors
category: linear_algebra
difficulty: beginner
prerequisites: []
acm_relevant: false
created: 2026-02-20
updated: 2026-03-11
status: complete
subject: linear_algebra
chapter: 08
---

# 向量空间基础 (Vector Spaces)

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

## 1. 向量空间的定义

### 1.1 域

设 $\mathbb{F}$ 是一个域（通常 $\mathbb{F} = \mathbb{R}$ 或 $\mathbb{F} = \mathbb{C}$）。

### 1.2 向量空间的定义

向量空间 $V$ 是一个集合，配备了两个运算：
- **加法**：$V \times V \to V$，记作 $\mathbf{u} + \mathbf{v}$
- **标量乘法**：$\mathbb{F} \times V \to V$，记作 $\lambda\mathbf{v}$

满足以下公理：

**加法公理：**
1. **封闭性**：$\forall \mathbf{u}, \mathbf{v} \in V, \mathbf{u} + \mathbf{v} \in V$
2. **结合律**：$\forall \mathbf{u}, \mathbf{v}, \mathbf{w} \in V, (\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$
3. **交换律**：$\forall \mathbf{u}, \mathbf{v} \in V, \mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$
4. **零元素**：$\exists \mathbf{0} \in V, \forall \mathbf{v} \in V, \mathbf{v} + \mathbf{0} = \mathbf{v}$
5. **逆元素**：$\forall \mathbf{v} \in V, \exists -\mathbf{v} \in V, \mathbf{v} + (-\mathbf{v}) = \mathbf{0}$

**标量乘法公理：**
6. **封闭性**：$\forall \lambda \in \mathbb{F}, \mathbf{v} \in V, \lambda\mathbf{v} \in V$
7. **结合律**：$\forall \lambda, \mu \in \mathbb{F}, \mathbf{v} \in V, \lambda(\mu\mathbf{v}) = (\lambda\mu)\mathbf{v}$
8. **单位元**：$\forall \mathbf{v} \in V, 1\cdot\mathbf{v} = \mathbf{v}$
9. **分配律**：$\forall \lambda, \mu \in \mathbb{F}, \mathbf{v} \in V, (\lambda + \mu)\mathbf{v} = \lambda\mathbf{v} + \mu\mathbf{v}$
10. **分配律**：$\forall \lambda \in \mathbb{F}, \mathbf{u}, \mathbf{v} \in V, \lambda(\mathbf{u} + \mathbf{v}) = \lambda\mathbf{u} + \lambda\mathbf{v}$

### 1.3 常见的向量空间

1. **$\mathbb{R}^n$**：所有 $n$ 维实向量
2. **$\mathbb{C}^n$**：所有 $n$ 维复向量
3. **多项式空间** $P_n$：次数不超过 $n$ 的所有多项式
4. **连续函数空间** $C[a, b]$：区间 $[a, b]$ 上的所有连续函数
5. **矩阵空间** $M_{m \times n}$：所有 $m \times n$ 矩阵

## 2. 向量的表示

### 2.1 几何表示（箭头观点）

在二维和三维空间中，向量可以表示为从原点出发的箭头：

```
y
│       v = [3, 2]
│       ╱
│      ╱
│     ╱
│    ╱
│   ╱
│  ╱
│ ╱
│╱
└───────── x
```

- **箭头的长度**：向量的范数
- **箭头的方向**：向量的方向
- **箭头的位置**：通常从原点出发

### 2.2 坐标表示（代数观点）

在 $\mathbb{R}^n$ 中，向量表示为有序的 $n$ 元组：
$$\mathbf{v} = [v_1, v_2, \ldots, v_n]^T$$

### 2.3 函数表示（抽象观点）

在函数空间中，向量是一个函数：
$$\mathbf{v}(x) = f(x)$$

## 3. 3Blue1Brown 的三种观点

### 观点 1：向量作为箭头（几何观点）

这种观点对于理解：
- 向量加法：首尾相连
- 标量乘法：伸缩或反转
- 点积：投影

### 观点 2：向量作为数字列表（计算机科学观点）

在编程和机器学习中，向量就是有序的数字列表：

```python
v = [3, 2, 1]  # 三维向量
```

每个数字代表不同的特征或属性。例如：
- 在图像处理中：[R, G, B] 表示颜色
- 在机器学习中：[身高, 体重, 年龄] 表示一个人的特征
- 在自然语言处理中：[词频1, 词频2, ...] 表示文档特征

这种观点对于：
- 数据存储和处理
- 特征工程
- 机器学习算法实现

### 观点 3：向量作为抽象的数学对象（数学观点）

向量是满足特定运算规则的抽象对象。在这个观点中，我们关注的是**向量空间**的公理。

这种观点对于：
- 理论证明
- 推广到抽象空间
- 理解函数空间、多项式空间等

**关键洞察**：在不同的问题中，切换不同的观点会让你更容易理解和解决问题。

## 4. 向量运算

### 4.1 向量加法

$$\mathbf{u} + \mathbf{v} = [u_1 + v_1, u_2 + v_2, \ldots, u_n + v_n]^T$$

**几何意义**：平行四边形法则或三角形法则

### 4.2 标量乘法

$$\lambda\mathbf{v} = [\lambda v_1, \lambda v_2, \ldots, \lambda v_n]^T$$

**几何意义**：伸缩或反转

### 4.3 内积（点积）

对于 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$：

$$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i$$

**几何意义**：$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$，其中 $\theta$ 是两向量的夹角。

### 4.4 向量范数

**L2 范数（欧几里得范数）**：
$$\|\mathbf{v}\|_2 = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}$$

**L1 范数（曼哈顿范数）**：
$$\|\mathbf{v}\|_1 = |v_1| + |v_2| + \cdots + |v_n|$$

**L∞ 范数（最大范数）**：
$$\|\mathbf{v}\|_\infty = \max\{|v_1|, |v_2|, \ldots, |v_n|\}$$

## 代码示例

### 示例 1：基本向量运算

```python
import numpy as np

# 创建向量
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(f"向量 v1: {v1}")
print(f"向量 v2: {v2}")

# 向量加法
v_sum = v1 + v2
print(f"向量加法: {v_sum}")

# 标量乘法
scalar = 2
v_scaled = scalar * v1
print(f"标量乘法 (2 * v1): {v_scaled}")

# 点积
dot_product = np.dot(v1, v2)
print(f"点积: {dot_product}")

# 向量范数
norm_v1_l2 = np.linalg.norm(v1, ord=2)
norm_v1_l1 = np.linalg.norm(v1, ord=1)
norm_v1_inf = np.linalg.norm(v1, ord=np.inf)
print(f"L2 范数: {norm_v1_l2:.6f}")
print(f"L1 范数: {norm_v1_l1:.6f}")
print(f"L∞ 范数: {norm_v1_inf:.6f}")

# 向量夹角
cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
theta = np.arccos(cos_theta)
print(f"向量夹角（弧度）: {theta:.6f}")
print(f"向量夹角（度数）: {np.degrees(theta):.6f}")
```

### 示例 2：向量投影

```python
import numpy as np

def vector_projection(u, v):
    """计算向量 u 在向量 v 上的投影"""
    # proj_v(u) = (u·v / v·v) * v
    return (np.dot(u, v) / np.dot(v, v)) * v

def vector_orthogonal_component(u, v):
    """计算 u 在 v 方向上的正交分量"""
    return u - vector_projection(u, v)

# 示例
u = np.array([3, 4])
v = np.array([5, 0])

proj = vector_projection(u, v)
orth = vector_orthogonal_component(u, v)

print(f"向量 u: {u}")
print(f"向量 v: {v}")
print(f"投影分量: {proj}")
print(f"正交分量: {orth}")

# 验证：u = 投影 + 正交
print(f"验证 u = 投影 + 正交: {np.allclose(u, proj + orth)}")

# 验证：投影与 v 平行，正交与 v 垂直
print(f"投影与 v 平行: {np.allclose(proj[1], 0)}")
print(f"正交与 v 垂直: {np.isclose(np.dot(orth, v), 0)}")
```

### 示例 3：柯西-施瓦茨不等式验证

```python
import numpy as np

def verify_cauchy_schwarz(n_tests=1000, dim=5):
    """验证柯西-施瓦茨不等式"""
    violations = 0
    
    for _ in range(n_tests):
        # 生成两个随机向量
        u = np.random.randn(dim)
        v = np.random.randn(dim)
        
        # 计算不等式两边
        left = np.dot(u, v) ** 2
        right = np.dot(u, u) * np.dot(v, v)
        
        # 验证不等式
        if left > right + 1e-10:
            violations += 1
            print(f"违反：(u·v)² = {left:.6f}, ||u||²·||v||² = {right:.6f}")
    
    print(f"柯西-施瓦茨不等式在 {n_tests} 次测试中违反 {violations} 次")
    return violations == 0

verify_cauchy_schwarz()
```

### 示例 4：三角不等式验证

```python
import numpy as np

def verify_triangle_inequality(n_tests=1000, dim=5):
    """验证三角不等式 ||u + v|| ≤ ||u|| + ||v||"""
    violations = 0
    
    for _ in range(n_tests):
        # 生成两个随机向量
        u = np.random.randn(dim)
        v = np.random.randn(dim)
        
        # 计算不等式两边
        left = np.linalg.norm(u + v)
        right = np.linalg.norm(u) + np.linalg.norm(v)
        
        # 验证不等式
        if left > right + 1e-10:
            violations += 1
            print(f"违反：||u+v|| = {left:.6f}, ||u|| + ||v|| = {right:.6f}")
    
    print(f"三角不等式在 {n_tests} 次测试中违反 {violations} 次")
    return violations == 0

verify_triangle_inequality()
```

## 机器学习应用

### 应用 1：特征向量与数据表示

在机器学习中，数据通常表示为向量：
- 每个样本是一个向量
- 每个特征是向量的一个维度

```python
import numpy as np

# 机器学习中的特征向量
# 假设我们有一个数据集，包含 3 个特征
samples = np.array([
    [5.1, 3.5, 1.4],  # 样本 1
    [4.9, 3.0, 1.4],  # 样本 2
    [4.7, 3.2, 1.3],  # 样本 3
    [4.6, 3.1, 1.5],  # 样本 4
    [5.0, 3.6, 1.4]   # 样本 5
])

print(f"数据集形状: {samples.shape}")
print(f"数据集:\n{samples}")

# 计算特征均值（按列）
feature_means = np.mean(samples, axis=0)
print(f"\n特征均值: {feature_means}")

# 数据标准化（零均值单位方差）
samples_standardized = (samples - feature_means) / np.std(samples, axis=0)
print(f"\n标准化后的数据:\n{samples_standardized}")

# 计算样本间的相似度（使用余弦相似度）
def cosine_similarity(v1, v2):
    """计算余弦相似度"""
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# 计算相似度矩阵
n_samples = len(samples)
similarity_matrix = np.zeros((n_samples, n_samples))
for i in range(n_samples):
    for j in range(n_samples):
        similarity_matrix[i, j] = cosine_similarity(samples_standardized[i], samples_standardized[j])

print(f"\n相似度矩阵:\n{similarity_matrix}")
```

### 应用 2：词嵌入（Word Embeddings）

在自然语言处理中，单词表示为高维向量（词嵌入）。

```python
import numpy as np

# 模拟词嵌入向量
word_embeddings = {
    'king': np.array([0.9, 0.3, 0.8]),
    'queen': np.array([0.8, 0.2, 0.9]),
    'man': np.array([0.95, 0.4, 0.7]),
    'woman': np.array([0.85, 0.3, 0.8]),
}

def cosine_similarity(v1, v2):
    """计算余弦相似度"""
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# 计算词之间的相似度
words = list(word_embeddings.keys())
for i, word1 in enumerate(words):
    for word2 in words[i+1:]:
        similarity = cosine_similarity(word_embeddings[word1], word_embeddings[word2])
        print(f"{word1} - {word2}: {similarity:.4f}")

# 验证词向量运算：king - man + woman ≈ queen
analogy = word_embeddings['king'] - word_embeddings['man'] + word_embeddings['woman']
closest_word = None
closest_similarity = -1

for word, embedding in word_embeddings.items():
    if word not in ['king', 'man', 'woman']:
        similarity = cosine_similarity(analogy, embedding)
        if similarity > closest_similarity:
            closest_similarity = similarity
            closest_word = word

print(f"\n词向量类比：king - man + woman ≈ {closest_word}")
print(f"相似度: {closest_similarity:.4f}")
```

### 应用 3：向量归一化在深度学习中的应用

在深度学习中，经常需要对向量进行归一化以保持数值稳定性。

```python
import numpy as np

def normalize_vector(v, norm_type='l2'):
    """向量归一化"""
    if norm_type == 'l2':
        norm = np.linalg.norm(v, ord=2)
    elif norm_type == 'l1':
        norm = np.linalg.norm(v, ord=1)
    elif norm_type == 'max':
        norm = np.linalg.norm(v, ord=np.inf)
    else:
        raise ValueError(f"未知的范数类型: {norm_type}")
    
    if norm == 0:
        return v
    return v / norm

# 示例：批量归一化（Batch Normalization）
def batch_normalization(batch, epsilon=1e-5):
    """批量归一化"""
    # 计算均值和方差
    mean = np.mean(batch, axis=0)
    variance = np.var(batch, axis=0)
    
    # 归一化
    normalized = (batch - mean) / np.sqrt(variance + epsilon)
    
    return normalized

# 模拟一个批次的数据
batch = np.random.randn(32, 128)  # 32个样本，每个128维
print(f"原始数据均值: {np.mean(batch):.6f}")
print(f"原始数据方差: {np.var(batch):.6f}")

# 应用批量归一化
normalized_batch = batch_normalization(batch)
print(f"归一化后均值: {np.mean(normalized_batch):.6f}")
print(f"归一化后方差: {np.var(normalized_batch):.6f}")
```

## 严格证明

### 证明 1：零向量的唯一性

**定理**：向量空间 $V$ 中的零向量是唯一的。

**证明**：
假设 $\mathbf{0}_1$ 和 $\mathbf{0}_2$ 都是 $V$ 的零向量。

根据零向量的定义：
- $\forall \mathbf{v} \in V, \mathbf{v} + \mathbf{0}_1 = \mathbf{v}$
- $\forall \mathbf{v} \in V, \mathbf{v} + \mathbf{0}_2 = \mathbf{v}$

特别地，取 $\mathbf{v} = \mathbf{0}_2$：
$$\mathbf{0}_2 + \mathbf{0}_1 = \mathbf{0}_2$$

取 $\mathbf{v} = \mathbf{0}_1$：
$$\mathbf{0}_1 + \mathbf{0}_2 = \mathbf{0}_1$$

由交换律：
$$\mathbf{0}_1 + \mathbf{0}_2 = \mathbf{0}_2 + \mathbf{0}_1$$

因此 $\mathbf{0}_1 = \mathbf{0}_2$，零向量唯一。

### 证明 2：逆向量的唯一性

**定理**：对于任意 $\mathbf{v} \in V$，其逆向量 $-\mathbf{v}$ 是唯一的。

**证明**：
假设 $\mathbf{w}_1$ 和 $\mathbf{w}_2$ 都是 $\mathbf{v}$ 的逆向量，即：
$$\mathbf{v} + \mathbf{w}_1 = \mathbf{0}$$
$$\mathbf{v} + \mathbf{w}_2 = \mathbf{0}$$

因此：
$$\mathbf{v} + \mathbf{w}_1 = \mathbf{v} + \mathbf{w}_2$$

两边同时加上 $-\mathbf{v}$：
$$(-\mathbf{v}) + \mathbf{v} + \mathbf{w}_1 = (-\mathbf{v}) + \mathbf{v} + \mathbf{w}_2$$

由结合律和逆向量的定义：
$$\mathbf{0} + \mathbf{w}_1 = \mathbf{0} + \mathbf{w}_2$$

因此 $\mathbf{w}_1 = \mathbf{w}_2$，逆向量唯一。

### 证明 3：柯西-施瓦茨不等式

**定理**：对于任意 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$：
$$|\mathbf{u} \cdot \mathbf{v}| \leq \|\mathbf{u}\| \|\mathbf{v}\|$$

**证明**（使用二次函数判别式）：

对于任意 $\lambda \in \mathbb{R}$，考虑向量 $\mathbf{u} + \lambda\mathbf{v}$ 的范数的平方：
$$\|\mathbf{u} + \lambda\mathbf{v}\|^2 \geq 0$$

展开：
$$(\mathbf{u} + \lambda\mathbf{v}) \cdot (\mathbf{u} + \lambda\mathbf{v}) \geq 0$$

$$\mathbf{u} \cdot \mathbf{u} + 2\lambda(\mathbf{u} \cdot \mathbf{v}) + \lambda^2(\mathbf{v} \cdot \mathbf{v}) \geq 0$$

记 $a = \mathbf{v} \cdot \mathbf{v}$，$b = \mathbf{u} \cdot \mathbf{v}$，$c = \mathbf{u} \cdot \mathbf{u}$，则：
$$a\lambda^2 + 2b\lambda + c \geq 0$$

这是一个关于 $\lambda$ 的二次函数，对于所有 $\lambda$ 都非负，因此其判别式必须非正：
$$(2b)^2 - 4ac \leq 0$$

$$4b^2 - 4ac \leq 0$$

$$b^2 \leq ac$$

即：
$$(\mathbf{u} \cdot \mathbf{v})^2 \leq (\mathbf{u} \cdot \mathbf{u})(\mathbf{v} \cdot \mathbf{v})$$

开方得：
$$|\mathbf{u} \cdot \mathbf{v}| \leq \|\mathbf{u}\| \|\mathbf{v}\|$$

等号成立当且仅当 $\mathbf{u}$ 和 $\mathbf{v}$ 线性相关。

### 证明 4：三角不等式

**定理**：对于任意 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$：
$$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$$

**证明**：

考虑 $\|\mathbf{u} + \mathbf{v}\|^2$：
$$\|\mathbf{u} + \mathbf{v}\|^2 = (\mathbf{u} + \mathbf{v}) \cdot (\mathbf{u} + \mathbf{v})$$

$$= \mathbf{u} \cdot \mathbf{u} + 2\mathbf{u} \cdot \mathbf{v} + \mathbf{v} \cdot \mathbf{v}$$

$$= \|\mathbf{u}\|^2 + 2\mathbf{u} \cdot \mathbf{v} + \|\mathbf{v}\|^2$$

由柯西-施瓦茨不等式：
$$\mathbf{u} \cdot \mathbf{v} \leq |\mathbf{u} \cdot \mathbf{v}| \leq \|\mathbf{u}\| \|\mathbf{v}\|$$

因此：
$$\|\mathbf{u} + \mathbf{v}\|^2 \leq \|\mathbf{u}\|^2 + 2\|\mathbf{u}\| \|\mathbf{v}\| + \|\mathbf{v}\|^2$$

$$= (\|\mathbf{u}\| + \|\mathbf{v}\|)^2$$

开方得：
$$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$$

## 例题

### 例题 1：计算向量的范数和夹角

**问题**：设 $\mathbf{u} = [1, 2, 3]$，$\mathbf{v} = [4, 5, 6]$，求：
1. $\|\mathbf{u}\|$ 和 $\|\mathbf{v}\|$
2. $\mathbf{u} \cdot \mathbf{v}$
3. $\mathbf{u}$ 和 $\mathbf{v}$ 的夹角 $\theta$

**解**：

1. $\|\mathbf{u}\| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14}$
   $\|\mathbf{v}\| = \sqrt{4^2 + 5^2 + 6^2} = \sqrt{77}$

2. $\mathbf{u} \cdot \mathbf{v} = 1 \times 4 + 2 \times 5 + 3 \times 6 = 32$

3. $\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|} = \frac{32}{\sqrt{14} \times \sqrt{77}} = \frac{32}{\sqrt{1078}}$

   $\theta = \arccos\left(\frac{32}{\sqrt{1078}}\right)$

### 例题 2：向量投影

**问题**：设 $\mathbf{u} = [1, 2, 3]$，$\mathbf{v} = [2, 0, 0]$，求 $\mathbf{u}$ 在 $\mathbf{v}$ 上的投影。

**解**：

投影公式：$\text{proj}_{\mathbf{v}}(\mathbf{u}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}} \mathbf{v}$

$\mathbf{u} \cdot \mathbf{v} = 1 \times 2 + 2 \times 0 + 3 \times 0 = 2$

$\mathbf{v} \cdot \mathbf{v} = 2^2 + 0^2 + 0^2 = 4$

$\text{proj}_{\mathbf{v}}(\mathbf{u}) = \frac{2}{4} [2, 0, 0] = [1, 0, 0]$

### 例题 3：验证柯西-施瓦茨不等式

**问题**：验证 $\mathbf{u} = [1, 1]$ 和 $\mathbf{v} = [1, -1]$ 是否满足柯西-施瓦茨不等式。

**解**：

$\mathbf{u} \cdot \mathbf{v} = 1 \times 1 + 1 \times (-1) = 0$

$\|\mathbf{u}\| = \sqrt{1^2 + 1^2} = \sqrt{2}$

$\|\mathbf{v}\| = \sqrt{1^2 + (-1)^2} = \sqrt{2}$

左边：$|\mathbf{u} \cdot \mathbf{v}| = 0$

右边：$\|\mathbf{u}\| \|\mathbf{v}\| = \sqrt{2} \times \sqrt{2} = 2$

$0 \leq 2$，不等式成立。

实际上，由于 $\mathbf{u} \cdot \mathbf{v} = 0$，这两个向量正交。

## 习题

### 基础题

1. 计算向量 $\mathbf{v} = [3, 4]$ 的 L2 范数、L1 范数和 L∞ 范数。

2. 设 $\mathbf{u} = [1, 2, 3]$，$\mathbf{v} = [4, 5, 6]$，求 $\mathbf{u} + \mathbf{v}$ 和 $2\mathbf{u} - 3\mathbf{v}$。

3. 计算向量 $\mathbf{u} = [1, 2, 3]$ 和 $\mathbf{v} = [4, 5, 6]$ 的点积和夹角。

4. 求向量 $\mathbf{u} = [1, 2, 3]$ 在向量 $\mathbf{v} = [1, 0, 0]$ 上的投影。

5. 验证三角不等式：$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$，其中 $\mathbf{u} = [1, 2]$，$\mathbf{v} = [3, 4]$。

### 进阶题

6. 证明：对于任意 $\mathbf{v} \in V$，$0 \cdot \mathbf{v} = \mathbf{0}$。

7. 证明：对于任意 $\mathbf{v} \in V$，$(-1) \cdot \mathbf{v} = -\mathbf{v}$。

8. 设 $\mathbf{u}, \mathbf{v}, \mathbf{w} \in \mathbb{R}^n$，证明：
   $$\|\mathbf{u} - \mathbf{v}\|^2 + \|\mathbf{v} - \mathbf{w}\|^2 + \|\mathbf{w} - \mathbf{u}\|^2 = \frac{1}{2} \|\mathbf{u} - \mathbf{v}\|^2 + \frac{1}{2} \|\mathbf{v} - \mathbf{w}\|^2 + \frac{1}{2} \|\mathbf{w} - \mathbf{u}\|^2$$

9. 证明平行四边形定律：
   $$\|\mathbf{u} + \mathbf{v}\|^2 + \|\mathbf{u} - \mathbf{v}\|^2 = 2\|\mathbf{u}\|^2 + 2\|\mathbf{v}\|^2$$

10. 证明：柯西-施瓦茨不等式中等号成立当且仅当 $\mathbf{u}$ 和 $\mathbf{v}$ 线性相关。

### 挑战题

11. 证明闵可夫斯基不等式（Lp 范数的三角不等式）：
    $$\left(\sum_{i=1}^n |u_i + v_i|^p\right)^{1/p} \leq \left(\sum_{i=1}^n |u_i|^p\right)^{1/p} + \left(\sum_{i=1}^n |v_i|^p\right)^{1/p}$$
    其中 $p \geq 1$。

12. 证明 Hölder 不等式：
    $$\sum_{i=1}^n |u_i v_i| \leq \left(\sum_{i=1}^n |u_i|^p\right)^{1/p} \left(\sum_{i=1}^n |v_i|^q\right)^{1/q}$$
    其中 $\frac{1}{p} + \frac{1}{q} = 1$ 且 $p, q > 1$。

13. 在机器学习中，为什么使用余弦相似度而不是欧几里得距离来比较向量？给出具体例子说明。

14. 证明：对于任意 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$，有：
    $$\|\mathbf{u} + \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 + 2\mathbf{u} \cdot \mathbf{v}$$
    并解释其几何意义。

15. 研究函数空间 $C[0, 1]$（区间 $[0, 1]$ 上的连续函数空间）的向量空间结构，定义合适的内积并验证其满足内积空间的公理。

## 注意事项

⚠️ **常见错误**

1. **混淆向量和矩阵**
   - 向量是 $n \times 1$ 或 $1 \times n$ 的矩阵
   - 矩阵乘法不满足交换律，但向量点积满足交换律

2. **忽略向量空间的公理**
   - 不是所有集合都是向量空间
   - 需要验证所有10条公理

3. **范数和距离的混淆**
   - 范数是向量的"长度"
   - 距离是两个向量之间的"间隔"
   - 距离可以由范数定义：$d(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\|$

✅ **最佳实践**

1. **掌握多种视角**
   - 几何观点：理解直观意义
   - 代数观点：进行计算
   - 抽象观点：进行理论证明

2. **熟练使用不等式**
   - 柯西-施瓦茨不等式是最重要的工具
   - 三角不等式用于估计和证明

3. **理解内积的几何意义**
   - 内积可以计算投影、角度和相似度
   - 在机器学习中用于余弦相似度、相关性等

## 题型总结与思路技巧

### 向量运算核心方法

#### 📋 运算类型

| 运算 | 定义 | 几何意义 |
|-----|------|---------|
| 加法 | 逐元素相加 | 向量合成 |
| 数乘 | 各元素乘标量 | 缩放 |
| 内积 | $\sum a_i b_i$ | 投影、角度 |
| 外积 | 叉乘（3D） | 垂直向量 |

### 💡 核心技巧与常用结论

#### 1. 内积公式

**代数形式**：$\langle \mathbf{a}, \mathbf{b} \rangle = \sum_{i=1}^n a_i b_i$

**几何形式**：$\langle \mathbf{a}, \mathbf{b} \rangle = \|\mathbf{a}\| \|\mathbf{b}\| \cos\theta$

**应用**：
- 求角度：$\cos\theta = \frac{\langle \mathbf{a}, \mathbf{b} \rangle}{\|\mathbf{a}\| \|\mathbf{b}\|}$
- 求投影：$\text{proj}_{\mathbf{b}} \mathbf{a} = \frac{\langle \mathbf{a}, \mathbf{b} \rangle}{\|\mathbf{b}\|^2} \mathbf{b}$
- 判断正交：$\langle \mathbf{a}, \mathbf{b} \rangle = 0$

#### 2. 重要不等式

**柯西-施瓦茨不等式**：
$$|\langle \mathbf{a}, \mathbf{b} \rangle| \leq \|\mathbf{a}\| \|\mathbf{b}\|$$

**三角不等式**：
$$\|\mathbf{a} + \mathbf{b}\| \leq \|\mathbf{a}\| + \|\mathbf{b}\|$$

#### 3. 范数比较

| 范数 | 定义 | 特点 |
|-----|------|------|
| L1 | $\sum |x_i|$ | 稀疏性 |
| L2 | $\sqrt{\sum x_i^2}$ | 欧氏距离 |
| L∞ | $\max |x_i|$ | 一致逼近 |

#### 4. 向量空间判定

验证10条公理：
1. 加法交换律、结合律
2. 零向量存在
3. 负向量存在
4. 数乘结合律
5. 数乘分配律（两个）
6. 1·v = v

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 求内积 | 代数或几何公式 | 选择方便的形式 |
| 求角度 | 内积公式 | 取绝对值 |
| 判断正交 | 内积为0 | 验证$\langle\mathbf{a},\mathbf{b}\rangle=0$ |
| 证明不等式 | 柯西-施瓦茨 | 放缩技巧 |
| 判定向量空间 | 验证10条公理 | 找零向量和负向量 |

### ⚠️ 常见错误

**错误一**：内积与范数混淆
- $\|\mathbf{a}\|^2 = \langle \mathbf{a}, \mathbf{a} \rangle$
- 范数是非负实数

**错误二**：正交向量
- 正交向量夹角为90°
- 零向量与任何向量正交

**错误三**：范数不等式
- L1范数 $\geq$ L2范数（同维度下）

## 本章小结

### 重要定义
1. 向量空间：满足10条公理的集合
2. 向量运算：加法、标量乘法、内积、范数
3. 向量范数：L2、L1、L∞ 范数

### 重要定理
1. 零向量的唯一性
2. 逆向量的唯一性
3. 柯西-施瓦茨不等式
4. 三角不等式
5. 平行四边形定律

### 重要证明
1. 零向量和逆向量的唯一性证明
2. 柯西-施瓦茨不等式的证明（使用二次函数判别式）
3. 三角不等式的证明（使用柯西-施瓦茨不等式）

### 重要应用
1. 机器学习中的特征向量
2. 词嵌入和余弦相似度
3. 批量归一化和数值稳定性

本章为后续学习线性代数奠定了基础。

## 相关概念

- [[02_Linear_Equations]] - 线性方程组
- [[03_Matrix_Basics]] - 矩阵基础
- [[04_Matrix_Operations]] - 矩阵运算
- [[09_Inner_Product]] - 内积空间
- [[00_Python_Index|Python]] - NumPy 向量运算

