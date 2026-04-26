---
type: snippets
topic: graph_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/图论, 算法/模板, Snippets]
---

# 图论模板

> 这里只收“能直接搬进竞赛代码”的图论模板，优先高频、低抽象。

## 1) BFS / DFS

```cpp
#include <vector>
using namespace std;

void dfs(int node, const vector<vector<int>>& graph, vector<int>& visited) {
    visited[node] = 1;
    for (int next : graph[node]) {
        if (!visited[next]) {
            dfs(next, graph, visited);
        }
    }
}
```

## 2) Dijkstra

```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll INF = 4e18;

vector<ll> dijkstra(int start, const vector<vector<pair<int, int>>>& graph) {
    int n = static_cast<int>(graph.size());
    vector<ll> dist(n, INF);
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [current_dist, node] = pq.top();
        pq.pop();
        if (current_dist != dist[node]) continue;

        for (auto [next, weight] : graph[node]) {
            if (dist[next] > dist[node] + weight) {
                dist[next] = dist[node] + weight;
                pq.push({dist[next], next});
            }
        }
    }

    return dist;
}
```

## 3) 0-1 BFS

```cpp
#include <deque>
#include <vector>
using namespace std;

vector<int> zeroOneBfs(int start, const vector<vector<pair<int, int>>>& graph) {
    const int INF = 1e9;
    int n = static_cast<int>(graph.size());
    vector<int> dist(n, INF);
    deque<int> dq;

    dist[start] = 0;
    dq.push_back(start);

    while (!dq.empty()) {
        int node = dq.front();
        dq.pop_front();

        for (auto [next, weight] : graph[node]) {
            if (dist[next] > dist[node] + weight) {
                dist[next] = dist[node] + weight;
                if (weight == 0) {
                    dq.push_front(next);
                } else {
                    dq.push_back(next);
                }
            }
        }
    }

    return dist;
}
```

## 4) 拓扑排序

```cpp
#include <queue>
#include <vector>
using namespace std;

vector<int> topoSort(const vector<vector<int>>& graph) {
    int n = static_cast<int>(graph.size());
    vector<int> indegree(n, 0);
    for (int node = 0; node < n; ++node) {
        for (int next : graph[node]) {
            ++indegree[next];
        }
    }

    queue<int> q;
    for (int node = 0; node < n; ++node) {
        if (indegree[node] == 0) {
            q.push(node);
        }
    }

    vector<int> order;
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        order.push_back(node);

        for (int next : graph[node]) {
            if (--indegree[next] == 0) {
                q.push(next);
            }
        }
    }

    return order;
}
```

## 5) LCA 倍增（骨架）

```cpp
#include <vector>
using namespace std;

struct LCA {
    int n;
    int log_n;
    vector<vector<int>> up;
    vector<int> depth;
    vector<vector<int>> graph;

    LCA(int n, const vector<vector<int>>& graph) : n(n), graph(graph) {
        log_n = 1;
        while ((1 << log_n) <= n) ++log_n;
        up.assign(log_n, vector<int>(n, -1));
        depth.assign(n, 0);
    }

    void dfs(int node, int parent) {
        up[0][node] = parent;
        for (int level = 1; level < log_n; ++level) {
            if (up[level - 1][node] == -1) break;
            up[level][node] = up[level - 1][up[level - 1][node]];
        }

        for (int next : graph[node]) {
            if (next == parent) continue;
            depth[next] = depth[node] + 1;
            dfs(next, node);
        }
    }

    int lift(int node, int steps) {
        for (int level = 0; level < log_n; ++level) {
            if (steps & (1 << level)) {
                node = up[level][node];
            }
        }
        return node;
    }

    int query(int a, int b) {
        if (depth[a] < depth[b]) swap(a, b);
        a = lift(a, depth[a] - depth[b]);
        if (a == b) return a;
        for (int level = log_n - 1; level >= 0; --level) {
            if (up[level][a] != up[level][b]) {
                a = up[level][a];
                b = up[level][b];
            }
        }
        return up[0][a];
    }
};
```

## 6) Dinic 最大流（骨架）

```cpp
#include <queue>
#include <vector>
using namespace std;

struct Edge {
    int to;
    int capacity;
    int rev;
};

struct Dinic {
    int n;
    vector<vector<Edge>> graph;
    vector<int> level;
    vector<int> ptr;

    Dinic(int n) : n(n), graph(n), level(n), ptr(n) {}

    void addEdge(int from, int to, int capacity) {
        Edge forward{to, capacity, static_cast<int>(graph[to].size())};
        Edge backward{from, 0, static_cast<int>(graph[from].size())};
        graph[from].push_back(forward);
        graph[to].push_back(backward);
    }

    bool bfs(int source, int sink) {
        fill(level.begin(), level.end(), -1);
        queue<int> q;
        level[source] = 0;
        q.push(source);

        while (!q.empty()) {
            int node = q.front();
            q.pop();
            for (const auto& edge : graph[node]) {
                if (edge.capacity > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[node] + 1;
                    q.push(edge.to);
                }
            }
        }

        return level[sink] != -1;
    }

    int dfs(int node, int sink, int pushed) {
        if (node == sink || pushed == 0) return pushed;
        for (int& index = ptr[node]; index < static_cast<int>(graph[node].size()); ++index) {
            Edge& edge = graph[node][index];
            if (level[edge.to] != level[node] + 1 || edge.capacity == 0) continue;

            int flow = dfs(edge.to, sink, min(pushed, edge.capacity));
            if (flow == 0) continue;

            edge.capacity -= flow;
            graph[edge.to][edge.rev].capacity += flow;
            return flow;
        }
        return 0;
    }

    int maxFlow(int source, int sink) {
        int flow = 0;
        while (bfs(source, sink)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (int pushed = dfs(source, sink, 1e9)) {
                flow += pushed;
            }
        }
        return flow;
    }
};
```

## 使用建议

- 优先掌握 Dijkstra、拓扑、LCA、Dinic
- 0-1 BFS 和 SCC 属于高频补充
- 代码尽量保持可直接粘贴进比赛模板的状态
