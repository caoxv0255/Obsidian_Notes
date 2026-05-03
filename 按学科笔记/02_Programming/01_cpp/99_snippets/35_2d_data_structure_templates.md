---
type: snippets
topic: two_dimensional_data_structure_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数据结构, 树套树, 二维树状数组, Snippets]
---

# 树套树 / 二维数据结构模板

> 常用于二维点修改 + 矩形查询，或离线后的二维统计。

## 1) 二维树状数组

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct Fenwick2D {
    int n;
    int m;
    vector<vector<long long>> tree;

    Fenwick2D(int n, int m) : n(n), m(m), tree(n + 1, vector<long long>(m + 1, 0)) {}

    void add(int x, int y, long long delta) {
        for (int i = x; i <= n; i += i & -i) {
            for (int j = y; j <= m; j += j & -j) {
                tree[i][j] += delta;
            }
        }
    }

    long long sum(int x, int y) const {
        long long result = 0;
        for (int i = x; i > 0; i -= i & -i) {
            for (int j = y; j > 0; j -= j & -j) {
                result += tree[i][j];
            }
        }
        return result;
    }

    long long query(int x1, int y1, int x2, int y2) const {
        return sum(x2, y2) - sum(x1 - 1, y2) - sum(x2, y1 - 1) + sum(x1 - 1, y1 - 1);
    }
};
```

## 2) 说明

```cpp
// 如果题目需要更强的“树套树”，通常是二维线段树或 Fenwick + 坐标压缩。
// 这份模板优先覆盖竞赛里最常见的二维点改、矩形和查询。
```

## 使用建议

- 二维点修改 + 矩形查询：二维 BIT
- 题目坐标很大时，先离散化再建树
- 如果需要更强版本，可以再扩展二维线段树
