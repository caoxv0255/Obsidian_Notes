---
type: concept
topic: preprocessor
category: compilation
difficulty: intermediate
prerequisites: [[02_Variables_Types]], [[05_Functions]]
acm_relevant: true
created: 2026-02-20
status: complete
---

# C++ 预处理器

## 核心定义

预处理器是 C++ 编译过程中的第一个阶段，它在实际编译之前对源代码进行文本替换和条件编译处理。预处理器指令以 # 开头，不是 C++ 语句，不需要以分号结尾。

## 直观解释

想象一个文本编辑器，在编译器看到你的代码之前，它会先扫描你的代码，做一些简单的"查找和替换"操作。比如，它会把所有的 PI 替换成 3.14159，把某些代码片段插入到指定位置，或者根据条件决定保留或删除某些代码。

## 详细说明

### 主要的预处理器指令

1. **#define - 宏定义**
   - 定义符号常量或宏函数
   - 在预处理阶段进行文本替换

2. **#include - 文件包含**
   - 将指定文件的内容插入到当前位置
   - 用于包含头文件

3. **#ifdef / #ifndef / #endif - 条件编译**
   - 根据宏是否定义来决定是否编译某段代码

4. **#if / #elif / #else - 条件编译**
   - 根据表达式的值决定是否编译

5. **#undef - 取消宏定义**

6. **#error - 生成编译错误**

7. **#pragma - 编译器特定指令**

## 代码示例

### 示例 1：符号常量宏定义

```cpp
#include <iostream>

#define PI 3.14159
#define MAX_SIZE 1000
#define DEBUG_MODE true

int main() {
    double radius = 5.0;
    double area = PI * radius * radius;
    
    int arr[MAX_SIZE];
    
    if (DEBUG_MODE) {
        std::cout << "Radius: " << radius << std::endl;
        std::cout << "Area: " << area << std::endl;
    }
    
    return 0;
}
```
### 示例 2：带参数的宏函数

```cpp
#include <iostream>

#define SQUARE(x) ((x) * (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define ABS(x) ((x) < 0 ? -(x) : (x))

int main() {
    int a = 5, b = 10;
    
    std::cout << "SQUARE(5) = " << SQUARE(5) << std::endl;
    std::cout << "MAX(5, 10) = " << MAX(a, b) << std::endl;
    std::cout << "ABS(-7) = " << ABS(-7) << std::endl;
    
    // 注意：宏的参数要加上括号，避免运算符优先级问题
    int x = 3;
    std::cout << "SQUARE(x+1) = " << SQUARE(x+1) << std::endl;  // 正确：16
    
    return 0;
}
```
### 示例 3：条件编译（防止头文件重复包含）

```cpp
// myheader.h
#ifndef MYHEADER_H
#define MYHEADER_H

void myFunction();
int myVariable = 42;

#endif  // MYHEADER_H
```
```cpp
// main.cpp
#include <iostream>
#include "myheader.h"
#include "myheader.h"  // 第二次包含不会导致重复定义错误

int main() {
    myFunction();
    std::cout << "myVariable = " << myVariable << std::endl;
    return 0;
}
```
### 示例 4：条件编译（调试版本和发布版本）

```cpp
#include <iostream>

#define DEBUG_MODE

void processArray(int arr[], int size) {
    #ifdef DEBUG_MODE
        std::cout << "Processing array of size: " << size << std::endl;
        std::cout << "Array contents: ";
        for (int i = 0; i < size; i++) {
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;
    #endif
    
    // 实际处理逻辑
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    
    #ifdef DEBUG_MODE
        std::cout << "Sum: " << sum << std::endl;
    #endif
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    processArray(arr, 5);
    return 0;
}
```
### 示例 5：平台特定的代码

```cpp
#include <iostream>

// 检测操作系统平台
#if defined(_WIN32) || defined(_WIN64)
    #define PLATFORM_NAME "Windows"
    #define PATH_SEPARATOR "\\"
#elif defined(__linux__)
    #define PLATFORM_NAME "Linux"
    #define PATH_SEPARATOR "/"
#elif defined(__APPLE__)
    #define PLATFORM_NAME "macOS"
    #define PATH_SEPARATOR "/"
#else
    #define PLATFORM_NAME "Unknown"
    #define PATH_SEPARATOR "/"
#endif

int main() {
    std::cout << "Running on: " << PLATFORM_NAME << std::endl;
    std::cout << "Path separator: " << PATH_SEPARATOR << std::endl;
    return 0;
}
```
## ACM 竞赛应用

### 快速 IO 配置

```cpp
#include <iostream>
#include <cstdio>

// 快速 IO 宏定义
#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL)
#define endl '\n'

int main() {
    FAST_IO;  // 启用快速 IO
    
    int n;
    std::cin >> n;
    
    for (int i = 0; i < n; i++) {
        int x;
        std::cin >> x;
        std::cout << x * 2 << endl;
    }
    
    return 0;
}
```
### 调试开关

```cpp
#include <iostream>

#define ONLINE_JUDGE

#ifdef ONLINE_JUDGE
    #define debug(x)
#else
    #define debug(x) std::cout << "[DEBUG] " << #x << " = " << x << std::endl
#endif

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    
    for (int i = 0; i < 5; i++) {
        debug(arr[i]);  // 在本地调试时会输出，在线评测时会被忽略
    }
    
    return 0;
}
```
### 多测试用例处理

