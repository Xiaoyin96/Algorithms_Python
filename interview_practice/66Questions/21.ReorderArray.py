#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

#%%
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
'''
class solution:
    def swap(self, array):
        if len(array) == 0 or not array:
            return None

        pBegin = 0
        pEnd = len(array) - 1

        while pBegin < pEnd:
            while pBegin < pEnd and not self.isEven(array[pBegin]):
                pBegin += 1
            while pBegin < pEnd and self.isEven(array[pEnd]):
                pEnd -= 1
            #swap
            array[pBegin], array[pEnd] = array[pEnd], array[pBegin]
        return array


    def isEven(self, num):
        return num % 2 == 0

arr = [1,2,3,4,5]
s = solution()
print(s.swap(arr))

#%%
'''
在题一基础上，要求奇数和奇数，偶数和偶数的相对位置保持不变。
'''
def reorder(array):
    if len(array) == 0 or not array:
        return None

    odd = []
    even = []
    for num in array:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return odd + even

arr = [1,2,3,4,5]
print(reorder(arr))