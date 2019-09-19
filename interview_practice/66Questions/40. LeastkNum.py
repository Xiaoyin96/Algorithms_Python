#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''
import heapq
import random
import time
class solution:
    def sort_find(self,nums,k): # time: O(nlogn)
        if not nums or len(nums) < k:
            return None

        nums.sort() # built-in sort function or use quick-sort partition
        return nums[:k]
    def heapq_builtin(self, nums, k):
        if not nums or len(nums) < k:
            return None

        return heapq.nsmallest(k, nums)



nums = [4,5,1,6,2,7,3,8]
nums1 = [2,3,1]
nums2 = list(range(100000))
random.shuffle(nums2)
# print(nums2)

s = solution()
tic1 = time.time()
print(s.sort_find(nums2,10)) # 0.066s
print(time.time() - tic1)

tic2 = time.time()
print(s.heapq_builtin(nums2,10)) # 0.0035s much faster
print(time.time() - tic2)
