---
type: case_study
topic: finance_analysis
category: case_studies
difficulty: advanced
prerequisites: [[temp_data_acquisition, temp_data_cleaning, temp_data_analysis, temp_data_visualization]]
acm_relevant: false
created: 2026-02-20
status: complete
---

# 金融分析案例

> 端到端金融数据分析：股票数据处理、技术指标计算、收益率分析和风险评估

## 案例目标

构建一个完整的股票分析系统，包括数据获取、技术指标计算、收益率分析、风险评估和投资组合优化。

## 数据获取

```python
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 获取股票数据
def get_stock_data(symbol, start_date, end_date):
    """获取股票历史数据"""
    stock = yf.Ticker(symbol)
    df = stock.history(start=start_date, end=end_date)
    return df

# 示例：获取苹果公司股票数据
df = get_stock_data('AAPL', '2020-01-01', '2024-12-31')
print(df.head())
```

## 数据清洗

```python
def clean_stock_data(df):
    """清洗股票数据"""
    # 删除缺失值
    df = df.dropna()
    
    # 重置索引
    df = df.reset_index()
    
    # 转换日期格式
    df['Date'] = pd.to_datetime(df['Date'])
    
    # 添加日期特征
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['Weekday'] = df['Date'].dt.weekday
    
    return df

df_clean = clean_stock_data(df)
```

## 技术指标计算

```python
def calculate_technical_indicators(df):
    """计算技术指标"""
    
    # 移动平均线
    df['MA5'] = df['Close'].rolling(window=5).mean()
    df['MA10'] = df['Close'].rolling(window=10).mean()
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA60'] = df['Close'].rolling(window=60).mean()
    
    # MACD (Moving Average Convergence Divergence)
    exp12 = df['Close'].ewm(span=12, adjust=False).mean()
    exp26 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = exp12 - exp26
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    df['Histogram'] = df['MACD'] - df['Signal']
    
    # RSI (Relative Strength Index)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # 布林带
    df['BB_Middle'] = df['Close'].rolling(window=20).mean()
    bb_std = df['Close'].rolling(window=20).std()
    df['BB_Upper'] = df['BB_Middle'] + 2 * bb_std
    df['BB_Lower'] = df['BB_Middle'] - 2 * bb_std
    
    # 成交量移动平均
    df['Volume_MA5'] = df['Volume'].rolling(window=5).mean()
    df['Volume_MA20'] = df['Volume'].rolling(window=20).mean()
    
    return df

df_with_indicators = calculate_technical_indicators(df_clean)
```

## 收益率计算

```python
def calculate_returns(df):
    """计算收益率"""
    
    # 日收益率
    df['Daily_Return'] = df['Close'].pct_change()
    
    # 对数收益率
    df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
    
    # 累积收益率
    df['Cumulative_Return'] = (1 + df['Daily_Return']).cumprod() - 1
    
    # 涨跌幅
    df['Price_Change'] = df['Close'] - df['Close'].shift(1)
    df['Percent_Change'] = df['Price_Change'] / df['Close'].shift(1) * 100
    
    return df

df_with_returns = calculate_returns(df_with_indicators)
```

## 风险评估

```python
def calculate_risk_metrics(df):
    """计算风险指标"""
    
    # 年化波动率
    daily_volatility = df['Daily_Return'].std()
    annual_volatility = daily_volatility * np.sqrt(252)
    
    # 最大回撤
    df['Cumulative_Max'] = df['Close'].cummax()
    df['Drawdown'] = (df['Close'] - df['Cumulative_Max']) / df['Cumulative_Max']
    max_drawdown = df['Drawdown'].min()
    
    # 夏普比率
    risk_free_rate = 0.02  # 假设无风险利率 2%
    annual_return = df['Daily_Return'].mean() * 252
    sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility
    
    # VaR (Value at Risk) - 95% 置信水平
    var_95 = df['Daily_Return'].quantile(0.05)
    
    # CVaR (Conditional VaR)
    cvar_95 = df[df['Daily_Return'] <= var_95]['Daily_Return'].mean()
    
    metrics = {
        'Annual_Volatility': annual_volatility,
        'Max_Drawdown': max_drawdown,
        'Sharpe_Ratio': sharpe_ratio,
        'VaR_95': var_95,
        'CVaR_95': cvar_95,
        'Annual_Return': annual_return
    }
    
    return metrics

risk_metrics = calculate_risk_metrics(df_with_returns)
print("风险指标:")
for metric, value in risk_metrics.items():
    print(f"{metric}: {value:.4f}")
```

