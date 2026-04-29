---
type: concept
topic: training_loop
category: pytorch
difficulty: intermediate
prerequisites: [[03_NN_Module]]
acm_relevant: false
created: 2026-02-20
status: complete
---

# PyTorch 训练循环

## 核心定义

训练循环是训练神经网络的标准流程。

## 代码示例

```python
import torch
import torch.nn as nn
import torch.optim as optim

# 模型、损失函数、优化器
model = SimpleNN(10, 5, 1)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 训练循环
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')
```

## 机器学习应用

模型训练、参数优化、性能监控等。