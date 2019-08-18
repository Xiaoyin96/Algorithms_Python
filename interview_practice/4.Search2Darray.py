#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:05:55 2019

@author: xiaoyin
"""

'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        col = cols - 1
        row = 0 # start from the right corner
        
        while col >= 0 and row <= rows - 1:
            num = matrix[row][col]
            if num ==  target:
                return True
            if num < target:
                row += 1
            if num > target:
                col -= 1
                
        return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 100

search = Solution()
print(search.searchMatrix(matrix, target))


    