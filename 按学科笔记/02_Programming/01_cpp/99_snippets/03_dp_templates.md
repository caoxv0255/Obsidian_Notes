---
type: snippets
topic: dp_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/DP, 算法/模板, Snippets]
---

# DP 模板

> 只保留最常见、最容易直接搬用的 DP 模板。

## 1) 记忆化搜索

```cpp
#include <vector>
using namespace std;

int dfs(int state, vector<int>& memo) {
    if (state == 0) return 0;
    if (memo[state] != -1) return memo[state];

    int result = state;
    for (int next = 0; next < state; ++next) {
        result = min(result, dfs(next, memo) + 1);
    }

    return memo[state] = result;
}
```

## 2) 0/1 背包

```cpp
#include <algorithm>
#include <vector>
using namespace std;

int zeroOneKnapsack(int capacity, const vector<int>& weight, const vector<int>& value) {
    vector<int> dp(capacity + 1, 0);
    int n = static_cast<int>(weight.size());

    for (int item = 0; item < n; ++item) {
        for (int current = capacity; current >= weight[item]; --current) {
            dp[current] = max(dp[current], dp[current - weight[item]] + value[item]);
        }
    }

    return dp[capacity];
}
```

## 3) 完全背包

```cpp
#include <algorithm>
#include <vector>
using namespace std;

int completeKnapsack(int capacity, const vector<int>& weight, const vector<int>& value) {
    vector<int> dp(capacity + 1, 0);
    int n = static_cast<int>(weight.size());

    for (int item = 0; item < n; ++item) {
        for (int current = weight[item]; current <= capacity; ++current) {
            dp[current] = max(dp[current], dp[current - weight[item]] + value[item]);
        }
    }

    return dp[capacity];
}
```

## 4) 最长递增子序列 LIS

```cpp
#include <algorithm>
#include <vector>
using namespace std;

int lisLength(const vector<int>& values) {
    vector<int> tails;
    for (int value : values) {
        auto it = lower_bound(tails.begin(), tails.end(), value);
        if (it == tails.end()) {
            tails.push_back(value);
        } else {
            *it = value;
        }
    }
    return static_cast<int>(tails.size());
}
```

## 5) 区间 DP（骨架）

```cpp
#include <vector>
using namespace std;

int intervalDp(const vector<int>& values) {
    int n = static_cast<int>(values.size());
    vector<vector<int>> dp(n, vector<int>(n, 0));

    for (int length = 2; length <= n; ++length) {
        for (int left = 0; left + length - 1 < n; ++left) {
            int right = left + length - 1;
            dp[left][right] = 1e9;
            for (int split = left; split < right; ++split) {
                dp[left][right] = min(dp[left][right], dp[left][split] + dp[split + 1][right]);
            }
        }
    }

    return dp[0][n - 1];
}
```

## 6) 树形 DP（骨架）

```cpp
#include <vector>
using namespace std;

void treeDp(int node, int parent, const vector<vector<int>>& graph, vector<int>& dp) {
    dp[node] = 1;
    for (int next : graph[node]) {
        if (next == parent) continue;
        treeDp(next, node, graph, dp);
        dp[node] += dp[next];
    }
}
```

## 7) 线性 DP（爬楼梯示意）

```cpp
#include <vector>
using namespace std;

int climbStairs(int n) {
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    for (int step = 1; step <= n; ++step) {
        dp[step] += dp[step - 1];
        if (step >= 2) dp[step] += dp[step - 2];
    }
    return dp[n];
}
```

## 使用建议

- 先掌握 0/1 背包、完全背包、LIS、区间 DP、树形 DP
- 记忆化搜索适合做状态定义验证
- 如果状态过多，先画状态图再写转移
