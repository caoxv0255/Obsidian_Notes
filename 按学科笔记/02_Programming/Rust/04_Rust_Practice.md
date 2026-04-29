---
type: project
topic: rust_practice_grep
category: rust
difficulty: intermediate
prerequisites: [[03_Rust_Cargo_Error_Handling]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# Rust 实战：命令行文件搜索器

## 目标

做一个小型的 `grep` 风格工具，支持在文件中搜索关键字、区分大小写、输出命中行，并用测试保证搜索逻辑稳定。

## 模块拆分

- `config`：命令行参数解析。
- `search`：纯搜索逻辑。
- `output`：结果输出格式。
- `cli`：入口和错误处理。
- `tests`：单元测试和集成测试。

## 实现顺序

1. 先实现纯搜索函数。
2. 再把命令行参数解析出来。
3. 接入文件读取和错误返回。
4. 增加大小写控制。
5. 最后写测试和打包说明。

## 配置骨架

```rust
use std::env;

pub struct Config {
    pub query: String,
    pub file_path: String,
    pub case_sensitive: bool,
}

impl Config {
    pub fn build(mut args: impl Iterator<Item = String>) -> Result<Self, String> {
        let _program = args.next();
        let query = args.next().ok_or_else(|| "missing query".to_string())?;
        let file_path = args.next().ok_or_else(|| "missing file path".to_string())?;
        let case_sensitive = env::var("CASE_INSENSITIVE").is_err();

        Ok(Self {
            query,
            file_path,
            case_sensitive,
        })
    }
}
```

## 搜索函数

```rust
pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    contents
        .lines()
        .filter(|line| line.contains(query))
        .collect()
}
```

## 代码骨架

```rust
use std::error::Error;
use std::fs;

fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(&config.file_path)?;
    let matches = if config.case_sensitive {
        search(&config.query, &contents)
    } else {
        search(&config.query.to_lowercase(), &contents.to_lowercase())
    };

    for line in matches {
        println!("{}", line);
    }

    Ok(())
}
```

## 常见坑

- 把 I/O、解析和搜索逻辑揉成一个函数。
- 过度使用 `unwrap()`。
- 忘记给搜索函数写测试。
- 借用返回值时没有想清楚生命周期。

## 测试建议

- 给纯搜索函数写单元测试。
- 给大小写敏感和不敏感场景分别建测试。
- 给参数缺失和文件不存在场景写错误测试。

## 练习

1. 增加大小写不敏感搜索。
2. 给命令行参数解析写测试。
3. 把输出格式改成带行号。
4. 给项目加一个 README，说明使用方法。
