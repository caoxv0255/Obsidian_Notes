# Python 环境与语法

## 核心概念

Python 是一种高级、解释型、面向对象的编程语言，由 Guido van Rossum 于 1991 年创建。Python 的设计哲学强调代码的可读性和简洁的语法，相较于 C、C++ 或 Java，Python 通常能用更少的代码表达相同的逻辑。

**Python 环境组成：**
- **Python 解释器**：执行 Python 代码的程序，主流版本是 Python 3.x
- **pip**：Python 包管理工具，用于安装和管理第三方库
- **虚拟环境（venv）**：隔离不同项目的依赖，避免版本冲突
- **conda**：另一个环境管理工具，特别流行于数据科学领域

**Python 语法特点：**
- 使用缩进（通常 4 个空格）来划分代码块，而不是花括号
- 变量不需要声明类型，类型由赋值决定（动态类型语言）
- 语句结尾不需要分号（但加上去也不会报错）
- 单行注释用 `#`，多行注释用 `'''` 或 `"""`

**数据科学常用环境：**
- **Anaconda**：打包了 Python + 150+ 科学计算库，适合新手
- **Miniconda**：精简版，只包含 Python + conda
- **Jupyter Notebook/Lab**：交互式编程环境，数据分析必备

## 代码实现

### 1. 安装与管理 Python 环境

```bash
# 检查 Python 版本
python --version
python3 --version

# 使用 venv 创建虚拟环境
python -m venv myenv
source myenv/bin/activate        # Linux/macOS
myenv\Scripts\activate          # Windows

# 使用 conda 创建环境
conda create -n myenv python=3.11
conda activate myenv

# pip 常用命令
pip install numpy pandas matplotlib
pip install numpy==1.24.0       # 指定版本
pip list                        # 查看已安装的包
pip freeze > requirements.txt   # 导出依赖
```

### 2. 第一个 Python 程序

```python
# hello.py
print("Hello, Python!")

# 变量与数据类型
name = "Data Science"      # 字符串
version = 3.11             # 浮点数
is_awesome = True          # 布尔值
students = 45              # 整数

# 多个变量赋值
x, y, z = 1, 2, 3

# 基本运算
a = 10
b = 3
print(a + b)   # 13 加法
print(a - b)   # 7  减法
print(a * b)   # 30 乘法
print(a / b)   # 3.333... 除法（总是浮点数）
print(a // b)  # 3  整除
print(a % b)   # 1  取余
print(a ** b)  # 1000 幂运算
```

### 3. 字符串操作

```python
# 字符串基本操作
s = "Data Science"
print(s.upper())           # DATA SCIENCE
print(s.lower())           # data science
print(s.split())           # ['Data', 'Science']
print(s.replace("Data", "Big"))  # Big Science

# 字符串格式化
name = "Alice"
age = 20

# f-string (Python 3.6+，推荐)
print(f"{name} is {age} years old")

# format 方法
print("{} is {} years old".format(name, age))

# 索引和切片
s = "Python"
print(s[0])      # P
print(s[-1])     # n
print(s[0:3])    # Pyt
print(s[::2])    # Pto (跳步)
```

### 4. Python 环境在数据科学中的实际应用

```python
# 查看已安装库的版本（数据科学必备）
import sys
print(f"Python 版本: {sys.version}")

try:
    import numpy as np
    print(f"NumPy 版本: {np.__version__}")
except ImportError:
    print("NumPy 未安装")

try:
    import pandas as pd
    print(f"Pandas 版本: {pd.__version__}")
except ImportError:
    print("Pandas 未安装")

try:
    import matplotlib
    print(f"Matplotlib 版本: {matplotlib.__version__}")
except ImportError:
    print("Matplotlib 未安装")

# 简单的数据分析流程
data = [25, 30, 35, 40, 45, 50, 55, 60]
mean_val = sum(data) / len(data)
print(f"平均值: {mean_val:.2f}")
```

## 实战技巧

**1. 使用 Jupyter Lab 进行探索性编程**
Jupyter Lab 是数据科学家最喜欢的开发环境，支持 Notebook、代码编辑、数据可视化等多种功能。安装方式：`pip install jupyterlab`，启动命令：`jupyter lab`

**2. 使用 `%timeit` 测量代码执行时间**
在 Jupyter 中，可以使用 magic 命令测量代码运行时间：
```python
%timeit [x**2 for x in range(1000)]
```

**3. 利用类型注解提高代码可读性**
虽然 Python 是动态类型语言，但添加类型注解可以让代码更易维护：
```python
def calculate_mean(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)
```

**4. 使用 `__main__` 入口**
编写脚本时，使用以下模式可以让你既可以作为模块导入，也可以直接运行：
```python
if __name__ == "__main__":
    main()
```

**5. requirements.txt 管理依赖**
在项目中创建 `requirements.txt`，团队成员可以一键安装所有依赖：`pip install -r requirements.txt`

## 常见错误

**1. IndentationError：缩进错误**
Python 使用缩进来划分代码块，混合使用空格和 Tab 是最常见的错误来源。
```python
# 错误示例
if True:
print("Hello")    # IndentationError

# 正确示例
if True:
    print("Hello")
```
**解决方案**：在编辑器中设置 Tab 转换为 4 个空格，并开启"显示空白字符"选项。

**2. NameError：变量未定义**
```python
# 错误示例
print(my_variable)   # NameError: name 'my_variable' is not defined

# 正确示例
my_variable = 100
print(my_variable)
```

**3. ModuleNotFoundError：模块未安装**
```python
# 错误示例
import numpy as np   # ModuleNotFoundError: No module named 'numpy'

# 解决方案：先安装
# pip install numpy
```

**4. 虚拟环境未激活导致的版本冲突**
在同一台机器上开发多个项目时，如果没有正确激活虚拟环境，可能会出现安装了包但运行时找不到的情况。养成习惯：每次开始项目前先激活虚拟环境。

**5. Python 2 与 Python 3 的语法差异**
```python
# Python 2 中 print 是语句
print "Hello"    # Python 2 有效

# Python 3 中 print 是函数
print("Hello")   # Python 3 必须加括号
```
**建议**：坚持使用 Python 3，避免使用已经不维护的 Python 2。
