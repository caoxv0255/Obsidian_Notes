---
type: snippets
topic: li_chao_segment_tree_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数据结构, 李超线段树, 函数最值, Snippets]
---

# 李超线段树模板

> 用于维护直线集合，在指定 $x$ 上查询最大值或最小值。

## 1) 动态开点李超树（最小值）

```cpp
#include <algorithm>
#include <limits>
#include <vector>
using namespace std;

struct Line {
    long long slope = 0;
    long long intercept = numeric_limits<long long>::max() / 4;

    long long value(long long x) const {
        return slope * x + intercept;
    }
};

struct LiChaoSegmentTree {
    struct Node {
        Line line;
        int leftChild = -1;
        int rightChild = -1;
        Node() = default;
    };

    long long leftBound;
    long long rightBound;
    vector<Node> nodes;

    LiChaoSegmentTree(long long leftBound, long long rightBound)
        : leftBound(leftBound), rightBound(rightBound) {
        nodes.reserve(1 << 20);
        nodes.push_back(Node());
    }

    int createNode() {
        nodes.push_back(Node());
        return static_cast<int>(nodes.size()) - 1;
    }

    void addLine(int& root, long long left, long long right, Line line) {
        if (root == -1) {
            root = createNode();
            nodes[root].line = line;
            return;
        }

        long long middle = left + (right - left) / 2;
        bool leftBetter = line.value(left) < nodes[root].line.value(left);
        bool middleBetter = line.value(middle) < nodes[root].line.value(middle);

        if (middleBetter) {
            swap(line, nodes[root].line);
        }

        if (left == right) {
            return;
        }

        if (leftBetter != middleBetter) {
            addLine(nodes[root].leftChild, left, middle, line);
        } else {
            addLine(nodes[root].rightChild, middle + 1, right, line);
        }
    }

    long long query(int root, long long left, long long right, long long x) const {
        if (root == -1) return numeric_limits<long long>::max() / 4;
        long long answer = nodes[root].line.value(x);
        if (left == right) return answer;

        long long middle = left + (right - left) / 2;
        if (x <= middle) {
            return min(answer, query(nodes[root].leftChild, left, middle, x));
        }
        return min(answer, query(nodes[root].rightChild, middle + 1, right, x));
    }
};
```

## 使用建议

- 维护直线集合、求最小值/最大值：李超线段树
- $x$ 范围已知且查询在线时非常合适
- 如果斜率和区间都很多，先想 Li Chao，再想暴力
