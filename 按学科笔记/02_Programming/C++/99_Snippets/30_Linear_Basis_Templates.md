---
type: snippets
topic: linear_basis_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数据结构, 线性基, 异或, Snippets]
---

# 线性基模板

> 处理异或最大值、可表示性、不同子集异或值等问题。

## 1) 基础线性基

```cpp
#include <algorithm>
#include <array>
#include <vector>
using namespace std;

struct LinearBasis {
    static constexpr int MAX_BITS = 60;
    array<long long, MAX_BITS + 1> basis{};
    int rank = 0;

    bool insert(long long value) {
        for (int bit = MAX_BITS; bit >= 0; --bit) {
            if (((value >> bit) & 1LL) == 0) continue;
            if (basis[bit] == 0) {
                basis[bit] = value;
                ++rank;
                return true;
            }
            value ^= basis[bit];
        }
        return false;
    }

    bool canRepresent(long long value) const {
        for (int bit = MAX_BITS; bit >= 0; --bit) {
            if (((value >> bit) & 1LL) == 0) continue;
            if (basis[bit] == 0) return false;
            value ^= basis[bit];
        }
        return true;
    }

    long long maximize(long long value = 0) const {
        long long result = value;
        for (int bit = MAX_BITS; bit >= 0; --bit) {
            if (basis[bit] == 0) continue;
            result = max(result, result ^ basis[bit]);
        }
        return result;
    }

    vector<long long> rebuild() const {
        vector<long long> values;
        for (int bit = MAX_BITS; bit >= 0; --bit) {
            if (basis[bit] != 0) {
                values.push_back(basis[bit]);
            }
        }
        return values;
    }
};
```

## 使用建议

- 求异或最大值：直接 `maximize`
- 判断某个值能否由子集异或得到：`canRepresent`
- 题目需要区间线性基时，可以把线性基和倍增/主席树结合起来
