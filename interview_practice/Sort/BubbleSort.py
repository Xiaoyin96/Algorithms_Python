#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

import random

def bubble_sort(seq):
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]

    return seq

seq = list(range(20))
random.shuffle(seq)
print(seq)
print(bubble_sort(seq))
assert bubble_sort(seq) == list(range(20))