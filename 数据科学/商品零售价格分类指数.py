import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Map

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

df = pd.read_csv('全国月度商品零售价格价格分类指数.csv', usecols=[0, 1, 2], header=None,
                 names=['time', '商品', '食品类'])

df = df.sort_index(axis=0, ascending=False)
df = df.reset_index(drop=True)
df = df.dropna()
df['商品'] = df['商品'].astype(float)
df['食品类'] = df['食品类'].astype(float)
df = df[df['商品'] != 0]

df.plot.scatter(x='time',
                y='食品类',
                c='商品',
                colormap='viridis')
plt.savefig('商品零售价格指数.png')

plt.show()
print(df.dtypes)
print(df)
