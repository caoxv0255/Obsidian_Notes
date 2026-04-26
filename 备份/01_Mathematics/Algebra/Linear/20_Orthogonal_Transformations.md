---
type: concept
topic: orthogonal_transformations
category: linear_algebra
difficulty: advanced
prerequisites:
  - [[19_Orthogonality]]
acm_relevant: false
created: 2026-03-11
updated: 2026-03-11
status: complete
---
# 正交变换与正交矩阵 (Orthogonal Transformations)

## 1. 定义

### 1.1 正交矩阵

$n \times n$ 矩阵 $Q$ 是正交矩阵，如果满足：
$$Q^T Q = Q Q^T = I$$

### 1.2 正交变换

线性变换 $T: \mathbb{R}^n \to \mathbb{R}^n$ 是正交变换，如果其变换矩阵 $Q$ 是正交矩阵。

## 2. 性质

### 2.1 基本性质

1. $Q^{-1} = Q^T$
2. $|\det(Q)| = 1$
3. 正交变换保持向量的长度：$\|Q\mathbf{x}\| = \|\mathbf{x}\|$
4. 正交变换保持向量的夹角：$\langle Q\mathbf{x}, Q\mathbf{y} \rangle = \langle \mathbf{x}, \mathbf{y} \rangle$

### 2.2 几何意义

- 当 $\det(Q) = 1$ 时，表示旋转
- 当 $\det(Q) = -1$ 时，表示反射或旋转+反射

### 2.3 特征值

正交矩阵的特征值 $\lambda$ 满足 $|\lambda| = 1$。

## 3. 常见的正交变换

### 3.1 旋转矩阵

$$R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$

表示在 $\mathbb{R}^2$ 中逆时针旋转 $\theta$ 角度。

### 3.2 反射矩阵

关于直线 $y = x$ 的反射：
$$S = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$

关于原点的反射：
$$S_0 = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$$

### 3.3 Householder变换

$$H = I - 2\frac{\mathbf{v}\mathbf{v}^T}{\mathbf{v}^T\mathbf{v}}$$

用于将向量反射到另一个方向。

## 4. 应用

### 4.1 QR分解

使用Householder变换或Givens旋转实现QR分解。

### 4.2 特征值计算

QR算法用于计算矩阵的特征值。

### 4.3 数值稳定性

正交变换具有良好的数值稳定性。

## 代码示例

### 示例 1：验证正交矩阵

```python
import numpy as np

def is_orthogonal(Q, tolerance=1e-10):
    """检查矩阵是否正交"""
    n = Q.shape[0]
    return np.allclose(Q.T @ Q, np.eye(n), atol=tolerance) and \
           np.allclose(Q @ Q.T, np.eye(n), atol=tolerance)

# 旋转矩阵
theta = np.pi / 4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])

print(f"旋转矩阵 R:\n{R}")
print(f"R 是否正交: {is_orthogonal(R)}")
print(f"R^T R:\n{R.T @ R}")
print(f"|det(R)| = {abs(np.linalg.det(R)):.6f}")

# 反射矩阵
S = np.array([[0, 1],
              [1, 0]])

print(f"\n反射矩阵 S:\n{S}")
print(f"S 是否正交: {is_orthogonal(S)}")
print(f"|det(S)| = {abs(np.linalg.det(S)):.6f}")
```

### 示例 2：Householder变换

```python
import numpy as np

def householder_reflection(v):
    """构造Householder变换矩阵"""
    v = np.array(v, dtype=float)
    n = len(v)
    
    # 构造单位向量 e1
    e1 = np.zeros(n)
    e1[0] = 1
    
    # 计算反射向量
    u = v + np.sign(v[0]) * np.linalg.norm(v) * e1
    u = u / np.linalg.norm(u)
    
    # Householder矩阵
    H = np.eye(n) - 2 * np.outer(u, u)
    
    return H

# 示例：将向量 [1, 2, 3] 反射到第一轴方向
v = np.array([1, 2, 3])
H = householder_reflection(v)

print(f"原向量 v: {v}")
print(f"Householder矩阵 H:\n{H}")
print(f"H 是否正交: {is_orthogonal(H)}")
print(f"Hv: {H @ v}")
print(f"第一轴单位向量: {[np.linalg.norm(v), 0, 0]}")
```

### 示例 3：旋转矩阵的性质

