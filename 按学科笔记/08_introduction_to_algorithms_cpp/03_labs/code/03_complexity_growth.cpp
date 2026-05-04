#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <chrono>

struct ComplexityFunctions {
    static long long constant(int n) {
        return 1;
    }
    
    static long long logarithmic(int n) {
        return static_cast<long long>(std::log2(n));
    }
    
    static long long linear(int n) {
        return n;
    }
    
    static long long linearithmic(int n) {
        return n * static_cast<long long>(std::log2(n));
    }
    
    static long long quadratic(int n) {
        return static_cast<long long>(n) * n;
    }
    
    static long long cubic(int n) {
        return static_cast<long long>(n) * n * n;
    }
    
    static long long exponential(int n) {
        if (n > 63) return LLONG_MAX;
        return 1LL << n;
    }
    
    static long long factorial(int n) {
        if (n > 20) return LLONG_MAX;
        long long result = 1;
        for (int i = 2; i <= n; ++i) {
            result *= i;
        }
        return result;
    }
};

long long linear_search(const std::vector<int>& arr, int target) {
    long long operations = 0;
    for (size_t i = 0; i < arr.size(); ++i) {
        operations++;
        if (arr[i] == target) {
            break;
        }
    }
    return operations;
}

long long binary_search(const std::vector<int>& arr, int target) {
    long long operations = 0;
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        operations++;
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return operations;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return operations;
}

void test_函数的增长() {
    std::cout << "=== 函数的增长测试 ===" << std::endl;
    
    std::cout << "\n测试1: 复杂度函数增长比较" << std::endl;
    std::vector<int> sizes = {10, 100, 1000, 10000};
    
    std::cout << std::left;
    std::cout << std::setw(10) << "n"
              << std::setw(15) << "O(1)"
              << std::setw(15) << "O(log n)"
              << std::setw(15) << "O(n)"
              << std::setw(15) << "O(n log n)"
              << std::setw(15) << "O(n²)"
              << std::setw(15) << "O(n³)" << std::endl;
    std::cout << std::string(100, '-') << std::endl;
    
    for (int n : sizes) {
        std::cout << std::setw(10) << n
                  << std::setw(15) << ComplexityFunctions::constant(n)
                  << std::setw(15) << ComplexityFunctions::logarithmic(n)
                  << std::setw(15) << ComplexityFunctions::linear(n)
                  << std::setw(15) << ComplexityFunctions::linearithmic(n)
                  << std::setw(15) << ComplexityFunctions::quadratic(n)
                  << std::setw(15) << ComplexityFunctions::cubic(n) << std::endl;
    }
    std::cout << std::endl;
}

int main() {
    test_函数的增长();
    return 0;
}
