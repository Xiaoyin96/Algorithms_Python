#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

import random

def insert_sort(seq):

    n = len(seq)
    for i in range(1,n):
        val = seq[i]
        pos = i
        while pos > 0 and val < seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = val # insert value

    return seq

seq = list(range(20))
random.shuffle(seq)
print(seq)
print(insert_sort(seq))