## 数据可视化

```python
def plot_stock_analysis(df):
    """绘制股票分析图表"""
    
    fig, axes = plt.subplots(3, 2, figsize=(15, 12))
    
    # 1. 价格和移动平均线
    axes[0, 0].plot(df['Date'], df['Close'], label='Close Price', linewidth=1)
    axes[0, 0].plot(df['Date'], df['MA20'], label='MA20', linewidth=1)
    axes[0, 0].plot(df['Date'], df['MA60'], label='MA60', linewidth=1)
    axes[0, 0].set_title('Price and Moving Averages')
    axes[0, 0].legend()
    axes[0, 0].grid(True)
    
    # 2. MACD
    axes[0, 1].plot(df['Date'], df['MACD'], label='MACD', linewidth=1)
    axes[0, 1].plot(df['Date'], df['Signal'], label='Signal', linewidth=1)
    axes[0, 1].bar(df['Date'], df['Histogram'], label='Histogram', alpha=0.3)
    axes[0, 1].set_title('MACD')
    axes[0, 1].legend()
    axes[0, 1].grid(True)
    
    # 3. RSI
    axes[1, 0].plot(df['Date'], df['RSI'], linewidth=1)
    axes[1, 0].axhline(y=70, color='r', linestyle='--', label='Overbought')
    axes[1, 0].axhline(y=30, color='g', linestyle='--', label='Oversold')
    axes[1, 0].set_title('RSI')
    axes[1, 0].legend()
    axes[1, 0].grid(True)
    
    # 4. 布林带
    axes[1, 1].plot(df['Date'], df['Close'], label='Close', linewidth=1)
    axes[1, 1].plot(df['Date'], df['BB_Upper'], label='BB_Upper', linewidth=1)
    axes[1, 1].plot(df['Date'], df['BB_Lower'], label='BB_Lower', linewidth=1)
    axes[1, 1].fill_between(df['Date'], df['BB_Upper'], df['BB_Lower'], alpha=0.2)
    axes[1, 1].set_title('Bollinger Bands')
    axes[1, 1].legend()
    axes[1, 1].grid(True)
    
    # 5. 累积收益率
    axes[2, 0].plot(df['Date'], df['Cumulative_Return'] * 100, linewidth=1)
    axes[2, 0].set_title('Cumulative Return (%)')
    axes[2, 0].grid(True)
    
    # 6. 回撤
    axes[2, 1].plot(df['Date'], df['Drawdown'] * 100, linewidth=1, color='red')
    axes[2, 1].fill_between(df['Date'], df['Drawdown'] * 100, 0, alpha=0.3, color='red')
    axes[2, 1].set_title('Drawdown (%)')
    axes[2, 1].grid(True)
    
    plt.tight_layout()
    plt.show()

plot_stock_analysis(df_with_returns)
```

## 投资组合优化

```python
from scipy.optimize import minimize

def optimize_portfolio(returns):
    """投资组合优化"""
    
    # 计算平均收益和协方差矩阵
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    
    # 定义目标函数（最小化风险）
    def portfolio_variance(weights, mean_returns, cov_matrix):
        return np.dot(weights.T, np.dot(cov_matrix, weights))
    
    # 约束条件
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(len(mean_returns)))
    
    # 初始权重
    num_assets = len(mean_returns)
    initial_weights = num_assets * [1. / num_assets]
    
    # 优化
    result = minimize(portfolio_variance, initial_weights,
                     args=(mean_returns, cov_matrix),
                     method='SLSQP',
                     bounds=bounds,
                     constraints=constraints)
    
    return result.x

# 示例：多股票投资组合
symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
portfolio_data = []
for symbol in symbols:
    data = get_stock_data(symbol, '2020-01-01', '2024-12-31')
    portfolio_data.append(data['Close'])

portfolio_df = pd.concat(portfolio_data, axis=1)
portfolio_df.columns = symbols
portfolio_returns = portfolio_df.pct_change().dropna()

optimal_weights = optimize_portfolio(portfolio_returns)
print("最优投资组合权重:")
for symbol, weight in zip(symbols, optimal_weights):
    print(f"{symbol}: {weight:.2%}")
```

