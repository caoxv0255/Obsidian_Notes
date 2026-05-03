---
type: advanced
topic: http_static_file_server
category: advanced
difficulty: advanced
acm_relevant: false
engineering_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, Linux, 项目实战, WebServer, epoll, HTTP, 后端]
---

# HTTP 静态文件服务器

> 从 `epoll` 服务器骨架出发，把连接管理、HTTP 解析、静态资源映射、日志和压测补成一个可交付项目。

## 1) 目标

- 支持 `GET` 和 `HEAD`。
- 支持 `keep-alive` 和连接复用。
- 支持静态文件、目录页、`404`、`403`、`500`。
- 支持基础日志、超时回收和简单压测。

## 2) 模块拆分

- 网络层：`accept`、`epoll`、非阻塞读写、连接生命周期。
- 协议层：请求行、请求头、响应行、状态码、`Content-Length`。
- 资源层：文件路径映射、MIME 类型、`sendfile` 或 `mmap`。
- 运维层：配置、日志、统计、压测脚本。

## 3) 实现顺序

1. 先写阻塞版单连接服务器。
2. 再改成 `epoll` 事件循环。
3. 实现请求解析和响应构造。
4. 接入静态文件读取和错误页。
5. 加入 `keep-alive`、超时和连接复用。
6. 最后补线程池、统计和压测。

## 4) 接口草图

```cpp
struct HttpRequest {
    std::string method;
    std::string path;
    std::unordered_map<std::string, std::string> headers;
};

struct HttpResponse {
    int statusCode;
    std::string body;
    std::unordered_map<std::string, std::string> headers;
};
```

## 5) 验收标准

- 多连接下不会频繁泄漏 `fd`。
- 错误请求能返回正确状态码。
- 同一连接可连续处理多个请求。
- 压测时能清楚看到 QPS、延迟和错误率。

## 6) 详细实现

### 6.1 连接状态机

建议把每个连接拆成以下状态：

- `ReadingRequestLine`
- `ReadingHeaders`
- `ReadingBody`
- `WritingResponse`
- `Closed`

这样做的好处是，`epoll` 只负责“什么时候可读/可写”，业务逻辑只负责“当前状态下该做什么”。

### 6.2 请求处理主链路

```cpp
void HttpConnection::onReadable() {
    while (true) {
        ssize_t n = ::read(fd_, buffer_ + used_, sizeof(buffer_) - used_);
        if (n > 0) {
            used_ += static_cast<size_t>(n);
            if (tryParseRequest()) {
                buildResponse();
                switchToWritable();
                return;
            }
            continue;
        }
        if (n == 0) {
            closeConnection();
            return;
        }
        if (errno == EAGAIN || errno == EWOULDBLOCK) {
            return;
        }
        closeConnection();
        return;
    }
}
```

### 6.3 静态资源映射

- URL 只允许映射到固定根目录下的文件。
- 路径需要做规范化，禁止 `..` 回退。
- 文件扩展名要映射到 MIME 类型。
- `GET` 返回正文，`HEAD` 只返回头部。

### 6.4 发送路径选择

- 文件较大时优先考虑 `sendfile`。
- 需要修改响应头或拼接错误页时可以用 `mmap`。
- 如果只想做最小实现，普通 `read` + `write` 也足够，但吞吐会差一些。

## 7) 常见坑

- 忘记处理半包和粘包。
- 在边沿触发模式下没有一次性读空缓冲区。
- 头部解析没有限制长度，导致被大包拖死。
- 直接拼接路径，留下目录穿越风险。
- 长连接下没有清理超时连接。

## 8) 测试建议

- `curl -I` 检查 `HEAD`。
- `curl` 连续请求同一连接，确认 `keep-alive`。
- `ab` 或 `wrk` 做并发压测。
- 手工构造错误请求，确认 `400`、`403`、`404`、`500` 的返回。

## 9) 与现有笔记的对应关系

- [epoll + Reactor 服务器骨架](07_Epoll_Reactor_Server.md)
- [Linux 网络编程：socket、TCP、epoll](09_Network_Programming_Socket_Epoll.md)
- [Linux 并发与性能调优](10_Concurrency_Performance_Tuning.md)
- [Linux 工程闭环与项目实战](11_Linux_Project_Closure.md)

## 10) 最小启动流程

```cpp
int main() {
    ServerConfig config = loadServerConfig("config/server.conf");
    HttpServer server(config);
    server.run();
    return 0;
}
```

启动顺序建议是：

1. 读取配置。
2. 初始化日志。
3. 创建监听 socket。
4. 注册 `epoll`。
5. 进入事件循环。

## 11) 代码结构建议

- `HttpServer`：管理监听 socket、事件循环、连接表、定时器。
- `HttpConnection`：保存读写缓冲、解析状态、响应状态。
- `HttpParser`：只负责把字节流变成请求对象。
- `FileMapper`：只负责路径规范化、文件打开和 MIME 映射。

### 10.1 一次请求的完整链路

