# 03 Pandas数据处理

## 目录

- [1. Pandas简介](#1-pandas简介)
- [2. Series数据结构](#2-series数据结构)
- [3. DataFrame数据结构](#3-dataframe数据结构)
- [4. 数据读取与存储](#4-数据读取与存储)
- [5. 数据选择与切片](#5-数据选择与切片)
- [6. 数据清洗](#6-数据清洗)
- [7. 分组与聚合](#7-分组与聚合)
- [8. 金融数据处理实战](#8-金融数据处理实战)

---

## 1. Pandas简介

**Pandas** 是 Python 中最常用的数据处理库，提供了高性能、易用的数据结构和数据分析工具。在量化交易中，Pandas 是处理时间序列数据的核心工具。

**核心数据结构**：
- `Series`：一维带标签的数组
- `DataFrame`：二维带标签的表格数据（类似 Excel/数据库表）

**导入约定**：

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 10)  # 显示更多列
pd.set_option('display.width', 200)      # 显示更宽
```

---

## 2. Series数据结构

### 2.1 创建Series

```python
# 从列表创建
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)
# a    10
# b    20
# c    30
# d    40
# dtype: int64

# 从字典创建
s2 = pd.Series({'苹果': 3.5, '香蕉': 2.0, '橙子': 4.0})
print(s2)
# 苹果    3.5
# 香蕉    2.0
# 橙子    4.0
# dtype: float64

# 从标量创建
s3 = pd.Series(5, index=['x', 'y', 'z'])  # 所有值都是5
```

### 2.2 Series基本操作

```python
# 索引和标签
print(s['b'])      # 20
print(s[1])        # 20（位置索引）

# 切片
print(s['a':'c'])  # 包含两端
# a    10
# b    20
# c    30

# 布尔索引
print(s[s > 25])   # 筛选大于25的值
# c    30
# d    40

# 数学运算
print(s * 2)       # 逐元素乘法
print(s + 100)     # 逐元素加法

# 统计方法
print(s.sum())     # 求和
print(s.mean())    # 均值
print(s.std())     # 标准差
print(s.describe()) # 描述性统计
```

---

## 3. DataFrame数据结构

### 3.1 创建DataFrame

```python
# 从字典创建（最常用）
df = pd.DataFrame({
    '日期': ['2024-01-01', '2024-01-02', '2024-01-03'],
    '开盘价': [100.0, 101.5, 102.3],
    '收盘价': [101.0, 102.2, 103.5],
    '成交量': [10000, 12000, 15000]
})
print(df)
#          日期    开盘价    收盘价     成交量
# 0  2024-01-01   100.0   101.0   10000
# 1  2024-01-02   101.5   102.2   12000
# 2  2024-01-03   102.3   103.5   15000

# 设置日期为索引
df['日期'] = pd.to_datetime(df['日期'])
df.set_index('日期', inplace=True)
print(df)
#              开盘价    收盘价     成交量
# 日期
# 2024-01-01   100.0   101.0   10000
# 2024-01-02   101.5   102.2   12000
# 2024-01-03   102.3   103.5   15000
```

### 3.2 DataFrame基本属性

```python
print(df.shape)      # (3, 3) - 行数、列数
print(df.columns)    # 列名索引
print(df.index)      # 行索引（日期）
print(df.dtypes)     # 每列数据类型
print(df.head(2))    # 前2行
print(df.tail(2))    # 后2行
print(df.info())     # 数据概览
print(df.describe()) # 数值列描述性统计
```

---

## 4. 数据读取与存储

### 4.1 读取常见格式

```python
# CSV（最常用）
df = pd.read_csv('stock_data.csv', parse_dates=['日期'], index_col='日期')

# Excel
df = pd.read_excel('financial_data.xlsx', sheet_name='季度数据')

# 从URL读取
df = pd.read_csv('https://raw.githubusercontent.com/datasets/s-and-p-500/main/data/constituents.csv')

# Parquet（高效压缩格式，适合大数据）
df = pd.read_parquet('data.parquet')

# 从SQL数据库读取
# df = pd.read_sql('SELECT * FROM stock_prices', connection)

# 读取多个CSV文件并合并
import glob
csv_files = glob.glob('data/*.csv')
df_list = [pd.read_csv(f) for f in csv_files]
df = pd.concat(df_list, ignore_index=True)
```

### 4.2 保存数据

```python
# 保存为CSV
df.to_csv('output.csv', encoding='utf-8-sig')  # utf-8-sig 支持Excel中文

# 保存为Excel
df.to_excel('output.xlsx', sheet_name='Sheet1')

# 保存为Parquet（推荐，更小更快）
df.to_parquet('output.parquet')

# 保存为JSON
df.to_json('output.json', orient='records', date_format='iso')
```

---

## 5. 数据选择与切片

### 5.1 选择列

```python
# 单列 → Series
close_prices = df['收盘价']

# 多列 → DataFrame
subset = df[['开盘价', '收盘价']]

# 使用loc（标签索引）和iloc（位置索引）
print(df.loc['2024-01-02'])           # 选择一行（返回Series）
print(df.loc['2024-01-01':'2024-01-03'])  # 切片（包含两端）

print(df.iloc[0])                     # 第1行
print(df.iloc[0:3])                    # 前3行

# 条件选择
print(df[df['收盘价'] > 102])          # 收盘价大于102的行
print(df[(df['收盘价'] > 101) & (df['成交量'] > 11000)])  # 多条件
```

### 5.2 高级索引

```python
# query方法（更直观的SQL风格）
print(df.query('收盘价 > 102 and 成交量 > 11000'))

# 字符串包含
# df[df['股票代码'].str.contains('SH')]

# 索引查找
# idxmax / idxmin：返回最大/最小值的索引标签
print(df['收盘价'].idxmax())  # 收盘价最高那天的日期

# 切片与条件结合
df['2024-01':'2024-03']['收盘价']['收盘价 > 101']
```

---

## 6. 数据清洗

### 6.1 缺失值处理

```python
# 检测缺失值
print(df.isnull())          # 返回布尔DataFrame
print(df.isnull().sum())    # 每列缺失值数量
print(df.dropna())          # 删除有缺失值的行

# 填充缺失值
df.fillna(method='ffill')  # 前向填充（用前一个值填）
df.fillna(method='bfill')  # 后向填充
df.fillna(df.mean())       # 用均值填充
df.fillna({'开盘价': 100, '收盘价': 100})  # 按列指定值

# 插值
df['收盘价'].interpolate(method='linear')  # 线性插值
```

### 6.2 重复值与异常值

```python
# 去除重复
df.drop_duplicates(inplace=True)

# 异常值检测（IQR方法）
Q1 = df['收盘价'].quantile(0.25)
Q3 = df['收盘价'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_clean = df[(df['收盘价'] >= lower_bound) & (df['收盘价'] <= upper_bound)]

# Z-score方法（标准差方法）
from scipy import stats
z_scores = np.abs(stats.zscore(df['收盘价']))
df_clean = df[z_scores < 3]  # 删除Z-score > 3的异常值
```

### 6.3 数据类型转换

```python
# 转换类型
df['成交量'] = df['成交量'].astype(int)

# 字符串处理
df['股票代码'] = df['股票代码'].str.upper()  # 转大写
df['股票代码'] = df['股票代码'].str.strip()   # 去空格

# 正则提取
# df['行业'] = df['公司名'].str.extract(r'-(.*)-')
```

---

## 7. 分组与聚合

### 7.1 groupby基础

```python
# 按单列分组
grouped = df.groupby('行业')['收盘价'].mean()

# 按多列分组
grouped = df.groupby(['行业', '年份'])['成交量'].sum()

# 多个聚合函数
result = df.groupby('行业').agg({
    '收盘价': ['mean', 'max', 'min', 'std'],
    '成交量': ['sum', 'count']
})
```

### 7.2 金融数据聚合示例

```python
# 按月聚合股票数据
df_monthly = df.resample('M').agg({
    '开盘价': 'first',      # 月初开盘价
    '收盘价': 'last',       # 月末收盘价
    '最高价': 'max',        # 月最高价
    '最低价': 'min',        # 月最低价
    '成交量': 'sum'         # 月总成交量
})

# 计算月收益率
df_monthly['月收益率'] = df_monthly['收盘价'].pct_change() * 100

# 按季度聚合
df_quarterly = df.resample('Q')[['收盘价', '成交量']].agg({'收盘价': 'last', '成交量': 'sum'})
```

---

## 8. 金融数据处理实战

### 8.1 计算收益率序列

```python
# 对数收益率（金融中更常用）
df['log_return'] = np.log(df['收盘价'] / df['收盘价'].shift(1))

# 简单收益率
df['simple_return'] = df['收盘价'].pct_change()

# 滚动收益率（过去N天）
df['rolling_5d_return'] = df['收盘价'].pct_change(5)

# 年化收益率（假设252个交易日）
annualized_return = df['log_return'].mean() * 252
annualized_vol = df['log_return'].std() * np.sqrt(252)
print(f"年化收益率: {annualized_return:.2%}")
print(f"年化波动率: {annualized_vol:.2%}")
```

### 8.2 移动平均线计算

```python
# 简单移动平均（SMA）
df['MA5'] = df['收盘价'].rolling(window=5).mean()
df['MA20'] = df['收盘价'].rolling(window=20).mean()
df['MA60'] = df['收盘价'].rolling(window=60).mean()

# 指数移动平均（EMA，对近期更敏感）
df['EMA12'] = df['收盘价'].ewm(span=12).mean()
df['EMA26'] = df['收盘价'].ewm(span=26).mean()

# MACD
df['MACD'] = df['EMA12'] - df['EMA26']
df['MACD_signal'] = df['MACD'].ewm(span=9).mean()

# 布林带（Bollinger Bands）
df['BB_middle'] = df['收盘价'].rolling(window=20).mean()
BB_std = df['收盘价'].rolling(window=20).std()
df['BB_upper'] = df['BB_middle'] + 2 * BB_std
df['BB_lower'] = df['BB_middle'] - 2 * BB_std
```

### 8.3 交易信号生成

```python
# 金叉/死叉策略
df['signal'] = 0
df.loc[df['MA5'] > df['MA20'], 'signal'] = 1   # 金叉买入
df.loc[df['MA5'] <= df['MA20'], 'signal'] = -1  # 死叉卖出

# 计算持仓（signal的滞后一期，避免未来函数）
df['position'] = df['signal'].shift(1)

# 计算策略收益
df['strategy_return'] = df['position'] * df['log_return']

# 累计收益曲线
df['cumulative_market'] = (1 + df['log_return']).cumprod()
df['cumulative_strategy'] = (1 + df['strategy_return']).cumprod()

# 可视化
plt.figure(figsize=(14, 8))
plt.plot(df.index, df['cumulative_market'], label='买入持有', linewidth=2)
plt.plot(df.index, df['cumulative_strategy'], label='MA5/20策略', linewidth=2)
plt.title('策略累计收益对比')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

## 📝 小结

| 功能 | 关键函数 |
|------|----------|
| 数据读取 | `pd.read_csv()`, `pd.read_excel()` |
| 数据选择 | `df[]`, `.loc[]`, `.iloc[]`, `.query()` |
| 缺失值处理 | `.isnull()`, `.fillna()`, `.interpolate()` |
| 分组聚合 | `.groupby()`, `.resample()`, `.agg()` |
| 金融指标 | `pct_change()`, `rolling()`, `ewm()` |
| 收益率计算 | `np.log(P/P_prev)` |

> 💡 **量化提示**：Pandas是量化策略研发的基石。建议熟练掌握`groupby`、`resample`、`rolling`三大核心操作，它们构成了大多数因子计算的基础。

---

*本笔记为Python编程系列第三部分，前置内容：01_Python基础语法、02_科学计算入门*
