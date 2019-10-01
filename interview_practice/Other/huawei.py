#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
import os

def path_join(url1, url2):

    if not url1 and not url2:
        return '/'

    if url1 and not url2:
        if url1[0] == '/':
            return url1
        elif url1[0] != '/':
            return '/' + url1

    if url2 and not url1:
        if url2[0] == '/':
            return url2
        elif url2[0] != '/':
            return '/' + url2

    if '/' not in url1:
        if '/' not in url2: # a + b = /a/b
            return '/' + url1 + '/' + url2
        elif url2[0] == '/':
            return '/' + url1 + url2 # a + /b = /a/b or a + /b/ = /a/b/


    if url1[0] == '/' and url1[-1] != '/':
        if url2[0] == '/': # /a + /b = /a/b or /a + /b/ = /a/b/
            return url1 + url2
        elif '/' not in url2: # /a + b = /a/b
            return url1 + '/' + url2

    if url1[0] == '/' and url1[-1] == '/' :
        if '/' not in url2: # /a/ + b = /a/b
            return url1 + url2
        elif url2[0] == '/':
            return url1[:-1] + url2




print(path_join('/a','/b'))
print(path_join('/a/','b'))
print(path_join('/a','b'))
print(path_join('a','/b'))
print(path_join('a','b'))
print(path_join('/a/','/b'))
print(path_join('','b'))
print(path_join('/a/',''))