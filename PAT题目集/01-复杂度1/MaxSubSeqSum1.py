# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:58:01 2019

@author: Administrator
"""
# 最大子列和问题：算法1
K = int(input())
KList = list(map(int, input().split()))

MaxSum = 0
for i in range(K):
    for j in range(i, K):
        ThisSum = 0
        for k in range(i, j+1):
            ThisSum += KList[k]
            
        if ThisSum > MaxSum:
            MaxSum = ThisSum
            
print(MaxSum)