from statsmodels.stats.diagnostic import acorr_ljungbox
import pandas as pd

data = pd.read_excel('数据文件.xls')

# diff_ 标记为1的数据需要进行一阶差分
diff_ = [0, 1, 1, 1, 1, 1, 0, 1]
df = pd.DataFrame(index=[i for i in range(1, 11)], columns=['Region%d' % i for i in range(1, 9)])

for i in range(1, 9):
    ts = data.iloc[:, i]
    if diff_[i - 1] == 1:
        ts = ts.diff().dropna()

    # 进行Ljung-Box检验
    # 判断准则：
    # 对于每一个滞后阶数（行索引），
    # p值大于显著性水平（如0.05），不能拒绝原假设，序列为白噪声；
    # p值小于显著性水平（如0.05），拒绝原假设，序列非白噪声；

    result = acorr_ljungbox(ts, lags=10)
    df['Region%d' % i] = result['lb_pvalue']

df.index.name = '滞后阶数'
print(df)