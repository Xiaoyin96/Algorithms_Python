#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
给你一根长度为n的绳子，请把绳子剪成m段(m,n都是整数，且n>1,m>1),每段绳子的长度记为k[0],k[1],k[2],...,k[m]。请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
例如，当绳子的长度为8时，我们把它剪成长度分别为2，3，3的三段，此时得到的最大乘积为18。
'''
#%% method 1 dynamic programming
## time: O(n2), space: O(n)

def DP_cut(n):
    product = [0] * (n+1)
    if n < 2:
        return 0
    if n == 2: # n>1 and m>1
        return 1
    if n == 3:
        return 2

    product[0] = 0
    product[1] = 1
    product[2] = 2
    product[3] = 3


    for i in range(4,n+1):
        max = 0
        for j in range(1, i//2+1): # range(1,i)也可以，多循环半个loop, 最短的长度是1，但是不增加max, 所以至少长度是2
            prod= product[i-j] * product[j]
            if max < prod:
                max = prod
            product[i] = max

    return product[n]

print(DP_cut(8))

#%% method 2: greedy algorithm
# n >=5 m = 3 then m = 2, time, space: O(1)

def greedy_cut(n):
    if n < 2:
        return 0
    if n == 2:  # n>1 and m>1
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4

    t3 = n // 3 # 尽可能多剪3
    if n - t3 * 3 == 1:
        t3 -= 1 # 剩下4

    t2 = (n - t3 * 3) // 2 # 剩下的剪2

    return (3**t3) * (2**t2)

print(greedy_cut(8))
print(DP_cut(8))






