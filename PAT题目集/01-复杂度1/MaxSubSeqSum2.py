# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:04:15 2019

@author: Administrator
"""

# 最大子列和问题：算法2
K = int(input())
KList = list(map(int, input().split()))

MaxSum = 0

for i in range(K):
    ThisSum = 0
    for j in range(i, K):
        ThisSum += KList[j]
        
        if ThisSum > MaxSum:
            MaxSum = ThisSum
        
print(MaxSum)