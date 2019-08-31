#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
Longest common subsequence
'''

s1 = [1,3,4,5,6,7,7,8]
s2 = [3,5,7,4,8,6,7,8,2]

d = [[0]*(len(s2)+1) for i in range(len(s1)+1) ]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]: # 比较第i，j个元素是否相等
            d[i][j] = d[i-1][j-1]+1 # 多了一个common element, +1
        else:
            d[i][j] = max(d[i-1][j],d[i][j-1])

print(d[-1][-1])