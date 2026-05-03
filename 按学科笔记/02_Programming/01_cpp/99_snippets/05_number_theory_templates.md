---
type: snippets
topic: number_theory_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数论, 算法/模板, Snippets]
---

# 数论模板

> 只保留 ACM 里最常见的数论工具，目标是“写得快、错得少”。

## 1) gcd / lcm

```cpp
#include <numeric>
using namespace std;

long long gcdll(long long a, long long b) {
    return std::gcd(a, b);
}

long long lcmll(long long a, long long b) {
    return a / gcdll(a, b) * b;
}
```

## 2) 快速幂

```cpp
using ll = long long;

ll modPow(ll base, ll exponent, ll mod) {
    ll result = 1 % mod;
    base %= mod;
    while (exponent > 0) {
        if (exponent & 1) {
            result = result * base % mod;
        }
        base = base * base % mod;
        exponent >>= 1;
    }
    return result;
}
```

## 3) 扩展欧几里得与逆元

```cpp
using ll = long long;

ll exgcd(ll a, ll b, ll& x, ll& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    ll x1 = 0, y1 = 0;
    ll g = exgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - a / b * y1;
    return g;
}

ll modInverse(ll a, ll mod) {
    ll x = 0, y = 0;
    ll g = exgcd(a, mod, x, y);
    if (g != 1) return -1;
    x %= mod;
    if (x < 0) x += mod;
    return x;
}
```

## 4) 筛法

```cpp
#include <vector>
using namespace std;

vector<int> linearSieve(int n) {
    vector<int> primes;
    vector<int> isComposite(n + 1, 0);
    for (int i = 2; i <= n; ++i) {
        if (!isComposite[i]) {
            primes.push_back(i);
        }
        for (int prime : primes) {
            long long multiple = 1LL * i * prime;
            if (multiple > n) break;
            isComposite[multiple] = 1;
            if (i % prime == 0) break;
        }
    }
    return primes;
}
```

## 5) 组合数预处理

```cpp
#include <vector>
using namespace std;

struct Combinatorics {
    int mod;
    vector<long long> fact;
    vector<long long> invFact;

    Combinatorics(int n, int mod) : mod(mod), fact(n + 1, 1), invFact(n + 1, 1) {
        for (int i = 1; i <= n; ++i) {
            fact[i] = fact[i - 1] * i % mod;
        }
        invFact[n] = modPow(fact[n], mod - 2, mod);
        for (int i = n; i >= 1; --i) {
            invFact[i - 1] = invFact[i] * i % mod;
        }
    }

    long long modPow(long long base, long long exponent, int mod) const {
        long long result = 1 % mod;
        base %= mod;
        while (exponent > 0) {
            if (exponent & 1) result = result * base % mod;
            base = base * base % mod;
            exponent >>= 1;
        }
        return result;
    }

    long long choose(int n, int k) const {
        if (k < 0 || k > n) return 0;
        return fact[n] * invFact[k] % mod * invFact[n - k] % mod;
    }
};
```

## 6) CRT（骨架）

```cpp
#include <vector>
using namespace std;

long long crt(const vector<long long>& remainder, const vector<long long>& modulus) {
    long long result = remainder[0];
    long long currentMod = modulus[0];

    for (int i = 1; i < static_cast<int>(remainder.size()); ++i) {
        long long x = 0, y = 0;
        long long g = exgcd(currentMod, modulus[i], x, y);
        if ((remainder[i] - result) % g != 0) return -1;

        long long step = modulus[i] / g;
        long long delta = (remainder[i] - result) / g % step;
        x = (x % step + step) % step;
        long long add = delta * x % step;
        result += currentMod * add;
        currentMod *= step;
        result = (result % currentMod + currentMod) % currentMod;
    }

    return result;
}
```

## 使用建议

- 先掌握快速幂、逆元、筛法、组合数
- CRT 属于进阶补充，题目需要时再上
- 大数/NTT/高斯消元可以后续单独拆页
