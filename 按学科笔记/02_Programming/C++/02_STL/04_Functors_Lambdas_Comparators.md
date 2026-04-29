---
type: concept
topic: stl_functors
category: stl
difficulty: intermediate
prerequisites: [[03_STL_Algorithms]]
acm_relevant: true
created: 2026-04-25
status: complete
---

# 函数对象、Lambda 与比较器

## 核心定义

- 函数对象（Functor）：重载 `operator()` 的对象。
- Lambda：匿名可调用对象。
- 比较器：定义元素比较规则，常用于 `sort`、`set`、`priority_queue`。

## 什么时候用什么

1. 一次性逻辑：Lambda。
2. 需要保存状态或复用：函数对象。
3. 容器全局排序规则：自定义比较器类型。

## 代码示例

```cpp
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

struct ByAbs {
    bool operator()(int a, int b) const {
        if (std::abs(a) != std::abs(b)) return std::abs(a) < std::abs(b);
        return a < b;
    }
};

int main() {
    std::vector<int> v = {-3, 1, -2, 2, 4};

    std::sort(v.begin(), v.end(), ByAbs());

    auto greater_cmp = [](int a, int b) { return a > b; };
    std::priority_queue<int, std::vector<int>, decltype(greater_cmp)> min_heap(greater_cmp);

    for (int x : v) min_heap.push(x);
    std::cout << "heap top=" << min_heap.top() << "\n";
    return 0;
}
```

## 常见坑点

- `set`/`map` 比较器必须形成严格弱序，否则行为不正确。
- Lambda 捕获引用时要注意生命周期，避免悬垂引用。
- 比较器和排序规则要一致，特别是二分查找场景。

## 相关链接

- [[03_STL_Algorithms]]
- [[00_STL_Index|返回 STL 索引]]
