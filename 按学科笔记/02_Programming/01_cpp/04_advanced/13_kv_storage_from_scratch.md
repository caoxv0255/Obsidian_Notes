---
type: advanced
topic: kv_storage_from_scratch
category: advanced
difficulty: advanced
acm_relevant: false
engineering_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, Linux, 项目实战, 数据库, 存储, Redis, 持久化]
---

# 简化版 KV 存储

> 先做内存型 KV，再补持久化、恢复和过期策略，目标是把“能写”扩展成“能恢复、能解释、能压测”。

## 1) 目标

- 支持 `GET`、`SET`、`DEL`、`EXPIRE`。
- 支持内存存储和持久化恢复。
- 支持最小可用的过期键清理。
- 支持崩溃后重启恢复。

## 2) 模块拆分

- 协议层：文本协议或 `RESP` 子集。
- 存储层：`unordered_map`、版本号、过期时间。
- 持久化：`AOF`、快照、恢复流程。
- 维护层：日志、压测、数据校验。

## 3) 实现顺序

1. 先实现纯内存 `map` 版。
2. 再补命令解析和统一返回格式。
3. 接入追加写日志 `AOF`。
4. 增加快照和重启恢复。
5. 最后补过期键清理和基础压测。

## 4) 接口草图

```cpp
class KvStore {
public:
    bool set(const std::string& key, const std::string& value);
    std::optional<std::string> get(const std::string& key) const;
    bool erase(const std::string& key);
};
```

## 5) 验收标准

- 重启后能恢复历史数据。
- AOF 损坏时能明确报错或跳过尾部坏记录。
- 过期键不会长期占用内存。
- 写入、读取、恢复三个路径都有独立测试。

## 6) 详细实现

### 6.1 数据模型

一个最小的 KV 项可以包含以下字段：

- key
- value
- version
- expireAt

`version` 的作用是避免并发或重放恢复时把旧值覆盖新值，`expireAt` 则用于最小过期策略。

### 6.2 持久化格式

建议把持久化拆成两层：

- `AOF` 记录单条命令，便于增量恢复。
- 快照记录某一时刻的完整状态，便于快速启动。

一个简单的 AOF 记录可以长这样：

```text
SET key value 1700000000
DEL key
EXPIRE key 1700000300
```

### 6.3 恢复流程

1. 启动时先加载快照。
2. 再回放快照之后的 AOF。
3. 回放时跳过格式错误或尾部不完整的记录。
4. 最后做一次过期键清理。

### 6.4 命令处理骨架

```cpp
class KvStore {
public:
    bool set(const std::string& key, const std::string& value);
    std::optional<std::string> get(const std::string& key) const;
    bool erase(const std::string& key);

private:
    struct Entry {
        std::string value;
        uint64_t version = 0;
        std::chrono::system_clock::time_point expireAt;
    };

    std::unordered_map<std::string, Entry> data_;
};
```

## 7) 常见坑

- 只写 AOF 不做截断恢复，启动时容易被半条记录卡死。
- 只写快照不保留增量日志，恢复时间会越来越长。
- 过期键只在查询时清理，内存会慢慢膨胀。
- 没有统一日志格式，排障时无法区分恢复失败和命令错误。

## 8) 测试建议

- 连续写入后强制杀进程，验证恢复结果。
- 构造尾部损坏的 AOF，验证截断行为。
- 写入带过期时间的数据，等待后再查询。
- 对比 `SET` / `GET` / `DEL` 的行为和日志。

## 9) 与现有笔记的对应关系

- [Linux OS 基础：进程、线程、信号与文件 I/O](08_Linux_OS_Fundamentals.md)
- [Linux 网络编程：socket、TCP、epoll](09_Network_Programming_Socket_Epoll.md)
- [Linux 工程闭环与项目实战](11_Linux_Project_Closure.md)

## 11) 最小启动流程

```cpp
int main() {
    KvStore store;
    store.loadSnapshot();
    store.replayWal();

    CommandParser parser;
    while (auto line = readLine()) {
        auto command = parser.parse(*line);
        if (!command) {
            continue;
        }
        auto reply = store.execute(*command);
        writeReply(reply);
    }
    return 0;
}
```

启动顺序建议是：

1. 加载快照。
2. 回放 WAL。
3. 启动命令循环。
4. 周期性重写快照。

## 10) 文件与恢复设计

### 10.1 WAL 记录格式

建议把每条命令编码成可追加的日志记录：

```text
[magic][version][length][command bytes][checksum]
```

- `magic` 用于快速识别文件。
- `version` 方便未来升级格式。
- `length` 用于截断或跳过半条记录。
- `checksum` 用于发现损坏。

### 10.2 快照格式

快照保存的是某一时刻的完整状态，可以包含：

- key 数量。
- 每个 key 的 value。
- 过期时间。
- 最近一次回放到的日志位置。

### 10.3 恢复算法

```cpp
void recover() {
    loadSnapshot();
    for (const auto& record : replayableWalRecords()) {
        apply(record);
    }
    purgeExpiredKeys();
}
```

### 10.4 简单清理策略

