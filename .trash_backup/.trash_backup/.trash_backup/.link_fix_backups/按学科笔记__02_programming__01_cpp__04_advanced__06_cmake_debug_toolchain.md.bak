---
type: concept
topic: cmake_debug_toolchain
category: advanced
difficulty: intermediate
prerequisites: [[../01_Basics/19_Error_Handling]]
acm_relevant: false
created: 2026-04-22
status: draft
cpp_standard: 11
tags: [编程/C++, 工程/CMake, 工程/调试, Linux]
---

# CMake + 调试诊断（gdb/core/sanitizers）

## 核心目标
- 能从 0 写一个可维护的 `CMakeLists.txt`
- 能在 Linux 上定位：崩溃、内存越界、未定义行为、数据竞争
- 建立“编译 → 运行 → 复现 → 定位 → 修复”的闭环

## 工程最小闭环（提纲）
1. CMake 配置 Debug/Release
2. 打开告警与调试符号
3. 启用 sanitizers（ASan/UBSan/TSan）
4. 生成 core dump + gdb 回溯

## CMake 关键点
- `CMAKE_CXX_STANDARD`：固定语言版本
- `target_compile_options`：按 target 加告警
- `target_link_libraries`：显式声明依赖
- 尽量用 target 级别配置，不要全局乱撒编译选项

## CMake 最小模板（占位）
```cmake
cmake_minimum_required(VERSION 3.20)
project(demo CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(demo main.cpp)

target_compile_options(demo PRIVATE -Wall -Wextra -Wpedantic)
```

## 常用诊断工具速查（占位）
### gdb
- `run` / `bt` / `frame` / `info locals`

### core dump
- `ulimit -c unlimited`
- `gdb ./demo core`

### sanitizers（建议在 Debug 下）
- ASan：越界/Use-after-free
- UBSan：未定义行为
- TSan：数据竞争

## 常用编译参数（占位）
- `-Wall -Wextra -Wpedantic`
- `-g -O0`：便于调试
- `-fsanitize=address,undefined`
- 多线程问题再考虑 `-fsanitize=thread`

## 最小可编译示例（补充）
### 一个带告警与调试信息的 CMake 目标
```cmake
cmake_minimum_required(VERSION 3.20)
project(demo CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(demo main.cpp)
target_compile_options(demo PRIVATE -Wall -Wextra -Wpedantic -g)
```

## 练习（建议）
1. 刻意写一个越界 bug，用 ASan 抓到堆栈
2. 写一个 double free，用 UBSan/ASan 对比报告
3. 给一个已有项目补上 `Debug`/`Release` 两套构建配置

## 相关链接
- [[07_Epoll_Reactor_Server|epoll/网络服务端（调试重点）]]

## 参考资料
- CMake 官方文档：target_* 体系
- LLVM Sanitizers 文档
- 《程序员的自我修养》《CSAPP》（相关章节）
