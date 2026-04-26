---
type: advanced
topic: linux_os_fundamentals
category: advanced
difficulty: intermediate
acm_relevant: false
engineering_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, Linux, 操作系统, 文件IO, 信号]
---

# Linux C++ 工程基础：进程、线程、信号与文件 I/O

> 这一页补的是 Linux C++ 的底层语义：进程/线程、fd、信号、阻塞与非阻塞、mmap。

## 1) 必须先分清的抽象

- 进程是资源容器，线程是调度实体。
- 文件描述符是内核对象的句柄，不是文件本身。
- 信号是异步通知，不是同步函数调用。
- 阻塞 I/O 和非阻塞 I/O 的区别，直接决定事件循环的写法。

## 2) 最常用的系统调用链

- `fork()` / `execve()` / `waitpid()`：启动子进程、回收退出状态。
- `open()` / `read()` / `write()` / `close()`：最基础的文件 I/O。
- `mmap()` / `munmap()`：把文件或匿名内存映射到进程地址空间。
- `sigaction()`：统一、可控地安装信号处理器。

## 3) 容易踩坑的地方

- `read()` 和 `write()` 都可能短读短写。
- 系统调用可能被 `EINTR` 中断，要重试。
- `fork()` 后子进程会继承 fd，必须显式关闭不需要的句柄。
- 非阻塞 fd 配合事件循环时，必须循环读写直到 `EAGAIN`。

## 4) 一组实用的系统调用包装

```cpp
#include <cerrno>
#include <csignal>
#include <fcntl.h>
#include <sys/wait.h>
#include <unistd.h>

inline int setNonBlocking(int fd) {
    int flags = fcntl(fd, F_GETFL, 0);
    if (flags == -1) {
        return -1;
    }
    return fcntl(fd, F_SETFL, flags | O_NONBLOCK);
}

inline void ignoreSigPipe() {
    struct sigaction action {};
    action.sa_handler = SIG_IGN;
    sigemptyset(&action.sa_mask);
    sigaction(SIGPIPE, &action, nullptr);
}

inline ssize_t readFull(int fd, void* buffer, size_t length) {
    size_t total = 0;
    char* data = static_cast<char*>(buffer);
    while (total < length) {
        ssize_t bytes = ::read(fd, data + total, length - total);
        if (bytes > 0) {
            total += static_cast<size_t>(bytes);
            continue;
        }
        if (bytes == 0) {
            break;
        }
        if (errno == EINTR) {
            continue;
        }
        return -1;
    }
    return static_cast<ssize_t>(total);
}

inline ssize_t writeFull(int fd, const void* buffer, size_t length) {
    size_t total = 0;
    const char* data = static_cast<const char*>(buffer);
    while (total < length) {
        ssize_t bytes = ::write(fd, data + total, length - total);
        if (bytes > 0) {
            total += static_cast<size_t>(bytes);
            continue;
        }
        if (bytes == -1 && errno == EINTR) {
            continue;
        }
        return -1;
    }
    return static_cast<ssize_t>(total);
}
```

## 5) 工具链建议

- `strace` 看系统调用序列。
- `lsof` 看 fd 归属。
- `pmap` 看进程内存映射。
- `top` / `htop` 看线程和 CPU 占用。
