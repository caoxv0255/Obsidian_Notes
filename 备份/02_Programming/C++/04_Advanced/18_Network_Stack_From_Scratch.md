---
type: advanced
topic: network_stack_from_scratch
category: advanced
difficulty: advanced
acm_relevant: false
engineering_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, Linux, 项目实战, Network Stack, TCP/IP, 协议栈, 系统编程]
---

# Network Stack 从零实现

> 这不是完整内核协议栈，而是一个最小可运行的 TCP/IP 模型，用来理解分层、状态机和重传。

## 1) 目标

- 支持最小的以太网、ARP、IP 和 TCP 语义。
- 支持连接建立、数据收发和超时重传。
- 支持基础校验和和包解析。
- 支持本地测试或 `TUN/TAP` 测试。

## 2) 模块拆分

- 链路层：帧格式、MAC、ARP。
- 网络层：IP 头、路由、TTL。
- 传输层：TCP 头、序号、确认号、窗口。
- 定时层：重传、超时、状态机。

## 3) 实现顺序

1. 先做数据结构和报文解析。
2. 再做 ARP 和 IP 收发。
3. 接着实现 TCP 三次握手。
4. 再加数据传输和 ACK。
5. 最后补重传和超时管理。

## 4) 接口草图

```cpp
class TcpConnection {
public:
    void onSegment(const std::vector<uint8_t>& segment);
    void send(const std::vector<uint8_t>& payload);
};
```

## 5) 验收标准

- 握手状态迁移正确。
- 丢包后能触发重传。
- 校验和错误时能丢弃报文。
- 本地测试时能解释每一层发生了什么。

## 6) 详细实现

### 6.1 分层结构

最小模型可以按下面的调用关系组织：

- 应用层只负责收发字节流。
- 传输层负责连接状态和可靠传输。
- 网络层负责路由和地址。
- 链路层负责帧封装和局域网发现。

### 6.2 TCP 状态机

可以先支持这些状态：

- `CLOSED`
- `SYN_SENT`
- `SYN_RECEIVED`
- `ESTABLISHED`
- `FIN_WAIT`
- `CLOSE_WAIT`

状态机要显式写出来，否则握手、挥手和重传很容易互相打架。

### 6.3 重传与定时器

```cpp
struct PendingSegment {
    std::vector<uint8_t> data;
    std::chrono::steady_clock::time_point deadline;
    uint32_t retries = 0;
};
```

- 每个未确认分段都要挂一个重传计时器。
- 超时后重发，但重试次数要有限制。
- 收到 ACK 后及时移除 pending 项。

### 6.4 测试接入方式

- 如果不想碰内核，先用纯模拟方式跑状态机。
- 想进一步验证，可以接 `TUN/TAP`。
- 最后再考虑和真实 `socket` / 原始包收发做联调。

## 7) 常见坑

- 只看字节流，不看状态机。
- ACK 号和序号搞混。
- 忘记处理超时重传，链路只要丢一个包就死。
- 校验和或头部长度处理不完整，导致无法和真实协议兼容。

## 8) 测试建议

- 先用固定输入驱动状态机，确认状态迁移。
- 再模拟丢包和乱序，确认重传和 ACK。
- 最后用小包、大包和超时场景验证边界。

## 9) 与现有笔记的对应关系

- [Linux OS 基础：进程、线程、信号与文件 I/O](08_Linux_OS_Fundamentals.md)
- [Linux 网络编程：socket、TCP、epoll](09_Network_Programming_Socket_Epoll.md)
- [Linux 工程闭环与项目实战](11_Linux_Project_Closure.md)

## 11) 最小启动流程

```cpp
int main() {
    NetStack stack;
    stack.openDevice("tun0");
    stack.run();
    return 0;
}
```

启动顺序建议是：

1. 打开虚拟网卡或测试设备。
2. 加载本地地址和路由表。
3. 启动收包和发包循环。
4. 驱动 TCP 状态机和重传计时器。

## 10) 报文队列与定时器设计

### 10.1 发送与接收队列

- 发送队列保存已经发出但未确认的数据包。
- 接收队列保存已经收到但尚未交给上层的数据包。
- `pendingAck` 表保存序号和确认号对应关系。

### 10.2 报文布局

一个最小的 TCP 片段可以包括：

- 源端口、目标端口。
- 序号、确认号。
- 标志位。
- 窗口大小。
- 负载和校验和。

### 10.3 重传定时器

```cpp
void TcpConnection::onTimer() {
    for (auto& segment : pendingSegments_) {
        if (segment.deadline <= now()) {
            resend(segment);
            segment.deadline = now() + retransmitTimeout;
            ++segment.retries;
        }
    }
}
```

这份笔记已经可以直接拆成 `ethernet`、`arp_table`、`ip_router`、`tcp_connection` 和 `retransmission_timer` 五层实现。

## 12) 第一版源码草案

建议先落一个 `src/main.cpp`，把设备打开和协议栈循环串起来：

