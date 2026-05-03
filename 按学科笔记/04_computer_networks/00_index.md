---
title: 计算机网络 课程索引
course: 计算机网络
tags: [index, 网络, networking]
---

# 计算机网络（课程索引）

简短描述：面向学生的计算机网络课程主页，按“分层模型 - 协议机制 - 抓包验证 - 网络应用项目”组织学习。

## 课程定位

计算机网络研究的是“分布式通信如何在不可靠链路上实现可靠协作”。学习网络，不只是背协议头字段，更要建立“分层抽象、端到端原则、性能与拥塞、可观测性与故障分析”的系统视角。

## 学习目标

- 理解分层模型、协议栈与报文封装/解封装的整体流程。
- 掌握链路层、网络层、传输层和应用层的核心机制。
- 能读懂抓包结果、路由过程与 TCP 行为。
- 能将基础协议知识用于设计一个可工作的网络应用。

## 先修知识

- 基础编程能力：至少能用一门语言编写文件、套接字与字符串处理逻辑。
- 计算机组成基础：比特、字节、地址、编码与系统调用。
- 基本数学：概率、排队、延迟与吞吐量的概念。

## 知识地图

1. 网络体系结构：OSI 与 TCP/IP，分层设计的价值。
2. 物理层与链路层：编码、介质访问、交换、VLAN、ARP。
3. 网络层：IP 编址、子网划分、路由、转发、NAT。
4. 传输层：UDP、TCP、连接管理、可靠传输、流量控制、拥塞控制。
5. 应用层：DNS、HTTP、SMTP、TLS、CDN 与 Web 架构。
6. 网络性能：时延、吞吐量、带宽、抖动、丢包与拥塞分析。
7. 网络安全与可观测性：加密、认证、抓包、日志、故障定位。

## 首篇笔记

- [网络体系结构与分层模型](01_lecture_notes/01_network_architecture.md)

## 进阶笔记

- [TCP 与可靠传输](01_lecture_notes/02_tcp_and_reliability.md)
- [网络层与路由](01_lecture_notes/03_network_layer_and_routing.md)
- [应用层协议](01_lecture_notes/04_application_layer_protocols.md)
- [网络性能](01_lecture_notes/05_network_performance.md)
- [网络安全与可观测性](01_lecture_notes/06_network_security.md)
- [网络项目与复盘](01_lecture_notes/07_network_project_review.md)

## 全部章节导航

1. [网络体系结构与分层模型](01_lecture_notes/01_network_architecture.md)
2. [TCP 与可靠传输](01_lecture_notes/02_tcp_and_reliability.md)
3. [网络层与路由](01_lecture_notes/03_network_layer_and_routing.md)
4. [应用层协议](01_lecture_notes/04_application_layer_protocols.md)
5. [网络性能](01_lecture_notes/05_network_performance.md)
6. [网络安全与可观测性](01_lecture_notes/06_network_security.md)
7. [网络项目与复盘](01_lecture_notes/07_network_project_review.md)

## 章节推进建议

- 第一轮：建立分层与封装的总图，先把“每层负责什么”说清楚。
- 第二轮：攻克 TCP 与 IP，因为它们是理解现代网络的核心。
- 第三轮：把 HTTP、DNS、TLS 串成一次完整网页访问过程。
- 第四轮：用抓包、路由、端口与 NAT 案例把协议落到现实环境。

## 推荐目录结构

- `01_lecture_notes/`：课堂笔记（按章节编号）。
- `02_problems/`：练习题与解答。
- `03_labs/`：实验与动手练习说明。
- `04_references/`：教材、RFC、工具文档。

## 项目式学习路径

### 阶段 0：工具与抓包

- 目标：学会用抓包和命令行观察网络。
- 任务：使用 ping、traceroute、nslookup、netstat、Wireshark 观察一次网页访问。
- 产出：抓包截图、字段解释、从 DNS 到 HTTP 的路径说明。

### 阶段 1：协议理解

- 目标：把协议头、状态机与数据流关系讲清楚。
- 任务：手绘或用 Markdown 画出链路层、IP、TCP、HTTP 的封装关系。
- 产出：协议字段表、状态转换图、关键概念对照表。

### 阶段 2：实现一个客户端/服务端

- 目标：把套接字编程与协议知识结合起来。
- 任务：实现一个简单 TCP 回显服务、一个多线程聊天室或一个静态文件服务器。
- 产出：协议说明、接口设计、异常处理、测试记录。

### 阶段 3：拥塞与性能分析

- 目标：理解网络性能的瓶颈来自哪里。
- 任务：在不同网络条件下测试 RTT、吞吐量和重传；比较不同 TCP 参数的影响。
- 产出：实验表格、性能图表、结论摘要。

### 阶段 4：综合项目

- 目标：做一个能连通现实环境的小型网络系统。
- 任务建议：
	- 实现一个带 HTTP 协议解析的静态网站小服务器。
	- 或实现一个局域网文件传输工具，支持断点续传、校验与日志。
- 产出：设计文档、协议格式说明、运行日志、故障排查记录。

## 课程检核清单

- 是否能解释一条 URL 从输入到页面显示的完整路径。
- 是否能解释 TCP 建连、挥手、重传与拥塞控制。
- 是否能读懂一个常见抓包中 IP/TCP/HTTP 的关键字段。
- 是否能说明路由、交换、NAT 和 DNS 分别解决什么问题。
- 是否能说清楚“端到端原则”的含义。

## 常用链接

- 练习入口：[02_problems/](02_problems/)
- 实验入口：[03_labs/](03_labs/)
- 参考资料：[04_references/](04_references/)

## 使用说明
复制本索引后，先建立“网络分层图 + 抓包实验 + 应用层项目”三层结构，再按协议层级逐步填充笔记。
