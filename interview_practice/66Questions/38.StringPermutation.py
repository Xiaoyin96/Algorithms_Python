#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
class Solution:
    def method1(self, string):
        if not string:
            return None
        length = len(string)
        import itertools
        lst = list(itertools.permutations(string, length))
        new_list = []
        for item in lst:
            str = ''.join(item)
            if str:
                new_list.append(str)
        return list(set(new_list)) # no repeated permutation


    def method2(self, string): # recursion
        if not string:
            return []

        if len(string)==1:
            return list(string)

        p_list = []
        s_list = list(string)
        s_list.sort()

        for i in range(len(s_list)):
            if i>0 and s_list[i] == s_list[i-1]: # no repeated
                continue
            temp = self.method2(''.join(s_list[:i]) + ''.join(s_list[i+1:]))
            for item in temp:
                p_list.append(s_list[i] + item)

        return p_list


s = Solution()
print(s.method1('abcc')) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(s.method2('abcc'))