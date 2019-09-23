#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成“a”，1翻译成“b”，……，11翻译成“1”,……，25翻译成“z”。一个数字可能有多个翻译。
例如：12258有5种不同的翻译，分别是“bccfi”、“bwfi”、“bczi”、“mcfi”和“mzi”。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
递归思路，从尾部开始避免重复解决子问题 f(i) = f(i+1) + g(i,i+1)*f(i+2), g(i,i+1)=1 when 10-25
'''
class Solution:
    def count(self, num):
        if num < 0:
            return 0

        string = str(num)
        return self.core(string)

    def core(self, string):
        length = len(string)
        dp = [0] * length

        for i in range(length-1, -1, -1) : # 倒序，从num[length-1] -> num[0]
            count = 0
            if i < length - 1:
                count += dp[i+1]
            else:
                count = 1 # 起始

            if i < length - 1:
                dig1 = int(string[i])
                dig2 = int(string[i+1])
                total = dig1*10 + dig2 # 两位数
                if 10 <= total <= 25:
                    if i < length - 2: # 针对i+2的条件
                        count += dp[i+2]
                    else:
                        count += 1

            dp[i] = count

        return dp[0]

s = Solution()
print(s.count(12238)) # 5
print(s.count(0)) # 1
print(s.count(-1)) # 0