---
type: snippets
topic: ntt_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数论, NTT, 多项式, Snippets]
---

# NTT 模板

> 用于多项式卷积和大规模乘法。

## 1) 原地 NTT

```cpp
#include <algorithm>
#include <utility>
#include <vector>
using namespace std;

static const int MOD = 998244353;
static const int G = 3;

long long nttPow(long long base, long long exponent) {
    long long result = 1;
    while (exponent > 0) {
        if (exponent & 1) {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exponent >>= 1;
    }
    return result;
}

void ntt(vector<int>& values, bool invert) {
    int n = static_cast<int>(values.size());
    for (int i = 1, j = 0; i < n; ++i) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) {
            j ^= bit;
        }
        j ^= bit;
        if (i < j) {
            swap(values[i], values[j]);
        }
    }

    for (int length = 2; length <= n; length <<= 1) {
        long long wLen = nttPow(G, (MOD - 1) / length);
        if (invert) {
            wLen = nttPow(wLen, MOD - 2);
        }

        for (int left = 0; left < n; left += length) {
            long long w = 1;
            for (int index = 0; index < length / 2; ++index) {
                int u = values[left + index];
                int v = static_cast<int>(w * values[left + index + length / 2] % MOD);
                values[left + index] = u + v < MOD ? u + v : u + v - MOD;
                values[left + index + length / 2] = u - v >= 0 ? u - v : u - v + MOD;
                w = w * wLen % MOD;
            }
        }
    }

    if (invert) {
        long long invN = nttPow(n, MOD - 2);
        for (int& value : values) {
            value = static_cast<int>(value * invN % MOD);
        }
    }
}

vector<int> convolution(vector<int> left, vector<int> right) {
    int resultSize = static_cast<int>(left.size() + right.size() - 1);
    int n = 1;
    while (n < resultSize) {
        n <<= 1;
    }

    left.resize(n);
    right.resize(n);

    ntt(left, false);
    ntt(right, false);
    for (int index = 0; index < n; ++index) {
        left[index] = static_cast<int>(1LL * left[index] * right[index] % MOD);
    }
    ntt(left, true);

    left.resize(resultSize);
    return left;
}
```

## 使用建议

- 模数通常使用 `998244353`
- 不能用这个模数时，考虑 CRT 或其他卷积方法
- 多项式乘法、卷积优化、计数题常见
