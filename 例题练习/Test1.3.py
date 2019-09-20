# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:15:18 2019

@author: Administrator
"""

# 比较两种多项式计算函数的效率

import time

def poly1(n, a, x):
    y = a[0]
    for i in range(1, n+1):
        y += a[i]*(x**i)
    
    return y
        
def poly2(n, a, x):
    y = a[-1]
    for i in range(n, 0, -1):
        y = a[i-1] + y*x

    return y

# 重复运行函数，计时
def run(f, n, a, x, MAXK, case_n):
    t0 = time.process_time()
    for i in range(MAXK):
        f(n, a, x)
        
    dt = (time.process_time() - t0)/MAXK
    print('case{0}: dt = {1}s'.format(case_n, dt))

    
# 多项式阶数+1
MAXN = 10
# 多项式系数
a = [i for i in range(10)]
# 重复次数
MAXK = 10**7
f = [poly1, poly2]
for i in range(2):
    run(f[i], MAXN-1, a, 1.1, MAXK, i)

