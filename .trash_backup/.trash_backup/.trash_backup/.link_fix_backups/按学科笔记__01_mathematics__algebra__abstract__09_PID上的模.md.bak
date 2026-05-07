---
type: note
subject: abstract_algebra
chapter: 09
created: 2026-04-03
updated: 2026-04-24
status: complete
---

# PID上的模

## 📌 学习目标

- 理解 PID 上有限生成模的结构定理
- 掌握不变因子、初等因子和 Smith 标准形的关系
- 能用模论视角解释有限生成 Abel 群和 Jordan 标准形

## ✅ 先修

- [[08_模的基础理论]]
- [[04_环的定义与理想]]
- [[03_群的结构]]
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层

- **基础**：PID、有限生成模、扭模
- **进阶**：结构定理、不变因子、初等因子
- **拓展**：Smith 标准形、有限 Abel 群、Jordan 对照

## 自测（3问速测）

1. 为什么 PID 上有限生成模可以分解成自由部分和扭部分？
2. 不变因子和初等因子有什么区别？
3. Smith 标准形为什么能读出模结构？

## 一、主理想整环上的模

### 1.1 回顾

**主理想整环（PID）**：每个理想都是主理想的整环。

**例**：$\mathbb{Z}$, $F[x]$, $\mathbb{Z}[i]$

### 1.2 有限生成模

**定义**：模 $M$ 称为**有限生成的**，若存在 $m_1, \ldots, m_n \in M$ 使得
$$M = R m_1 + \cdots + R m_n$$

---

## 二、结构定理

### 2.1 主定理

**定理**：设 $R$ 是PID，$M$ 是有限生成 $R$-模。则
$$M \cong R^r \oplus R/\langle d_1 \rangle \oplus R/\langle d_2 \rangle \oplus \cdots \oplus R/\langle d_k \rangle$$
其中：
- $r \geq 0$ 是 $M$ 的**秩**
- $d_1 \mid d_2 \mid \cdots \mid d_k$，$d_i$ 非零非单位

**唯一性**：$r$ 和 $d_i$（在相伴意义下）由 $M$ 唯一确定。

### 2.2 不变因子

**定义**：$d_1, d_2, \ldots, d_k$ 称为 $M$ 的**不变因子**。

### 2.3 初等因子形式

**定理**：设 $d_k$ 的素因子分解为 $d_k = p_1^{e_{k1}} \cdots p_m^{e_{km}}$，则
$$M \cong R^r \oplus \bigoplus_{i,j} R/\langle p_i^{e_{ij}} \rangle$$

$p_i^{e_{ij}}$ 称为**初等因子**。

---

## 三、应用：有限生成Abel群

### 3.1 结构定理

**定理**：每个有限生成Abel群同构于
$$\mathbb{Z}^r \oplus \mathbb{Z}_{d_1} \oplus \cdots \oplus \mathbb{Z}_{d_k}$$
其中 $d_1 \mid d_2 \mid \cdots \mid d_k$。

### 3.2 例子

**例1**：$\mathbb{Z}_{12} \cong \mathbb{Z}_3 \oplus \mathbb{Z}_4$（初等因子形式）

**例2**：$\mathbb{Z}_{60} \cong \mathbb{Z}_{12} \oplus \mathbb{Z}_5 \cong \mathbb{Z}_3 \oplus \mathbb{Z}_4 \oplus \mathbb{Z}_5 \cong \mathbb{Z}_3 \oplus \mathbb{Z}_{20}$

**例3**：确定 $\mathbb{Z}_{72}$ 的结构：
- $72 = 2^3 \cdot 3^2$
- 初等因子形式：$\mathbb{Z}_8 \oplus \mathbb{Z}_9$ 或 $\mathbb{Z}_2 \oplus \mathbb{Z}_4 \oplus \mathbb{Z}_9$ 等
- 不变因子形式：$\mathbb{Z}_{72}$（因为不变因子必须整除）

---

## 四、应用：线性变换的标准形

### 4.1 模论视角

设 $V$ 是域 $F$ 上的 $n$ 维向量空间，$T: V \to V$ 是线性变换。

**关键观察**：$V$ 可以看作 $F[x]$-模，作用定义为
$$f(x) \cdot v = f(T)(v)$$

### 4.2 结构定理的应用

**定理**：设 $R = F[x]$，$M = V$ 是有限生成 $F[x]$-模，则
$$M \cong F[x]/\langle d_1(x) \rangle \oplus \cdots \oplus F[x]/\langle d_k(x) \rangle$$
其中 $d_1 \mid d_2 \mid \cdots \mid d_k$。

### 4.3 有理标准形

