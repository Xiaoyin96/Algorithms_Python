#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？ 
e.g. f(8) = f(7) + f(6), 竖着放: f(n-1), 横着放，下面也必须横着放: f(n-2).
'''
class Soltuion():
    def cover(self, n):
        a, b =1, 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n+1):
            c = a + b
            a, b = b, c
        return c # here, b=c
s = Soltuion()
s.cover(10)

#%%
class Solution:
    def rectCover(self, number):
        # write code here
        if number<=0:
            return 0
        if number==1:
            return 1
        if number==2:
            return 2
        small,big=1,2
        for i in range(3,number+1):
            sum_i=small+big
            small=big
            big=sum_i
        return big

sol = Solution()
print(sol.rectCover(10))