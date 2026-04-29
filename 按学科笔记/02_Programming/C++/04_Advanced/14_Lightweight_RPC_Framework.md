---
type: advanced
topic: lightweight_rpc_framework
category: advanced
difficulty: advanced
acm_relevant: false
engineering_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, Linux, 项目实战, RPC, 网络, 分布式, 后端]
---

# 轻量 RPC 框架

> 目标不是一次做成完整中间件，而是先把请求帧、序列化、超时、重试和连接池打通。

## 1) 目标

- 支持客户端发起远程调用。
- 支持请求 ID 和响应匹配。
- 支持超时、重试和失败返回。
- 支持简单的服务注册和接口分发。

## 2) 模块拆分

- 编解码：请求帧、响应帧、序列化、反序列化。
- 传输层：TCP 连接、粘包拆包、心跳、超时。
- 调度层：路由、服务注册、方法分发。
- 客户端层：Stub、连接池、重试策略。

## 3) 实现顺序

1. 先实现定长包头和固定字段。
2. 再实现请求 ID 和基本序列化。
3. 接入客户端调用和服务端分发。
4. 加上超时、失败码和重试。
5. 最后做连接池和压测。

## 4) 接口草图

```cpp
struct RpcHeader {
    uint32_t requestId;
    uint32_t methodId;
    uint32_t payloadSize;
};

class RpcClient;
class RpcServer;
```

## 5) 验收标准

- 能区分网络错误和业务错误。
- 响应能准确回到对应请求。
- 超时和重试不会导致重复写入失控。
- 并发提升后仍能稳定工作。

## 6) 详细实现

### 6.1 一次调用的链路

一次 RPC 调用建议按下面的顺序走：

1. 客户端 Stub 组装参数。
2. 序列化器把参数转成字节流。
3. 传输层打包请求头并发送。
4. 服务端解包，按方法 ID 分发。
5. 业务函数执行后生成响应。
6. 客户端按 requestId 匹配响应。

### 6.2 请求帧设计

```cpp
struct RpcHeader {
    uint32_t requestId;
    uint32_t methodId;
    uint32_t payloadSize;
    uint32_t flags;
};
```

- `requestId` 用于请求和响应配对。
- `methodId` 用于定位服务方法。
- `payloadSize` 用于拆包。
- `flags` 可以保留给压缩、加密或错误码。

### 6.3 客户端与服务端骨架

```cpp
class RpcClient {
public:
    std::string call(uint32_t methodId, const std::string& payload);
};

class RpcServer {
public:
    void onMessage(int fd, const std::string& frame);
    std::string dispatch(uint32_t methodId, const std::string& payload);
};
```

### 6.4 超时与重试规则

- 超时只重试幂等请求。
- 重试次数要有限制。
- 服务端必须能识别重复请求，避免重复写入。
- 出错时日志里要明确写出是连接失败、超时还是业务失败。

## 7) 常见坑

- 没有 requestId，导致并发响应乱序。
- 粘包拆包做得太简化，实际收包后很难复原。
- 把所有失败都当成“超时”，排障会很痛苦。
- 重试策略不区分幂等和非幂等，容易把问题放大。

## 8) 测试建议

- 单机模拟正常调用、超时调用和失败调用。
- 故意打乱响应顺序，确认 requestId 匹配正确。
- 在高并发下统计超时率和成功率。
- 对幂等与非幂等接口分别压测。

## 9) 与现有笔记的对应关系

- [epoll + Reactor 服务器骨架](07_Epoll_Reactor_Server.md)
- [Linux 网络编程：socket、TCP、epoll](09_Network_Programming_Socket_Epoll.md)
- [Linux 并发与性能调优](10_Concurrency_Performance_Tuning.md)
- [Linux 工程闭环与项目实战](11_Linux_Project_Closure.md)

## 11) 最小启动流程

```cpp
int main() {
    RpcServer server;
    server.registerService(1, 1, [](const std::string& payload) {
        return handleEcho(payload);
    });
    server.start("0.0.0.0", 9000);
    return 0;
}
```

启动顺序建议是：

1. 注册服务和方法。
2. 初始化编码器和连接池。
3. 绑定端口。
4. 启动收发循环。
5. 开始超时与心跳管理。

## 10) 接口与编解码设计

### 10.1 服务定义

建议先把 RPC 接口写成最小形式：

```cpp
struct RpcMethod {
    uint32_t serviceId;
    uint32_t methodId;
    std::string name;
};
```

- `serviceId` 用来区分服务。
- `methodId` 用来区分方法。
- `name` 便于调试和日志输出。

### 10.2 编解码器接口

```cpp
class Codec {
public:
    std::string encodeHeader(const RpcHeader& header) const;
    RpcHeader decodeHeader(const std::string& frame) const;
    std::string encodePayload(const std::string& payload) const;
};
```

### 10.3 请求与响应匹配

- 客户端发起请求时分配唯一 `requestId`。
- 服务端原样回传 `requestId`。
- 客户端维护一个 `requestId -> promise` 或 `requestId -> callback` 的映射。

### 10.4 超时和连接池

- 每个请求都要记录 deadline。
- 连接池要区分空闲连接、活跃连接和失效连接。
- 如果服务端主动断开连接，客户端要立刻清理待处理请求。

## 11) 里程碑

