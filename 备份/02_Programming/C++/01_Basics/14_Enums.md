---
type: concept
topic: Enums
category: basics
difficulty: 入门
prerequisites: [[13_Struct_Union]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 1.0
practice_problems: 2
ml_relevance: low
cpp_standard: 11
tags: [编程/C++, 基础/枚举, ACM/基础]
---

# 枚举类型 (Enums)

> 枚举类型用于定义一组命名的整型常量，提高代码的可读性

## 📌 核心定义

枚举（enumeration）是一种用户定义类型，包含一组命名的整型常量。C++11 引入了 enum class，提供了更强的类型安全性。

## 💡 直觉理解

枚举就像"标签系统"：
- 每个枚举值 = 一个带名字的标签
- 标签背后 = 一个整数值
- 好处 = 使用名字而非数字，代码更清晰

## 📖 详细说明

### 1. C 风格枚举

```cpp
enum Color {
    RED,
    GREEN,
    BLUE
};  // RED=0, GREEN=1, BLUE=2
```
### 2. C++11 枚举类（推荐）

```cpp
enum class Color {
    RED,
    GREEN,
    BLUE
};  // 作用域受限，类型安全
```
### 3. 指定值

```cpp
enum class Status {
    PENDING = 0,
    RUNNING = 1,
    COMPLETED = 2
};
```
## 💻 代码示例

### 示例 1: 枚举基本使用

```cpp
#include <iostream>

enum class Color {
    RED,
    GREEN,
    BLUE
};

int main() {
    Color myColor = Color::BLUE;
    
    if (myColor == Color::BLUE) {
        std::cout << "The color is blue" << std::endl;
    }
    
    return 0;
}
```
### 示例 2: 开关状态（ACM 常用）

```cpp
#include <iostream>

enum class Direction {
    UP,
    DOWN,
    LEFT,
    RIGHT
};

void move(Direction dir) {
    switch (dir) {
        case Direction::UP:
            std::cout << "Moving up" << std::endl;
            break;
        case Direction::DOWN:
            std::cout << "Moving down" << std::endl;
            break;
        case Direction::LEFT:
            std::cout << "Moving left" << std::endl;
            break;
        case Direction::RIGHT:
            std::cout << "Moving right" << std::endl;
            break;
    }
}

int main() {
    move(Direction::UP);
    move(Direction::RIGHT);
    
    return 0;
}
```
### 示例 3: 机器学习中的应用

```cpp
#include <iostream>

enum class ActivationType {
    RELU,
    SIGMOID,
    TANH,
    SOFTMAX
};

std::string getActivationName(ActivationType type) {
    switch (type) {
        case ActivationType::RELU: return "ReLU";
        case ActivationType::SIGMOID: return "Sigmoid";
        case ActivationType::TANH: return "Tanh";
        case ActivationType::SOFTMAX: return "Softmax";
    }
}

int main() {
    ActivationType activation = ActivationType::RELU;
    std::cout << "Using: " << getActivationName(activation) << std::endl;
    
    return 0;
}
```
## 🎯 应用场景

### ACM 竞赛中的应用
- 方向控制：上下左右
- 状态管理：状态机
- 游戏开发：角色属性

### 机器学习中的应用
- 激活函数类型
- 优化器类型
- 损失函数类型

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| enum class | 推荐，类型安全 |
| 隐式转换 | enum class 不支持隐式转换 |
| 作用域 | enum class 需要限定作用域 |
| 整型值 | 枚举值的底层数据类型 |

## 🔗 相关概念

- [[13_Struct_Union]] - 结构体与联合体

## 📝 练习题

1. 编写程序使用枚举表示星期
2. 理解 enum 和 enum class 的区别

## 📚 参考资料

- [C++ Reference - Enumeration](https://en.cppreference.com/w/cpp/language/enum)