```python
import numpy as np

def rotation_matrix_2d(theta):
    """2D旋转矩阵"""
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

# 测试旋转的性质
theta = np.pi / 3
R = rotation_matrix_2d(theta)

v1 = np.array([1, 0])
v2 = np.array([0, 1])

# 旋转后的向量
v1_rotated = R @ v1
v2_rotated = R @ v2

print(f"旋转角度: {theta} 弧度 = {np.degrees(theta)} 度")
print(f"\n原向量 v1: {v1}, v2: {v2}")
print(f"旋转后 v1': {v1_rotated}, v2': {v2_rotated}")

# 验证长度保持不变
print(f"\n||v1|| = {np.linalg.norm(v1):.6f}, ||v1'|| = {np.linalg.norm(v1_rotated):.6f}")
print(f"||v2|| = {np.linalg.norm(v2):.6f}, ||v2'|| = {np.linalg.norm(v2_rotated):.6f}")

# 验证夹角保持不变（90度）
dot_original = np.dot(v1, v2)
dot_rotated = np.dot(v1_rotated, v2_rotated)
print(f"\n原夹角余弦: {dot_original / (np.linalg.norm(v1) * np.linalg.norm(v2)):.6f}")
print(f"旋转后夹角余弦: {dot_rotated / (np.linalg.norm(v1_rotated) * np.linalg.norm(v2_rotated)):.6f}")
```

### 示例 4：连续旋转

```python
import numpy as np

def rotation_matrix_2d(theta):
    """2D旋转矩阵"""
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

# 连续旋转
theta1 = np.pi / 6
theta2 = np.pi / 4

R1 = rotation_matrix_2d(theta1)
R2 = rotation_matrix_2d(theta2)

# 连续旋转矩阵
R_combined = R2 @ R1

# 直接旋转到总角度
theta_total = theta1 + theta2
R_total = rotation_matrix_2d(theta_total)

print(f"旋转角度 1: {np.degrees(theta1)} 度")
print(f"旋转角度 2: {np.degrees(theta2)} 度")
print(f"总旋转角度: {np.degrees(theta_total)} 度")
print(f"\n连续旋转矩阵:\n{R_combined}")
print(f"\n直接旋转矩阵:\n{R_total}")
print(f"\n是否相等: {np.allclose(R_combined, R_total)}")
```

### 示例 5：3D旋转

```python
import numpy as np

def rotation_x(theta):
    """绕x轴旋转"""
    return np.array([[1, 0, 0],
                     [0, np.cos(theta), -np.sin(theta)],
                     [0, np.sin(theta), np.cos(theta)]])

def rotation_y(theta):
    """绕y轴旋转"""
    return np.array([[np.cos(theta), 0, np.sin(theta)],
                     [0, 1, 0],
                     [-np.sin(theta), 0, np.cos(theta)]])

def rotation_z(theta):
    """绕z轴旋转"""
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0],
                     [0, 0, 1]])

# 测试3D旋转
Rx = rotation_x(np.pi/4)
Ry = rotation_y(np.pi/4)
Rz = rotation_z(np.pi/4)

print(f"Rx 是否正交: {is_orthogonal(Rx)}")
print(f"Ry 是否正交: {is_orthogonal(Ry)}")
print(f"Rz 是否正交: {is_orthogonal(Rz)}")

# 复合旋转
R = Rz @ Ry @ Rx
print(f"\n复合旋转矩阵:\n{R}")
print(f"复合旋转是否正交: {is_orthogonal(R)}")
```

## 机器学习应用

### 应用 1：图像旋转

使用正交矩阵进行图像旋转，不改变图像的像素值。

### 应用 2：数据预处理

使用旋转矩阵对数据进行预处理，保持数据分布的形状。

### 应用 3：PCA

PCA中的主成分变换涉及正交变换。

```python
import numpy as np
from sklearn.decomposition import PCA

# 生成数据
np.random.seed(42)
X = np.random.randn(100, 2) @ np.array([[2, 0.5], [0.5, 1]])

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print(f"PCA变换矩阵（主成分）:\n{pca.components_.T}")
print(f"变换矩阵是否正交: {is_orthogonal(pca.components_.T)}")
print(f"解释方差比: {pca.explained_variance_ratio_}")
```

## 严格证明

### 证明：正交变换保持长度

**定理**：如果 $Q$ 是正交矩阵，则 $\|Q\mathbf{x}\| = \|\mathbf{x}\|$ 对所有 $\mathbf{x}$ 成立。

**证明**：

$$\|Q\mathbf{x}\|^2 = (Q\mathbf{x})^T (Q\mathbf{x}) = \mathbf{x}^T Q^T Q \mathbf{x} = \mathbf{x}^T I \mathbf{x} = \mathbf{x}^T \mathbf{x} = \|\mathbf{x}\|^2$$

因此 $\|Q\mathbf{x}\| = \|\mathbf{x}\|$。

### 证明：正交变换保持夹角

**定理**：如果 $Q$ 是正交矩阵，则 $\langle Q\mathbf{x}, Q\mathbf{y} \rangle = \langle \mathbf{x}, \mathbf{y} \rangle$。

**证明**：

