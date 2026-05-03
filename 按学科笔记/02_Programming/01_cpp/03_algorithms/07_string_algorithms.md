---
type: concept
topic: algorithms_string
category: algorithms
difficulty: advanced
prerequisites: [[03_Algorithms_Sorting_Searching]]
acm_relevant: true
created: 2026-04-25
status: complete
---

# 字符串算法 (String Algorithms)

## 核心清单

1. KMP：单模式串匹配，$O(n+m)$
2. Z-Algorithm：前缀匹配数组
3. Trie：字典树，前缀检索
4. Rolling Hash：子串比较
5. Manacher：最长回文子串，$O(n)$

## 代码示例：KMP

```cpp
#include <iostream>
#include <string>
#include <vector>

std::vector<int> build_lps(const std::string& p) {
    std::vector<int> lps(p.size(), 0);
    for (int i = 1, len = 0; i < (int)p.size();) {
        if (p[i] == p[len]) {
            lps[i++] = ++len;
        } else if (len) {
            len = lps[len - 1];
        } else {
            lps[i++] = 0;
        }
    }
    return lps;
}

int kmp_find(const std::string& s, const std::string& p) {
    if (p.empty()) return 0;
    auto lps = build_lps(p);
    for (int i = 0, j = 0; i < (int)s.size();) {
        if (s[i] == p[j]) {
            ++i;
            ++j;
            if (j == (int)p.size()) return i - j;
        } else if (j) {
            j = lps[j - 1];
        } else {
            ++i;
        }
    }
    return -1;
}

int main() {
    std::cout << kmp_find("ababcabcacbab", "abcac") << "\n";
    return 0;
}
```

## 选型建议

- 单次匹配 + 代码简洁：`std::string::find`
- 大规模模式匹配：KMP / Z
- 海量前缀查询：Trie

## 相关链接

- [[00_Algorithms_Index|返回算法索引]]