```cpp
#include <iostream>

#define MAX_N 100005
#define MOD 1000000007

int arr[MAX_N];

int solve() {
    int n;
    std::cin >> n;
    
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
    
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        sum = (sum + arr[i]) % MOD;
    }
    
    return sum;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int t;
    std::cin >> t;
    while (t--) {
        std::cout << solve() << '\n';
    }
    
    return 0;
}
```
## 机器学习应用

### 编译时配置参数

```cpp
#include <iostream>

// 机器学习模型的编译时配置
#define INPUT_SIZE 784      // MNIST 输入维度
#define HIDDEN_SIZE 128     // 隐藏层大小
#define OUTPUT_SIZE 10      // 输出类别数
#define LEARNING_RATE 0.01  // 学习率
#define BATCH_SIZE 32       // 批次大小
#define EPOCHS 100          // 训练轮数

struct NeuralNetwork {
    double weights1[INPUT_SIZE][HIDDEN_SIZE];
    double biases1[HIDDEN_SIZE];
    double weights2[HIDDEN_SIZE][OUTPUT_SIZE];
    double biases2[OUTPUT_SIZE];
};

void printConfig() {
    std::cout << "Neural Network Configuration:" << std::endl;
    std::cout << "Input Size: " << INPUT_SIZE << std::endl;
    std::cout << "Hidden Size: " << HIDDEN_SIZE << std::endl;
    std::cout << "Output Size: " << OUTPUT_SIZE << std::endl;
    std::cout << "Learning Rate: " << LEARNING_RATE << std::endl;
    std::cout << "Batch Size: " << BATCH_SIZE << std::endl;
    std::cout << "Epochs: " << EPOCHS << std::endl;
}

int main() {
    NeuralNetwork nn;
    printConfig();
    return 0;
}
```
### 条件编译优化

```cpp
#include <iostream>

// 根据是否使用 GPU 优化选择不同的实现
#define USE_GPU_OPTIMIZATION

void matrixMultiply(double* A, double* B, double* C, int n) {
    #ifdef USE_GPU_OPTIMIZATION
        std::cout << "Using GPU-optimized matrix multiplication" << std::endl;
        // GPU 实现代码
    #else
        std::cout << "Using CPU matrix multiplication" << std::endl;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                C[i * n + j] = 0;
                for (int k = 0; k < n; k++) {
                    C[i * n + j] += A[i * n + k] * B[k * n + j];
                }
            }
        }
    #endif
}

int main() {
    const int n = 100;
    double A[n * n], B[n * n], C[n * n];
    matrixMultiply(A, B, C, n);
    return 0;
}
```
## 注意事项

⚠️ **宏定义的陷阱**

1. **缺少括号导致优先级问题**
   ```cpp
   #define SQUARE(x) x * x  // 错误！
   SQUARE(x+1) 会展开为 x+1 * x+1，而不是 (x+1) * (x+1)
   
   // 正确做法：
   #define SQUARE(x) ((x) * (x))
   ```
2. **宏函数的副作用**
   ```cpp
   #define MAX(a, b) ((a) > (b) ? (a) : (b))
   int x = 5;
   MAX(x++, x)  // x 会被递增两次！
   ```
3. **宏没有类型检查**
   - 宏只是文本替换，不进行类型检查
   - 容易导致难以发现的错误

4. **调试困难**
   - 宏展开后的代码难以阅读和调试

✅ **最佳实践**

1. **使用 const 或 constexpr 代替符号常量宏**
   ```cpp
   // 推荐：
   const double PI = 3.14159;
   constexpr int MAX_SIZE = 1000;
   
   // 不推荐：
   #define PI 3.14159
   #define MAX_SIZE 1000
   ```
2. **使用内联函数代替宏函数**
   ```cpp
   // 推荐：
   inline int square(int x) { return x * x; }
   
   // 不推荐：
   #define SQUARE(x) ((x) * (x))
   ```
3. **始终使用 #ifndef 保护头文件**
   ```cpp
   #ifndef HEADER_H
   #define HEADER_H
   // 头文件内容
   #endif
   ```
4. **给宏参数和整个表达式加上括号**
   ```cpp
   #define MIN(a, b) (((a) < (b)) ? (a) : (b))
   ```
## 相关概念

- [[02_Variables_Types]] - 变量和常量
- [[05_Functions]] - 函数定义和调用
- [[12_Const_Volatile]] - const 关键字
- [[20_Best_Practices]] - 最佳实践

## 练习题

1. 编写一个宏 IS_EVEN(x)，判断 x 是否为偶数
2. 使用条件编译实现一个可以在不同平台上运行的程序
3. 编写一个宏 SWAP(a, b)，交换两个变量的值
4. 创建一个头文件，并使用 #ifndef 保护它
5. 使用 #ifdef 实现调试输出功能

## 参考资料

- C++ Preprocessor - cppreference.com
- The C Preprocessor - gcc.gnu.org
- Effective C++ - Item 1: Prefer const and inline to #define
