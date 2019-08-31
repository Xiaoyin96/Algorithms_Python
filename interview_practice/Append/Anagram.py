#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
两个字符串是否是变位词
'''

def Anagram(string1, string2):
    dic1 = {}
    dic2 = {}
    for s in string1:
        if s not in dic1:
            dic1[s] = 1
        else:
            dic1[s] += 1

    for s in string2:
        if s not in dic2:
            dic2[s] = 1
        else:
            dic2[s] += 1

    return dic1 == dic2

print(Anagram('abcccd','acbccd'))