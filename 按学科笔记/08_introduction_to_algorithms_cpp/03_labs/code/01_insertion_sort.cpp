#include <iostream>
#include <vector>
#include <span>
#include <algorithm>
#include <concepts>

/**
 * @brief 插入排序算法实现
 * 
 * @tparam T 可排序的类型（支持比较操作）
 * @param arr 待排序的数组（使用C++20 std::span）
 * 
 * @note 时间复杂度: O(n²) - 最坏和平均情况
 * @note 时间复杂度: O(n) - 最好情况（已排序）
 * @note 空间复杂度: O(1) - 原地排序
 * @note 稳定性: 稳定排序
 */
template <std::sortable T>
void insertion_sort(std::span<T> arr) {
    // 从第二个元素开始，假设第一个元素已经排序
    for (size_t i = 1; i < arr.size(); ++i) {
        T key = std::move(arr[i]);  // 移动语义优化
        auto j = static_cast<ptrdiff_t>(i) - 1;
        
        // 将大于key的元素向右移动
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = std::move(arr[j]);
            --j;
        }
        
        // 插入key到正确位置
        arr[j + 1] = std::move(key);
    }
}

/**
 * @brief 插入排序的迭代器版本（兼容STL容器）
 * 
 * @tparam It 随机访问迭代器类型
 * @param first 起始迭代器
 * @param last 结束迭代器
 */
template <std::random_access_iterator It>
void insertion_sort(It first, It last) {
    if (first == last) return;
    
    for (auto it = first + 1; it != last; ++it) {
        auto key = std::move(*it);
        auto current = it - 1;
        
        while (current >= first && *current > key) {
            *(current + 1) = std::move(*current);
            --current;
        }
        
        *(current + 1) = std::move(key);
    }
}

// ============ 测试用例 ============

/**
 * @brief 测试插入排序函数
 */
void test_insertion_sort() {
    std::cout << "=== 插入排序测试 ===" << std::endl;
    
    // 测试1: 整数数组
    {
        std::vector<int> numbers = {5, 2, 4, 6, 1, 3};
        std::cout << "原始数组: ";
        for (const auto& num : numbers) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
        
        insertion_sort(std::span{numbers});
        
        std::cout << "排序后: ";
        for (const auto& num : numbers) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }
    
    // 测试2: 已排序数组（最好情况）
    {
        std::vector<int> sorted = {1, 2, 3, 4, 5, 6};
        std::vector<int> copy = sorted;
        insertion_sort(std::span{copy});
        std::cout << "已排序数组测试: " 
                  << (copy == sorted ? "通过" : "失败") 
                  << std::endl;
    }
    
    // 测试3: 逆序数组（最坏情况）
    {
        std::vector<int> reversed = {6, 5, 4, 3, 2, 1};
        std::vector<int> expected = {1, 2, 3, 4, 5, 6};
        insertion_sort(std::span{reversed});
        std::cout << "逆序数组测试: " 
                  << (reversed == expected ? "通过" : "失败") 
                  << std::endl;
    }
    
    // 测试4: 字符串数组
    {
        std::vector<std::string> words = {"banana", "apple", "cherry", "date"};
        insertion_sort(std::span{words});
        
        std::cout << "字符串排序: ";
        for (const auto& word : words) {
            std::cout << word << " ";
        }
        std::cout << std::endl;
    }
    
    // 测试5: 空数组和单元素数组
    {
        std::vector<int> empty;
        std::vector<int> single = {42};
        
        insertion_sort(std::span{empty});
        insertion_sort(std::span{single});
        
        std::cout << "边界测试: " 
                  << (empty.empty() && single.size() == 1 ? "通过" : "失败") 
                  << std::endl;
    }
}

int main() {
    test_insertion_sort();
    return 0;
}
