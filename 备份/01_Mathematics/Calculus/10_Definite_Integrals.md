---
type: concept

topic: definite_integrals

category: calculus

difficulty: intermediate

prerequisites:
    - [[03_Continuity]]
    - [[05_Derivatives]]
    - [[09_Indefinite_Integrals]]

acm_relevant: false

created: 2026-02-20

status: complete

subject: calculus
chapter: 10
updated: 2026-04-27
---

# 定积分 (Definite Integrals)

## 📌 学习目标

1. ✅ **掌握定积分的定义及其性质**
2. ✅ **理解积分上限函数，熟练掌握积分上限函数的导数**
3. ✅ **理解并掌握原函数存在定理**
4. ✅ **熟练掌握牛顿－莱布尼茨公式**
5. ✅ **熟练掌握定积分的换元积分公式及分部积分公式**
6. ✅ **理解元素法，会用元素法计算平面图形面积、平行截面面积为已知的立体的体积、旋转体的体积**

> 注：✅ 高亮条目为重点掌握内容

## 难度分层

- **基础**：定积分定义（黎曼和）、基本性质、牛顿-莱布尼茨公式与常见计算
- **进阶**：达布和、可积判别与关键证明（为什么可积/为什么等式成立）
- **拓展**：数值积分与“累积量”建模（物理/统计/机器学习）

## ✅ 先修

- [[03_Continuity]]
- [[05_Derivatives]]
- [[09_Indefinite_Integrals]]
- [[../00_Symbols_Conventions|符号与约定总表]]

---

## 1. 定义

### 1.1 定积分的定义（黎曼积分）

函数 $f(x)$ 在区间 $[a, b]$ 上的定积分定义
为黎曼和的极限：
$$\int_a^b f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*) \cdot \Delta x$$

其中：
- $\Delta x = \frac{b-a}{n}$ 是每个子区间的长度
- $x_i^*$ 是第 $i$ 个子区间 $[x_{i-1}, x_i]$ 中的任意点
- 极限的存在性要求 $f$ 在 $[a, b]$ 上可积

**几何意义**：表示曲线 $y = f(x)$ 与 $x$ 轴在区间 $[a, b]$ 之间围成的有向面积。
- $f(x) > 0$ 时面积为正
- $f(x) < 0$ 时面积为负
- 曲线上方和下方的面积相互抵消

### 1.2 黎曼和的定义

对于区间 $[a, b]$ 的划分 $P = \{x_0, x_1, \ldots, x_n\}$，其中 $a = x_0 < x_1 < \ldots < x_n = b$，黎曼和定义为：
$$R(f, P) = \sum_{i=1}^n f(\xi_i) \cdot (x_i - x_{i-1})$$

其中 $\xi_i \in [x_{i-1}, x_i]$ 是任意选取的点。

### 1.3 黎曼积分的可积条件

#### 达布和（Darboux Sums）

设 $f$ 在 $[a, b]$ 上有界，对区间 $[a, b]$ 作划分 $P = \{x_0, x_1, \ldots, x_n\}$，其中 $a = x_0 < x_1 < \ldots < x_n = b$。

- **达布下和**（小和）：$L(f, P) = \sum_{i=1}^n m_i \Delta x_i$，其中 $m_i = \inf_{x \in [x_{i-1}, x_i]} f(x)$
- **达布上和**（大和）：$U(f, P) = \sum_{i=1}^n M_i \Delta x_i$，其中 $M_i = \sup_{x \in [x_{i-1}, x_i]} f(x)$

**性质**：
1. 同一划分下，$L(f, P) \leq U(f, P)$
2. 细化划分不降低下和、不提高上和
3. 下和的上确界称为**下积分**：$\underline{\int_a^b} f(x) dx$
4. 上和的下确界称为**上积分**：$\overline{\int_a^b} f(x) dx$

#### Lebesgue定理（可积的充要条件）

函数 $f$ 在 $[a, b]$ 上可积当且仅当：对于任意 $\varepsilon > 0$，存在划分 $P$，使得：
$$U(f, P) - L(f, P) < \varepsilon$$

**等价表述**：$f$ 可积 $\Leftrightarrow$ 上积分等于下积分，即 $\underline{\int_a^b} f = \overline{\int_a^b} f$

#### 可积函数类

函数 $f$ 在 $[a, b]$ 上可积的充分条件：
- $f$ 在 $[a, b]$ 上**连续**
- $f$ 在 $[a, b]$ 上**有界**且只有**有限个间断点**
- $f$ 在 $[a, b]$ 上**单调**（单调函数至多有可数个间断点，故可积）

**必要条件**：如果 $f$ 在 $[a, b]$ 上可积，则 $f$ 在 $[a, b]$ 上**有界**。

### 1.4 定积分的物理意义

- **位移**：速度函数 $v(t)$ 在时间区间 $[a, b]$ 上的定积分 $\int_a^b v(t) dt$ 表示从时刻 $a$ 到 $b$ 的总位移
- **功**：力函数 $F(x)$ 在位移区间 $[a, b]$ 上的定积分 $\int_a^b F(x) dx$ 表示力在该位移上做的功
- **累积量**：定积分表示累积的总量

## 2. 定理

### 2.1 微积分基本定理（第一基本定理）

**定理**：设 $f$ 在 $[a, b]$ 上连续，定义函数 $F(x) = \int_a^x f(t) \, dt$，则 $F$ 在 $[a, b]$ 上可导，且：
$$F'(x) = f(x)$$

**意义**：这个定理建立了定积分与导数之间的联系，说明积分函数的导数等于被积函数。

### 2.2 微积分基本定理（第二基本定理，牛顿-莱布尼茨公式）

**定理**：设 $f$ 在 $[a, b]$ 上*连续*，且 $F$ 是 $f$ 的任意一个原函数（即 $F' = f$），则：
$$\int_a^b f(x) \, dx = F(b) - F(a)$$

**意义**：这个公式提供了计算定积分的基本方法，将定积分的计算转化为求原函数在端点的差值。

### 2.3 积分中值定理

**定理**（积分第一中值定理）：设 $f$ 在 $[a, b]$ 上*连续*，则存在 $c \in [a, b]$，使得：
$$\int_a^b f(x) \, dx = f(c)(b - a)$$

**几何意义**：存在一个高度为 $f(c)$ 的矩形，其面积等于曲线下的面积。

**定理**（积分第二中值定理）：设 $f$ 在 $[a, b]$ 上可积，$g$ 在 $[a, b]$ 上单调：
1. 若 $g$ 单调递增且 $g(a) \geq 0$，则存在 $\xi \in [a, b]$，使得：
$$\int_a^b f(x) g(x) \, dx = g(b) \int_{\xi}^b f(x) \, dx$$

2. 若 $g$ 单调递减且 $g(b) \geq 0$，则存在 $\xi \in [a, b]$，使得：
$$\int_a^b f(x) g(x) \, dx = g(a) \int_a^{\xi} f(x) \, dx$$

**推论**（阿贝尔定理）：若 $f$ 可积，$g$ 单调有界，则 $\int_a^b f(x) g(x) \, dx$ 存在。

### 2.4 积分不等式定理

**定理**：设 $f$ 和 $g$ 在 $[a, b]$ 上可积，且 $f(x) \leq g(x)$ 对所有 $x \in [a, b]$ 成立，则：
$$\int_a^b f(x) \, dx \leq \int_a^b g(x) \, dx$$

特别地，如果 $m \leq f(x) \leq M$ 对所有 $x \in [a, b]$，则：
$$m(b - a) \leq \int_a^b f(x) \, dx \leq M(b - a)$$

### 2.5 积分绝对值不等式

**定理**：设 $f$ 在 $[a, b]$ 上可积，则：
$$\left|\int_a^b f(x) \, dx\right| \leq \int_a^b |f(x)| \, dx$$

### 2.6 原函数存在定理

**定理**（原函数存在定理）：如果函数 $f(x)$ 在区间 $I$ 上连续，则 $f(x)$ 在 $I$ 上必有原函数，即存在可导函数 $F(x)$ 使得 $F'(x) = f(x)$。

**注意**：
1. 连续函数必有原函数（第一基本定理的逆命题部分成立）
2. 但有原函数的函数不一定连续（例如 $f(x) = \begin{cases} 2x\sin\frac{1}{x} - \cos\frac{1}{x} & x \neq 0 \\ 0 & x = 0 \end{cases}$ 的原函数 $F(x) = \begin{cases} x^2\sin\frac{1}{x} & x \neq 0 \\ 0 & x = 0 \end{cases}$ 在 $x=0$ 处可导，但其导函数在 $x=0$ 处不连续）

**不定积分**：函数 $f(x)$ 的全体原函数称为不定积分，记作：
$$\int f(x) \, dx = F(x) + C$$
其中 $F(x)$ 是 $f(x)$ 的一个原函数，$C$ 是任意常数。

---

## 2. 证明

### 2.1 微积分基本定理（第一基本定理）的证明

**证明**：对于 $x \in [a, b]$，考虑：
$$F(x + h) - F(x) = \int_a^{x+h} f(t) \, dt - \int_a^{x} f(t) \, dt = \int_x^{x+h} f(t) \, dt$$

因此：
$$\frac{F(x + h) - F(x)}{h} = \frac{1}{h} \int_x^{x+h} f(t) \, dt$$

由于 $f$ 在 $x$ 处连续，对于任意 $\varepsilon > 0$，存在 $\delta > 0$，使得当 $|t - x| < \delta$ 时，$|f(t) - f(x)| < \varepsilon$。

