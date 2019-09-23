#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
第一个只出现一次的字符
题：在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符。
'''

class Solution:
    def python_method(self, string):
        if not string:
            return None

        for s in string:
            if string.count(s) == 1:
                return s

    def hash(self, string):
        if not string:
            return None

        dict = {}
        for s in string:
            if s not in dict:
                dict[s] = 1
            else:
                dict[s] += 1

        for s in string:
            if dict[s] == 1:
                return s

s = Solution()
print(s.python_method('abaccedff'))
print(s.hash('abaccedff'))