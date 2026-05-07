---
type: cookbook
topic: data_cleaning
category: data_science
difficulty: intermediate
prerequisites: [[temp_data_acquisition]]
acm_relevant: false
created: 2026-02-20
status: complete
---

# 数据清洗与预处理

> 快速参考：缺失值、异常值、重复值处理和数据规范化

## 核心概念

数据清洗是数据科学中最耗时的环节，通常占项目 60-80% 的时间。

## 快速参考

### 1. 缺失值处理

```python
import pandas as pd
import numpy as np

# 检测缺失值
df.isnull().sum()  # 每列的缺失值数量
df.isnull().mean()  # 缺失值比例

# 删除缺失值
df.dropna()  # 删除包含缺失值的行
df.dropna(axis=1)  # 删除包含缺失值的列
df.dropna(subset=['column1', 'column2'])  # 指定列检查
df.dropna(thresh=2)  # 至少有 2 个非缺失值才保留

# 填充缺失值
df.fillna(0)  # 填充 0
df.fillna(df.mean())  # 用均值填充
df.fillna(df.median())  # 用中位数填充
df.fillna(method='ffill')  # 前向填充
df.fillna(method='bfill')  # 后向填充

# 分列填充
df['column'].fillna(df['column'].mean(), inplace=True)

# 插值法填充
df['column'].interpolate(method='linear')

# 标记缺失值
df['column_is_missing'] = df['column'].isnull()
```

### 2. 重复值处理

```python
# 检测重复值
df.duplicated().sum()  # 重复值数量

# 删除重复值
df.drop_duplicates()  # 删除完全重复的行
df.drop_duplicates(subset=['column1'])  # 基于指定列删除
df.drop_duplicates(keep='first')  # 保留第一个
df.drop_duplicates(keep='last')  # 保留最后一个

# 统计重复值
df['column'].value_counts()
```

### 3. 异常值检测与处理

```python
import numpy as np

# Z-score 方法
from scipy import stats
z_scores = np.abs(stats.zscore(df['numeric_column']))
threshold = 3
outliers = z_scores > threshold

# IQR 方法（推荐）
Q1 = df['numeric_column'].quantile(0.25)
Q3 = df['numeric_column'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = (df['numeric_column'] < lower_bound) | (df['numeric_column'] > upper_bound)

# 处理异常值
df_clean = df[(df['numeric_column'] >= lower_bound) & (df['numeric_column'] <= upper_bound)]

# 削尾处理（保留中间 95%）
lower = df['numeric_column'].quantile(0.025)
upper = df['numeric_column'].quantile(0.975)
df['numeric_column'] = df['numeric_column'].clip(lower, upper)

# 用中位数替换异常值
median = df['numeric_column'].median()
df.loc[outliers, 'numeric_column'] = median
```

### 4. 数据类型转换

```python
# 类型转换
df['column'] = df['column'].astype(int)  # 转整数
df['column'] = df['column'].astype(float)  # 转浮点
df['column'] = df['column'].astype(str)  # 转字符串

# 日期转换
df['date_column'] = pd.to_datetime(df['date_column'])
df['year'] = df['date_column'].dt.year
df['month'] = df['date_column'].dt.month
df['day'] = df['date_column'].dt.day
df['weekday'] = df['date_column'].dt.weekday

# 分类数据转换
df['category_column'] = df['category_column'].astype('category')

# 智能转换
df = df.convert_dtypes()  # 自动推断最佳类型
```

### 5. 字符串清洗

```python
# 去除空格
df['text'] = df['text'].str.strip()  # 去除首尾空格
df['text'] = df['text'].str.replace(' ', '')  # 去除所有空格

# 大小写转换
df['text'] = df['text'].str.lower()  # 转小写
df['text'] = df['text'].str.upper()  # 转大写
df['text'] = df['text'].str.title()  # 首字母大写

# 替换
df['text'] = df['text'].str.replace('old', 'new')

# 提取
df['text'].str.extract(r'(\d+)')  # 提取数字
df['text'].str.split(' ', expand=True)  # 分割字符串

# 去除特殊字符
import re
df['text'] = df['text'].apply(lambda x: re.sub(r'[^\w\s]', '', str(x)))
```

### 6. 数据规范化

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# 标准化（Z-score）
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['column1', 'column2']])

# 归一化（0-1）
scaler = MinMaxScaler()
df_normalized = scaler.fit_transform(df[['column1', 'column2']])

# 鲁棒缩放（对异常值不敏感）
scaler = RobustScaler()
df_robust = scaler.fit_transform(df[['column1', 'column2']])

# 对数变换（处理偏态数据）
df['log_column'] = np.log1p(df['column'])  # log(1+x) 避免 log(0)

# Box-Cox 变换
from scipy import stats
df['boxcox_column'], _ = stats.boxcox(df['column'])
```

### 7. 特征编码

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# 标签编码（有序）
le = LabelEncoder()
df['encoded_column'] = le.fit_transform(df['category_column'])

# 独热编码（无序）
df_encoded = pd.get_dummies(df, columns=['category_column'])

# OneHotEncoder
encoder = OneHotEncoder()
encoded = encoder.fit_transform(df[['category_column']]).toarray()
```

### 8. 数据一致性检查

```python
# 检查数据范围
df.describe()

# 检查唯一值
df['column'].unique()
df['column'].nunique()

# 检查数据分布
df['column'].hist()

# 检查相关性
df.corr()

# 检查数据完整性
df.info()
```

## 最佳实践

| 实践 | 说明 |
|------|------|
| 先备份 | 清洗前先备份原始数据 `df_backup = df.copy()` |
| 处理顺序 | 缺失值 → 重复值 → 异常值 → 类型转换 → 规范化 |
| 记录操作 | 记录每一步清洗操作，便于追溯 |
| 可视化检查 | 清洗前后可视化对比 |
| 自动化脚本 | 将清洗流程写成函数，便于复用 |

## 快速清洗模板

```python
def clean_data(df):
    """快速数据清洗模板"""
    # 1. 备份
    df_clean = df.copy()
    
    # 2. 处理缺失值
    df_clean = df_clean.fillna(df_clean.mean())
    
    # 3. 删除重复值
    df_clean = df_clean.drop_duplicates()
    
    # 4. 处理异常值（IQR 方法）
    for col in df_clean.select_dtypes(include=[np.number]).columns:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        df_clean = df_clean[(df_clean[col] >= Q1 - 1.5*IQR) & 
                            (df_clean[col] <= Q3 + 1.5*IQR)]
    
    # 5. 类型转换
    df_clean['date_column'] = pd.to_datetime(df_clean['date_column'])
    
    return df_clean
```

## 相关链接
- [[temp_data_acquisition|数据获取]]
- [[temp_data_analysis|数据分析]]
- [[temp_ml_pipeline|ML 全流程]]