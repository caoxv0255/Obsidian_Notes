"""
主程序 - 股票因子策略
"""
import sys
import os
import pandas as pd
import numpy as np

# 添加当前目录到路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import DB_PATH, STRATEGY_CONFIG, FACTOR_WEIGHTS, BACKTEST_CONFIG
from data_processor import DataProcessor
from factor_builder import FactorBuilder
from factor_analyzer import FactorAnalyzer
from strategy import FactorStrategy
from backtester import Backtester
from performance import PerformanceEvaluator

def main():
    """主函数"""
    print("=" * 60)
    print("股票因子策略回测系统")
    print("=" * 60)

    # 1. 数据准备
    print("\n【步骤1】数据准备")
    print("-" * 60)

    dp = DataProcessor(DB_PATH)

    # 获取股票列表
    cursor = dp.conn.cursor()
    cursor.execute("SELECT ts_code FROM stock_list WHERE is_active = 1")
    stock_list = [row[0] for row in cursor.fetchall()]

    print(f"股票数量: {len(stock_list)}")

    # 2. 因子构建
    print("\n【步骤2】因子构建")
    print("-" * 60)

    fb = FactorBuilder(dp)

    # 构建所有股票的因子
    all_factors = []
    all_prices = []
    all_returns = []

    for i, ts_code in enumerate(stock_list):
        print(f"处理股票 ({i+1}/{len(stock_list)}): {ts_code}")

        # 获取数据
        daily_df = dp.get_data('daily_data', ts_code=ts_code)
        financial_df = dp.get_data('financial_data', ts_code=ts_code)

        if len(daily_df) == 0:
            continue

        # 构建因子
        factors = fb.build_all_factors(daily_df, financial_df)
        factors = fb.standardize_factors(factors, method='zscore')
        factors = fb.neutralize_factors(factors)

        # 计算未来收益（用于因子分析）
        returns = daily_df['close'].pct_change().shift(-1)  # 下一日收益

        # 添加股票代码
        factors['ts_code'] = ts_code
        returns.name = 'return'

        all_factors.append(factors)
        all_returns.append(returns)
        all_prices.append(daily_df[['trade_date', 'close']].set_index('trade_date'))

    # 合并所有数据
    print("\n合并数据...")
    factors_df = pd.concat(all_factors)
    factors_df = factors_df.set_index('trade_date')

    returns_df = pd.concat(all_returns)
    returns_df = returns_df.reset_index()

    # 创建MultiIndex
    factors_df = factors_df.reset_index().set_index(['trade_date', 'ts_code'])
    returns_df = returns_df.set_index(['trade_date', 'ts_code'])

    print(f"因子数据: {len(factors_df)} 行")
    print(f"收益数据: {len(returns_df)} 行")

    # 3. 因子分析
    print("\n【步骤3】因子分析")
    print("-" * 60)

    fa = FactorAnalyzer(dp)

    # 分析所有因子
    factor_analysis = fa.analyze_all_factors(factors_df, returns_df)

    print("\n因子分析结果:")
    print(factor_analysis[['factor_name', 'mean_ic', 'ir', 't_stat']].to_string(index=False))

    # 选择有效因子
    selected_factors = fa.select_factors(factor_analysis, min_ir=0.3, min_t_stat=1.5)
    print(f"\n选择的因子: {selected_factors}")

    # 4. 策略构建
    print("\n【步骤4】策略构建")
    print("-" * 60)

    # 使用选择的因子构建策略
    selected_weights = {k: v for k, v in FACTOR_WEIGHTS.items() if k in selected_factors}

    # 重新归一化权重
    total_weight = sum(selected_weights.values())
    if total_weight > 0:
        selected_weights = {k: v/total_weight for k, v in selected_weights.items()}

    strategy = FactorStrategy(
        factor_weights=selected_weights,
        top_n=STRATEGY_CONFIG['top_n']
    )

    print(f"策略配置:")
    print(f"  选股数量: {STRATEGY_CONFIG['top_n']}")
    print(f"  因子权重: {selected_weights}")

    # 5. 回测
    print("\n【步骤5】回测")
    print("-" * 60)

    backtester = Backtester(
        initial_capital=BACKTEST_CONFIG['initial_capital'],
        transaction_cost=STRATEGY_CONFIG['transaction_cost']
    )

    # 准备价格数据
    prices_dict = {}
    for df in all_prices:
        for date, price in df['close'].items():
            if date not in prices_dict:
                prices_dict[date] = {}
            prices_dict[date][ts_code] = price

    prices_df = pd.DataFrame(prices_dict).T

    # 运行回测
    backtest_result = backtester.run_backtest(
        strategy=strategy,
        factor_df=factors_df,
        returns_df=returns_df,
        prices_df=prices_df
    )

    print(f"回测完成")
    print(f"  交易次数: {len(backtest_result['trades'])}")
    print(f"  回测天数: {len(backtest_result['values'])}")

    # 6. 绩效评估
    print("\n【步骤6】绩效评估")
    print("-" * 60)

    performance = backtester.calculate_performance(backtest_result)

    # 添加初始资金
    performance['initial_capital'] = BACKTEST_CONFIG['initial_capital']

    # 生成绩效报告
    evaluator = PerformanceEvaluator()
    report = evaluator.generate_report(performance, backtest_result['values'])

    print(report)

    # 可视化
    print("\n生成可视化图表...")

    # 绩效曲线
    evaluator.plot_performance(backtest_result['values'])

    # 回撤曲线
    evaluator.plot_drawdown(backtest_result['values'])

    # 月度收益热图
    evaluator.plot_monthly_returns(backtest_result['values'])

    # 关闭数据库连接
    dp.close()

    print("\n" + "=" * 60)
    print("回测完成！")
    print("=" * 60)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()