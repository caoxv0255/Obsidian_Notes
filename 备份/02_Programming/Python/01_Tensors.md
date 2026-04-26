---
type: concept
topic: tensors
category: pytorch
difficulty: beginner
prerequisites: [[00_Python_Index|Python 科学计算与深度学习]]
acm_relevant: false
created: 2026-02-20
status: complete
---

# PyTorch 张量基础

## 核心定义

张量是 PyTorch 的基本数据结构，类似于 NumPy 数组但支持 GPU 加速。

## 代码示例

```python
import torch

# 创建张量
tensor = torch.tensor([1, 2, 3, 4, 5])
print(f"张量: {tensor}")

# 张量运算
result = tensor * 2
print(f"乘以 2: {result}")

# GPU 张量
if torch.cuda.is_available():
    tensor_gpu = tensor.cuda()
    print(f"GPU 张量: {tensor_gpu}")
```

## 机器学习应用

神经网络输入、权重存储、梯度计算等。