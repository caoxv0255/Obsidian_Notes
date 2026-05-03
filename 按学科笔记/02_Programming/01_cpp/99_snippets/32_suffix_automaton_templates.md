---
type: snippets
topic: suffix_automaton_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/字符串, 后缀自动机, SAM, Snippets]
---

# 后缀自动机模板

> 用于统计不同子串个数、最长重复子串、最长公共子串等问题。

## 1) SAM 核心模板

```cpp
#include <algorithm>
#include <array>
#include <string>
#include <vector>
using namespace std;

struct SuffixAutomaton {
    static constexpr int ALPHABET = 26;

    struct State {
        array<int, ALPHABET> next;
        int link = -1;
        int length = 0;
        int occurrence = 0;

        State() {
            next.fill(-1);
        }
    };

    vector<State> states;
    int last = 0;

    SuffixAutomaton() {
        states.reserve(1 << 20);
        states.push_back(State());
    }

    int toIndex(char ch) const {
        return ch - 'a';
    }

    void extend(char ch) {
        int c = toIndex(ch);
        int current = static_cast<int>(states.size());
        states.push_back(State());
        states[current].length = states[last].length + 1;
        states[current].occurrence = 1;

        int parent = last;
        while (parent != -1 && states[parent].next[c] == -1) {
            states[parent].next[c] = current;
            parent = states[parent].link;
        }

        if (parent == -1) {
            states[current].link = 0;
        } else {
            int existing = states[parent].next[c];
            if (states[parent].length + 1 == states[existing].length) {
                states[current].link = existing;
            } else {
                int clone = static_cast<int>(states.size());
                states.push_back(states[existing]);
                states[clone].length = states[parent].length + 1;
                states[clone].occurrence = 0;

                while (parent != -1 && states[parent].next[c] == existing) {
                    states[parent].next[c] = clone;
                    parent = states[parent].link;
                }

                states[existing].link = states[current].link = clone;
            }
        }

        last = current;
    }

    void build(const string& text) {
        for (char ch : text) {
            if (ch < 'a' || ch > 'z') continue;
            extend(ch);
        }
    }

    long long countDistinctSubstrings() const {
        long long total = 0;
        for (size_t index = 1; index < states.size(); ++index) {
            total += states[index].length - states[states[index].link].length;
        }
        return total;
    }

    void propagateOccurrences() {
        vector<int> order(states.size());
        for (size_t index = 0; index < states.size(); ++index) {
            order[index] = static_cast<int>(index);
        }
        sort(order.begin(), order.end(), [&](int left, int right) {
            return states[left].length > states[right].length;
        });

        for (int index : order) {
            if (states[index].link != -1) {
                states[states[index].link].occurrence += states[index].occurrence;
            }
        }
    }

    int longestCommonSubstring(const string& text) const {
        int node = 0;
        int matched = 0;
        int best = 0;

        for (char ch : text) {
            if (ch < 'a' || ch > 'z') {
                node = 0;
                matched = 0;
                continue;
            }

            int c = toIndex(ch);
            while (node != 0 && states[node].next[c] == -1) {
                node = states[node].link;
                matched = states[node].length;
            }

            if (states[node].next[c] != -1) {
                node = states[node].next[c];
                ++matched;
            } else {
                node = 0;
                matched = 0;
            }

            best = max(best, matched);
        }

        return best;
    }
};
```

## 使用建议

- 不同子串个数：`countDistinctSubstrings`
- 子串出现次数：先 `propagateOccurrences`
- 两串最长公共子串：`longestCommonSubstring`
