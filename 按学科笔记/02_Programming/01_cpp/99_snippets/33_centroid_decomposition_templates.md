---
type: snippets
topic: centroid_decomposition_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/图论, 点分治, 树分治, Snippets]
---

# 点分治模板

> 适合树上路径统计、树上距离计数、树上最短/最长路径类问题。

## 1) 经典点分治骨架

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct CentroidDecomposition {
    int n;
    vector<vector<pair<int, int>>> graph;
    vector<int> subtreeSize;
    vector<int> removed;

    explicit CentroidDecomposition(int n)
        : n(n), graph(n), subtreeSize(n, 0), removed(n, 0) {}

    void addEdge(int u, int v, int weight = 1) {
        graph[u].push_back({v, weight});
        graph[v].push_back({u, weight});
    }

    int computeSize(int node, int parent) {
        subtreeSize[node] = 1;
        for (const auto& edge : graph[node]) {
            int next = edge.first;
            if (next == parent || removed[next]) continue;
            subtreeSize[node] += computeSize(next, node);
        }
        return subtreeSize[node];
    }

    int findCentroid(int node, int parent, int totalSize) {
        for (const auto& edge : graph[node]) {
            int next = edge.first;
            if (next == parent || removed[next]) continue;
            if (subtreeSize[next] * 2 > totalSize) {
                return findCentroid(next, node, totalSize);
            }
        }
        return node;
    }

    void collectDistances(int node, int parent, int distance, vector<int>& distances) {
        distances.push_back(distance);
        for (const auto& edge : graph[node]) {
            int next = edge.first;
            int weight = edge.second;
            if (next == parent || removed[next]) continue;
            collectDistances(next, node, distance + weight, distances);
        }
    }

    void decompose(int entryPoint) {
        int totalSize = computeSize(entryPoint, -1);
        int centroid = findCentroid(entryPoint, -1, totalSize);
        removed[centroid] = 1;

        // 在这里处理经过 centroid 的路径统计

        for (const auto& edge : graph[centroid]) {
            int next = edge.first;
            if (removed[next]) continue;
            decompose(next);
        }
    }
};
```

## 使用建议

- 树上距离计数、树上路径统计：点分治
- 需要“经过某个中心点”聚合答案时很合适
- 如果只做单点查询，LCA 通常更轻
