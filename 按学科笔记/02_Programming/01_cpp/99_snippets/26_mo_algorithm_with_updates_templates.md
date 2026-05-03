---
type: snippets
topic: mo_algorithm_with_updates_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数据结构, 莫队, 带修改莫队, Snippets]
---

# 带修改莫队模板

> 适合静态区间统计加上少量离线修改的题目。

## 1) 三维莫队骨架

```cpp
#include <algorithm>
#include <cmath>
#include <utility>
#include <vector>
using namespace std;

struct Query {
    int left;
    int right;
    int time;
    int index;
};

struct Modification {
    int position;
    int previousValue;
    int newValue;
};

struct MoWithUpdates {
    int blockSize;
    vector<int> values;
    vector<int> frequency;
    int distinctCount = 0;

    explicit MoWithUpdates(vector<int> values) : values(std::move(values)) {
        blockSize = max(1, static_cast<int>(pow(this->values.size(), 2.0 / 3.0)));
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

    void applyModification(const Modification& modification, int left, int right) {
        int position = modification.position;
        if (left <= position && position <= right) {
            remove(position);
        }
        values[position] = modification.newValue;
        if (left <= position && position <= right) {
            add(position);
        }
    }

    void rollbackModification(const Modification& modification, int left, int right) {
        int position = modification.position;
        if (left <= position && position <= right) {
            remove(position);
        }
        values[position] = modification.previousValue;
        if (left <= position && position <= right) {
            add(position);
        }
    }

    vector<int> solve(vector<Query> queries, const vector<Modification>& modifications, int valueRange) {
        frequency.assign(valueRange, 0);
        sort(queries.begin(), queries.end(), [&](const Query& leftQuery, const Query& rightQuery) {
            int leftBlock = leftQuery.left / blockSize;
            int rightBlock = rightQuery.left / blockSize;
            if (leftBlock != rightBlock) return leftBlock < rightBlock;

            int leftRightBlock = leftQuery.right / blockSize;
            int rightRightBlock = rightQuery.right / blockSize;
            if (leftRightBlock != rightRightBlock) return leftRightBlock < rightRightBlock;

            return leftQuery.time < rightQuery.time;
        });

        vector<int> answer(queries.size());
        int currentLeft = 0;
        int currentRight = -1;
        int currentTime = 0;
        distinctCount = 0;

        for (const auto& query : queries) {
            while (currentTime < query.time) {
                applyModification(modifications[currentTime], currentLeft, currentRight);
                ++currentTime;
            }
            while (currentTime > query.time) {
                --currentTime;
                rollbackModification(modifications[currentTime], currentLeft, currentRight);
            }

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

- 区间不同数个数、区间代价函数、可离线回滚的统计问题都能用
- 值域先离散化，再把修改记录成 `previousValue/newValue`
- 这类题的关键是把“时间维”也当成一个指针来维护
