# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:16:52 2019

@author: Administrator
"""

# 最大子列和问题：算法4
K = int(input())
KList = list(map(int, input().split()))

MaxSum = 0
ThisSum = 0

for i in range(K):
    ThisSum += KList[i]
    if ThisSum > MaxSum:
        MaxSum = ThisSum
    elif ThisSum < 0:
        ThisSum = 0
    
print(MaxSum)