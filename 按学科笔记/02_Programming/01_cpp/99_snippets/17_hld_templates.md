---
type: snippets
topic: hld_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/图论, 树链剖分, 线段树, Snippets]
---

# 树链剖分模板

> 常见于树上路径查询、路径修改、子树查询。

## 1) 路径和 + 子树和

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct SegmentTree {
    int n;
    vector<long long> tree;

    explicit SegmentTree(int n) : n(n), tree(4 * n, 0) {}

    void build(int node, int left, int right, const vector<long long>& values) {
        if (left == right) {
            tree[node] = values[left];
            return;
        }

        int mid = left + (right - left) / 2;
        build(node * 2, left, mid, values);
        build(node * 2 + 1, mid + 1, right, values);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    void update(int node, int left, int right, int index, long long value) {
        if (left == right) {
            tree[node] = value;
            return;
        }

        int mid = left + (right - left) / 2;
        if (index <= mid) update(node * 2, left, mid, index, value);
        else update(node * 2 + 1, mid + 1, right, index, value);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    long long query(int node, int left, int right, int queryLeft, int queryRight) const {
        if (queryRight < left || right < queryLeft) return 0;
        if (queryLeft <= left && right <= queryRight) return tree[node];
        int mid = left + (right - left) / 2;
        return query(node * 2, left, mid, queryLeft, queryRight) +
               query(node * 2 + 1, mid + 1, right, queryLeft, queryRight);
    }
};

struct HeavyLightDecomposition {
    int n;
    vector<vector<int>> graph;
    vector<int> parent;
    vector<int> depth;
    vector<int> heavyChild;
    vector<int> subtreeSize;
    vector<int> head;
    vector<int> position;
    vector<int> reversePosition;
    int currentPosition = 0;
    SegmentTree segmentTree;

    explicit HeavyLightDecomposition(int n)
        : n(n), graph(n), parent(n, -1), depth(n, 0), heavyChild(n, -1), subtreeSize(n, 0),
          head(n, 0), position(n, 0), reversePosition(n, 0), segmentTree(n) {}

    void addEdge(int u, int v) {
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int dfs1(int node, int parentNode) {
        parent[node] = parentNode;
        subtreeSize[node] = 1;
        int bestSize = 0;

        for (int next : graph[node]) {
            if (next == parentNode) continue;
            depth[next] = depth[node] + 1;
            int childSize = dfs1(next, node);
            subtreeSize[node] += childSize;
            if (childSize > bestSize) {
                bestSize = childSize;
                heavyChild[node] = next;
            }
        }

        return subtreeSize[node];
    }

    void dfs2(int node, int chainHead) {
        head[node] = chainHead;
        position[node] = currentPosition;
        reversePosition[currentPosition] = node;
        ++currentPosition;

        if (heavyChild[node] != -1) {
            dfs2(heavyChild[node], chainHead);
        }

        for (int next : graph[node]) {
            if (next == parent[node] || next == heavyChild[node]) continue;
            dfs2(next, next);
        }
    }

    void build(int root, const vector<long long>& values) {
        depth[root] = 0;
        dfs1(root, -1);
        currentPosition = 0;
        dfs2(root, root);

        vector<long long> orderedValues(n);
        for (int node = 0; node < n; ++node) {
            orderedValues[position[node]] = values[node];
        }
        segmentTree.build(1, 0, n - 1, orderedValues);
    }

    void updateNode(int node, long long value) {
        segmentTree.update(1, 0, n - 1, position[node], value);
    }

    long long queryPath(int leftNode, int rightNode) const {
        long long answer = 0;
        int u = leftNode;
        int v = rightNode;

        while (head[u] != head[v]) {
            if (depth[head[u]] < depth[head[v]]) swap(u, v);
            answer += segmentTree.query(1, 0, n - 1, position[head[u]], position[u]);
            u = parent[head[u]];
        }

        if (depth[u] > depth[v]) swap(u, v);
        answer += segmentTree.query(1, 0, n - 1, position[u], position[v]);
        return answer;
    }

    long long querySubtree(int node) const {
        return segmentTree.query(1, 0, n - 1, position[node], position[node] + subtreeSize[node] - 1);
    }
};
```

## 使用建议

- 树上路径查询：树链剖分
- 树上子树查询：HLD 也能顺手支持
- 如果只是静态倍增 LCA，别硬上 HLD
