'''
Given an array of positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, write a function that returns the number of ways to make change for that target amount using the given coin denominations.

Note that an unlimited amount of coins is at your disposal.

Sample Input
n = 6
denoms = [1, 5]
Sample Output
2 // 1x1 + 1x5 and 6x1
'''


def n_of_ways_to_make_change(n, denoms):
    min_coins = [0] * (n + 1)
    min_coins[0] = 1

    for i, denom in enumerate(denoms):
        for amount in range(len(min_coins)):
            if denom <= amount:
                min_coins[amount] += min_coins[amount - denom]
    return min_coins[n]

change = 6
denominations = [1, 5]
print(n_of_ways_to_make_change(change, denominations))

'''
Time: O(n*d) where n is the target amount and d is the number of denominations
Space: O(n)
'''