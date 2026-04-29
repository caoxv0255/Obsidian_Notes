---
type: project
topic: java_practice_cli
category: java
difficulty: intermediate
prerequisites: [[03_Java_JVM_Concurrency]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# Java 实战：命令行任务管理器

## 目标

做一个小型 CLI 程序，支持添加任务、列出任务、标记完成和保存到文件。这个项目会把基础语法、OOP、集合、文件 I/O 和测试连起来。

## 模块拆分

- `model`：Task 对象。
- `service`：任务管理逻辑。
- `storage`：文件读写。
- `cli`：命令解析与交互。
- `test`：JUnit 测试。

## 实现顺序

1. 先在内存里维护任务列表。
2. 再做命令解析。
3. 接入文件保存和加载。
4. 增加排序、筛选和状态更新。
5. 最后补测试和打包配置。

## 数据模型

```java
public record Task(long id, String title, boolean done) {
}
```

## 服务骨架

```java
import java.util.ArrayList;
import java.util.List;

public class TaskService {
    private final List<Task> tasks = new ArrayList<>();

    public Task add(String title) {
        Task task = new Task(tasks.size() + 1L, title, false);
        tasks.add(task);
        return task;
    }

    public List<Task> list() {
        return List.copyOf(tasks);
    }
}
```

## 文件保存思路

- 先用简单的文本格式保存。
- 每行一个任务，字段用分隔符拼接。
- 加载时做解析和容错。

## 常见坑

- 让 UI、服务逻辑和存储逻辑耦合在一起。
- 没有测试就直接写复杂的解析器。
- 没处理空输入和重复任务。

## 练习

1. 给任务管理器加 `done` 和 `delete`。
2. 写一个文件存储实现。
3. 给 `TaskService` 写 JUnit 测试。