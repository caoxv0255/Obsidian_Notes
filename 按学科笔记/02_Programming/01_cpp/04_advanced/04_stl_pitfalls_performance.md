---
type: concept
topic: stl_pitfalls_performance
category: advanced
difficulty: intermediate
prerequisites: [[../02_STL/01_Containers]], [[../02_STL/02_Iterators]]
acm_relevant: true
created: 2026-04-22
status: draft
cpp_standard: 11
tags: [编程/C++, STL, 工程/性能, ACM/技巧]
---

# STL 坑点与性能（写对复杂度）

## 核心目标
- 记住“迭代器失效/复杂度/内存”三件套
- 能在竞赛中写出稳定快的 STL 代码（`reserve`、避免退化）
- 能在工程中避免隐蔽 bug（`string_view` 生命周期、erase 习惯用法）

## 速查：容器选择
- `vector`：默认首选（cache 友好）
- `deque`：两端 push/pop
- `list`：需要稳定迭代器/频繁中间插入（但 cache 差）
- `map/set`：有序 + logN
- `unordered_map/set`：平均 O(1)，要关注 hash 退化与 rehash

## 必背要点（提纲）
### 1) 迭代器失效
- `vector` 扩容后，所有迭代器/引用/指针都可能失效
- `erase` 之后，被删除位置后的迭代器通常要重新获取
- `unordered_*` 在 rehash 后，迭代器失效风险更高

### 2) 常用算法套路
- `sort + unique`：去重
- `remove_if + erase`：删除满足条件的元素
- `lower_bound/upper_bound`：二分边界
- `nth_element`：找第 k 小，常用于竞赛选边界

### 3) 负载与预分配
- `vector::reserve` 能减少扩容次数
- `unordered_map::reserve` 能减少 rehash
- 频繁插入前先估算规模，通常比“边插边扩”稳定

## 关键坑点清单（待填）
### 1) 迭代器失效（必须背）
- `vector`：扩容会使所有迭代器/引用失效
- `deque`：插入删除可能失效（规则更复杂）
- `list`：插入不失效，删除只使被删元素迭代器失效
- `unordered_*`：rehash 会使迭代器失效

### 2) erase / remove_if 习惯用法
```cpp
// vector 删除满足条件的元素
v.erase(std::remove_if(v.begin(), v.end(), pred), v.end());
```

### 3) reserve / shrink_to_fit / rehash
- `vector::reserve(n)`：避免多次扩容
- `unordered_map::reserve(n)`：避免频繁 rehash

### 4) unordered_map 的性能与安全
- 负载因子、hash 函数质量、最坏退化
- 竞赛：必要时用自定义 hash

### 5) string 与 string_view
- `string_view` 不拥有内存：引用的字符串必须活得更久

### 6) 其他常见坑（占位）
- `vector<bool>` 特化
- `endl` 强制 flush
- `operator[]` 会插入（map/unordered_map）

## 最小可编译示例（补充）
### 示例：删除元素 + 去重 + 二分
```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
	std::vector<int> values = {5, 1, 2, 2, 3, 4, 5, 6};

	values.erase(std::remove_if(values.begin(), values.end(), [](int value) {
		return value % 2 == 0;
	}), values.end());

	std::sort(values.begin(), values.end());
	values.erase(std::unique(values.begin(), values.end()), values.end());

	auto it = std::lower_bound(values.begin(), values.end(), 3);
	if (it != values.end()) {
		std::cout << *it << '\n';
	}
}
```

## 练习（建议）
1. 写一份“容器选择题”：给场景选容器并说明复杂度
2. 用 `reserve` 前后对比 push_back 性能（计时）
3. 手工构造 `vector` 迭代器失效案例，确认什么时候必须重新取迭代器

## 相关链接
- [[../02_STL/01_Containers|STL 容器]]
- [[../02_STL/02_Iterators|STL 迭代器]]

## 参考资料
- cppreference：container requirements
- C++ Core Guidelines：ES.1 / Per.*