$$\langle Q\mathbf{x}, Q\mathbf{y} \rangle = (Q\mathbf{x})^T (Q\mathbf{y}) = \mathbf{x}^T Q^T Q \mathbf{y} = \mathbf{x}^T I \mathbf{y} = \mathbf{x}^T \mathbf{y} = \langle \mathbf{x}, \mathbf{y} \rangle$$

## 例题

### 例题 1：验证旋转矩阵的正交性

**问题**：验证 $R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ 是正交矩阵。

**解**：

计算 $R^T R$：
$$R^T R = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$

$$= \begin{bmatrix} \cos^2\theta + \sin^2\theta & -\cos\theta\sin\theta + \sin\theta\cos\theta \\ -\sin\theta\cos\theta + \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta \end{bmatrix}$$

$$= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$$

因此 $R(\theta)$ 是正交矩阵。

### 例题 2：构造反射矩阵

**问题**：构造关于直线 $y = 2x$ 的反射矩阵。

**解**：

直线的方向向量为 $\mathbf{v} = [1, 2]^T$，单位化为 $\mathbf{u} = \frac{1}{\sqrt{5}}[1, 2]^T$。

反射矩阵为：
$$H = 2\mathbf{u}\mathbf{u}^T - I = 2 \cdot \frac{1}{5}\begin{bmatrix} 1 \\ 2 \end{bmatrix}[1, 2] - I$$

$$= \frac{2}{5}\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} - \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} -3/5 & 4/5 \\ 4/5 & 3/5 \end{bmatrix}$$

### 例题 3：正交矩阵的特征值

**问题**：求正交矩阵 $Q = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ 的特征值。

**解**：

特征方程：$|Q - \lambda I| = \begin{vmatrix} -\lambda & -1 \\ 1 & -\lambda \end{vmatrix} = \lambda^2 + 1 = 0$

解得 $\lambda = \pm i$，满足 $|\lambda| = 1$。

### 例题 4：连续旋转

**问题**：计算 $R(\pi/6) R(\pi/4)$。

**解**：

$$R(\pi/6) R(\pi/4) = \begin{bmatrix} \cos\frac{\pi}{6} & -\sin\frac{\pi}{6} \\ \sin\frac{\pi}{6} & \cos\frac{\pi}{6} \end{bmatrix} \begin{bmatrix} \cos\frac{\pi}{4} & -\sin\frac{\pi}{4} \\ \sin\frac{\pi}{4} & \cos\frac{\pi}{4} \end{bmatrix}$$

$$= \begin{bmatrix} \frac{\sqrt{3}}{2} & -\frac{1}{2} \\ \frac{1}{2} & \frac{\sqrt{3}}{2} \end{bmatrix} \begin{bmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{bmatrix}$$

$$= \begin{bmatrix} \frac{\sqrt{6} - \sqrt{2}}{4} & -\frac{\sqrt{6} + \sqrt{2}}{4} \\ \frac{\sqrt{6} + \sqrt{2}}{4} & \frac{\sqrt{6} - \sqrt{2}}{4} \end{bmatrix} = R(5\pi/12)$$

这验证了 $R(\theta_1) R(\theta_2) = R(\theta_1 + \theta_2)$。

### 例题 5：Householder变换的应用

**问题**：用Householder变换将 $\mathbf{v} = [3, 4]^T$ 变换到第一轴。

**解**：

计算 $\|\mathbf{v}\| = 5$。

构造 $\mathbf{u} = \frac{\mathbf{v} + 5\mathbf{e}_1}{\|\mathbf{v} + 5\mathbf{e}_1\|} = \frac{[8, 4]^T}{\sqrt{80}} = \frac{1}{2\sqrt{5}}[8, 4]^T = \frac{2}{\sqrt{5}}[2, 1]^T$

Householder矩阵：
$$H = I - 2\mathbf{u}\mathbf{u}^T = I - \frac{8}{5}\begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} -\frac{27}{5} & -\frac{16}{5} \\ -\frac{16}{5} & -\frac{3}{5} \end{bmatrix}$$

验证：$H\mathbf{v} = \begin{bmatrix} -\frac{27}{5} & -\frac{16}{5} \\ -\frac{16}{5} & -\frac{3}{5} \end{bmatrix}\begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} -25 \\ 0 \end{bmatrix}$

成功将 $\mathbf{v}$ 变换到第一轴方向（负方向）。

## 习题

### 基础题

1. 验证 $Q = \begin{bmatrix} 1/\sqrt{2} & -1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{bmatrix}$ 是正交矩阵。

2. 证明：正交矩阵的行列式为 $\pm 1$。

3. 构造绕y轴旋转 $\pi/3$ 的3D旋转矩阵。

4. 验证Householder变换 $H = I - 2\frac{\mathbf{v}\mathbf{v}^T}{\mathbf{v}^T\mathbf{v}}$ 是正交矩阵。

