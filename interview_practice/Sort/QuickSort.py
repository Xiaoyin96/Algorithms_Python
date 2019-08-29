#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
import random

#%% method 1: 每次遍历找partition
def quick_sort(seq):

    length = len(seq)
    if length == 1 or length == 0: # 递归出口
        return seq

    idx = 0
    pivot = seq[idx]

    less = [i for i in seq[idx+1:] if i <= pivot] # 每次遍历
    great = [i for i in seq[idx+1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(great)

array = list(range(10))
random.shuffle(array)

print(quick_sort(array))

#%% method 2: 一次遍历找less and great
import sys
sys.setrecursionlimit(1500)

def partition(seq, beg, end):
    pivot = seq[beg] # beginning index as pivot index
    left = beg + 1
    right = end - 1

    while True:
        while left <= right and seq[left] <= pivot:
            left += 1

        while right >= left and seq[right] > pivot:
            right -= 1

        if left > right:
            break
        else: # swap left and right
            seq[left], seq[right] = seq[right], seq[left]

    # swap pivot and right pointer
    seq[beg], seq[right] = seq[right], seq[beg] # inplace
    return right # 新的pivot位置


# # partition(seq, 0, 6)

def quicksort_inplace(seq, beg, end): # 左开右闭
    if beg < end: # beg == end: 递归出口
        pivot = partition(seq, beg, end)
        quicksort_inplace(seq, beg, pivot) # inplace的sort,没有return
        quicksort_inplace(seq, pivot+1, end)

seq = [9,2,3,4,6,8,7,11,15,0]
quicksort_inplace(seq, 0, len(seq))
print(seq)