取 $|h| < \delta$，则对于 $t \in [x, x+h]$（或 $[x+h, x]$），有 $|f(t) - f(x)| < \varepsilon$。

因此：
$$\left|f(x) - \frac{1}{h} \int_x^{x+h} f(t) \, dt\right| = \left|\frac{1}{h} \int_x^{x+h} [f(x) - f(t)] \, dt\right|$$
$$\leq \frac{1}{|h|} \int_x^{x+h} |f(x) - f(t)| \, dt$$
$$< \frac{1}{|h|} \int_x^{x+h} \varepsilon \, dt = \varepsilon$$

令 $h \to 0$，得：
$$\lim_{h \to 0} \frac{F(x + h) - F(x)}{h} = f(x)$$

即 $F'(x) = f(x)$。

### 2.2 牛顿-莱布尼茨公式的证明

**证明**：由第一基本定理，函数 $G(x) = \int_a^x f(t) \, dt$ 满足 $G'(x) = f(x)$。

因此 $G(x)$ 和 $F(x)$ 都是 $f$ 的原函数，故 $G(x) - F(x)$ 是常数。

设 $G(x) - F(x) = C$，则 $G(a) - F(a) = C$。

但 $G(a) = \int_a^a f(t) \, dt = 0$，故 $C = -F(a)$。

因此 $G(x) = F(x) - F(a)$。

特别地：
$$G(b) = \int_a^b f(t) \, dt = F(b) - F(a)$$

### 2.3 积分中值定理的证明

**证明**：设 $f$ 在 $[a, b]$ 上连续，由最值定理，$f$ 在 $[a, b]$ 上有最大值 $M$ 和最小值 $m$，即 $m \leq f(x) \leq M$。

由积分不等式定理：
$$m(b - a) \leq \int_a^b f(x) \, dx \leq M(b - a)$$

即：
$$m \leq \frac{1}{b - a} \int_a^b f(x) \, dx \leq M$$

由介值定理，存在 $c \in [a, b]$，使得：
$$f(c) = \frac{1}{b - a} \int_a^b f(x) \, dx$$

因此：
$$\int_a^b f(x) \, dx = f(c)(b - a)$$

### 2.4 换元法定理的证明

**证明**：设 $F$ 是 $f$ 的一个原函数，即 $F'(x) = f(x)$。

令 $x = g(t)$，其中 $g(t)$ 满足定理条件。考虑复合函数 $F(g(t))$，由链式法则：
$$\frac{d}{dt} F(g(t)) = F'(g(t)) \cdot g'(t) = f(g(t)) \cdot g'(t)$$

因此 $f(g(t)) \cdot g'(t)$ 的原函数是 $F(g(t))$。

由牛顿-莱布尼茨公式：
$$\int_{\alpha}^{\beta} f(g(t)) \cdot g'(t) \, dt = \left[ F(g(t)) \right]_{\alpha}^{\beta} = F(g(\beta)) - F(g(\alpha))$$

由于 $g(\alpha) = a$，$g(\beta) = b$，所以：
$$F(g(\beta)) - F(g(\alpha)) = F(b) - F(a) = \int_a^b f(x) \, dx$$

得证：
$$\int_a^b f(x) \, dx = \int_{\alpha}^{\beta} f(g(t)) \cdot g'(t) \, dt$$

### 2.5 分部积分法定理的证明

**证明**：设 $u$ 和 $v$ 在 $[a, b]$ 上可导，由乘积法则：
$$\frac{d}{dx} [u(x) v(x)] = u'(x) v(x) + u(x) v'(x)$$

即：
$$u(x) v'(x) = \frac{d}{dx} [u(x) v(x)] - u'(x) v(x)$$

两边在 $[a, b]$ 上积分：
$$\int_a^b u(x) v'(x) \, dx = \int_a^b \frac{d}{dx} [u(x) v(x)] \, dx - \int_a^b u'(x) v(x) \, dx$$

由牛顿-莱布尼茨公式：
$$\int_a^b \frac{d}{dx} [u(x) v(x)] \, dx = [u(x) v(x)]_a^b = u(b)v(b) - u(a)v(a)$$

因此：
$$\int_a^b u(x) v'(x) \, dx = \left[ u(x) v(x) \right]_a^b - \int_a^b u'(x) v(x) \, dx$$

记 $du = u'(x) \, dx$，$dv = v'(x) \, dx$，则：
$$\int_a^b u \, dv = \left[ uv \right]_a^b - \int_a^b v \, du$$

得证。

### 2.6 积分线性性的证明

**证明**：设 $h(x) = \alpha f(x) + \beta g(x)$，则：
$$\int_a^b h(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^n h(x_i^*) \cdot \Delta x$$
$$= \lim_{n \to \infty} \sum_{i=1}^n [\alpha f(x_i^*) + \beta g(x_i^*)] \cdot \Delta x$$
$$= \alpha \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*) \cdot \Delta x + \beta \lim_{n \to \infty} \sum_{i=1}^n g(x_i^*) \cdot \Delta x$$
$$= \alpha \int_a^b f(x) \, dx + \beta \int_a^b g(x) \, dx$$

### 2.7 积分区间可加性的证明

**证明**：设 $a < b < c$，将 $[a, c]$ 分成 $[a, b]$ 和 $[b, c]$ 两部分。

对于任意划分和采样点，可以将和分成两部分，分别对应 $[a, b]$ 和 $[b, c]$。

取极限得：
$$\int_a^c f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*) \cdot \Delta x$$
$$= \lim_{n_1 \to \infty} \sum_{i=1}^{n_1} f(x_i^*) \cdot \Delta x + \lim_{n_2 \to \infty} \sum_{j=1}^{n_2} f(x_j^*) \cdot \Delta x$$
$$= \int_a^b f(x) \, dx + \int_b^c f(x) \, dx$$

### 2.8 绝对值不等式的证明

**证明**：由 $-|f(x)| \leq f(x) \leq |f(x)|$，根据积分保序性：
$$\int_a^b (-|f(x)|) \, dx \leq \int_a^b f(x) \, dx \leq \int_a^b |f(x)| \, dx$$

即：
$$-\int_a^b |f(x)| \, dx \leq \int_a^b f(x) \, dx \leq \int_a^b |f(x)| \, dx$$

因此：
$$\left|\int_a^b f(x) \, dx\right| \leq \int_a^b |f(x)| \, dx$$

### 2.9 区间再现公式的证明

**证明**：令 $t = a + b - x$，则 $x = a + b - t$，$dx = -dt$。

当 $x = a$ 时，$t = a + b - a = b$；
当 $x = b$ 时，$t = a + b - b = a$。

于是：
$$\int_a^b f(x) \, dx = \int_b^a f(a + b - t) \cdot (-dt) = \int_a^b f(a + b - t) \, dt$$

将积分变量 $t$ 换回 $x$（定积分与积分变量无关）：
$$\int_a^b f(a + b - t) \, dt = \int_a^b f(a + b - x) \, dx$$

得证：
$$\int_a^b f(x) \, dx = \int_a^b f(a + b - x) \, dx$$

## 4. 推论\性质

### 4.1 定积分的线性性

**推论1**：设 $f$ 和 $g$ 在 $[a, b]$ 上可积，$\alpha$ 和 $\beta$ 为常数，则：
$$\int_a^b [\alpha f(x) + \beta g(x)] \, dx = \alpha \int_a^b f(x) \, dx + \beta \int_a^b g(x) \, dx$$

### 4.2 积分区间的可加性

**推论2**：设 $f$ 在 $[a, c]$ 上可积，且 $a < b < c$，则：
$$\int_a^c f(x) \, dx = \int_a^b f(x) \, dx + \int_b^c f(x) \, dx$$

**推广**：对于任意划分 $a = x_0 < x_1 < \ldots < x_n = b$：
$$\int_a^b f(x) \, dx = \sum_{i=1}^n \int_{x_{i-1}}^{x_i} f(x) \, dx$$

### 4.3 积分的保序性

**推论3**：设 $f$ 和 $g$ 在 $[a, b]$ 上可积，且 $f(x) \leq g(x)$ 对所有 $x \in [a, b]$，则：
$$\int_a^b f(x) \, dx \leq \int_a^b g(x) \, dx$$

特别地，如果 $f(x) \geq 0$ 对所有 $x \in [a, b]$，则 $\int_a^b f(x) \, dx \geq 0$。

### 4.4 积分的绝对值不等式

**推论4**：设 $f$ 在 $[a, b]$ 上可积，则：
$$\left|\int_a^b f(x) \, dx\right| \leq \int_a^b |f(x)| \, dx$$

### 4.5 积分的对称性

**推论5**：设 $f$ 在 $[-a, a]$ 上可积：
- 如果 $f$ 是偶函数（$f(-x) = f(x)$），则 $\int_{-a}^a f(x) dx = 2 \int_0^a f(x) dx$
- 如果 $f$ 是奇函数（$f(-x) = -f(x)$），则 $\int_{-a}^a f(x) dx = 0$

### 4.6 积分的估值

**推论6**：设 $m \leq f(x) \leq M$ 对所有 $x \in [a, b]$，则：
$$m(b - a) \leq \int_a^b f(x) \, dx \leq M(b - a)$$

### 4.7 积分学基本定理的进一步结果

