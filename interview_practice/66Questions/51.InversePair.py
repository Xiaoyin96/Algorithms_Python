#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
'''
import copy
class Solution:
    def brute_force(self, array):
        if not array or len(array) <= 1:
            return 0

        cnt = 0
        for i in range(len(array)-1):
            for j in range(i+1, len(array)):
                if array[i] > array[j]:
                    cnt += 1

        return cnt

    def merge_sort(self, array):
        pass

    def method3(self, array):
        if not array or len(array) <= 1:
            return 0
        arr = copy.deepcopy(array)
        arr.sort()
        cnt = 0

        for i in range(len(arr)):
            cnt += array.index(arr[i])
            array.remove(arr[i])

        return cnt


s = Solution()
array = [7,5,6,4]
arr = [1,2,3,4,5,6,7,0]
print(s.brute_force(array))
print(s.brute_force(arr))
print(s.method3(array))
print(s.method3(arr))