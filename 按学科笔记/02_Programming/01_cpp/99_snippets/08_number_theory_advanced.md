---
type: snippets
topic: number_theory_advanced
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数论, NTT, 矩阵快速幂, Snippets]
---

# 进阶数论模板

> 这页放比基础数论更常用的进阶工具：矩阵快速幂、NTT 等。

## 1) 矩阵快速幂

```cpp
#include <array>
using namespace std;

struct Matrix2x2 {
    long long a00 = 1, a01 = 0, a10 = 0, a11 = 1;
};

Matrix2x2 multiply(const Matrix2x2& left, const Matrix2x2& right, long long mod) {
    Matrix2x2 result;
    result.a00 = (left.a00 * right.a00 + left.a01 * right.a10) % mod;
    result.a01 = (left.a00 * right.a01 + left.a01 * right.a11) % mod;
    result.a10 = (left.a10 * right.a00 + left.a11 * right.a10) % mod;
    result.a11 = (left.a10 * right.a01 + left.a11 * right.a11) % mod;
    return result;
}

Matrix2x2 matrixPower(Matrix2x2 base, long long exponent, long long mod) {
    Matrix2x2 result;
    while (exponent > 0) {
        if (exponent & 1) {
            result = multiply(result, base, mod);
        }
        base = multiply(base, base, mod);
        exponent >>= 1;
    }
    return result;
}
```

## 2) NTT（卷积）

```cpp
#include <algorithm>
#include <vector>
using namespace std;

static const int MOD = 998244353;
static const int G = 3;

long long modPow(long long base, long long exponent) {
    long long result = 1;
    base %= MOD;
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
        if (i < j) swap(values[i], values[j]);
    }

    for (int length = 2; length <= n; length <<= 1) {
        long long wLen = modPow(G, (MOD - 1) / length);
        if (invert) {
            wLen = modPow(wLen, MOD - 2);
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
        long long invN = modPow(n, MOD - 2);
        for (int& value : values) {
            value = static_cast<int>(value * invN % MOD);
        }
    }
}

vector<int> convolution(vector<int> left, vector<int> right) {
    int n = 1;
    while (n < static_cast<int>(left.size() + right.size() - 1)) {
        n <<= 1;
    }
    left.resize(n);
    right.resize(n);

    ntt(left, false);
    ntt(right, false);
    for (int i = 0; i < n; ++i) {
        left[i] = static_cast<int>(1LL * left[i] * right[i] % MOD);
    }
    ntt(left, true);
    return left;
}
```

## 使用建议

- 矩阵快速幂常用于斐波那契、递推式加速
- NTT 主要处理多项式卷积和大整数乘法
- 如果模数不合适，先考虑 CRT 或换用其他卷积方法
