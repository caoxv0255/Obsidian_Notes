---
type: concept
topic: error_handling
category: robustness
difficulty: intermediate
prerequisites: [[05_Functions]], [[12_Const_Volatile]]
acm_relevant: true
created: 2026-02-20
status: complete
---

# C++ 错误处理

## 核心定义

错误处理是程序中用于检测、报告和恢复异常情况的机制。C++ 提供了多种错误处理方式，包括断言（assert）、错误码、异常处理（try-catch）等，帮助开发者编写健壮的代码。

## 直观解释

想象你在开车，如果遇到红灯，你会停下来；如果遇到爆胎，你会靠边停车处理。错误处理就像汽车的仪表盘和应急系统，它会在出现问题（红灯、爆胎）时提醒你，并提供处理方案（停车、换胎），而不是让汽车继续行驶直到出事故。

## 详细说明

### 错误处理的主要方式

1. **断言（assert）**
   - 用于调试阶段检查程序的不变量
   - 在 Release 模式下会被移除
   - 用于检测"不应该发生"的情况

2. **错误码**
   - 函数返回特定的值表示错误
   - 需要调用者检查返回值
   - 传统 C 风格的错误处理

3. **异常处理（try-catch）**
   - 使用 try、catch、throw 关键字
   - 可以在调用栈中向上传播错误
   - 适用于严重错误

4. **错误对象**
   - 使用结构体或类封装错误信息
   - 可以提供详细的错误描述

### 错误处理的选择

- **断言**：用于调试，检查前提条件
- **错误码**：用于可预期的错误，需要立即处理
- **异常**：用于严重错误，需要特殊处理
- **错误对象**：需要详细错误信息的情况

## 代码示例

### 示例 1：使用 assert 进行调试检查

```cpp
#include <iostream>
#include <cassert>
#include <cmath>

double divide(double a, double b) {
    assert(b != 0 && "Division by zero!");  // 如果 b == 0，程序会终止
    return a / b;
}

double sqrtSafe(double x) {
    assert(x >= 0 && "Cannot calculate square root of negative number!");
    return std::sqrt(x);
}

int main() {
    std::cout << "10 / 2 = " << divide(10, 2) << std::endl;
    std::cout << "sqrt(16) = " << sqrtSafe(16) << std::endl;
    
    // 这些 assert 会在运行时检查，如果条件不满足，程序会终止
    // divide(10, 0);   // 这会触发 assert
    // sqrtSafe(-4);    // 这会触发 assert
    
    return 0;
}
```
### 示例 2：使用错误码

```cpp
#include <iostream>
#include <string>

enum ErrorCode {
    SUCCESS = 0,
    INVALID_INPUT = -1,
    DIVISION_BY_ZERO = -2,
    FILE_NOT_FOUND = -3
};

ErrorCode divide(double a, double b, double* result) {
    if (b == 0) {
        return DIVISION_BY_ZERO;
    }
    *result = a / b;
    return SUCCESS;
}

ErrorCode readFile(const std::string& filename, std::string* content) {
    if (filename.empty()) {
        return INVALID_INPUT;
    }
    
    // 模拟文件读取
    if (filename == "nonexistent.txt") {
        return FILE_NOT_FOUND;
    }
    
    *content = "File content here";
    return SUCCESS;
}

void printError(ErrorCode code) {
    switch (code) {
        case SUCCESS:
            std::cout << "Operation successful" << std::endl;
            break;
        case INVALID_INPUT:
            std::cout << "Error: Invalid input" << std::endl;
            break;
        case DIVISION_BY_ZERO:
            std::cout << "Error: Division by zero" << std::endl;
            break;
        case FILE_NOT_FOUND:
            std::cout << "Error: File not found" << std::endl;
            break;
        default:
            std::cout << "Error: Unknown error" << std::endl;
    }
}

int main() {
    double result;
    ErrorCode code = divide(10, 2, &result);
    
    if (code == SUCCESS) {
        std::cout << "Result: " << result << std::endl;
    } else {
        printError(code);
    }
    
    code = divide(10, 0, &result);
    if (code != SUCCESS) {
        printError(code);
    }
    
    std::string content;
    code = readFile("nonexistent.txt", &content);
    if (code != SUCCESS) {
        printError(code);
    }
    
    return 0;
}
```
### 示例 3：使用异常处理

