---
type: concept
topic: javascript_core
category: javascript
difficulty: beginner
prerequisites: [[00_JavaScript_Index]]
acm_relevant: false
created: 2026-04-25
status: complete
---

# JavaScript 核心语法

## 核心定义

JavaScript 是动态类型、原型继承、以函数为核心的语言。它最常见的运行环境是浏览器和 Node.js。

## 快速参考

| 主题 | 要点 |
| ------ | ------ |
| 变量 | `let` / `const` 优先，少用 `var` |
| 类型 | primitive 与 object 两大类 |
| 函数 | 函数声明、函数表达式、箭头函数 |
| 对象 | 字面量、属性、方法、原型链 |
| 数组 | `map` / `filter` / `reduce` 很常用 |
| 比较 | 通常优先 `===`，少用 `==` |
| 作用域 | 全局、函数、块级作用域 |
| 模块 | `export` / `import` |

## 数据模型

- primitive：`number`、`string`、`boolean`、`undefined`、`null`、`symbol`、`bigint`
- object：普通对象、数组、函数、日期、正则、Map、Set
- JS 里的对象是引用语义，赋值通常复制的是引用

## 代码示例

```javascript
const numbers = [1, 2, 3, 4, 5];

const square = (value) => value * value;
const result = numbers.map(square).filter((value) => value > 10);

console.log(result);
```

## 补充示例：闭包与对象

```javascript
function createCounter() {
    let value = 0;
    return () => ++value;
}

const next = createCounter();
console.log(next());
console.log(next());

class User {
    constructor(name) {
        this.name = name;
    }

    greet() {
        return `Hello, ${this.name}`;
    }
}
```

## 重点

- JS 的对象是键值结构，数组也是对象的一种特例。
- 闭包可以保存外部变量的引用。
- `JSON` 是前后端常见的数据交换格式。
- `this` 的值取决于调用方式，箭头函数不会重新绑定 `this`。
- `NaN` 不等于自身，判断时用 `Number.isNaN`。

## 常见坑

- 把 `==` 当作内容比较。
- 忘记处理整数和浮点比较的边界。
- 误以为 `String`、数组、对象是值传递。
- 在箭头函数里期待 `this` 指向调用对象。

## 练习

1. 用 `map` / `filter` / `reduce` 处理数组。
2. 写一个闭包计数器。
3. 对比 `===` 与 `==`。
4. 写一个 `class` 和一个普通对象，比较它们的使用方式。
