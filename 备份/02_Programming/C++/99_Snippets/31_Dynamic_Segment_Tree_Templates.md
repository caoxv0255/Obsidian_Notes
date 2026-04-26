---
type: snippets
topic: dynamic_segment_tree_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/数据结构, 动态开点线段树, 线段树, Snippets]
---

# 动态开点线段树模板

> 适合值域很大、实际修改点很少的题目。

## 1) 点加 + 区间和查询

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct DynamicSegmentTree {
    struct Node {
        int leftChild = -1;
        int rightChild = -1;
        long long sum = 0;
    };

    vector<Node> nodes;

    DynamicSegmentTree() {
        nodes.reserve(1 << 20);
        nodes.push_back(Node());
    }

    int createNode() {
        nodes.push_back(Node());
        return static_cast<int>(nodes.size()) - 1;
    }

    void add(int& root, int left, int right, int position, long long delta) {
        if (root == -1) {
            root = createNode();
        }
        nodes[root].sum += delta;
        if (left == right) return;

        int mid = left + (right - left) / 2;
        if (position <= mid) {
            add(nodes[root].leftChild, left, mid, position, delta);
        } else {
            add(nodes[root].rightChild, mid + 1, right, position, delta);
        }
    }

    long long query(int root, int left, int right, int queryLeft, int queryRight) const {
        if (root == -1 || queryRight < left || right < queryLeft) return 0;
        if (queryLeft <= left && right <= queryRight) return nodes[root].sum;

        int mid = left + (right - left) / 2;
        return query(nodes[root].leftChild, left, mid, queryLeft, queryRight) +
               query(nodes[root].rightChild, mid + 1, right, queryLeft, queryRight);
    }
};
```

## 使用建议

- 值域大、点数少：动态开点线段树
- 需要区间加和懒标记时，也可以继续往这个骨架里扩
- 配合离散化，能覆盖很多稀疏坐标题
