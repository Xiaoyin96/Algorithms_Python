#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''
import random
class Solution:
    def sort_find(self, nums):
        if not nums:
            return None

        length =  len(nums)
        nums.sort()
        if length % 2 == 1:
            return nums[length//2]
        else:
            return (nums[length//2-1] + nums[length//2])/2

    def heapq_find(self, nums): # 使用最大堆、最小堆, 待补充
        if not nums:
            return None
        pass

nums = list(range(1,100))
random.shuffle(nums)

s = Solution()
print(s.sort_find(nums)) # 50

