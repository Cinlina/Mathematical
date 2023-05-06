import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

data = pd.read_excel('数据文件.xls')

fig, ax = plt.subplots(8, 2, figsize=(15, 40))

# diff_ 标记为1的数据需要进行一阶差分
diff_ = [0, 1, 1, 1, 1, 1, 0, 1]

for i in range(1, 9):

    # 绘制时间序列的ACF和PACF图
    # 图表每一行代表一个地区
    ts = data.iloc[:, i]
    if diff_[i - 1] == 1:
        ts = ts.diff().dropna()

    plot_acf(ts, ax=ax[i-1, 0])
    plot_pacf(ts, ax=ax[i-1, 1], method='ywm')
    ax[i-1, 0].set_title('region%d-ACF' % i)
    ax[i-1, 1].set_title('region%d-PACF' % i)
    ax[i-1, 0].set_ylabel('自相关系数')
    ax[i-1, 1].set_ylabel('偏相关系数')

plt.show()
