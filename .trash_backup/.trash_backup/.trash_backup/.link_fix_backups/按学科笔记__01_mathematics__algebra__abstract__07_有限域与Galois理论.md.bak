---
type: note
subject: abstract_algebra
chapter: 07
created: 2026-04-03
updated: 2026-04-25
status: complete
---

# 有限域与Galois理论

## 📌 学习目标

- 理解有限域的存在唯一性与基本构造
- 掌握 Galois 群、分裂域与可解性判据的联系
- 能用 Galois 理论分析方程可解性和尺规作图问题

## ✅ 先修

- [[06_域扩张]]
- [[05_整环域与多项式环]]
- [[03_群的结构]]
- [[../00_Symbols_Conventions|符号与约定总表]]

## 难度分层

- **基础**：有限域、Galois 群、分裂域
- **进阶**：Galois 基本定理、可解性判据
- **拓展**：Abel-Ruffini、尺规作图、古典作图问题

## 自测（3问速测）

1. 为什么有限域的阶必须是素数幂？
2. Galois 群与根的对称性有什么关系？
3. 为什么五次一般方程不能用根式求解？

## 一、有限域

### 1.1 存在性与唯一性

**定理**：
1. 有限域的阶是素数幂 $p^n$
2. 对每个素数幂 $p^n$，存在唯一（同构意义下）的 $p^n$ 阶有限域，记为 $\mathbb{F}_{p^n}$ 或 $GF(p^n)$

### 1.2 构造

**方法**：$\mathbb{F}_{p^n} \cong \mathbb{F}_p[x]/\langle f \rangle$，其中 $f$ 是 $\mathbb{F}_p[x]$ 中 $n$ 次不可约多项式。

**例**：$\mathbb{F}_4 \cong \mathbb{F}_2[x]/\langle x^2 + x + 1 \rangle$

元素：$0, 1, \alpha, \alpha + 1$，其中 $\alpha^2 = \alpha + 1$。

**完整例题：构造 $\mathbb{F}_4$ 并看 Frobenius 作用**

在 $\mathbb{F}_2[x]$ 中取不可约多项式 $x^2 + x + 1$。令
$$\mathbb{F}_4 = \mathbb{F}_2[x]/\langle x^2 + x + 1 \rangle$$
并记 $\alpha$ 为 $x$ 的剩余类，则有
$$\alpha^2 = \alpha + 1$$

因此所有元素只有四个：
$$0, 1, \alpha, \alpha+1$$

再看 Frobenius 映射 $\varphi(x) = x^2$：
$$\varphi(0)=0, \quad \varphi(1)=1$$
$$\varphi(\alpha) = \alpha^2 = \alpha + 1$$
$$\varphi(\alpha+1) = (\alpha+1)^2 = \alpha^2 + 1 = (\alpha+1)+1 = \alpha$$

所以 Frobenius 在 $\alpha$ 与 $\alpha+1$ 之间交换，它生成的 Galois 群是
$$\text{Gal}(\mathbb{F}_4/\mathbb{F}_2) \cong \mathbb{Z}_2$$

**直观理解**：有限域不是“很多元素的随便集合”，而是可被一个不可约多项式精确构造出来；Frobenius 映射则把域内元素按 $p$ 次幂重新排列，体现了它的自同构结构。

### 1.3 乘法群

**定理**：$\mathbb{F}_{p^n}^*$ 是 $p^n - 1$ 阶循环群。

**证明**：有限域的乘法群是有限Abel群，由有限Abel群的结构定理，若不是循环群，则存在元素满足 $x^d = 1$ 的解多于 $d$ 个，但多项式 $x^d - 1$ 至多有 $d$ 个根。

### 1.4 子域结构

**定理**：$\mathbb{F}_{p^m}$ 是 $\mathbb{F}_{p^n}$ 的子域当且仅当 $m \mid n$。

**子域链**：$\mathbb{F}_p \subseteq \mathbb{F}_{p^m} \subseteq \mathbb{F}_{p^n}$（$m \mid n$）

---

## 二、Frobenius映射

### 2.1 定义

**定义**：**Frobenius映射** $\varphi: \mathbb{F}_{p^n} \to \mathbb{F}_{p^n}$ 定义为
$$\varphi(x) = x^p$$

### 2.2 性质

**定理**：Frobenius映射是域自同构。

**证明**：
- $\varphi(x + y) = (x + y)^p = x^p + y^p = \varphi(x) + \varphi(y)$（特征 $p$）
- $\varphi(xy) = (xy)^p = x^p y^p = \varphi(x)\varphi(y)$
- 单射：$x^p = 0 \Rightarrow x = 0$，有限域上单射即双射

### 2.3 生成Galois群

**定理**：$\text{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p) = \langle \varphi \rangle$，是 $n$ 阶循环群。

---

## 三、Galois群

### 3.1 定义

**定义**：域扩张 $K/F$ 的**Galois群**是所有 $F$-自同构构成的群：
$$\text{Gal}(K/F) = \{\sigma : K \to K \mid \sigma \text{ 是域同构，}\sigma|_F = \text{id}\}$$

### 3.2 基本例子

**例1**：$\text{Gal}(\mathbb{C}/\mathbb{R}) = \{\text{id}, \text{共轭}\} \cong \mathbb{Z}_2$

**例2**：$\text{Gal}(\mathbb{Q}(\sqrt{2})/\mathbb{Q}) = \{\text{id}, \sigma\}$，其中 $\sigma(a + b\sqrt{2}) = a - b\sqrt{2}$

