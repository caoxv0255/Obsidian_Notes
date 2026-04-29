---
type: concept
topic: rust_ownership_borrowing
category: rust
difficulty: intermediate
prerequisites: [[01_Rust_Basics]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# Rust 所有权与借用

## 核心定义

所有权、借用和生命周期是 Rust 最重要的语言机制，也是它能做到内存安全的基础。

## 快速参考

| 概念 | 要点 |
| ------ | ------ |
| 所有权 | 一个值同一时刻只有一个所有者 |
| 移动 | 赋值、传参后默认转移所有权 |
| 借用 | 通过引用临时访问，不拿走所有权 |
| 可变借用 | 同一时刻只能有一个 |
| 不可变借用 | 可以有多个 |
| 生命周期 | 描述引用有效范围 |
| 切片 | `&str`、`&[T]` 是常见借用形态 |

## 代码示例

```rust
fn longest<'a>(left: &'a str, right: &'a str) -> &'a str {
    if left.len() >= right.len() {
        left
    } else {
        right
    }
}

fn main() {
    let a = String::from("rust");
    let b = "language";
    println!("{}", longest(&a, b));
}
```

## 补充示例：切片与可变借用

```rust
fn first_word(text: &str) -> &str {
    match text.find(' ') {
        Some(index) => &text[..index],
        None => text,
    }
}

fn push_suffix(value: &mut String) {
    value.push_str("_done");
}
```

## 重点

- 先理解“移动”再理解“借用”。
- 只要涉及引用返回，就要关注生命周期。
- `Vec<T>`、`String`、`Box<T>` 都是常见的所有权载体。
- `Copy` 类型在赋值后不会失去原值，`Clone` 则需要显式克隆。

## 常见坑

- 从函数返回引用，但被引用的数据活得不够久。
- 在同一作用域里同时保留多个可变借用。
- 把 `String` 传给函数后还以为还能继续使用原值。
- 只盯着生命周期语法，不理解“引用必须活得更久”这个语义。

## 练习

1. 写一个返回更长字符串切片的函数。
2. 对比移动和借用对变量可用性的影响。
3. 用 `Vec<String>` 组织一组字符串。
4. 写一个 `first_word` 函数并返回切片。
