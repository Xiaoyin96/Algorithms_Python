#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一个整形数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O（n）
Dynamic Programming
'''
class Solution:
    def max_sum(self, nums):
        if not nums or len(nums) <= 0:
            return 0

        curSum = 0
        maxSum = nums[0]
        for num in nums:
            if curSum <= 0:
                curSum = num
            else:
                curSum += num

            if curSum > maxSum:
                maxSum = curSum

        return maxSum

    def max_sum_dp(self, nums):
        if not nums or len(nums) <= 0:
            return 0
        dp = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0 or dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)

s = Solution()
nums = [1,-2,3,10,-4,7,2,-5]
print(s.max_sum(nums)) # 18
print(s.max_sum_dp(nums)) # 18
