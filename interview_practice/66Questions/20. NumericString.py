#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''

#%% built-in python
def isNumeric(string):
    try:
        if float(string):
            return True
    except:
        return False


#%% 考虑是否有e存在，如果有，e后面必须有数字，且必须是整数（正整数o或负整数），如果没有e存在，则判断它是不是普通的数字。
class solution:
    def isDigit(self, list):
        dotNum = 0
        element = ['0','1','2','3','4','5','6','7','8','9','+','-','.']
        for i, e in enumerate(list):
            if e not in element:
                return False
            if e == '.':
                dotNum += 1
            if e in ['+','-'] and i != 0:
                return False
        if dotNum > 1:
            return False

        return True


    def isNumeric(self, string):

        if len(string) <= 0 or not string:
            return False

        slist = [s.lower() for s in string]

        if 'e' in slist:
            idx = slist.index('e')
            left = slist[:idx]
            right = slist[idx+1:]
            if '.' in right or len(right) == 0:
                return False
            return self.isDigit(left) and self.isDigit(right)
        else:
            return self.isDigit(slist)

sol = solution()
print(sol.isNumeric('1.2.3'))
print(isNumeric('1.2.3'))

