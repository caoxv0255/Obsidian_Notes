---
type: snippets
topic: biconnected_components_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/图论, 双连通分量, 割点, 割边, Snippets]
---

# 双连通分量模板

> 这里放无向图的桥、割点、点双和边双。

## 1) 桥与割点

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct LowLink {
    struct Edge {
        int to;
        int id;
    };

    int n;
    int edgeCount = 0;
    int timer = 0;
    vector<vector<Edge>> graph;
    vector<int> dfn;
    vector<int> low;
    vector<char> isCut;
    vector<char> isBridge;

    explicit LowLink(int n)
        : n(n), graph(n), dfn(n, 0), low(n, 0), isCut(n, 0), isBridge() {}

    void addEdge(int u, int v) {
        graph[u].push_back({v, edgeCount});
        graph[v].push_back({u, edgeCount});
        ++edgeCount;
    }

    void dfs(int node, int parentEdge) {
        dfn[node] = low[node] = ++timer;
        int childCount = 0;

        for (const auto& edge : graph[node]) {
            if (edge.id == parentEdge) continue;
            if (dfn[edge.to] == 0) {
                ++childCount;
                dfs(edge.to, edge.id);
                low[node] = min(low[node], low[edge.to]);
                if (parentEdge != -1 && low[edge.to] >= dfn[node]) {
                    isCut[node] = 1;
                }
                if (low[edge.to] > dfn[node]) {
                    isBridge[edge.id] = 1;
                }
            } else {
                low[node] = min(low[node], dfn[edge.to]);
            }
        }

        if (parentEdge == -1 && childCount > 1) {
            isCut[node] = 1;
        }
    }

    void build() {
        isBridge.assign(edgeCount, 0);
        for (int node = 0; node < n; ++node) {
            if (dfn[node] == 0) {
                dfs(node, -1);
            }
        }
    }
};
```

## 2) 边双连通分量

```cpp
#include <vector>
using namespace std;

struct EdgeBiconnectedComponents {
    LowLink lowLink;
    vector<int> componentId;

    explicit EdgeBiconnectedComponents(int n) : lowLink(n), componentId(n, -1) {}

    void addEdge(int u, int v) {
        lowLink.addEdge(u, v);
    }

    void dfsComponent(int node, int color) {
        componentId[node] = color;
        for (const auto& edge : lowLink.graph[node]) {
            if (lowLink.isBridge[edge.id] || componentId[edge.to] != -1) continue;
            dfsComponent(edge.to, color);
        }
    }

    vector<int> build() {
        lowLink.build();
        fill(componentId.begin(), componentId.end(), -1);

        int color = 0;
        for (int node = 0; node < lowLink.n; ++node) {
            if (componentId[node] == -1) {
                dfsComponent(node, color++);
            }
        }

        return componentId;
    }
};
```

## 使用建议

- 找桥、割点：LowLink
- 压缩边双分量：先找桥，再 DFS 染色
- 需要点双时，可以把 DFS 栈再补一层
