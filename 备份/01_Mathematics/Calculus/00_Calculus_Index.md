---
type: index
subject: calculus
created: 2026-02-20
updated: 2026-04-27
status: complete
---

# 微积分 (Calculus)

## 速查

- [[../00_Symbols_Conventions|符号与约定总表]]

## 学习进度

### 第一部分：实数与极限基础
- [x] 01_Real_Numbers - 实数理论
- [x] 02_Limits - 极限
- [x] 03_Continuity - 连续性
- [x] 04_Uniform_Continuity - 一致连续性

### 第二部分：微分学
- [x] 05_Derivatives - 导数与微分
- [x] 06_Mean_Value_Theorem - 微分中值定理
- [x] 07_Taylor_Series - 泰勒公式
- [x] 08_Derivative_Applications - 导数的应用

### 第三部分：积分学
- [x] 09_Indefinite_Integrals - 不定积分
- [x] 10_Definite_Integrals - 定积分
- [x] 11_Variable_Limit_Integrals - 变限积分
- [x] 12_Improper_Integrals - 反常积分
- [x] 13_Integral_Applications - 积分的应用

### 第四部分：级数理论
- [x] 14_Series - 数项级数
- [x] 15_Function_Series - 函数项级数
- [x] 16_Power_Series - 幂级数
- [x] 17_Fourier_Series - 傅里叶级数

### 第五部分：多元微积分
- [x] 18_Multivariable_Limits - 多元函数极限与连续
- [x] 19_Partial_Derivatives - 偏导数与全微分
- [x] 20_Multivariable_Applications - 多元函数应用
- [x] 21_Multiple_Integrals - 重积分
- [x] 22_Curve_Integrals - 曲线积分
- [x] 23_Surface_Integrals - 曲面积分
- [x] 24_Vector_Calculus - 向量微积分

### 第六部分：应用专题
- [x] 25_Applications - 微积分应用

### 第七部分：微分方程
- [x] 27_Differential_Equations - 微分方程

### 第八部分：概念索引
- [x] 28_Concept_Index - 微积分概念索引

## 模块概览

微积分是数学的重要分支，研究函数的变化率和累积量。它是机器学习、物理、工程等领域的基础工具。本笔记基于以下经典教材编写：

- **《数学分析原理》** - Walter Rudin
- **《数学分析》（第5版）** - 华东师范大学数学系
- **《高等数学》（第八版）** - 同济大学数学科学学院
- **《托马斯微积分》（第十版）** - Thomas

## 学习进度

- **已完成**：28/28章节（100%）
- **状态**：✅ 完整

## 学习路径

1. **实数与极限基础** - 建立严格的数学基础
2. **微分学** - 理解瞬时变化率及其应用
3. **积分学** - 掌握累积理论及其应用
4. **级数理论** - 研究无限和的收敛性
5. **多元微积分** - 扩展到多维空间
6. **应用专题** - 将理论应用于实际问题
7. **微分方程** - 研究变化规律的数学工具
8. **概念索引** - 快速查找和导航工具

## 学习附件对照（高数 + 数分）

### 高数侧（同济/托马斯/吉米多维奇）
- **计算与题型训练**：极限计算、求导计算、积分技巧、级数判别
- **对应章节**：[[02_Limits]]、[[05_Derivatives]]、[[09_Indefinite_Integrals]]、[[10_Definite_Integrals]]、[[14_Series]]
- **建议用法**：每章先做 8-15 道典型题，再回看定理条件

### 数分侧（华师大/北大数分/Rudin）
- **定义与证明训练**：$\varepsilon$-$\delta$、一致收敛、可积判别、交换极限条件
- **对应章节**：[[02_Limits]]、[[15_Function_Series]]、[[16_Power_Series]]、[[17_Fourier_Series]]、[[26_Real_Analysis_Appendix]]
- **建议用法**：每章至少写 1 个“定理证明主线”与 1 个“反例”

### 章节补强优先级（已补）
1. [[02_Limits]]：高数五步法 + 数分严谨证明模板
2. [[05_Derivatives]]：求导题型树 + 可导与连续的区分反例
3. [[10_Definite_Integrals]]：积分估计与不等式专题
4. [[17_Fourier_Series]]：收敛点判定 + Parseval 应用

