#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
Binary Search
https://leetcode.com/problems/binary-search/
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((right + left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
