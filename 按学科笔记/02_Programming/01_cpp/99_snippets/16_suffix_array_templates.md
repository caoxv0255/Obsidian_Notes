---
type: snippets
topic: suffix_array_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/字符串, 后缀数组, LCP, Snippets]
---

# 后缀数组模板

> 适合字符串排序、后缀比较、LCP、重复子串等题目。

## 1) Doubling + LCP

```cpp
#include <algorithm>
#include <string>
#include <utility>
#include <vector>
using namespace std;

struct SuffixArray {
    string text;
    vector<int> suffixArray;
    vector<int> rankArray;
    vector<int> lcpArray;

    explicit SuffixArray(string text) : text(std::move(text)) {
        build();
    }

    void build() {
        int n = static_cast<int>(text.size());
        if (n == 0) {
            suffixArray.clear();
            rankArray.clear();
            lcpArray.clear();
            return;
        }
        suffixArray.resize(n);
        rankArray.resize(n);

        for (int index = 0; index < n; ++index) {
            suffixArray[index] = index;
            rankArray[index] = static_cast<unsigned char>(text[index]);
        }

        vector<int> tempRank(n);
        for (int length = 1; length < n; length <<= 1) {
            sort(suffixArray.begin(), suffixArray.end(), [&](int left, int right) {
                if (rankArray[left] != rankArray[right]) return rankArray[left] < rankArray[right];
                int leftRank = left + length < n ? rankArray[left + length] : -1;
                int rightRank = right + length < n ? rankArray[right + length] : -1;
                return leftRank < rightRank;
            });

            tempRank[suffixArray[0]] = 0;
            for (int index = 1; index < n; ++index) {
                int previous = suffixArray[index - 1];
                int current = suffixArray[index];
                bool sameClass = rankArray[previous] == rankArray[current] &&
                                 (previous + length < n ? rankArray[previous + length] : -1) ==
                                 (current + length < n ? rankArray[current + length] : -1);
                tempRank[current] = tempRank[previous] + (sameClass ? 0 : 1);
            }
            rankArray = tempRank;
            if (rankArray[suffixArray.back()] == n - 1) break;
        }

        buildLcp();
    }

    void buildLcp() {
        int n = static_cast<int>(text.size());
        lcpArray.assign(max(0, n - 1), 0);
        vector<int> position(n);
        for (int index = 0; index < n; ++index) {
            position[suffixArray[index]] = index;
        }

        int matched = 0;
        for (int index = 0; index < n; ++index) {
            int rank = position[index];
            if (rank == n - 1) {
                matched = 0;
                continue;
            }

            int nextSuffix = suffixArray[rank + 1];
            while (index + matched < n && nextSuffix + matched < n &&
                   text[index + matched] == text[nextSuffix + matched]) {
                ++matched;
            }
            lcpArray[rank] = matched;
            if (matched > 0) --matched;
        }
    }
};
```

## 使用建议

- 排序全部后缀：后缀数组
- 求任意两个后缀公共前缀：LCP + RMQ
- 查重复子串、循环同构、字符串字典序比较：都很常见
