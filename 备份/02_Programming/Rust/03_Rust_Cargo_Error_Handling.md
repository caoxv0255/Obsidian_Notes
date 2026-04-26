---
type: concept
topic: rust_cargo_error_handling
category: rust
difficulty: intermediate
prerequisites: [[02_Rust_Ownership_Borrowing]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# Rust Cargo 与错误处理

## 核心定义

Cargo 负责项目构建、依赖管理和测试；`Result`、`Option` 和 `?` 则是 Rust 中最常见的错误处理方式。

## 快速参考

| 主题 | 要点 |
| ------ | ------ |
| 构建 | `cargo build`、`cargo run`、`cargo test` |
| 格式化 | `cargo fmt` |
| 检查 | `cargo clippy` |
| 错误类型 | `Result<T, E>` 适合可恢复错误 |
| 空值 | `Option<T>` 适合可能为空的值 |
| 传播 | `?` 可以快速传播错误 |

## Cargo 常用结构

```text
project/
  Cargo.toml
  src/
    main.rs
    lib.rs
  tests/
```

## 代码示例

```rust
use std::fs;

fn read_file(path: &str) -> Result<String, std::io::Error> {
    let content = fs::read_to_string(path)?;
    Ok(content)
}

fn main() {
    match read_file("README.md") {
        Ok(content) => println!("{}", content.len()),
        Err(error) => eprintln!("error: {}", error),
    }
}
```

## 补充示例：Option 与 Result 的组合

```rust
fn parse_port(input: Option<&str>) -> Result<u16, String> {
    let text = input.ok_or_else(|| "missing port".to_string())?;
    text.parse::<u16>().map_err(|error| error.to_string())
}
```

## 重点

- Rust 鼓励把错误处理写在类型系统里。
- 单元测试和文档测试都可以直接集成到 Cargo 工作流。
- `cargo fmt` 和 `cargo clippy` 很适合保持代码质量。
- `map`、`and_then`、`ok_or_else` 这类组合函数很常用。

## 常见坑

- 过度使用 `unwrap()`。
- 让错误一路变成字符串，最后丢失语义。
- 忘记给库和二进制项目安排清晰的 `src/lib.rs`、`src/main.rs`。
- 不把测试放进 Cargo 的标准流程里。

## 练习

1. 给一个文件读取函数补上 `Result`。
2. 写一个 `Option` 到 `Result` 的转换例子。
3. 用 `cargo test` 写一个简单单元测试。
4. 写一个函数，把字符串解析成端口号并返回 `Result`。
