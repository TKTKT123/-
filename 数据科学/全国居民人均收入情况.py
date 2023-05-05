import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Map

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

df = pd.read_csv('年度全国居民人均收入情况.csv', usecols=[0, 1], header=None,
                 names=['year', '居民人均可支配收入(元)'])
df = df.loc[~(df == 0).all(axis=1)]
df = df.sort_index(axis=0, ascending=False)
df = df.reset_index(drop=True)
df = df.dropna()
df['居民人均可支配收入(元)'] = df['居民人均可支配收入(元)'].astype(float)
df = df[df['居民人均可支配收入(元)'] != 0]

print(df.dtypes)

df.plot(x='year', y='居民人均可支配收入(元)')
plt.savefig('居民人均可支配收入.png')

print(df)
plt.show()
