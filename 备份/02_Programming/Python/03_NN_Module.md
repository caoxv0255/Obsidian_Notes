---
type: concept
topic: nn_module
category: pytorch
difficulty: intermediate
prerequisites: [[02_Autograd]]
acm_relevant: false
created: 2026-02-20
status: complete
---

# PyTorch 神经网络模块

## 核心定义

nn.Module 是 PyTorch 中所有神经网络模块的基类。

## 代码示例

```python
import torch
import torch.nn as nn

# 定义神经网络
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 创建模型
model = SimpleNN(10, 5, 1)
print(model)
```

## 机器学习应用

构建神经网络模型、定义网络结构等。