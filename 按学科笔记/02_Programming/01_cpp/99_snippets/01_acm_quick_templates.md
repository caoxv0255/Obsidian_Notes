---
type: snippets
topic: acm_quick_templates
category: snippets
difficulty: intermediate
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/模板, 算法/工具, Snippets]
---

# ACM 快速模板

> 放“比赛里随手就能抄”的短模板，优先覆盖高频、低风险、可复用的代码。

## 1) 快速 IO

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
}
```

## 2) 调试输出

```cpp
#include <iostream>
#include <vector>
using namespace std;

#ifdef LOCAL
#define debug(x) cerr << #x << " = " << (x) << '\n'
#else
#define debug(x) ((void)0)
#endif
```

## 3) 并查集 DSU

```cpp
#include <algorithm>
#include <numeric>
#include <vector>
using namespace std;

struct DSU {
    vector<int> parent, size;

    DSU(int n) : parent(n), size(n, 1) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) swap(a, b);
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
};
```

## 4) 树状数组 Fenwick

```cpp
#include <vector>
using namespace std;

struct Fenwick {
    int n;
    vector<long long> bit;

    Fenwick(int n) : n(n), bit(n + 1, 0) {}

    void add(int index, long long delta) {
        for (; index <= n; index += index & -index) {
            bit[index] += delta;
        }
    }

    long long sum(int index) const {
        long long result = 0;
        for (; index > 0; index -= index & -index) {
            result += bit[index];
        }
        return result;
    }
};
```

## 5) 离散化

```cpp
#include <algorithm>
#include <vector>
using namespace std;

vector<int> compress(vector<int> values) {
    sort(values.begin(), values.end());
    values.erase(unique(values.begin(), values.end()), values.end());
    return values;
}
```

## 6) 二分答案骨架

```cpp
bool check(long long mid) {
    return mid >= 0;
}

long long binary_search_answer(long long left, long long right) {
    while (left < right) {
        long long mid = left + (right - left) / 2;
        if (check(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

## 使用建议

- 只放真正高频的模板，避免索引臃肿
- 每个模板都尽量保持“能直接贴进题目里改两行就能用”
- 代码块优先保持短、清晰、无多余抽象
