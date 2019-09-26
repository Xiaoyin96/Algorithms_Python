#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
统计一个数字在排序数组（已经有顺序了！）中出现的次数。
'''

class Solution:
    def hash(self, array, num):
        if not array:
            return 0

        hash = {}
        for a in array:
            if a not in hash:
                hash[a] = 1
            else:
                hash[a] += 1

        return hash[num]

    def binary_search(self, data, k):
        # write code here
        number = 0
        if data != None and len(data) > 0:
            length = len(data)
            first = self.GetFirst(data, length, k, 0, length - 1)
            last = self.GetLast(data, length, k, 0, length - 1)
            if first > -1 and last > -1:
                number = last - first + 1
        return number

    def GetFirst(self, data, lenth, k, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if data[middle] == k:
            if middle > 0 and data[middle - 1] == k:
                end = middle - 1
            else:
                return middle
        elif data[middle] > k:
            end = middle - 1
        else:
            start = middle + 1
        return self.GetFirst(data, lenth, k, start, end)

    def GetLast(self, data, lenth, k, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if data[middle] == k:
            if middle < end and data[middle + 1] == k:
                start = middle + 1
            else:
                return middle
        elif data[middle] > k:
            end = middle - 1
        else:
            start = middle + 1
        return self.GetLast(data, lenth, k, start, end)

s = Solution()
arr = [1,2,3,3,3,3,4,5]
print(s.hash(arr,3))
print(s.binary_search(arr,3))