```cpp
#include <iostream>
#include <stdexcept>
#include <string>

class InvalidInputException : public std::runtime_error {
public:
    InvalidInputException(const std::string& msg) : std::runtime_error(msg) {}
};

class DivisionByZeroException : public std::runtime_error {
public:
    DivisionByZeroException() : std::runtime_error("Division by zero") {}
};

double divide(double a, double b) {
    if (b == 0) {
        throw DivisionByZeroException();
    }
    return a / b;
}

void processInput(int value) {
    if (value < 0) {
        throw InvalidInputException("Input must be non-negative");
    }
    std::cout << "Processing: " << value << std::endl;
}

int main() {
    // 示例 1: 基本的 try-catch
    try {
        std::cout << "10 / 2 = " << divide(10, 2) << std::endl;
        std::cout << "10 / 0 = " << divide(10, 0) << std::endl;
    } catch (const DivisionByZeroException& e) {
        std::cerr << "Caught exception: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Caught general exception: " << e.what() << std::endl;
    }
    
    // 示例 2: 处理多种异常类型
    try {
        processInput(42);
        processInput(-10);
    } catch (const InvalidInputException& e) {
        std::cerr << "Invalid input: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    
    // 示例 3: 捕获所有异常
    try {
        throw std::string("Custom string exception");
    } catch (...) {
        std::cerr << "Caught an unknown exception" << std::endl;
    }
    
    return 0;
}
```
### 示例 4：错误对象和详细信息

```cpp
#include <iostream>
#include <string>
#include <vector>

struct Error {
    bool success;
    std::string message;
    int code;
    
    Error(bool s, const std::string& msg, int c = 0) 
        : success(s), message(msg), code(c) {}
    
    static Error ok() {
        return Error(true, "Success");
    }
    
    static Error fail(const std::string& msg, int code = -1) {
        return Error(false, msg, code);
    }
};

Error divide(double a, double b, double* result) {
    if (b == 0) {
        return Error::fail("Division by zero", 1001);
    }
    *result = a / b;
    return Error::ok();
}

Error readFile(const std::string& filename, std::vector<std::string>* lines) {
    if (filename.empty()) {
        return Error::fail("Filename is empty", 2001);
    }
    
    // 模拟文件读取
    if (filename == "missing.txt") {
        return Error::fail("File not found: " + filename, 2002);
    }
    
    lines->push_back("Line 1");
    lines->push_back("Line 2");
    lines->push_back("Line 3");
    
    return Error::ok();
}

void handleError(const Error& err) {
    if (!err.success) {
        std::cerr << "Error [" << err.code << "]: " << err.message << std::endl;
    }
}

int main() {
    double result;
    Error err = divide(10, 2, &result);
    
    if (err.success) {
        std::cout << "Result: " << result << std::endl;
    } else {
        handleError(err);
    }
    
    err = divide(10, 0, &result);
    if (!err.success) {
        handleError(err);
    }
    
    std::vector<std::string> lines;
    err = readFile("missing.txt", &lines);
    if (!err.success) {
        handleError(err);
    }
    
    return 0;
}
```
### 示例 5：资源获取即初始化（RAII）和异常安全

```cpp
#include <iostream>
#include <fstream>
#include <stdexcept>

class FileHandler {
private:
    std::ofstream file;
    
public:
    FileHandler(const std::string& filename) {
        file.open(filename);
        if (!file.is_open()) {
            throw std::runtime_error("Failed to open file: " + filename);
        }
        std::cout << "File opened: " << filename << std::endl;
    }
    
    ~FileHandler() {
        if (file.is_open()) {
            file.close();
            std::cout << "File closed" << std::endl;
        }
    }
    
    void write(const std::string& content) {
        file << content;
    }
};

void processData(const std::string& input) {
    FileHandler fh("output.txt");
    fh.write("Processing: ");
    fh.write(input);
    
    if (input.empty()) {
        throw std::runtime_error("Input is empty");
    }
    
    // 如果抛出异常，FileHandler 的析构函数会被自动调用
}

int main() {
    try {
        processData("Hello, World!");
        std::cout << "Processing successful" << std::endl;
        
        processData("");  // 这会抛出异常
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    
    // FileHandler 会被正确关闭，即使发生了异常
    
    return 0;
}
```
## ACM 竞赛应用

