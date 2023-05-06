from statsmodels.stats.diagnostic import acorr_ljungbox
import pandas as pd

data = pd.read_excel('数据文件.xls')

# diff_ 标记为1的数据需要进行一阶差分
diff_ = [0, 1, 1, 1, 1, 1, 0, 1]

for i in range(1, 9):
    ts = data.iloc[:, i]
    if diff_[i - 1] == 1:
        ts = ts.diff().dropna()

    print('=' * 30)
    print('region%d:' % i)
    # 进行Ljung-Box检验
    # 判断准则：
    # 对于每一个滞后阶数，
    # LB统计量小于选定置信水平下的临界值，或者值大于显著性水平（如0.05），不能拒绝原假设，序列为白噪声；
    # LB统计量大于选定置信水平下的临界值，或者值小于显著性水平（如0.05），拒绝原假设，序列非白噪声；

    print(acorr_ljungbox(ts, lags=10).rename(columns={'lb_stat': 'LB统计量', 'lb_pvalue': 'p值'}))