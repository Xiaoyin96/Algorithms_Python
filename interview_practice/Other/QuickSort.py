#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

def quick_sort(array):

    if len(array) < 2:
        return array

    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot] # exclude pivot
    great = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(great)

import random
array = list(range(20))
random.shuffle(array)
print(array)
print(quick_sort(array))