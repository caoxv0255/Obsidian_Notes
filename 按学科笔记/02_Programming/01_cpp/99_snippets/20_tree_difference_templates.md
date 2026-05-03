---
type: snippets
topic: tree_difference_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/图论, 树上差分, LCA, Snippets]
---

# 树上差分模板

> 常见于多次路径加、统计边/点被经过的次数。

## 1) 先预处理，再批量加，最后统一汇总

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct TreeDifference {
    int n;
    int logSize;
    vector<vector<int>> graph;
    vector<vector<int>> up;
    vector<int> parent;
    vector<int> depth;
    vector<long long> diff;
    vector<long long> answer;

    explicit TreeDifference(int n)
        : n(n), logSize(1), graph(n), parent(n, -1), depth(n, 0), diff(n, 0), answer(n, 0) {
        while ((1 << logSize) <= n) {
            ++logSize;
        }
        up.assign(logSize, vector<int>(n, -1));
    }

    void addEdge(int u, int v) {
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    void prepare(int root = 0) {
        depth[root] = 0;
        dfsBuild(root, -1);
    }

    void dfsBuild(int node, int parentNode) {
        parent[node] = parentNode;
        up[0][node] = parentNode;
        for (int level = 1; level < logSize; ++level) {
            int mid = up[level - 1][node];
            up[level][node] = mid == -1 ? -1 : up[level - 1][mid];
        }

        for (int next : graph[node]) {
            if (next == parentNode) continue;
            depth[next] = depth[node] + 1;
            dfsBuild(next, node);
        }
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

    void addPathNode(int left, int right, long long delta) {
        int ancestor = lca(left, right);
        diff[left] += delta;
        diff[right] += delta;
        diff[ancestor] -= delta;
        if (parent[ancestor] != -1) {
            diff[parent[ancestor]] -= delta;
        }
    }

    void addPathEdge(int left, int right, long long delta) {
        int ancestor = lca(left, right);
        diff[left] += delta;
        diff[right] += delta;
        diff[ancestor] -= 2 * delta;
    }

    long long dfsAccumulate(int node, int parentNode) {
        long long total = diff[node];
        for (int next : graph[node]) {
            if (next == parentNode) continue;
            total += dfsAccumulate(next, node);
        }
        answer[node] = total;
        return total;
    }

    vector<long long> collect(int root = 0) {
        fill(answer.begin(), answer.end(), 0);
        dfsAccumulate(root, -1);
        return answer;
    }
};
```

## 使用建议

- 多次路径加、最后统一统计：树上差分
- 点权统计用 `addPathNode`
- 边权统计用 `addPathEdge`
- 使用顺序：`prepare` -> 批量 `addPath*` -> `collect`
