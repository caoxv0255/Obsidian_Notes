---
type: concept
topic: dynamic_programming
category: algorithms
difficulty: advanced
prerequisites: [[03_Algorithms_Sorting_Searching]]
acm_relevant: true
created: 2026-02-20
status: complete
---

# 动态规划 (Dynamic Programming)

## 核心定义

动态规划是一种优化技术，通过将复杂问题分解为子问题，并存储子问题的解来避免重复计算。

## 直观解释

想象你要爬楼梯，每次可以爬 1 或 2 步。要到达第 n 级，你可以从第 n-1 级或第 n-2 级上来。如果你已经知道到达这两级的方法数，就可以算出到达第 n 级的方法数。

## 详细说明

### DP 特征

1. **最优子结构**：问题的最优解包含子问题的最优解
2. **重叠子问题**：子问题被多次计算
3. **无后效性**：一旦某个状态确定，就不受之后决策的影响

### 常见 DP 问题

- 斐波那契数列
- 最长公共子序列
- 背包问题
- 最短路径

## 代码示例

```cpp
#include <iostream>
#include <vector>

// 斐波那契数列（记忆化）
int fib(int n, std::vector<int>& memo) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
    return memo[n];
}

int main() {
    int n = 10;
    std::vector<int> memo(n + 1, -1);
    std::cout << "fib(" << n << ") = " << fib(n, memo) << std::endl;
    return 0;
}
```
