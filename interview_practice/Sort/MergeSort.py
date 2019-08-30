#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

import random

def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        mid = int(len(seq)/2)
        left = merge_sort(seq[:mid])
        right = merge_sort(seq[mid:])

    new_seq = merge_sorted(left, right)
    return new_seq

def merge_sorted(left, right):
    '''

    :param left: sorted list,
    :param right: sorted list
    :return: one sorted list
    '''
    a = len(left)
    b = len(right)
    l = r = 0
    sorted = []

    while l < a and r < b:
        if left[l] < right[r]:
            sorted.append(left[l])
            l += 1
        else:
            sorted.append(right[r])
            r += 1

    if l < a: # a中还有元素
        sorted.extend(left[l:])
    else:
        sorted.extend(right[r:])

    return sorted

# left = list(range(10))
# right = list(range(5))
# print(merge_sorted(left, right))
seq = list(range(20))
random.shuffle(seq)
print(seq)
print(merge_sort(seq))