**定理**：$T$ 的**有理标准形**是分块对角矩阵
$$\begin{pmatrix} C(d_1) & & \\ & \ddots & \\ & & C(d_k) \end{pmatrix}$$
其中 $C(d_i)$ 是 $d_i$ 的**伴侣矩阵**：
$$C(d) = \begin{pmatrix} 0 & 0 & \cdots & 0 & -a_0 \\ 1 & 0 & \cdots & 0 & -a_1 \\ 0 & 1 & \cdots & 0 & -a_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & -a_{n-1} \end{pmatrix}$$
若 $d(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0$。

### 4.4 Jordan标准形

设 $d_k(x) = (x - \lambda_1)^{e_1} \cdots (x - \lambda_m)^{e_m}$（在 $\mathbb{C}$ 上分解），则 $V$ 分解为
$$V = \bigoplus_{i,j} V_{ij}$$
其中 $T|_{V_{ij}}$ 的矩阵是Jordan块 $J_{e_j}(\lambda_i)$。

---

## 五、扭模

### 5.1 定义

**定义**：元素 $m \in M$ 称为**扭元素**，若存在非零 $r \in R$ 使 $rm = 0$。

**扭子模**：$\text{Tor}(M) = \{m \in M : \exists r \neq 0, rm = 0\}$

**定义**：模 $M$ 称为**扭模**，若 $M = \text{Tor}(M)$。

### 5.2 分解

**定理**：有限生成模 $M$ 分解为
$$M \cong M_{\text{free}} \oplus M_{\text{tor}}$$
其中 $M_{\text{free}}$ 是自由部分，$M_{\text{tor}}$ 是扭部分。

### 5.3 准素分解

**定理**：设 $R$ 是PID，$M$ 是扭模。设 $p_1, \ldots, p_s$ 是初等因子涉及的素元，则
$$M = M_{p_1} \oplus \cdots \oplus M_{p_s}$$
其中 $M_{p_i} = \{m \in M : p_i^k m = 0 \text{ 对某 } k\}$。

---

## 六、不变因子的计算

### 6.1 矩阵方法

给定矩阵 $A$，计算其Smith标准形：

1. 构造关系矩阵
2. 通过初等变换化为对角形
3. 对角元的适当幂次就是不变因子

### 6.2 例题

**例**：求 $\mathbb{Z}^3$ 由 $(2, 1, 0)$, $(4, 0, 2)$, $(0, 4, 2)$ 生成的子群的结构。

**解**：构造矩阵
$$A = \begin{pmatrix} 2 & 1 & 0 \\ 4 & 0 & 2 \\ 0 & 4 & 2 \end{pmatrix}$$

通过初等变换化为Smith标准形
$$\begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix}$$

故商群 $\mathbb{Z}^3 / H \cong \mathbb{Z}_2 \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_2$。

---

## 七、与线性代数的对照

| 模论概念 | 线性代数对应 |
|----------|--------------|
| $F[x]$-模 $V$ | 向量空间 + 线性变换 $T$ |
| 不变因子 $d_i(x)$ | 特征多项式的因子 |
| 初等因子 $(x-\lambda)^e$ | Jordan块的大小 |
| 扭模 | 有限维表示 |

---

## 重要定理汇总

| 定理 | 内容 |
|------|------|
| 结构定理 | $M \cong R^r \oplus \bigoplus R/\langle d_i \rangle$ |
| 有限生成Abel群 | $\cong \mathbb{Z}^r \oplus \bigoplus \mathbb{Z}_{d_i}$ |
| 有理标准形 | 伴侣矩阵的分块对角 |
| Jordan标准形 | Jordan块的分块对角 |

---

## 相关链接

- [[08_模的基础理论]] - 模的基础概念
- [[16_Jordan_Canonical|Jordan标准形]] - 线性代数视角
- [[03_群的结构]] - 有限Abel群结构定理

## 总结

- PID 上有限生成模的结构定理是模论的核心分类结果之一。
- 不变因子和初等因子给出了同一结构的两种编码方式。
- 该理论把 Abel 群、线性变换和矩阵标准形统一在同一框架里。

## 易错点

- 把自由部分和扭部分混淆。
- 误把不变因子和初等因子当成同一组数据。
- 忽略结构定理适用于有限生成模而不是任意模。
- 在 Smith 标准形中忘记初等变换必须保持等价类。

## 练习（分层）

### A档（基础）

1. 判断一个模是否扭模。
2. 写出一个 PID 上有限生成模的简单分解。
3. 计算一个整数模的自由部分和扭部分。
4. 判断一个矩阵是否可以化为 Smith 标准形。

### B档（进阶）

1. 求一个具体模的不变因子。
2. 用 Smith 标准形计算商模结构。
3. 证明一个有限生成模是直和分解。
4. 比较同一个模的不变因子和初等因子表示。

### C档（挑战）

1. 证明 PID 上有限生成模结构定理。
2. 推导有限 Abel 群分类定理。
3. 说明 Jordan 标准形与初等因子的对应。
4. 分析一个具体矩阵诱导的模结构。

---

**创建时间**：2026年4月3日
**所属模块**：近世代数 → 模论