## 交易信号生成

```python
def generate_trading_signals(df):
    """生成交易信号"""
    
    df['Signal'] = 0
    
    # MACD 金叉死叉
    df.loc[(df['MACD'] > df['Signal']) & (df['MACD'].shift(1) <= df['Signal'].shift(1)), 'Signal'] = 1
    df.loc[(df['MACD'] < df['Signal']) & (df['MACD'].shift(1) >= df['Signal'].shift(1)), 'Signal'] = -1
    
    # RSI 超买超卖
    df.loc[df['RSI'] < 30, 'Signal'] = 1  # 超卖买入
    df.loc[df['RSI'] > 70, 'Signal'] = -1  # 超买卖出
    
    # 布林带突破
    df.loc[df['Close'] < df['BB_Lower'], 'Signal'] = 1  # 下轨买入
    df.loc[df['Close'] > df['BB_Upper'], 'Signal'] = -1  # 上轨卖出
    
    return df

df_with_signals = generate_trading_signals(df_with_returns)
```

## 回测框架

```python
def backtest_strategy(df, initial_capital=100000):
    """简单回测框架"""
    
    capital = initial_capital
    position = 0
    holdings = 0
    portfolio_value = []
    
    for i in range(len(df)):
        if df.iloc[i]['Signal'] == 1 and position == 0:  # 买入信号
            holdings = capital // df.iloc[i]['Close']
            position = 1
            capital = capital - holdings * df.iloc[i]['Close']
        
        elif df.iloc[i]['Signal'] == -1 and position == 1:  # 卖出信号
            capital = capital + holdings * df.iloc[i]['Close']
            holdings = 0
            position = 0
        
        portfolio_value.append(capital + holdings * df.iloc[i]['Close'])
    
    df['Portfolio_Value'] = portfolio_value
    df['Strategy_Return'] = df['Portfolio_Value'].pct_change()
    
    # 计算策略表现
    strategy_return = (portfolio_value[-1] - initial_capital) / initial_capital
    buy_and_hold_return = (df.iloc[-1]['Close'] - df.iloc[0]['Close']) / df.iloc[0]['Close']
    
    print(f"策略收益率: {strategy_return:.2%}")
    print(f"买入持有收益率: {buy_and_hold_return:.2%}")
    
    return df

backtest_results = backtest_strategy(df_with_signals)
```

## 完整分析流程

```python
def full_financial_analysis(symbol, start_date, end_date):
    """完整金融分析流程"""
    
    # 1. 数据获取
    df = get_stock_data(symbol, start_date, end_date)
    
    # 2. 数据清洗
    df = clean_stock_data(df)
    
    # 3. 计算技术指标
    df = calculate_technical_indicators(df)
    
    # 4. 计算收益率
    df = calculate_returns(df)
    
    # 5. 风险评估
    risk_metrics = calculate_risk_metrics(df)
    print("风险指标:", risk_metrics)
    
    # 6. 生成交易信号
    df = generate_trading_signals(df)
    
    # 7. 回测
    df = backtest_strategy(df)
    
    # 8. 可视化
    plot_stock_analysis(df)
    
    return df

# 运行完整分析
results = full_financial_analysis('AAPL', '2020-01-01', '2024-12-31')
```

## 最佳实践

| 实践 | 说明 |
|------|------|
| 数据验证 | 检查数据完整性和异常值 |
| 避免未来函数 | 严格按时间顺序计算指标 |
| 风险管理 | 设置止损和仓位管理 |
| 样本外测试 | 使用不同时间段验证策略 |
| 交易成本 | 考虑手续费和滑点 |

## 相关链接
- [[temp_data_acquisition|数据获取]]
- [[temp_data_analysis|数据分析]]
- [[temp_ml_pipeline|ML 全流程]]