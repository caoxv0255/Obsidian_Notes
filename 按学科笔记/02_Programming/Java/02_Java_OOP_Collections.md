---
type: concept
topic: java_oop_collections
category: java
difficulty: intermediate
prerequisites: [[01_Java_Basics]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# Java 面向对象与集合框架

## 核心定义

Java 的 OOP 重点是封装、继承、多态和接口；集合框架则提供了 `List`、`Set`、`Map` 等常用容器。

这部分是 Java 的核心竞争力之一：它把“对象建模”和“标准容器”统一在一套类型系统里。

## 快速参考

- `interface` 适合描述能力，`abstract class` 适合描述共享骨架。
- 泛型让集合和工具类保持类型安全。
- `ArrayList` 适合随机访问，`HashMap` 适合键值查询。
- 用对象做 `Map` 的键时，要实现 `equals()` 和 `hashCode()`。
- 继承适合“is-a”，组合更常见也更灵活。
- `Comparable` 和 `Comparator` 用于排序。
- `Iterator` 能安全遍历并删除元素。

## OOP 要点

| 概念 | 作用 |
|------|------|
| 封装 | 隐藏内部状态，只暴露稳定 API |
| 继承 | 复用父类行为，表达 is-a 关系 |
| 多态 | 同一接口，不同实现 |
| 接口 | 只声明能力，不关心实现细节 |
| 抽象类 | 共享代码和部分约束 |

## 集合速查

| 容器 | 特点 | 常见用途 |
|------|------|----------|
| `ArrayList` | 动态数组，随机访问快 | 顺序数据、缓存 |
| `LinkedList` | 链表 | 插删频繁但很少随机访问 |
| `HashSet` | 无序去重 | 判重、集合运算 |
| `HashMap` | 键值映射 | 计数、索引、缓存 |
| `TreeMap` | 有序映射 | 排序键值、范围查询 |

## 代码示例

```java
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class WordCount {
    public static void main(String[] args) {
        List<String> words = List.of("java", "rust", "java", "js");
        Map<String, Integer> count = new HashMap<>();

        for (String word : words) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }

        System.out.println(count);
    }
}
```

## 补充示例：接口与多态

```java
interface Shape {
    double area();
}

class Circle implements Shape {
    private final double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}
```

## 重点

- `List` 保证顺序，`Set` 负责去重，`Map` 负责映射。
- `Stream` 适合做声明式处理，但先把集合 API 学熟。
- `record` 可用于表达简单不可变数据对象（较新版本 Java）。
- 泛型擦除会影响运行时类型信息。
- 可变对象当作 `HashMap` 键非常危险。

## 常见坑

- 忘记重写 `hashCode()`。
- 在增强 `for` 中删除集合元素。
- 过度继承，忽视组合。
- 对泛型使用原始类型导致类型不安全。

## 练习

1. 用 `Map` 统计单词频率。
2. 写一个 `interface` 和两个实现类。
3. 对比 `ArrayList` 和 `LinkedList` 的使用场景。
4. 写一个 `Comparator` 对学生按分数排序。