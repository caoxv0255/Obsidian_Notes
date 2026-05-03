---
type: snippets
topic: fft_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数论, FFT, 卷积, Snippets]
---

# FFT 模板

> 适合实数卷积、任意模数前的浮点卷积、图像/信号类变形题。

## 1) 迭代版 FFT

```cpp
#include <algorithm>
#include <complex>
#include <vector>
using namespace std;

using Complex = complex<double>;
const double PI = acos(-1.0);

void fft(vector<Complex>& values, bool invert) {
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
        double angle = 2.0 * PI / length * (invert ? -1.0 : 1.0);
        Complex rootOfUnity(cos(angle), sin(angle));
        for (int left = 0; left < n; left += length) {
            Complex factor(1.0, 0.0);
            for (int index = 0; index < length / 2; ++index) {
                Complex u = values[left + index];
                Complex v = factor * values[left + index + length / 2];
                values[left + index] = u + v;
                values[left + index + length / 2] = u - v;
                factor *= rootOfUnity;
            }
        }
    }

    if (invert) {
        for (Complex& value : values) {
            value /= n;
        }
    }
}

vector<long long> convolution(const vector<int>& left, const vector<int>& right) {
    int resultSize = static_cast<int>(left.size() + right.size() - 1);
    int n = 1;
    while (n < resultSize) {
        n <<= 1;
    }

    vector<Complex> a(n), b(n);
    for (int i = 0; i < static_cast<int>(left.size()); ++i) a[i] = left[i];
    for (int i = 0; i < static_cast<int>(right.size()); ++i) b[i] = right[i];

    fft(a, false);
    fft(b, false);
    for (int i = 0; i < n; ++i) {
        a[i] *= b[i];
    }
    fft(a, true);

    vector<long long> result(resultSize);
    for (int i = 0; i < resultSize; ++i) {
        result[i] = static_cast<long long>(llround(a[i].real()));
    }
    return result;
}
```

## 使用建议

- 实数卷积、字符串统计、乘法近似问题：FFT
- 需要整数模卷积时，优先考虑 NTT
- 浮点误差要靠 `round` 或 `llround` 收尾
