#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
在一个mxn的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0），你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格，直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计算你最多能拿多少价值的礼物？
DP: f(i,j)=max(f(i-1,j),f(i,j-1))+gift(i,j)
'''

class Solution:
    def gift(self, matrix):
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        if cols <= 0 or rows <= 0:
            return 0


        dp = [[ 0 for i in range(cols)] for j in range(rows)] # 利用二维数组

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    # 如果行号大于0，说明它上面有数字
                    up = dp[i - 1][j]
                if j > 0:
                    # 如果列号大于0，说明它左边有数字
                    left = dp[i][j - 1]
                dp[i][j] = max(up, left) + matrix[i][j]
        return dp[rows - 1][cols - 1]

    def gift2(self, matrix):
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        if cols <= 0 or rows <= 0:
            return 0

        dp = [0 for i in range(cols)] # 1d-array
        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0: # 上面有数字
                    up = dp[j]
                if j > 0: # 左边有数字
                    left = dp[j-1]
                dp[j] = max(up,left) + matrix[i][j]

        return dp[cols-1]


matrix = [[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]
s = Solution()
print(s.gift(matrix)) # 53
print(s.gift2(matrix)) # 53
