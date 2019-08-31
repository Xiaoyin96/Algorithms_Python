#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元？
DP problem
dp[0] = 0，
dp[i] = min{dp[i - coins[j]] + 1}, 且 其中 i >= coins[j], 0 <= j < coins.length
'''
#%% DP
def coinChange(coins, amount):

    coins.sort()  # 给硬币从小到大排序
    dp = {0: 0} #初始化dp
    for i in range(1, amount + 1):
        dp[i] = float('inf') # upper limit，找最小值
        for coin in coins:
            if coin <= i: # coin < amount
                dp[i] = min(dp[i], dp[i-coin]+1)

    # for i in range(1, amount + 1):
    #     print('dp[%d]:'%(i), dp[i])

    if dp[amount] == float('inf'): #当最小硬币个数为初始值时，代表不存在硬币组合能构成此金额
            return -1
        else:
            return dp[amount]

print(coinChange([1,4,5], 22))

#%% recursion
def recursion_change(coins, amount):
    min_count = amount
    if amount in coins:
        return 1
    avail_coin = [i for i in coins if i < amount]
    for coin in avail_coin:
        count = 1 + recursion_change(coins, amount-coin)
        if count < min_count:
            min_count = count

    return min_count
import time
tic = time.time()
print(recursion_change([1,4,5], 22))
print(time.time() - tic)