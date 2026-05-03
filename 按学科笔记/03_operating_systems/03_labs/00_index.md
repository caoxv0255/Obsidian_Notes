---
title: 操作系统实验索引
course: 操作系统
tags: [os, labs, index]
---

这里收录操作系统课程的动手实验与实验记录模板，配合 [01_shell_and_threading_lab.md](01_shell_and_threading_lab.md) 和 [02_process_and_memory_lab.md](02_process_and_memory_lab.md) 使用。

## 内容入口

- [Shell 与线程同步实验](01_shell_and_threading_lab.md)
- [进程观察与分页模拟](02_process_and_memory_lab.md)
- 章节实验：
	- [第1章实验](03_chapter01_lab.md)
	- [第2章实验](04_chapter02_lab.md)
	- [第3章实验](05_chapter03_lab.md)
	- [第4章实验](06_chapter04_lab.md)
	- [第5章实验](07_chapter05_lab.md)
	- [第6章实验](08_chapter06_lab.md)

## 实验目标

- 把课堂概念变成可观察现象。
- 把“知道”变成“能验证”。
- 把抽象机制落到命令、日志和图示上。

## 实验主题

### 1. 进程观察

- 观察 PID、PPID、状态、资源占用。
- 记录启动、运行、退出的生命周期。

### 2. 调度模拟

- 用简单程序模拟 FIFO、RR、Priority。
- 比较吞吐量、等待时间、响应时间。

### 3. 并发与同步

- 复现竞态条件。
- 用锁、信号量或条件变量修复问题。

### 4. 内存与分页

- 模拟页表和地址转换。
- 观察局部性和页面置换。

### 5. 文件系统与 I/O

- 观察文件访问路径和缓冲行为。
- 对比同步与异步 I/O。

## 实验记录模板

- 实验目的
- 环境信息
- 操作步骤
- 观测结果
- 问题分析
- 结论