5. 求正交矩阵 $Q = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ 的特征值。

### 进阶题

6. 证明：正交变换保持向量的长度和夹角。

7. 证明：两个正交矩阵的乘积仍然是正交矩阵。

8. 证明：正交矩阵的特征值模长为1。

9. 证明：$R(\theta_1) R(\theta_2) = R(\theta_1 + \theta_2)$。

10. 构造关于平面 $x + y + z = 0$ 的反射矩阵。

### 挑战题

11. 研究Givens旋转及其在稀疏矩阵中的应用。

12. 证明：任何正交矩阵都可以分解为Householder变换的乘积。

13. 在计算机图形学中，为什么使用四元数而不是旋转矩阵？

14. 研究快速旋转算法（CORDIC算法）。

15. 证明：正交矩阵的实特征值只能是 $1$ 或 $-1$。

## 注意事项

⚠️ **常见错误**

1. **混淆旋转和反射**
   - 旋转的行列式为 $1$
   - 反射的行列式为 $-1$

2. **忽略角度的方向**
   - 逆时针旋转为正
   - 顺时针旋转为负

3. **错误构造Householder变换**
   - 要归一化反射向量
   - 注意方向的选择

✅ **最佳实践**

1. **利用正交性**
   - 正交变换保持几何性质
   - 数值稳定性好

2. **掌握基本变换**
   - 旋转矩阵
   - 反射矩阵
   - Householder变换

3. **应用QR分解**
   - 用于数值计算
   - 用于特征值算法

## 题型总结与思路技巧

### 正交变换核心要点

#### 📋 常见正交变换

| 变换类型 | 矩阵形式 | 特点 |
|---------|---------|------|
| **旋转** | $\begin{bmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{bmatrix}$ | $\det = 1$，保持定向 |
| **反射** | $\begin{bmatrix}1 & 0 \\ 0 & -1\end{bmatrix}$ | $\det = -1$，改变定向 |
| **Householder** | $H = I - 2\mathbf{u}\mathbf{u}^T$ | 反射变换 |
| **Givens** | 特殊旋转矩阵 | 消去特定元素 |

### 💡 核心技巧与常用结论

#### 1. 正交矩阵的判定

**充要条件**（任选其一）：
- $Q^T Q = I$
- $Q^{-1} = Q^T$
- 列向量（或行向量）标准正交

#### 2. 正交矩阵的性质

- $\det Q = \pm 1$
- 特征值 $|\lambda| = 1$
- 保持内积、长度、角度
- $(AB)^T = B^T A^T$，正交矩阵乘积仍正交

#### 3. QR分解

**定理**：任何$m \times n$矩阵$A$（$m \geq n$）可分解为$A = QR$
- $Q$：$m \times n$正交矩阵（$Q^T Q = I_n$）
- $R$：$n \times n$上三角矩阵

**应用**：
- 最小二乘问题
- 特征值计算（QR算法）
- 线性方程组求解

#### 4. Householder变换

**公式**：$H = I - 2\frac{\mathbf{v}\mathbf{v}^T}{\mathbf{v}^T\mathbf{v}}$

**用途**：将向量反射到另一个方向，用于QR分解

### 🎯 题型分类与对策

| 题型 | 方法 | 关键点 |
|-----|------|-------|
| 判定正交矩阵 | 验证$Q^T Q = I$ | 列向量标准正交 |
| 求QR分解 | Gram-Schmidt或Householder | 两种方法 |
| 构造反射矩阵 | Householder公式 | 目标向量 |
| 构造旋转矩阵 | 角度参数化 | 确定旋转角 |

### ⚠️ 常见错误

**错误一**：混淆旋转与反射
- 旋转：$\det = 1$，保持定向
- 反射：$\det = -1$，改变定向

**错误二**：QR分解的条件
- 要求$m \geq n$（列满秩更好）
- $Q$不一定是方阵

**错误三**：Householder方向
- Householder是反射，不是旋转
- 会改变定向

## 本章小结

### 重要定义
1. 正交矩阵：$Q^T Q = I$
2. 正交变换：变换矩阵为正交矩阵的线性变换

### 重要定理
1. 正交变换保持长度和夹角
2. 正交矩阵的特征值模长为1
3. 正交矩阵的行列式为 $\pm 1$

### 重要方法
1. 旋转矩阵
2. 反射矩阵
3. Householder变换

### 重要应用
1. QR分解
2. 特征值计算
3. 图像变换
4. PCA

## 相关概念

- [[19_Orthogonality]] - 正交性
- [[21_SVD]] - 奇异值分解
- [[23_Linear_Maps]] - 线性映射

## 参考教材

- 《线性代数》（第6版），同济大学数学系，第五章
- 《Introduction to Linear Algebra》（第5版），Gilbert Strang, Chapter 4

