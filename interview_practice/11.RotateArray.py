#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
使用二分法
'''

class Solution():
    def find_min(self, nums):

        n = len(nums)
        left = 0
        right = n-1
        mid = left
        while nums[left] >= nums[right]:
            if right - left == 1:
                return nums[right]
                break

            mid = int((left + right) / 2)
            # print(nums[left], nums[right], nums[mid])
            if nums[left] <= nums[mid]:
                left = mid
            if nums[right] >= nums[mid]:
                right = mid
            if nums[left] == nums[right] == nums[mid]:
                return min(nums) #必须遍历
        return nums[0] #如果顺序的话，第一个最小

sol = Solution()
nums = [3,4,5,6,1,2] # 0.00025s
num = [1,0,1,1,1,1] # 0.00012s
num1 = [1,2,3,4,5,6] # 0.000132s

#%%
import time
tic = time.time()
print(sol.find_min(num1))
print(time.time() - tic)