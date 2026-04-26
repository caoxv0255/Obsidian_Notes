---
type: advanced
topic: git_from_scratch
category: advanced
difficulty: advanced
acm_relevant: false
engineering_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, Linux, 项目实战, Git, 文件系统, 版本控制]
---

# Git 从零实现

> 重点不是完整兼容 Git，而是理解对象存储、提交图、引用和工作区之间的关系。

## 1) 目标

- 支持仓库初始化。
- 支持对象写入和哈希校验。
- 支持提交、分支和日志。
- 支持检出和工作区同步。

## 2) 模块拆分

- 对象层：blob、tree、commit。
- 引用层：`HEAD`、branch、tag。
- 工作区层：文件扫描、差异、暂存区。
- 命令层：`init`、`add`、`commit`、`log`、`checkout`。

## 3) 实现顺序

1. 先做仓库初始化和对象存储。
2. 再做 blob 和 commit。
3. 接着实现分支和日志。
4. 再补 checkout 和状态检查。
5. 最后加入 diff 和基础错误处理。

## 4) 接口草图

```cpp
class Repository {
public:
    void init(const std::string& path);
    std::string writeBlob(const std::string& content);
    std::string commit(const std::string& message);
};
```

## 5) 验收标准

- 对象哈希可重复计算和校验。
- 分支切换后工作区能恢复到预期状态。
- 提交历史能正确形成有向无环图。
- 基础命令出错时有明确提示。

## 6) 详细实现

### 6.1 仓库内部结构

可以先做一个最小版本的目录布局：

```text
.mini-git/
    objects/
    refs/
    HEAD
    index
```

- `objects` 存 blob、tree、commit。
- `refs` 存分支引用。
- `HEAD` 指向当前分支。
- `index` 记录暂存区。

### 6.2 对象模型

```cpp
struct BlobObject {
        std::string hash;
        std::string content;
};

struct CommitObject {
        std::string treeHash;
        std::string parentHash;
        std::string message;
};
```

对象哈希可以先用“内容 + 类型 + 长度”的字符串做输入，后续再决定是否接入压缩和更完整的对象编码。

### 6.3 核心命令流程

- `add`：扫描工作区，把变更写入 index。
- `commit`：把 index 里的内容打成 tree，再生成 commit。
- `log`：沿着 parent 链回溯。
- `checkout`：按目标 commit 恢复工作区。

### 6.4 状态检查与 diff

- `status` 先比较工作区和 index。
- `diff` 先只做文本行级比较。
- 文件删除、重命名和大文件场景可以后补。

## 7) 常见坑

- 没有统一编码对象格式，后期很难恢复。
- 直接拿文件路径当对象名，无法模拟真正的 Git 结构。
- checkout 覆盖工作区时没有备份未提交内容。
- 暂存区和工作区比较逻辑混在一起，容易出错。

## 8) 测试建议

- 初始化仓库后检查对象目录和引用是否创建。
- 多次 commit 后检查 parent 链。
- 切换分支再回到原分支，验证文件内容变化。
- 删除文件、修改文件、未跟踪文件分别测 status。

## 9) 与现有笔记的对应关系

- [Linux OS 基础：进程、线程、信号与文件 I/O](08_Linux_OS_Fundamentals.md)
- [Linux 工程闭环与项目实战](11_Linux_Project_Closure.md)

## 11) 最小启动流程

```cpp
int main(int argc, char** argv) {
    Repository repo;
    repo.init(std::filesystem::current_path().string());
    return runGitCli(repo, argc, argv);
}
```

启动顺序建议是：

1. 确认当前工作目录。
2. 加载仓库对象目录和引用。
3. 进入命令分发。
4. 处理 `init`、`add`、`commit`、`log`、`checkout`。

## 10) 对象写入与引用更新

### 10.1 Loose object

最小实现可以先采用 loose object：

```text
.mini-git/objects/ab/cdef...
```

- 通过哈希前两位做目录。
- 剩余哈希做文件名。
- 文件内容可以是压缩前的对象体，后面再升级格式。

### 10.2 暂存区模型

暂存区可以保存：

- 文件路径。
- 文件内容哈希。
- 文件模式。
- 最后修改时间。

### 10.3 提交更新流程

```cpp
std::string Repository::commit(const std::string& message) {
    auto treeHash = buildTreeFromIndex();
    auto parentHash = readHeadCommit();
    auto commitHash = writeCommit(treeHash, parentHash, message);
    updateRef("HEAD", commitHash);
    return commitHash;
}
```

### 10.4 diff 与状态

- `diff` 先支持文本比较。
- `status` 要分别显示已暂存、未暂存和未跟踪文件。
- `checkout` 需要明确是否覆盖工作区。

