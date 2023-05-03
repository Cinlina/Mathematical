import pandas as pd
from statsmodels.tsa.stattools import adfuller

data = pd.read_excel('数据文件.xls')
for i in range(1, 9):
    ts = data.iloc[:, i]

    # 使用adfuller函数进行ADF检验
    result = adfuller(ts)

    # 检验结果
    print('-'*25 + 'region%d' % i + '-'*25)
    print('-'*10 + '0阶差分' + '-'*10)
    print('ADF统计量：', result[0])
    print('p-value：', result[1])
    print('临界值：', result[4])
    print('-'*10 + '1阶差分' + '-'*10)
    ts = ts.diff().dropna()
    result = adfuller(ts)
    print('ADF统计量：', result[0])
    print('p-value：', result[1])
    print('临界值：', result[4])
    print('-'*50 + '\n')
