'''
Given an array of positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, write a function that returns the smallest number of coins needed to make change for that target amount using the given coin denominations.

If it's impossible to make change for the target amount, return -1.

Note that an unlimited amount of coins is at your disposal.

Sample Input
n = 7
denoms = [1, 5, 10]
Sample Output
3 // 2x1 + 1x5
'''

def min_number_of_coins(n, denoms):
    min_coins = [float('inf') for amount in range(n + 1)]
    min_coins[0] = 0

    for i, denom in enumerate(denoms):
        for amount in range(len(min_coins)):
            if denom <= amount:
                min_coins[amount] = min(min_coins[amount - denom] + 1, min_coins[amount])
    return min_coins[amount] if min_coins[amount] != float('inf') else -1


change = 7
denominations = [1, 5, 10]
print(min_number_of_coins(change, denominations))

'''
Time: O(n*d) where n is the target amount and d is the number of coin denominations.
Space: O(n)
'''