在 ACM 竞赛中，错误处理相对简单，通常不需要复杂的异常处理：

### 使用 assert 进行边界检查

```cpp
#include <iostream>
#include <cassert>
#include <vector>

const int MAX_N = 100005;

void solve() {
    int n;
    std::cin >> n;
    
    assert(n > 0 && n <= MAX_N && "Invalid array size!");
    
    std::vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
        assert(arr[i] >= 0 && arr[i] <= 1000000 && "Invalid array element!");
    }
    
    // 处理数组
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    
    std::cout << sum << std::endl;
}

int main() {
    int t;
    std::cin >> t;
    assert(t >= 1 && t <= 100 && "Invalid number of test cases!");
    
    while (t--) {
        solve();
    }
    
    return 0;
}
```
### 检查边界条件

```cpp
#include <iostream>
#include <string>
#include <algorithm>

bool isValidString(const std::string& s) {
    // 检查字符串是否只包含小写字母
    for (char c : s) {
        if (c < 'a' || c > 'z') {
            return false;
        }
    }
    return true;
}

void solve() {
    std::string s;
    std::cin >> s;
    
    // 检查字符串长度
    if (s.length() == 0 || s.length() > 1000) {
        std::cout << "Invalid string length" << std::endl;
        return;
    }
    
    // 检查字符串内容
    if (!isValidString(s)) {
        std::cout << "String contains invalid characters" << std::endl;
        return;
    }
    
    // 处理字符串
    std::sort(s.begin(), s.end());
    std::cout << s << std::endl;
}

int main() {
    solve();
    return 0;
}
```
## 机器学习应用

在机器学习应用中，错误处理非常重要，用于处理数据加载、模型训练等过程中的各种问题：

### 数据加载错误处理

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <stdexcept>

class DataLoadError : public std::runtime_error {
public:
    DataLoadError(const std::string& msg) : std::runtime_error(msg) {}
};

std::vector<std::vector<double>> loadCSV(const std::string& filename) {
    std::ifstream file(filename);
    
    if (!file.is_open()) {
        throw DataLoadError("Cannot open file: " + filename);
    }
    
    std::vector<std::vector<double>> data;
    std::string line;
    int lineNum = 0;
    
    while (std::getline(file, line)) {
        lineNum++;
        if (line.empty()) continue;
        
        std::vector<double> row;
        std::stringstream ss(line);
        std::string cell;
        int colNum = 0;
        
        while (std::getline(ss, cell, ',')) {
            colNum++;
            try {
                row.push_back(std::stod(cell));
            } catch (const std::exception& e) {
                throw DataLoadError("Invalid number at line " + std::to_string(lineNum) + 
                                   ", column " + std::to_string(colNum) + ": " + cell);
            }
        }
        
        if (row.empty()) {
            throw DataLoadError("Empty row at line " + std::to_string(lineNum));
        }
        
        data.push_back(row);
    }
    
    if (data.empty()) {
        throw DataLoadError("No data loaded from file: " + filename);
    }
    
    return data;
}

