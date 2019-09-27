#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S
如果有多对数字的和等于S，输出任意一对
'''
class Solution:
    def brute_force(self, array, s): # time: O(n2)
        if not array or not s:
            return None

        for i in range(len(array)):
            res = s - array[i]
            for j in range(i+1, len(array)):
                if array[j] == res:
                    return array[i], array[j]

        return None

    def hash(self, array, s):
        if not array or not s:
            return None

        hash = {}
        for num in array:
            if num not in hash:
                hash[num] = s - num
            if hash[num] in array:
                return num, hash[num]

        return None

    def TwoPointer(self, array, s): # array is sorted already, time: O(n)
        if not array or not s:
            return None

        l = 0
        r = len(array) - 1

        while l < r:
            if array[l] + array[r] == s:
                return array[l], array[r]
            elif array[l] + array[r] > s:
                r -= 1
            elif array[l] + array[r] < s:
                l += 1
        return None

s = Solution()
arr = [1,2,4,7,11,15]
print(s.brute_force(arr,15)) # (4,11)
print(s.hash(arr,15))
print(s.TwoPointer(arr,15))

#%%
'''
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
class Solution:
    def ContinuousSeq(self, sum):
        if sum < 3:
            return None

        small = 1
        big = 2
        mid = (1+sum)//2 # small的上限
        res = []
        curSum = small + big

        while small < mid:
            if curSum == sum:
                res.append(list(range(small, big+1)))
            while curSum > sum and small < mid:
                curSum -= small
                small += 1
                if curSum == sum:
                    res.append(list(range(small, big+1)))

            big += 1
            curSum += big

        return res


s = Solution()
print(s.ContinuousSeq(15)) # [[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]
