#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
翻转单词顺序，保持单词内部顺序不变
“student. a am I” --> "I am a student.”
'''

class Solution:
    def reverse1(self, string):
        if not string or len(string) <= 0:
            return ''

        line = string.split(' ')
        line = line[::-1]

        return ' '.join(line)

    def reverseTwice(self, string):
        if not string or len(string) <= 0:
            return ''

        str1 = self.reverse_core(string)  #'.tneduts a ma I'
        line = str1.split(' ')
        new_line = [self.reverse_core(s) for s in line]
        return ' '.join(new_line)



    def reverse_core(self, substr): # reverse a substring
        if not substr or len(substr) <= 0:
            return ''

        str_list = [ s for s in substr]

        l = 0
        r = len(str_list) - 1
        while l < r:
            str_list[l], str_list[r] = str_list[r], str_list[l]
            l += 1
            r -= 1

        return ''.join(str_list)



str = 'I am a student.'
s = Solution()
print(s.reverse1(str)) # student. a am I
print(s.reverse_core(str)) # .tneduts a ma I
print(s.reverseTwice(str)) # student. a am I