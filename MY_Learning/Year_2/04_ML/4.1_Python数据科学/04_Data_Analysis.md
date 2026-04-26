---
type: cookbook
topic: data_analysis
category: data_science
difficulty: intermediate
prerequisites: [[temp_data_cleaning]]
acm_relevant: false
created: 2026-02-20
status: complete
---

# 数据分析与统计

> 快速参考：描述性统计、分组聚合、数据透视和时间序列分析

## 核心概念

数据分析通过统计方法和可视化技术，从数据中提取有价值的洞察。

## 快速参考

### 1. 描述性统计

```python
import pandas as pd
import numpy as np

# 基本统计
df.describe()  # 数值列统计
df.info()  # 数据概览
df.shape  # 行列数
df.dtypes  # 数据类型

# 单列统计
df['column'].mean()  # 均值
df['column'].median()  # 中位数
df['column'].std()  # 标准差
df['column'].var()  # 方差
df['column'].min()  # 最小值
df['column'].max()  # 最大值
df['column'].sum()  # 求和
df['column'].count()  # 非空值数量
df['column'].quantile(0.25)  # 25% 分位数
df['column'].quantile(0.75)  # 75% 分位数

# 众数
df['column'].mode()
df['column'].value_counts()  # 值计数

# 偏度和峰度
df['column'].skew()  # 偏度
df['column'].kurt()  # 峰度

# 累积统计
df['column'].cumsum()  # 累积和
df['column'].cumprod()  # 累积积
df['column'].cummax()  # 累积最大值
df['column'].cummin()  # 累积最小值
```

### 2. 分组聚合

```python
# 单列分组
grouped = df.groupby('category_column')

# 聚合函数
grouped.mean()
grouped.sum()
grouped.count()
grouped.median()
grouped.std()

# 多列分组
grouped = df.groupby(['category1', 'category2'])

# 多个聚合函数
grouped.agg(['mean', 'std', 'count'])
grouped.agg({'column1': ['mean', 'std'], 'column2': ['sum', 'count']})

# 自定义聚合
grouped.agg({'column': lambda x: x.max() - x.min()})

# 分组后选择列
grouped['column'].mean()

# 分组统计描述
grouped.describe()

# 分组大小
grouped.size()

# 分组数量
grouped.nunique()
```

### 3. 数据透视表

```python
# 基础透视表
pivot = pd.pivot_table(df, values='value_column', 
                       index='row_column', 
                       columns='column_column',
                       aggfunc='mean')

# 多个聚合函数
pivot = pd.pivot_table(df, values='value_column',
                       index='row_column',
                       columns='column_column',
                       aggfunc=['mean', 'std', 'count'])

# 多级索引
pivot = pd.pivot_table(df, values='value_column',
                       index=['row_column1', 'row_column2'],
                       columns=['column_column1', 'column_column2'])

# 填充缺失值
pivot = pd.pivot_table(df, values='value_column',
                       index='row_column',
                       columns='column_column',
                       aggfunc='mean',
                       fill_value=0)

# 总计
pivot = pd.pivot_table(df, values='value_column',
                       index='row_column',
                       columns='column_column',
                       aggfunc='mean',
                       margins=True,
                       margins_name='Total')

# crosstab（列联表）
pd.crosstab(df['column1'], df['column2'])
pd.crosstab(df['column1'], df['column2'], normalize='index')  # 行百分比
pd.crosstab(df['column1'], df['column2'], normalize='columns')  # 列百分比
```

### 4. 时间序列分析

```python
# 创建时间序列
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# 重采样
df.resample('D').mean()  # 日均值
df.resample('W').sum()  # 周总和
df.resample('M').last()  # 月末值
df.resample('Q').mean()  # 季度均值

# 滚动统计
df['column'].rolling(window=7).mean()  # 7天移动平均
df['column'].rolling(window=30).std()  # 30天滚动标准差
df['column'].rolling(window=7, min_periods=1).sum()  # 最小周期为1

# 扩展统计
df['column'].expanding().mean()  # 累积平均
df['column'].expanding().sum()  # 累积和

# 时间差
df['time_diff'] = df['date_column'].diff()
df['time_diff_days'] = df['time_diff'].dt.days

# 时间特征提取
df['year'] = df.index.year
df['month'] = df.index.month
df['day'] = df.index.day
df['weekday'] = df.index.weekday
df['hour'] = df.index.hour
df['is_weekend'] = df.index.weekday >= 5
```

