import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

data = pd.read_excel('数据文件.xls')

fig = plt.figure(figsize=(15, 40))
diff_ = [0, 1, 1, 1, 1, 1, 0, 1]

for i in range(1, 9):

    # 绘制时间序列的ACF和PACF图
    # 图表每一行代表一个地区
    ts = data.iloc[:, i]
    if diff_[i - 1] == 1:
        ts = ts.diff().dropna()
    ax1 = fig.add_subplot(8, 2, 2*i - 1)
    ax2 = fig.add_subplot(8, 2, 2*i)

    plot_acf(ts, ax=ax1)
    plot_pacf(ts, ax=ax2, method='ywm')

plt.show()
