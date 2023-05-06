import fit_ARIMA
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

resid = fit_ARIMA.main()[1]
fig, ax = plt.subplots(4, 2, figsize=(15, 18))
for i in range(0, 4):

    # 绘制残差的概率图
    # 数据点大致分布在直线附近，说明残差近似服从正态分布
    sm.qqplot(resid[2*i], ax=ax[i, 0], line='s')
    sm.qqplot(resid[2*i+1], ax=ax[i, 1], line='s')
    ax[i, 0].set_title('Region%d' % (2*i+1))
    ax[i, 1].set_title('Region%d' % (2*i+2))
    fig.subplots_adjust(hspace=0.5)

plt.show()
