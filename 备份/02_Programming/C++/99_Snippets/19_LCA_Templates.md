---
type: snippets
topic: lca_templates
category: snippets
difficulty: intermediate
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/图论, LCA, 倍增, Snippets]
---

# LCA 模板

> 树上距离、祖先判断、树上路径题的基础设施。

## 1) 倍增 LCA

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct LCATree {
    int n;
    int logSize;
    vector<vector<int>> graph;
    vector<vector<int>> up;
    vector<int> depth;

    explicit LCATree(int n) : n(n), logSize(1), graph(n), depth(n, 0) {
        while ((1 << logSize) <= n) {
            ++logSize;
        }
        up.assign(logSize, vector<int>(n, -1));
    }

    void addEdge(int u, int v) {
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    void dfs(int node, int parent) {
        up[0][node] = parent;
        for (int level = 1; level < logSize; ++level) {
            int mid = up[level - 1][node];
            up[level][node] = mid == -1 ? -1 : up[level - 1][mid];
        }

        for (int next : graph[node]) {
            if (next == parent) continue;
            depth[next] = depth[node] + 1;
            dfs(next, node);
        }
    }

    void build(int root = 0) {
        depth[root] = 0;
        dfs(root, -1);
    }

    int lift(int node, int steps) const {
        for (int level = 0; level < logSize && node != -1; ++level) {
            if (steps & (1 << level)) {
                node = up[level][node];
            }
        }
        return node;
    }

    int lca(int left, int right) const {
        if (depth[left] < depth[right]) {
            swap(left, right);
        }

        left = lift(left, depth[left] - depth[right]);
        if (left == right) return left;

        for (int level = logSize - 1; level >= 0; --level) {
            if (up[level][left] != up[level][right]) {
                left = up[level][left];
                right = up[level][right];
            }
        }

        return up[0][left];
    }

    int distance(int left, int right) const {
        int ancestor = lca(left, right);
        return depth[left] + depth[right] - 2 * depth[ancestor];
    }
};
```

## 使用建议

- 判断祖先关系：先求 LCA，再看深度
- 求树上两点距离：`depth[u] + depth[v] - 2 * depth[lca]`
- 如果题目有大量动态修改，LCA 可能不够，要看链剖分或 Link-Cut Tree
