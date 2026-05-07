---
type: concept
topic: Memory Management
category: basics
difficulty: 进阶
prerequisites: [[06_Pointers]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 3.0
practice_problems: 5
ml_relevance: high
cpp_standard: 11
tags: [编程/C++, 基础/内存管理, ACM/基础, ML/内存管理]
---

# 内存管理 (Memory Management)

> 内存管理涉及动态内存分配和释放，是 C++ 中最重要也最容易出错的主题之一

## 📌 核心定义

内存管理是指程序如何在运行时分配和释放内存。C++ 提供了 new/delete 操作符用于动态内存分配，同时支持 C 风格的 malloc/free。

## 💡 直觉理解

内存就像"仓库空间"：
- 栈 = 自动管理的临时空间
- 堆 = 手动管理的长期空间
- new/delete = 从堆中租用和归还空间

## 📖 详细说明

### 1. 内存区域

| 区域 | 特点 | 生命周期 |
|------|------|----------|
| 栈 | 自动分配释放 | 作用域结束时 |
| 堆 | 手动分配释放 | 直到手动释放 |
| 全局/静态 | 程序启动到结束 | 整个程序期间 |

### 2. new/delete 操作符

```cpp
int* ptr = new int(42);  // 分配内存
delete ptr;              // 释放内存
ptr = nullptr;            // 避免悬空指针
```
### 3. 数组分配

```cpp
int* arr = new int[10];   // 分配数组
delete[] arr;              // 释放数组
arr = nullptr;
```
## 💻 代码示例

### 示例 1: 基本动态内存分配

```cpp
#include <iostream>

int main() {
    // 分配单个整数
    int* ptr = new int(42);
    std::cout << "Value: " << *ptr << std::endl;
    delete ptr;
    ptr = nullptr;
    
    return 0;
}
```
### 示例 2: 动态数组

```cpp
#include <iostream>

int main() {
    int size = 5;
    int* arr = new int[size];
    
    // 初始化数组
    for (int i = 0; i < size; i++) {
        arr[i] = i * 10;
    }
    
    // 输出数组
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    
    // 释放内存
    delete[] arr;
    arr = nullptr;
    
    return 0;
}
```
### 示例 3: 机器学习中的应用

```cpp
#include <iostream>

// 动态分配特征向量
double* createFeatures(int size) {
    return new double[size];
}

// 释放特征向量
void freeFeatures(double* features) {
    delete[] features;
}

int main() {
    int feature_size = 1000;
    double* features = createFeatures(feature_size);
    
    // 初始化特征
    for (int i = 0; i < feature_size; i++) {
        features[i] = 0.0;
    }
    
    std::cout << "Created features of size: " << feature_size << std::endl;
    
    freeFeatures(features);
    
    return 0;
}
```
### 示例 4: 内存泄漏示例

```cpp
#include <iostream>

void leakExample() {
    int* ptr = new int(42);
    // 忘记 delete，导致内存泄漏
}

int main() {
    leakExample();
    std::cout << "Memory leaked!" << std::endl;
    return 0;
}
```
## 🎯 应用场景

### ACM 竞赛中的应用
- 动态数组：处理不确定大小的数据
- 图邻接表：动态存储边信息

### 机器学习中的应用
- 动态张量：分配神经网络参数
- 批量数据：动态加载训练数据

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| 内存泄漏 | 必须配对 new/delete 或 new[]/delete[] |
| 悬空指针 | 释放后设置为 nullptr |
| 重复释放 | 同一内存不能释放两次 |
| 未初始化指针 | 始终初始化指针为 nullptr |

## 🔗 相关概念

- [[06_Pointers]] - 指针
- [[08_Arrays]] - 数组

## 📝 练习题

1. 编写函数动态创建二维数组
2. 编写程序检测内存泄漏

## 📚 参考资料

- [C++ Reference - new Expression](https://en.cppreference.com/w/cpp/language/new)
