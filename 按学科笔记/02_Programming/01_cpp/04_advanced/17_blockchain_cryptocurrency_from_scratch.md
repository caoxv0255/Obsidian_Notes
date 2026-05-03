---
type: advanced
topic: blockchain_cryptocurrency_from_scratch
category: advanced
difficulty: advanced
acm_relevant: false
engineering_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, Linux, 项目实战, Blockchain, Cryptocurrency, 哈希, 分布式]
---

# 区块链 / 加密货币从零实现

> 先做最小链、最小共识和最小交易模型，重点理解哈希链、验证规则和数据不可篡改。

## 1) 目标

- 支持区块、交易和链验证。
- 支持工作量证明或最小难度挖矿。
- 支持链的持久化和重放。
- 支持基础的双花和篡改检测。

## 2) 模块拆分

- 数据层：区块头、交易、交易池。
- 共识层：哈希、难度、挖矿、验证。
- 存储层：区块文件、索引、恢复。
- 网络层：节点同步、广播、冲突处理。

## 3) 实现顺序

1. 先做单链和区块哈希。
2. 再做交易模型和链验证。
3. 然后补工作量证明。
4. 再做本地持久化和重放。
5. 最后考虑最小网络同步。

## 4) 接口草图

```cpp
struct Block {
    std::string prevHash;
    std::vector<std::string> transactions;
    uint64_t nonce;
};
```

## 5) 验收标准

- 改动历史数据后校验会失败。
- 难度变化后挖矿结果可复现。
- 节点重启后可恢复本地链。
- 链分叉时能说明采用哪条分支。

## 6) 详细实现

### 6.1 区块和交易模型

最小版本里，一个区块至少要包含：

- `prevHash`
- `height`
- `timestamp`
- `nonce`
- `transactions`

交易模型可以先简化成字符串列表，等链结构稳定后再补签名和余额校验。

### 6.2 挖矿和验证

```cpp
std::string mineBlock(Block block, uint32_t difficulty) {
    while (true) {
        auto hash = hashBlock(block);
        if (hash.starts_with(std::string(difficulty, '0'))) {
            return hash;
        }
        ++block.nonce;
    }
}
```

- `difficulty` 越高，找到合法哈希越慢。
- 验证时不需要重新“猜”，只需要检查当前区块和前驱区块是否合法。

### 6.3 链选择与分叉

- 最简单的规则是“最长链优先”。
- 如果后续想更接近真实系统，可以再引入“累计工作量”优先。
- 分叉处理一定要能回滚和重放。

### 6.4 持久化与同步

- 先把区块写到本地文件。
- 再做重启重放。
- 最后再考虑节点同步和广播。

## 7) 常见坑

- 只验证哈希，不验证前驱链接。
- 挖矿循环没有退出条件，导致卡死。
- 没有考虑重启后的区块重复导入。
- 交易模型太早复杂化，导致链主干还没跑通就被细节拖住。

## 8) 测试建议

- 修改历史区块内容，确认校验失败。
- 修改 `nonce`，确认哈希变化。
- 人为制造分叉，验证链选择规则。
- 重启后重新加载链，确认状态一致。

## 9) 与现有笔记的对应关系

- [Linux 网络编程：socket、TCP、epoll](09_Network_Programming_Socket_Epoll.md)
- [Linux 工程闭环与项目实战](11_Linux_Project_Closure.md)

## 11) 最小启动流程

```cpp
int main() {
    Blockchain chain;
    chain.loadGenesis("data/genesis.json");
    Miner miner(chain);
    miner.run();
    return 0;
}
```

启动顺序建议是：

1. 加载创世块。
2. 恢复本地链状态。
3. 初始化交易池。
4. 启动挖矿或同步循环。

## 10) 链验证与交易处理

### 10.1 最小交易模型

最小版本可以先用账户模型：

```cpp
struct Transaction {
    std::string from;
    std::string to;
    uint64_t amount;
    uint64_t nonce;
};
```

如果不想一开始就引入签名，也可以先把 `signature` 留成可选字段，重点先跑通链和验证。

### 10.2 验证流程

1. 检查区块头格式。
2. 检查前驱哈希是否匹配。
3. 检查交易列表是否合法。
4. 检查 PoW 是否达标。
5. 检查本地区块高度和重放顺序。

### 10.3 挖矿与出块

- 挖矿本质上是不断调整 `nonce`。
- 生成新区块后先本地验证，再广播。
- 节点收到新区块后先做链验证，再决定是否接入主链。

### 10.4 状态保存

- 只保留当前主链和少量分叉候选。
- 重启时先加载高度，再回放链上的交易。
- 如果后续要做钱包，可以再补账户余额索引。

