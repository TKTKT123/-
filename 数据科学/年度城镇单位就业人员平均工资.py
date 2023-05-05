import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Map

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

df = pd.read_csv('年度城镇单位就业人员平均工资.csv', usecols=[0, 1], header=None,
                 names=['year', '城镇单位就业人员平均工资(元)'])
df = df.loc[~(df == 0).all(axis=1)]
df = df.sort_index(axis=0, ascending=False)
df = df.reset_index(drop=True)
df = df.dropna()
df['城镇单位就业人员平均工资(元)'] = df['城镇单位就业人员平均工资(元)'].astype(float)
df = df[df['城镇单位就业人员平均工资(元)'] != 0]

print(df.dtypes)

df.plot(x='year', y='城镇单位就业人员平均工资(元)')
plt.savefig('城镇单位就业人员平均工资.png')

print(df)
plt.show()
