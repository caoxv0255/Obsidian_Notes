---
type: concept
topic: stl_allocators
category: stl
difficulty: advanced
prerequisites: [[01_Containers]], [[03_STL_Algorithms]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# Allocator 与 PMR（内存资源）

## 核心定义

Allocator 负责容器的内存分配策略。C++17 引入 PMR（Polymorphic Memory Resource），让容器在运行时切换内存资源。

## 为什么重要

- 高频分配场景（日志、交易撮合、网络服务）中，分配器可显著影响性能。
- PMR 便于做内存池、短生命周期批量回收。

## 基础示例

```cpp
#include <iostream>
#include <memory_resource>
#include <string>
#include <vector>

int main() {
    std::byte buffer[4096];
    std::pmr::monotonic_buffer_resource pool(buffer, sizeof(buffer));

    std::pmr::vector<std::pmr::string> names{&pool};
    names.emplace_back("alice");
    names.emplace_back("bob");

    std::cout << names[0] << " " << names[1] << "\n";
    return 0;
}
```

## 常见资源类型

1. `monotonic_buffer_resource`：只增不减，整体释放，速度快。
2. `unsynchronized_pool_resource`：单线程池化复用。
3. `synchronized_pool_resource`：线程安全池化。

## 使用建议

- 算法竞赛通常不必深挖 Allocator。
- 工程场景要做压测再决定是否引入 PMR。
- 不要过早优化，先定位热点再改分配策略。

## 相关链接

- [[00_STL_Index|返回 STL 索引]]
