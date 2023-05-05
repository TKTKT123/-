import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Map

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

df = pd.read_csv('年度城镇登记失业人员及失业率.csv', usecols=[0, 1], header=None,
                 names=['year', '城镇登记失业人数(万人)'])
df = df.loc[~(df == 0).all(axis=1)]
df = df.sort_index(axis=0, ascending=False)
df = df.reset_index(drop=True)
df = df.dropna()
df['城镇登记失业人数(万人)'] = df['城镇登记失业人数(万人)'].astype(float)
df = df[df['城镇登记失业人数(万人)'] != 0]

print(df.dtypes)

df.plot(x='year', y='城镇登记失业人数(万人)')
plt.savefig('城镇登记失业人数.png')

print(df)
plt.show()
