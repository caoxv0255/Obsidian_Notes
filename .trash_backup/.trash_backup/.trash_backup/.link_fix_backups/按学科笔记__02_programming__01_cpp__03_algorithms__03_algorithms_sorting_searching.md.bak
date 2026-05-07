---
type: concept
topic: algorithms_sort
category: algorithms
difficulty: intermediate
prerequisites: [[../02_STL/01_Containers]]
acm_relevant: true
created: 2026-02-20
status: complete
---

# 排序和搜索算法 (Sorting and Searching)

## 核心定义

排序和搜索是计算机科学中的基本算法，用于组织和查找数据。

## 直观解释

- **排序**：像整理书架，把书按顺序排列
- **搜索**：像在书架找书，快速找到目标

## 详细说明

### 常见排序算法

1. **快速排序**：平均 O(n log n)，最坏 O(n²)
2. **归并排序**：稳定 O(n log n)
3. **堆排序**：O(n log n)

### 搜索算法

1. **二分查找**：O(log n)，要求数组有序
2. **线性查找**：O(n)，适用于无序数据

## 代码示例

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> arr = {5, 2, 8, 1, 9, 3};
    
    // 排序
    std::sort(arr.begin(), arr.end());
    
    // 二分查找
    int target = 5;
    auto it = std::lower_bound(arr.begin(), arr.end(), target);
    
    if (it != arr.end() && *it == target) {
        std::cout << "Found " << target << " at position " 
                  << (it - arr.begin()) << std::endl;
    }
    
    return 0;
}
```