```cpp
#include "net/net_stack.hpp"

int main() {
    NetStack stack;
    stack.openDevice("tun0");
    stack.run();
    return 0;
}
```

然后再补 `src/l4/tcp_connection.cpp`、`src/l3/ip_router.cpp` 和 `src/device/tun_device.cpp`，先把收发路径跑通，再补重传和状态机。

## 13) 头文件与源码骨架

```cpp
// include/net/net_stack.hpp
class NetStack {
public:
    void openDevice(const std::string& deviceName);
    void run();
};

// src/main.cpp
int main() {
    NetStack stack;
    stack.openDevice("tun0");
    stack.run();
    return 0;
}
```

- 重传超时要逐步退避。
- 重试上限到了就关闭连接。
- 收到 ACK 后要删除对应分段。

### 10.4 调试方式

- 先用纯内存模拟器验证状态机。
- 再接 `TUN/TAP` 测试报文流转。
- 最后再考虑和真实网络栈做联调。

## 11) 里程碑

- M1：报文解析和基本结构。
- M2：ARP / IP 转发。
- M3：TCP 三次握手和挥手。
- M4：数据收发和 ACK。
- M5：超时、重传和 TUN/TAP 测试。

## 12) 建议目录结构

```text
netstack/
    include/
        net/
    src/
        l2/
        l3/
        l4/
        timer/
        device/
        utils/
    tests/
    captures/
    docs/
```

## 13) 核心边界

- `EthernetFrame`：链路层帧封装。
- `ArpTable`：地址解析缓存。
- `IpRouter`：IP 头解析、路由和转发。
- `TcpConnection`：TCP 状态机、ACK 和重传。
- `RetransmissionTimer`：超时检测和重发。

## 14) 最小测试矩阵

- 解析各种报文头。
- 三次握手与四次挥手。
- 丢包后的重传。
- 校验和错误丢弃。
- 乱序包与重复 ACK。
- TUN/TAP 环境下的本地联调。

## 15) 类与函数签名

```cpp
struct EthernetFrame {
    std::array<uint8_t, 6> dstMac;
    std::array<uint8_t, 6> srcMac;
    uint16_t etherType;
};

class ArpTable {
public:
    void update(const std::string& ip, const std::array<uint8_t, 6>& mac);
    std::optional<std::array<uint8_t, 6>> lookup(const std::string& ip) const;
};

class IpRouter {
public:
    bool routePacket(const std::vector<uint8_t>& packet);
};

class TcpConnection {
public:
    void onSegment(const std::vector<uint8_t>& segment);
    void onAck(uint32_t ackNumber);
    void send(const std::vector<uint8_t>& payload);
};
```

## 16) 主流程伪代码

```cpp
void onFrameReceived(const std::vector<uint8_t>& frame) {
    auto ethernet = parseEthernet(frame);
    if (ethernet.etherType == ARP) {
        arpTable.handle(frame);
        return;
    }
    if (ethernet.etherType == IP) {
        auto packet = parseIp(frame);
        if (packet.protocol == TCP) {
            tcpConnection.onSegment(packet.payload);
        }
    }
}
```

协议栈建议按下面顺序收敛：

1. 先做报文解析。
2. 再做路由与地址解析。
3. 再做 TCP 状态机。
4. 再做定时器和重传。
5. 最后做 TUN/TAP 联调。

## 17) 配置项

- `mtu`
- `retransmit_timeout_ms`
- `window_size`
- `local_ip`
- `local_mac`
- `device_name`

## 18) 关键实现片段

```cpp
void TcpConnection::onSegment(const std::vector<uint8_t>& segment) {
    auto header = parseTcpHeader(segment);
    if (!validateChecksum(segment)) {
        return;
    }
    switch (state_) {
    case State::SynSent:
        handleSynAck(header);
        break;
    case State::Established:
        handlePayload(segment);
        break;
    default:
        break;
    }
}

void RetransmissionTimer::tick() {
    for (auto& pending : pendingSegments_) {
        if (pending.deadline <= now()) {
            resend(pending);
            pending.deadline = now() + timeout_;
        }
    }
}
```

## 19) 文件拆分建议

```text
netstack/
  include/net/ethernet.hpp
  include/net/arp_table.hpp
  include/net/ip_router.hpp
  include/net/tcp_connection.hpp
  include/net/retransmission_timer.hpp
  src/l2/ethernet.cpp
  src/l2/arp_table.cpp
  src/l3/ip_router.cpp
  src/l4/tcp_connection.cpp
  src/timer/retransmission_timer.cpp
  src/device/tun_device.cpp
  tests/netstack_test.cpp
```

## 20) 集成测试与验收

- 以太网 / ARP / IP 报文都能解析。
- TCP 三次握手和四次挥手可用。
- 丢包后能触发重传。
- 乱序包不会破坏连接状态。
- 校验和错误会被丢弃。
- TUN/TAP 联调能看到完整的状态迁移。

这份笔记已经可以直接拆成 `ethernet`、`arp_table`、`ip_router`、`tcp_connection` 和 `retransmission_timer` 五层实现。
