---
type: concept
topic: autograd
category: pytorch
difficulty: intermediate
prerequisites: [[01_Tensors]]
acm_relevant: false
created: 2026-02-20
status: complete
---

# PyTorch 自动微分

## 核心定义

Autograd 是 PyTorch 的自动微分引擎，用于计算梯度。

## 代码示例

```python
import torch

# 创建需要梯度的张量
x = torch.tensor([2.0], requires_grad=True)

# 计算过程
y = x ** 2 + 3 * x + 1

# 反向传播
y.backward()

print(f"梯度: {x.grad}")
```

## 机器学习应用

神经网络训练、梯度计算、反向传播等。