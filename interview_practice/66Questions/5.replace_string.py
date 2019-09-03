#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:40:42 2019

@author: xiaoyin

"""
'''
替换空格：
把字符串中的空格替换成'20%'
'''
#%% method 1
def replace(string):
    return string.replace(' ', '20%')

string = "We are happy."
print(replace(string))

#%% method 2
import re
string = "We are happy."
re.sub(' ', '20%', string, count=0, flags=0)