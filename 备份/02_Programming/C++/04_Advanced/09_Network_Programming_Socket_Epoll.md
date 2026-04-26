---
type: advanced
topic: network_programming_socket_epoll
category: advanced
difficulty: advanced
acm_relevant: false
engineering_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, Linux, 网络编程, socket, epoll]
---

# Linux 网络编程：socket、TCP、epoll

> 这一页把 socket 生命周期、协议 framing、非阻塞读写和 epoll 的关系串起来。

## 1) socket 生命周期

- `socket()` 创建端点。
- `bind()` 绑定地址与端口。
- `listen()` 进入监听状态。
- `accept()` 接收连接。
- `recv()` / `send()` 处理数据。
- `close()` 释放连接。

## 2) TCP 编程的几个关键选项

- `SO_REUSEADDR`：快速重启服务。
- `TCP_NODELAY`：减少小包延迟。
- `SO_KEEPALIVE`：保活探测。
- 非阻塞 socket：配合 `epoll` 使用。

## 3) framing 一定要自己做

- TCP 是字节流，不保留消息边界。
- 常见协议：长度字段 + payload。
- 读写都可能短操作，必须循环处理。

## 4) epoll 的使用原则

- LT 模式更容易写对，ET 模式更省系统调用。
- ET 模式下，必须把 fd 读到 `EAGAIN`。
- `accept()`、`read()`、`write()` 都要准备好循环。

## 5) 一组可复用的网络辅助函数

```cpp
#include <arpa/inet.h>
#include <cerrno>
#include <cstdint>
#include <cstring>
#include <fcntl.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <string>
#include <sys/socket.h>
#include <unistd.h>

inline int createListeningSocket(std::uint16_t port) {
    int fd = ::socket(AF_INET, SOCK_STREAM, 0);
    if (fd == -1) {
        return -1;
    }

    int reuse = 1;
    ::setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &reuse, sizeof(reuse));

    sockaddr_in address {};
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(port);

    if (::bind(fd, reinterpret_cast<sockaddr*>(&address), sizeof(address)) == -1) {
        ::close(fd);
        return -1;
    }

    if (::listen(fd, SOMAXCONN) == -1) {
        ::close(fd);
        return -1;
    }

    return fd;
}

inline bool readExact(int fd, void* buffer, std::size_t length) {
    std::size_t total = 0;
    char* data = static_cast<char*>(buffer);
    while (total < length) {
        ssize_t bytes = ::recv(fd, data + total, length - total, 0);
        if (bytes > 0) {
            total += static_cast<std::size_t>(bytes);
            continue;
        }
        if (bytes == 0) {
            return false;
        }
        if (errno == EINTR) {
            continue;
        }
        if (errno == EAGAIN || errno == EWOULDBLOCK) {
            continue;
        }
        return false;
    }
    return true;
}

inline bool writeExact(int fd, const void* buffer, std::size_t length) {
    std::size_t total = 0;
    const char* data = static_cast<const char*>(buffer);
    while (total < length) {
        ssize_t bytes = ::send(fd, data + total, length - total, 0);
        if (bytes > 0) {
            total += static_cast<std::size_t>(bytes);
            continue;
        }
        if (bytes == -1 && errno == EINTR) {
            continue;
        }
        if (errno == EAGAIN || errno == EWOULDBLOCK) {
            continue;
        }
        return false;
    }
    return true;
}

inline bool readLengthPrefixedMessage(int fd, std::string& message) {
    std::uint32_t networkLength = 0;
    if (!readExact(fd, &networkLength, sizeof(networkLength))) {
        return false;
    }

    std::uint32_t length = ntohl(networkLength);
    message.resize(length);
    return readExact(fd, message.data(), length);
}
```

## 6) 实战建议

- 把协议拆成“连接管理”和“消息编解码”两层。
- epoll 只负责告诉你“哪个 fd 可读/可写”。
- 协议正确性、粘包拆包、超时和心跳要单独设计。
