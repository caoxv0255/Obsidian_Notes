"""
因子分析器
"""
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

class FactorAnalyzer:
    """因子分析器"""

    def __init__(self, data_processor):
        self.dp = data_processor

    def calculate_ic(self, factor_values, future_returns):
        """
        计算信息系数（IC）

        参数:
            factor_values: 因子值序列
            future_returns: 未来收益序列

        返回:
            float: IC值
        """
        # 删除缺失值
        common_index = factor_values.dropna().index.intersection(future_returns.dropna().index)
        factor_values_clean = factor_values.loc[common_index]
        future_returns_clean = future_returns.loc[common_index]

        # 计算皮尔逊相关系数
        ic = factor_values_clean.corr(future_returns_clean)

        return ic

    def calculate_ic_series(self, factor_df, returns_df, factor_name):
        """
        计算IC时间序列

        参数:
            factor_df: 因子数据
            returns_df: 收益数据
            factor_name: 因子名称

        返回:
            Series: IC时间序列
        """
        ic_series = pd.Series(dtype=float)

        # 按月计算IC
        for date in factor_df.index.unique():
            factor_values = factor_df.loc[date, factor_name]
            future_returns = returns_df.loc[date]

            ic = self.calculate_ic(factor_values, future_returns)

            if not np.isnan(ic):
                ic_series[date] = ic

        return ic_series

    def calculate_ir(self, ic_series):
        """
        计算信息比率（IR）

        参数:
            ic_series: IC时间序列

        返回:
            float: IR值
        """
        mean_ic = ic_series.mean()
        std_ic = ic_series.std()

        if std_ic > 0:
            ir = mean_ic / std_ic
        else:
            ir = 0

        return ir

    def calculate_t_stat(self, ic_series):
        """
        计算t统计量

        参数:
            ic_series: IC时间序列

        返回:
            float: t统计量
        """
        mean_ic = ic_series.mean()
        std_ic = ic_series.std()
        n = len(ic_series)

        if std_ic > 0 and n > 1:
            t_stat = mean_ic / (std_ic / np.sqrt(n))
        else:
            t_stat = 0

        return t_stat

    def analyze_factor(self, factor_df, returns_df, factor_name):
        """
        分析单个因子

        参数:
            factor_df: 因子数据
            returns_df: 收益数据
            factor_name: 因子名称

        返回:
            dict: 分析结果
        """
        # 计算IC序列
        ic_series = self.calculate_ic_series(factor_df, returns_df, factor_name)

        # 计算统计量
        mean_ic = ic_series.mean()
        std_ic = ic_series.std()
        ir = self.calculate_ir(ic_series)
        t_stat = self.calculate_t_stat(ic_series)

        # IC正值比例
        positive_ic_ratio = (ic_series > 0).mean()

        # IC绝对值 > 0.02 的比例
        significant_ic_ratio = (ic_series.abs() > 0.02).mean()

        result = {
            'factor_name': factor_name,
            'mean_ic': mean_ic,
            'std_ic': std_ic,
            'ir': ir,
            't_stat': t_stat,
            'positive_ic_ratio': positive_ic_ratio,
            'significant_ic_ratio': significant_ic_ratio,
            'ic_series': ic_series
        }

        return result

    def analyze_all_factors(self, factor_df, returns_df):
        """
        分析所有因子

        参数:
            factor_df: 因子数据
            returns_df: 收益数据

        返回:
            DataFrame: 所有因子的分析结果
        """
        results = []

        for factor_name in factor_df.columns:
            result = self.analyze_factor(factor_df, returns_df, factor_name)
            results.append(result)

        # 转换为DataFrame
        result_df = pd.DataFrame(results)

        # 按IR排序
        result_df = result_df.sort_values('ir', ascending=False)

        return result_df

    def plot_ic_series(self, ic_series, factor_name):
        """
        绘制IC序列图

        参数:
            ic_series: IC时间序列
            factor_name: 因子名称
        """
        plt.figure(figsize=(12, 6))

        plt.plot(ic_series.index, ic_series.values, marker='o', linewidth=2)

        plt.axhline(y=ic_series.mean(), color='r', linestyle='--',
                   label=f'Mean IC: {ic_series.mean():.4f}')

        plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)

        plt.title(f'IC Time Series - {factor_name}')
        plt.xlabel('Date')
        plt.ylabel('IC')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def select_factors(self, factor_analysis_df, min_ir=0.5, min_t_stat=2.0):
        """
        选择有效因子

        参数:
            factor_analysis_df: 因子分析结果
            min_ir: 最小IR值
            min_t_stat: 最小t统计量

        返回:
            list: 选择的因子列表
        """
        # 筛选条件
        selected = factor_analysis_df[
            (factor_analysis_df['ir'] >= min_ir) &
            (abs(factor_analysis_df['t_stat']) >= min_t_stat)
        ]

        return selected['factor_name'].tolist()