# 01_Python 基础语法

> 📅 学习日期：2026-04-07
> 🎯 学习目标：掌握 Python 基本语法元素，为后续数据科学学习打下坚实基础

---

## 一、Hello World 与 Python 基本运行

Python 是目前最流行的编程语言之一，尤其在数据科学、机器学习、Web 开发等领域应用广泛。相比 C++ 或 Java，Python 的语法简洁清晰，非常适合零基础学习者入门。

让我们从最简单的程序开始：

```python
print("Hello, World!")
```

执行结果：
```
Hello, World!
```

`print()` 是 Python 的内置函数，用于向屏幕输出内容。Python 的代码不需要像 C 语言那样用分号结尾，也不需要用大括号包裹代码块——它靠**缩进**来识别代码结构。

```python
# 这是单行注释
"""
这是多行注释（也叫做文档字符串）
通常用于模块、函数或类的说明
"""

print("Python 入门第一步！")
```

> 💡 **小贴士**：Python 3 和 Python 2 在语法上有些差异，建议初学者直接学习 Python 3。本教程默认使用 Python 3。

---

## 二、变量与数据类型

### 2.1 变量是什么？

变量是程序中用于**存储数据**的容器。你可以把它想象成一个贴了标签的盒子，盒子里放什么数据由你决定。

```python
name = "Alice"      # 字符串类型
age = 20            # 整数类型
height = 1.68       # 浮点数类型
is_student = True   # 布尔类型
```

在上面的例子中：
- `name`、`age`、`height`、`is_student` 是变量名
- `=` 是赋值符号，表示把右边的值赋给左边的变量

### 2.2 Python 的基本数据类型

Python 内置了丰富的数据类型，主要有以下几种：

| 类型 | 说明 | 示例 |
|------|------|------|
| `int` | 整数 | `10`, `-5`, `0` |
| `float` | 浮点数（小数） | `3.14`, `-0.5` |
| `str` | 字符串 | `"Hello"`, `'Python'` |
| `bool` | 布尔值 | `True`, `False` |
| `list` | 列表（有序可变） | `[1, 2, 3]` |
| `tuple` | 元组（有序不可变） | `(1, 2, 3)` |
| `dict` | 字典（键值对） | `{"name": "Alice"}` |

```python
# 字符串
message = "欢迎学习 Python！"
print(message)

# 列表
fruits = ["苹果", "香蕉", "橙子"]
print(fruits)

# 字典
person = {"姓名": "小明", "年龄": 18, "专业": "数据科学"}
print(person)
```

### 2.3 类型转换

不同类型之间可以相互转换，这在做数据处理时非常有用：

```python
# 字符串转整数
num_str = "100"
num_int = int(num_str)  # 转换为整数
print(num_int + 50)     # 输出 150

# 整数转字符串
age = 20
age_str = str(age)
print("我的年龄是 " + age_str)

# 浮点数转整数（会截断小数部分）
pi = 3.14159
pi_int = int(pi)  # 结果是 3，不是四舍五入

# 列表转字符串
nums = [1, 2, 3]
nums_str = str(nums)  # "[1, 2, 3]"
```

---

## 三、运算符

### 3.1 算术运算符

```python
a, b = 10, 3

print(a + b)   # 加法：13
print(a - b)   # 减法：7
print(a * b)   # 乘法：30
print(a / b)   # 除法：3.3333...（结果始终是浮点数）
print(a // b)  # 整除：3（取整数部分）
print(a % b)   # 取余：1
print(a ** b)  # 幂运算：10的3次方 = 1000
```

### 3.2 比较运算符

比较运算符返回布尔值（`True` 或 `False`）：

```python
x, y = 5, 8

print(x == y)  # 等于：False
print(x != y)  # 不等于：True
print(x < y)   # 小于：True
print(x > y)   # 大于：False
print(x <= y)  # 小于等于：True
print(x >= y)  # 大于等于：False
```

### 3.3 逻辑运算符

```python
a, b = True, False

print(a and b)  # 逻辑与：False
print(a or b)   # 逻辑或：True
print(not a)   # 逻辑非：False
```

> ⚠️ **注意**：Python 中的 `and`、`or`、`not` 与 C/Java 中的 `&&`、`||`、`!` 不同，是英文单词。

### 3.4 赋值运算符

```python
n = 10
n += 5    # 相当于 n = n + 5，结果是 15
n -= 3    # 相当于 n = n - 3，结果是 12
n *= 2    # 相当于 n = n * 2，结果是 24
n /= 4    # 相当于 n = n / 4，结果是 6.0
n //= 2   # 相当于 n = n // 2，结果是 3.0
```

---

## 四、控制流：条件语句

### 4.1 if 语句

Python 的条件语句结构如下：

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("需要努力")
```

**注意**：Python 用**缩进**（通常4个空格）来区分代码块，同一层级的代码必须有相同的缩进。

### 4.2 嵌套条件

```python
age = 20
has_ticket = True

if age >= 18:
    print("已成年")
    if has_ticket:
        print("可以进入")
    else:
        print("需要购票")
else:
    print("未成年，需要成人陪同")
```

### 4.3 三元表达式

如果条件分支很简单，可以用一行代码完成：

```python
score = 75
result = "及格" if score >= 60 else "不及格"
print(result)  # 及格
```

---

## 五、控制流：循环

### 5.1 for 循环

`for` 循环用于遍历可迭代对象（字符串、列表、元组等）：

```python
# 遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
for fruit in fruits:
    print(fruit)

# 使用 range() 生成数字序列
print("\n1到10的整数：")
for i in range(1, 11):   # range(start, stop) 不包含 stop
    print(i, end=" ")
