---
type: snippets
topic: ac_automaton_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/字符串, AC自动机, Trie, Snippets]
---

# AC 自动机模板

> 适合多模式串匹配，竞赛里经常和字符串统计一起出现。

## 1) 基础模板

```cpp
#include <array>
#include <queue>
#include <string>
#include <vector>
using namespace std;

struct AhoCorasick {
    static constexpr int ALPHABET = 26;

    struct Node {
        array<int, ALPHABET> next;
        int fail = 0;
        int output = 0;

        Node() {
            next.fill(-1);
        }
    };

    vector<Node> trie;

    AhoCorasick() {
        trie.emplace_back();
    }

    void insert(const string& pattern) {
        int node = 0;
        for (char ch : pattern) {
            if (ch < 'a' || ch > 'z') continue;
            int index = ch - 'a';
            if (trie[node].next[index] == -1) {
                trie[node].next[index] = static_cast<int>(trie.size());
                trie.emplace_back();
            }
            node = trie[node].next[index];
        }
        ++trie[node].output;
    }

    void build() {
        queue<int> pending;
        for (int index = 0; index < ALPHABET; ++index) {
            int child = trie[0].next[index];
            if (child != -1) {
                trie[child].fail = 0;
                pending.push(child);
            } else {
                trie[0].next[index] = 0;
            }
        }

        while (!pending.empty()) {
            int node = pending.front();
            pending.pop();

            trie[node].output += trie[trie[node].fail].output;

            for (int index = 0; index < ALPHABET; ++index) {
                int child = trie[node].next[index];
                if (child != -1) {
                    trie[child].fail = trie[trie[node].fail].next[index];
                    pending.push(child);
                } else {
                    trie[node].next[index] = trie[trie[node].fail].next[index];
                }
            }
        }
    }

    long long countMatches(const string& text) const {
        int node = 0;
        long long matches = 0;
        for (char ch : text) {
            if (ch < 'a' || ch > 'z') {
                node = 0;
                continue;
            }
            node = trie[node].next[ch - 'a'];
            matches += trie[node].output;
        }
        return matches;
    }
};
```

## 使用建议

- 多模式串匹配：AC 自动机
- 统计文本中模式串出现次数：先建 Trie，再建 fail
- 字符集不止小写字母时，把 `ALPHABET` 和映射函数一起改掉
