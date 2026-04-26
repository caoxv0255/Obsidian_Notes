"""
绩效评估模块
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class PerformanceEvaluator:
    """绩效评估器"""

    def __init__(self):
        pass

    def plot_performance(self, values_df, benchmark_values=None):
        """
        绘制绩效曲线

        参数:
            values_df: 组合价值数据
            benchmark_values: 基准价值数据
        """
        # 计算累计收益
        portfolio_cumulative = (values_df['portfolio_value'] / values_df['portfolio_value'].iloc[0] - 1) * 100

        plt.figure(figsize=(12, 6))

        plt.plot(portfolio_cumulative.index, portfolio_cumulative.values,
                label='Portfolio', linewidth=2)

        if benchmark_values is not None:
            benchmark_cumulative = (benchmark_values / benchmark_values.iloc[0] - 1) * 100
            plt.plot(benchmark_cumulative.index, benchmark_cumulative.values,
                    label='Benchmark', linewidth=2, alpha=0.7)

        plt.title('Portfolio Performance')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Return (%)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_drawdown(self, values_df):
        """
        绘制回撤曲线

        参数:
            values_df: 组合价值数据
        """
        # 计算收益率
        returns = values_df['portfolio_value'].pct_change().dropna()

        # 计算累计收益
        cumulative = (1 + returns).cumprod()

        # 计算回撤
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max * 100

        plt.figure(figsize=(12, 6))

        plt.fill_between(drawdown.index, drawdown.values, 0,
                       where=drawdown.values < 0,
                       color='red', alpha=0.3, label='Drawdown')

        plt.plot(drawdown.index, drawdown.values,
                color='red', linewidth=1)

        plt.title('Portfolio Drawdown')
        plt.xlabel('Date')
        plt.ylabel('Drawdown (%)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_monthly_returns(self, values_df):
        """
        绘制月度收益热图

        参数:
            values_df: 组合价值数据
        """
        # 计算日收益率
        returns = values_df['portfolio_value'].pct_change().dropna()

        # 转换为月度收益
        monthly_returns = returns.resample('M').apply(lambda x: (1 + x).prod() - 1)

        # 创建年-月表格
        monthly_returns.index = pd.to_datetime(monthly_returns.index)
        monthly_returns['year'] = monthly_returns.index.year
        monthly_returns['month'] = monthly_returns.index.month

        # 透视表
        heatmap_data = monthly_returns.pivot(index='year', columns='month', values='portfolio_value')

        # 转换为百分比
        heatmap_data = heatmap_data * 100

        plt.figure(figsize=(12, 8))

        plt.imshow(heatmap_data.values, cmap='RdYlGn', aspect='auto')

        # 设置标签
        plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        plt.yticks(range(len(heatmap_data.index)), heatmap_data.index)

        # 添加数值标签
        for i in range(len(heatmap_data.index)):
            for j in range(12):
                value = heatmap_data.iloc[i, j]
                if not pd.isna(value):
                    text_color = 'white' if abs(value) > 10 else 'black'
                    plt.text(j, i, f'{value:.1f}%', ha='center', va='center',
                            color=text_color, fontsize=9)

        plt.colorbar(label='Monthly Return (%)')
        plt.title('Monthly Returns Heatmap')
        plt.tight_layout()
        plt.show()

    def generate_report(self, performance, values_df):
        """
        生成绩效报告

        参数:
            performance: 绩效指标字典
            values_df: 组合价值数据

        返回:
            str: 绩效报告
        """
        report = "=" * 60 + "\n"
        report += "策略绩效报告\n"
        report += "=" * 60 + "\n\n"

        # 基本指标
        report += "【基本指标】\n"
        report += f"初始资金: ¥{performance.get('initial_capital', 1000000):,.2f}\n"
        report += f"最终资金: ¥{performance.get('final_value', 0):,.2f}\n"
        report += f"总收益率: {performance.get('total_return', 0)*100:.2f}%\n"
        report += f"年化收益率: {performance.get('annual_return', 0)*100:.2f}%\n"
        report += f"年化波动率: {performance.get('annual_volatility', 0)*100:.2f}%\n\n"

        # 风险指标
        report += "【风险指标】\n"
        report += f"夏普比率: {performance.get('sharpe_ratio', 0):.4f}\n"
        report += f"最大回撤: {performance.get('max_drawdown', 0)*100:.2f}%\n"
        report += f"胜率: {performance.get('win_rate', 0)*100:.2f}%\n\n"

        # 相对指标
        if 'excess_return' in performance:
            report += "【相对基准】\n"
            report += f"超额收益: {performance.get('excess_return', 0)*100:.2f}%\n"
            report += f"跟踪误差: {performance.get('tracking_error', 0)*100:.2f}%\n"
            report += f"信息比率: {performance.get('information_ratio', 0):.4f}\n\n"

        # 交易统计
        report += "【交易统计】\n"
        report += f"回测天数: {len(values_df)} 天\n"

        return report

    def compare_strategies(self, performance_dict):
        """
        比较多个策略

        参数:
            performance_dict: 策略绩效字典 {策略名: 绩效指标}
        """
        # 创建比较表
        comparison_df = pd.DataFrame(performance_dict).T

        # 选择关键指标
        key_metrics = ['total_return', 'annual_return', 'sharpe_ratio',
                      'max_drawdown', 'win_rate']

        comparison_df = comparison_df[key_metrics]

        # 格式化显示
        comparison_df['total_return'] = comparison_df['total_return'] * 100
        comparison_df['annual_return'] = comparison_df['annual_return'] * 100
        comparison_df['max_drawdown'] = comparison_df['max_drawdown'] * 100
        comparison_df['win_rate'] = comparison_df['win_rate'] * 100

        # 重命名列
        comparison_df.columns = ['总收益率(%)', '年化收益率(%)', '夏普比率',
                                '最大回撤(%)', '胜率(%)']

        print("=" * 60)
        print("策略比较")
        print("=" * 60)
        print(comparison_df.round(2))
        print("=" * 60)