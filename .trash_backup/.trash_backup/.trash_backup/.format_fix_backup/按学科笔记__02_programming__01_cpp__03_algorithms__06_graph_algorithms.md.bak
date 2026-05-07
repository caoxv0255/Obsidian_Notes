---
type: concept
topic: algorithms_graph
category: algorithms
difficulty: advanced
prerequisites: [[03_Algorithms_Sorting_Searching]], [[05_Greedy]]
acm_relevant: true
created: 2026-04-25
status: complete
---

# 图算法 (Graph Algorithms)

## 核心清单

1. 图存储：邻接表、邻接矩阵
2. 遍历：BFS、DFS
3. 最短路：Dijkstra、Bellman-Ford、Floyd
4. 最小生成树：Kruskal、Prim
5. DAG：拓扑排序
6. 联通性：并查集、强连通分量（Tarjan）

## 复杂度速记

- BFS/DFS：$O(n + m)$
- Dijkstra（堆优化）：$O((n + m) \log n)$
- Kruskal：$O(m \log m)$

## 代码示例：Dijkstra

```cpp
#include <iostream>
#include <queue>
#include <utility>
#include <vector>

int main() {
    int n = 5;
    std::vector<std::vector<std::pair<int, int>>> g(n);
    auto add_edge = [&](int u, int v, int w) {
        g[u].push_back({v, w});
        g[v].push_back({u, w});
    };

    add_edge(0, 1, 2);
    add_edge(1, 2, 3);
    add_edge(0, 3, 6);
    add_edge(3, 4, 1);
    add_edge(2, 4, 2);

    const int INF = 1e9;
    std::vector<int> dist(n, INF);
    dist[0] = 0;

    using Node = std::pair<int, int>; // {dist, vertex}
    std::priority_queue<Node, std::vector<Node>, std::greater<Node>> pq;
    pq.push({0, 0});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d != dist[u]) continue;

        for (auto [v, w] : g[u]) {
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }

    std::cout << "dist(0->4)=" << dist[4] << "\n";
    return 0;
}
```

## 注意事项

- Dijkstra 不能处理负权边。
- 稠密图小规模可考虑 Floyd，稀疏图优先堆优化 Dijkstra。

## 相关链接

- [[05_Greedy]]
- [[00_Algorithms_Index|返回算法索引]]
