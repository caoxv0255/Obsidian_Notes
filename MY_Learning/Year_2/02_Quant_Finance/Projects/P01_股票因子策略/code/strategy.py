"""
策略实现
"""
import pandas as pd
import numpy as np

class FactorStrategy:
    """多因子策略"""

    def __init__(self, factor_weights, top_n=10):
        """
        初始化策略

        参数:
            factor_weights: 因子权重字典
            top_n: 选股数量
        """
        self.factor_weights = factor_weights
        self.top_n = top_n

    def calculate_factor_score(self, factor_df):
        """
        计算因子综合得分

        参数:
            factor_df: 因子数据（DataFrame，列为因子，行为股票）

        返回:
            Series: 股票得分
        """
        # 计算加权得分
        score = pd.Series(0.0, index=factor_df.index)

        for factor_name, weight in self.factor_weights.items():
            if factor_name in factor_df.columns:
                # 标准化因子值
                factor_values = factor_df[factor_name]

                # 处理缺失值
                factor_values = factor_values.fillna(0)

                # 加权求和
                score += factor_values * weight

        return score

    def select_stocks(self, score_series):
        """
        选股

        参数:
            score_series: 股票得分序列

        返回:
            list: 选中的股票代码列表
        """
        # 选择得分最高的N只股票
        top_stocks = score_series.nlargest(self.top_n)

        return top_stocks.index.tolist()

    def calculate_positions(self, selected_stocks, total_capital):
        """
        计算仓位

        参数:
            selected_stocks: 选中的股票列表
            total_capital: 总资金

        返回:
            dict: 股票仓位 {股票代码: 仓位金额}
        """
        # 等权配置
        position_size = total_capital / len(selected_stocks)

        positions = {stock: position_size for stock in selected_stocks}

        return positions

    def generate_trades(self, current_positions, new_positions):
        """
        生成交易指令

        参数:
            current_positions: 当前持仓
            new_positions: 新持仓

        返回:
            list: 交易指令列表
        """
        trades = []

        # 卖出不在新持仓中的股票
        for stock in current_positions:
            if stock not in new_positions:
                trades.append({
                    'stock': stock,
                    'action': 'sell',
                    'quantity': current_positions[stock]
                })

        # 买入新持仓中的股票
        for stock in new_positions:
            if stock not in current_positions:
                trades.append({
                    'stock': stock,
                    'action': 'buy',
                    'quantity': new_positions[stock]
                })
            elif current_positions[stock] != new_positions[stock]:
                # 调整仓位
                trades.append({
                    'stock': stock,
                    'action': 'adjust',
                    'quantity': new_positions[stock] - current_positions[stock]
                })

        return trades

    def backtest(self, factor_df, returns_df, rebalance_freq='monthly'):
        """
        回测策略

        参数:
            factor_df: 因子数据（MultiIndex: [date, stock]）
            returns_df: 收益数据（MultiIndex: [date, stock]）
            rebalance_freq: 调仓频率

        返回:
            dict: 回测结果
        """
        # 按日期分组
        dates = factor_df.index.get_level_values(0).unique()

        # 结果存储
        results = {
            'dates': [],
            'selected_stocks': [],
            'portfolio_returns': []
        }

        # 当前持仓
        current_positions = {}

        for date in dates:
            # 获取当日因子数据
            daily_factors = factor_df.loc[date]

            # 计算因子得分
            scores = self.calculate_factor_score(daily_factors)

            # 选股
            selected_stocks = self.select_stocks(scores)

            # 记录
            results['dates'].append(date)
            results['selected_stocks'].append(selected_stocks)

            # 计算组合收益
            if len(selected_stocks) > 0:
                # 获取选中的股票的收益
                daily_returns = returns_df.loc[date].loc[selected_stocks]

                # 等权平均收益
                portfolio_return = daily_returns.mean()

                results['portfolio_returns'].append(portfolio_return)
            else:
                results['portfolio_returns'].append(0.0)

        # 转换为DataFrame
        result_df = pd.DataFrame({
            'date': results['dates'],
            'selected_stocks': results['selected_stocks'],
            'portfolio_return': results['portfolio_returns']
        })

        result_df.set_index('date', inplace=True)

        return result_df