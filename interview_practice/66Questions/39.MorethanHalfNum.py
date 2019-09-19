#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
数组中出现次数超过一半的数字
'''
class solution:
    def find_num(self, nums):
        if not nums:
            return None

        length = len(nums)
        if length == 1:
            return nums

        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
            if hash[num] > length/2:
                return num

    def partition(self, nums):

nums = [1,2,3,2,2,2,5,4,2]
num1 = [1,2]
s = solution()
print(s.find_num(num1))