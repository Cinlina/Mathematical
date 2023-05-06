import pandas as pd
import matplotlib.pyplot as plt
import fit_ARIMA
import numpy as np

data = pd.read_excel('数据文件.xls')
forecast, resid = fit_ARIMA.main()
fig, ax = plt.subplots(8, 1, figsize=(15, 40))
for i in range(1, 9):

    ts = data.iloc[:, i]

    ax[i-1].plot(ts, label='Original')
    ax[i-1].plot(forecast[i-1], label='Forecast')

    # 因残差近似服从正态分布，所以基于2σ准则判断异常点
    resid_std = resid[i-1].std()
    resid_mean = resid[i-1].mean()

    # 不在（μ - 2σ，μ + 2σ）区间内的布尔索引，即异常值的布尔索引
    outliers = (resid_mean + 2 * resid_std < resid[i-1]) | (resid[i-1] < resid_mean - 2 * resid_std)

    # ARIMA模型标注的异常点为红色
    # 箱形图标注的异常点为绿色，有可能把同一个位置的红色点覆盖掉
    ax[i-1].scatter(np.arange(100)[outliers], ts[outliers], c='red', s=100, label='ARIMA-Outliers')

    # 箱形图
    q1, q3 = ts.quantile(q=[0.25, 0.75])
    iqr = q3 - q1
    outliers_index = (ts < (q1 - 1.5 * iqr)) | (ts > (q3 + 1.5 * iqr))
    ax[i-1].scatter(np.arange(100)[outliers_index], ts[outliers_index], c='green', s=100, label='Boxplot-Outliers')
    ax[i-1].set_title('region%d' % i, fontsize=20)
    ax[i-1].legend()

plt.show()