**定理**（ Leibniz 公式）：设 $f$ 连续，$u(x), v(x)$ 可导，则：
$$\frac{d}{dx} \int_{u(x)}^{v(x)} f(t) \, dt = f(v(x))v'(x) - f(u(x))u'(x)$$

**定理**（含参量积分的可微性）：设 $f(x, t)$ 在区域 $[a, b] \times [c, d]$ 上连续，且 $\frac{\partial f}{\partial x}$ 连续，则：
$$\frac{d}{dx} \int_c^d f(x, t) \, dt = \int_c^d \frac{\partial f}{\partial x}(x, t) \, dt$$

**定理**（含参量积分的连续性）：设 $f(x, t)$ 在 $[a, b] \times [c, d]$ 上连续，则 $F(x) = \int_c^d f(x, t) dt$ 在 $[a, b]$ 上连续。

**定理**（Riemann-Lebesgue 引理）：若 $f$ 在 $[a, b]$ 上可积，则：
$$\lim_{p \to \infty} \int_a^b f(x) \sin(px) \, dx = 0$$
$$\lim_{p \to \infty} \int_a^b f(x) \cos(px) \, dx = 0$$

---

## 5. 广义积分

### 5.1 无穷限积分

**定义**（无穷限积分）：
$$\int_a^{\infty} f(x) dx = \lim_{b \to \infty} \int_a^b f(x) dx$$
$$\int_{-\infty}^b f(x) dx = \lim_{a \to -\infty} \int_a^b f(x) dx$$
$$\int_{-\infty}^{\infty} f(x) dx = \int_{-\infty}^c f(x) dx + \int_c^{\infty} f(x) dx$$

- 收敛：极限存在
- 发散：极限不存在或不等
### 5.2 无界函数积分

**定义**（无界函数积分/瑕积分）：设 $f$ 在 $[a, b]$ 上无界（在 $a$ 点），则：
$$\int_a^b f(x) dx = \lim_{c \to a^+} \int_c^b f(x) dx$$

**瑕点**：无界函数积分中，函数趋向无穷的点称为瑕点。

### 5.3 广义积分的收敛判别法

**极限比较判别法**：设 $f$ 和 $g$ 在 $[a, \infty)$ 上非负，且 $\lim_{x \to \infty} \frac{f(x)}{g(x)} = L$：
- 若 $0 < L < \infty$，则 $\int_a^{\infty} f(x) dx$ 与 $\int_a^{\infty} g(x) dx$ 同敛散
- 若 $L = 0$ 且 $\int_a^{\infty} g(x) dx$ 收敛，则 $\int_a^{\infty} f(x) dx$ 也收敛
- 若 $L = \infty$ 且 $\int_a^{\infty} g(x) dx$ 发散，则 $\int_a^{\infty} f(x) dx$ 也发散

**p-判别法**（无穷限积分）：
- $\int_1^{\infty} \frac{1}{x^p} dx$ 收敛当且仅当 $p > 1$
- $\int_0^1 \frac{1}{x^p} dx$ 收敛当且仅当 $p < 1$

**柯西判别法**：设 $f$ 在 $[a, \infty)$ 上非负：
- 若 $\lim_{x \to \infty} x^p f(x) = L$，则：
  - 若 $p > 1$ 且 $L < \infty$，则 $\int_a^{\infty} f(x) dx$ 收敛
  - 若 $p \leq 1$ 且 $L > 0$（或 $L = \infty$），则 $\int_a^{\infty} f(x) dx$ 发散

### 5.4 绝对收敛与条件收敛

**定义**：设 $\int_a^{\infty} f(x) dx$ 收敛：
- 若 $\int_a^{\infty} |f(x)| dx$ 也收敛，则称原积分**绝对收敛**
- 若 $\int_a^{\infty} |f(x) dx|$ 发散，而 $\int_a^{\infty} f(x) dx$ 收敛，则称原积分**条件收敛**

**性质**：绝对收敛的广义积分必定收敛。

**莱布尼茨判别法**（交错级数形式）：设 $f(x)$ 在 $[a, \infty)$ 上单调递减且 $\lim_{x \to \infty} f(x) = 0$，则 $\int_a^{\infty} (-1)^{[x]} f(x) dx$ 收敛。

### 5.5 柯西主值

**定义**（主值积分）：对于无穷限积分，若极限存在，则称为主值积分：
$$\text{P.V.} \int_{-\infty}^{\infty} f(x) dx = \lim_{A \to \infty} \int_{-A}^{A} f(x) dx$$

**定义**（瑕积分主值）：设 $f$ 在 $c \in (a, b)$ 无界：
$$\text{P.V.} \int_a^b f(x) dx = \lim_{\varepsilon \to 0^+} \left( \int_a^{c-\varepsilon} f(x) dx + \int_{c+\varepsilon}^b f(x) dx \right)$$

**例**：$\text{P.V.} \int_{-\infty}^{\infty} x dx = 0$（虽然 $\int_{-\infty}^{\infty} x dx$ 发散）

### 5.6 常用广义积分公式

| 积分                                    | 收敛条件    | 值                      |
| ------------------------------------- | ------- | ---------------------- |
| $\int_0^{\infty} \frac{\sin x}{x} dx$ | 收敛      | $\frac{\pi}{2}$        |
| $\int_0^{\infty} e^{-ax} \sin(bx) dx$ | $a > 0$ | $\frac{b}{a^2 + b^2}$  |
| $\int_0^{\infty} e^{-ax} \cos(bx) dx$ | $a > 0$ | $\frac{a}{a^2 + b^2}$  |
| $\int_0^{\infty} \frac{1}{1+x^2} dx$  | 收敛      | $\frac{\pi}{2}$        |
| $\int_0^1 \frac{1}{x^p} dx$           | $p < 1$ | $\frac{1}{1-p}$        |
| $\int_1^{\infty} \frac{1}{x^p} dx$    | $p > 1$ | $\frac{1}{p-1}$        |
| $\int_0^{\infty} e^{-x^2} dx$         | 收敛      | $\frac{\sqrt{\pi}}{2}$ |
| $\int_0^{\pi/2} \ln(\sin x) dx$       | 收敛      | $-\frac{\pi}{2} \ln 2$ |

---

## 6. 计算方法

### 6.1 换元法的常用技巧

**技巧1**（凑微分法）：如果 $f'(x) = g(x)$，即 $g$ 是 $f$ 的原函数，则：
$$\int_a^b f'(x) \, dx = f(b) - f(a)$$

