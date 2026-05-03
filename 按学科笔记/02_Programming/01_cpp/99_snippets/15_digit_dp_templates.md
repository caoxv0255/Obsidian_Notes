---
type: snippets
topic: digit_dp_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/DP, 数位DP, 记忆化搜索, Snippets]
---

# 数位 DP 模板

> 常见于“统计区间内满足某种数字性质的数”的题目。

## 1) 数字和对模数取模

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct DigitSumModDP {
    int mod;
    vector<int> digits;
    vector<vector<long long>> memo;

    explicit DigitSumModDP(int mod) : mod(mod) {}

    long long dfs(int pos, int sumMod, bool tight) {
        if (pos == static_cast<int>(digits.size())) {
            return sumMod == 0 ? 1 : 0;
        }

        if (!tight && memo[pos][sumMod] != -1) {
            return memo[pos][sumMod];
        }

        int upper = tight ? digits[pos] : 9;
        long long answer = 0;
        for (int digit = 0; digit <= upper; ++digit) {
            int nextMod = (sumMod + digit) % mod;
            answer += dfs(pos + 1, nextMod, tight && digit == upper);
        }

        if (!tight) {
            memo[pos][sumMod] = answer;
        }
        return answer;
    }

    long long countUpTo(long long value) {
        if (value < 0) return 0;

        digits.clear();
        if (value == 0) {
            digits.push_back(0);
        } else {
            while (value > 0) {
                digits.push_back(static_cast<int>(value % 10));
                value /= 10;
            }
            reverse(digits.begin(), digits.end());
        }

        memo.assign(digits.size(), vector<long long>(mod, -1));
        return dfs(0, 0, true);
    }

    long long countInRange(long long left, long long right) {
        return countUpTo(right) - countUpTo(left - 1);
    }
};
```

## 使用建议

- 统计区间内数字和、数字和取模、特定位数状态：数位 DP
- 如果题目还限制前导零、相邻数字关系，可以在状态里再加 `started` 或 `lastDigit`
- 这类题最重要的是先把“状态定义”写清楚，再写转移
