---
type: concept
topic: Struct and Union
category: basics
difficulty: 基础
prerequisites: [[02_Variables_Types]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 2.0
practice_problems: 4
ml_relevance: medium
cpp_standard: 11
tags: [编程/C++, 基础/结构体, ACM/基础, ML/数据结构]
---

# 结构体与联合体 (Struct and Union)

> 结构体和联合体允许将不同类型的数据组合成一个自定义类型

## 📌 核心定义

结构体（struct）是将不同类型的数据组合在一起的用户自定义类型。联合体（union）允许在同一内存位置存储不同类型的数据，但同时只能使用其中一种。

## 💡 直觉理解

- **结构体** = 一个"包裹"，里面可以放不同类型的东西
- **联合体** = 一个"魔盒"，同一时间只能放一样东西

## 📖 详细说明

### 1. 结构体

```cpp
struct Student {
    int id;
    std::string name;
    int age;
    double score;
};
```
### 2. 联合体

```cpp
union Data {
    int i;
    float f;
    char c;
};
```
### 3. 位域

```cpp
struct Flags {
    unsigned int flag1 : 1;
    unsigned int flag2 : 3;
    unsigned int flag3 : 4;
};
```
## 💻 代码示例

### 示例 1: 结构体基本使用

```cpp
#include <iostream>
#include <string>

struct Point {
    double x;
    double y;
};

int main() {
    Point p1;
    p1.x = 3.14;
    p1.y = 2.71;
    
    std::cout << "Point: (" << p1.x << ", " << p1.y << ")" << std::endl;
    
    return 0;
}
```
### 示例 2: 结构体数组

```cpp
#include <iostream>
#include <string>

struct Student {
    int id;
    std::string name;
    double score;
};

int main() {
    Student students[3] = {
        {1, "Alice", 95.5},
        {2, "Bob", 87.0},
        {3, "Charlie", 92.5}
    };
    
    for (int i = 0; i < 3; i++) {
        std::cout << students[i].name << ": " << students[i].score << std::endl;
    }
    
    return 0;
}
```
### 示例 3: 机器学习中的应用

```cpp
#include <iostream>
#include <vector>

// 神经网络层结构
struct Layer {
    int input_size;
    int output_size;
    std::string activation;
};

int main() {
    std::vector<Layer> network = {
        {784, 256, "ReLU"},
        {256, 128, "ReLU"},
        {128, 10, "Softmax"}
    };
    
    std::cout << "Neural Network Architecture:" << std::endl;
    for (size_t i = 0; i < network.size(); i++) {
        std::cout << "Layer " << i << ": "
                  << network[i].input_size << " -> "
                  << network[i].output_size << " ("
                  << network[i].activation << ")" << std::endl;
    }
    
    return 0;
}
```
### 示例 4: 联合体

```cpp
#include <iostream>

union Data {
    int i;
    float f;
    char c;
};

int main() {
    Data data;
    data.i = 42;
    std::cout << "As int: " << data.i << std::endl;
    
    data.f = 3.14f;
    std::cout << "As float: " << data.f << std::endl;
    
    return 0;
}
```
## 🎯 应用场景

### ACM 竞赛中的应用
- 数据点：存储坐标
- 配置：存储多个相关参数
- 位运算：节省内存

### 机器学习中的应用
- 神经网络结构：定义层配置
- 数据样本：存储特征和标签
- 模型参数：组织权重和偏置

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| 内存对齐 | 结构体可能有填充字节 |
| 大小计算 | 使用 sizeof 获取实际大小 |
| 联合体使用 | 同时只能访问一个成员 |
| 指针操作 | 结构体指针访问成员使用 -> |

## 🔗 相关概念

- [[02_Variables_Types]] - 变量与数据类型
- [[08_Arrays]] - 数组

## 📝 练习题

1. 编写程序使用结构体存储学生信息
2. 理解结构体和数组的结合使用

## 📚 参考资料

- [C++ Reference - Classes](https://en.cppreference.com/w/cpp/language/class)