### 第七章：多元函数微分学目标映射
1. **欧式空间 / 点集拓扑** -> [[01_Real_Numbers]]、[[18_Multivariable_Limits]]
2. **多重极限 / 二重极限 / 累次极限** -> [[18_Multivariable_Limits]]
3. **多元连续性 / 有界闭域最值性质** -> [[18_Multivariable_Limits]]
4. **偏导数 / 高阶偏导数 / 全微分** -> [[19_Partial_Derivatives]]
5. **链式法则 / 隐函数求导** -> [[19_Partial_Derivatives]]、[[20_Multivariable_Applications]]
6. **极值 / Hessian / 拉格朗日乘数法** -> [[20_Multivariable_Applications]]

第七章的 8 项学习目标由 [[18_Multivariable_Limits]]、[[19_Partial_Derivatives]]、[[20_Multivariable_Applications]] 三章共同覆盖；其中第 1 项的点集与欧式空间预备由 [[01_Real_Numbers]] 提供支撑。

## 已完成笔记

### 第一部分：实数与极限基础
- [[01_Real_Numbers]] - 实数理论（Dedekind分割、确界原理、柯西准则）
- [[02_Limits]] - 极限的定义和计算（ε-δ定义、连续性、极限计算）
- [[03_Continuity]] - 连续性（介值定理、极值定理、一致连续）
- [[04_Uniform_Continuity]] - 一致连续性（Cantor定理、Lipschitz条件）

### 第二部分：微分学
- [[05_Derivatives]] - 导数和微分（定义、计算、链式法则、应用）
- [[06_Mean_Value_Theorem]] - 微分中值定理（罗尔、拉格朗日、柯西、洛必达）
- [[07_Taylor_Series]] - 泰勒公式（展开、收敛半径、常用函数）
- [[08_Derivative_Applications]] - 导数的应用（单调性、极值、凹凸性、作图）

### 第三部分：积分学
- [[09_Indefinite_Integrals]] - 不定积分（基本公式、凑微分、分部积分、换元法）
- [[10_Definite_Integrals]] - 定积分（黎曼和、微积分基本定理、应用）
- [[11_Variable_Limit_Integrals]] - 变限积分（积分上限函数、微积分基本定理）
- [[12_Improper_Integrals]] - 反常积分（无穷区间、无界函数、收敛判别法）
- [[13_Integral_Applications]] - 积分的应用（面积、体积、弧长、物理应用）

### 第四部分：级数理论
- [[14_Series]] - 数项级数（收敛性判别法、绝对收敛、条件收敛）
- [[15_Function_Series]] - 函数项级数（一致收敛、M判别法）
- [[16_Power_Series]] - 幂级数（收敛半径、展开、应用）
- [[17_Fourier_Series]] - 傅里叶级数（系数计算、收敛定理）

### 第五部分：多元微积分
- [[18_Multivariable_Limits]] - 多元函数极限与连续（极限定义、连续性）
- [[19_Partial_Derivatives]] - 偏导数与全微分（梯度、方向导数、链式法则）
- [[20_Multivariable_Applications]] - 多元函数应用（极值、条件极值、最值）
- [[21_Multiple_Integrals]] - 重积分（二重积分、三重积分、变量代换）
- [[22_Curve_Integrals]] - 曲线积分（第一类、第二类、格林公式）
- [[23_Surface_Integrals]] - 曲面积分（第一类、第二类、高斯公式、斯托克斯公式）
- [[24_Vector_Calculus]] - 向量微积分（梯度、散度、旋度、场论）

### 第六部分：应用专题
- [[25_Applications]] - 微积分应用（物理、工程、机器学习案例）

### 第七部分：微分方程
- [[27_Differential_Equations]] - 微分方程（常微分方程、偏微分方程、求解方法与应用）

### 第八部分：附录
- [[26_Real_Analysis_Appendix]] - 实分析初步（测度论、Lebesgue积分、L^p空间）

### 第九部分：概念索引
- [[28_Concept_Index]] - 微积分概念索引（按字母顺序排列的核心概念）

## 相关链接

- [[00_Linear_Algebra_Index|线性代数]] - 多元微积分的基础
- [[00_Probability_Index|概率统计]] - 积分在概率中的应用
- [[00_Optimization_Index|优化理论]] - 导数和积分的应用

---

**创建时间：2026年2月20日**  
**最后更新：2026年4月27日**
**总笔记数：28章（完整）**
