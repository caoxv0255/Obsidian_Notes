---
type: concept
topic: stl_containers
category: stl
difficulty: intermediate
prerequisites: [[../01_Basics/05_Functions]], [[../01_Basics/08_Arrays]]
acm_relevant: true
created: 2026-02-20
status: complete
---

# STL 容器 (STL Containers)

## 核心定义

STL（Standard Template Library）容器是 C++ 标准库提供的数据结构，用于存储和管理数据集合。主要包括序列容器、关联容器和无序关联容器。

## 直观解释

想象你有不同类型的容器：
- **序列容器**：像一排盒子（vector）、一列可以插入的盒子（list）
- **关联容器**：像字典，可以根据键快速找到值（map, set）
- **无序容器**：像哈希表，查找速度更快但不保证顺序

## 详细说明

### 序列容器

1. **vector** - 动态数组
   - 随机访问：O(1)
   - 尾部插入：均摊 O(1)
   - 中间插入：O(n)

2. **list** - 双向链表
   - 任意位置插入：O(1)
   - 随机访问：O(n)

3. **deque** - 双端队列
   - 两端插入：O(1)
   - 随机访问：O(1)

### 关联容器

1. **map** - 键值对映射
   - 查找：O(log n)
   - 有序存储

2. **set** - 唯一元素集合
   - 查找：O(log n)
   - 自动排序

3. **unordered_map** - 哈希映射
   - 查找：平均 O(1)
   - 无序存储

## 代码示例

### 示例 1：Vector 使用

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // 创建 vector
    std::vector<int> vec = {1, 2, 3, 4, 5};
    
    // 添加元素
    vec.push_back(6);
    vec.emplace_back(7);
    
    // 访问元素
    std::cout << "First element: " << vec[0] << std::endl;
    std::cout << "Last element: " << vec.back() << std::endl;
    
    // 遍历
    for (int x : vec) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    
    // 排序
    std::sort(vec.begin(), vec.end());
    
    // 二分查找
    auto it = std::lower_bound(vec.begin(), vec.end(), 4);
    if (it != vec.end()) {
        std::cout << "Found: " << *it << std::endl;
    }
    
    return 0;
}
```

### 示例 2：Map 使用

```cpp
#include <iostream>
#include <map>
#include <string>

int main() {
    // 创建 map
    std::map<std::string, int> scores;
    
    // 插入键值对
    scores["Alice"] = 95;
    scores["Bob"] = 87;
    scores.insert({"Charlie", 92});
    
    // 查找
    std::string name = "Alice";
    if (scores.find(name) != scores.end()) {
        std::cout << name << "'s score: " << scores[name] << std::endl;
    }
    
    // 遍历
    for (const auto& pair : scores) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    
    return 0;
}
```

### 示例 3：Set 使用

```cpp
#include <iostream>
#include <set>

int main() {
    // 创建 set
    std::set<int> s = {3, 1, 4, 1, 5, 9, 2, 6};
    
    // 自动去重和排序
    std::cout << "Set contents: ";
    for (int x : s) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    
    // 查找
    if (s.find(5) != s.end()) {
        std::cout << "5 is in the set" << std::endl;
    }
    
    // 插入和删除
    s.insert(7);
    s.erase(3);
    
    return 0;
}
```

### 示例 4：Unordered_map（哈希表）

```cpp
#include <iostream>
#include <unordered_map>
#include <string>

int main() {
    // 创建 unordered_map
    std::unordered_map<std::string, int> word_count;
    
    // 统计词频
    std::string text = "hello world hello c++";
    std::string word;
    for (char c : text) {
        if (c == ' ') {
            word_count[word]++;
            word.clear();
        } else {
            word += c;
        }
    }
    word_count[word]++;
    
    // 输出统计结果
    for (const auto& pair : word_count) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    
    return 0;
}
```

### 示例 5：机器学习应用 - 特征存储

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

class FeatureStore {
private:
    std::unordered_map<std::string, std::vector<double>> features;
    
public:
    void addFeature(const std::string& name, const std::vector<double>& values) {
        features[name] = values;
    }
    
    std::vector<double> getFeature(const std::string& name) {
        if (features.find(name) != features.end()) {
            return features[name];
        }
        return {};
    }
    
    void printAllFeatures() {
        for (const auto& pair : features) {
            std::cout << pair.first << ": ";
            for (double val : pair.second) {
                std::cout << val << " ";
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    FeatureStore store;
    
    // 添加特征
    store.addFeature("age", {25, 30, 35, 40});
    store.addFeature("income", {50000, 60000, 70000, 80000});
    store.addFeature("score", {85.5, 92.3, 78.9, 95.2});
    
    // 获取特征
    auto age = store.getFeature("age");
    std::cout << "Age feature size: " << age.size() << std::endl;
    
    // 打印所有特征
    store.printAllFeatures();
    
    return 0;
}
```

## ACM 竞赛应用

### 使用 vector 和 map 解决问题

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

int main() {
    // 快速 IO
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int n;
    std::cin >> n;
    
    std::vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
    
    // 使用 map 统计频率
    std::map<int, int> freq;
    for (int x : arr) {
        freq[x]++;
    }
    
    // 找出现次数最多的元素
    int max_freq = 0, most_common = arr[0];
    for (const auto& pair : freq) {
        if (pair.second > max_freq) {
            max_freq = pair.second;
            most_common = pair.first;
        }
    }
    
    std::cout << "Most common: " << most_common 
              << " (appears " << max_freq << " times)" << std::endl;
    
    return 0;
}
```

## 注意事项

⚠️ **常见错误**

1. **迭代器失效**
   ```cpp
   std::vector<int> vec = {1, 2, 3};
   auto it = vec.begin();
   vec.push_back(4);  // it 可能失效！
   // std::cout << *it;  // 错误
   ```

2. **错误的容器选择**
   - 频繁中间插入 → 使用 list
   - 需要随机访问 → 使用 vector
   - 需要快速查找 → 使用 map/set

✅ **最佳实践**

1. **使用 emplace_back 代替 push_back**
   ```cpp
   vec.emplace_back(arg1, arg2);  // 更高效
   ```

2. **使用 reserve 预分配空间**
   ```cpp
   vec.reserve(1000);  // 避免多次重新分配
   ```

3. **使用 auto 简化迭代器**
   ```cpp
   for (const auto& x : vec) { ... }
   ```

## 相关概念

- [[02_STL_Iterators]] - 迭代器
- [[03_Algorithms]] - 算法
- [[06_Pointers]] - 指针