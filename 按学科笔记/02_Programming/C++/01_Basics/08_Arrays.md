---
type: concept
topic: Arrays
category: basics
difficulty: 基础
prerequisites: [[06_Pointers]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 2.0
practice_problems: 5
ml_relevance: high
cpp_standard: 11
tags: [编程/C++, 基础/数组, ACM/基础, ML/数据结构]
---

# 数组 (Arrays)

> 数组是存储相同类型元素的连续内存块，是 C++ 中最基本的数据结构

## 📌 核心定义

数组是一组相同类型元素的集合，这些元素在内存中连续存储。数组通过索引访问元素，索引从 0 开始。数组的大小在编译时确定，不能动态改变。

## 💡 直觉理解

数组就像"一排盒子"：
- 数组 = 一排大小相同的盒子
- 索引 = 盒子的编号（从 0 开始）
- 元素 = 盒子里存放的东西
- 数组名 = 整排盒子的地址

## 📖 详细说明

### 1. 数组的声明和初始化

```cpp
int arr[5];                    // 声明大小为 5 的数组
int arr2[] = {1, 2, 3, 4, 5};  // 自动推断大小
int arr3[5] = {1, 2, 3};       // 剩余元素初始化为 0
```
### 2. 数组访问

```cpp
int arr[5] = {10, 20, 30, 40, 50};
int first = arr[0];    // 10
int last = arr[4];     // 50
```
### 3. 数组与指针

```cpp
int arr[5];
int* ptr = arr;  // 数组名自动转换为指向首元素的指针
```
## 💻 代码示例

### 示例 1: 基本数组操作

```cpp
#include <iostream>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    
    // 遍历数组
    for (int i = 0; i < 5; i++) {
        std::cout << "arr[" << i << "] = " << arr[i] << std::endl;
    }
    
    // 计算数组大小
    int size = sizeof(arr) / sizeof(arr[0]);
    std::cout << "Array size: " << size << std::endl;
    
    return 0;
}
```
### 示例 2: 数组作为函数参数

```cpp
#include <iostream>

// 数组作为参数（退化为指针）
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    printArray(arr, 5);
    return 0;
}
```
### 示例 3: 二维数组

```cpp
#include <iostream>

int main() {
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    // 访问二维数组
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
    
    return 0;
}
```
### 示例 4: 机器学习中的应用

```cpp
#include <iostream>

// 向量点积
double dotProduct(double a[], double b[], int size) {
    double result = 0.0;
    for (int i = 0; i < size; i++) {
        result += a[i] * b[i];
    }
    return result;
}

// 向量加法
void vectorAdd(double a[], double b[], double result[], int size) {
    for (int i = 0; i < size; i++) {
        result[i] = a[i] + b[i];
    }
}

int main() {
    double v1[] = {1.0, 2.0, 3.0};
    double v2[] = {4.0, 5.0, 6.0};
    double v3[3];
    
    std::cout << "Dot product: " << dotProduct(v1, v2, 3) << std::endl;
    
    vectorAdd(v1, v2, v3, 3);
    std::cout << "Vector sum: ";
    for (int i = 0; i < 3; i++) {
        std::cout << v3[i] << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```
## 🎯 应用场景

### ACM 竞赛中的应用
- 数据存储：存储大量数据
- 前缀和：快速查询区间和
- 动态规划：存储状态

### 机器学习中的应用
- 特征向量：存储特征数据
- 权重矩阵：神经网络参数
- 批处理：批量数据处理

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| 数组越界 | 访问超出范围的索引会导致未定义行为 |
| 数组大小 | 必须是编译时常量 |
| 数组退化 | 作为函数参数时退化为指针 |
| 初始化 | 未初始化的数组包含垃圾值 |

## 🔗 相关概念

- [[06_Pointers]] - 指针
- [[../../02_STL/01_Vectors|STL Vector]] - 动态数组

## 📝 练习题

1. 编写函数反转数组
2. 编写函数查找数组中的最大值和最小值

## 📚 参考资料

- [C++ Reference - Arrays](https://en.cppreference.com/w/cpp/language/array)
