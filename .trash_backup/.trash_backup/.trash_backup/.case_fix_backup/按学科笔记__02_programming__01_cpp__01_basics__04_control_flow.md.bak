---
type: concept
topic: Control Flow
category: basics
difficulty: 基础
prerequisites: [[03_Operators]]
acm_relevant: true
created: 2026-02-20
status: learning
estimated_time: 2.0
practice_problems: 5
ml_relevance: high
cpp_standard: 11
tags: [编程/C++, 基础/控制流, ACM/基础, ML/算法基础]
---

# 控制流 (Control Flow)

> 控制流语句用于控制程序的执行顺序，包括条件判断和循环

## 📌 核心定义

控制流语句决定了程序中语句的执行顺序。C++ 提供了条件语句（if-else、switch）、循环语句（for、while、do-while）和跳转语句（break、continue、goto）。

## 💡 直觉理解

控制流就像交通规则：
- if-else = 分岔路口，根据条件选择方向
- 循环 = 环形路，反复执行直到满足条件
- break = 出口标志，跳出当前循环
- continue = 继续标志，跳过本次循环

## 📖 详细说明

### 1. if-else 语句

```cpp
if (condition) {
    // 条件为真时执行
} else if (another_condition) {
    // 另一个条件为真时执行
} else {
    // 所有条件都为假时执行
}
```

### 2. switch 语句

```cpp
switch (expression) {
    case value1:
        // 代码
        break;
    case value2:
        // 代码
        break;
    default:
        // 默认代码
}
```

### 3. for 循环

```cpp
for (initialization; condition; update) {
    // 循环体
}
```

### 4. while 循环

```cpp
while (condition) {
    // 循环体
}
```

### 5. do-while 循环

```cpp
do {
    // 循环体
} while (condition);
```

## 💻 代码示例

### 示例 1: if-else 使用

```cpp
#include <iostream>

int main() {
    int score = 85;
    
    if (score >= 90) {
        std::cout << "优秀" << std::endl;
    } else if (score >= 80) {
        std::cout << "良好" << std::endl;
    } else if (score >= 60) {
        std::cout << "及格" << std::endl;
    } else {
        std::cout << "不及格" << std::endl;
    }
    
    return 0;
}
```

### 示例 2: for 循环

```cpp
#include <iostream>

int main() {
    // 计算 1 到 100 的和
    int sum = 0;
    for (int i = 1; i <= 100; i++) {
        sum += i;
    }
    
    std::cout << "1 + 2 + ... + 100 = " << sum << std::endl;
    
    return 0;
}
```

### 示例 3: 嵌套循环（ACM 常用）

```cpp
#include <iostream>

int main() {
    // 打印九九乘法表
    for (int i = 1; i <= 9; i++) {
        for (int j = 1; j <= i; j++) {
            std::cout << j << "x" << i << "=" << i*j << "\t";
        }
        std::cout << std::endl;
    }
    
    return 0;
}
```

## 🎯 应用场景

### ACM 竞赛中的应用
- 模拟题：使用循环和条件判断
- 贪心算法：使用循环遍历
- 搜索算法：使用递归和循环

### 机器学习中的应用
- 迭代优化：使用 for 循环
- 条件判断：使用 if-else
- 数据预处理：使用循环遍历数据

## ⚠️ 注意事项

| 注意事项 | 说明 |
|----------|------|
| 循环条件 | 确保循环能够终止 |
| 分号遗漏 | if 后面不要加分号 |
| break vs continue | break 跳出循环，continue 跳过本次 |
| 循环变量 | for 循环中的变量作用域 |

## 🔗 相关概念

- [[03_Operators]] - 运算符
- [[05_Functions]] - 函数

## 📝 练习题

1. 编写程序判断一个数是否为素数
2. 编写程序打印斐波那契数列前 20 项

## 📚 参考资料

- [C++ Reference - Control Flow](https://en.cppreference.com/w/cpp/language/statements)