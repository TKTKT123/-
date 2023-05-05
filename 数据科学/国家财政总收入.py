import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Map

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

df = pd.read_csv('国家财政收入.csv', usecols=[0, 1, 2], header=None,
                 names=['time', '国家财政收入累计值(亿元)', '国家财政收入累计增长%'])

df = df.sort_index(axis=0, ascending=False)
df = df.reset_index(drop=True)
df = df.dropna()
df['国家财政收入累计值(亿元)'] = df['国家财政收入累计值(亿元)'].astype(float)
df['国家财政收入累计增长%'] = df['国家财政收入累计增长%'].astype(float)
df = df[df['国家财政收入累计值(亿元)'] != 0]

# 绘柱状图
plt.bar(x=df['time'], height=df['国家财政收入累计值(亿元)'], label='国家财政收入累计值(亿元)', color='Coral', width=99)

# 在左侧显示图例
plt.legend(loc="upper left")

# 设置标题
plt.title("国家财政收入")
# 为两条坐标轴设置名称
plt.xlabel("time")

# 画折线图
ax2 = plt.twinx()
ax2.set_ylabel("增长率")
# 设置坐标轴范围
ax2.set_ylim([-20, 50]);
plt.plot(df['time'], df['国家财政收入累计增长%'], marker='.', c='r', ms=5, linewidth='1', label="增长率")
# 显示数字
for a, b in zip(df['国家财政收入累计值(亿元)'], df['国家财政收入累计增长%']):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=8)
# 在右侧显示图例
plt.legend(loc="upper right")
plt.savefig('国家财政收入.png')

plt.show()
