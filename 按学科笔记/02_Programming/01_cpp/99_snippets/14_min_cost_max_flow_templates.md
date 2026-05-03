---
type: snippets
topic: min_cost_max_flow_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/图论, 最小费用最大流, SPFA, Snippets]
---

# 最小费用最大流模板

> 适合带费用的流量分配、最优匹配、运输类问题。

## 1) SPFA 增广版

```cpp
#include <climits>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

struct MinCostMaxFlow {
    struct Edge {
        int to;
        int rev;
        int cap;
        int cost;
    };

    int n;
    vector<vector<Edge>> graph;

    explicit MinCostMaxFlow(int n) : n(n), graph(n) {}

    void addEdge(int from, int to, int cap, int cost) {
        Edge forward{to, static_cast<int>(graph[to].size()), cap, cost};
        Edge backward{from, static_cast<int>(graph[from].size()), 0, -cost};
        graph[from].push_back(forward);
        graph[to].push_back(backward);
    }

    bool spfa(int source, int sink, vector<int>& prevNode, vector<int>& prevEdge, vector<long long>& dist) {
        const long long INF = LLONG_MAX / 4;
        dist.assign(n, INF);
        vector<bool> inQueue(n, false);
        queue<int> pending;

        dist[source] = 0;
        pending.push(source);
        inQueue[source] = true;

        while (!pending.empty()) {
            int node = pending.front();
            pending.pop();
            inQueue[node] = false;

            for (int index = 0; index < static_cast<int>(graph[node].size()); ++index) {
                const Edge& edge = graph[node][index];
                if (edge.cap <= 0) continue;
                if (dist[edge.to] > dist[node] + edge.cost) {
                    dist[edge.to] = dist[node] + edge.cost;
                    prevNode[edge.to] = node;
                    prevEdge[edge.to] = index;
                    if (!inQueue[edge.to]) {
                        inQueue[edge.to] = true;
                        pending.push(edge.to);
                    }
                }
            }
        }

        return dist[sink] != INF;
    }

    pair<int, long long> minCostMaxFlow(int source, int sink) {
        int flow = 0;
        long long cost = 0;
        vector<int> prevNode(n, -1);
        vector<int> prevEdge(n, -1);
        vector<long long> dist;

        while (spfa(source, sink, prevNode, prevEdge, dist)) {
            int augment = INT_MAX;
            for (int node = sink; node != source; node = prevNode[node]) {
                const Edge& edge = graph[prevNode[node]][prevEdge[node]];
                augment = min(augment, edge.cap);
            }

            for (int node = sink; node != source; node = prevNode[node]) {
                Edge& edge = graph[prevNode[node]][prevEdge[node]];
                edge.cap -= augment;
                graph[node][edge.rev].cap += augment;
                cost += 1LL * augment * edge.cost;
            }

            flow += augment;
        }

        return {flow, cost};
    }
};
```

## 使用建议

- 有费用的匹配、分配、运输问题：最小费用最大流
- 如果边很多、图较大，可以再升级为带势能的 Dijkstra 版本
- 这份模板优先保证“能直接写对”，再考虑极限性能
