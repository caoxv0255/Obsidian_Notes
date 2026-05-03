---
type: concept
topic: javascript_browser_modules
category: javascript
difficulty: intermediate
prerequisites: [[01_JavaScript_Core]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# JavaScript 浏览器与模块

## 核心定义

浏览器端 JavaScript 最常见的任务是操作 DOM、响应事件、组织模块和调用网络 API。

## 快速参考

| 场景 | 常用能力 |
| ------ | ---------- |
| DOM | `querySelector`、`createElement`、`textContent` |
| 事件 | `addEventListener`、事件冒泡、事件委托 |
| 模块 | `export` / `import`、`type="module"` |
| 网络 | `fetch`、`Response`、`Request` |
| 存储 | `localStorage`、`sessionStorage` |
| 生命周期 | `DOMContentLoaded`、`defer` |

## 代码示例

```javascript
const button = document.querySelector('#submit');

button.addEventListener('click', () => {
    const title = document.querySelector('#title');
    title.textContent = 'Clicked';
});
```

## 补充示例：事件委托

```javascript
document.addEventListener('click', (event) => {
    const button = event.target.closest('[data-action]');
    if (!button) {
        return;
    }

    console.log(button.dataset.action);
});
```

## 模块化思路

- 视图层负责渲染
- 状态层负责保存任务列表
- 存储层负责 localStorage / fetch 同步
- 事件层负责把用户输入转成状态变更

## 补充示例：localStorage

```javascript
const STORAGE_KEY = 'todo-app-v1';

export function saveTasks(tasks) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

export function loadTasks() {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
}
```

## 重点

- 模块化可以避免全局变量污染。
- DOM 操作前要确认节点已加载，或把脚本放到 `body` 末尾。
- `fetch` 常用于浏览器网络请求。
- 事件委托适合列表、菜单和动态节点。
- 状态和 DOM 最好分开，不要让页面只剩“手写同步”。

## 常见坑

- 在 DOM 未加载时就查询节点。
- 直接修改 DOM 却没有稳定的状态来源。
- 对 `fetch` 的 `response.ok` 和错误码处理不完整。
- 在表单逻辑里忽略防抖、校验和提交态。

## 练习

1. 写一个点击按钮修改文本的页面。
2. 用 `export` / `import` 拆分一个小工具模块。
3. 给表单加简单校验。
4. 用 `localStorage` 保存一个待办列表。