**技巧2**（常见凑微分形式）：
- $\int_a^b f(ax + b) \, dx = \frac{1}{a} \int_{a a+b}^{ab+b} f(u) \, du$
- $\int_a^b f(x^2) \cdot x \, dx = \frac{1}{2} \int_{a^2}^{b^2} f(u) \, du$
- $\int_a^b \frac{f'(x)}{f(x)} \, dx = \ln \left| \frac{f(b)}{f(a)} \right|$

### 6.2 分部积分的常见公式

**技巧3**（循环公式）：对于 $\int e^x \sin x \, dx$ 或 $\int e^x \cos x \, dx$，使用两次分部积分后会出现原积分，可解方程求得结果。

**技巧4**（降幂公式）：
- $\int \sin^n x \, dx = -\frac{1}{n} \sin^{n-1} x \cos x + \frac{n-1}{n} \int \sin^{n-2} x \, dx$
- $\int \cos^n x \, dx = \frac{1}{n} \cos^{n-1} x \sin x + \frac{n-1}{n} \int \cos^{n-2} x \, dx$

**技巧5**（分部积分的表格法）：对于 $\int u \, dv$，可用表格法快速计算：
- 轮流取导和积分为两列
- 从左上到右下斜乘取正，从右上到左下斜乘取负
- 遇到导数为0时停止

### 6.3 常用积分公式表

**有理函数积分**：

| 积分                      | 结果                                        |
| ----------------------- | ----------------------------------------- |
| $\int x^n dx$           | $\frac{x^{n+1}}{n+1} + C$（$n \neq -1$）    |
| $\int \frac{1}{x} dx$   | $\ln\vert x \vert +C$                     |
| $\int \frac{1}{x^2} dx$ | $-\frac{1}{x} + C$                        |
| $\int \frac{1}{x^n} dx$ | $-\frac{1}{(n-1)x^{n-1}} + C$（$n \neq 1$） |

**指数函数积分**：

| 积分 | 结果 |
|------|------|
| $\int e^x dx$ | $e^x + C$ |
| $\int a^x dx$ | $\frac{a^x}{\ln a} + C$ |
| $\int x e^x dx$ | $(x-1)e^x + C$ |
| $\int x^2 e^x dx$ | $(x^2-2x+2)e^x + C$ |

**三角函数积分**：

| 积分                         | 结果                                    |
| -------------------------- | ------------------------------------- |
| $\int \sin x \, dx$        | $-\cos x + C$                         |
| $\int \cos x \, dx$        | $\sin x + C$                          |
| $\int \tan x \, dx$        | $-\ln \vert\cos x\vert + C$           |
| $\int \cot x \, dx$        | $\ln \vert\sin x\vert + C$            |
| $\int \sec x \, dx$        | $\ln \vert\sec x + \tan x\vert + C$   |
| $\int \csc x \, dx$        | $\ln \vert\csc x - \cot x\vert + C$   |
| $\int \sin^2 x \, dx$      | $\frac{x}{2} - \frac{\sin 2x}{4} + C$ |
| $\int \cos^2 x \, dx$      | $\frac{x}{2} + \frac{\sin 2x}{4} + C$ |
| $\int \sec^2 x \, dx$      | $\tan x + C$                          |
| $\int \csc^2 x \, dx$      | $-\cot x + C$                         |
| $\int \sec x \tan x \, dx$ | $\sec x + C$                          |
| $\int \csc x \cot x \, dx$ | $-\csc x + C$                         |

**反三角函数积分**：

| 积分 | 结果 |
|------|------|
| $\int \frac{1}{\sqrt{1-x^2}} dx$ | $\arcsin x + C$ |
| $\int \frac{1}{1+x^2} dx$ | $\arctan x + C$ |

**对数函数积分**：

| 积分 | 结果 |
|------|------|
| $\int \ln x dx$ | $x \ln x - x + C$ |
| $\int \log_a x dx$ | $x \log_a x - \frac{x}{\ln a} + C$ |

**常见定积分公式**：

| 积分 | 结果 |
|------|------|
| $\int_0^{\pi} \sin x dx$ | $2$ |
| $\int_0^{\pi} \cos x dx$ | $0$ |
| $\int_0^{\pi/2} \sin^n x dx$ | $\frac{(n-1)!!}{n!!} \cdot \frac{\pi}{2}$（$n$ 为偶数） |
| $\int_0^{\pi/2} \sin^n x dx$ | $\frac{(n-1)!!}{n!!}$（$n$ 为奇数） |
| $\int_0^{\pi} x \sin x dx$ | $\pi$ |
| $\int_0^{\pi} x \cos x dx$ | $-2$ |
| $\int_0^{2\pi} \sin^2 x dx$ | $\pi$ |
| $\int_0^{2\pi} \cos^2 x dx$ | $\pi$ |
| $\int_0^{\infty} e^{-x} dx$ | $1$ |
| $\int_0^{\infty} x e^{-x} dx$ | $1$ |
| $\int_0^{\infty} e^{-x^2} dx$ | $\frac{\sqrt{\pi}}{2}$（高斯积分） |
| $\int_0^1 x^{\alpha} dx$ | $\frac{1}{\alpha+1}$（$\alpha > -1$） |

---

## 7. 积分技巧

### 7.1 区间再现公式

**公式**：对于任意可积函数 $f(x)$，都有：
$$\int_a^b f(x) \, dx = \int_a^b f(a + b - x) \, dx$$

**证明**：令 $t = a + b - x$，则 $x = a + b - t$，$dx = -dt$。

当 $x = a$ 时，$t = b$；当 $x = b$ 时，$t = a$。

$$\int_a^b f(x) \, dx = \int_b^a f(a + b - t) \cdot (-dt) = \int_a^b f(a + b - t) \, dt = \int_a^b f(a + b - x) \, dx$$

**应用场景**：
- 计算 $\int_0^{\pi/2} \sin^n x \, dx$ 与 $\int_0^{\pi/2} \cos^n x \, dx$ 的关系
- 计算 $\int_0^{\pi} x f(\sin x) \, dx$ 类型的问题
- 被积函数含有 $a+b-x$ 形式的结构

**经典应用**：设 $I_n = \int_0^{\pi/2} \sin^n x \, dx$，则 $I_n = \int_0^{\pi/2} \cos^n x \, dx$。

### 7.2 偶倍奇零（对称区间积分）

**公式**：设 $f$ 在 $[-a, a]$ 上可积：
- **偶函数**：若 $f(-x) = f(x)$，则 $\int_{-a}^a f(x) \, dx = 2 \int_0^a f(x) \, dx$
- **奇函数**：若 $f(-x) = -f(x)$，则 $\int_{-a}^a f(x) \, dx = 0$

**推广**：
- $\int_{-a}^a f(x) \, dx = \int_0^a [f(x) + f(-x)] \, dx$
- 任何函数可分解为偶函数和奇函数之和：$f(x) = \frac{f(x) + f(-x)}{2} + \frac{f(x) - f(-x)}{2}$

**常见奇函数**：$x, x^3, \sin x, \tan x, \arcsin x, \arctan x$ 等
**常见偶函数**：$x^2, x^4, \cos x, e^x + e^{-x}, |x|$ 等

### 7.3 周期函数积分

**性质1**（周期函数的定积分）：若 $f(x)$ 是周期为 $T$ 的可积函数，则：
$$\int_a^{a+T} f(x) \, dx = \int_0^T f(x) \, dx$$

即周期函数在任意长度为一个周期的区间上的积分值相等。

**性质2**（周期函数的对称性）：若 $f(x)$ 是周期为 $T$ 的函数：
- $\int_0^{nT} f(x) \, dx = n \int_0^T f(x) \, dx$（$n$ 为整数）
- $\int_{a}^{a+nT} f(x) \, dx = n \int_0^T f(x) \, dx$

**性质3**（三角函数系的正交性）：
$$\int_0^{2\pi} \sin mx \cdot \sin nx \, dx = \begin{cases} \pi & m = n \neq 0 \\ 0 & m \neq n \end{cases}$$
$$\int_0^{2\pi} \cos mx \cdot \cos nx \, dx = \begin{cases} \pi & m = n \neq 0 \\ 0 & m \neq n \end{cases}$$
$$\int_0^{2\pi} \sin mx \cdot \cos nx \, dx = 0$$
$$\int_0^{2\pi} \sin mx \, dx = \int_0^{2\pi} \cos mx \, dx = 0 \quad (m \geq 1)$$

### 7.4 常用积分技巧组合

**技巧1**（区间再现 + 对称性）：计算 $I = \int_0^{\pi} \frac{x \sin x}{1 + \cos^2 x} \, dx$

解：令 $t = \pi - x$，则 $x = \pi - t$，$dx = -dt$：
$$I = \int_{\pi}^0 \frac{(\pi - t) \sin(\pi - t)}{1 + \cos^2(\pi - t)} \cdot (-dt) = \int_0^{\pi} \frac{(\pi - t) \sin t}{1 + \cos^2 t} \, dt$$

两式相加：
$$2I = \pi \int_0^{\pi} \frac{\sin t}{1 + \cos^2 t} \, dt$$

令 $u = \cos t$，$du = -\sin t \, dt$：
$$2I = \pi \int_{1}^{-1} \frac{-du}{1 + u^2} = \pi \int_{-1}^{1} \frac{du}{1 + u^2} = \pi \left[ \arctan u \right]_{-1}^{1} = \pi \left( \frac{\pi}{4} - (-\frac{\pi}{4}) \right) = \frac{\pi^2}{2}$$

因此 $I = \frac{\pi^2}{4}$。

**技巧2**（分部积分 + 递推公式）：计算 $I_n = \int_0^{\pi/2} \sin^n x \, dx$

由分部积分可得递推公式：
$$I_n = \frac{n-1}{n} I_{n-2} \quad (n \geq 2)$$

且 $I_0 = \frac{\pi}{2}$，$I_1 = 1$。

因此：
$$I_n = \begin{cases} \frac{(n-1)!!}{n!!} \cdot \frac{\pi}{2} & n \text{ 为偶数} \\ \frac{(n-1)!!}{n!!} & n \text{ 为奇数} \end{cases}$$

### 7.5 积分技巧小结

| 技巧 | 适用场景 | 关键思想 |
|------|----------|----------|
| 区间再现 | 被积函数含 $a+b-x$ 结构 | 变量替换 $t = a+b-x$ |
| 偶倍奇零 | 对称区间 $[-a, a]$ | 判断函数的奇偶性 |
| 周期函数 | 积分区间包含整数个周期 | 积分值与起始点无关 |
| 分部积分 | 被积函数为乘积形式 | 选择合适的 $u, dv$ |
| 换元法 | 复杂被积函数 | 化简被积函数 |

---

## 8. Γ函数

### 8.1 Gamma函数定义

**定义**（Gamma函数）：Gamma函数是阶乘函数的连续延拓，定义为：
$$\Gamma(s) = \int_0^{\infty} x^{s-1} e^{-x} \, dx \quad (s > 0)$$

### 8.2 Gamma函数性质

**性质1**（递推公式）：
$$\Gamma(s+1) = s\Gamma(s)$$
特别地，对于正整数 $n$：$\Gamma(n+1) = n!$

**性质2**（余元公式）：
$$\Gamma(s) \Gamma(1-s) = \frac{\pi}{\sin(\pi s)} \quad (0 < s < 1)$$

**性质3**（倍元公式/Legendre公式）：
$$\Gamma(2s) = \frac{2^{2s-1}}{\sqrt{\pi}} \Gamma(s) \Gamma\left(s + \frac{1}{2}\right)$$

**性质4**（与Beta函数的关系）：
$$B(p, q) = \int_0^1 x^{p-1} (1-x)^{q-1} \, dx = \frac{\Gamma(p) \Gamma(q)}{\Gamma(p+q)}$$

**常见值**：
- $\Gamma(1) = 1$
- $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$
- $\Gamma\left(\frac{3}{2}\right) = \frac{\sqrt{\pi}}{2}$
- $\Gamma(n+1) = n!$（$n$ 为正整数）

---

## 9. 应用

### 9.1 几何应用：面积

**面积公式**：曲线 $y = f(x)$ 与 $x$ 轴在 $[a, b]$ 之间的面积为：
$$A = \int_a^b |f(x)| dx$$

### 9.2 几何应用：体积

**旋转体体积**（圆盘法）：绕 $x$ 轴旋转的体积：
$$V = \pi \int_a^b [f(x)]^2 dx$$

### 9.3 几何应用：弧长

**弧长公式**：曲线 $y = f(x)$ 在 $[a, b]$ 上的弧长：
$$L = \int_a^b \sqrt{1 + [f'(x)]^2} dx$$

### 9.4 经济应用：元素法的经济应用

**定义**（收益流）：设收益率为时间 $t$ 的函数 $r(t)$（单位时间内的收益），则在时间区间 $[a, b]$ 内的总收益为：
$$R = \int_a^b r(t) \, dt$$

**现值**（Present Value）：未来收益按贴现率 $i$ 折算到当前时刻的价值。设收益流 $r(t)$ 在 $[0, T]$ 时刻开始产生，贴现率为常数 $i$，则收益流的现值为：
$$PV = \int_0^T r(t) \cdot e^{-it} \, dt$$

**将来值**（Future Value）：将收益流按复利 $i$ 累积到未来时刻 $T$ 的价值：
$$FV = \int_0^T r(t) \cdot e^{i(T-t)} \, dt = e^{iT} \int_0^T r(t) \cdot e^{-it} \, dt = e^{iT} \cdot PV$$

**投资回收期**：设初始投资为 $P$，年收益流为常数 $r$，贴现率为 $i$，则投资回收期满足：
$$P = \int_0^{T} r \cdot e^{-it} \, dt = \frac{r}{i}(1 - e^{-iT})$$

解得：
$$T = -\frac{1}{i} \ln\left(1 - \frac{Pi}{r}\right)$$

**资本价值**：设资产使用寿命为 $T$，期末残值为 $L$，年收益流为 $r(t)$，贴现率为 $i$，则资本价值为：
$$NV = \int_0^T r(t) \cdot e^{-it} \, dt + L \cdot e^{-iT} - P$$

其中 $P$ 为初始投资。

---

## 10. 例题

### 例题1：利用牛顿-莱布尼茨公式计算定积分

**问题**：计算 $\int_0^{\pi} \sin x \, dx$

**解**：$\sin x$ 的一个原函数是 $-\cos x$，由牛顿-莱布尼茨公式：
$$\int_0^{\pi} \sin x \, dx = [-\cos x]_0^{\pi} = -\cos \pi + \cos 0 = -(-1) + 1 = 2$$

### 例题2：利用积分的线性性

**问题**：计算 $\int_0^1 (3x^2 + 2x + 1) \, dx$

**解**：由积分的线性性：
$$\int_0^1 (3x^2 + 2x + 1) \, dx = 3\int_0^1 x^2 \, dx + 2\int_0^1 x \, dx + \int_0^1 1 \, dx$$
$$= 3 \cdot \left[\frac{x^3}{3}\right]_0^1 + 2 \cdot \left[\frac{x^2}{2}\right]_0^1 + [x]_0^1$$
$$= 3 \cdot \frac{1}{3} + 2 \cdot \frac{1}{2} + 1 = 1 + 1 + 1 = 3$$

### 例题3：利用积分的对称性

**问题**：计算 $\int_{-\pi}^{\pi} x^2 \sin x \, dx$

**解**：被积函数 $f(x) = x^2 \sin x$ 是奇函数（因为 $f(-x) = (-x)^2 \sin(-x) = -x^2 \sin x = -f(x)$），且积分区间关于原点对称。

因此：
$$\int_{-\pi}^{\pi} x^2 \sin x \, dx = 0$$

### 例题4：利用积分中值定理

**问题**：证明存在 $c \in [0, \pi/2]$，使得 $\int_0^{\pi/2} \sin x \, dx = \sin c \cdot \frac{\pi}{2}$

**解**：$\sin x$ 在 $[0, \pi/2]$ 上连续，由积分中值定理，存在 $c \in [0, \pi/2]$，使得：
$$\int_0^{\pi/2} \sin x \, dx = \sin c \cdot \left(\frac{\pi}{2} - 0\right) = \sin c \cdot \frac{\pi}{2}$$

由例题1，$\int_0^{\pi} \sin x \, dx = 2$，故 $\int_0^{\pi/2} \sin x \, dx = 1$。

因此 $\sin c \cdot \frac{\pi}{2} = 1$，即 $\sin c = \frac{2}{\pi}$，$c = \arcsin\left(\frac{2}{\pi}\right)$。

### 例题5：计算面积

**问题**：计算曲线 $y = x^2$ 与 $x$ 轴在 $[0, 1]$ 之间的面积

**解**：由于 $x^2 \geq 0$ 对所有 $x \in [0, 1]$，面积等于定积分：
$$\text{面积} = \int_0^1 x^2 \, dx = \left[\frac{x^3}{3}\right]_0^1 = \frac{1}{3} - 0 = \frac{1}{3}$$

### 例题6：计算旋转体的体积

**问题**：计算曲线 $y = \sqrt{x}$ 在 $[0, 1]$ 上绕 $x$ 轴旋转形成的旋转体体积

**解**：使用圆盘法：
$$V = \pi \int_0^1 (\sqrt{x})^2 \, dx = \pi \int_0^1 x \, dx = \pi \left[\frac{x^2}{2}\right]_0^1 = \frac{\pi}{2}$$

### 例题7：计算曲线的弧长

**问题**：计算曲线 $y = \frac{2}{3}x^{3/2}$ 在 $[0, 3]$ 上的弧长

**解**：首先计算导数：
$$y' = \frac{d}{dx}\left(\frac{2}{3}x^{3/2}\right) = x^{1/2} = \sqrt{x}$$

弧长公式：
$$L = \int_0^3 \sqrt{1 + (y')^2} \, dx = \int_0^3 \sqrt{1 + x} \, dx$$

设 $u = 1 + x$，$du = dx$：
$$L = \int_1^4 \sqrt{u} \, du = \left[\frac{2}{3}u^{3/2}\right]_1^4 = \frac{2}{3}(8 - 1) = \frac{14}{3}$$

### 例题10：利用积分不等式估计

**问题**：估计 $\int_0^{\pi} e^{-x} \sin x \, dx$ 的范围

**解**：由于 $e^{-x} \sin x$ 在 $[0, \pi]$ 上非负，且最大值在 $x = \frac{\pi}{2}$ 处取得：
$$\max_{x \in [0, \pi]} e^{-x} \sin x = e^{-\pi/2} \cdot 1 = e^{-\pi/2}$$

因此：
$$0 \leq \int_0^{\pi} e^{-x} \sin x \, dx \leq e^{-\pi/2} \cdot \pi$$

计算精确值：
$$\int_0^{\pi} e^{-x} \sin x \, dx = \left[-\frac{e^{-x}}{2}(\sin x + \cos x)\right]_0^{\pi} = \frac{1 + e^{-\pi}}{2}$$

### 例题11：利用换元法计算定积分

**问题**：计算 $\int_0^4 \frac{1}{1 + \sqrt{x}} \, dx$

**解**：令 $t = \sqrt{x}$，则 $x = t^2$，$dx = 2t \, dt$。

当 $x = 0$ 时，$t = 0$；当 $x = 4$ 时，$t = 2$。

$$\int_0^4 \frac{1}{1 + \sqrt{x}} \, dx = \int_0^2 \frac{1}{1 + t} \cdot 2t \, dt = \int_0^2 \frac{2t}{1 + t} \, dt$$

化简：
$$\frac{2t}{1 + t} = 2 - \frac{2}{1 + t}$$

因此：
$$\int_0^2 \frac{2t}{1 + t} \, dt = \int_0^2 \left(2 - \frac{2}{1 + t}\right) dt = \left[2t - 2\ln(1+t)\right]_0^2$$
$$= (4 - 2\ln 3) - (0 - 2\ln 1) = 4 - 2\ln 3$$

### 例题12：利用换元法计算三角函数积分

**问题**：计算 $\int_0^{\pi/2} \sin^2 x \, dx$

**解**：方法一（换元法）：令 $u = 2x$，$du = 2dx$，$dx = \frac{1}{2} du$。

当 $x = 0$ 时，$u = 0$；当 $x = \pi/2$ 时，$u = \pi$。

$$\int_0^{\pi/2} \sin^2 x \, dx = \frac{1}{2} \int_0^{\pi} \sin^2 u \, du = \frac{1}{2} \int_0^{\pi} \frac{1 - \cos 2u}{2} \, du$$
$$= \frac{1}{4} \int_0^{\pi} (1 - \cos 2u) \, du = \frac{1}{4} \left[u - \frac{\sin 2u}{2}\right]_0^{\pi}$$
$$= \frac{1}{4} \left(\pi - 0\right) = \frac{\pi}{4}$$

方法二（公式法）：$\sin^2 x = \frac{1 - \cos 2x}{2}$，结果相同。

### 例题13：利用分部积分法计算定积分

**问题**：计算 $\int_0^1 x e^x \, dx$

**解**：设 $u = x$，$dv = e^x \, dx$，则 $du = dx$，$v = e^x$。

由分部积分公式：
$$\int_0^1 x e^x \, dx = \left[ x e^x \right]_0^1 - \int_0^1 e^x \, dx = (1 \cdot e^1 - 0 \cdot e^0) - \left[e^x\right]_0^1$$
$$= e - (e - 1) = 1$$

### 例题14：利用分部积分法计算对数函数积分

**问题**：计算 $\int_1^e \ln x \, dx$

**解**：设 $u = \ln x$，$dv = dx$，则 $du = \frac{1}{x} dx$，$v = x$。

由分部积分公式：
$$\int_1^e \ln x \, dx = \left[ x \ln x \right]_1^e - \int_1^e x \cdot \frac{1}{x} \, dx = (e \ln e - 1 \cdot \ln 1) - \int_1^e 1 \, dx$$
$$= (e \cdot 1 - 0) - [x]_1^e = e - (e - 1) = 1$$

### 例题15：利用分部积分法的循环公式

**问题**：计算 $\int_0^{\pi} e^x \sin x \, dx$

**解**：设 $I = \int e^x \sin x \, dx$。

第一次分部积分：令 $u = \sin x$，$dv = e^x dx$，则 $du = \cos x dx$，$v = e^x$。
$$I = e^x \sin x - \int e^x \cos x \, dx$$

第二次分部积分：令 $u = \cos x$，$dv = e^x dx$，则 $du = -\sin x dx$，$v = e^x$。
$$\int e^x \cos x \, dx = e^x \cos x + \int e^x \sin x \, dx = e^x \cos x + I$$

因此：
$$I = e^x \sin x - (e^x \cos x + I) = e^x (\sin x - \cos x) - I$$

解得：
$$2I = e^x (\sin x - \cos x) \implies I = \frac{e^x}{2} (\sin x - \cos x)$$

代入上下限：
$$\int_0^{\pi} e^x \sin x \, dx = \left[\frac{e^x}{2} (\sin x - \cos x)\right]_0^{\pi}$$
$$= \frac{e^{\pi}}{2} (\sin \pi - \cos \pi) - \frac{e^0}{2} (\sin 0 - \cos 0)$$
$$= \frac{e^{\pi}}{2} (0 - (-1)) - \frac{1}{2} (0 - 1) = \frac{e^{\pi}}{2} + \frac{1}{2} = \frac{e^{\pi} + 1}{2}$$

### 例题16：换元法与分部积分法综合

**问题**：计算 $\int_0^{\pi^2/4} \sin \sqrt{x} \, dx$

**解**：令 $t = \sqrt{x}$，则 $x = t^2$，$dx = 2t \, dt$。

当 $x = 0$ 时，$t = 0$；当 $x = \pi^2/4$ 时，$t = \pi/2$。

$$\int_0^{\pi^2/4} \sin \sqrt{x} \, dx = \int_0^{\pi/2} \sin t \cdot 2t \, dt = 2 \int_0^{\pi/2} t \sin t \, dt$$

现在使用分部积分：设 $u = t$，$dv = \sin t \, dt$，则 $du = dt$，$v = -\cos t$。
$$2 \int_0^{\pi/2} t \sin t \, dt = 2 \left(\left[ -t \cos t \right]_0^{\pi/2} + \int_0^{\pi/2} \cos t \, dt \right)$$
$$= 2 \left(-\frac{\pi}{2} \cdot \cos \frac{\pi}{2} + 0 \cdot \cos 0 + \left[\sin t\right]_0^{\pi/2}\right)$$
$$= 2 \left(0 + \sin \frac{\pi}{2} - \sin 0\right) = 2 \cdot 1 = 2$$

### 例题17：收益流的现值计算

**问题**：某投资项目在10年内每年可产生收益5000元，贴现率为5%，求该收益流的现值。

**解**：设年收益流为常数 $r(t) = 5000$ 元，贴现率 $i = 5\% = 0.05$，收益期 $T = 10$ 年。

收益流的现值公式：
$$PV = \int_0^T r(t) \cdot e^{-it} \, dt$$

由于收益流为常数：
$$PV = 5000 \int_0^{10} e^{-0.05t} \, dt = 5000 \left[-\frac{1}{0.05} e^{-0.05t}\right]_0^{10}$$
$$= 5000 \cdot 20 \cdot (1 - e^{-0.5}) = 100000 \cdot (1 - e^{-0.5})$$

计算 $e^{-0.5} \approx 0.60653$，所以：
$$PV \approx 100000 \cdot (1 - 0.60653) = 100000 \cdot 0.39347 = 39347 \text{ 元}$$

**答案**：该收益流的现值约为39347元。

### 例题18：资本价值计算

**问题**：某设备初始投资10万元，使用5年后残值为2万元。使用期间每年产生收益3万元，贴现率为8%。求该设备的资本价值。

**解**：设初始投资 $P = 100000$ 元，年收益流 $r(t) = 30000$ 元，使用寿命 $T = 5$ 年，残值 $L = 20000$ 元，贴现率 $i = 0.08$。

资本价值公式：
$$NV = \int_0^T r(t) \cdot e^{-it} \, dt + L \cdot e^{-iT} - P$$

第一部分（收益流现值）：
$$\int_0^5 30000 \cdot e^{-0.08t} \, dt = 30000 \cdot \left[-\frac{1}{0.08} e^{-0.08t}\right]_0^5$$
$$= 30000 \cdot 12.5 \cdot (1 - e^{-0.4}) = 375000 \cdot (1 - 0.67032)$$
$$= 375000 \cdot 0.32968 = 123630 \text{ 元}$$

第二部分（残值现值）：
$$L \cdot e^{-iT} = 20000 \cdot e^{-0.4} = 20000 \cdot 0.67032 = 13406 \text{ 元}$$

资本价值：
$$NV = 123630 + 13406 - 100000 = 37036 \text{ 元}$$

**答案**：该设备的资本价值约为3.7万元（正值表示该项目可行）。

## 11. 代码示例（机器学习应用）

### 示例1：数值积分方法

```python
import numpy as np

def riemann_sum(f, a, b, n=1000, method='left'):
    """黎曼和法"""
    x = np.linspace(a, b, n+1)
    if method == 'left':
        x_mid = x[:-1]
    elif method == 'right':
        x_mid = x[1:]
    elif method == 'midpoint':
        x_mid = (x[:-1] + x[1:]) / 2
    
    y = f(x_mid)
    return np.sum(y) * (b - a) / n

def trapezoidal_rule(f, a, b, n=1000):
    """梯形法则"""
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (b - a) / (2 * n) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpsons_rule(f, a, b, n=1000):
    """辛普森法则（更精确）"""
    if n % 2 != 0:
        n += 1  # 辛普森法则需要偶数个区间
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

# 测试函数：f(x) = x²，在 [0, 1] 上的积分
f = lambda x: x**2
a, b = 0, 1
exact = 1/3  # 精确解

print("数值积分方法比较:")
print("-" * 60)
print(f"{'方法':<15} {'结果':<15} {'误差':<15} {'误差率':<15}")
print("-" * 60)

methods = [
    ('黎曼和（左）', lambda: riemann_sum(f, a, b, method='left')),
    ('黎曼和（中）', lambda: riemann_sum(f, a, b, method='midpoint')),
    ('梯形法则', lambda: trapezoidal_rule(f, a, b)),
    ('辛普森法则', lambda: simpsons_rule(f, a, b)),
]

for name, method in methods:
    result = method()
    error = abs(result - exact)
    error_rate = error / exact * 100
    print(f"{name:<15} {result:<15.10f} {error:<15.2e} {error_rate:<15.4f}%")

print(f"\n精确解: {exact}")
```

### 示例2：期望和方差的计算

```python
import numpy as np

def expected_value(pdf, x_range, nx=10000):
    """计算期望 E[X] = ∫x·f(x) dx"""
    a, b = x_range
    x = np.linspace(a, b, nx)
    f_x = pdf(x)
    return np.trapz(x * f_x, x)

def variance(pdf, x_range, nx=10000):
    """计算方差 Var(X) = E[X²] - (E[X])²"""
    a, b = x_range
    x = np.linspace(a, b, nx)
    f_x = pdf(x)
    
    e_x = np.trapz(x * f_x, x)
    e_x2 = np.trapz(x**2 * f_x, x)
    
    return e_x2 - e_x**2

# 均匀分布 U[0, 1]
uniform_pdf = lambda x: np.where((x >= 0) & (x <= 1), 1, 0)
e_uniform = expected_value(uniform_pdf, [-1, 2])
var_uniform = variance(uniform_pdf, [-1, 2])

print("均匀分布 U[0, 1]:")
print(f"期望 E[X] = {e_uniform:.6f} (理论值: 0.5)")
print(f"方差 Var(X) = {var_uniform:.6f} (理论值: 1/12 ≈ 0.0833)")

# 指数分布 Exp(λ=2)
lambda_param = 2
exp_pdf = lambda x: np.where(x >= 0, lambda_param * np.exp(-lambda_param * x), 0)
e_exp = expected_value(exp_pdf, [0, 10])
var_exp = variance(exp_pdf, [0, 10])

print(f"\n指数分布 Exp(λ={lambda_param}):")
print(f"期望 E[X] = {e_exp:.6f} (理论值: 1/λ = {1/lambda_param})")
print(f"方差 Var(X) = {var_exp:.6f} (理论值: 1/λ² = {1/lambda_param**2})")
```

### 示例3：损失函数的计算

```python
import numpy as np

def calculate_rmse(y_true, y_pred):
    """计算均方根误差"""
    return np.sqrt(np.mean((y_true - y_pred)**2))

def calculate_mae(y_true, y_pred):
    """计算平均绝对误差"""
    return np.mean(np.abs(y_true - y_pred))

def calculate_log_loss(y_true, y_prob):
    """计算对数损失"""
    epsilon = 1e-15
    y_prob = np.clip(y_prob, epsilon, 1 - epsilon)
    return -np.mean(y_true * np.log(y_prob) + (1 - y_true) * np.log(1 - y_prob))

# 示例数据
y_true = np.array([1, 0, 1, 1, 0])
y_pred_reg = np.array([0.9, 0.1, 0.8, 0.7, 0.2])
y_pred_class = np.array([0.85, 0.15, 0.75, 0.65, 0.25])

rmse = calculate_rmse(y_true, y_pred_reg)
mae = calculate_mae(y_true, y_pred_reg)
logloss = calculate_log_loss(y_true, y_pred_class)

print("损失函数计算:")
print(f"均方根误差 (RMSE): {rmse:.6f}")
print(f"平均绝对误差 (MAE): {mae:.6f}")
print(f"对数损失 (Log Loss): {logloss:.6f}")
```

### 示例4：贝叶斯推断中的边缘似然

```python
import numpy as np
from scipy import integrate

# 边缘似然计算
def marginal_likelihood(likelihood, prior, param_range):
    """
    计算边缘似然 P(D) = ∫P(D|θ)·P(θ) dθ
    
    参数:
        likelihood: 似然函数 P(D|θ)
        prior: 先验分布 P(θ)
        param_range: 参数范围
    """
    result, error = integrate.quad(
        lambda theta: likelihood(theta) * prior(theta),
        param_range[0],
        param_range[1]
    )
    return result

# 示例：伯努利实验的边缘似然
# 观察到 3 次成功，2 次失败
data = {'success': 3, 'failure': 2}

# 似然函数：P(D|p) = p^3 · (1-p)^2
likelihood = lambda p: p**3 * (1-p)**2

# 先验分布：Beta(1, 1)（均匀分布）
prior = lambda p: 1 if 0 <= p <= 1 else 0

# 计算边缘似然
p_marginal = marginal_likelihood(likelihood, prior, [0, 1])

print("贝叶斯推断 - 边缘似然计算:")
print(f"边缘似然 P(D) = {p_marginal:.10f}")
print(f"解析解: ∫(0 to 1) p³(1-p)² dp = B(4, 3) = 1/60 ≈ {1/60:.10f}")

# 后验分布：P(p|D) ∝ P(D|p)·P(p)
# 使用 Beta 分布：Beta(α=4, β=3）
alpha_post = data['success'] + 1
beta_post = data['failure'] + 1

print(f"\n后验分布: Beta({alpha_post}, {beta_post})")
print(f"后验均值: {alpha_post/(alpha_post+beta_post):.4f}")
print(f"后验方差: {(alpha_post*beta_post)/((alpha_post+beta_post)**2*(alpha_post+beta_post+1)):.4f}")
```

## 根据题型整理的做题方法
### 定积分计算的五大策略

遇到定积分问题，按以下思路分析。

#### 🔍 第一步：判断积分类型

| 积分类型 | 特点 | 主要方法 |
|---------|------|---------|
| **常义定积分** | 区间有限，函数有界 | 牛顿-莱布尼茨公式 |
| **广义积分** | 无限区间或无界函数 | 极限定义法 |
| **变限积分** | 积分限含变量 $x$ | 微积分基本定理 |
| **分段函数积分** | 函数在不同区间表达式不同 | 分段积分后求和 |

#### 📊 第二步：选择计算方法

```
定积分计算
    │
    ├── 能直接找原函数？
    │       └── 是 → 牛顿-莱布尼茨公式
    │
    ├── 被积函数含复合结构？
    │       └── 是 → 换元积分法（注意换限）
    │
    ├── 是乘积形式？
    │       └── 是 → 分部积分法
    │
    ├── 对称区间 [-a, a]？
    │       └── 是 → 检查奇偶性
    │           ├── 偶函数 → 2∫₀ᵃ
    │           └── 奇函数 → 0
    │
    ├── 周期函数？
    │       └── 是 → 利用周期性质
    │
    └── 含特殊结构？
            └── 是 → 区间再现公式
```

#### ✏️ 第三步：执行计算

**关键注意事项**：
1. **换元法**：积分限必须同时变换（$x \to t$，则 $a \to \alpha, b \to \beta$）
2. **分部积分**：定积分要代入上下限
3. **分段积分**：注意各区间上的表达式
4. **广义积分**：先判断收敛性再计算

#### ✅ 第四步：验证结果

- 检查结果符号是否合理
- 利用估值公式检验范围
- 数值方法验证

### 💡 核心技巧与常用结论

#### 1. 牛顿-莱布尼茨公式的应用

**公式**：$\int_a^b f(x) dx = F(b) - F(a)$

**使用条件**：
- $f(x)$ 在 $[a, b]$ 上连续
- $F(x)$ 是 $f(x)$ 的一个原函数

**常见陷阱**：
- 忘记常数 $C$ 对定积分无影响
- 原函数找错导致结果错误

#### 2. 换元积分法的要点

**公式**：$\int_a^b f(g(x))g'(x)dx = \int_{g(a)}^{g(b)} f(u)du$

**关键步骤**：
1. 设 $u = g(x)$
2. 计算 $du = g'(x)dx$
3. **换限**：当 $x = a$ 时，$u = g(a)$；当 $x = b$ 时，$u = g(b)$
4. 计算新积分
5. 不用换回原变量（定积分）

**常见换元**：

| 被积函数特征 | 换元方式 |
|-------------|---------|
| $f(\sqrt{x})$ | $t = \sqrt{x}$ |
| $f(ax+b)$ | $u = ax+b$ |
| $f(e^x)$ | $t = e^x$ |
| $\sqrt{a^2-x^2}$ | $x = a\sin t$ |
| $\sqrt{a^2+x^2}$ | $x = a\tan t$ |
| $\sqrt{x^2-a^2}$ | $x = a\sec t$ |

#### 3. 定积分分部积分法

**公式**：$\int_a^b u dv = [uv]_a^b - \int_a^b v du$

**与不定积分的区别**：
- 不定积分要加 $C$
- 定积分直接代入上下限

**$u$ 的选择口诀**："反、对、幂、指、三"

#### 4. 奇偶函数在对称区间上的积分

**偶函数**（$f(-x) = f(x)$）：
$$\int_{-a}^a f(x) dx = 2\int_0^a f(x) dx$$

**奇函数**（$f(-x) = -f(x)$）：
$$\int_{-a}^a f(x) dx = 0$$

**常见偶函数**：$x^2, \cos x, e^x + e^{-x}, |x|$
**常见奇函数**：$x, x^3, \sin x, \tan x, \arctan x$

**应用技巧**：非奇非偶函数可分解：
$$\int_{-a}^a f(x) dx = \int_{-a}^a \frac{f(x)+f(-x)}{2} dx = \int_0^a [f(x)+f(-x)] dx$$

#### 5. 区间再现公式

**公式**：$\int_a^b f(x) dx = \int_a^b f(a+b-x) dx$

**适用场景**：
- 计算 $\int_0^{\pi} x f(\sin x) dx$ 类型
- 建立 $I + I = ?$ 的方程

**经典应用**：$I = \int_0^{\pi} \frac{x \sin x}{1+\cos^2 x} dx$
- 设 $t = \pi - x$，得 $I = \int_0^{\pi} \frac{(\pi-x)\sin x}{1+\cos^2 x} dx$
- 两式相加：$2I = \pi \int_0^{\pi} \frac{\sin x}{1+\cos^2 x} dx$
- 解得 $I = \frac{\pi^2}{4}$

#### 6. 周期函数积分

**性质**：若 $f(x)$ 是周期为 $T$ 的函数：
$$\int_a^{a+T} f(x) dx = \int_0^T f(x) dx$$

**推论**：
$$\int_0^{nT} f(x) dx = n\int_0^T f(x) dx$$

#### 7. 常用定积分公式

**必须熟记**：

| 积分 | 值 |
|-----|---|
| $\int_0^{\pi/2} \sin^n x dx$ | $\frac{(n-1)!!}{n!!} \cdot \frac{\pi}{2}$（$n$ 偶） |
| $\int_0^{\pi/2} \sin^n x dx$ | $\frac{(n-1)!!}{n!!}$（$n$ 奇） |
| $\int_0^{\pi/2} \sin^n x dx = \int_0^{\pi/2} \cos^n x dx$ | 区间再现可证 |
| $\int_0^{\pi} x f(\sin x) dx$ | $\frac{\pi}{2}\int_0^{\pi} f(\sin x) dx$ |
| $\int_0^{\infty} e^{-x^2} dx$ | $\frac{\sqrt{\pi}}{2}$（高斯积分） |
| $\int_0^{\infty} \frac{\sin x}{x} dx$ | $\frac{\pi}{2}$ |

#### 8. 积分不等式与估值

**估值公式**：若 $m \leq f(x) \leq M$：
$$m(b-a) \leq \int_a^b f(x) dx \leq M(b-a)$$

**绝对值不等式**：
$$\left|\int_a^b f(x) dx\right| \leq \int_a^b |f(x)| dx$$

**Schwarz 不等式**：
$$\left(\int_a^b f(x)g(x) dx\right)^2 \leq \int_a^b f^2(x) dx \cdot \int_a^b g^2(x) dx$$

### 🎯 题型分类与对策

| 题型 | 特点 | 推荐方法 |
|-----|------|---------|
| 基本定积分 | 可直接找原函数 | 牛顿-莱布尼茨 |
| 换元积分 | 复合函数结构 | 换元法（注意换限） |
| 分部积分 | 乘积形式 | 分部积分法 |
| 对称区间 | $[-a, a]$ | 奇偶性分析 |
| 周期函数 | 含周期函数 | 周期性质 |
| 广义积分 | 无限限或无界函数 | 极限定义 |
| 变限积分 | 积分限含 $x$ | 微积分基本定理 |
| 证明题 | 不等式或等式证明 | 积分性质 + 技巧 |

## 易错点

**错误一**：换元不换限
- ❌ $\int_0^1 f(x^2) \cdot x dx = \frac{1}{2}\int_0^1 f(u) du$
- ✅ $\int_0^1 f(x^2) \cdot x dx = \frac{1}{2}\int_0^1 f(u) du$（$u = x^2$ 时，$x=0 \to u=0, x=1 \to u=1$，此例恰好不变）

**错误二**：奇偶性判断错误
- ❌ $\int_{-1}^1 x^2 \sin x dx \neq 0$（$x^2 \sin x$ 是奇函数，应为 0）
- ✅ $\int_{-1}^1 x^2 \sin x dx = 0$

**错误三**：广义积分忽略收敛性
- ❌ $\int_{-1}^1 \frac{1}{x} dx = [\ln|x|]_{-1}^1 = 0$
- ✅ $\int_{-1}^1 \frac{1}{x} dx$ 发散（瑕点在 $x=0$）

**错误四**：分部积分忘记代入上下限
- ❌ $\int_0^1 x e^x dx = xe^x - \int e^x dx$
- ✅ $\int_0^1 x e^x dx = [xe^x]_0^1 - \int_0^1 e^x dx$

## 10. 总结
### 10.1 重要定义

1. **定积分（黎曼积分）**：函数 $f(x)$ 在区间 $[a, b]$ 上的定积分定义为黎曼和的极限，表示曲线下的有向面积。
2. **黎曼和**：对于区间划分 $P = \{x_0, x_1, \ldots, x_n\}$，黎曼和 $R(f, P) = \sum_{i=1}^n f(\xi_i) \cdot (x_i - x_{i-1})$。
3. **达布和**：$L(f, P) = \sum m_i \Delta x_i$（下和），$U(f, P) = \sum M_i \Delta x_i$（上和）
4. **可积条件**：函数在闭区间上连续或有界且只有有限个间断点时可积；单调函数必可积。
5. **Lebesgue定理**：$f$ 可积 $\Leftrightarrow$ $\forall \varepsilon > 0, \exists P$ 使得 $U(f, P) - L(f, P) < \varepsilon$

### 10.2 重要定理

1. **微积分基本定理**：建立了定积分与导数之间的互逆关系，是积分学的核心定理。
   - 第一基本定理：$F(x) = \int_a^x f(t) dt$ 的导数 $F'(x) = f(x)$
   - 第二基本定理（牛顿-莱布尼茨公式）：$\int_a^b f(x) dx = F(b) - F(a)$

2. **积分第一中值定理**：存在 $c \in [a, b]$ 使得 $\int_a^b f(x) dx = f(c)(b-a)$。

3. **积分第二中值定理**：$f$ 可积，$g$ 单调，则存在 $\xi$ 使得 $\int_a^b f g = g(a)\int_a^\xi f + g(b)\int_\xi^b f$。

4. **积分不等式定理**：提供了积分的比较方法，是估计积分值的重要工具。

5. **含参量积分的可微性**：$\frac{d}{dx} \int_c^d f(x,t) dt = \int_c^d \frac{\partial f}{\partial x}(x,t) dt$。

6. **Riemann-Lebesgue引理**：若 $f$ 可积，则 $\lim_{p\to\infty} \int_a^b f(x)\sin(px) dx = 0$。

### 10.3 重要证明

1. **微积分基本定理的证明**：利用连续函数的性质和极限的定义，证明了积分函数的可导性。
2. **牛顿-莱布尼茨公式的证明**：基于第一基本定理，证明了任意原函数与积分函数的差为常数。
3. **积分中值定理的证明**：结合最值定理、积分不等式和介值定理，证明了积分中值的存在性。
4. **积分线性性的证明**：利用黎曼和的线性性质和极限的线性性质证明了积分的线性性。
5. **区间再现公式的证明**：通过变量替换 $t = a+b-x$，证明了 $\int_a^b f(x) dx = \int_a^b f(a+b-x) dx$。

### 10.4 重要性质

1. **线性性**：积分运算保持线性关系，$\int [\alpha f + \beta g] = \alpha \int f + \beta \int g$。
2. **区间可加性**：积分可以按区间分割，$\int_a^c f = \int_a^b f + \int_b^c f$。
3. **保序性**：函数的大小关系在积分中保持，$f \leq g \implies \int f \leq \int g$。
4. **绝对值不等式**：$|\int f| \leq \int |f|$，提供了积分的估计方法。
5. **对称性**：偶函数在对称区间上的积分等于两倍的正半区间积分，奇函数在对称区间上的积分为零。
6. **估值不等式**：$m(b-a) \leq \int_a^b f(x) dx \leq M(b-a)$，其中 $m \leq f(x) \leq M$。

### 10.5 积分技巧总结

1. **区间再现公式**：
   - 公式：$\int_a^b f(x) dx = \int_a^b f(a+b-x) dx$
   - 适用：被积函数含 $a+b-x$ 结构、计算 $\int_0^{\pi} x f(\sin x) dx$ 等

2. **偶倍奇零**：
   - 偶函数：$\int_{-a}^a f(x) dx = 2\int_0^a f(x) dx$
   - 奇函数：$\int_{-a}^a f(x) dx = 0$
   - 适用：对称区间 $[-a, a]$ 上的积分

3. **周期函数积分**：
   - 性质：$\int_a^{a+T} f(x) dx = \int_0^T f(x) dx$（$T$ 为周期）
   - 性质：$\int_0^{nT} f(x) dx = n \int_0^T f(x) dx$
   - 三角函数正交性：$\int_0^{2\pi} \sin mx \cdot \sin nx dx = \begin{cases} \pi & m=n\neq0 \\ 0 & m\neq n \end{cases}$

4. **常用技巧组合**：
   - 区间再现 + 对称性：处理含 $x$ 与 $\sin x$、$\cos x$ 乘积的积分
   - 分部积分 + 递推公式：计算 $\int_0^{\pi/2} \sin^n x dx$ 等

本章为后续学习多元积分、广义积分、微分方程等内容奠定了基础。定积分在概率统计、机器学习、物理、工程等领域有广泛应用。

## 自测（3问速测）

1. 我能解释为什么定积分本质上是“面积的极限”吗？
2. 我能在换元积分时同步换限并避免漏项吗？
3. 我能判断一个广义积分是收敛、条件收敛还是发散吗？

## 11. 练习（分层）
本节练习题参考以下教材：
- 《高等数学 上册 第八版》（同济大学数学科学院 编）第五章 定积分
- 《高等数学 下册 第八版》（同济大学数学科学学院 编）第十一章 无穷级数
- 《数学分析(第5版) 上》（华东师范大学数学系）第九章 定积分
- 《数学分析(第5版) 下》（华东师范大学数学系）第十五章 广义积分

### A档（基础）
1. 计算：∫₀¹x³dx（参考《高等数学 上册 第八版》第5章习题5-1第1题）
2. 计算：∫₀^π/2cosxdx（参考《数学分析(第5版) 上》第9章习题9-1第3题）
3. 计算：∫₋₁¹x²dx（参考《高等数学 上册 第八版》第5章习题5-1第2题）
4. 计算：∫₀^πsin²xdx（参考《数学分析(第5版) 上》第9章习题9-2第4题）
5. 计算：曲线y=x²在[0,1]上的面积（参考《高等数学 上册 第八版》第5章习题5-2第1题）

### B档（进阶）
1. 证明：微积分基本定理（参考《数学分析(第5版) 上》第9章定理9.1）
2. 计算广义积分：∫₀^∞e⁻ˣdx（参考《数学分析(第5版) 下》第15章习题15-1第2题）
3. 计算广义积分：∫₀¹1/√xdx（参考《数学分析(第5版) 下》第15章习题15-1第3题）
4. 证明：如果f在[a,b]上连续且非负，且∫ₐᵇf(x)dx=0，则f(x)=0（参考《数学分析(第5版) 上》第9章习题9-4第5题）
5. 利用积分中值定理证明：存在c∈[a,b]使得∫ₐᵇf(x)g(x)dx=f(c)∫ₐᵇg(x)dx（参考《高等数学 上册 第八版》第5章总习题第13题）

### C档（挑战）
1. 在机器学习中，如何使用定积分计算概率？（参考《数学分析(第5版) 下》第15章概率分布部分）
2. 证明：卷积函数的积分性质（参考《高等数学 下册 第八版》第10章傅里叶变换部分）
3. 研究：黎曼积分与勒贝格积分的区别（参考《数学分析(第5版) 下》第15章广义积分）
4. 计算高斯积分：∫₋∞^∞e⁻ˣ²dx（参考《数学分析(第5版) 下》第15章例15.3）
5. 应用：定积分方法解决一个机器学习中的实际问题（如计算期望、KL散度等）（参考《高等数学 下册 第八版》第10章应用部分）
6. 证明：若f在[a,b]上可积，则f几乎处处连续（Lebesgue定理）
7. 证明积分第二中值定理（参考《数学分析(第5版) 上》第9章定理9.16）
8. 证明：Riemann-Lebesgue引理（参考《数学分析(第5版) 下》第15章）
9. 讨论：∫₀^∞ sin(x)/x 的收敛性（条件收敛但非绝对收敛）
10. 研究：Gamma函数与Beta函数的关系及其在概率论中的应用





