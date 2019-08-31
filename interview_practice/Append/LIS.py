#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
给定一个未经排序的整数数组，寻找最长递增子序列的长度。 (LIS)
'''

nums = [2 ,1, 5, 3, 6 ,4 ,8 ,9, 7]

def Longest(nums):
    if not nums:
        return 0
    size = len(nums)
    dp = [1] * size
    for i in range(size):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(Longest(nums))
print(Longest([]))