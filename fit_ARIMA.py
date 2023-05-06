import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings('ignore', message="Non-invertible starting MA parameters found")


def main():
    data = pd.read_excel('数据文件.xls')

    # ARIMA(Autoregressive Integrated Moving Average model)差分整合移动平均自回归模型
    # 模型的参数(p, d, q), 每一个元组对应一个地区的模型参数(参数的设置由ACF、PACF图和ADF检验得来)
    # p: 时间序列数据本身的滞后数(属于Autoregressive model自回归模型)
    # d: 数据进行差分的次数
    # q: 预测误差的滞后数(属于Moving average model滑动平均模型)
    param = [(2, 0, 3), (2, 1, 1), (0, 1, 2), (2, 1, 1), (2, 1, 1), (2, 1, 1), (2, 0, 2), (0, 1, 0)]
    dw = pd.DataFrame(index=['region%d' % i for i in range(1, 9)], columns=['统计量'])

    resid, forecast = [], []

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

        # 残差
        resid.append(result.resid)

        # 预测
        forecast.append(result.predict(start=0, end=len(ts)-1, typ='levels'))

    return forecast, resid

if __name__ == '__main__':
    main()
