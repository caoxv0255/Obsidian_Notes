---
type: snippets
topic: bipartite_matching_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/图论, 二分图匹配, 匈牙利算法, Hopcroft-Karp, Snippets]
---

# 二分图匹配模板

> 小规模可用匈牙利，大规模优先 Hopcroft-Karp。

## 1) 匈牙利算法（DFS 增广）

```cpp
#include <vector>
using namespace std;

struct HungarianMatching {
    int leftSize;
    int rightSize;
    vector<vector<int>> graph;
    vector<int> matchRight;
    vector<int> visited;
    int visitToken = 0;

    HungarianMatching(int leftSize, int rightSize)
        : leftSize(leftSize), rightSize(rightSize), graph(leftSize), matchRight(rightSize, -1), visited(rightSize, 0) {}

    void addEdge(int leftNode, int rightNode) {
        graph[leftNode].push_back(rightNode);
    }

    bool dfs(int leftNode) {
        for (int rightNode : graph[leftNode]) {
            if (visited[rightNode] == visitToken) continue;
            visited[rightNode] = visitToken;
            if (matchRight[rightNode] == -1 || dfs(matchRight[rightNode])) {
                matchRight[rightNode] = leftNode;
                return true;
            }
        }
        return false;
    }

    int maxMatching() {
        int answer = 0;
        for (int leftNode = 0; leftNode < leftSize; ++leftNode) {
            ++visitToken;
            if (dfs(leftNode)) {
                ++answer;
            }
        }
        return answer;
    }
};
```

## 2) Hopcroft-Karp

```cpp
#include <queue>
#include <vector>
using namespace std;

struct HopcroftKarp {
    int leftSize;
    int rightSize;
    vector<vector<int>> graph;
    vector<int> dist;
    vector<int> matchLeft;
    vector<int> matchRight;

    HopcroftKarp(int leftSize, int rightSize)
        : leftSize(leftSize), rightSize(rightSize), graph(leftSize), dist(leftSize), matchLeft(leftSize, -1), matchRight(rightSize, -1) {}

    void addEdge(int leftNode, int rightNode) {
        graph[leftNode].push_back(rightNode);
    }

    bool bfs() {
        queue<int> pending;
        bool foundFreeVertex = false;

        for (int leftNode = 0; leftNode < leftSize; ++leftNode) {
            if (matchLeft[leftNode] == -1) {
                dist[leftNode] = 0;
                pending.push(leftNode);
            } else {
                dist[leftNode] = -1;
            }
        }

        while (!pending.empty()) {
            int leftNode = pending.front();
            pending.pop();

            for (int rightNode : graph[leftNode]) {
                int pairedLeft = matchRight[rightNode];
                if (pairedLeft == -1) {
                    foundFreeVertex = true;
                } else if (dist[pairedLeft] == -1) {
                    dist[pairedLeft] = dist[leftNode] + 1;
                    pending.push(pairedLeft);
                }
            }
        }

        return foundFreeVertex;
    }

    bool dfs(int leftNode) {
        for (int rightNode : graph[leftNode]) {
            int pairedLeft = matchRight[rightNode];
            if (pairedLeft == -1 || (dist[pairedLeft] == dist[leftNode] + 1 && dfs(pairedLeft))) {
                matchLeft[leftNode] = rightNode;
                matchRight[rightNode] = leftNode;
                return true;
            }
        }

        dist[leftNode] = -1;
        return false;
    }

    int maxMatching() {
        int answer = 0;
        while (bfs()) {
            for (int leftNode = 0; leftNode < leftSize; ++leftNode) {
                if (matchLeft[leftNode] == -1 && dfs(leftNode)) {
                    ++answer;
                }
            }
        }
        return answer;
    }
};
```

## 使用建议

- 点数不大、代码要短：匈牙利
- 点数和边数都比较大：Hopcroft-Karp
- 这类题常和建图、分组、覆盖问题一起出现
