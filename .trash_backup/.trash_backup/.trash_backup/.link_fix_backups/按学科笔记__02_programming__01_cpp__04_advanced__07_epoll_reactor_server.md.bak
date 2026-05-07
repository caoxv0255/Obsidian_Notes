---
type: concept
topic: epoll_reactor
category: advanced
difficulty: advanced
prerequisites: [[06_CMake_Debug_Toolchain]], [[../01_Basics/16_Memory_Management]], [[../01_Basics/19_Error_Handling]]
acm_relevant: false
created: 2026-04-22
status: draft
cpp_standard: 11
tags: [编程/C++, Linux/网络, 工程/高性能网络, 后端]
---

# epoll + Reactor：从 0 到 1 的 TCP 服务器骨架

## 核心目标
- 跑通一个最小的 epoll TCP server（accept/read/write）
- 理解 Reactor：事件循环 + fd 回调 + 非阻塞 IO
- 能解释：LT/ET、backpressure、半包/粘包、连接状态机

## 必备前置（占位）
- socket 基础：`socket/bind/listen/accept/connect`
- 非阻塞：`fcntl(fd, O_NONBLOCK)`
- 错误码：`EAGAIN/EWOULDBLOCK/EINTR`

## 核心概念
- **Reactor**：事件到来时再分发处理
- **非阻塞 IO**：避免单个连接卡住整个线程
- **读写缓冲**：解决半包、粘包和部分写

## Reactor 结构（提纲）
- Acceptor：监听 socket，accept 新连接
- EventLoop：`epoll_wait` 拉取事件
- Connection：每个连接一个状态（读缓冲/写缓冲/协议解析）
- Handler：业务回调

## 事件与模式（提纲）
- LT（Level Trigger）：易写但可能频繁触发
- ET（Edge Trigger）：高性能但必须读/写到 `EAGAIN`

### 1) 推荐开发顺序
- 先做 LT 版本跑通
- 再切 ET 并补齐边界处理
- 最后加线程池和业务层解耦

## 最小伪代码（占位）
```text
setup_listen_fd(nonblocking)
add_to_epoll(listen_fd, READ)

while (true):
  events = epoll_wait()
  for ev in events:
    if ev.fd == listen_fd:
      while accept() succeeds:
        set_nonblocking(conn_fd)
        add_to_epoll(conn_fd, READ)
    else:
      if ev.readable:
        read_until_EAGAIN()
        parse_protocol_frames()
        maybe_enable_write_event()
      if ev.writable:
        write_until_EAGAIN()
        maybe_disable_write_event()
```

## 协议与缓冲（提纲）
- 建议先用“长度字段协议”（4 字节长度 + payload）
- 输入缓冲：累积 bytes → 尝试切帧
- 输出缓冲：未写完的数据留在缓冲，下次可写继续

## 最小可编译示例（补充）
### 事件循环伪代码对应的状态机
```text
state = ACCEPTING

if readable on listen_fd:
  accept until EAGAIN

if readable on conn_fd:
  append_to_input_buffer()
  while can_parse_frame():
    handle_frame()

if writable on conn_fd:
  flush_output_buffer_until_EAGAIN()
```

## 容易踩的坑（占位清单）
- [ ] ET 模式下没读到 `EAGAIN` 导致事件丢失
- [ ] 忘记处理 `EPOLLRDHUP`/对端关闭
- [ ] 写缓冲无限增长（无 backpressure）
- [ ] 业务逻辑阻塞 event loop（需要线程池/异步）

## 练习（建议）
1. 实现 echo server：支持多连接，稳定跑压测
2. 加入线程池：把业务处理从 IO 线程剥离
3. 增加统计：QPS/连接数/平均延迟
4. 为协议增加长度字段，验证粘包拆包处理是否正确

## 相关链接
- [[06_CMake_Debug_Toolchain|CMake + 调试诊断]]

## 参考资料
- APUE（网络/IO 相关章节）
- TCP/IP Illustrated（理解粘包/拥塞/重传）
- muduo 设计（Reactor 思路）
