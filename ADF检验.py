import pandas as pd
from statsmodels.tsa.stattools import adfuller

data = pd.read_excel('数据文件.xls')

def ADF(ts):

    index = ['ADF统计值', 'p值', '临界值(1%)', '临界值(5%)', '临界值(10%)']
    df = pd.DataFrame(index=index, columns=['0阶差分', '1阶差分'])

    result = adfuller(ts)
    df['0阶差分'] = [result[0], result[1], result[4]['1%'], result[4]['5%'], result[4]['10%']]

    ts = ts.diff().dropna()
    result = adfuller(ts)
    df['1阶差分'] = [result[0], result[1], result[4]['1%'], result[4]['5%'], result[4]['10%']]

    return df

for i in range(1, 9):
    ts = data.iloc[:, i]
    print('='*30)
    print('region%d:' % i)

    # ADF检验数据
    print(ADF(ts))
