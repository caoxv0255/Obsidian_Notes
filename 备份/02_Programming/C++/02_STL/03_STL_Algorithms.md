---
type: concept
topic: stl_algorithms
category: stl
difficulty: intermediate
prerequisites: [[01_Containers]], [[02_Iterators]]
acm_relevant: true
created: 2026-04-25
status: complete
---

# STL 算法库 (STL Algorithms)

## 核心定义

STL 算法库是定义在 `<algorithm>`、`<numeric>`、`<ranges>` 等头文件中的通用算法集合。算法与容器解耦，只依赖迭代器区间。

## 常用分类

1. 非修改序列：`all_of`、`any_of`、`count`、`find`
2. 修改序列：`copy`、`move`、`fill`、`transform`、`remove_if`
3. 排序相关：`sort`、`stable_sort`、`nth_element`、`partial_sort`
4. 二分相关：`lower_bound`、`upper_bound`、`binary_search`
5. 堆相关：`make_heap`、`push_heap`、`pop_heap`
6. 数值算法：`accumulate`、`partial_sum`、`iota`

## 复杂度与选型要点

- 全排序用 `sort`，复杂度 $O(n \log n)$。
- 只关心第 k 小用 `nth_element`，平均 $O(n)$。
- 区间有序后用 `lower_bound`，单次查询 $O(\log n)$。
- 稳定性要求保留相等元素相对顺序时，优先 `stable_sort`。

## 代码示例

```cpp
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> a = {7, 2, 9, 4, 1, 8, 3};

    std::sort(a.begin(), a.end());

    int x = 4;
    auto it = std::lower_bound(a.begin(), a.end(), x);
    if (it != a.end() && *it == x) {
        std::cout << "found " << x << "\n";
    }

    int sum = std::accumulate(a.begin(), a.end(), 0);
    std::cout << "sum=" << sum << "\n";

    std::nth_element(a.begin(), a.begin() + 2, a.end());
    std::cout << "3rd smallest=" << a[2] << "\n";
    return 0;
}
```

## 注意事项

- `remove`/`remove_if` 不会真的删除元素，要配合 `erase`：

```cpp
v.erase(std::remove(v.begin(), v.end(), target), v.end());
```

- 二分族算法要求区间已按同一比较规则排序，否则结果未定义。

## 相关链接

- [[01_Containers]]
- [[02_Iterators]]
- [[00_STL_Index|返回 STL 索引]]
