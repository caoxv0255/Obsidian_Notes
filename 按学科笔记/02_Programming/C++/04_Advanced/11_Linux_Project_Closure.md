---
type: advanced
topic: linux_project_closure
category: advanced
difficulty: advanced
acm_relevant: false
engineering_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, Linux, 项目实战, 工程闭环, 后端]
---

# Linux C++ 工程闭环与项目实战

> 这一页不是讲单个知识点，而是讲一个工程项目从“能跑”到“能交付”的闭环。

## 1) 推荐的项目结构

```text
project/
  CMakeLists.txt
  include/
  src/
  tests/
  benchmark/
  configs/
  scripts/
  docs/
```

## 2) 一个项目至少要有的四件事

- 配置：端口、日志级别、线程数、超时、缓存大小。
- 日志：错误日志、请求日志、性能日志。
- 测试：单元测试 + 集成测试 + 压测。
- 观测：QPS、延迟、错误率、内存占用、fd 占用。

## 3) 推荐的项目路线

1. [HTTP 静态文件服务器](12_HTTP_Static_File_Server.md)
2. [简化版 KV 存储](13_KV_Storage_From_Scratch.md)
3. [轻量 RPC 框架](14_Lightweight_RPC_Framework.md)
4. [Shell 从零实现](15_Shell_From_Scratch.md)
5. [Git 从零实现](16_Git_From_Scratch.md)
6. [区块链 / 加密货币从零实现](17_Blockchain_Cryptocurrency_From_Scratch.md)
7. [Network Stack 从零实现](18_Network_Stack_From_Scratch.md)

这些项目按“网络入口 -> 协议处理 -> 存储落盘 -> 观测与压测”的顺序展开，也和 0Voice 与 build-your-own-x 的交集方向一致。

## 4) 外部路线对齐

- CodeCrafters 的 `build-your-own-x` 更适合作为“从零实现系统组件”的项目灵感库，重点可取 Web Server、Database、Network Stack、Operating System、Blockchain / Cryptocurrency、Git 和 Shell。
- 0Voice 的课程大纲更偏“Linux C/C++ 工程落地”，重点覆盖后端、高性能网络、存储、基础架构、安全，也兼顾音视频、游戏和嵌入式的工程化能力。
- 两者结合后，最适合当前笔记体系的交集不是泛泛地堆项目，而是按“网络入口 -> 协议处理 -> 存储落盘 -> 观测与压测”的顺序，把项目补成闭环。

## 5) 可直接开工的具体项目

### 5.1 HTTP 静态文件服务器

- 核心模块：`epoll` 事件循环、`accept`/`read`/`write` 封装、HTTP 请求解析、静态文件映射、连接复用、日志。
- 实现顺序：单线程阻塞版 -> `epoll` 版 -> 线程池版 -> 支持 `keep-alive` -> 支持目录页和 `404` 页面 -> 增加简单压测脚本。
- 验收标准：能稳定处理并发连接，支持 `GET`/`HEAD`，超时连接会被正确回收，错误请求有明确日志。

### 5.2 简化版 KV 存储

- 核心模块：内存表、命令解析、追加写日志、快照恢复、简单过期策略。
- 实现顺序：内存 `map` 版 -> AOF 版 -> 快照恢复版 -> 崩溃恢复版 -> 基础压测与数据校验。
- 验收标准：重启后数据可恢复，写入与查询接口稳定，能解释数据丢失和恢复边界。

### 5.3 轻量 RPC 服务框架

- 核心模块：请求帧封装、序列化、超时控制、心跳、错误码、连接池。
- 实现顺序：定长包头版 -> 请求 ID 版 -> 超时与重试版 -> 简单服务注册版 -> 压测与链路追踪日志。
- 验收标准：能区分业务失败和网络失败，客户端能看到明确的超时和重试结果。

### 5.4 从零实现系统组件的补充选题

- `Shell`：命令解析、重定向、管道、后台任务。
- `Git`：对象存储、提交、分支、日志、检出。
- `Blockchain / Cryptocurrency`：区块头、哈希链、工作量证明、交易校验、链一致性检查。
- `Network Stack`：ARP、IP、TCP 连接状态、重传与超时的最小模型。

## 6) 每个项目都要写清楚的验收标准

- 能处理什么协议。
- 多少并发下还能稳定。
- 失败时如何降级或退出。
- 如何重启、如何排障、如何回滚。

## 7) 0Voice 方向的具体对齐点

- 后端与网络：Nginx、TCP/IP、epoll、线程池、负载均衡、连接管理。
- 存储与数据库：MySQL、Redis、持久化、缓存、WAL、恢复流程。
- 基础架构：Linux 内核、文件系统、性能优化、容器和虚拟化。
- 高性能与工程化：DPDK、压测、监控、故障定位、资源隔离。

## 8) 文档化的最小清单

- 架构图：线程模型、事件模型、数据流。
- 启动方式：参数、配置、环境变量。
- 排错清单：常见错误、定位工具、恢复步骤。
- 压测结论：瓶颈和优化前后对比。

## 9) 与前面笔记的对应关系

- [CMake + 调试诊断](06_CMake_Debug_Toolchain.md)
- [epoll + Reactor 服务器骨架](07_Epoll_Reactor_Server.md)
- [Linux 网络编程：socket、TCP、epoll](09_Network_Programming_Socket_Epoll.md)
- [Linux C++ 并发与性能调优](10_Concurrency_Performance_Tuning.md)
