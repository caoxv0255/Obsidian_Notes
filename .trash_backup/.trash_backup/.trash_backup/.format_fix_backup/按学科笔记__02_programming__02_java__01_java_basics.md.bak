---
type: concept
topic: java_basics
category: java
difficulty: beginner
prerequisites: [[00_Java_Index]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# Java 基础语法与类

## 核心定义

Java 是静态类型、面向对象、运行在 JVM 上的语言。它的入口通常是 `public static void main(String[] args)`。

Java 的设计重点是“类型明确、接口清晰、跨平台运行”。理解它时，先把它看成“编译成字节码，再交给 JVM 执行”的语言。

## 快速参考

- 变量默认有类型，数值、字符串、布尔值各自独立。
- 控制流主要是 `if`、`switch`、`for`、`while`。
- 类是 Java 的核心抽象，方法属于类或对象。
- `String` 不可变，数组长度固定。
- 基本类型包括 `byte`、`short`、`int`、`long`、`float`、`double`、`char`、`boolean`。
- 包装类 `Integer`、`Long` 等用于集合和泛型场景。
- Java 是“值传递”，对象引用也是按值复制。

## 语法地图

| 主题 | 要点 |
|------|------|
| 变量 | `int x = 1;`，类型必须明确 |
| 条件 | `if` / `switch` / 三元运算符 |
| 循环 | `for`、增强 `for`、`while`、`do-while` |
| 方法 | 形参、返回值、重载 |
| 类 | 字段、构造函数、实例方法、静态成员 |
| 包 | `package` / `import` 用于组织代码 |

## 代码示例

```java
public class Main {
    public static void main(String[] args) {
        Point point = new Point(3, 4);
        System.out.println(point.distance());
    }
}

class Point {
    private final int x;
    private final int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    int distance() {
        return x * x + y * y;
    }
}
```

## 补充示例：数组与字符串

```java
public class TextDemo {
    public static void main(String[] args) {
        String text = "hello";
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            builder.append(Character.toUpperCase(text.charAt(i)));
        }
        System.out.println(builder.toString());
    }
}
```

## 重点

- `==` 比较引用，`equals()` 比较内容。
- `final` 常用于常量、不可变字段和不可继承类。
- 每个源文件通常对应一个公开类。
- `StringBuilder` 适合循环拼接字符串。
- `null` 是 Java 里必须谨慎处理的值。

## 常见坑

- 把 `==` 当作内容比较。
- 忘记处理整数除法导致精度丢失。
- 误以为 `String` 可以原地修改。
- 忘记导入包或把类名和文件名写错。

## 练习

1. 写一个包含 `main`、构造函数和成员方法的最小类。
2. 比较 `==` 与 `equals()` 的差异。
3. 把一个二维点类改成不可变对象。
4. 用 `StringBuilder` 写一个字符串反转函数。