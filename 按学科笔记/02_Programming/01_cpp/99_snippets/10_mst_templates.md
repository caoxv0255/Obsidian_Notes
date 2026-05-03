---
type: snippets
topic: mst_templates
category: snippets
difficulty: intermediate
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/图论, 最小生成树, Kruskal, Prim, Snippets]
---

# 最小生成树模板

> 竞赛里最常用的是 Kruskal，Prim 作为补充。

## 1) Kruskal

```cpp
#include <algorithm>
#include <numeric>
#include <vector>
using namespace std;

struct DisjointSetUnion {
    vector<int> parent;
    vector<int> size;

    explicit DisjointSetUnion(int n) : parent(n), size(n, 1) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int node) {
        if (parent[node] == node) return node;
        return parent[node] = find(parent[node]);
    }

    bool unite(int left, int right) {
        left = find(left);
        right = find(right);
        if (left == right) return false;
        if (size[left] < size[right]) swap(left, right);
        parent[right] = left;
        size[left] += size[right];
        return true;
    }
};

struct Edge {
    int u;
    int v;
    long long w;
};

long long kruskal(int n, vector<Edge> edges) {
    sort(edges.begin(), edges.end(), [](const Edge& left, const Edge& right) {
        return left.w < right.w;
    });

    DisjointSetUnion dsu(n);
    long long totalWeight = 0;
    int usedEdges = 0;

    for (const auto& edge : edges) {
        if (dsu.unite(edge.u, edge.v)) {
            totalWeight += edge.w;
            ++usedEdges;
            if (usedEdges == n - 1) break;
        }
    }

    return usedEdges == n - 1 ? totalWeight : -1;
}
```

## 2) Prim（稠密图）

```cpp
#include <algorithm>
#include <limits>
#include <vector>
using namespace std;

long long prim(const vector<vector<long long>>& graph) {
    int n = static_cast<int>(graph.size());
    vector<long long> minEdge(n, numeric_limits<long long>::max());
    vector<bool> used(n, false);
    minEdge[0] = 0;

    long long totalWeight = 0;

    for (int step = 0; step < n; ++step) {
        int vertex = -1;
        for (int index = 0; index < n; ++index) {
            if (!used[index] && (vertex == -1 || minEdge[index] < minEdge[vertex])) {
                vertex = index;
            }
        }

        if (vertex == -1 || minEdge[vertex] == numeric_limits<long long>::max()) {
            return -1;
        }

        used[vertex] = true;
        totalWeight += minEdge[vertex];

        for (int next = 0; next < n; ++next) {
            if (!used[next] && graph[vertex][next] < minEdge[next]) {
                minEdge[next] = graph[vertex][next];
            }
        }
    }

    return totalWeight;
}
```

## 使用建议

- 稀疏图：优先 Kruskal
- 稠密图：可用 Prim
- 动态连通性判断：Kruskal + 并查集最顺手
