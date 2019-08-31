#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
假设我们有n件物品，分别编号为1, 2...n。其中编号为i的物品价值为vi，它的重量为wi。
现在，假设我们有一个背包，它能够承载的重量是W。现在，我们希望往包里装这些物品，使得包里装的物品价值最大化，那么我们该如何来选择装的东西呢？
'''

w = [0, 1, 4, 3, 1]   #n个物体的重量(w[0]无用)
v = [0, 1500, 3000, 2000, 2000]
W = 4 # 背包承重


def bag(w, v, W):
    n = len(w) - 1 # 东西个数
    x = []  # True表示已经装入
    dp = [[0 for col in range(W + 1)] for row in range(n + 1)]  # zero matrix
    for i in range(1, n + 1): # 第几个东西
        for j in range(1, W + 1): # 重量
            if j >= w[i]: # 可以放入时
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
            else:
                dp[i][j] = dp[i-1][j]
    j = W
    for i in range(n,0,-1):
        if dp[i][j] > dp[i-1][j]:
            x.append(i)
            j = j-w[i]

    return dp[n][W], x

print(bag(w,v,W))
