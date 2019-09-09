#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入数字n, 按顺序打印从1最大的n位十进制数
比如输入3, 则打印出1、2、3、到最大的3位数即999
python整型不会溢出！！int到32位自动转成Long
'''

def Print(n):
    if n == 0:
        return 0
    for i in range(1,10**n):
        print(i)

Print(3)
