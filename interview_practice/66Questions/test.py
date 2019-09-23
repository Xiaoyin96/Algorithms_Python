#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
n = 5
nums = [1,3,4,2,5]
cnt = 0
for i in range(n):
    for j in range(i+1, n):

        print(nums[i], nums[j])
        if nums[i] > nums[j]:
            cnt += abs(i-j)

cnt = 0
for i in range(n):
    if i!= n-1 and min(nums[i+1:])>nums[i]:
        continue
    for j in range(i+1, n):
        if nums[i] > nums[j]:
            cnt += abs(i-j)
print(cnt)
