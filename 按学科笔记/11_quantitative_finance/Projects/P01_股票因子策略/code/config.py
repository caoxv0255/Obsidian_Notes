"""
配置文件
"""

# 数据库配置
DB_PATH = 'data/stocks.db'

# 策略配置
STRATEGY_CONFIG = {
    'rebalance_freq': 'monthly',  # 调仓频率
    'top_n': 10,                   # 选股数量
    'position_size': 0.1,          # 单个股票仓位（10%）
    'transaction_cost': 0.001,     # 交易成本（0.1%）
}

# 因子权重配置
FACTOR_WEIGHTS = {
    'momentum': 0.25,
    'reversal': 0.15,
    'volatility': 0.15,
    'liquidity': 0.10,
    'pe_ratio': 0.15,
    'pb_ratio': 0.10,
    'roe': 0.05,
    'turnover_rate': 0.05,
}

# 回测配置
BACKTEST_CONFIG = {
    'start_date': '2021-01-01',
    'end_date': '2023-12-31',
    'initial_capital': 1000000,
    'benchmark': '000300.SH',  # 沪深300
}