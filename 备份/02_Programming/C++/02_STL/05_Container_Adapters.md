---
type: concept
topic: stl_adapters
category: stl
difficulty: intermediate
prerequisites: [[01_Containers]]
acm_relevant: true
created: 2026-04-25
status: complete
---

# 容器适配器 (stack/queue/priority_queue)

## 核心定义

容器适配器不是新容器结构，而是对底层容器进行接口约束后的封装。

- `stack`：后进先出（LIFO）
- `queue`：先进先出（FIFO）
- `priority_queue`：堆，按优先级取元素

## 底层容器

- `stack` 默认 `deque`
- `queue` 默认 `deque`
- `priority_queue` 默认 `vector`（堆操作）

## 代码示例

```cpp
#include <iostream>
#include <queue>
#include <stack>

int main() {
    std::stack<int> st;
    st.push(1);
    st.push(2);
    std::cout << st.top() << "\n"; // 2

    std::queue<int> q;
    q.push(10);
    q.push(20);
    std::cout << q.front() << " " << q.back() << "\n";

    std::priority_queue<int> pq;
    pq.push(3);
    pq.push(1);
    pq.push(5);
    std::cout << pq.top() << "\n"; // 5
    return 0;
}
```

## ACM 高频场景

- `stack`：括号匹配、单调栈
- `queue`：BFS、拓扑排序
- `priority_queue`：Dijkstra、TopK、区间调度

## 注意事项

- 适配器不提供迭代器，不能像 `vector` 一样遍历。
- 最小堆写法：

```cpp
std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
```

## 相关链接

- [[01_Containers]]
- [[00_STL_Index|返回 STL 索引]]