### 5. 相关性分析

```python
# 相关系数矩阵
df.corr()

# 单列相关性
df['column1'].corr(df['column2'])

# Spearman 相关性（非线性）
df.corr(method='spearman')

# Kendall 相关性
df.corr(method='kendall')

# 相关系数显著性检验
from scipy import stats
corr, p_value = stats.pearsonr(df['column1'], df['column2'])

# 可视化相关性
import seaborn as sns
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
```

### 6. 假设检验

```python
from scipy import stats

# t 检验（两组均值比较）
t_stat, p_value = stats.ttest_ind(group1, group2)

# 配对 t 检验
t_stat, p_value = stats.ttest_rel(group1, group2)

# 单样本 t 检验
t_stat, p_value = stats.ttest_1samp(sample, popmean)

# 卡方检验（分类变量关联性）
chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)

# ANOVA（多组均值比较）
f_stat, p_value = stats.f_oneway(group1, group2, group3)

# 正态性检验
stat, p_value = stats.shapiro(df['column'])  # Shapiro-Wilk 检验
stat, p_value = stats.normaltest(df['column'])  # D'Agostino 检验

# 秩和检验（非参数）
stat, p_value = stats.mannwhitneyu(group1, group2)
```

### 7. 数据过滤与选择

```python
# 条件过滤
df[df['column'] > 0]
df[(df['column1'] > 0) & (df['column2'] < 10)]
df[df['column'].isin([1, 2, 3])]
df[~df['column'].isin([1, 2, 3])]  # 不在列表中

# 字符串过滤
df[df['text'].str.contains('keyword')]
df[df['text'].str.startswith('prefix')]
df[df['text'].str.endswith('suffix')]

# 索引过滤
df.loc[df['column'] > 0, ['column1', 'column2']]
df.iloc[:100]  # 前100行

# 重复值过滤
df.drop_duplicates(subset=['column'])

# Top N
df.nlargest(10, 'column')
df.nsmallest(10, 'column')
```

### 8. 数据转换

```python
# 排序
df.sort_values('column')
df.sort_values(['column1', 'column2'], ascending=[True, False])

# 随机抽样
df.sample(frac=0.1)  # 随机抽样10%
df.sample(n=100)  # 随机抽样100行

# 分层抽样
from sklearn.model_selection import train_test_split
train, test = train_test_split(df, test_size=0.2, stratify=df['category'])

# 交叉表
pd.crosstab(df['column1'], df['column2'])

# 熔融（宽表转长表）
pd.melt(df, id_vars=['id'], value_vars=['col1', 'col2'])

# 透视（长表转宽表）
pd.pivot(df, index='id', columns='variable', values='value')
```

## 最佳实践

| 实践 | 说明 |
|------|------|
| 先探索 | 使用 `describe()` 和 `info()` 快速了解数据 |
| 可视化 | 结合图表验证分析结果 |
| 分组分析 | 使用 `groupby` 深入了解不同组别差异 |
| 时间序列 | 注意时间索引的设置和重采样频率 |
| 相关性 | 区分相关性和因果性 |

## 快速分析模板

```python
def quick_analysis(df):
    """快速数据分析模板"""
    print("=== 数据概览 ===")
    print(df.info())
    print("\n=== 描述性统计 ===")
    print(df.describe())
    print("\n=== 缺失值 ===")
    print(df.isnull().sum())
    print("\n=== 相关性 ===")
    print(df.corr())
    return df
```

## 相关链接
- [[temp_data_cleaning|数据清洗]]
- [[temp_data_visualization|数据可视化]]
- [[temp_ml_pipeline|ML 全流程]]