- 每次写入后按比例检查是否需要重写快照。
- 当 WAL 超过阈值时，合并快照和增量日志。
- 过期键可以在读路径清理，也可以定时扫描清理。

## 11) 里程碑

- M1：纯内存版本能跑通基本命令。
- M2：WAL 可追加、可回放、可截断。
- M3：快照和恢复能配合工作。
- M4：过期键和清理策略稳定。
- M5：加入压测与恢复边界测试。

## 12) 建议目录结构

```text
kv-store/
    include/
        kv/
    src/
        db/
        wal/
        snapshot/
        expire/
        protocol/
    tests/
    data/
    scripts/
    docs/
```

## 13) 核心边界

- `KvStore`：对外 `set/get/erase/exire` 接口。
- `WalWriter`：追加日志、刷盘、截断恢复。
- `SnapshotManager`：快照生成和加载。
- `ExpireManager`：过期键扫描和清理。
- `CommandParser`：文本命令解析和返回码构造。

## 14) 最小测试矩阵

- `SET/GET/DEL` 基本路径。
- AOF 回放恢复。
- 崩溃后重启恢复。
- 损坏日志截断恢复。
- 过期键清理。
- 大批量写入后的快照切换。

## 15) 类与函数签名

```cpp
struct Command {
    std::string name;
    std::vector<std::string> args;
};

class CommandParser {
public:
    std::optional<Command> parse(const std::string& line) const;
};

class WalWriter {
public:
    bool append(const Command& command);
    bool flush();
};

class SnapshotManager {
public:
    bool saveSnapshot(const KvStore& store);
    bool loadSnapshot(KvStore& store);
};

class KvStore {
public:
    bool set(const std::string& key, const std::string& value);
    std::optional<std::string> get(const std::string& key) const;
    bool erase(const std::string& key);
    bool expire(const std::string& key, uint64_t expireAtMs);
};
```

## 16) 主流程伪代码

```cpp
int main() {
    KvStore store;
    store.loadSnapshot();
    store.replayWal();

    while (auto line = readLine()) {
        auto command = parser.parse(*line);
        if (!command) {
            continue;
        }
        auto reply = store.execute(*command);
        writeReply(reply);
    }
    return 0;
}
```

恢复链路建议按下面顺序实现：

1. 加载快照。
2. 回放 WAL。
3. 清理过期键。
4. 打开命令循环。
5. 每隔一段时间重写快照。

## 17) 配置项

- `wal_path`
- `snapshot_path`
- `flush_interval_ms`
- `snapshot_threshold`
- `expire_scan_interval_ms`
- `max_key_count`

## 18) 关键实现片段

```cpp
bool WalWriter::append(const Command& command) {
    auto record = encodeRecord(command);
    if (!file_.write(record.data(), record.size())) {
        return false;
    }
    return true;
}

std::optional<std::string> KvStore::get(const std::string& key) const {
    auto it = data_.find(key);
    if (it == data_.end()) {
        return std::nullopt;
    }
    if (isExpired(it->second)) {
        return std::nullopt;
    }
    return it->second.value;
}
## 19) 文件拆分建议

```text
kv-store/
    include/kv/command_parser.hpp
    include/kv/kv_store.hpp
    include/kv/wal_writer.hpp
    include/kv/snapshot_manager.hpp
    include/kv/expire_manager.hpp
    src/protocol/command_parser.cpp
    src/db/kv_store.cpp
    src/wal/wal_writer.cpp
    src/snapshot/snapshot_manager.cpp
    src/expire/expire_manager.cpp
    src/util/checksum.cpp
    tests/kv_store_test.cpp
```

## 20) 集成测试与验收

- `SET/GET/DEL/EXPIRE` 全链路可跑通。
- 写入后强杀进程，重启可恢复数据。
- 制造坏日志尾部，恢复时可正确截断。
- 快照生成后，WAL 重放结果一致。
- 过期键在读路径和定时清理路径都能消失。
- 大量写入后重启时间不会失控增长。

这份笔记已经可以直接拆成 `command_parser`、`wal_writer`、`snapshot_manager` 和 `kv_store` 四层实现。

## 12) 第一版源码草案

建议先落一个 `src/main.cpp`，把恢复和命令循环串起来：

```cpp
#include "kv/kv_store.hpp"

int main() {
    KvStore store;
    store.loadSnapshot();
    store.replayWal();
    return runKvCli(store);
}
```

然后再补 `src/db/kv_store.cpp`、`src/wal/wal_writer.cpp` 和 `src/snapshot/snapshot_manager.cpp`，先打通 `SET/GET/DEL`，再补 `EXPIRE` 和恢复。

## 13) 头文件与源码骨架

```cpp
// include/kv/kv_store.hpp
class KvStore {
public:
    bool set(const std::string& key, const std::string& value);
    std::optional<std::string> get(const std::string& key) const;
    bool erase(const std::string& key);
    bool expire(const std::string& key, uint64_t expireAtMs);
};

// src/main.cpp
int main() {
    KvStore store;
    store.loadSnapshot();
    store.replayWal();
    return runKvCli(store);
}
```
