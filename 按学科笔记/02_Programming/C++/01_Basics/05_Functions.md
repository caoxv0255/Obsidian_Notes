---
type: concept
topic: Functions
category: basics
difficulty: 基础
prerequisites: [[04_Control_Flow]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 2.5
practice_problems: 5
ml_relevance: high
cpp_standard: 11
tags: [编程/C++, 基础/函数, ACM/基础, ML/算法基础]
---

# 函数 (Functions)

> 函数是执行特定任务的代码块，可重复使用，提高代码的可读性和可维护性

## 📌 核心定义

函数是一段完成特定任务的代码块，具有名称、参数列表和返回值。函数可以将复杂问题分解为更小的、可管理的部分，实现代码的模块化和复用。

## 💡 直觉理解

函数就像一个"工具箱"：
- 函数名 = 工具箱的标签
- 参数 = 放入工具箱的原料
- 返回值 = 工具箱处理后的产品
- 函数体 = 工具箱内部的加工过程

## 📖 详细说明

### 1. 函数声明与定义

```cpp
// 函数声明（原型）
return_type function_name(parameter_list);

// 函数定义
return_type function_name(parameter_list) {
    // 函数体
    return value;
}
```

### 2. 参数传递方式

| 方式 | 说明 | 示例 |
|------|------|------|
| 值传递 | 传递参数的副本 | void func(int x) |
| 指针传递 | 传递参数的地址 | void func(int* x) |
| 引用传递 | 传递参数的别名 | void func(int& x) |

### 3. 函数重载

允许同名函数存在，只要参数列表不同。

## 💻 代码示例

### 示例 1: 基本函数使用

```cpp
#include <iostream>

// 函数声明
int add(int a, int b);
void printResult(int result);

int main() {
    int x = 5, y = 3;
    int sum = add(x, y);
    printResult(sum);
    return 0;
}

// 函数定义：两个数相加
int add(int a, int b) {
    return a + b;
}

// 函数定义：打印结果
void printResult(int result) {
    std::cout << "结果是: " << result << std::endl;
}
```

### 示例 2: 函数重载

```cpp
#include <iostream>

// 重载函数：整数相加
int add(int a, int b) {
    return a + b;
}

// 重载函数：浮点数相加
double add(double a, double b) {
    return a + b;
}

// 重载函数：三个数相加
int add(int a, int b, int c) {
    return a + b + c;
}

int main() {
    std::cout << "int: " << add(1, 2) << std::endl;
    std::cout << "double: " << add(1.5, 2.5) << std::endl;
    std::cout << "three: " << add(1, 2, 3) << std::endl;
    return 0;
}
```

### 示例 3: 递归函数（ACM 常用）

```cpp
#include <iostream>

// 阶乘函数（递归实现）
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// 斐波那契数列（递归实现）
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    std::cout << "5! = " << factorial(5) << std::endl;
    std::cout << "fib(10) = " << fibonacci(10) << std::endl;
    return 0;
}
```

### 示例 4: 机器学习中的应用

```cpp
#include <iostream>
#include <vector>

// 激活函数：ReLU
double relu(double x) {
    return x > 0 ? x : 0;
}

// 激活函数：Sigmoid
double sigmoid(double x) {
    return 1.0 / (1.0 + std::exp(-x));
}

// 简单的损失函数（均方误差）
double mse(const std::vector<double>& predicted, 
           const std::vector<double>& actual) {
    double sum = 0.0;
    for (size_t i = 0; i < predicted.size(); i++) {
        double diff = predicted[i] - actual[i];
        sum += diff * diff;
    }
    return sum / predicted.size();
}

int main() {
    std::cout << "ReLU(-1) = " << relu(-1) << std::endl;
    std::cout << "ReLU(2) = " << relu(2) << std::endl;
    std::cout << "Sigmoid(0) = " << sigmoid(0) << std::endl;
    
    std::vector<double> pred = {1.0, 2.0, 3.0};
    std::vector<double> act = {1.1, 1.9, 3.2};
    std::cout << "MSE: " << mse(pred, act) << std::endl;
    
    return 0;
}
```

## 🎯 应用场景

### ACM 竞赛中的应用
- 递归算法：DFS、分治算法
- 数学函数：阶乘、斐波那契
- 工具函数：最大公约数、快速幂

### 机器学习中的应用
- 激活函数：ReLU、Sigmoid、Tanh
- 损失函数：MSE、交叉熵
- 优化函数：梯度下降

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| 参数传递 | 理解值传递、指针传递、引用传递的区别 |
| 栈溢出 | 递归深度过大可能导致栈溢出 |
| 内联函数 | 小函数可以使用 inline 优化 |
| 返回值 | 函数可以返回值或 void |

## 🔗 相关概念

- [[04_Control_Flow]] - 控制流
- [[06_Pointers]] - 指针
- [[07_References]] - 引用

## 📝 练习题

1. 编写函数计算最大公约数（GCD）
2. 编写递归函数实现快速幂算法

## 📚 参考资料

- [C++ Reference - Functions](https://en.cppreference.com/w/cpp/language/functions)