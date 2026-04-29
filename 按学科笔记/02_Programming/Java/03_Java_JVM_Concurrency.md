---
type: concept
topic: java_jvm_concurrency
category: java
difficulty: intermediate
prerequisites: [[02_Java_OOP_Collections]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# Java JVM 与并发

## 核心定义

JVM 负责字节码执行、内存管理和垃圾回收；并发部分通常围绕线程、线程池和同步工具展开。

理解 Java 时，JVM 是绕不开的中间层。它负责把字节码翻译成真正执行的程序，并管理对象生命周期。

## 快速参考

- JVM 常见概念：堆、栈、方法区、类加载。
- `synchronized` 适合互斥，`volatile` 适合可见性。
- `ExecutorService` 比直接创建线程更适合管理任务。
- `ConcurrentHashMap` 适合高并发读写场景。
- `AtomicInteger` 适合无锁计数。
- `CountDownLatch`、`Semaphore`、`ReentrantLock` 是常用并发工具。

## JVM 速查

| 主题 | 要点 |
|------|------|
| 类加载 | 加载、验证、准备、解析、初始化 |
| 内存区域 | 堆、栈、方法区、程序计数器、本地方法栈 |
| GC | 标记清除、复制、分代回收、停顿 |
| 调优 | `-Xms`、`-Xmx`、GC 日志、堆转储 |

## 并发速查

| 工具 | 作用 |
|------|------|
| `Thread` | 直接创建线程 |
| `Runnable` / `Callable` | 任务抽象 |
| `ExecutorService` | 线程池管理 |
| `Future` | 异步结果 |
| `CompletableFuture` | 异步组合 |
| `synchronized` | 互斥 |
| `Lock` | 更灵活的锁控制 |

## 代码示例

```java
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class ParallelSum {
    public static void main(String[] args) throws Exception {
        ExecutorService pool = Executors.newFixedThreadPool(2);
        List<Callable<Integer>> tasks = List.of(
            () -> 1 + 2 + 3,
            () -> 4 + 5 + 6
        );

        int total = 0;
        for (Future<Integer> future : pool.invokeAll(tasks)) {
            total += future.get();
        }

        pool.shutdown();
        System.out.println(total);
    }
}
```

## 补充示例：原子计数

```java
import java.util.concurrent.atomic.AtomicInteger;

public class CounterDemo {
    public static void main(String[] args) {
        AtomicInteger counter = new AtomicInteger(0);
        counter.incrementAndGet();
        counter.addAndGet(2);
        System.out.println(counter.get());
    }
}
```

## 重点

- GC 不是越频繁越好，关键是延迟和吞吐平衡。
- 并发优先考虑任务分解、线程池和共享状态最小化。
- `CompletableFuture` 适合组合异步流程。
- 先判断是不是需要共享状态，再决定用锁还是线程封装。

## 常见坑

- 忘记关闭线程池。
- 把大量共享可变状态直接暴露给多个线程。
- 误判 `volatile` 能替代所有同步。
- 在高并发代码里随意使用不安全集合。

## 练习

1. 用线程池改写一个串行计算。
2. 用 `synchronized` 保护计数器。
3. 观察 `volatile` 与非 `volatile` 的差异。
4. 写一个返回 `CompletableFuture` 的异步函数。