- M1：本机函数调用模拟 RPC 接口。
- M2：TCP 请求-响应链路打通。
- M3：requestId 和超时机制生效。
- M4：接入连接池和基础重试。
- M5：压测、错误注入和超时统计完成。

## 12) 建议目录结构

```text
rpc-framework/
    include/
        rpc/
    src/
        client/
        server/
        codec/
        transport/
        registry/
    tests/
    examples/
    scripts/
```

## 13) 核心边界

- `RpcClient`：请求发起、超时、重试、回调匹配。
- `RpcServer`：接收请求、方法分发、响应发送。
- `Codec`：请求帧、响应帧、序列化与反序列化。
- `ConnectionPool`：空闲连接复用和失效处理。
- `PendingCall`：请求 ID、deadline、结果状态。

## 14) 最小测试矩阵

- 单次调用成功返回。
- 响应乱序匹配 requestId。
- 超时后重试一次。
- 服务端断连后的清理。
- 业务错误与网络错误区分。
- 并发 100/1000 次调用稳定性。

## 15) 类与函数签名

```cpp
struct PendingCall {
    uint32_t requestId;
    std::string method;
    std::chrono::steady_clock::time_point deadline;
    std::promise<std::string> promise;
};

class RpcCodec {
public:
    std::string encodeRequest(uint32_t methodId, const std::string& payload, uint32_t requestId) const;
    std::optional<RpcHeader> decodeHeader(const std::string& frame) const;
};

class ServiceRegistry {
public:
    void registerMethod(uint32_t serviceId, uint32_t methodId, const std::function<std::string(const std::string&)>& handler);
};

class RpcClient {
public:
    std::future<std::string> call(uint32_t serviceId, uint32_t methodId, const std::string& payload);
};

class RpcServer {
public:
    void onFrame(int fd, const std::string& frame);
};
```

## 16) 主流程伪代码

```cpp
auto future = client.call(serviceId, methodId, payload);
if (future.wait_for(timeout) == std::future_status::ready) {
    auto result = future.get();
    handleResult(result);
} else {
    retryOrFail();
}
```

服务端主链路可以拆成：

1. 收到字节流。
2. 解码请求头。
3. 查找 serviceId 和 methodId。
4. 执行业务处理函数。
5. 封装响应并发送。

## 17) 配置项

- `connect_timeout_ms`
- `request_timeout_ms`
- `retry_count`
- `max_frame_size`
- `pool_size`
- `heartbeat_interval_ms`

## 18) 关键实现片段

```cpp
std::future<std::string> RpcClient::call(uint32_t serviceId, uint32_t methodId, const std::string& payload) {
    auto requestId = nextRequestId_++;
    PendingCall pending;
    pending.requestId = requestId;
    pending.deadline = std::chrono::steady_clock::now() + requestTimeout_;
    auto future = pending.promise.get_future();
    pendingCalls_.emplace(requestId, std::move(pending));
    sendFrame(codec_.encodeRequest(methodId, payload, requestId));
    return future;
}

void RpcServer::onFrame(int fd, const std::string& frame) {
    auto header = codec_.decodeHeader(frame);
    if (!header) {
        closeConnection(fd);
        return;
    }
    auto response = registry_.dispatch(header->methodId, extractPayload(frame));
    sendResponse(fd, codec_.encodeResponse(*header, response));
}
## 19) 文件拆分建议

```text
rpc-framework/
    include/rpc/rpc_codec.hpp
    include/rpc/rpc_client.hpp
    include/rpc/rpc_server.hpp
    include/rpc/service_registry.hpp
    include/rpc/connection_pool.hpp
    src/codec/rpc_codec.cpp
    src/client/rpc_client.cpp
    src/server/rpc_server.cpp
    src/server/service_registry.cpp
    src/transport/connection_pool.cpp
    src/transport/tcp_transport.cpp
    tests/rpc_framework_test.cpp
```

## 20) 集成测试与验收

- 客户端可成功调用服务端方法。
- requestId 混乱时仍能正确匹配响应。
- 超时请求会触发重试或失败返回。
- 服务端断开连接后，客户端能清理 pending call。
- 并发调用下结果不串包、不丢包。
- 压测时能统计成功率、超时率和重试率。

这份笔记已经可以直接拆成 `codec`、`client`、`server`、`registry` 和 `connection_pool` 五层实现。

## 12) 第一版源码草案

建议先落一个 `src/main.cpp`，把服务注册和启动串起来：

```cpp
#include "rpc/rpc_server.hpp"

int main() {
    RpcServer server;
    server.registerService(1, 1, [](const std::string& payload) {
        return handleEcho(payload);
    });
    server.start("0.0.0.0", 9000);
    return 0;
}
```

然后再补 `src/server/rpc_server.cpp`、`src/client/rpc_client.cpp` 和 `src/codec/rpc_codec.cpp`，先让一次调用闭环，再补连接池和重试。

## 13) 头文件与源码骨架

```cpp
// include/rpc/rpc_server.hpp
class RpcServer {
public:
    void registerService(uint32_t serviceId, uint32_t methodId, std::function<std::string(const std::string&)> handler);
    void start(const std::string& host, uint16_t port);
};

// src/main.cpp
int main() {
    RpcServer server;
    server.registerService(1, 1, [](const std::string& payload) {
        return handleEcho(payload);
    });
    server.start("0.0.0.0", 9000);
    return 0;
}
```
