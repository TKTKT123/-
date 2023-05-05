import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Map
from datetime import datetime

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

df = pd.read_csv('服务业生产指数.csv', usecols=[0, 1, 2], header=None,
                 names=['time', '服务业生产指数当月同比增速(%)', '服务业生产指数累计同比增速(%)'])

df = df.sort_index(axis=0, ascending=False)
df = df.reset_index(drop=True)
df = df.dropna()
df['服务业生产指数当月同比增速(%)'] = df['服务业生产指数当月同比增速(%)'].astype(float)
df['服务业生产指数累计同比增速(%)'] = df['服务业生产指数累计同比增速(%)'].astype(float)
df = df[df['服务业生产指数当月同比增速(%)'] != 0]
df['time'] = pd.to_datetime(df['time'], format='%Y%m')

df.plot.scatter(x='time',
                y='服务业生产指数当月同比增速(%)',)
plt.savefig('服务业生产指数1.png')
df.plot.scatter(x='time',
                y='服务业生产指数累计同比增速(%)',)
plt.savefig('服务业生产指数2.png')

plt.show()
print(df.dtypes)
print(df)