## 11) 里程碑

- M1：单链验证和区块哈希。
- M2：PoW 和挖矿。
- M3：本地持久化和重启恢复。
- M4：分叉处理和链选择。
- M5：节点同步和最小广播。

## 12) 建议目录结构

```text
blockchain/
    include/
        chain/
    src/
        chain/
        mining/
        mempool/
        storage/
        network/
    tests/
    data/
    docs/
```

## 13) 核心边界

- `Block`：区块头、交易列表、nonce。
- `Transaction`：交易输入输出或简化账户转账。
- `Blockchain`：链管理、验证和分叉选择。
- `Miner`：PoW 计算和出块。
- `Node`：同步、广播和重放。

## 14) 最小测试矩阵

- 区块哈希和前驱校验。
- PoW 挖矿成功。
- 篡改历史后验证失败。
- 重启后恢复主链。
- 人为分叉后的链选择。
- 重复交易和空交易处理。

## 15) 类与函数签名

```cpp
struct Transaction {
    std::string from;
    std::string to;
    uint64_t amount;
    uint64_t nonce;
};

struct BlockHeader {
    std::string prevHash;
    uint64_t height;
    uint64_t timestamp;
    uint64_t nonce;
};

class Blockchain {
public:
    bool appendBlock(const Block& block);
    bool validateBlock(const Block& block) const;
};

class Miner {
public:
    Block mineNextBlock(const std::vector<Transaction>& txs);
};

class Node {
public:
    void receiveBlock(const Block& block);
    void broadcastBlock(const Block& block);
};
```

## 16) 主流程伪代码

```cpp
Block mineNextBlock(const std::vector<Transaction>& txs) {
    Block block;
    block.header.prevHash = chain.tipHash();
    block.transactions = txs;
    while (!chain.validatePow(block)) {
        ++block.header.nonce;
    }
    chain.appendBlock(block);
    node.broadcastBlock(block);
    return block;
}
```

工作流可以拆成：

1. 收集交易。
2. 构造新区块。
3. 进行 PoW。
4. 本地验证。
5. 广播给其他节点。
6. 接收方做链验证和分叉处理。

## 17) 配置项

- `genesis_path`
- `difficulty`
- `block_interval_ms`
- `peer_list`
- `storage_path`
- `max_pending_tx`

## 18) 关键实现片段

```cpp
bool Blockchain::validateBlock(const Block& block) const {
    if (block.header.prevHash != tipHash()) {
        return false;
    }
    if (!validateTransactions(block.transactions)) {
        return false;
    }
    return validatePow(block);
}

Block Miner::mineNextBlock(const std::vector<Transaction>& txs) {
    Block block;
    block.transactions = txs;
    block.header.prevHash = chain_.tipHash();
    while (!chain_.validatePow(block)) {
        ++block.header.nonce;
    }
    return block;
}
## 19) 文件拆分建议

```text
blockchain/
    include/chain/block.hpp
    include/chain/blockchain.hpp
    include/chain/transaction.hpp
    include/chain/miner.hpp
    include/chain/node.hpp
    src/chain/block.cpp
    src/chain/blockchain.cpp
    src/chain/transaction.cpp
    src/mining/miner.cpp
    src/storage/block_storage.cpp
    src/network/node.cpp
    tests/blockchain_test.cpp
```

## 20) 集成测试与验收

- 创世块可生成并校验。
- PoW 挖矿结果满足难度要求。
- 篡改历史后链验证失败。
- 重启后本地链可恢复。
- 人为制造分叉后能按规则选择主链。
- 重复交易或空交易会被拒绝或忽略。

这份笔记已经可以直接拆成 `block`、`blockchain`、`miner`、`storage` 和 `node` 五层实现。

## 12) 第一版源码草案

建议先落一个 `src/main.cpp`，把创世块加载和挖矿循环串起来：

```cpp
#include "chain/blockchain.hpp"

int main() {
    Blockchain chain;
    chain.loadGenesis("data/genesis.json");
    Miner miner(chain);
    miner.run();
    return 0;
}
```

然后再补 `src/chain/blockchain.cpp`、`src/mining/miner.cpp` 和 `src/network/node.cpp`，先跑通区块验证，再补分叉和同步。

## 13) 头文件与源码骨架

```cpp
// include/chain/blockchain.hpp
class Blockchain {
public:
    bool appendBlock(const Block& block);
    bool validateBlock(const Block& block) const;
    std::string tipHash() const;
};

// src/main.cpp
int main() {
    Blockchain chain;
    chain.loadGenesis("data/genesis.json");
    Miner miner(chain);
    miner.run();
    return 0;
}
```
