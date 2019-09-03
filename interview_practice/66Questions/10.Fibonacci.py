#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''



#%% Sol 1, iteration
import time
class Solution():
    def Fib(self,n):
        a, b = 0, 1
        if n == 0:
            return 0
        elif n == 1:
            return 1

        for i in range(2,n+1):
            c = a + b
            a, b = b, c
        return b

tic = time.time()
sol = Solution()
print(sol.Fib(30))
print('Time elapsed', time.time()-tic)  #0.00069

#%% Sol 2, generator
import time
class Solution2():
    def fib_yield(self,num):
        a, b = 0, 1
        for i in range(num):
            yield b
            a, b = b, a + b
    def fib(self, num):
        return list(self.fib_yield(num))[-1]

tic = time.time()
sol2 = Solution2()
print(sol2.fib(30))
print('Time elapsed', time.time()-tic) #0.00021 fastest! using generator

#%% Sol 3, resursion
class Solution3():
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        return self.fib(n-1) + self.fib(n-2)

tic = time.time()
sol3 = Solution3()
print(sol3.fib(30))
print('Time elapsed', time.time()-tic) # 0.53 too slow