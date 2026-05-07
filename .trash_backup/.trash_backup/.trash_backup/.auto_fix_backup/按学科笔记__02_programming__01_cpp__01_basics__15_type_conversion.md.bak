---
type: concept
topic: Type Conversion
category: basics
difficulty: 基础
prerequisites: [[02_Variables_Types]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 1.5
practice_problems: 4
ml_relevance: medium
cpp_standard: 11
tags: [编程/C++, 基础/类型转换, ACM/基础]
---

# 类型转换 (Type Conversion)

> 类型转换是将一种类型的值转换为另一种类型的过程

## 📌 核心定义

C++ 支持多种类型转换方式：隐式转换（自动）、显式转换（C风格）和 C++ 风格的转换（static_cast, dynamic_cast, const_cast, reinterpret_cast）。

## 💡 直觉理解

类型转换就像"换包装"：
- 将物品从一种包装换成另一种包装
- 有时自动完成（隐式）
- 有时需要手动指定（显式）

## 📖 详细说明

### 1. 隐式转换

```cpp
int i = 42;
double d = i;  // int 自动转换为 double
```
### 2. C 风格显式转换

```cpp
double pi = 3.14159;
int int_pi = (int)pi;  // 截断为 3
```
### 3. C++ 风格转换（推荐）

| 转换 | 用途 |
|------|------|
| static_cast | 相关类型之间的转换 |
| const_cast | 添加或移除 const |
| reinterpret_cast | 不相关类型的转换 |
| dynamic_cast | 运行时类型检查（多态） |

## 💻 代码示例

### 示例 1: 隐式转换

```cpp
#include <iostream>

int main() {
    int i = 10;
    double d = i;  // 隐式转换
    
    std::cout << "int: " << i << std::endl;
    std::cout << "double: " << d << std::endl;
    
    return 0;
}
```
### 示例 2: static_cast

```cpp
#include <iostream>

int main() {
    double d = 3.14159;
    int i = static_cast<int>(d);  // 显式转换
    
    std::cout << "Original: " << d << std::endl;
    std::cout << "Converted: " << i << std::endl;
    
    return 0;
}
```
### 示例 3: 指针转换

```cpp
#include <iostream>

int main() {
    int x = 42;
    double* dp = static_cast<double*>(&x);
    
    // 注意：这可能不是你想要的
    std::cout << "Address: " << dp << std::endl;
    
    return 0;
}
```
### 示例 4: 常见陷阱

```cpp
#include <iostream>

int main() {
    // 陷阱 1: 整数除法
    int a = 5, b = 2;
    std::cout << "5 / 2 = " << (a / b) << std::endl;  // 2
    
    // 正确做法
    std::cout << "5.0 / 2 = " << (5.0 / 2) << std::endl;  // 2.5
    
    // 陷阱 2: 精度损失
    double pi = 3.141592653589793;
    int int_pi = static_cast<int>(pi);
    std::cout << "Truncated: " << int_pi << std::endl;  // 3
    
    return 0;
}
```
## 🎯 应用场景

### ACM 竞赛中的应用
- 数学计算：确保正确的类型
- 坐标处理：浮点数与整数转换

### 机器学习中的应用
- 数据归一化：转换数据类型
- 精度控制：float vs double

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| 精度损失 | 浮点数转整数会截断小数部分 |
| 范围检查 | 确保目标类型能表示转换后的值 |
| 指针转换 | 指针转换需要格外小心 |
| dynamic_cast | 需要虚函数支持 |

## 🔗 相关概念

- [[02_Variables_Types]] - 变量与数据类型
- [[06_Pointers]] - 指针

## 📝 练习题

1. 编写程序演示各种类型转换
2. 理解 static_cast 的正确用法

## 📚 参考资料

- [C++ Reference - Type Conversions](https://en.cppreference.com/w/cpp/language/implicit_conversion)
