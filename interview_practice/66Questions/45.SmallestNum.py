#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
from functools import cmp_to_key
from itertools import permutations
class Solution:
    def BruteForce(self,nums):
        if not nums:
            return ''

        str_num = [str(i) for i in nums]
        perm = list(permutations(str_num))
        join = [''.join(i) for i in perm]
        return min(join)

    def compare(self, nums): # 若 ab > ba 则 b应该在a前面。
        if not nums:
            return ''

        str_num = [str(i) for i in nums]
        res = sorted(str_num, key=cmp_to_key(lambda a, b: int(a+b)-int(b+a))) # 比较ab, ba， sorted使最小的排在前面
        return ''.join(res)


nums = [3,32,321]
s = Solution()
print(s.BruteForce(nums)) # 321323
print(s.compare(nums))