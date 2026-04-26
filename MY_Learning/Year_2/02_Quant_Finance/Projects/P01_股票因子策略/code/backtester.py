"""
回测引擎
"""
import pandas as pd
import numpy as np
from datetime import datetime

class Backtester:
    """回测引擎"""

    def __init__(self, initial_capital=1000000, transaction_cost=0.001):
        """
        初始化回测引擎

        参数:
            initial_capital: 初始资金
            transaction_cost: 交易成本（比例）
        """
        self.initial_capital = initial_capital
        self.transaction_cost = transaction_cost

        # 回测状态
        self.capital = initial_capital
        self.positions = {}  # {股票代码: 持仓数量}
        self.cash = initial_capital

        # 交易记录
        self.trades = []
        self.daily_values = []

    def execute_trades(self, trades, prices, date):
        """
        执行交易

        参数:
            trades: 交易指令列表
            prices: 价格字典 {股票代码: 价格}
            date: 交易日期
        """
        for trade in trades:
            stock = trade['stock']
            action = trade['action']
            quantity = trade['quantity']

            if action == 'sell' or action == 'adjust' and quantity < 0:
                # 卖出
                if stock in self.positions and self.positions[stock] > 0:
                    sell_quantity = min(abs(quantity), self.positions[stock])
                    price = prices.get(stock, 0)

                    if price > 0:
                        # 计算交易金额（扣除交易成本）
                        trade_amount = sell_quantity * price * (1 - self.transaction_cost)

                        # 更新现金和持仓
                        self.cash += trade_amount
                        self.positions[stock] -= sell_quantity

                        if self.positions[stock] == 0:
                            del self.positions[stock]

                        # 记录交易
                        self.trades.append({
                            'date': date,
                            'stock': stock,
                            'action': 'sell',
                            'quantity': sell_quantity,
                            'price': price,
                            'amount': trade_amount
                        })

            elif action == 'buy' or action == 'adjust' and quantity > 0:
                # 买入
                price = prices.get(stock, 0)

                if price > 0 and self.cash > 0:
                    # 计算可买入数量（考虑交易成本）
                    max_quantity = int(self.cash / (price * (1 + self.transaction_cost)))
                    buy_quantity = min(quantity, max_quantity)

                    if buy_quantity > 0:
                        # 计算交易金额（包含交易成本）
                        trade_amount = buy_quantity * price * (1 + self.transaction_cost)

                        # 更新现金和持仓
                        self.cash -= trade_amount
                        self.positions[stock] = self.positions.get(stock, 0) + buy_quantity

                        # 记录交易
                        self.trades.append({
                            'date': date,
                            'stock': stock,
                            'action': 'buy',
                            'quantity': buy_quantity,
                            'price': price,
                            'amount': trade_amount
                        })

    def calculate_portfolio_value(self, prices):
        """
        计算组合价值

        参数:
            prices: 价格字典 {股票代码: 价格}

        返回:
            float: 组合总价值
        """
        # 计算持仓价值
        position_value = 0.0

        for stock, quantity in self.positions.items():
            price = prices.get(stock, 0)
            position_value += quantity * price

        # 组合总价值 = 持仓价值 + 现金
        total_value = position_value + self.cash

        return total_value

    def record_daily_value(self, date, prices):
        """
        记录每日价值

        参数:
            date: 日期
            prices: 价格字典
        """
        value = self.calculate_portfolio_value(prices)

        self.daily_values.append({
            'date': date,
            'portfolio_value': value,
            'cash': self.cash,
            'positions': self.positions.copy()
        })

    def run_backtest(self, strategy, factor_df, returns_df, prices_df):
        """
        运行回测

        参数:
            strategy: 策略对象
            factor_df: 因子数据
            returns_df: 收益数据
            prices_df: 价格数据

        返回:
            dict: 回测结果
        """
        # 重置状态
        self.capital = self.initial_capital
        self.cash = self.initial_capital
        self.positions = {}
        self.trades = []
        self.daily_values = []

        # 按日期分组
        dates = factor_df.index.get_level_values(0).unique()

        for date in dates:
            # 获取当日数据
            daily_factors = factor_df.loc[date]
            daily_prices = prices_df.loc[date]

            # 计算因子得分并选股
            scores = strategy.calculate_factor_score(daily_factors)
            selected_stocks = strategy.select_stocks(scores)

            # 计算目标仓位
            target_positions = strategy.calculate_positions(
                selected_stocks,
                self.calculate_portfolio_value(daily_prices)
            )

            # 生成交易指令
            trades = strategy.generate_trades(self.positions, target_positions)

            # 执行交易
            self.execute_trades(trades, daily_prices, date)

            # 记录每日价值
            self.record_daily_value(date, daily_prices)

        # 转换为DataFrame
        values_df = pd.DataFrame(self.daily_values)
        values_df.set_index('date', inplace=True)

        # 计算收益率
        values_df['return'] = values_df['portfolio_value'].pct_change()

        return {
            'values': values_df,
            'trades': pd.DataFrame(self.trades)
        }

    def calculate_performance(self, backtest_result, benchmark_returns=None):
        """
        计算绩效指标

        参数:
            backtest_result: 回测结果
            benchmark_returns: 基准收益序列

        返回:
            dict: 绩效指标
        """
        values_df = backtest_result['values']

        # 计算收益率
        returns = values_df['return'].dropna()

        # 年化收益率
        n_days = len(returns)
        annual_return = (1 + returns.mean()) ** 252 - 1

        # 年化波动率
        annual_volatility = returns.std() * np.sqrt(252)

        # 夏普比率（假设无风险利率为3%）
        risk_free_rate = 0.03
        sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility if annual_volatility > 0 else 0

        # 最大回撤
        cumulative_returns = (1 + returns).cumprod()
        running_max = cumulative_returns.expanding().max()
        drawdown = (cumulative_returns - running_max) / running_max
        max_drawdown = drawdown.min()

        # 胜率
        win_rate = (returns > 0).mean()

        # 总收益率
        total_return = (values_df['portfolio_value'].iloc[-1] / self.initial_capital) - 1

        performance = {
            'total_return': total_return,
            'annual_return': annual_return,
            'annual_volatility': annual_volatility,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown,
            'win_rate': win_rate,
            'final_value': values_df['portfolio_value'].iloc[-1]
        }

        # 如果有基准，计算相对指标
        if benchmark_returns is not None:
            # 对齐日期
            common_dates = returns.index.intersection(benchmark_returns.index)
            strategy_returns_aligned = returns.loc[common_dates]
            benchmark_returns_aligned = benchmark_returns.loc[common_dates]

            # 超额收益
            excess_returns = strategy_returns_aligned - benchmark_returns_aligned
            excess_annual_return = (1 + excess_returns.mean()) ** 252 - 1

            # 信息比率
            tracking_error = excess_returns.std() * np.sqrt(252)
            information_ratio = excess_annual_return / tracking_error if tracking_error > 0 else 0

            performance['excess_return'] = excess_annual_return
            performance['tracking_error'] = tracking_error
            performance['information_ratio'] = information_ratio

        return performance