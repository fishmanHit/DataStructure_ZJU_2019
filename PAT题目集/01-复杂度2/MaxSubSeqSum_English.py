# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:28:25 2019

@author: Administrator
"""

# 01-复杂度2 Maximum Subsequence Sum
# 若所有K个整数为负，则输出0，首尾整数
# 若有重复最大子列和，则输出下标较小者

K = int(input())
KList = list(map(int, input().split()))

MaxSum = KList[0]
ThisSum = 0
SubSeq = [None, None]
SubSeq[0] = SubSeq[1] = KList[0]
NewStart = KList[0]

for i in range(K):
    ThisSum += KList[i]    
    if ThisSum > MaxSum:
        MaxSum = ThisSum
        SubSeq[0] = NewStart
        SubSeq[1] = KList[i]
        
    elif ThisSum < 0:
        ThisSum = 0
        NewStart = KList[i+1] if i<K-1 else KList[-1]      

if max(KList) < 0:
    print(0, KList[0], KList[-1])
else:
    print(MaxSum, SubSeq[0], SubSeq[1])   # 子列首尾两个数，若重复，则给出下标较小者
    
