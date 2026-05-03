---
type: project
topic: javascript_practice_todo_app
category: javascript
difficulty: intermediate
prerequisites: [[03_JavaScript_Async_Node]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# JavaScript 实战：浏览器待办事项管理器

## 目标

做一个基于浏览器的待办事项应用，支持添加、完成、删除、筛选和本地持久化。这个项目会把核心语法、DOM、模块、事件和存储串起来。

## 模块拆分

- `state`：任务状态和过滤条件。
- `render`：把状态渲染到页面。
- `storage`：localStorage 读写。
- `events`：按钮、表单和列表事件处理。
- `api`：可选的远程同步层。

## 实现顺序

1. 先渲染一个静态列表。
2. 再实现新增、完成、删除。
3. 接入 localStorage 持久化。
4. 增加筛选、搜索和排序。
5. 最后拆成模块并用 Vite 打包。

## 数据模型

```javascript
export function createTask(title) {
    return {
        id: crypto.randomUUID(),
        title,
        done: false,
        createdAt: Date.now(),
    };
}
```

## 状态骨架

```javascript
const state = {
    tasks: [],
    filter: 'all',
};
```

## 文件结构建议

```text
src/
  main.js
  state.js
  storage.js
  render.js
  events.js
  api.js
```

## 本地存储思路

- 任务列表全部保存在 localStorage。
- 初始化时从 localStorage 恢复。
- 状态变化后统一调用保存函数。
- 页面刷新后应该保持任务列表不丢失。

## 代码骨架

```javascript
import { loadTasks, saveTasks } from './storage.js';
import { renderApp } from './render.js';

const state = {
    tasks: loadTasks(),
    filter: 'all',
};

function commit(nextState) {
    Object.assign(state, nextState);
    saveTasks(state.tasks);
    renderApp(state);
}

renderApp(state);
```

## 常见坑

- 直接操作 DOM 却没有稳定的状态来源。
- localStorage 保存的是字符串，读写时要 `JSON.parse` / `JSON.stringify`。
- 事件绑定散落在各处，后期很难维护。
- 把远程同步和本地状态混在一个函数里。

## 测试建议

- 纯函数优先写单元测试。
- 任务过滤、排序和状态切换适合单测。
- 浏览器端交互可以做手工回归测试。

## 练习

1. 给待办事项增加编辑功能。
2. 增加已完成筛选和搜索框。
3. 给存储层加一个简单的导入/导出功能。
4. 用 Vite 把项目跑起来并写一个 README。
