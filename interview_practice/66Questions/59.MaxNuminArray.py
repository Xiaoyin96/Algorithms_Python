#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
滑动窗口的最大值, array, k (size of sliding windows)
'''
class Solution:
    def brute_force(self, array, k): # time: O(nk)
        if not array or k <= 0 or len(array) < k:
            return []

        l = 0
        r = k
        win = []
        while r <= len(array):
            idx = list(range(l,r))
            seq = []
            for i in idx:
                seq.append(array[i])
            max_num = max(seq)
            win.append(max_num)
            l += 1
            r += 1

        return win

    def deque(self, num, k):
        if not array or k <= 0 or len(array) < k:
            return []

        res = []
        deque = []
        for i in range(k): # first k num
            while deque and num[i] >= num[deque[-1]]:
                deque.pop()
            deque.append(i)

        for i in range(k, len(num)): # k ~ length
            res.append(num[deque[0]])
            while (deque and num[i] >= num[deque[-1]]):
                deque.pop()
            if deque and deque[0] <= i - k:
                deque.pop(0)
            deque.append(i)
        res.append(num[deque[0]])
        return res


array = [1,2,3,4,5,6,7]
k = 3
s = Solution()
print(s.brute_force(array, k))
print(s.deque(array,k))