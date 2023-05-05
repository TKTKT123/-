import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Map

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

df1 = pd.read_csv('全国月度居民消费价格分类指数.csv', usecols=[0, 1], header=None,
                  names=['time', '居民消费价格指数'])
df2 = pd.read_csv('全国月度居民消费价格分类指数-2016.csv', usecols=[0, 1], header=None,
                  names=['time', '居民消费价格指数'])
df = pd.concat([df1, df2], axis=0)

df = df.sort_index(axis=0, ascending=False)
df = df.reset_index(drop=True)
df = df.dropna()
df['居民消费价格指数'] = df['居民消费价格指数'].astype(float)
df = df[df['居民消费价格指数'] != 0]
df.plot.scatter(x='time',
                y='居民消费价格指数', )
plt.savefig('居民消费价格指数.png')
df.plot(x='time', y='居民消费价格指数')

plt.show()
print(df.dtypes)
print(df)