## 11) 里程碑

- M1：init/add/commit 跑通。
- M2：log 和 checkout 可用。
- M3：status 和 diff 可用。
- M4：分支与 HEAD 切换可用。
- M5：补错误提示和工作区保护。

## 12) 建议目录结构

```text
mini-git/
    include/
        git/
    src/
        objects/
        refs/
        index/
        worktree/
        commands/
    tests/
    repo/
    docs/
```

## 13) 核心边界

- `ObjectStore`：写入/读取 blob、tree、commit。
- `Index`：暂存区管理。
- `RefStore`：`HEAD` 和分支引用。
- `Worktree`：工作区扫描和恢复。
- `CommandDispatcher`：命令路由到实现。

## 14) 最小测试矩阵

- `init` 后目录结构正确。
- `add/commit/log` 主链路。
- `checkout` 后工作区恢复。
- `status` 区分未跟踪和已修改。
- `diff` 输出稳定。
- 分支切换与 HEAD 更新。

## 15) 类与函数签名

```cpp
class ObjectStore {
public:
    std::string writeBlob(const std::string& content);
    std::string writeTree(const std::vector<std::string>& entries);
    std::string writeCommit(const std::string& treeHash, const std::string& parentHash, const std::string& message);
};

class Index {
public:
    void addFile(const std::string& path);
    std::vector<std::string> stagedFiles() const;
};

class RefStore {
public:
    std::string head() const;
    void updateHead(const std::string& commitHash);
};

class Repository {
public:
    void init(const std::string& path);
    std::string commit(const std::string& message);
    void checkout(const std::string& refName);
};
```

## 16) 主流程伪代码

```cpp
void Repository::commit(const std::string& message) {
    auto entries = index.stagedFiles();
    auto treeHash = objectStore.writeTree(entries);
    auto parentHash = refStore.head();
    auto commitHash = objectStore.writeCommit(treeHash, parentHash, message);
    refStore.updateHead(commitHash);
    worktree.applyCommit(commitHash);
}
```

流程建议按下面拆：

1. 扫描暂存区。
2. 生成 tree 对象。
3. 生成 commit 对象。
4. 更新 HEAD 和 branch。
5. 必要时同步工作区。

## 17) 配置项

- `repo_path`
- `objects_dir`
- `refs_dir`
- `index_path`
- `default_branch`

## 18) 关键实现片段

```cpp
std::string ObjectStore::writeBlob(const std::string& content) {
    auto hash = hashObject("blob", content);
    writeLooseObject(hash, content);
    return hash;
}

void Repository::checkout(const std::string& refName) {
    auto commitHash = refStore.resolve(refName);
    auto tree = objectStore.readTree(commitHash);
    worktree.restore(tree);
    refStore.setHead(refName);
}
## 19) 文件拆分建议

```text
mini-git/
    include/git/object_store.hpp
    include/git/index.hpp
    include/git/ref_store.hpp
    include/git/worktree.hpp
    include/git/repository.hpp
    src/objects/object_store.cpp
    src/index/index.cpp
    src/refs/ref_store.cpp
    src/worktree/worktree.cpp
    src/repository/repository.cpp
    src/commands/command_dispatcher.cpp
    tests/git_repository_test.cpp
```

## 20) 集成测试与验收

- `init` 后仓库目录完整。
- `add` 后暂存区有变化。
- `commit` 后 HEAD 正确移动。
- `log` 能沿 parent 链回溯。
- `checkout` 能恢复文件内容。
- `status` 与 `diff` 对修改、删除、未跟踪文件区分正确。

这份笔记已经可以直接拆成 `object_store`、`index`、`ref_store`、`worktree` 和 `repository` 五层实现。

## 12) 第一版源码草案

建议先落一个 `src/main.cpp`，把仓库初始化和命令分发串起来：

```cpp
#include "git/repository.hpp"

int main(int argc, char** argv) {
    Repository repo;
    repo.init(std::filesystem::current_path().string());
    return runGitCli(repo, argc, argv);
}
```

然后再补 `src/repository/repository.cpp`、`src/objects/object_store.cpp` 和 `src/refs/ref_store.cpp`，先让 `init`、`add`、`commit` 跑通。

## 13) 头文件与源码骨架

```cpp
// include/git/repository.hpp
class Repository {
public:
    void init(const std::string& path);
    std::string commit(const std::string& message);
    void checkout(const std::string& refName);
};

// src/main.cpp
int main(int argc, char** argv) {
    Repository repo;
    repo.init(std::filesystem::current_path().string());
    return runGitCli(repo, argc, argv);
}
```
