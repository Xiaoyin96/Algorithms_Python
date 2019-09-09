#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
https://leetcode.com/problems/regular-expression-matching/
'''
#%% recursion: time limit exceeds
class solution:
    def match(self, string, pattern):

        if len(string) == 0 and len(pattern) == 0: # recursion's break condition
            return True

        if len(string) > 0 and len(pattern) == 0:
            return False

        # case 1 pattern第二个元素是*
        if len(pattern) > 1 and pattern[1] == '*':
        # 如果字符串第一个模式跟模式第一个字符匹配(相等或匹配到".")，可以有3种匹配方式：
            if len(string) > 0 and ( string[0] == pattern[0] or pattern[0] == '.'):
                # 1、模式后移2字符，相当于X*被忽略
                # 2、字符串后移1字符，模式后移两字符；
                # 3、字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位
                return self.match(string, pattern[2:]) or self.match(string[1:], pattern[2:]) or self.match(string[1:], pattern)
            else: # 第一位不匹配，跳过pattern里的*
                return self.match(string, pattern[2:])

        # case 2 pattern第二个元素不是*
        if len(string) > 0 and (string[0] == pattern[0] or pattern[0] == '.'):
            return self.match(string[1:], pattern[1:])

        return False

#%% dynamic programming
class Solution:
    def isMatch(self, s, p):
        # Initialize DP table
        # Row indices represent the lengths of subpatterns
        # Col indices represent the lengths of substrings
        T = [
            [False for _ in range(len(s)+1)]
            for _ in range(len(p)+1)
        ]

        # Mark the origin as True, since p[:0] == "" and s[:0] == ""
        T[0][0] = True

        # Consider all subpatterns p[:i], i > 0 against empty string s[:0]
        for i in range(1, len(p)+1):
            # Subpattern matches "" only if it consists of "{a-z}*" pairs
            T[i][0] = i > 1 and T[i-2][0] and p[i-1] == '*'

        # Consider the empty pattern p[:0] against all substrings s[:j], j > 0
        # Since an empty pattern cannot match non-empty strings, cells remain False

        # Match the remaining subpatterns (p[:i], i > 0) with the remaining
        # substrings (s[:j], j > 0)
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):

                # Case 1: Last char of subpattern p[i-1] is an alphabet or '.'
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    T[i][j] |= T[i-1][j-1]

                # Case 2: Last char of subpattern p[i-1] is '*'
                elif p[i-1] == '*':

                    # Case 2a: Subpattern doesn't need '*' to match the substring

                    # If the subpattern without '*' matches the substring,
                    # the subpattern with '*' must still match
                    T[i][j] |= T[i-1][j]

                    # If the subpattern without '*' and its preceding alphabet
                    # matches the substring, then the subpattern with them
                    # must still match
                    T[i][j] |= i > 1 and T[i-2][j]

                    # Case 2b: Subpattern needs '*' to match the substring

                    # If the alphabet preceding '*' matches the last char of
                    # the substring, then '*' is used to extend the match for
                    # the substring without its last char
                    if i > 1 and p[i-2] == s[j-1] or p[i-2] == '.':
                        T[i][j] |= T[i][j-1]

        return T[-1][-1]




#%% bult-in re
import re
class Solution3:
    def isMatch(self, s, p):
        result = re.match(p, s)
        if result and result.start() == 0 and result.end() == len(s):
            return True
        return False