1. `epoll` 通知可读。
2. 连接对象读取到缓冲区。
3. 解析器把缓冲区拆成请求。
4. 路由层根据路径决定返回静态文件或错误页。
5. 响应对象写入发送缓冲。
6. `epoll` 通知可写后完成发送。
7. 如果 `keep-alive` 打开，则回到读状态，否则关闭连接。

### 10.2 最小伪代码

```cpp
class HttpServer {
public:
    void run();

private:
    void acceptNewConnection();
    void onReadable(int fd);
    void onWritable(int fd);
};
```

## 11) 里程碑

- M1：只返回固定 `200 OK`。
- M2：支持单个静态文件 `GET`。
- M3：支持 `HEAD`、`404`、`403`、`keep-alive`。
- M4：接入超时回收和基础压测。
- M5：补日志、统计和更严格的路径安全检查。

## 12) 建议目录结构

```text
http-server/
    include/
        http/
    src/
        server/
        http/
        net/
        util/
    tests/
    configs/
    scripts/
    docs/
```

## 13) 核心边界

- `HttpServer`：监听 socket、事件循环、连接分发。
- `HttpConnection`：单连接读写、状态机、缓冲区。
- `HttpParser`：请求行、请求头、请求体解析。
- `ResponseBuilder`：状态码、响应头、正文拼装。
- `MimeTable`：扩展名到 MIME 类型映射。

## 14) 最小测试矩阵

- 单文件 `GET`。
- `HEAD` 请求。
- `404`、`403`、`500` 返回。
- 长连接连续两次请求。
- 非法路径和目录穿越拦截。
- 并发压测下的连接回收。

## 15) 类与函数签名

```cpp
class Buffer {
public:
    void append(const char* data, size_t size);
    const char* data() const;
    size_t readableBytes() const;
    void retrieve(size_t size);
};

class HttpParser {
public:
    bool parseRequest(Buffer& input, HttpRequest& request);
};

class HttpConnection {
public:
    void onReadable();
    void onWritable();
    void closeConnection();
};

class HttpServer {
public:
    explicit HttpServer(const ServerConfig& config);
    void run();
};
```

## 16) 主流程伪代码

```cpp
int main() {
    ServerConfig config = loadServerConfig("config/server.conf");
    HttpServer server(config);
    server.run();
    return 0;
}
```

运行时主循环可以拆成下面几步：

1. 读取配置。
2. 创建监听 socket。
3. 初始化 `epoll` 和连接表。
4. 进入事件循环。
5. 根据可读可写事件驱动连接状态机。
6. 定时清理空闲连接。

## 17) 配置项

- `listen_host`
- `listen_port`
- `doc_root`
- `max_connections`
- `idle_timeout_ms`
- `enable_keep_alive`
- `log_path`

## 18) 关键实现片段

```cpp
bool HttpParser::parseRequest(Buffer& input, HttpRequest& request) {
    auto lineEnd = findLineEnd(input);
    if (!lineEnd) {
        return false;
    }

    request = parseRequestLine(input, *lineEnd);
    parseHeaders(input, request);
    return true;
}

void HttpConnection::onReadable() {
    if (!readIntoBuffer()) {
        closeConnection();
        return;
    }
    if (!parser_.parseRequest(inputBuffer_, request_)) {
        return;
    }
    response_ = buildResponse(request_);
}
## 19) 文件拆分建议

```text
http-server/
    include/http/buffer.hpp
    include/http/http_parser.hpp
    include/http/http_connection.hpp
    include/http/http_server.hpp
    src/http/buffer.cpp
    src/http/http_parser.cpp
    src/http/http_connection.cpp
    src/http/http_server.cpp
    src/net/socket_utils.cpp
    src/net/epoll_utils.cpp
    src/util/file_mapper.cpp
    src/util/logger.cpp
    tests/http_server_test.cpp
```

## 20) 集成测试与验收

- 启动后可通过 `curl` 请求静态资源。
- 同一连接连续发送两个请求，响应顺序正确。
- 故意请求不存在的文件，返回 `404`。
- 访问目录外路径，返回 `403` 或直接拒绝。
- 压测时连接数上升后没有明显 `fd` 泄漏。
- 关闭客户端后服务端能及时回收连接状态。

这份笔记已经可以直接拆成 `buffer`、`parser`、`connection` 和 `server` 四层实现。

## 12) 第一版源码草案

建议先落一个 `src/main.cpp`，把配置、日志和服务器启动串起来：

```cpp
#include "http/http_server.hpp"

int main() {
    auto config = loadServerConfig("config/server.conf");
    HttpServer server(config);
    server.run();
    return 0;
}
```

然后再补 `src/http/http_server.cpp`、`src/http/http_connection.cpp` 和 `src/http/http_parser.cpp`，按“监听 -> 读写 -> 解析 -> 响应”的顺序填充。

## 13) 头文件与源码骨架

```cpp
// include/http/http_server.hpp
class HttpServer {
public:
    explicit HttpServer(const ServerConfig& config);
    void run();

private:
    void acceptNewConnection();
    void onReadable(int fd);
    void onWritable(int fd);
};

// src/main.cpp
int main() {
    auto config = loadServerConfig("config/server.conf");
    HttpServer server(config);
    server.run();
    return 0;
}
```