print()

# range() 的三种形式
print(list(range(5)))      # [0, 1, 2, 3, 4]        — 一个参数，从0开始
print(list(range(2, 8)))   # [2, 3, 4, 5, 6, 7]     — 两个参数，从start到stop-1
print(list(range(0, 10, 3))) # [0, 3, 6, 9]        — 三个参数，step=3
```

### 5.2 while 循环

`while` 循环在条件为真时反复执行：

```python
count = 0
while count < 5:
    print(f"当前计数：{count}")
    count += 1
print("循环结束")

# 猜数字游戏示例
import random
target = random.randint(1, 10)
guess = 0
attempts = 0

while guess != target:
    guess = int(input("猜一个1-10之间的数字："))
    attempts += 1
    if guess < target:
        print("太小了，再试一次！")
    elif guess > target:
        print("太大了，再试一次！")
    else:
        print(f"恭喜你！猜对了！用了 {attempts} 次机会。")
```

### 5.3 循环控制：break 和 continue

```python
# break：提前跳出循环
for i in range(1, 10):
    if i == 5:
        print("遇到5，跳出循环")
        break
    print(i, end=" ")
# 输出：1 2 3 4 遇到5，跳出循环

# continue：跳过当前迭代，进入下一次
print("\n跳过偶数：")
for i in range(1, 8):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i, end=" ")
# 输出：1 3 5 7
```

### 5.4 列表推导式

列表推导式是 Python 的特色语法，可以在一行内生成新列表：

```python
# 传统写法
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# 列表推导式写法
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# 带条件的列表推导式
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
```

---

## 六、函数基础

### 6.1 定义和调用函数

函数是组织代码的基本单位，可以提高代码的复用性：

```python
def greet(name):
    """问候函数"""
    return f"你好，{name}！欢迎学习 Python。"

message = greet("小明")
print(message)
```

### 6.2 参数默认值

```python
def power(base, exponent=2):
    """计算base的exponent次方，默认 exponent=2（平方"""
    return base ** exponent

print(power(3))      # 9（默认平方）
print(power(3, 3))   # 27（立方）
print(power(exponent=3, base=2))  # 8（关键字参数，可以打乱顺序）
```

### 6.3 可变参数

```python
# *args：接收任意数量的位置参数
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))         # 6
print(sum_all(10, 20, 30, 40))  # 100

# **kwargs：接收任意数量的关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=20, major="数据科学")
# 输出：
# name: Alice
# age: 20
# major: 数据科学
```

### 6.4 函数的返回值

```python
def check_grade(score):
    """根据分数返回等级"""
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade  # 返回结果

result = check_grade(85)
print(f"等级：{result}")  # 等级：B
```

### 6.5 变量作用域

```python
x = 10  # 全局变量

def test_scope():
    x = 20  # 局部变量，与全局变量同名
    print(f"函数内部 x = {x}")

test_scope()
print(f"函数外部 x = {x}")  # 输出：函数内部 x = 20，函数外部 x = 10

# 如果想在函数内修改全局变量，使用 global 关键字
def test_global():
    global x
    x = 20
    print(f"修改后函数内部 x = {x}")

test_global()
print(f"修改后函数外部 x = {x}")  # 输出：20
```

---

## 七、字符串处理

### 7.1 字符串基本操作

```python
s = "Hello, Python!"

print(s[0])        # H（索引，从0开始）
print(s[-1])       # !（最后一个字符）
print(s[0:5])      # Hello（切片，左闭右开）
print(s[7:])       # Python!（从第7个字符到末尾）
print(s.upper())  # HELLO, PYTHON!
print(s.lower())  # hello, python!
print(len(s))      # 14（字符串长度）
```

### 7.2 字符串方法

```python
s = "  欢迎来到 Python 世界！  "

print(s.strip())       # 去除首尾空格
print(s.replace("Python", "数据分析"))  # 替换
print(s.split(","))    # 按逗号分割 → ['  欢迎来到 Python 世界！  ']

# 字符串格式化
name = "小明"
age = 18
print(f"我叫{name}，今年{age}岁")  # f-string（推荐写法）

# format 方法
template = "我叫{}，今年{}岁"
print(template.format(name, age))

# % 格式化（旧式）
print("我叫%s，今年%d岁" % (name, age))
```

---

## 八、实战练习

### 练习 1：计算器函数

```python
def calculator(a, b, operator):
    """简单的计算器函数"""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "错误：除数不能为零"
    else:
        return "错误：不支持的运算符"

print(calculator(10, 3, "+"))   # 13
print(calculator(10, 3, "/"))   # 3.3333...
print(calculator(10, 0, "/"))   # 错误：除数不能为零
```

### 练习 2：判断闰年

```python
def is_leap_year(year):
    """判断是否为闰年"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# 测试
for year in [2020, 2021, 2022, 2024, 1900, 2000]:
    result = "是闰年" if is_leap_year(year) else "不是闰年"
    print(f"{year}年 {result}")
```

---

## 📌 本章小结

| 知识点 | 关键内容 |
|--------|----------|
| 变量 | 赋值、常见数据类型、类型转换 |
| 运算符 | 算术、比较、逻辑、赋值 |
| 条件语句 | if / elif / else，缩进规则 |
| 循环 | for / while，break / continue，列表推导式 |
| 函数 | 定义、参数默认值、可变参数、返回值、作用域 |
| 字符串 | 索引、切片、常用方法、格式化 |

> 🚀 **下一章预告**：学习完基础语法后，我们将进入科学计算的世界——NumPy 和 Matplotlib 是 Python 数据分析的左膀右臂！

---

*笔记整理：AI 姐姐 🧡*
