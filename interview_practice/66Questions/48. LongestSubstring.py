#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长字符串的长度。假设字符串中只包含‘a’-‘z’的字符。
例如，在字符串“arabcacfr”中，最长的不含重复字符的子字符串是“acfr”，长度为4。
DP
'''

class Solution:
    def find_substring(self, string):
        if not string:
            return 0

        if len(string) == 1:
            return 1

        start = 0
        maxLength = 0
        used = {}
        for i in range(len(string)):
            if string[i] in used and start <= used[string[i]]: # 重复出现的元素在现在子字符串的中间，重置开始位置
                start = used[string[i]] + 1
            else:
                maxLength = max(i - start + 1, maxLength)
            used[string[i]] = i

        return maxLength

s = Solution()
print(s.find_substring('arabcacfr')) # 4
print(s.find_substring('abcabcbb')) # 3


