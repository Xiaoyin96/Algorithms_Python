#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
from itertools import combinations
nums = list(range(10))
for i in combinations(nums,2):
    print(i)

# for num in lst:
#     x, y = num
#     print(x,y)

# for i in range(len(nums)-1):
#     # print(i)
#     x = nums[i]
#     for j in range(i+1,len(nums)):
#         # print(j)
#         y = nums[j]
#         print(x,y)