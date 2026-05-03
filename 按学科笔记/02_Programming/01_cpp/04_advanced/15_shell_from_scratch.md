---
type: advanced
topic: shell_from_scratch
category: advanced
difficulty: advanced
acm_relevant: false
engineering_relevant: true
created: 2026-04-24
status: draft
tags: [编程/C++, Linux, 项目实战, Shell, 进程, 信号, 系统编程]
---

# Shell 从零实现

> 用 `fork`、`exec`、`pipe`、`dup2` 和 `waitpid` 做出一个最小交互式 Shell，重点是命令解析、管道、重定向、后台任务和信号处理。

## 1) 目标

- 支持普通命令执行。
- 支持管道和重定向。
- 支持内建命令 `cd`、`exit`、`export`。
- 支持后台任务和基础信号处理。

## 2) 模块拆分

- 词法层：命令切分、引号、转义。
- 语法层：管道、重定向、后台执行。
- 执行层：`fork`、`execvp`、`dup2`、`waitpid`。
- 交互层：提示符、历史记录、环境变量。

## 3) 语法与 AST 设计

可以先支持下面的最小语法：

```text
line        := pipeline [ '&' ]
pipeline    := command { '|' command }
command     := simple_command { redirection }
simple_cmd  := word { word }
redirection := '<' file | '>' file | '>>' file
```

建议的 AST 节点：

- `Token`：词法单元。
- `CommandNode`：单个命令和参数。
- `PipelineNode`：多个命令的管道。
- `RedirectNode`：输入输出重定向。
- `JobNode`：后台任务标记。

## 4) 执行模型

Shell 的执行链路可以按这个顺序实现：

1. 读取一行输入。
2. 词法分析得到 tokens。
3. 语法分析构建 AST。
4. 先检查内建命令。
5. 再执行外部命令或管道。
6. 最后回收后台子进程。

```cpp
std::vector<Token> Tokenizer::tokenize(const std::string& line) const {
    std::vector<Token> tokens;
    std::string current;
    bool quoted = false;

    for (char ch : line) {
        if (ch == '"') {
            quoted = !quoted;
            continue;
        }
        if (!quoted && std::isspace(static_cast<unsigned char>(ch))) {
            if (!current.empty()) {
                tokens.push_back({current, false});
                current.clear();
            }
            continue;
        }
        current.push_back(ch);
    }

    if (!current.empty()) {
        tokens.push_back({current, quoted});
    }
    return tokens;
}

int Executor::execute(const PipelineNode& pipeline) {
    if (builtinRegistry_.handle(pipeline.commands.front())) {
        return 0;
    }
    return runPipeline(pipeline);
}
```

## 5) 关键类与函数签名

```cpp
struct Token {
    std::string text;
    bool quoted = false;
};

class Tokenizer {
public:
    std::vector<Token> tokenize(const std::string& line) const;
};

class Parser {
public:
    std::optional<PipelineNode> parse(const std::vector<Token>& tokens) const;
};

class Executor {
public:
    int execute(const PipelineNode& pipeline);
};

class BuiltinRegistry {
public:
    bool handle(const CommandNode& command);
};
```

## 6) 常见坑

- 父进程忘记关闭管道端，导致读端一直不 EOF。
- 子进程没有恢复默认信号处理，`Ctrl-C` 行为异常。
- 重定向和管道的优先级处理不一致。
- 后台进程没有回收，形成僵尸。

## 7) 测试建议

- `echo hello` 测单命令执行。
- `echo hello | tr a-z A-Z` 测管道。
- `cat < in.txt > out.txt` 测重定向。
- `cd`、`export`、`exit` 测内建命令。
- `sleep 1 &` 测后台任务和回收。
- `Ctrl-C` 测前台进程组处理。

## 8) 文件拆分建议

```text
shell/
  include/shell/tokenizer.hpp
  include/shell/parser.hpp
  include/shell/executor.hpp
  include/shell/builtin_registry.hpp
  include/shell/job_controller.hpp
  src/lexer/tokenizer.cpp
  src/parser/parser.cpp
  src/executor/executor.cpp
  src/builtins/builtin_registry.cpp
  src/jobs/job_controller.cpp
  src/signals/signal_handler.cpp
  tests/shell_test.cpp
```

## 9) 集成测试与验收

- `echo hello` 能正确输出。
- 管道 `echo hello | tr a-z A-Z` 可用。
- `cat < in.txt > out.txt` 可用。
- `cd`、`export`、`exit` 在父进程中生效。
- 后台任务执行后不会残留僵尸进程。
- `Ctrl-C` 不会杀掉 Shell 本体。

## 10) 与现有笔记的对应关系

- [[08_Linux_OS_Fundamentals|Linux OS 基础：进程、线程、信号与文件 I/O]]
- [[11_Linux_Project_Closure|Linux 工程闭环与项目实战]]

## 11) 最小启动流程

```cpp
int main() {
    Shell shell;
    return shell.run();
}
```

启动顺序建议是：

1. 初始化提示符和环境变量。
2. 安装信号处理器。
3. 进入读取-解析-执行循环。
4. 回收后台子进程。

这份笔记已经可以直接拆成 `lexer`、`parser`、`executor`、`builtins` 和 `jobs` 五层实现。

## 12) 第一版源码草案

建议先落一个 `src/main.cpp`，把 Shell 的交互入口串起来：

```cpp
#include "shell/shell.hpp"

int main() {
    Shell shell;
    return shell.run();
}
```

然后再补 `src/lexer/tokenizer.cpp`、`src/parser/parser.cpp` 和 `src/executor/executor.cpp`，先跑通单命令，再补管道和重定向。

## 13) 头文件与源码骨架

```cpp
// include/shell/shell.hpp
class Shell {
public:
    int run();

private:
    int executeLine(const std::string& line);
};

// src/main.cpp
int main() {
    Shell shell;
    return shell.run();
}
```
