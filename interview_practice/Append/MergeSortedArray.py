#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
合并两个有序列表
'''
#%% method 1
def merge_sorted_list(arr1, arr2):
    a = len(arr1)
    b = len(arr2)
    l = r = 0
    arr = []

    while l < a and r < b:
        if arr1[l] < arr2[r]:
            arr.append(arr1[l])
            l += 1
        else:
            arr.append(arr2[r])
            r += 1

    if l < a:
        arr.extend(arr1[l:])
    else:
        arr.extend(arr2[l:])

    return arr

arr1 = list(range(10))
arr2 = list(range(5))

print(merge_sorted_list(arr1, arr2))

#%% tail recursion

def recursion_merge_sort(l1, l2, temp):
    if len(l1) == 0 or len(l2) == 0: # 递归出口
        temp.extend(l1)
        temp.extend(l2)
        return temp
    else:
        if l1[0] < l2[0]:
            temp.append(l1[0])
            del l1[0]
        else:
            temp.append(l2[0])
            del l2[0]
        print(l1, l2, temp)

        return recursion_merge_sort(l1, l2, temp)


arr1 = list(range(10))
arr2 = list(range(5))

print(recursion_merge_sort(arr1, arr2, []))

#%% method 3 loop
def loop_merge_sort(l1, l2):
    temp = []
    while len(l1) > 0 and len(l2) > 0: # 停止的条件是l1,l2中有一个遍历完了
        if l1[0] < l2[0]:
            temp.append(l1[0])
            del l1[0]
        else:
            temp.append(l2[0])
            del l2[0]

    temp.extend(l1)
    temp.extend(l2) # l1, l2里有一个为空了

    return temp

arr1 = list(range(10))
arr2 = list(range(5))

print(loop_merge_sort(arr1, arr2))
