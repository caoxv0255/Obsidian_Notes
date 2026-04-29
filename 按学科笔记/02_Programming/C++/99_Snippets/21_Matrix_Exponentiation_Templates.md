---
type: snippets
topic: matrix_exponentiation_templates
category: snippets
difficulty: intermediate
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数论, 矩阵快速幂, 递推, Snippets]
---

# 矩阵快速幂模板

> 适合线性递推、状态转移加速、图上计数。

## 1) 通用矩阵模板

```cpp
#include <vector>
using namespace std;

struct Matrix {
    int n;
    long long mod;
    vector<vector<long long>> value;

    Matrix(int n, long long mod, bool identity = false) : n(n), mod(mod), value(n, vector<long long>(n, 0)) {
        if (identity) {
            for (int index = 0; index < n; ++index) {
                value[index][index] = 1 % mod;
            }
        }
    }

    static Matrix identity(int n, long long mod) {
        return Matrix(n, mod, true);
    }
};

Matrix multiply(const Matrix& left, const Matrix& right) {
    Matrix result(left.n, left.mod);
    for (int row = 0; row < left.n; ++row) {
        for (int mid = 0; mid < left.n; ++mid) {
            if (left.value[row][mid] == 0) continue;
            for (int col = 0; col < left.n; ++col) {
                result.value[row][col] = (result.value[row][col] + left.value[row][mid] * right.value[mid][col]) % left.mod;
            }
        }
    }
    return result;
}

Matrix power(Matrix base, long long exponent) {
    Matrix result = Matrix::identity(base.n, base.mod);
    while (exponent > 0) {
        if (exponent & 1) {
            result = multiply(result, base);
        }
        base = multiply(base, base);
        exponent >>= 1;
    }
    return result;
}
```

## 2) 斐波那契示例

```cpp
long long fibonacci(long long n, long long mod) {
    if (n <= 1) return n % mod;

    Matrix base(2, mod);
    base.value[0][0] = 1;
    base.value[0][1] = 1;
    base.value[1][0] = 1;
    base.value[1][1] = 0;

    Matrix result = power(base, n - 1);
    return result.value[0][0] % mod;
}
```

## 使用建议

- 递推转移能写成矩阵乘法时，优先考虑矩阵快速幂
- 维度不宜太大，通常适合小状态数
- 线性递推、计数问题、图路径计数都很常见
