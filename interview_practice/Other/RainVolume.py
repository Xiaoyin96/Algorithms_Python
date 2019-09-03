#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

def Volume(array):
    v = 0
    l, r = 0, len(array) - 1
    l_max, r_max = 0, 0

    while l < r:
        if array[l] < array[r]:
            if array[l] >= l_max:
                l_max = array[l]
            else:
                v += l_max - array[l]
            l += 1
        else:
            if array[r] >= r_max:
                r_max = array[r]
            else:
                v += r_max - array[r]
            r -= 1
    return v

array1 = [2, 1, 3, 4, 0, 3, 0, 0 ,1]
array2 = [2, 1, 3, 0, 3, 0, 0 ,1]
array3 = [0, 1, 3, 0, 0, 1, 0]
array4 = [1,2,3]
array5 = [1]
array6 = []
print(Volume(array1))
assert Volume(array1) == Volume(array2) == 6
assert Volume(array3) == 2
assert Volume(array4) == Volume(array5) == Volume(array6) == 0




