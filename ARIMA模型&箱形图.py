import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
plt.style.use('seaborn-v0_8-whitegrid')

# ARIMA(Autoregressive Integrated Moving Average model)差分整合移动平均自回归模型
# 模型的参数(p, d, q), 每一个元组对应一个地区的模型参数(参数的设置由ACF、PACF图和ADF检验得来)
# p: 时间序列数据本身的滞后数(属于Autoregressive model自回归模型)
# d: 数据进行差分的次数
# q: 预测误差的滞后数(属于Moving average model滑动平均模型)
param = [(2, 0, 3), (2, 1, 1), (0, 1, 2), (2, 1, 1), (2, 1, 1), (2, 1, 1), (2, 0, 2), (0, 1, 0)]
data = pd.read_excel('数据文件.xls')
fig, ax = plt.subplots(8, 1, figsize=(15, 40))

for i in range(1, 9):
    ts = data.iloc[:, i]

    # 进行自动 ARIMA 模型拟合(想看算法拟合的参数可以把下面四行的#去掉)
    # from pmdarima import auto_arima
    # model = auto_arima(ts)
    # order = model.order
    # print(order)

    # 训练 ARIMA 模型
    model = ARIMA(ts, order=param[i - 1])
    result = model.fit()

    # 预测
    forecast = result.predict(start=0, end=len(ts)-1, typ='levels')

    ax[i-1].plot(ts, label='Original')
    ax[i-1].plot(forecast, label='Forecast')

    # 基于2σ准则判断异常点
    # 假设模型的预测值和真实值的差，即残差服从高斯分布
    diff = np.array(ts - forecast)
    diff_std = diff.std()
    diff_mean = diff.mean()

    # 不在（μ - 2σ，μ + 2σ）区间内的布尔索引，即异常值的布尔索引
    outliers = (diff_mean + 2 * diff_std < diff) | (diff < diff_mean - 2 * diff_std)

    # ARIMA模型标注的异常点为红色
    # 箱形图标注的异常点为绿色，有可能把同一个位置的红色点覆盖掉
    ax[i-1].scatter(np.arange(100)[outliers], ts[outliers], c='red', s=100, label='ARIMA-Outliers')

    # 箱形图
    q1, q3 = ts.quantile(q=[0.25, 0.75])
    iqr = q3 - q1
    outliers_index = (ts < (q1 - 1.5 * iqr)) | (ts > (q3 + 1.5 * iqr))
    ax[i-1].scatter(np.arange(100)[outliers_index], ts[outliers_index], c='green', s=100, label='Boxplot-Outliers')
    ax[i-1].set_title('region%d' % i)
    ax[i-1].legend()

    # AIC和BIC指标是评估ARIMA模型的，越小越好
    # print('-'*25 + 'region' + str(i) + '-'*25)
    # # 计算模型的AIC和BIC指标
    # print('AIC:', result.aic)
    # print('BIC:', result.bic)
    # print()

plt.show()
