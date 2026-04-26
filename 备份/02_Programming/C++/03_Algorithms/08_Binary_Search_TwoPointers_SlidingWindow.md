---
type: concept
topic: algorithms_core_techniques
category: algorithms
difficulty: intermediate
prerequisites: [[03_Algorithms_Sorting_Searching]]
acm_relevant: true
created: 2026-04-25
status: complete
---

# 二分答案、双指针与滑动窗口

## 核心定义

- 二分答案：在单调可判定空间上二分最优值。
- 双指针：用两个下标维护区间或相向扫描。
- 滑动窗口：在线维护满足条件的连续区间。

## 二分答案模板

```cpp
int left = 0, right = 1000000000;
while (left < right) {
    int mid = left + (right - left) / 2;
    if (check(mid)) right = mid;
    else left = mid + 1;
}
// left 为最小可行解
```

## 双指针示例：有序数组两数之和

```cpp
int l = 0, r = (int)a.size() - 1;
while (l < r) {
    int sum = a[l] + a[r];
    if (sum == target) break;
    if (sum < target) ++l;
    else --r;
}
```

## 滑动窗口示例：最长无重复子串

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string s = "abcaefgh";
    std::vector<int> last(256, -1);
    int ans = 0;
    for (int l = 0, r = 0; r < (int)s.size(); ++r) {
        l = std::max(l, last[(unsigned char)s[r]] + 1);
        last[(unsigned char)s[r]] = r;
        ans = std::max(ans, r - l + 1);
    }
    std::cout << ans << "\n";
    return 0;
}
```

## 常见错误

- 二分边界更新不对导致死循环。
- 滑窗条件维护不完整导致漏解。
- 双指针前提未满足（如数组未排序）。

## 相关链接

- [[03_Algorithms_Sorting_Searching]]
- [[00_Algorithms_Index|返回算法索引]]
