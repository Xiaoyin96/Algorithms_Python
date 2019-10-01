#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

s = '(a,b)'

lst = [(3,6),(1,5),(6,7)]


def available(tuple1, tuple2):  # tuple1[0] <= tuple2[0], sorted
    if not tuple1 or not tuple2:
        return False

    if tuple1[1] <= tuple2[0]:
        return True
    return False
#
# print(available((1,3),(2,6)))

res = []
max = 0
for i in range(len(lst)):
    temp = []
    temp.append(lst[i])
    for j in range(i+1, len(lst)):
        if available(temp[-1], lst[j]):
            temp.append(lst[j])
    if len(temp) >= max:
        res.append(temp)
        max = len(temp)

print(res)

