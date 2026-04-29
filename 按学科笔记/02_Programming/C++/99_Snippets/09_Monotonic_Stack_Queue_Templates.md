---
type: snippets
topic: monotonic_stack_queue_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/单调栈, ACM/单调队列, 算法/模板, Snippets]
---

# 单调栈 / 单调队列模板

> 高频、短小、直接可用。

## 1) 下一个更大元素

```cpp
#include <vector>
using namespace std;

vector<int> nextGreaterElement(const vector<int>& values) {
    int n = static_cast<int>(values.size());
    vector<int> answer(n, -1);
    vector<int> stackIndices;

    for (int index = 0; index < n; ++index) {
        while (!stackIndices.empty() && values[stackIndices.back()] < values[index]) {
            answer[stackIndices.back()] = values[index];
            stackIndices.pop_back();
        }
        stackIndices.push_back(index);
    }

    return answer;
}
```

## 2) 滑动窗口最大值

```cpp
#include <deque>
#include <vector>
using namespace std;

vector<int> slidingWindowMaximum(const vector<int>& values, int windowSize) {
    vector<int> answer;
    deque<int> indices;

    for (int index = 0; index < static_cast<int>(values.size()); ++index) {
        while (!indices.empty() && indices.front() <= index - windowSize) {
            indices.pop_front();
        }

        while (!indices.empty() && values[indices.back()] <= values[index]) {
            indices.pop_back();
        }

        indices.push_back(index);
        if (index >= windowSize - 1) {
            answer.push_back(values[indices.front()]);
        }
    }

    return answer;
}
```

## 3) 柱状图最大矩形

```cpp
#include <vector>
using namespace std;

long long largestRectangleArea(const vector<int>& heights) {
    int n = static_cast<int>(heights.size());
    vector<int> stackIndices;
    long long best = 0;

    for (int index = 0; index <= n; ++index) {
        int currentHeight = (index == n ? 0 : heights[index]);
        while (!stackIndices.empty() && heights[stackIndices.back()] >= currentHeight) {
            int heightIndex = stackIndices.back();
            stackIndices.pop_back();

            int leftBoundary = stackIndices.empty() ? -1 : stackIndices.back();
            long long width = index - leftBoundary - 1;
            best = max(best, 1LL * heights[heightIndex] * width);
        }
        stackIndices.push_back(index);
    }

    return best;
}
```

## 使用建议

- 下一个更大/更小元素：单调栈
- 区间最值维护：单调队列
- 柱状图 / 直方图面积：单调栈
