import pandas as pd
from statsmodels.tsa.stattools import adfuller

data = pd.read_excel('数据文件.xls')

index = ['ADF统计值', 'p值', '临界值(1%)', '临界值(5%)', '临界值(10%)']
df_0 = pd.DataFrame(index=index, columns=['Region%d' % i for i in range(1, 9)])
df_1 = pd.DataFrame(index=index, columns=['Region%d' % i for i in range(1, 9)])

# ADF检验
for i in range(1, 9):
    ts = data.iloc[:, i]

    # ADF检验数据
    # 没有差分的DataFrame
    result = adfuller(ts)
    df_0['Region%d' % i] = [result[0], result[1], result[4]['1%'], result[4]['5%'], result[4]['10%']]

    # 进行差分的DataFrame
    ts = ts.diff().dropna()
    result = adfuller(ts)
    df_1['Region%d' % i] = [result[0], result[1], result[4]['1%'], result[4]['5%'], result[4]['10%']]

print('原始数据的ADF检验结果：')
print(df_0)
print('一阶差分后的ADF检验结果：')
print(df_1)
