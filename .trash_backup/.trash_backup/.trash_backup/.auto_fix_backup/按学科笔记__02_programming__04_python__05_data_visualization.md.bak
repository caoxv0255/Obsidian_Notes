---
type: cookbook
topic: data_visualization
category: data_science
difficulty: beginner
prerequisites: [[temp_data_cleaning]]
acm_relevant: false
created: 2026-02-20
status: complete
---

# 数据可视化

> 快速参考：Matplotlib、Seaborn 和 Plotly 的常用图表和最佳实践

## 核心概念

可视化是数据沟通的关键工具，能够直观地展示数据模式和洞察。

## 快速参考

### 1. Matplotlib 基础图表

```python
import matplotlib.pyplot as plt
import numpy as np

# 设置中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 折线图
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Line 1', color='blue', linewidth=2, linestyle='-')
plt.plot(x, y2, label='Line 2', color='red', linewidth=2, linestyle='--')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.title('折线图')
plt.legend()
plt.grid(True)
plt.show()

# 柱状图
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue')
plt.xlabel('类别')
plt.ylabel('值')
plt.title('柱状图')
plt.show()

# 散点图
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', alpha=0.6, s=100)
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.title('散点图')
plt.show()

# 直方图
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='green', alpha=0.7, edgecolor='black')
plt.xlabel('值')
plt.ylabel('频数')
plt.title('直方图')
plt.show()

# 箱线图
plt.figure(figsize=(10, 6))
plt.boxplot([data1, data2, data3], labels=['A', 'B', 'C'])
plt.title('箱线图')
plt.show()

# 饼图
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('饼图')
plt.show()

# 子图
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y)
axes[0, 0].set_title('折线图')
axes[0, 1].bar(categories, values)
axes[0, 1].set_title('柱状图')
axes[1, 0].scatter(x, y)
axes[1, 0].set_title('散点图')
axes[1, 1].hist(data)
axes[1, 1].set_title('直方图')
plt.tight_layout()
plt.show()
```

### 2. Seaborn 统计可视化

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 设置风格
sns.set_style('whitegrid')
sns.set_palette('husl')

# 分布图
plt.figure(figsize=(10, 6))
sns.histplot(data, kde=True, bins=30)
plt.title('分布图')
plt.show()

# 箱线图（分组）
plt.figure(figsize=(10, 6))
sns.boxplot(x='category', y='value', data=df)
plt.title('分组箱线图')
plt.show()

# 小提琴图
plt.figure(figsize=(10, 6))
sns.violinplot(x='category', y='value', data=df)
plt.title('小提琴图')
plt.show()

# 条形图（带误差线）
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='value', data=df, ci=95)
plt.title('条形图')
plt.show()

# 散点图（带回归线）
plt.figure(figsize=(10, 6))
sns.regplot(x='x_column', y='y_column', data=df)
plt.title('散点图 + 回归线')
plt.show()

# 热力图
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('相关性热力图')
plt.show()

# 成对关系图
sns.pairplot(df, hue='category')
plt.show()

# 计数图
plt.figure(figsize=(10, 6))
sns.countplot(x='category', data=df)
plt.title('计数图')
plt.show()

# 分面网格
g = sns.FacetGrid(df, col='category1', row='category2')
g.map(plt.hist, 'value')
plt.show()
```

### 3. Plotly 交互式可视化

```python
import plotly.express as px
import plotly.graph_objects as go

# 折线图（交互式）
fig = px.line(df, x='date', y='value', color='category')
fig.show()

# 散点图（交互式）
fig = px.scatter(df, x='x_column', y='y_column', 
                 color='category', size='value',
                 hover_data=['column1', 'column2'])
fig.show()

# 柱状图（交互式）
fig = px.bar(df, x='category', y='value', color='category')
fig.show()

# 热力图（交互式）
fig = px.imshow(df.corr(), text_auto=True, aspect='auto')
fig.show()

