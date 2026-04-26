---
type: concept
topic: stl_iterators
category: stl
difficulty: intermediate
prerequisites: [[01_Containers]]
acm_relevant: true
created: 2026-02-20
status: complete
---

# STL 迭代器 (STL Iterators)

## 核心定义

迭代器是一种对象，用于遍历容器中的元素。它提供了统一的接口来访问不同类型的容器。

## 直观解释

迭代器就像一个指针，指向容器中的某个元素。你可以通过迭代器"移动"到下一个或上一个元素，访问或修改元素值。

## 详细说明

### 迭代器类型

1. **输入迭代器**：只读，单向
2. **输出迭代器**：只写，单向
3. **前向迭代器**：读写，单向
4. **双向迭代器**：读写，双向
5. **随机访问迭代器**：读写，随机访问

### 常用操作

- `++it` / `it++`：前进
- `--it` / `it--`：后退（双向迭代器）
- `*it`：访问元素
- `it->member`：访问成员
- `it + n` / `it - n`：随机访问（随机访问迭代器）

## 代码示例

```cpp
#include <iostream>
#include <vector>
#include <list>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    
    // 使用迭代器遍历
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    // 修改元素
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        *it *= 2;
    }
    
    // 使用反向迭代器
    for (auto it = vec.rbegin(); it != vec.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```