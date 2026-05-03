---
type: cookbook
topic: data_acquisition
category: data_science
difficulty: beginner
prerequisites: []
acm_relevant: false
created: 2026-02-20
status: complete
---

# 数据获取与导入

> 快速参考：各种数据源的读取方法和常用操作

## 核心概念

数据获取是数据科学项目的第一步，包括从文件、数据库、API 等多种来源导入数据。

## 快速参考

### 1. 读取 CSV 文件

```python
import pandas as pd

# 基础读取
df = pd.read_csv('data.csv')

# 指定编码（处理中文）
df = pd.read_csv('data.csv', encoding='utf-8')

# 指定分隔符
df = pd.read_csv('data.csv', sep=',')

# 读取指定列
df = pd.read_csv('data.csv', usecols=['column1', 'column2'])

# 跳过行
df = pd.read_csv('data.csv', skiprows=1)  # 跳过第一行

# 读取前 N 行
df = pd.read_csv('data.csv', nrows=1000)

# 处理缺失值
df = pd.read_csv('data.csv', na_values=['NA', 'null', 'NaN'])
```

### 2. 读取 Excel 文件

```python
import pandas as pd

# 读取 Excel
df = pd.read_excel('data.xlsx')

# 指定工作表
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# 读取多个工作表
sheets = pd.read_excel('data.xlsx', sheet_name=['Sheet1', 'Sheet2'])

# 指定列
df = pd.read_excel('data.xlsx', usecols='A:C')
```

### 3. 读取 JSON 文件

```python
import pandas as pd

# 读取 JSON
df = pd.read_json('data.json')

# 处理嵌套 JSON
df = pd.read_json('data.json', orient='records')

# 从 URL 读取 JSON
df = pd.read_json('https://api.example.com/data.json')
```

### 4. 数据库连接

```python
import pandas as pd
import sqlite3

# SQLite
conn = sqlite3.connect('database.db')
df = pd.read_sql('SELECT * FROM table', conn)
conn.close()

# MySQL
import pymysql
conn = pymysql.connect(host='localhost', user='user', password='pass', database='db')
df = pd.read_sql('SELECT * FROM table', conn)

# PostgreSQL
import psycopg2
conn = psycopg2.connect(host='localhost', database='db', user='user', password='pass')
df = pd.read_sql('SELECT * FROM table', conn)
```

### 5. API 数据获取

```python
import requests
import pandas as pd

# GET 请求
response = requests.get('https://api.example.com/data')
data = response.json()
df = pd.DataFrame(data)

# 带参数的请求
params = {'param1': 'value1', 'param2': 'value2'}
response = requests.get('https://api.example.com/data', params=params)

# POST 请求
payload = {'key': 'value'}
response = requests.post('https://api.example.com/data', json=payload)

# 处理分页
all_data = []
page = 1
while True:
    response = requests.get(f'https://api.example.com/data?page={page}')
    data = response.json()
    if not data:
        break
    all_data.extend(data)
    page += 1
df = pd.DataFrame(all_data)
```

### 6. 爬虫获取数据

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 简单爬虫
url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 提取数据
data = []
items = soup.find_all('div', class_='item')
for item in items:
    title = item.find('h2').text
    price = item.find('span', class_='price').text
    data.append({'title': title, 'price': price})

df = pd.DataFrame(data)
```

### 7. 大数据格式

```python
import pandas as pd

# Parquet（推荐，高性能）
df = pd.read_parquet('data.parquet')
df.to_parquet('output.parquet')

# Feather（快速读写）
df = pd.read_feather('data.feather')
df.to_feather('output.feather')

# HDF5（适合大数据）
df = pd.read_hdf('data.h5', key='df')
df.to_hdf('output.h5', key='df')
```

### 8. 实时数据流

```python
import pandas as pd

# 监控文件变化（伪代码）
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CSVHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.csv'):
            df = pd.read_csv(event.src_path)
            # 处理数据
            process_data(df)

observer = Observer()
observer.schedule(CSVHandler(), path='.')
observer.start()
```

## 最佳实践

| 实践 | 说明 |
|------|------|
| 指定编码 | 处理中文数据时指定 `encoding='utf-8'` 或 `encoding='gbk'` |
| 使用 chunksize | 大文件使用 `pd.read_csv(chunksize=10000)` 分块读取 |
| 指定列类型 | 使用 `dtype` 参数提高读取性能 |
| 关闭连接 | 数据库操作后记得 `conn.close()` 或使用 `with` 语句 |
| 错误处理 | API 调用使用 try-except 处理网络异常 |
| 缓存数据 | 重复获取的数据使用 parquet/feather 缓存 |

## 常见问题

**Q: CSV 文件太大无法一次性读取？**
```python
# 分块读取
chunk_iter = pd.read_csv('large_file.csv', chunksize=10000)
for chunk in chunk_iter:
    process(chunk)
```

**Q: 日期格式错误？**
```python
df = pd.read_csv('data.csv', parse_dates=['date_column'])
df['date_column'] = pd.to_datetime(df['date_column'])
```

## 相关链接
- [[temp_data_cleaning|数据清洗]]
- [[temp_data_analysis|数据分析]]