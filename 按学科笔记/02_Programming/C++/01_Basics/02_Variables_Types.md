---
type: concept
topic: Variables and Types
category: basics
difficulty: 入门
prerequisites: [[01_Basic_Syntax]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 2.0
practice_problems: 5
ml_relevance: high
cpp_standard: 11
tags: [编程/C++, 基础/数据类型, ACM/基础, ML/数据结构]
---

# 变量与数据类型 (Variables and Types)

> C++ 中的变量用于存储数据，数据类型决定了变量的内存大小和可执行的操作

## 📌 核心定义

变量是程序中用于存储数据的命名内存位置。数据类型定义了变量可以存储的数据种类、占用内存大小以及可以执行的操作。

## 💡 直觉理解

可以把变量想象成容器：
- 数据类型 = 容器的类型（杯子、碗、桶）
- 变量名 = 容器的标签
- 变量值 = 容器中存放的东西

## 📖 详细说明

### 1. 基本数据类型

| 类型 | 说明 | 大小（字节） | 范围 |
|------|------|-------------|------|
| int | 整数 | 4 | -2,147,483,648 到 2,147,483,647 |
| float | 单精度浮点数 | 4 | 约 ±3.4e38 |
| double | 双精度浮点数 | 8 | 约 ±1.8e308 |
| char | 字符 | 1 | -128 到 127 |
| bool | 布尔值 | 1 | true 或 false |

### 2. 变量声明与初始化

```cpp
int age = 20;
double pi = 3.14159;
char grade = 'A';
bool is_student = true;
```

## 💻 代码示例

### 示例 1: 基本类型使用

```cpp
#include <iostream>

int main() {
    int integer = 42;
    double pi = 3.14159;
    char grade = 'A';
    bool is_student = true;
    
    std::cout << "Integer: " << integer << std::endl;
    std::cout << "Double: " << pi << std::endl;
    std::cout << "Char: " << grade << std::endl;
    std::cout << "Bool: " << is_student << std::endl;
    
    return 0;
}
```

### 示例 2: 类型大小检测

```cpp
#include <iostream>

int main() {
    std::cout << "Size of int: " << sizeof(int) << " bytes" << std::endl;
    std::cout << "Size of double: " << sizeof(double) << " bytes" << std::endl;
    std::cout << "Size of char: " << sizeof(char) << " bytes" << std::endl;
    
    return 0;
}
```

## 🎯 应用场景

### 机器学习中的应用
- 特征存储: 使用 double 保证精度
- 标签类型: 分类用 int，回归用 double
- 模型参数: 使用 double 类型

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| 初始化变量 | 始终初始化变量 |
| 整数溢出 | 大数运算时检查是否溢出 |
| 浮点精度 | 比较浮点数时使用误差范围 |

## 🔗 相关概念

- [[01_Basic_Syntax]] - C++ 基本语法
- [[03_Operators]] - 运算符

## 📝 练习题

1. 编写程序输出不同类型变量的大小
2. 编写程序计算圆的面积和周长

## 📚 参考资料

- [C++ Reference - Fundamental Types](https://en.cppreference.com/w/cpp/language/types)

## 🔄 待补充
- [ ] 添加更多类型转换示例
- [ ] 添加 auto 关键字说明
