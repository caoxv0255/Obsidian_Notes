---
type: concept
topic: rust_basics
category: rust
difficulty: beginner
prerequisites: [[00_Rust_Index]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# Rust 基础语法

## 核心定义

Rust 是静态类型、强调内存安全、零成本抽象的语言。它常用于系统编程、工具开发和高可靠服务。

## 快速参考

| 主题 | 要点 |
| ------ | ------ |
| 变量 | 默认不可变，使用 `mut` 才可修改 |
| 函数 | 表达式风格，最后一行可作为返回值 |
| 控制流 | `if`、`match`、`while`、`for`、`loop` |
| 数据结构 | `struct`、`enum`、元组结构体 |
| 模块 | `mod`、`use`、`pub` |
| 集合 | `Vec`、`String`、`HashMap` |
| 项目 | 从 `cargo new` 开始 |

## 代码示例

```rust
fn main() {
    let numbers = vec![1, 2, 3, 4];
    let sum: i32 = numbers.iter().sum();
    println!("{}", sum);
}
```

## 补充示例：结构体与枚举

```rust
#[derive(Debug)]
enum Command {
    Add(String),
    Done(u32),
    Quit,
}

struct Task {
    id: u32,
    title: String,
    done: bool,
}

impl Task {
    fn mark_done(&mut self) {
        self.done = true;
    }
}

fn handle(command: Command) {
    match command {
        Command::Add(title) => println!("add: {}", title),
        Command::Done(id) => println!("done: {}", id),
        Command::Quit => println!("quit"),
    }
}
```

## 重点

- `String` 和 `&str` 是不同层次的字符串类型。
- `Option` 和 `Result` 是常见返回类型。
- Rust 倾向于把错误和空值显式化。
- `match` 必须覆盖所有分支，编译器会强制检查。
- 语句和表达式的区别很重要，分号会改变返回值。

## 常见坑

- 忘记加 `mut`。
- 以为赋值总是复制，实际上很多类型会移动所有权。
- `match` 分支不完整。
- 把 `String` 和 `&str` 混成同一个类型。

## 练习

1. 用 `cargo new` 创建项目并运行 `cargo run`。
2. 用 `match` 处理一个 `enum`。
3. 对比 `String` 与 `&str`。
4. 写一个 `Task` 结构体并实现一个 `mark_done` 方法。
