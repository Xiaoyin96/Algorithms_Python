#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
要求：空间O(n), 时间O(1)
'''
class Solution:

    def FindNumsAppearOnce(self, array):

        from collections import Counter

        res=Counter(array).most_common()[-1:]
        return res[0][0]

arr = [2,3,4,5,2,3,4]
s = Solution()
print(s.FindNumsAppearOnce(arr))