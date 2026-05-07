---
type: concept
topic: References
category: basics
difficulty: 基础
prerequisites: [[06_Pointers]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 1.5
practice_problems: 3
ml_relevance: medium
cpp_standard: 11
tags: [编程/C++, 基础/引用, ACM/基础]
---

# 引用 (References)

> 引用是变量的别名，提供了另一种访问变量的方式，比指针更安全更直观

## 📌 核心定义

引用是已存在变量的别名。一旦引用被初始化指向一个变量，它就不能被改变指向其他变量。引用在函数参数传递中非常有用，可以避免值传递的开销。

## 💡 直觉理解

引用就像"绰号"或"别名"：
- 原变量 = 人的真名
- 引用 = 人的绰号
- 操作引用 = 直接操作原变量（不是副本）

## 📖 详细说明

### 1. 引用的声明

```cpp
int value = 42;
int& ref = value;  // ref 是 value 的引用
```


### 2. 引用 vs 指针

| 特性 | 引用 | 指针 |
|------|------|------|
| 声明 | int& ref | int* ptr |
| 初始化 | 必须初始化 | 可以不初始化 |
| 重新赋值 | 不能 | 可以 |
| 空值 | 不能为空 | 可以为 nullptr |
| 操作 | 像普通变量 | 需要解引用 |

### 3. 引用作为函数参数

```cpp
void swap(int& a, int& b);  // 使用引用
void swap(int* a, int* b);  // 使用指针
```

## 💻 代码示例

### 示例 1: 基本引用使用

```cpp
#include <iostream>

int main() {
    int value = 42;
    int& ref = value;
    
    std::cout << "value: " << value << std::endl;
    std::cout << "ref: " << ref << std::endl;
    std::cout << "&value: " << &value << std::endl;
    std::cout << "&ref: " << &ref << std::endl;
    
    ref = 100;  // 修改引用也会修改原变量
    std::cout << "After ref = 100:" << std::endl;
    std::cout << "value: " << value << std::endl;
    
    return 0;
}
```

### 示例 2: 引用 vs 指针

```cpp
#include <iostream>

void useReference(int& ref) {
    ref = 100;  // 直接修改
}

void usePointer(int* ptr) {
    *ptr = 100;  // 需要解引用
}

int main() {
    int a = 42, b = 42;
    
    useReference(a);
    usePointer(&b);
    
    std::cout << "After reference: a = " << a << std::endl;
    std::cout << "After pointer: b = " << b << std::endl;
    
    return 0;
}
```

### 示例 3: 引用作为返回值

```cpp
#include <iostream>

int arr[10];

// 返回数组元素的引用
int& getElement(int index) {
    return arr[index];
}

int main() {
    getElement(5) = 100;  // 直接修改数组元素
    std::cout << "arr[5] = " << arr[5] << std::endl;
    
    return 0;
}
```

## 🎯 应用场景

### ACM 竞赛中的应用
- 函数参数：避免值传递开销
- 返回大对象：提高效率
- 操作符重载：实现流畅的语法

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| 必须初始化 | 引用声明时必须初始化 |
| 不能重新绑定 | 引用一旦绑定就不能改变 |
| 不能为空 | 引用不能是 nullptr |
| const 引用 | 避免修改原变量时使用 |

## 🔗 相关概念

- [[06_Pointers]] - 指针
- [[05_Functions]] - 函数

## 📝 练习题

1. 编写函数使用引用交换两个数
2. 编写函数使用引用修改数组的元素

## 📚 参考资料

- [C++ Reference - References](https://en.cppreference.com/w/cpp/language/reference)
