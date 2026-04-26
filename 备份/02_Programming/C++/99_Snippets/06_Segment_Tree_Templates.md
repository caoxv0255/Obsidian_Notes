---
type: snippets
topic: segment_tree_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/线段树, 算法/模板, Snippets]
---

# 线段树模板

> 只保留比赛里最常用的两类：点修改区间查询、区间加区间查。

## 1) 点修改 + 区间和查询

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct SegmentTree {
    int n;
    vector<long long> tree;

    explicit SegmentTree(const vector<int>& values) {
        n = static_cast<int>(values.size());
        tree.assign(4 * n, 0);
        if (n > 0) build(1, 0, n - 1, values);
    }

    void build(int node, int left, int right, const vector<int>& values) {
        if (left == right) {
            tree[node] = values[left];
            return;
        }

        int mid = left + (right - left) / 2;
        build(node * 2, left, mid, values);
        build(node * 2 + 1, mid + 1, right, values);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    void update(int node, int left, int right, int index, int value) {
        if (left == right) {
            tree[node] = value;
            return;
        }

        int mid = left + (right - left) / 2;
        if (index <= mid) {
            update(node * 2, left, mid, index, value);
        } else {
            update(node * 2 + 1, mid + 1, right, index, value);
        }
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
```

## 2) 区间加 + 区间和查询

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct LazySegmentTree {
    int n;
    vector<long long> tree;
    vector<long long> lazy;

    explicit LazySegmentTree(const vector<int>& values) {
        n = static_cast<int>(values.size());
        tree.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
        if (n > 0) build(1, 0, n - 1, values);
    }

    void build(int node, int left, int right, const vector<int>& values) {
        if (left == right) {
            tree[node] = values[left];
            return;
        }

        int mid = left + (right - left) / 2;
        build(node * 2, left, mid, values);
        build(node * 2 + 1, mid + 1, right, values);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    void apply(int node, int left, int right, long long delta) {
        tree[node] += delta * (right - left + 1);
        lazy[node] += delta;
    }

    void push(int node, int left, int right) {
        if (lazy[node] == 0 || left == right) return;
        int mid = left + (right - left) / 2;
        apply(node * 2, left, mid, lazy[node]);
        apply(node * 2 + 1, mid + 1, right, lazy[node]);
        lazy[node] = 0;
    }

    void rangeAdd(int node, int left, int right, int queryLeft, int queryRight, long long delta) {
        if (queryRight < left || right < queryLeft) return;
        if (queryLeft <= left && right <= queryRight) {
            apply(node, left, right, delta);
            return;
        }

        push(node, left, right);
        int mid = left + (right - left) / 2;
        rangeAdd(node * 2, left, mid, queryLeft, queryRight, delta);
        rangeAdd(node * 2 + 1, mid + 1, right, queryLeft, queryRight, delta);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }

    long long rangeSum(int node, int left, int right, int queryLeft, int queryRight) {
        if (queryRight < left || right < queryLeft) return 0;
        if (queryLeft <= left && right <= queryRight) return tree[node];

        push(node, left, right);
        int mid = left + (right - left) / 2;
        return rangeSum(node * 2, left, mid, queryLeft, queryRight) +
               rangeSum(node * 2 + 1, mid + 1, right, queryLeft, queryRight);
    }
};
```

## 3) Sparse Table（RMQ）

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct SparseTable {
    int n;
    vector<int> logs;
    vector<vector<int>> st;

    explicit SparseTable(const vector<int>& values) {
        n = static_cast<int>(values.size());
        logs.assign(n + 1, 0);
        for (int i = 2; i <= n; ++i) {
            logs[i] = logs[i / 2] + 1;
        }

        int maxLog = logs[n] + 1;
        st.assign(maxLog, vector<int>(n));
        if (n == 0) return;

        st[0] = values;
        for (int level = 1; level < maxLog; ++level) {
            for (int index = 0; index + (1 << level) <= n; ++index) {
                st[level][index] = min(st[level - 1][index],
                                       st[level - 1][index + (1 << (level - 1))]);
            }
        }
    }

    int rangeMin(int left, int right) const {
        int level = logs[right - left + 1];
        return min(st[level][left], st[level][right - (1 << level) + 1]);
    }
};
```

## 使用建议

- 区间和 / 区间最值：线段树
- 静态 RMQ：Sparse Table
- 线段树模板优先掌握“点改区查”和“区加区查”两种
