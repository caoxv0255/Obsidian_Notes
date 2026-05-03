---
type: snippets
topic: tarjan_scc_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/图论, Tarjan, Snippets]
---

# Tarjan 模板

> 重点放强连通分量、桥和割点，都是竞赛高频图论工具。

## 1) 强连通分量 SCC

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct TarjanSCC {
    int n;
    vector<vector<int>> graph;
    vector<int> dfn;
    vector<int> low;
    vector<int> inStack;
    vector<int> component;
    vector<int> stackNodes;
    int timer = 0;
    int componentCount = 0;

    explicit TarjanSCC(int n) : n(n), graph(n), dfn(n, 0), low(n, 0), inStack(n, 0), component(n, -1) {}

    void addEdge(int from, int to) {
        graph[from].push_back(to);
    }

    void dfs(int node) {
        dfn[node] = low[node] = ++timer;
        stackNodes.push_back(node);
        inStack[node] = 1;

        for (int next : graph[node]) {
            if (dfn[next] == 0) {
                dfs(next);
                low[node] = min(low[node], low[next]);
            } else if (inStack[next]) {
                low[node] = min(low[node], dfn[next]);
            }
        }

        if (low[node] == dfn[node]) {
            while (true) {
                int top = stackNodes.back();
                stackNodes.pop_back();
                inStack[top] = 0;
                component[top] = componentCount;
                if (top == node) break;
            }
            ++componentCount;
        }
    }

    vector<int> solve() {
        for (int node = 0; node < n; ++node) {
            if (dfn[node] == 0) {
                dfs(node);
            }
        }
        return component;
    }
};
```

## 2) 桥（无向图）

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct BridgeFinder {
    struct Edge {
        int to;
        int id;
    };

    int n;
    int edgeCount = 0;
    vector<vector<Edge>> graph;
    vector<int> dfn;
    vector<int> low;
    vector<pair<int, int>> bridges;
    int timer = 0;

    explicit BridgeFinder(int n) : n(n), graph(n), dfn(n, 0), low(n, 0) {}

    void addEdge(int u, int v) {
        graph[u].push_back({v, edgeCount});
        graph[v].push_back({u, edgeCount});
        ++edgeCount;
    }

    void dfs(int node, int parentEdge) {
        dfn[node] = low[node] = ++timer;
        for (const auto& edge : graph[node]) {
            if (edge.id == parentEdge) continue;
            if (dfn[edge.to] == 0) {
                dfs(edge.to, edge.id);
                low[node] = min(low[node], low[edge.to]);
                if (low[edge.to] > dfn[node]) {
                    bridges.push_back({node, edge.to});
                }
            } else {
                low[node] = min(low[node], dfn[edge.to]);
            }
        }
    }

    vector<pair<int, int>> solve() {
        for (int node = 0; node < n; ++node) {
            if (dfn[node] == 0) {
                dfs(node, -1);
            }
        }
        return bridges;
    }
};
```

## 使用建议

- 有向图强连通：Tarjan SCC
- 无向图关键边：桥
- 无向图关键点：割点可以沿着 low-link 思路继续扩展
