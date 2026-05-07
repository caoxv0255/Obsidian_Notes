---
type: concept
topic: Const and Volatile
category: basics
difficulty: 基础
prerequisites: [[02_Variables_Types]]
acm_relevant: false
created: 2026-02-20
status: learning
estimated_time: 1.0
practice_problems: 2
ml_relevance: low
cpp_standard: 11
tags: [编程/C++, 基础/常量]
---

# const 与 volatile (Const and Volatile)

> const 关键字用于定义常量，volatile 关键字用于告知编译器不要优化变量

## 📌 核心定义

const 关键字用于声明只读变量，防止意外修改。volatile 关键字告诉编译器变量的值可能在程序控制之外改变，禁止某些优化。

## 💡 直觉理解

- **const** = 只读文件，不能修改
- **volatile** = 可能被外部改变，不要缓存

## 📖 详细说明

### 1. const 的用法

```cpp
const int MAX_SIZE = 100;      // 常量
const int* ptr;               // 指向常量的指针
int* const ptr2;               // 指针本身是常量
const int& ref = value;        // 常量引用
```
### 2. volatile 的用法

```cpp
volatile int flag = 0;         // 可能被硬件改变
volatile int* ptr3;            // 指向 volatile 变量
```
### 3. const 与指针

| 声明 | 含义 |
|------|------|
| const int* p | p 指向常量，不能通过 p 修改值 |
| int* const p | p 是常量指针，不能改变 p 的指向 |
| const int* const p | p 是常量指针，指向常量 |

## 💻 代码示例

### 示例 1: const 基本用法

```cpp
#include <iostream>

int main() {
    const int MAX_VALUE = 100;
    const double PI = 3.14159;
    
    // MAX_VALUE = 200;  // 错误：不能修改 const 变量
    
    std::cout << "MAX_VALUE: " << MAX_VALUE << std::endl;
    std::cout << "PI: " << PI << std::endl;
    
    return 0;
}
```

### 示例 2: const 与函数参数

```cpp
#include <iostream>

// const 引用参数：避免拷贝，防止修改
void printString(const std::string& s) {
    std::cout << s << std::endl;
    // s = "modified";  // 错误：不能修改 const 引用
}

int main() {
    std::string text = "Hello";
    printString(text);
    return 0;
}
```

### 示例 3: const 返回值

```cpp
#include <iostream>

class MyClass {
public:
    const int& getValue() const {
        return value;
    }
    
private:
    int value = 42;
};

int main() {
    MyClass obj;
    std::cout << obj.getValue() << std::endl;
    return 0;
}
```

### 示例 4: volatile 用法

```cpp
#include <iostream>
#include <thread>
#include <chrono>

volatile bool flag = false;

void worker() {
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    flag = true;
}

int main() {
    std::thread t(worker);
    
    while (!flag) {
        // 等待 flag 变为 true
    }
    
    t.join();
    std::cout << "Flag is now true" << std::endl;
    
    return 0;
}
```

## 🎯 应用场景

### 机器学习中的应用
- const 模型参数：防止意外修改
- const 配置：只读配置

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| const 初始化 | const 变量必须初始化 |
| mutable | 在 const 成员函数中使用 mutable |
| volatile 优化 | volatile 会影响性能 |
| const 正确性 | 使用 const 提高代码安全性 |

## 🔗 相关概念

- [[02_Variables_Types]] - 变量与数据类型
- [[07_References]] - 引用

## 📝 练习题

1. 编写函数使用 const 引用参数
2. 理解 const 与指针的不同组合

## 📚 参考资料

- [C++ Reference - cv-qualifiers](https://en.cppreference.com/w/cpp/language/cv)
