#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
要考虑次方是正数、负数和0，基数是0
-------------------------------
当n为偶数, a^n = a^(n/2) * a^(n/2)
当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
利用右移一位运算代替除以2
利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
优化代码速度
'''

#%% method 1 位操作
import time
def power(base,exponent):
     if base == 0.0 and exponent < 0:
        raise ValueError('0 cannot be divided')

     if exponent == 0:
         return 1
     if exponent == 1:
         return base
     if exponent == -1:
         return 1/base

     result = power(base, exponent >> 1) # 用右移一位来代替/2, recursion
     result *= result
     if (exponent & 0x1) == 1: # 用位与来判断奇偶，如果是奇数还需要乘以base
         result *= base
     return result

tic = time.time()
print(power(99.0,100))
print(time.time() - tic) # 0.000258

#%% 常规整除
import time
def power2(base,exponent):
    if base == 0.0 and exponent < 0:
        raise ValueError('0 cannot be divided')

    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent == -1:
        return 1 / base

    result = power2(base, exponent//2)
    result *= result
    if exponent % 2 == 1:
        result *= base

    return result

tic = time.time()
print(power2(99.0,100))
print(time.time() - tic) # 0.000253

