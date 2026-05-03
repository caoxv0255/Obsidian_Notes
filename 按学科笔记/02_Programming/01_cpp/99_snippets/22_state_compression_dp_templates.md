---
type: snippets
topic: state_compression_dp_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/DP, 状压DP, 子集DP, Snippets]
---

# 状压 DP 模板

> 常见于 TSP、集合覆盖、子集转移与网格轮廓类问题。

## 1) 子集枚举骨架

```cpp
#include <vector>
using namespace std;

void enumerateSubsets(int mask) {
    for (int sub = mask; sub; sub = (sub - 1) & mask) {
        // 处理 sub 和 mask 的关系
    }
}
```

## 2) 旅行商问题 TSP

```cpp
#include <algorithm>
#include <limits>
#include <vector>
using namespace std;

struct TspStateCompression {
    static constexpr long long INF = numeric_limits<long long>::max() / 4;

    int n;
    vector<vector<long long>> distance;

    explicit TspStateCompression(int n) : n(n), distance(n, vector<long long>(n, INF)) {}

    long long solve(int start) const {
        int totalStates = 1 << n;
        vector<vector<long long>> dp(totalStates, vector<long long>(n, INF));
        dp[1 << start][start] = 0;

        for (int mask = 0; mask < totalStates; ++mask) {
            if ((mask & (1 << start)) == 0) continue;
            for (int last = 0; last < n; ++last) {
                if (dp[mask][last] == INF) continue;
                for (int next = 0; next < n; ++next) {
                    if (mask & (1 << next)) continue;
                    if (distance[last][next] == INF) continue;
                    int nextMask = mask | (1 << next);
                    dp[nextMask][next] = min(dp[nextMask][next], dp[mask][last] + distance[last][next]);
                }
            }
        }

        long long answer = INF;
        int fullMask = totalStates - 1;
        for (int last = 0; last < n; ++last) {
            if (dp[fullMask][last] == INF || distance[last][start] == INF) continue;
            answer = min(answer, dp[fullMask][last] + distance[last][start]);
        }
        return answer;
    }
};
```

## 使用建议

- TSP、集合覆盖、最少访问状态：状态压缩 DP
- 子集枚举是最基础的状态压缩写法
- 如果转移和网格结构相关，可以再扩展轮廓 DP
