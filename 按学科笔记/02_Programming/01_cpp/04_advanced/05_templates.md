---
type: concept
topic: templates
category: advanced
difficulty: advanced
prerequisites: [[../02_STL/01_Containers]]
acm_relevant: false
created: 2026-02-20
status: complete
---

# 模板和泛型编程 (Templates and Generic Programming)

## 核心定义

模板是 C++ 的泛型编程机制，允许编写可以处理多种数据类型的代码。

## 直观解释

想象你有一个做饼干的模具。不管你用什么面团（巧克力、香草、黄油），都能做出形状相同的饼干。模板就是这样的"模具"。

## 详细说明

### 函数模板

```cpp
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}
```

### 类模板

```cpp
template <typename T>
class Stack {
    std::vector<T> elements;
public:
    void push(T value) { elements.push_back(value); }
    T pop() { 
        T val = elements.back();
        elements.pop_back();
        return val;
    }
};
```

## 必背要点

### 1) 模板参数
- 类型参数：`typename T` / `class T`
- 非类型参数：`template <typename T, std::size_t N>`
- 模板参数可以组合使用，常见于容器、数组、算法封装

### 2) 模板实参推导
- 编译器会根据调用点自动推导模板参数
- 复杂场景下推导失败时，可以显式写出模板参数

### 3) specialization
- **全特化**：为某个具体类型写专门版本
- **偏特化**：类模板常见，函数模板没有真正的偏特化
- 特化适合处理“某类类型有特殊规则”的情况

### 4) SFINAE / 约束（概念）
- 模板实例化失败不一定是错误，可能只是“候选项被丢弃”
- 现代 C++ 更推荐用 `requires` / concepts 表达约束（如果你用 C++20）

### 5) 代码组织
- 模板实现通常放在头文件
- 因为模板需要在编译期看到定义才能实例化

## 代码示例

```cpp
#include <iostream>
#include <vector>

// 函数模板
template <typename T>
T findMax(const std::vector<T>& vec) {
    T maxVal = vec[0];
    for (const T& val : vec) {
        if (val > maxVal) {
            maxVal = val;
        }
    }
    return maxVal;
}

int main() {
    std::vector<int> ints = {1, 5, 3, 9, 2};
    std::vector<double> doubles = {1.5, 2.7, 0.3, 8.9};
    
    std::cout << "Max int: " << findMax(ints) << std::endl;
    std::cout << "Max double: " << findMax(doubles) << std::endl;
    
    return 0;
}
```

## 进阶示例

### 示例 1：非类型模板参数
```cpp
#include <array>
#include <iostream>

template <typename T, std::size_t N>
void printArray(const std::array<T, N>& arr) {
    for (const auto& value : arr) {
        std::cout << value << ' ';
    }
    std::cout << '\n';
}

int main() {
    std::array<int, 4> arr = {1, 2, 3, 4};
    printArray(arr);
}
```

### 示例 2：类模板的简单特化
```cpp
#include <iostream>
#include <string>

template <typename T>
class Printer {
public:
    void print(const T& value) const {
        std::cout << value << '\n';
    }
};

template <>
class Printer<std::string> {
public:
    void print(const std::string& value) const {
        std::cout << "[string] " << value << '\n';
    }
};

int main() {
    Printer<int> int_printer;
    Printer<std::string> string_printer;
    int_printer.print(42);
    string_printer.print("hello");
}
```

## ACM/工程视角

- **ACM**：模板用于写数据结构、图算法、数学工具的通用版本
- **工程**：模板用于容器封装、策略类、零开销抽象
- 模板过度复杂会让错误信息爆炸，优先保持接口简单

## 常见坑

- [ ] 模板定义和声明分离后链接失败
- [ ] 过度依赖模板递归导致编译时间暴涨
- [ ] 特化规则没想清楚，导致行为与预期不一致
- [ ] 模板参数推导失败时，没有检查引用折叠/const 限定

## 练习

1. 写一个 `Min` / `Max` / `Clamp` 的模板工具集
2. 写一个 `Matrix<T, R, C>`，用非类型模板参数固定大小
3. 把你在 ACM 里常用的容器、边界检查、调试宏整理成模板工具头文件