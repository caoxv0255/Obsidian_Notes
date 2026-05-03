---
type: snippets
topic: mo_algorithm_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数据结构, 莫队, 离线查询, Snippets]
---

# 莫队模板

> 适合静态区间查询，尤其是频率统计、不同数个数、区间代价问题。

## 1) 普通莫队

```cpp
#include <algorithm>
#include <cmath>
#include <utility>
#include <vector>
using namespace std;

struct Query {
    int left;
    int right;
    int index;
};

struct MoAlgorithm {
    int blockSize;
    vector<int> values;
    vector<int> frequency;
    int distinctCount = 0;

    explicit MoAlgorithm(vector<int> values) : values(std::move(values)) {
        blockSize = max(1, static_cast<int>(sqrt(this->values.size())));
    }

    void add(int position) {
        int value = values[position];
        if (frequency[value] == 0) {
            ++distinctCount;
        }
        ++frequency[value];
    }

    void remove(int position) {
        int value = values[position];
        --frequency[value];
        if (frequency[value] == 0) {
            --distinctCount;
        }
    }

    vector<int> solve(vector<Query> queries, int valueRange) {
        frequency.assign(valueRange, 0);
        sort(queries.begin(), queries.end(), [&](const Query& left, const Query& right) {
            int leftBlock = left.left / blockSize;
            int rightBlock = right.left / blockSize;
            if (leftBlock != rightBlock) return leftBlock < rightBlock;
            if (leftBlock & 1) return left.right > right.right;
            return left.right < right.right;
        });

        vector<int> answer(queries.size());
        int currentLeft = 0;
        int currentRight = -1;
        distinctCount = 0;

        for (const auto& query : queries) {
            while (currentLeft > query.left) add(--currentLeft);
            while (currentRight < query.right) add(++currentRight);
            while (currentLeft < query.left) remove(currentLeft++);
            while (currentRight > query.right) remove(currentRight--);
            answer[query.index] = distinctCount;
        }

        return answer;
    }
};
```

## 使用建议

- 静态区间统计：莫队
- 常见统计目标：不同数个数、区间众数近似、区间代价函数
- 如果题目带修改，可以再升级为带修改的莫队