### 3.3 Galois扩张

**定义**：扩张 $K/F$ 称为**Galois扩张**，若 $|\text{Gal}(K/F)| = [K : F]$。

**等价条件**：
- 正规且可分
- $F$ 是 $\text{Gal}(K/F)$ 的不动域

---

## 四、Galois基本定理

### 4.1 定理陈述

**定理**：设 $K/F$ 是有限Galois扩张，$G = \text{Gal}(K/F)$。则存在双射：

$$\{\text{中间域 } E : F \subseteq E \subseteq K\} \longleftrightarrow \{\text{子群 } H \leq G\}$$

$$E \mapsto \text{Gal}(K/E)$$
$$K^H \leftarrow H$$

其中 $K^H = \{x \in K : \sigma(x) = x, \forall \sigma \in H\}$ 是 $H$ 的不动域。

### 4.2 性质

1. **反序对应**：$E_1 \subseteq E_2 \Leftrightarrow \text{Gal}(K/E_1) \supseteq \text{Gal}(K/E_2)$

2. **维数关系**：$[K : E] = |\text{Gal}(K/E)|$，$[E : F] = [G : \text{Gal}(K/E)]$

3. **正规性**：$E/F$ 正规 $\Leftrightarrow$ $\text{Gal}(K/E) \trianglelefteq G$
   此时 $\text{Gal}(E/F) \cong G/\text{Gal}(K/E)$

### 4.3 图示

```
          K ←→ {e}
         / \
        E   ←→ H
       /     \
      F       ←→ G
```

---

## 五、方程的可解性

### 5.1 多项式的Galois群

**定义**：多项式 $f \in F[x]$ 的**Galois群**是其分裂域在 $F$ 上的Galois群。

### 5.2 根的对称性

**定理**：Galois群同构于根集上的置换群的子群。

**例**：一般三次方程 $x^3 + ax + b = 0$ 的Galois群是 $S_3$。

### 5.3 可解性判据

**定理**：多项式方程可用根式求解当且仅当其Galois群是可解群。

### 5.4 Abel-Ruffini定理

**定理**：五次及以上一般方程不能用根式求解。

**证明**：一般 $n$ 次方程的Galois群是 $S_n$，$S_n$（$n \geq 5$）不可解。

---

## 六、具体例子

### 6.1 三次方程

设 $f(x) = x^3 + ax + b$，判别式 $\Delta = -4a^3 - 27b^2$。

- 若 $\Delta > 0$：三个实根，Galois群 $\cong A_3 \cong \mathbb{Z}_3$
- 若 $\Delta < 0$：一个实根两个复根，Galois群 $\cong S_3$

### 6.2 四次方程

一般四次方程的Galois群是 $S_4$，可解（$S_4$ 有正规列 $S_4 \triangleright A_4 \triangleright V_4 \triangleright \{e\}$）。

### 6.3 五次方程的不可解性

**例**：$f(x) = x^5 - x - 1$ 的Galois群是 $S_5$，不可解。

---

## 七、应用

### 7.1 尺规作图

**定理**：正 $n$ 边形可尺规作图当且仅当 $n = 2^k p_1 \cdots p_r$，其中 $p_i$ 是不同的Fermat素数。

**Fermat素数**：形如 $2^{2^m} + 1$ 的素数。已知的：$3, 5, 17, 257, 65537$。

### 7.2 古希腊三大难题

1. **化圆为方**：不可（$\pi$ 超越）
2. **倍立方体**：不可（$\sqrt[3]{2}$ 次数不是2的幂）
3. **三等分角**：一般不可（需要 $\cos(20°)$，次数为3）

---

## 重要定理汇总

| 定理 | 内容 |
|------|------|
| 有限域唯一性 | $\mathbb{F}_{p^n}$ 存在且唯一 |
| Galois基本定理 | 子域↔子群双射 |
| 可解性判据 | 根式可解 $\Leftrightarrow$ Galois群可解 |
| Abel-Ruffini | 五次方程一般不可根式解 |

---

## 总结

- 有限域由素数幂阶唯一刻画，是现代有限代数结构的基本对象。
- Galois 理论把域扩张、群作用和多项式可解性统一起来。
- Abel-Ruffini 定理说明了高次一般方程不存在根式解。

## 易错点

- 把有限域的阶误写成任意整数。
- 混淆分裂域与任意扩域。
- 把 Galois 群看成“所有置换”，而不是作用在根上的特定子群。
- 忘记“可解群”是根式可解性的判据。

## 练习（分层）

### A档（基础）

1. 构造一个 $\mathbb{F}_{p^n}$ 的例子。
2. 判断一个多项式是否在有限域上可分解。
3. 写出一个多项式的分裂域。
4. 说明有限域乘法群的阶。

### B档（进阶）

1. 计算一个具体有限域的元素运算。
2. 求一个多项式的 Galois 群的可能结构。
3. 用 Galois 基本定理分析子域与子群对应。
4. 判断一个方程是否可用根式求解。

### C档（挑战）

1. 证明有限域的存在唯一性。
2. 证明 Galois 基本定理。
3. 用群论证明 Abel-Ruffini 定理的思路。
4. 分析一个尺规作图问题的域扩张结构。

## 相关链接

- [[03_群的结构]] - 可解群、单群
- [[06_域扩张]] - 分裂域、正规扩张
- [[01_群的定义与基本性质]] - 群论基础

---

**创建时间**：2026年4月3日
**所属模块**：近世代数 → 域论
