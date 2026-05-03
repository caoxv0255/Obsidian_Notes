---
type: concept
topic: javascript_async_node
category: javascript
difficulty: intermediate
prerequisites: [[02_JavaScript_Browser_Modules]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# JavaScript 异步与 Node.js

## 核心定义

异步编程是 JavaScript 的核心能力之一。`Promise`、`async/await` 和事件循环决定了大多数实际项目的写法。

## 快速参考

| 主题 | 要点 |
| ------ | ------ |
| 回调 | 早期异步写法，层级容易嵌套 |
| Promise | 表示未来结果，支持链式组合 |
| async/await | 让异步代码更接近同步控制流 |
| 事件循环 | 解释宏任务、微任务和执行顺序 |
| Node.js | 适合脚本、服务端和工具开发 |
| 常用模块 | `fs`、`path`、`http`、`url` |

## 代码示例

```javascript
async function loadJson(url) {
    const response = await fetch(url);
    return await response.json();
}

loadJson('https://example.com/data.json')
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
```

## 补充示例：Promise 并发与错误处理

```javascript
const tasks = [
    fetch('/api/users').then((response) => response.json()),
    fetch('/api/posts').then((response) => response.json()),
];

Promise.all(tasks)
    .then(([users, posts]) => {
        console.log(users, posts);
    })
    .catch((error) => {
        console.error('request failed:', error);
    });
```

## Node.js 常见用法

- `process.argv` 处理命令行参数
- `node:fs/promises` 读写文件
- `node:path` 拼接路径
- `node:http` 搭最小服务
- `npm run` 管理脚本

## 补充示例：读取文件并统计行数

```javascript
import { readFile } from 'node:fs/promises';

async function countLines(filePath) {
    const text = await readFile(filePath, 'utf8');
    return text.split(/\r?\n/).length;
}

countLines('README.md')
    .then((count) => console.log(count))
    .catch((error) => console.error(error));
```

## 重点

- 异步流程要显式处理错误。
- Node.js 中 `npm` 管理依赖和脚本。
- 事件循环是理解性能和顺序的关键。
- `Promise.all` 适合并发请求，`Promise.race` 适合竞速。
- `async/await` 里依然要用 `try/catch` 控制错误传播。

## 常见坑

- 忽略 `catch` 或 `try/catch`，导致异步错误丢失。
- 误把同步阻塞代码放进 Node 热路径。
- 不区分微任务和宏任务，导致顺序判断错误。
- 在请求未完成前就继续依赖结果。

## 练习

1. 把回调风格改写成 `Promise`。
2. 用 `async/await` 封装一个请求函数。
3. 写一个简单的 Node.js HTTP 服务。
4. 用 `fs/promises` 写一个文件统计小脚本。