int main() {
    try {
        auto data = loadCSV("data.csv");
        std::cout << "Loaded " << data.size() << " rows, " 
                  << data[0].size() << " columns" << std::endl;
    } catch (const DataLoadError& e) {
        std::cerr << "Data loading error: " << e.what() << std::endl;
        return 1;
    } catch (const std::exception& e) {
        std::cerr << "Unexpected error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
```
### 模型训练错误处理

```cpp
#include <iostream>
#include <vector>
#include <stdexcept>

class TrainingError : public std::runtime_error {
public:
    TrainingError(const std::string& msg) : std::runtime_error(msg) {}
};

class NeuralNetwork {
private:
    std::vector<std::vector<double>> weights;
    std::vector<double> biases;
    
    bool validateInput(const std::vector<double>& input) {
        if (input.empty()) return false;
        if (input.size() != weights.size()) return false;
        return true;
    }
    
public:
    NeuralNetwork(int inputSize, int outputSize) {
        if (inputSize <= 0 || outputSize <= 0) {
            throw TrainingError("Invalid network dimensions");
        }
        
        weights.resize(inputSize, std::vector<double>(outputSize, 0.0));
        biases.resize(outputSize, 0.0);
    }
    
    std::vector<double> forward(const std::vector<double>& input) {
        if (!validateInput(input)) {
            throw TrainingError("Invalid input dimensions");
        }
        
        std::vector<double> output(biases.size(), 0.0);
        
        for (size_t j = 0; j < output.size(); j++) {
            for (size_t i = 0; i < input.size(); i++) {
                output[j] += input[i] * weights[i][j];
            }
            output[j] += biases[j];
        }
        
        return output;
    }
    
    void train(const std::vector<std::vector<double>>& inputs,
               const std::vector<std::vector<double>>& targets,
               double learningRate) {
        if (inputs.size() != targets.size()) {
            throw TrainingError("Number of inputs and targets must match");
        }
        
        if (inputs.empty()) {
            throw TrainingError("Training data is empty");
        }
        
        if (learningRate <= 0 || learningRate > 1) {
            throw TrainingError("Learning rate must be between 0 and 1");
        }
        
        std::cout << "Training with " << inputs.size() << " samples" << std::endl;
        // 简化的训练过程
    }
};

int main() {
    try {
        NeuralNetwork nn(10, 5);
        
        std::vector<std::vector<double>> inputs = {
            {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
            {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
        };
        
        std::vector<std::vector<double>> targets = {
            {0.1, 0.2, 0.3, 0.4, 0.5},
            {0.5, 0.4, 0.3, 0.2, 0.1}
        };
        
        nn.train(inputs, targets, 0.01);
        
        auto output = nn.forward(inputs[0]);
        std::cout << "Forward pass successful" << std::endl;
        
    } catch (const TrainingError& e) {
        std::cerr << "Training error: " << e.what() << std::endl;
        return 1;
    } catch (const std::exception& e) {
        std::cerr << "Unexpected error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
```
## 注意事项

⚠️ **错误处理的常见问题**

1. **滥用异常**
   - 异常不应该用于正常的控制流
   - 不要用异常来处理可预期的错误

2. **忽略错误码**
   ```cpp
   // 错误：忽略返回值
   divide(10, 0, &result);
   
   // 正确：检查返回值
   if (divide(10, 0, &result) != SUCCESS) {
       // 处理错误
   }
   ```
3. **捕获过于宽泛的异常**
   ```cpp
   // 不推荐：捕获所有异常
   try {
       // 代码
   } catch (...) {
       // 不知道发生了什么
   }
   
   // 推荐：捕获特定异常
   try {
       // 代码
   } catch (const std::runtime_error& e) {
       // 处理运行时错误
   }
   ```
4. **在析构函数中抛出异常**
   - 析构函数不应该抛出异常
   - 这会导致程序终止

✅ **最佳实践**

1. **使用 assert 进行调试检查**
   ```cpp
   assert(ptr != nullptr && "Pointer is null!");
   ```
2. **为可预期的错误使用错误码**
   ```cpp
   int result = func();
   if (result != 0) {
       // 处理错误
   }
   ```
3. **为严重错误使用异常**
   ```cpp
   if (fatalError) {
       throw std::runtime_error("Fatal error occurred");
   }
   ```
4. **提供详细的错误信息**
   ```cpp
   throw std::runtime_error("Failed to open file: " + filename + 
                            " (reason: " + strerror(errno) + ")");
   ```
5. **使用 RAII 确保资源释放**
   ```cpp
   {
       std::ofstream file("data.txt");
       // 如果抛出异常，文件会被自动关闭
   }
   ```
## 相关概念

- [[05_Functions]] - 函数的返回值
- [[12_Const_Volatile]] - const 关键字
- [[16_Memory_Management]] - 资源管理
- [[20_Best_Practices]] - 最佳实践

## 练习题

1. 编写一个函数，使用错误码来处理除法错误
2. 创建一个自定义异常类，并使用它来处理特定的错误情况
3. 使用 assert 来检查数组边界
4. 编写一个 RAII 类来管理文件资源
5. 实现一个错误处理函数，能够打印详细的错误信息

## 参考资料

- Error Handling - cppreference.com
- Exception Safety - isocpp.org
- assert.h - cplusplus.com
- C++ Core Guidelines - Error Handling
