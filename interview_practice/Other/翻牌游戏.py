#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
50 张扑克牌背面朝下，第 1 次把所有牌依次翻面，第 2 次每隔 1 张牌翻一次 面，第 3 次每隔 2 张牌翻一次面，。。。，第 50 次只翻最后一张。
问 50 次之 后有几张牌正面朝上？
'''


dp = [0] * 50 # 0: 背面， 1： 正面
for i in range(1,51): # 翻牌次数
    for j in range(1,51): # 对于50张牌
        if j % i == 0:
            if dp[j-1] == 0:
                dp[j-1] = 1
            else:
                dp[j-1] = 0

print(dp)
for i in range(len(dp)):
    if dp[i] == 1:
        print(i+1)

#%%
dp = list(range(1,121))
res = []
for i in dp:
    if i % 2 == 0:
        continue
    if i % 5 == 0:
        continue
    if i % 7 == 0:
        continue
    res.append(i)

print(len(res))