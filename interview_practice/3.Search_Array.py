#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:26:10 2019

@author: xiaoyin
"""
# Search duplicate elements in a 1D array. length: n, each element in [0,n-1]
#%% use hashmap
def find_array(array):
    '''
    input: 1D array
    output: duplicate element
    '''
    if array == []:
        return None
    
    dic = {}
    for num in array:
        if num not in dic.keys(): # use dict: O(n)
            dic[num] = 1
        else:
            dic[num] += 1
            return num
    return None
    


array = [2,3,1]
print(find_array(array))
            
#%% use index

class Solution:  
    def swap(self,array,i,j):
        '''
        swap the ith and jth element in an array
        '''
        assert i <= len(array) - 1 and j <= len(array) - 1
        
        if i == j:
            return array
        else:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            return array
    

    
    def duplicate(self, array):
        if array == []:
            return None
        
        for i in range(len(array)):
           if array[i] != i:
                if array[i] == array[array[i]]:
                    return array[i]
                else:
                    array = self.swap(array,array[i],i)
        return None   

dup = Solution()
array = [2,3,1,4,5,5,6]
print(dup.duplicate(array))
               