---
type: concept
topic: basic_syntax
category: fundamentals
difficulty: beginner
prerequisites: []
acm_relevant: true
created: 2026-02-20
status: complete
---

# C++ 基本语法

## 核心定义

C++ 是一种静态类型、编译式的通用编程语言，支持多种编程范式（过程式、面向对象、泛型编程）。基本语法包括程序结构、注释、语句和表达式等基础元素。

## 直观解释

想象你要写一篇文章，你需要知道：
- 文章的结构（开头、正文、结尾）→ 程序的结构
- 如何添加注释和说明 → 注释语法
- 如何写完整的句子 → 语句
- 如何表达想法 → 表达式

C++ 的基本语法就像写文章的规则，告诉你如何组织代码，让计算机能够理解你的意图。

## 详细说明

### 程序的基本结构

一个完整的 C++ 程序通常包含：
1. **预处理指令**：以 `#` 开头，如 `#include`
2. **主函数**：`int main()` 是程序的入口
3. **语句**：每条语句以分号 `;` 结尾
4. **返回值**：程序结束时返回一个整数值

### 注释

注释用于解释代码，不会被编译器执行：
- **单行注释**：以 `//` 开头
- **多行注释**：以 `/*` 开始，以 `*/` 结束

### 命名空间

使用命名空间可以避免命名冲突：
- `using namespace std;` 使用标准命名空间
- 或直接使用 `std::` 前缀

## 代码示例

### 示例 1：最简单的 C++ 程序

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### 示例 2：使用注释

```cpp
#include <iostream>

// 这是单行注释

/*
这是多行注释
可以跨越多行
*/

int main() {
    // 输出文本到控制台
    std::cout << "Hello, World!" << std::endl;  // endl 表示换行
    return 0;  // 返回 0 表示程序正常结束
}
```

### 示例 3：基本语句和表达式

```cpp
#include <iostream>

int main() {
    // 声明变量
    int a = 10;
    int b = 20;
    
    // 表达式和语句
    int sum = a + b;  // 算术表达式
    int product = a * b;  // 乘法表达式
    
    // 输出结果
    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b << std::endl;
    std::cout << "a + b = " << sum << std::endl;
    std::cout << "a * b = " << product << std::endl;
    
    return 0;
}
```

### 示例 4：使用命名空间

```cpp
#include <iostream>

// 方法 1：使用 using 声明
using std::cout;
using std::endl;

int main() {
    cout << "使用 using 声明" << endl;
    return 0;
}
```

```cpp
#include <iostream>

// 方法 2：使用 using namespace（不推荐在头文件中使用）
using namespace std;

int main() {
    cout << "使用 using namespace" << endl;
    return 0;
}
```

```cpp
#include <iostream>

// 方法 3：使用 std:: 前缀（推荐）
int main() {
    std::cout << "使用 std:: 前缀" << std::endl;
    return 0;
}
```

### 示例 5：多个输出

```cpp
#include <iostream>

int main() {
    int age = 25;
    double height = 1.75;
    std::string name = "张三";
    
    std::cout << "姓名: " << name << std::endl;
    std::cout << "年龄: " << age << " 岁" << std::endl;
    std::cout << "身高: " << height << " 米" << std::endl;
    
    return 0;
}
```

## ACM 竞赛应用

### 快速 IO 模板

```cpp
#include <iostream>
#include <cstdio>

// ACM 竞赛常用的快速 IO 模板
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int a, b;
    std::cin >> a >> b;
    std::cout << a + b << std::endl;
    
    return 0;
}
```

### 标准输出格式

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double pi = 3.141592653589793;
    
    // 保留两位小数
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "PI = " << pi << std::endl;
    
    // 科学计数法
    std::cout << std::scientific << pi << std::endl;
    
    return 0;
}
```

## 机器学习应用

### 输出模型信息

```cpp
#include <iostream>
#include <string>
#include <vector>

int main() {
    // 模拟神经网络模型信息
    std::string model_name = "Neural Network";
    int input_size = 784;
    int hidden_size = 128;
    int output_size = 10;
    double learning_rate = 0.01;
    
    std::cout << "================================" << std::endl;
    std::cout << "模型信息" << std::endl;
    std::cout << "================================" << std::endl;
    std::cout << "模型名称: " << model_name << std::endl;
    std::cout << "输入层大小: " << input_size << std::endl;
    std::cout << "隐藏层大小: " << hidden_size << std::endl;
    std::cout << "输出层大小: " << output_size << std::endl;
    std::cout << "学习率: " << learning_rate << std::endl;
    std::cout << "================================" << std::endl;
    
    return 0;
}
```

## 注意事项

⚠️ **常见错误**

1. **忘记分号**
   ```cpp
   int a = 10  // 错误：缺少分号
   int a = 10;  // 正确
   ```

2. **头文件拼写错误**
   ```cpp
   #include <iostream>  // 正确
   #include <iosteam>   // 错误：拼写错误
   ```

3. **使用未声明的变量**
   ```cpp
   int a = 10;
   std::cout << b;  // 错误：b 未声明
   ```

✅ **最佳实践**

1. **使用有意义的变量名**
   ```cpp
   int age = 25;  // 好
   int a = 25;    // 不好
   ```

2. **适当使用注释**
   ```cpp
   // 计算两个数的和
   int sum = a + b;
   ```

3. **一致的代码风格**
   - 使用一致的缩进（通常是 4 个空格）
   - 使用有意义的命名
   - 保持代码整洁

## 相关概念

- [[02_Variables_Types]] - 变量和数据类型
- [[03_Operators]] - 运算符
- [[04_Control_Flow]] - 控制流

## 练习题

1. 编写一个程序，输出你的姓名、年龄和爱好
2. 计算 1 到 100 的和并输出结果
3. 输出一个乘法表（9x9）
4. 编写一个程序，交换两个变量的值并输出
5. 输出当前日期和时间（使用标准库）

## 参考资料

- C++ Basic Syntax - cppreference.com
- Learn C++ - learncpp.com
- C++ Core Guidelines - isocpp.org