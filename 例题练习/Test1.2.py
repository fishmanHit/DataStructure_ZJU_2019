# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:09:02 2019

@author: Administrator
"""
# 打印1-N全部正整数：循环算法
# 计算不同N（10^0-10^6）所需的计算时间，并画图表示

import time
import matplotlib.pyplot as plt

def PrintN(N):
    for i in range(1, N+1):
        print(i)

TN = 7
dt = list(0 for i in range(TN))
for k in range(TN):
    t0 = time.process_time()
    PrintN(10**k)
    dt[k] = time.process_time() - t0

plt.plot(dt)
plt.xlabel('log(N)')
plt.ylabel('Time/s')
plt.show()



