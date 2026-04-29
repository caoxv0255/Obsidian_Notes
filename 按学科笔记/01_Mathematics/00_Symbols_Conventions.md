---
type: reference
subject: mathematics
created: 2026-04-22
updated: 2026-04-22
status: active
---

# 符号与约定总表 (Symbols & Conventions)

> 目标：统一各分支书写风格，减少“看得懂但对不上符号”的摩擦。

## 0. 通用

- 集合：$\mathbb{N},\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$
- 指示函数：$\mathbf{1}_A$ 表示事件/条件 $A$ 成立时取 1，否则取 0
- 渐近：$O(\cdot)$、$o(\cdot)$ 按 $n\to\infty$ 或 $x\to a$ 的上下文说明
- 约定：默认“向量是列向量”，除非特别声明

## 1. 线性代数

- 向量：$\mathbf{x},\mathbf{v}\in\mathbb{R}^n$
- 矩阵：$A\in\mathbb{R}^{m\times n}$；单位矩阵 $I$
- 转置：$A^T$；逆：$A^{-1}$（要求可逆）
- 内积：$\langle \mathbf{x},\mathbf{y}\rangle$；二范数：$\|\mathbf{x}\|_2$
- 特征对：$A\mathbf{v}=\lambda\mathbf{v}$；特征值 $\lambda$，特征向量 $\mathbf{v}$
- 半正定：$X\succeq 0$（PSD），$X\succ 0$（PD）
- 常用分解：QR、SVD：$A=U\Sigma V^T$

## 2. 微积分

- 极限：$\lim_{x\to a} f(x)$；数列极限：$\lim_{n\to\infty} a_n$
- 导数：$f'(x)$ 或 $\frac{df}{dx}$；高阶：$f^{(k)}(x)$
- 梯度：$\nabla f(\mathbf{x})$；Hessian：$\nabla^2 f(\mathbf{x})$
- 积分：不定积分 $\int f(x)\,dx$；定积分 $\int_a^b f(x)\,dx$

## 3. 概率论

- 随机变量：$X,Y$（大写）；取值：$x,y$（小写）
- 分布：$X\sim \mathcal{N}(\mu,\sigma^2)$；分布函数：$F_X(x)$；密度：$f_X(x)$
- 概率：$\mathbb{P}(A)$；条件概率：$\mathbb{P}(A\mid B)$
- 期望：$\mathbb{E}[X]$；方差：$\mathrm{Var}(X)$
- 条件期望：$\mathbb{E}[X\mid Y]$（随机变量/函数）
- 收敛：
  - 依分布：$X_n\xrightarrow{d}X$
  - 依概率：$X_n\xrightarrow{p}X$
  - 几乎处处：$X_n\xrightarrow{a.s.}X$

## 4. 优化

- 优化问题：$\min_x f(x)$ s.t. $g_i(x)\le 0,\ h_j(x)=0$
- 可行域：$\mathcal{X}$；最优解：$x^*$；最优值：$p^*=f(x^*)$
- 光滑常数：$L$（梯度 Lipschitz）；强凸参数：$\mu$
- 条件数：$\kappa=\frac{L}{\mu}$（强凸光滑时）
- 对偶：拉格朗日函数 $L(x,\lambda,\nu)$；对偶函数 $g(\lambda,\nu)$
- 不等式（锥）：$x\preceq_K y \Leftrightarrow y-x\in K$

## 5. 章节书写约定（强烈建议）

- 每章 YAML 里用 `prerequisites` 作为列表：
  - `prerequisites:`
  - `  - [[02_Limits]]`
  - `  - [[03_Continuity]]`
- 难度分层统一用：**基础 / 进阶 / 拓展**
- 练习分层统一用：**A档（熟练）/ B档（辨析）/ C档（证明/推导）**
