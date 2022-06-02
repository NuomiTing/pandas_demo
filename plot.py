import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# 中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签SimHei
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

x = [0, 1, 2, 3, 10,100,120,150,300,500,1000]
y = [69686, 67704, 106044, 152207, 373134,813008,1123595,537634,421940,375939,323624]

for x0,y0 in zip(x,y):
    plt.text(x0, y0, '%.0f' % y0, ha='left', va='bottom', fontdict={'fontsize': 6})

plt.xlabel('Pipline')
plt.ylabel('RPS')
# plt.legend(['SET'])
plt.title('SET')

plt.plot(x, y)
plt.plot(x, y,'o')
plt.show()







