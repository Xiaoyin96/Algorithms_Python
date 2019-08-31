#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

nums = [-1, 2, 1]

def MaxSum(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [0] * n

    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(dp[i-1]+nums[i], nums[i])

    return max(dp)

nums = [1]
print(MaxSum(nums))