## 主要页面

  

启动后打开根地址即可进入控制台页面：

  

- 平台总览

- 茶样评估

- 溯源查询

- 锚定状态查询与刷新

- 专家复核队列

- 操作日志

  

## 功能架构（产品 / UI 高层流程）

  

本节面向产品与交互设计，概述用户在平台上的主要任务流、页面组成与关键数据点，便于快速绘制交互稿与线框图。主要目标用户场景：提交茶样评估、查看评估结果与锚定状态、发起/处理专家复核、查询溯源链路与平台总览。

  

### 主要组件（高层）

- 后端服务：`src/server.js`（平台 API 与静态页面）

- 评估服务：`src/services/teaEvaluator.js` / `src/services/modelGateway.js`（本地规则与远程模型）

- 链上锚定：`src/services/blockchainAnchorService.js`（提交/查询/刷新锚定）

- 专家复核：`src/services/expertReview.js`（复核队列管理）

- 数据存储：`src/storage/teaDatabase.js`（SQLite，保存样本、批次、锚定与复核日志）

- 前端控制台：`src/web/`（桌面控制台）与小程序壳：`oneta-2026/miniprogram/`（移动端/小程序）

- 云函数：`oneta-2026/cloudfunctions/`（例：`evaluateTea/`、`platformGateway/`）

  

### 关键页面与交互流（示例用例）

下面每个流程给出主界面、关键交互点、所需数据字段与对应 API，便于设计时标注数据来源。

  

1) 茶样提交与评估流程（主流程）

- 页面/组件：提交评估表单（样本信息 + 三视图图片上传）与提交结果页（评分摘要 + 详情）

- 关键交互点：填写样本 → 上传图片 → 点击“提交评估” → 展示进度 → 显示评估结果或失败提示

- 必需数据字段（示例）：`sampleId`, `batchId`, `teaName`, `variety`, `farmerId`, `origin`（province/city/county/farmName）、`notes`、`images`、`signals`（dryTea/liquor/leafBottom/traceability/packaging/expertConfidence）

- 对应 API：`POST /api/tea/evaluate`

  

2) 链上锚定与状态查看

- 页面/组件：锚定状态列表/卡片（时间、链 tx/hash、状态）

- 关键交互点：查看 → 手动刷新 → 显示最新链状态或错误

- 对应 API：`GET /api/anchors`, `GET /api/anchors/status`, `POST /api/anchors/refresh`

  

3) 专家复核流程

- 页面/组件：复核队列（列表 + 筛选）、复核详情（样本信息 + 评估证据 + 评论区）

- 对应 API：`GET /api/reviews`, `POST /api/reviews`, `PATCH /api/reviews`

  

4) 溯源查询（按批次/样本）

- 页面/组件：溯源查询输入（批次ID/样本ID）、溯源时间线（事件列表/哈希/验证结果）

- 对应 API：`GET /api/tea/trace?batchId=...`

  

5) 平台总览（Dashboard）

- 页面/组件：总览面板（样本数、待复核数、锚定成功率、系统健康）

- 对应 API：`GET /api/platform/overview`, `GET /health`

  

### 设计注意点（给产品/设计的要点）

- 明确的状态与反馈（loading、排队、失败重试、确认操作）

- 在样本详情页提供完整时间线与可导出哈希证据以支持可追溯性

- 优先交付页面：提交评估、评估结果、复核队列；其次为溯源查询与锚定状态

- 图片上传需支持压缩与进度提示，移动端体验优化

  

### 给设计的交付清单（建议）

- 页面线框：Dashboard、提交评估、评估结果、复核队列、溯源时间线、锚定详情（共 6 页）

- 标注数据字段：为每个页面标注后端字段来源

- 状态矩阵：列出关键状态（处理中/失败/成功/需复核）与对应文案

- 可选图示：评估数据流序列图（提交 → 模型/规则 → 结果 → 条件触发锚定/复核）