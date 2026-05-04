#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

struct SubarrayResult {
    int max_sum;
    int left;
    int right;
    
    SubarrayResult() : max_sum(0), left(-1), right(-1) {}
    SubarrayResult(int sum, int l, int r) : max_sum(sum), left(l), right(r) {}
};

SubarrayResult max_crossing_subarray(const std::vector<int>& A, int low, int mid, int high) {
    int left_sum = INT_MIN;
    int sum = 0;
    int max_left = mid;
    
    for (int i = mid; i >= low; --i) {
        sum += A[i];
        if (sum > left_sum) {
            left_sum = sum;
            max_left = i;
        }
    }
    
    int right_sum = INT_MIN;
    sum = 0;
    int max_right = mid + 1;
    
    for (int j = mid + 1; j <= high; ++j) {
        sum += A[j];
        if (sum > right_sum) {
            right_sum = sum;
            max_right = j;
        }
    }
    
    return SubarrayResult(left_sum + right_sum, max_left, max_right);
}

SubarrayResult max_subarray_divide_conquer(const std::vector<int>& A, int low, int high) {
    if (low == high) {
        return SubarrayResult(A[low], low, high);
    }
    
    int mid = low + (high - low) / 2;
    
    SubarrayResult left_result = max_subarray_divide_conquer(A, low, mid);
    SubarrayResult right_result = max_subarray_divide_conquer(A, mid + 1, high);
    SubarrayResult cross_result = max_crossing_subarray(A, low, mid, high);
    
    if (left_result.max_sum >= right_result.max_sum && 
        left_result.max_sum >= cross_result.max_sum) {
        return left_result;
    } else if (right_result.max_sum >= left_result.max_sum && 
               right_result.max_sum >= cross_result.max_sum) {
        return right_result;
    } else {
        return cross_result;
    }
}

SubarrayResult max_subarray_kadane(const std::vector<int>& A) {
    if (A.empty()) {
        return SubarrayResult();
    }
    
    int max_sum = A[0];
    int current_sum = A[0];
    int start = 0, end = 0, temp_start = 0;
    
    for (int i = 1; i < A.size(); ++i) {
        if (current_sum + A[i] < A[i]) {
            current_sum = A[i];
            temp_start = i;
        } else {
            current_sum += A[i];
        }
        
        if (current_sum > max_sum) {
            max_sum = current_sum;
            start = temp_start;
            end = i;
        }
    }
    
    return SubarrayResult(max_sum, start, end);
}

void print_subarray_result(const SubarrayResult& result, const std::vector<int>& A) {
    if (result.left == -1 || result.right == -1) {
        std::cout << "最大子数组和: " << result.max_sum << " (空数组)" << std::endl;
        return;
    }
    
    std::cout << "最大子数组和: " << result.max_sum << std::endl;
    std::cout << "索引范围: [" << result.left << ", " << result.right << "]" << std::endl;
    std::cout << "子数组内容: [";
    for (int i = result.left; i <= result.right; ++i) {
        std::cout << A[i];
        if (i < result.right) std::cout << ", ";
    }
    std::cout << "]" << std::endl;
}

int main() {
    std::cout << "=== 分治策略测试：最大子数组问题 ===" << std::endl;
    std::cout << std::endl;
    
    std::vector<int> A = {13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7};
    
    std::cout << "输入数组: [";
    for (size_t i = 0; i < A.size(); ++i) {
        std::cout << A[i];
        if (i < A.size() - 1) std::cout << ", ";
    }
    std::cout << "]" << std::endl;
    std::cout << std::endl;
    
    std::cout << "分治法结果: ";
    auto result1 = max_subarray_divide_conquer(A, 0, A.size() - 1);
    print_subarray_result(result1, A);
    
    std::cout << "\nKadane算法结果: ";
    auto result2 = max_subarray_kadane(A);
    print_subarray_result(result2, A);
    
    std::cout << "\n两种算法结果一致: " << (result1.max_sum == result2.max_sum ? "是" : "否") << std::endl;
    
    return 0;
}
