# XuCao Obsidian Vault

一个以 Obsidian 为中心的长期学习知识库，覆盖数学、编程、算法、计算机系统、经济学，以及量化交易与计算神经科学双路径规划。

## 项目定位

- 目标：构建可持续迭代的本科到科研申请知识体系与证据链。
- 形态：课程笔记 + 专题索引 + 项目规划 + 日常记录 + 电子书资料库。
- 使用方式：以索引页为入口，通过双向链接和目录结构进行学习与检索。

## 仓库结构总览

```text
.
├── README.md
├── .obsidian/
├── copilot/
├── history/
├── MY_Learning/
├── 按学科笔记/
│   ├── 01_Mathematics/
│   ├── 02_Programming/
│   ├── 数据结构笔记(C++)/
│   ├── 算法导论笔记(C++)/
│   ├── 经济学笔记/
│   └── 计算机组织与设计_RISC-V版/
├── 电子书附件/
├── 记录/                      # 学习与复盘模板（daily/weekly/monthly/semester）
└── 其他课程与项目目录
```

## 核心入口导航

### 1) 总控入口

- [MY_Learning/00_Index.md](MY_Learning/00_Index.md)
	- 双路径（量化交易/计算神经科学）四年规划主索引
	- 包含进度状态、优先级待办、执行模板与阶段性报告

### 2) 学科与课程笔记入口

- 按学科总目录： [按学科笔记/](按学科笔记)
	- [01_Mathematics/](按学科笔记/01_Mathematics/)：数学笔记（代数、微积分、概率、优化）
		- 主要文件： [按学科笔记/01_Mathematics/00_Symbols_Conventions.md](按学科笔记/01_Mathematics/00_Symbols_Conventions.md)
	- [02_Programming/](按学科笔记/02_Programming/)：编程语言与工具
		- 子目录： `C++/`, `Python/`, `Java/`, `JavaScript/`, `Rust/`
		- 入口文件： [按学科笔记/02_Programming/00_Index.md](按学科笔记/02_Programming/00_Index.md)
	- [数据结构笔记(C++)/](按学科笔记/数据结构笔记%28C%2B%2B%29/)：系统章节化笔记（含章节索引与习题）
		- 入口文件： [按学科笔记/数据结构笔记(C++)/00_Index.md](按学科笔记/数据结构笔记%28C%2B%2B%29/00_Index.md)
	- [算法导论笔记(C++)/](按学科笔记/算法导论笔记%28C%2B%2B%29/)：CLRS 主题分册与专题
		- 入口文件： [按学科笔记/算法导论笔记(C++)/快速开始.md](按学科笔记/算法导论笔记%28C%2B%2B%29/快速开始.md)
	- [经济学笔记/](按学科笔记/经济学笔记/)：教材索引与主题分类
		- 入口文件： [按学科笔记/经济学笔记/00_Index.md](按学科笔记/经济学笔记/00_Index.md)
	- [计算机组织与设计_RISC-V版/](按学科笔记/计算机组织与设计_RISC-V版/)
		- 入口文件： [按学科笔记/计算机组织与设计_RISC-V版/00_Index.md](按学科笔记/计算机组织与设计_RISC-V版/00_Index.md)

 （注：各学科目录下通常包含 `00_Index.md` 或 `README.md` 作为模块入口）

### 3) 日常与项目实践入口

- [记录/](记录)
	- 学习与复盘模板（每日/每周/每月/学期），便于快速建笔记
- [MY_Learning/Projects/](MY_Learning/Projects)
	- 项目化学习与研究实践载体
- [MY_Learning/00_迭代报告/](MY_Learning/00_迭代报告)
	- 阶段性重构与执行回顾

### 4) 资料库入口

- [电子书附件/](电子书附件)
	- 编程、数学、经济学、文学理财与哲学等电子资料

## 内容特点

- 索引驱动：大部分模块都有 `00_Index.md` 或 `README.md` 作为入口。
- 双轨规划：`MY_Learning` 将共享基础与双方向能力矩阵统一管理。
- 结构化笔记：广泛使用 Markdown、YAML front matter、Obsidian 双链。
- 长周期迭代：通过日记与迭代报告跟踪实际进展，而非静态存档。

## 推荐使用流程

1. 从 [MY_Learning/00_Index.md](MY_Learning/00_Index.md) 进入，确认当前阶段目标。
2. 按需要跳转到对应学科索引（如 [按学科笔记/02_Programming/00_Index.md](按学科笔记/02_Programming/00_Index.md)）。
3. 学习后在 [记录/](记录) 或相应学科日记中留下当天输出与问题。
4. 定期在 [MY_Learning/00_迭代报告/](MY_Learning/00_迭代报告) 复盘，更新优先级与路线。

## 快速开始清单

- [ ] 打开 [MY_Learning/00_Index.md](MY_Learning/00_Index.md)，确认本周主线任务
- [ ] 打开一个学科索引并选定 1 个最小学习单元
- [ ] 当天输出 1 条可复用笔记（定义/例题/代码片段/总结其一）
- [ ] 在 [记录/](记录) 或 `coding_每日记录/`（如存在）记录进展、问题、下一步
- [ ] 每周复盘一次 [MY_Learning/00_迭代报告/](MY_Learning/00_迭代报告)

## 面向 Obsidian 的使用说明

- 建议在 Obsidian 中打开本目录作为一个 Vault。
- 优先使用双向链接（`[[...]]`）和标签做知识关联。
- 新增模块时，建议先创建索引页再补充分章节内容。
- 与长期规划相关的内容，优先挂接到 `MY_Learning` 的主线结构。

## 维护建议

- 保持入口稳定：尽量维持关键索引文件路径不频繁改名。
- 保持命名一致：章节文件建议使用编号前缀（如 `01_`, `02_`）。
- 保持增量更新：每次学习后补最小可复用笔记，而不是只留零散草稿。

## 当前状态

- 仓库已形成“学科笔记 + 双路径规划 + 日常记录 + 资料库”的完整骨架。
- 重点推进区域以 `MY_Learning/00_Index.md` 的进度和待办为准。

模板迁移（2026-04-29）：
- 为便于集中管理，我已在 `XuCao/记录/` 创建学习与复盘模板（`daily_template.md`、`weekly_template.md`、`monthly_template.md`、`semester_template.md`）并同步 `README`。
- 原位置 `MY_Learning/Tracking/` 下的模板已移除，原 `README.md` 内容已复制到 `记录/README.md` 以保留说明。

---

Last updated: 2026-04-29
