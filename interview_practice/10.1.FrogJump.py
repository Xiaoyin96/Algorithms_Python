#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
f(n) = f(n-1) + f(n-2)
'''
class Solution():
    def jump(self,n):
        a, b = 1, 2
        if n == 1:
            return 1
        elif n == 2:
            return 2

        for i in range(3, n+1):
            c = a + b
            a, b = b, c
        return b
sol = Solution()
print(sol.jump(50))

#%%
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number==1:
            return 1
        if number==2:
            return 2
        small,big=1,2
        for i in range(2,number):
            sum_i=small+big
            small=big
            big=sum_i
        return big

sol = Solution()
print(sol.jumpFloor(50))