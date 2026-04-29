---
type: concept
topic: Pointers
category: basics
difficulty: 基础
prerequisites: [[02_Variables_Types]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 3.0
practice_problems: 6
ml_relevance: high
cpp_standard: 11
tags: [编程/C++, 基础/指针, ACM/基础, ML/内存管理]
---

# 指针 (Pointers)

> 指针是存储内存地址的变量，是 C++ 最强大也是最容易出错的概念之一

## 📌 核心定义

指针是一种特殊类型的变量，它存储的是另一个变量的内存地址。通过指针，我们可以直接访问和操作内存中的数据，实现高效的内存管理和灵活的数据结构操作。

## 💡 直觉理解

指针就像"地址标签"：
- 指针变量 = 写有地址的标签
- 地址 = 内存中某个位置的编号
- 解引用 = 根据地址找到实际存放的东西

## 📖 详细说明

### 1. 指针的声明和使用

```cpp
int* ptr;           // 声明一个指向 int 的指针
int value = 42;
ptr = &value;       // ptr 现在存储 value 的地址
*ptr = 10;          // 通过指针修改 value 的值
```

### 2. 指针运算

| 运算 | 说明 | 示例 |
|------|------|------|
| & | 取地址 | &x 获取 x 的地址 |
| * | 解引用 | *p 获取 p 指向的值 |
| ++ | 指针递增 | p++ 指向下一个元素 |
| -- | 指针递减 | p-- 指向前一个元素 |

### 3. 空指针

```cpp
int* ptr = nullptr;  // C++11 推荐方式
int* ptr2 = NULL;   // C 风格（不推荐）
int* ptr3 = 0;      // 也表示空指针
```

## 💻 代码示例

### 示例 1: 基本指针操作

```cpp
#include <iostream>

int main() {
    int value = 42;
    int* ptr = &value;
    
    std::cout << "value: " << value << std::endl;
    std::cout << "Address of value: " << &value << std::endl;
    std::cout << "ptr: " << ptr << std::endl;
    std::cout << "*ptr: " << *ptr << std::endl;
    
    *ptr = 100;
    std::cout << "After modification: " << value << std::endl;
    
    return 0;
}
```

### 示例 2: 指针与数组

```cpp
#include <iostream>

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int* ptr = arr;  // 数组名自动转换为指向首元素的指针
    
    // 使用指针遍历数组
    for (int i = 0; i < 5; i++) {
        std::cout << "*(ptr + " << i << ") = " << *(ptr + i) << std::endl;
    }
    
    // 指针算术
    ptr++;
    std::cout << "After ptr++: " << *ptr << std::endl;
    
    return 0;
}
```

### 示例 3: 指针作为函数参数

```cpp
#include <iostream>

// 通过指针交换两个数
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    std::cout << "Before: x=" << x << ", y=" << y << std::endl;
    
    swap(&x, &y);
    
    std::cout << "After: x=" << x << ", y=" << y << std::endl;
    return 0;
}
```

### 示例 4: 机器学习中的应用

```cpp
#include <iostream>

// 简单的矩阵乘法（使用指针）
void matrixMultiply(int* A, int* B, int* C, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            *(C + i * n + j) = 0;
            for (int k = 0; k < n; k++) {
                *(C + i * n + j) += *(A + i * n + k) * *(B + k * n + j);
            }
        }
    }
}

int main() {
    int A[2][2] = {{1, 2}, {3, 4}};
    int B[2][2] = {{5, 6}, {7, 8}};
    int C[2][2];
    
    matrixMultiply(&A[0][0], &B[0][0], &C[0][0], 2);
    
    std::cout << "Result:" << std::endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            std::cout << C[i][j] << " ";
        }
        std::cout << std::endl;
    }
    
    return 0;
}
```

## 🎯 应用场景

### ACM 竞赛中的应用
- 动态内存分配：处理大数据
- 指针算法：快速遍历数组
- 图论：邻接表表示

### 机器学习中的应用
- 矩阵运算：高效访问矩阵元素
- GPU 编程：CUDA 指针操作
- 深度学习框架：底层内存管理

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| 空指针检查 | 使用指针前检查是否为 nullptr |
| 内存泄漏 | 动态分配的内存必须释放 |
| 野指针 | 避免使用指向已释放内存的指针 |
| 指针算术 | 确保指针算术在有效范围内 |

## 🔗 相关概念

- [[02_Variables_Types]] - 变量与数据类型
- [[07_References]] - 引用
- [[08_Arrays]] - 数组
- [[16_Memory_Management]] - 内存管理

## 📝 练习题

1. 编写函数使用指针反转数组
2. 编写函数使用指针查找数组中的最大值

## 📚 参考资料

- [C++ Reference - Pointers](https://en.cppreference.com/w/cpp/language/pointer)