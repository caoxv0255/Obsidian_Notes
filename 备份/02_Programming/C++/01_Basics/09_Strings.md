---
type: concept
topic: Strings
category: basics
difficulty: 基础
prerequisites: [[08_Arrays]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 2.0
practice_problems: 5
ml_relevance: high
cpp_standard: 11
tags: [编程/C++, 基础/字符串, ACM/基础, ML/数据处理]
---

# 字符串 (Strings)

> 字符串是字符的序列，C++ 提供了 C 风格字符串和 std::string 类两种处理方式

## 📌 核心定义

字符串是由字符组成的序列。C++ 支持两种字符串类型：C 风格字符串（字符数组）和 C++ 标准库的 std::string 类。std::string 提供了更安全、更方便的字符串操作接口。

## 💡 直觉理解

字符串就像"项链"：
- 字符串 = 由珠子（字符）串成的项链
- 每个珠子 = 一个字符
- 字符串长度 = 珠子的数量
- 字符串结束 = 特殊的终止符

## 📖 详细说明

### 1. C 风格字符串

```cpp
char str1[] = "Hello";      // 自动计算大小，包含结束符
char str2[10] = "World";   // 手动指定大小
char str3[] = {'H', 'e', 'l', 'l', 'o', '\0'};  // 显式指定结束符
```
### 2. std::string 类

```cpp
#include <string>
std::string s1 = "Hello";      // 构造
std::string s2(5, 'a');       // 5 个 'a'
std::string s3 = s1 + s2;     // 拼接
```
### 3. 常用操作

| 操作 | C 风格 | std::string |
|------|--------|-------------|
| 长度 | strlen() | s.length() |
| 拼接 | strcat() | s1 + s2 |
| 复制 | strcpy() | s1 = s2 |
| 比较 | strcmp() | s1 == s2 |

## 💻 代码示例

### 示例 1: std::string 基本操作

```cpp
#include <iostream>
#include <string>

int main() {
    std::string s1 = "Hello";
    std::string s2 = "World";
    
    // 拼接
    std::string s3 = s1 + " " + s2;
    std::cout << "Concatenated: " << s3 << std::endl;
    
    // 长度
    std::cout << "Length: " << s3.length() << std::endl;
    
    // 访问字符
    std::cout << "First char: " << s3[0] << std::endl;
    
    // 子串
    std::string sub = s3.substr(0, 5);
    std::cout << "Substring: " << sub << std::endl;
    
    // 查找
    size_t pos = s3.find("World");
    if (pos != std::string::npos) {
        std::cout << "Found at position: " << pos << std::endl;
    }
    
    return 0;
}
```
### 示例 2: 字符串遍历

```cpp
#include <iostream>
#include <string>

int main() {
    std::string s = "Hello World";
    
    // 使用索引遍历
    for (size_t i = 0; i < s.length(); i++) {
        std::cout << s[i] << " ";
    }
    std::cout << std::endl;
    
    // 使用范围 for 循环
    for (char c : s) {
        std::cout << c << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```
### 示例 3: 字符串处理（ACM 常用）

```cpp
#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::string s = "  Hello World  ";
    
    // 去除空格
    s.erase(0, s.find_first_not_of(" "));
    s.erase(s.find_last_not_of(" ") + 1);
    std::cout << "Trimmed: '" << s << "'" << std::endl;
    
    // 转换为大写
    std::transform(s.begin(), s.end(), s.begin(), ::toupper);
    std::cout << "Uppercase: " << s << std::endl;
    
    // 反转字符串
    std::reverse(s.begin(), s.end());
    std::cout << "Reversed: " << s << std::endl;
    
    return 0;
}
```
### 示例 4: 机器学习中的应用

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

// 分割字符串（常用功能）
std::vector<std::string> split(const std::string& s, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    
    while (std::getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    
    return tokens;
}

int main() {
    // CSV 数据处理
    std::string csv = "1.0,2.5,3.7,4.2";
    std::vector<std::string> values = split(csv, ',');
    
    std::cout << "Features:" << std::endl;
    for (const auto& val : values) {
        std::cout << "  " << val << std::endl;
    }
    
    // 转换为 double
    std::vector<double> features;
    for (const auto& val : values) {
        features.push_back(std::stod(val));
    }
    
    std::cout << "As doubles:" << std::endl;
    for (double f : features) {
        std::cout << "  " << f << std::endl;
    }
    
    return 0;
}
```
## 🎯 应用场景

### ACM 竞赛中的应用
- 字符串处理：去除空格、转换大小写
- 字符串匹配：查找子串
- 数据解析：分割字符串

### 机器学习中的应用
- 数据预处理：文本清洗
- 特征提取：从文本中提取特征
- 文件处理：读取 CSV 数据

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| C 风格字符串 | 手动管理内存，容易出错 |
| 结束符 | C 风格字符串必须有 '\0' |
| std::string | 推荐，更安全更方便 |
| 字符串比较 | 使用 s1 == s2 而非 s1 == "hello" |

## 🔗 相关概念

- [[08_Arrays]] - 数组
- [[10_IO]] - 输入输出

## 📝 练习题

1. 编写函数反转字符串
2. 编写函数判断字符串是否为回文

## 📚 参考资料

- [C++ Reference - Strings](https://en.cppreference.com/w/cpp/string)
