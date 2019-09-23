#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一个整数n,求1~n这n个整数的十进制表示中1出现的次数。例如，输入12，1~12这些整数中包含1的数字有1，10，11，12一共出现了5次。
'''
import time

class solution:
    def count(self, n):
        cnt = 0
        for i in range(1,n+1):
            cnt += self.core(i)

        return cnt

    def core(self, num):
        cnt = 0
        while num:
           if num % 10 == 1:
               cnt += 1
            num = num//10
        return cnt

    def count_string(self, n):
        cnt = 0
        for i in range(1, n+1):
            string = str(i)
            cnt += string.count('1')

        return cnt

s = solution()
tic1 = time.time()
print(s.count(120000))
print(time.time() - tic1)
tic2 = time.time()
print(s.count_string(120000)) # faster
print(time.time() - tic2)