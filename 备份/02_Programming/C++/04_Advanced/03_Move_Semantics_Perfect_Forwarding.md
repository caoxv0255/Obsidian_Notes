---
type: concept
topic: move_semantics
category: advanced
difficulty: advanced
prerequisites: [[01_OOP_Classes_Objects]], [[02_RAII_Smart_Pointers]]
acm_relevant: true
created: 2026-04-22
status: draft
cpp_standard: 11
tags: [编程/C++, 进阶/性能, 工程/优化, ACM/技巧]
---

# 移动语义与完美转发（写快而不写错）

## 核心目标
- 能区分：lvalue/rvalue、左值引用/右值引用
- 能写出正确的 move ctor / move assign
- 了解 `std::move` 只是“转成右值”，不等于真的移动
- 能在模板里用 `std::forward` 做完美转发

## 核心定义
- **左值（lvalue）**：有名字、可取地址的对象（直觉）
- **右值（rvalue）**：临时值/即将销毁的对象（直觉）
- **移动语义**：把资源所有权从 A 转移给 B，避免深拷贝

## 必背要点（提纲）
### 1) std::move vs std::forward
- `std::move(x)`：无条件把 `x` 转成右值（允许被搬走）
- `std::forward<T>(x)`：按模板参数保留值类别（完美转发）

### 1.1 常见误区
- `std::move` 不会移动资源，它只是一个类型转换
- 被 `std::move` 过的对象只能处于“可析构、可重新赋值”的状态
- 返回局部变量时，通常不要强行 `std::move`，让编译器做 RVO/NRVO

### 2) Rule of 5 与 noexcept
- move 操作尽量 `noexcept`，否则容器可能退化为拷贝

### 2.1 为什么 noexcept 重要
- 标准容器在扩容时，往往更愿意使用不会抛异常的移动操作
- 如果 move 可能抛异常，容器可能选择拷贝以保证安全性

### 3) 返回值优化（RVO/NRVO）
- 现代编译器很多情况下不需要手写 move

### 3.1 什么时候该显式 move
- 从局部变量返回通常不需要手写
- 从函数参数、成员变量或容器元素中“转移所有权”时，才考虑 `std::move`

## 最小可编译示例（占位）
### 示例 1：一个资源类的 move
```cpp
#include <utility>

class Buffer {
public:
    Buffer() = default;

    explicit Buffer(int* p) : p_(p) {}

    ~Buffer() { delete[] p_; }

    Buffer(const Buffer&) = delete;
    Buffer& operator=(const Buffer&) = delete;

    Buffer(Buffer&& other) noexcept : p_(other.p_) {
        other.p_ = nullptr;
    }

    Buffer& operator=(Buffer&& other) noexcept {
        if (this != &other) {
            delete[] p_;
            p_ = other.p_;
            other.p_ = nullptr;
        }
        return *this;
    }

private:
    int* p_{};
};

int main() {
    Buffer a(new int[10]);
    Buffer b(std::move(a));
}
```

### 示例 2：完美转发（示意）
```cpp
#include <utility>
#include <string>

struct X {
    explicit X(std::string s) : s_(std::move(s)) {}
    std::string s_;
};

template <class... Args>
X makeX(Args&&... args) {
    return X(std::forward<Args>(args)...);
}

int main() {
    auto x1 = makeX(std::string("hi"));
}
```

### 示例 3：转移资源所有权
```cpp
#include <iostream>
#include <utility>

class Buffer {
public:
    explicit Buffer(std::size_t size)
        : size_(size), data_(new int[size]()) {}

    ~Buffer() { delete[] data_; }

    Buffer(const Buffer&) = delete;
    Buffer& operator=(const Buffer&) = delete;

    Buffer(Buffer&& other) noexcept
        : size_(other.size_), data_(other.data_) {
        other.size_ = 0;
        other.data_ = nullptr;
    }

    Buffer& operator=(Buffer&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            size_ = other.size_;
            data_ = other.data_;
            other.size_ = 0;
            other.data_ = nullptr;
        }
        return *this;
    }

    std::size_t size() const { return size_; }

private:
    std::size_t size_{};
    int* data_{};
};

int main() {
    Buffer a(10);
    Buffer b(std::move(a));
    std::cout << b.size() << '\n';
}
```

## 常见坑（占位清单）
- [ ] move 后继续使用对象却假设其值不变（只保证“可析构、可赋值”）
- [ ] move ctor/assign 忘记处理自赋值/资源释放
- [ ] 在返回局部变量时强行 `std::move` 反而可能干扰 NRVO

## 练习（建议）
1. 给你已有的 `File`/`UniqueFd` 增加 move 并写测试用例
2. 写一个 `emplace` 友好的容器包装类，观测拷贝/移动次数
3. 比较 `push_back(temp)`、`push_back(std::move(temp))`、`emplace_back(...)` 的差异

## 相关链接
- [[01_OOP_Classes_Objects|类与对象（Rule of 5）]]
- [[04_STL_Pitfalls_Performance|STL 坑点与性能]]

## 参考资料
- cppreference：value category、std::move、std::forward
- C++ Core Guidelines：F.18 / F.19
