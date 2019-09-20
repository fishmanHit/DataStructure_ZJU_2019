# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:36:05 2019

@author: Administrator
"""
# 超出递归深度报错
# 目前测试到最大值：N=2953

import time
import matplotlib.pyplot as plt

def PrintN(N):
    if N>0:
        PrintN(N-1)
        print(N)

PrintN(2953)        
    
import sys       
sys.getrecursionlimit()