---
type: snippets
topic: string_templates
category: snippets
difficulty: advanced
acm_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, ACM/字符串, 算法/模板, Snippets]
---

# 字符串模板

> 只保留竞赛高频字符串算法，优先可直接复制使用的版本。

## 1) KMP

```cpp
#include <string>
#include <vector>
using namespace std;

vector<int> buildPrefix(const string& pattern) {
    int n = static_cast<int>(pattern.size());
    vector<int> prefix(n, 0);
    for (int i = 1, j = 0; i < n; ++i) {
        while (j > 0 && pattern[i] != pattern[j]) {
            j = prefix[j - 1];
        }
        if (pattern[i] == pattern[j]) {
            ++j;
        }
        prefix[i] = j;
    }
    return prefix;
}

vector<int> kmpSearch(const string& text, const string& pattern) {
    if (pattern.empty()) return {};
    vector<int> prefix = buildPrefix(pattern);
    vector<int> matches;
    for (int i = 0, j = 0; i < static_cast<int>(text.size()); ++i) {
        while (j > 0 && text[i] != pattern[j]) {
            j = prefix[j - 1];
        }
        if (text[i] == pattern[j]) {
            ++j;
        }
        if (j == static_cast<int>(pattern.size())) {
            matches.push_back(i - j + 1);
            j = prefix[j - 1];
        }
    }
    return matches;
}
```

## 2) Z 函数

```cpp
#include <string>
#include <vector>
using namespace std;

vector<int> zFunction(const string& s) {
    int n = static_cast<int>(s.size());
    vector<int> z(n, 0);
    for (int i = 1, left = 0, right = 0; i < n; ++i) {
        if (i <= right) {
            z[i] = min(right - i + 1, z[i - left]);
        }
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            ++z[i];
        }
        if (i + z[i] - 1 > right) {
            left = i;
            right = i + z[i] - 1;
        }
    }
    return z;
}
```

## 3) Rolling Hash

```cpp
#include <cstdint>
#include <string>
#include <vector>
using namespace std;

struct RollingHash {
    static constexpr uint64_t base = 1315423911ULL;
    vector<uint64_t> prefix;
    vector<uint64_t> power;

    explicit RollingHash(const string& s) {
        int n = static_cast<int>(s.size());
        prefix.assign(n + 1, 0);
        power.assign(n + 1, 1);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] * base + static_cast<unsigned char>(s[i]) + 1;
            power[i + 1] = power[i] * base;
        }
    }

    uint64_t get(int left, int right) const {
        return prefix[right + 1] - prefix[left] * power[right - left + 1];
    }
};
```

## 4) Trie

```cpp
#include <array>
#include <string>
#include <vector>
using namespace std;

struct Trie {
    struct Node {
        array<int, 26> next;
        int count = 0;

        Node() { next.fill(-1); }
    };

    vector<Node> nodes;

    Trie() { nodes.emplace_back(); }

    void insert(const string& word) {
        int node = 0;
        for (char ch : word) {
            int index = ch - 'a';
            if (nodes[node].next[index] == -1) {
                nodes[node].next[index] = static_cast<int>(nodes.size());
                nodes.emplace_back();
            }
            node = nodes[node].next[index];
        }
        ++nodes[node].count;
    }

    bool search(const string& word) const {
        int node = 0;
        for (char ch : word) {
            int index = ch - 'a';
            node = nodes[node].next[index];
            if (node == -1) return false;
        }
        return nodes[node].count > 0;
    }
};
```

## 5) 字符串前缀统计骨架

```cpp
#include <string>
#include <vector>
using namespace std;

vector<int> prefixCount(const string& s) {
    int n = static_cast<int>(s.size());
    vector<int> prefix(n, 0);
    for (int i = 1, j = 0; i < n; ++i) {
        while (j > 0 && s[i] != s[j]) {
            j = prefix[j - 1];
        }
        if (s[i] == s[j]) {
            ++j;
        }
        prefix[i] = j;
    }
    return prefix;
}
```

## 使用建议

- 先掌握 KMP、Z、Rolling Hash
- Trie 适合字典、前缀匹配、多模式输入
- 哈希模板要记得处理冲突风险，必要时双哈希或配合字符串验证
