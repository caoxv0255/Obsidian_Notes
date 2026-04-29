---
type: concept
topic: raii_smart_pointers
category: advanced
difficulty: intermediate
prerequisites: [[../01_Basics/16_Memory_Management]], [[../01_Basics/19_Error_Handling]]
acm_relevant: true
created: 2026-04-22
status: draft
cpp_standard: 11
tags: [编程/C++, 进阶/资源管理, 工程/可靠性, ACM/技巧]
---

# RAII 与智能指针（把资源关进对象里）

## 核心目标
- 用 RAII 解决：泄漏、早退、异常导致的资源未释放
- 正确使用：`unique_ptr/shared_ptr/weak_ptr`，理解所有权模型
- 能写一个“小而美”的资源封装类（fd/file/mutex/socket）

## 核心定义
- **RAII**：Resource Acquisition Is Initialization
  - 资源获取在构造中完成
  - 资源释放在析构中完成
- **异常安全**：出现异常时仍能保持资源不泄漏、不变量不破坏

## 直觉理解
把“释放资源”这件事交给析构函数，等价于：
- 你不需要记住所有 `return` 分支
- 也不怕中途 `throw`

## 智能指针速查
- `std::unique_ptr<T>`：独占所有权（默认首选）
- `std::shared_ptr<T>`：共享所有权（谨慎，关注循环引用）
- `std::weak_ptr<T>`：打破循环引用/观察者

## 必背要点（提纲）
### 1) 何时用哪种？
- 绝大多数：`unique_ptr`
- 多处共享且生命周期不清晰：`shared_ptr`（要求明确“谁拥有”）
- 需要 cache/observer：`weak_ptr`

### 1.1 什么时候不该用 shared_ptr
- 对象只有一个明确拥有者时，不要先想到 `shared_ptr`
- 过度使用 `shared_ptr` 会让所有权变模糊，也会增加引用计数开销
- 需要“观察”而非“拥有”时，优先 `weak_ptr`

### 2) 自定义 deleter
- 封装 `FILE*`、`DIR*`、socket fd 等
- deleter 里只做释放，不抛异常

### 2.1 资源封装的原则
- 构造时完成获取，析构时完成释放
- 类本身不提供“忘记释放”的机会
- 复制语义要么明确支持，要么直接禁用

### 3) 异常安全等级（占位）
- basic / strong / nothrow

## 最小可编译示例（占位）
### 示例 1：unique_ptr 管理动态资源
```cpp
#include <memory>
#include <string>

struct Node {
    std::string value;
    std::unique_ptr<Node> next;
};

int main() {
    auto head = std::make_unique<Node>();
    head->value = "a";
    head->next = std::make_unique<Node>();
    head->next->value = "b";
}
```

### 示例 2：RAII 封装文件句柄（示意）
```cpp
#include <cstdio>
#include <stdexcept>

class File {
public:
    explicit File(const char* path, const char* mode) {
        fp_ = std::fopen(path, mode);
        if (!fp_) throw std::runtime_error("fopen failed");
    }

    ~File() {
        if (fp_) std::fclose(fp_);
    }

    File(const File&) = delete;
    File& operator=(const File&) = delete;

    File(File&& other) noexcept : fp_(other.fp_) { other.fp_ = nullptr; }
    File& operator=(File&& other) noexcept {
        if (this != &other) {
            if (fp_) std::fclose(fp_);
            fp_ = other.fp_;
            other.fp_ = nullptr;
        }
        return *this;
    }

private:
    std::FILE* fp_{};
};

int main() {
    File f("a.txt", "w");
}
```

### 示例 3：Linux fd 的 RAII 包装（示意）
```cpp
#include <unistd.h>
#include <utility>

class UniqueFd {
public:
    explicit UniqueFd(int fd = -1) : fd_(fd) {}

    ~UniqueFd() {
        if (fd_ != -1) {
            ::close(fd_);
        }
    }

    UniqueFd(const UniqueFd&) = delete;
    UniqueFd& operator=(const UniqueFd&) = delete;

    UniqueFd(UniqueFd&& other) noexcept : fd_(other.fd_) {
        other.fd_ = -1;
    }

    UniqueFd& operator=(UniqueFd&& other) noexcept {
        if (this != &other) {
            reset();
            fd_ = other.fd_;
            other.fd_ = -1;
        }
        return *this;
    }

    int get() const { return fd_; }
    int release() {
        int tmp = fd_;
        fd_ = -1;
        return tmp;
    }
    void reset(int fd = -1) {
        if (fd_ != -1) {
            ::close(fd_);
        }
        fd_ = fd;
    }

private:
    int fd_;
};
```

## 常见坑（占位清单）
- [ ] `shared_ptr` 循环引用导致泄漏（用 `weak_ptr` 断环）
- [ ] `unique_ptr` 管理数组要用 `unique_ptr<T[]>` 或 vector
- [ ] 在析构里抛异常（会导致 terminate）

## 练习（建议）
1. 写 `UniqueFd`（Linux fd 的 RAII 包装），支持 move，不支持 copy
2. 写一个用 `shared_ptr` 的对象图，构造循环引用并用 `weak_ptr` 修复
3. 把一个“手动 fclose / close / delete”的函数改造成 RAII 版本

## 相关链接
- [[01_OOP_Classes_Objects|类与对象（特殊成员函数）]]
- [[03_Move_Semantics_Perfect_Forwarding|移动语义与完美转发]]

## 参考资料
- cppreference：smart pointers
- C++ Core Guidelines：R.1/R.5/R.20
