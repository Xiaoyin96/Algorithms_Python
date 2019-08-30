#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

import random

def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if seq[j] < seq[min_idx]:
                min_idx = j
                # print(min_idx, seq[min_idx])

        if min_idx != i:
            seq[min_idx], seq[i] = seq[i], seq[min_idx]

    return seq

seq = list(range(20))
random.shuffle(seq)
print(seq)
print(select_sort(seq))