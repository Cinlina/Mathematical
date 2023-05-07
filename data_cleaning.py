import pandas as pd

def clean(df):

    df.drop_duplicates(inplace=True)  # 去除重复行

    # 使用相邻两个数的平均值填充缺失值
    for col in df.columns:

        if df[col].isnull().sum() > 0:  # 如果列中有缺失值
            values = df[col].values  # 获取列数据
            for i in range(len(values)):
                if pd.isna(values[i]):  # 找到缺失值
                    if i == 0:  # 如果缺失值在列表开头，只能用后一个数据填充
                        avg = (values[i+1] + values[i+2]) / 2
                    elif i == len(values)-1:  # 如果缺失值在列表结尾，只能用前一个数据填充
                        avg = (values[i-2] + values[i-1]) / 2
                    else:  # 如果缺失值在列表中间，用前后两个数据的平均值填充
                        avg = (values[i-1] + values[i+1]) / 2

                    if pd.isna(avg):  # 如果前后两个数据都是缺失值，则用列的均值填充
                        values[i] = df[col].mean()
                    else:
                        values[i] = avg
            df[col] = values  # 将填充好的数据放回数据集

    return df

if __name__ == '__main__':
    df = pd.read_excel('数据文件.xls')
    df = clean(df)
    df.to_excel('数据文件2.xls', index=False)
    print(df)