# 3D 散点图
fig = px.scatter_3d(df, x='x', y='y', z='z', color='category')
fig.show()

# 地理图
fig = px.scatter_geo(df, lat='latitude', lon='longitude', 
                     color='value', size='value')
fig.show()

# 时间序列图
fig = px.line(df, x='date', y='value', title='时间序列')
fig.update_xaxes(rangeslider_visible=True)
fig.show()

# 子图
from plotly.subplots import make_subplots
fig = make_subplots(rows=2, cols=2)
fig.add_trace(go.Scatter(x=x, y=y), row=1, col=1)
fig.add_trace(go.Bar(x=categories, y=values), row=1, col=2)
fig.show()
```

### 4. 图表美化技巧

```python
# 设置图表大小
plt.figure(figsize=(12, 6))

# 设置颜色
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
plt.bar(categories, values, color=colors)

# 添加网格
plt.grid(True, linestyle='--', alpha=0.6)

# 添加注释
plt.annotate('最高值', xy=(max_x, max_y), xytext=(10, 10),
             textcoords='offset points', arrowprops=dict(arrowstyle='->'))

# 设置坐标轴范围
plt.xlim(0, 100)
plt.ylim(0, 1000)

# 设置坐标轴刻度
plt.xticks(rotation=45)
plt.yticks(range(0, 1000, 100))

# 添加文本
plt.text(50, 500, '中间值', ha='center', fontsize=12)

# 双 Y 轴
fig, ax1 = plt.subplots()
ax1.plot(x, y1, color='blue')
ax2 = ax1.twinx()
ax2.plot(x, y2, color='red')

# 保存图表
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.savefig('plot.pdf', format='pdf')
```

### 5. 特殊图表

```python
# 面积图
plt.figure(figsize=(10, 6))
plt.fill_between(x, y, alpha=0.3)
plt.plot(x, y)
plt.title('面积图')
plt.show()

# 堆叠柱状图
plt.figure(figsize=(10, 6))
plt.bar(categories, values1, label='A')
plt.bar(categories, values2, bottom=values1, label='B')
plt.legend()
plt.title('堆叠柱状图')
plt.show()

# 雷达图
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 3, 5, 2, 4]
angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]
plt.polar(angles, values)
plt.fill(angles, values, alpha=0.25)
plt.show()

# 树状图
import squarify
plt.figure(figsize=(10, 6))
squarify.plot(sizes=values, label=categories, alpha=0.7)
plt.axis('off')
plt.show()
```

### 6. 数据报告模板

```python
def create_dashboard(df):
    """创建数据仪表板"""
    fig = make_subplots(rows=2, cols=2, 
                        subplot_titles=('趋势图', '分布图', '相关性', '排名'))
    
    # 趋势图
    fig.add_trace(go.Scatter(x=df.index, y=df['value']), row=1, col=1)
    
    # 分布图
    fig.add_trace(go.Histogram(x=df['value']), row=1, col=2)
    
    # 相关性
    fig.add_trace(go.Heatmap(z=df.corr().values), row=2, col=1)
    
    # 排名
    fig.add_trace(go.Bar(x=df['category'], y=df['value']), row=2, col=2)
    
    fig.update_layout(height=800, showlegend=False)
    fig.show()
```

## 最佳实践

| 实践 | 说明 |
|------|------|
| 简洁明了 | 避免过度装饰，突出数据 |
| 合理配色 | 使用对比度适中、色盲友好的配色 |
| 清晰标注 | 标题、坐标轴标签、图例要完整 |
| 适当尺寸 | 根据用途选择合适的分辨率和尺寸 |
| 交互式 | 展示用交互式，报告用静态图 |

## 常见问题

**Q: 中文显示乱码？**
```python
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac
```

**Q: 图表重叠？**
```python
plt.tight_layout()  # 自动调整布局
```

## 相关链接
- [[temp_data_analysis|数据分析]]
- [[temp_ml_pipeline|ML 全流程]]