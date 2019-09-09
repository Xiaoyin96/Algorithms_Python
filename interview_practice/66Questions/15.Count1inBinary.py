#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
#%% binary calculation

print(1&0) # 0 与
print(0&0) # 0
print(1&1) # 1 或
print(1|0) # 1
print(1|1) # 1
print(1^1) # 0
print(1^0) # 1 异或，加法

#%% method 1
'''
把一个整数减去1，再和原整数做“与运算”，会把该整数最右边的1变成0。那么一个整数的二进制中表示中有多少个1，就可以进行多少次这样的操作。
'''

def solution1(n):
    count = 0
    if n < 0:
        n = n & 0xffffffff # 消除负数的影响

    while n:
        n = (n-1) & n
        count += 1

    return count



#%% python自带

def solution2(n):
    return bin(n & 0xffffffff).count("1")

print(bin(-99 & 0xffffffff))
print(solution1(-99))
print(solution2(-99))

#%%
'''
判断一个整数是不是2的整数次方: 二进制只会有一位是1，其他都是0
'''
def powerof2(num):
    return num & (num-1) == 0 # 唯一的1变成0，==0

print(powerof2(8))
print(powerof2(15))

#%%
'''
判断两个数的二进制表示有多少位不一样, 直接比较两个数的二进制异或, 再看里面有多少个1
'''
def diff(num1, num2):
    dif = num1^num2 # 按位异或，如果每位都一样,1^1 or 0^0，就是0，如果不一样才会有1
    cnt = 0
    while dif:
        dif = (dif - 1)&dif
        cnt += 1

    return cnt
print(bin(100), bin(99))
print(diff(100,99))