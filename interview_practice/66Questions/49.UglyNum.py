#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
class Solution:
    def brute_force(self, N):
        if N <= 0:
            return 0

        num = 0
        cnt = 0
        while cnt < N:
            num += 1
            if self.isUgly(num):
                cnt += 1

        return num

    def isUgly(self, num):
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5

        if num == 1:
            return True
        else:
            return False

    def space(self, N):
        if N <= 0:
            return 0

        res = [1]
        cur = 1
        t2 = t3 = t5 = 0
        while cur < N:
            min_val = min(res[t2]*2,res[t3]*3,res[t5]*5) # 下一个最小的ugly num
            res.append(min_val)
            # 更新t2,t3,t5
            while res[t2] * 2 <= min_val:
                t2 += 1
            while res[t3] * 3 <= min_val:
                t3 += 1
            while res[t5] * 5 <= min_val:
                t5 += 1
            cur += 1

        return res[N-1]


s = Solution()
print(s.brute_force(150)) # 5832
print(s.space(1500)) # faster! 859963392