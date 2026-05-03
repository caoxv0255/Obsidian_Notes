---
type: snippets
topic: persistent_segment_tree_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数据结构, 可持久化线段树, 主席树, Snippets]
---

# 可持久化线段树模板

> 最常见用途是主席树，解决区间第 k 小、前缀版本查询。

## 1) 第 k 小主席树

```cpp
#include <algorithm>
#include <utility>
#include <vector>
using namespace std;

struct PersistentSegmentTree {
    vector<int> leftChild;
    vector<int> rightChild;
    vector<int> sum;
    vector<int> roots;
    vector<int> values;
    int nodeCount = 0;
    int leftBound = 0;
    int rightBound = 0;

    explicit PersistentSegmentTree(vector<int> rawValues) : values(std::move(rawValues)) {
        sort(values.begin(), values.end());
        values.erase(unique(values.begin(), values.end()), values.end());
        leftBound = 0;
        rightBound = static_cast<int>(values.size()) - 1;

        leftChild.reserve(1 << 20);
        rightChild.reserve(1 << 20);
        sum.reserve(1 << 20);
        roots.push_back(0);
        newNode();
    }

    int newNode() {
        leftChild.push_back(0);
        rightChild.push_back(0);
        sum.push_back(0);
        return nodeCount++;
    }

    int update(int previousRoot, int left, int right, int position) {
        int currentRoot = newNode();
        leftChild[currentRoot] = leftChild[previousRoot];
        rightChild[currentRoot] = rightChild[previousRoot];
        sum[currentRoot] = sum[previousRoot] + 1;

        if (left != right) {
            int middle = left + (right - left) / 2;
            if (position <= middle) {
                leftChild[currentRoot] = update(leftChild[previousRoot], left, middle, position);
            } else {
                rightChild[currentRoot] = update(rightChild[previousRoot], middle + 1, right, position);
            }
        }

        return currentRoot;
    }

    int buildVersion(int previousRoot, int value) {
        int position = static_cast<int>(lower_bound(values.begin(), values.end(), value) - values.begin());
        return update(previousRoot, leftBound, rightBound, position);
    }

    int queryKth(int leftRoot, int rightRoot, int left, int right, int k) const {
        if (left == right) return left;
        int middle = left + (right - left) / 2;
        int leftCount = sum[leftChild[rightRoot]] - sum[leftChild[leftRoot]];
        if (k <= leftCount) {
            return queryKth(leftChild[leftRoot], leftChild[rightRoot], left, middle, k);
        }
        return queryKth(rightChild[leftRoot], rightChild[rightRoot], middle + 1, right, k - leftCount);
    }

    vector<int> buildFromArray(const vector<int>& array) {
        roots.assign(1, 0);
        for (int value : array) {
            roots.push_back(buildVersion(roots.back(), value));
        }
        return roots;
    }

    int kthNumber(int leftIndex, int rightIndex, int k) const {
        int compressedIndex = queryKth(roots[leftIndex - 1], roots[rightIndex], leftBound, rightBound, k);
        return values[compressedIndex];
    }
};
```

## 使用建议

- 区间第 k 小：主席树
- 版本化前缀统计：可持久化线段树
- 如果只是单点修改，不需要持久化，普通线段树更轻
