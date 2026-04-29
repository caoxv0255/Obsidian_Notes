---
type: concept
topic: Operators
category: basics
difficulty: 入门
prerequisites: [[02_Variables_Types]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 1.5
practice_problems: 4
ml_relevance: medium
cpp_standard: 11
tags: [编程/C++, 基础/运算符, ACM/基础]
---

# 运算符 (Operators)

> 运算符用于执行各种运算操作，包括算术、关系、逻辑和位运算

## 📌 核心定义

运算符是告诉编译器执行特定数学或逻辑操作的符号。C++ 提供了丰富的运算符，包括算术、关系、逻辑、位运算、赋值等。

## 💡 直觉理解

运算符就像计算器上的按钮：
- 算术运算符 = + - × ÷
- 关系运算符 = 比较（大于、小于、等于）
- 逻辑运算符 = 且、或、非
- 位运算符 = 二进制位的操作

## 📖 详细说明

### 1. 算术运算符

| 运算符 | 名称 | 示例 |
|--------|------|------|
| + | 加法 | a + b |
| - | 减法 | a - b |
| * | 乘法 | a * b |
| / | 除法 | a / b |
| % | 取模 | a % b |
| ++ | 自增 | a++ |
| -- | 自减 | a-- |

### 2. 关系运算符

| 运算符 | 名称 | 示例 |
|--------|------|------|
| == | 等于 | a == b |
| != | 不等于 | a != b |
| > | 大于 | a > b |
| < | 小于 | a < b |
| >= | 大于等于 | a >= b |
| <= | 小于等于 | a <= b |

### 3. 逻辑运算符

| 运算符  | 名称  | 示例       |
| ---- | --- | -------- |
| &&   | 逻辑与 | a && b   |
| \|\| | 逻辑或 | a \|\| b |
| !    | 逻辑非 | !a       |

### 4. 位运算符（详细讲解）

位运算符直接对整数的二进制位进行操作，是计算机底层运算的基础。

#### 位运算符详解

| 运算符 | 名称 | 逻辑 | 运算规则 |
|--------|------|------|----------|
| **&** | 按位与 | AND | 对应位都为 1 时结果为 1，否则为 0 |
| **\|** | 按位或 | OR | 对应位有一个为 1 时结果为 1，否则为 0 |
| **^** | 按位异或 | XOR | 对应位不同时结果为 1，相同时为 0 |
| **~** | 按位取反 | NOT | 每一位取反（0 变 1，1 变 0） |
| **<<** | 左移 | Left Shift | 所有位向左移动，右边补 0 |
| **>>** | 右移 | Right Shift | 所有位向右移动，左边补符号位 |

#### 位运算的详细运算过程

##### 1. 按位与（&）运算

**规则**：对应位都为 1 时结果为 1，否则为 0

```
示例：5 & 3
  5 = 0101 (二进制)
  3 = 0011 (二进制)
  ---------
结果 = 0001 = 1 (十进制)

详细过程：
- 第 0 位（最低位）：1 & 1 = 1
- 第 1 位：0 & 1 = 0
- 第 2 位：1 & 0 = 0
- 第 3 位（最高位）：0 & 0 = 0
```

**应用**：检查某一位是否为 1

```cpp
int num = 13;  // 二进制：1101
int mask = 8;   // 二进制：1000
if (num & mask) {
    // 第 3 位为 1
}
```

##### 2. 按位或（|）运算

**规则**：对应位有一个为 1 时结果为 1，否则为 0

```
示例：5 | 3
  5 = 0101 (二进制)
  3 = 0011 (二进制)
  ---------
结果 = 0111 = 7 (十进制)

详细过程：
- 第 0 位：1 | 1 = 1
- 第 1 位：0 | 1 = 1
- 第 2 位：1 | 0 = 1
- 第 3 位：0 | 0 = 0
```

**应用**：设置某一位为 1

```cpp
int num = 10;  // 二进制：1010
int mask = 4;   // 二进制：0100
int result = num | mask;  // 结果：1110 = 14
```

##### 3. 按位异或（^）运算

**规则**：对应位不同时结果为 1，相同时为 0

```
示例：5 ^ 3
  5 = 0 1 0 1 (二进制)
  3 = 0 0 1 1 (二进制)
  ---------
结果 = 0 1 1 0 = 6 (十进制)

详细过程：
- 第 0 位：1 ^ 1 = 0
- 第 1 位：0 ^ 1 = 1
- 第 2 位：1 ^ 0 = 1
- 第 3 位：0 ^ 0 = 0
```

**重要特性**：`a ^ a = 0`，`a ^ 0 = a`

**应用**：交换两个数（无需临时变量）

```cpp
int a = 5, b = 3;
a = a ^ b;  // a = 6, b = 3
b = a ^ b;  // a = 6, b = 5
a = a ^ b;  // a = 3, b = 5
// 现在 a=3, b=5，完成了交换
```

##### 4. 按位取反（~）运算

**规则**：每一位取反

```
示例：~5
  5 = 0000 0101 (假设 8 位整数)
  ~5 = 1111 1010 = -6 (十进制，补码表示)

详细过程：
- 原值：0000 0101
- 取反：1111 1010
- 这是 -6 的补码表示
```

**应用**：生成掩码、快速取反

```cpp
unsigned int mask = ~0;  // 所有位都为 1
unsigned int inverted = ~mask;  // 所有位都为 0
```

##### 5. 左移（<<）运算

**规则**：所有位向左移动 n 位，右边补 n 个 0

```
示例：5 << 2
  5 = 0000 0101 (假设 8 位整数)
  5 << 2 = 0001 0100 = 20 (十进制)

详细过程：
- 原值：0000 0101
- 左移 2 位：0001 0100
- 左移 1 位：0000 1010 = 10
- 左移 2 位：0001 0100 = 20

数学等价：a << n = a × 2^n
```

**应用**：快速乘法、设置标志位

```cpp
int num = 5;
int result = num << 3;  // 5 × 2³ = 5 × 8 = 40
```

##### 6. 右移（>>）运算

**规则**：所有位向右移动 n 位，左边补符号位

```
示例：5 >> 1
  5 = 0000 0101 (假设 8 位整数)
  5 >> 1 = 0000 0010 = 2 (十进制)

详细过程：
- 原值：0000 01 01
- 右移 1 位：0000 0010
- 丢弃最右边位：1
- 左边补 0：0000 0010

数学等价：a >> n = a ÷ 2^n（整数除法）
```

**应用**：快速除法、提取某一位

```cpp
int num = 20;  // 二进制：0001 0100
int bit0 = num & 1;  // 提取第 0 位
int bit1 = (num >> 1) & 1;  // 提取第 1 位
int bit2 = (num >> 2) & 1;  // 提取第 2 位
int bit3 = (num >> 3) & 1;  // 提取第 3 位
```

#### 位运算的优先级

从高到低：
1. `~`（按位取反）
2. `<<`、`>>`（移位）
3. `&`（按位与）
4. `^`（按位异或）
5. `|`（按位或）

## 💻 代码示例

### 示例 1：算术运算符

```cpp
#include <iostream>

int main() {
    int a = 10, b = 3;
    
    std::cout << "a + b = " << (a + b) << std::endl;
    std::cout << "a - b = " << (a - b) << std::endl;
    std::cout << "a * b = " << (a * b) << std::endl;
    std::cout << "a / b = " << (a / b) << std::endl;
    std::cout << "a % b = " << (a % b) << std::endl;
    
    return 0;
}
```

### 示例 2：位运算符详解（ACM 常用）

```cpp
#include <iostream>
#include <bitset>

int main() {
    int a = 5, b = 3;
    
    std::cout << "=== 位运算详解 ===" << std::endl;
    std::cout << "a = " << a << " (二进制: " << std::bitset<8>(a) << ")" << std::endl;
    std::cout << "b = " << b << " (二进制: " << std::bitset<8>(b) << ")" << std::endl;
    std::endl;
    
    // 按位与
    int and_result = a & b;
    std::cout << "a & b = " << and_result << " (二进制: " << std::bitset<8>(and_result) << ")" << std::endl;
    std::cout << "  解释：" << std::bitset<8>(a) << " & " << std::bitset<8>(b) << " = " << std::bitset<8>(and_result) << std::endl;
    std::endl;
    
    // 按位或
    int or_result = a | b;
    std::cout << "a | b = " << or_result << " (二进制: " << std::bitset<8>(or_result) << ")" << std::endl;
    std::cout << "  解释：" << std::bitset<8>(a) << " | " << std::bitset<8>(b) << " = " << std::bitset<8>(or_result) << std::endl;
    std::endl;
    
    // 按位异或
    int xor_result = a ^ b;
    std::cout << "a ^ b = " << xor_result << " (二进制: " << std::bitset<8>(xor_result) << ")" << std::endl;
    std::cout << "  解释：" << std::bitset<8>(a) << " ^ " << std::bitset<8>(b) << " = " << std::bitset<8>(xor_result) << std::endl;
    std::endl;
    
    // 按位取反
    int not_result = ~a;
    std::cout << "~a = " << not_result << " (二进制: " << std::bitset<8>(not_result) << ")" << std::endl;
    std::cout << "  解释：" << std::bitset<8>(a) << " ~ = " << std::bitset<8>(not_result) << std::endl;
    std::endl;
    
    // 左移
    std::cout << "a << 1 = " << (a << 1) << " (二进制: " << std::bitset<8>(a << 1) << ")" << std::endl;
    std::cout << "  解释：" << std::bitset<8>(a) << " << 1 = " << std::bitset<8>(a << 1) << " (相当于 ×2)" << std::endl;
    std::cout << "a << 2 = " << (a << 2) << " (二进制: " << std::bitset<8>(a << 2) << ")" << std::endl;
    std::cout << "  解释：" << std::bitset<8>(a) << " << 2 = " << std::bitset<8>(a << 2) << " (相当于 ×4)" << std::endl;
    std::endl;
    
    // 右移
    std::cout << "a >> 1 = " << (a >> 1) << " (二进制: " << std::bitset<8>(a >> 1) << ")" << std::endl;
    std::cout << "  解释：" << std::bitset<8>(a) << " >> 1 = " << std::bitset<8>(a >> 1) << " (相当于 ÷2)" << std::endl;
    std::cout << "a >> 2 = " << (a >> 2) << " (二进制: " << std::bitset<8>(a >> 2) << ")" << std::endl;
    std::cout << "  解释：" << std::bitset<8>(a) << " >> 2 = " << std::bitset<8>(a >> 2) << " (相当于 ÷4)" << std::endl;
    
    return 0;
}
```

### 示例 3：位运算的实用技巧

```cpp
#include <iostream>
#include <bitset>

int main() {
    int num = 21;  // 二进制：0001 0101
    
    std::cout << "num = " << num << " (二进制: " << std::bitset<8>(num) << ")" << std::endl;
    
    // 技巧 1：判断奇偶
    if (num & 1) {
        std::cout << "num 是奇数（最低位为 1）" << std::endl;
    } else {
        std::cout << "num 是偶数（最低位为 0）" << std::endl;
    }
    
    // 技巧 2：判断是否为 2 的幂
    bool isPowerOfTwo = (num & (num - 1)) == 0;
    std::cout << "num " << (isPowerOfTwo ? "是" : "不是") << " 2 的幂" << std::endl;
    
    // 技巧 3：提取特定位
    int bit0 = (num >> 0) & 1;
    int bit1 = (num >> 1) & 1;
    int bit2 = (num >> 2) & 1;
    int bit3 = (num >> 3) & 1;
    int bit4 = (num >> 4) & 1;
    
    std::cout << "二进制位分解：" << std::bitset<8>(num) << std::endl;
    std::cout << "第 0 位: " << bit0 << std::endl;
    std::cout << "第 1 位: " << bit1 << std::endl;
    std::cout << "第 2 位: " << bit2 << std::endl;
    std::cout << "第 3 位: " << bit3 << std::endl;
    std::cout << "第 4 位: " << bit4 << std::endl;
    
    // 技巧 4：设置某一位为 1
    int num2 = num | (1 << 2);  // 设置第 2 位为 1
    std::cout << "设置第 2 位为 1: " << num2 << " (二进制: " << std::bitset<8>(num2) << ")" << std::endl;
    
    // 技巧 5：清除某一位
    int num3 = num & ~(1 << 2);  // 清除第 2 位
    std::cout << "清除第 2 位: " << num3 << " (二进制: " << std::bitset<8>(num3) << ")" << std::endl;
    
    // 技巧 6：翻转某一位
    int num4 = num ^ (1 << 2);  // 翻转第 2 位
    std::cout << "翻转第 2 位: " << num4 << " (二进制: " << std::bitset<8>(num4) << ")" << std::endl;
    
    return 0;
}
```

### 示例 4：位运算的数学性质

```cpp
#include <iostream>
#include <bitset>

int main() {
    int a = 12, b = 10;
    
    std::cout << "=== 位运算的数学性质 ===" << std::endl;
    std::cout << "a = " << a << " (二进制: " << std::bitset<8>(a) << ")" << std::endl;
    std::cout << "b = " << b << " (二进制: " << std::bitset<8>(b) << ")" << std::endl;
    std::endl;
    
    // 交换律
    std::cout << "交换律：" << std::endl;
    std::cout << "a | b = " << (a | b) << " = " << (b | a) << std::endl;
    std::cout << "a & b = " << (a & b) << " = " << (b & a) << std::endl;
    std::cout << "a ^ b = " << (a ^ b) << " = " << (b ^ a) << std::endl;
    std::endl;
    
    // 结合律
    std::cout << "结合律：" << std::endl;
    std::cout << "(a | b) | c = a | (b | c)" << std::endl;
    std::cout << "(a & b) & c = a & (b & c)" << std::endl;
    std::endl;
    
    // 分配律
    std::cout << "分配律：" << std::endl;
    std::cout << "a & (b | c) = (a & b) | (a & c)" << std::endl;
    std::cout << "a | (b & c) = (a | b) & (a | c)" << std::endl;
    
    return 0;
}
```

## 🎯 应用场景

### ACM 竞赛中的应用
- 位运算优化：快速幂、状态压缩
- 判断奇偶：使用 & 1
- 快速乘除：使用 << 和 >>

## ⚠️ 注意事项

| 注意事项  | 说明            |
| ----- | ------------- |
| 整数除法  | 两个整数相除结果仍是整数  |
| 自增自减  | ++a 和 a++ 的区别 |
| 位运算   | 只对整数有效        |
| 运算优先级 | 注意运算符的优先级     |

## 🔗 相关概念

- [[02_Variables_Types]] - 变量与数据类型
- [[04_Control_Flow]] - 控制流

## 📝 练习题

1. 编写程序计算两个数的和、差、积、商
2. 使用位运算判断一个数是否为 2 的幂
3. 实现不使用临时变量交换两个数
4. 使用位运算计算整数绝对值

## 📚 参考资料

- [C++ Reference - Operators](https://en.cppreference.com/w/cpp/language/operators)

## 🔧 位运算高级技巧

### 快速幂算法（使用位运算优化）

```cpp
int fastPower(int base, int exponent) {
    int result = 1;
    while (exponent > 0) {
        if (exponent & 1) {
            result *= base;
        }
        base *= base;
        exponent >>= 1;
    }
    return result;
}

// 示例：2^10 = 1024
// 过程：exponent = 10(1010) -> 1(0001) -> 0(0000)
// result = 1 × 2² × 2⁸ = 4 × 256 = 1024
```

### 子集枚举（状态压缩）

```cpp
void enumerateSubsets(int n) {
    for (int mask = 0; mask < (1 << n); mask++) {
        // 遍历所有 2^n 个子集
        std::cout << "Subset " << mask << ": ";
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                std::cout << i << " ";
            }
        }
        std::cout << std::endl;
    }
}
// 对于 n=3，会遍历 0 到 7（000 到 111）
```

### 判断最低位的 1

```cpp
int getLowestSetBit(int x) {
    return x & (-x);
}

// 示例：x = 12 (1100)
// -x = ~x + 1 = 0011 + 1 = 0100 = 4
// 12 & 4 = 4 (0100)，即最低位的 1 在第 2 位
```
