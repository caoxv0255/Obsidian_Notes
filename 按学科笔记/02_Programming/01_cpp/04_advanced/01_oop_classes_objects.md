---
type: concept
topic: oop_classes_objects
category: advanced
difficulty: intermediate
prerequisites: [[../01_Basics/05_Functions]], [[../01_Basics/11_Scope_Lifetime]], [[../01_Basics/16_Memory_Management]]
acm_relevant: true
created: 2026-04-22
status: draft
cpp_standard: 11
tags: [编程/C++, 进阶/OOP, 工程/基础, ACM/技巧]
---

# 类与对象（构造/析构/拷贝移动）

## 核心目标
- 能写出**资源安全、语义清晰**的类（值语义/引用语义）
- 能解释并应用：**Rule of 0/3/5**、`const` 成员函数、拷贝 vs 移动
- 面对工程 bug：能从“对象生命周期”定位问题

## 核心定义
- **类（class/struct）**：封装数据与行为的类型
- **对象生命周期**：构造 → 使用 → 析构（离开作用域、delete、容器销毁等）
- **值语义**：对象拷贝后相互独立（常见：`std::string`）
- **引用语义**：多个对象共享同一资源（常见：`shared_ptr` 管理的资源）

## 直觉理解
- 构造/析构就像“申请/归还资源”的自动流程
- 拷贝是“复制一份资源”，移动是“把资源所有权交给新对象”

## 必背要点（提纲）
### 1) 构造与析构
- 默认构造、带参构造、委托构造
- 成员初始化列表 vs 赋值
- 析构函数：释放资源、保持 noexcept（尽量）

### 1.1 成员初始化列表为什么更重要
- 成员在进入构造函数体之前就完成初始化
- 对 `const` 成员、引用成员、没有默认构造的成员是必须的
- 对自定义类型，初始化列表通常比先默认构造再赋值更高效

### 1.2 构造函数设计建议
- 能 `explicit` 就 `explicit`，避免隐式转换
- 参数少时优先值传递 + `std::move`，大对象或只读对象用 `const&`
- 如果类需要不变量，尽量让构造完成后对象就是“有效状态”

### 2) 拷贝/移动（Rule of 0/3/5）
- Rule of 0：只用标准库成员（`vector/string/unique_ptr`），通常不需要自写拷贝/析构
- Rule of 3：自定义析构/拷贝构造/拷贝赋值常常要一起出现
- Rule of 5：加上移动构造/移动赋值

### 3) const 正确性
- `T foo() const`：承诺不修改对象可观察状态
- `const` 成员 + `mutable`（谨慎）

### 4) 访问控制与接口设计
- `public`：对外稳定 API
- `private`：保持不变量（invariant）

### 5) this、static、const 成员
- `this` 指向当前对象，成员函数内部经常用来消除歧义
- `static` 成员属于类而不是对象，常用于计数器、共享配置
- `static` 成员函数没有 `this`，适合工具型接口

### 6) 继承与多态（工程上必知）
- 基类析构函数通常应为 `virtual`
- 用基类指针删派生类对象时，缺少虚析构会出问题
- 继承不是默认方案，优先组合，再考虑继承

## 常见坑（占位清单）
- [ ] 析构函数非虚导致多态 delete UB
- [ ] 复制/移动后对象状态不合法
- [ ] 自写拷贝忘了异常安全（资源泄漏/部分构造）
- [ ] 以为“=default”总是正确（需要确认语义）

## 最小可编译示例（占位）
```cpp
#include <iostream>
#include <string>

class Person {
public:
    Person(std::string name, int age)
        : name_(std::move(name)), age_(age) {}

    const std::string& name() const { return name_; }
    int age() const { return age_; }

private:
    std::string name_;
    int age_{};
};

int main() {
    Person p("Alice", 20);
    std::cout << p.name() << ", " << p.age() << "\n";
}
```

## 进阶示例：带不变量的类
```cpp
#include <iostream>
#include <stdexcept>
#include <string>

class BankAccount {
public:
    explicit BankAccount(std::string owner, long long balance)
        : owner_(std::move(owner)), balance_(balance) {
        if (owner_.empty()) {
            throw std::invalid_argument("owner must not be empty");
        }
        if (balance_ < 0) {
            throw std::invalid_argument("balance must be non-negative");
        }
    }

    void deposit(long long amount) {
        if (amount < 0) throw std::invalid_argument("amount must be non-negative");
        balance_ += amount;
    }

    void withdraw(long long amount) {
        if (amount < 0 || amount > balance_) {
            throw std::runtime_error("insufficient funds");
        }
        balance_ -= amount;
    }

    long long balance() const { return balance_; }

private:
    std::string owner_;
    long long balance_{};
};

int main() {
    BankAccount acc("Alice", 1000);
    acc.deposit(500);
    acc.withdraw(300);
    std::cout << acc.balance() << '\n';
}
```

## 练习（建议）
1. 写一个 `SmallString`/`Buffer` 类，先做 Rule of 0，再做自管理资源版本
2. 为一个类补齐拷贝/移动，写 5 个断言验证语义
3. 写一个 `Matrix` 类，支持构造、拷贝、移动、下标访问和 `const` 访问

## 相关链接
- [[05_Templates|模板（泛型基础）]]
- [[02_RAII_Smart_Pointers|RAII 与智能指针]]
- [[03_Move_Semantics_Perfect_Forwarding|移动语义与完美转发]]

## 参考资料
- cppreference：special member functions
- C++ Core Guidelines：C.20 / C.21 / R.*
