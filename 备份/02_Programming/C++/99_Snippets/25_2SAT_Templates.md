---
type: snippets
topic: two_sat_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/图论, 2-SAT, SCC, Snippets]
---

# 2-SAT 模板

> 用于一类“每个变量只能取真/假之一”的约束问题。

## 1) Kosaraju 版

```cpp
#include <algorithm>
#include <vector>
using namespace std;

struct TwoSAT {
    int variables;
    vector<vector<int>> graph;
    vector<vector<int>> reverseGraph;
    vector<int> order;
    vector<int> component;
    vector<int> assignment;
    vector<char> visited;

    explicit TwoSAT(int variables)
        : variables(variables), graph(2 * variables), reverseGraph(2 * variables),
          component(2 * variables, -1), assignment(variables, 0), visited(2 * variables, 0) {}

    int literal(int variable, bool value) const {
        return variable * 2 + (value ? 0 : 1);
    }

    void addImplication(int from, int to) {
        graph[from].push_back(to);
        reverseGraph[to].push_back(from);
    }

    void addClause(int x, bool xValue, int y, bool yValue) {
        addImplication(literal(x, !xValue), literal(y, yValue));
        addImplication(literal(y, !yValue), literal(x, xValue));
    }

    void forceValue(int variable, bool value) {
        addImplication(literal(variable, !value), literal(variable, value));
    }

    void dfs1(int node) {
        visited[node] = 1;
        for (int next : graph[node]) {
            if (!visited[next]) {
                dfs1(next);
            }
        }
        order.push_back(node);
    }

    void dfs2(int node, int id) {
        component[node] = id;
        for (int next : reverseGraph[node]) {
            if (component[next] == -1) {
                dfs2(next, id);
            }
        }
    }

    bool solve() {
        fill(visited.begin(), visited.end(), 0);
        fill(component.begin(), component.end(), -1);
        order.clear();

        for (int node = 0; node < 2 * variables; ++node) {
            if (!visited[node]) {
                dfs1(node);
            }
        }

        int componentId = 0;
        for (int index = static_cast<int>(order.size()) - 1; index >= 0; --index) {
            int node = order[index];
            if (component[node] == -1) {
                dfs2(node, componentId++);
            }
        }

        for (int variable = 0; variable < variables; ++variable) {
            if (component[literal(variable, true)] == component[literal(variable, false)]) {
                return false;
            }
            assignment[variable] = component[literal(variable, true)] > component[literal(variable, false)];
        }

        return true;
    }

    int value(int variable) const {
        return assignment[variable];
    }
};
```

## 使用建议

- “A 或 B” 类约束：转成蕴含边
- “必须满足一个条件”：加单点约束
- 如果题目本身已经有 SCC，就可以直接复用 SCC 结果做 2-SAT
