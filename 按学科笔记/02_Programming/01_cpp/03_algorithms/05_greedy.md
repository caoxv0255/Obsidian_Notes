---
type: concept
topic: algorithms_greedy
category: algorithms
difficulty: intermediate
prerequisites: [[03_Algorithms_Sorting_Searching]]
acm_relevant: true
created: 2026-04-25
status: complete
---

# 贪心算法 (Greedy)

## 核心定义

贪心算法在每一步都做当前看起来最优的选择，期望得到全局最优解。

## 可用条件

1. 贪心选择性质：局部最优可导向全局最优。
2. 最优子结构：子问题最优可拼接成原问题最优。

## 经典模型

- 区间调度（最多不重叠区间）
- Huffman 编码
- 最小生成树（Kruskal/Prim）
- Dijkstra（非负边）

## 代码示例：区间调度

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<std::pair<int, int>> seg = {{1, 3}, {2, 4}, {3, 5}, {0, 7}, {5, 9}};
    std::sort(seg.begin(), seg.end(), [](auto a, auto b) {
        return a.second < b.second;
    });

    int ans = 0;
    int last_end = -1e9;
    for (auto [l, r] : seg) {
        if (l >= last_end) {
            ++ans;
            last_end = r;
        }
    }

    std::cout << "max non-overlap=" << ans << "\n";
    return 0;
}
```

## 反例意识

如果问题存在“当前最优导致后续受限”，通常要转 DP 或图搜索。

## 相关链接

- [[04_Dynamic_Programming]]
- [[00_Algorithms_Index|返回算法索引]]
