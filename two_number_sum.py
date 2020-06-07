'''
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

Sample Input
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
Sample Output
[-1, 11] // the numbers could be in reverse order
'''

'''
This can be solved with a brute force approach. In that case the time complexity would be O(n^2) and the space complexity O(1).
The solution shown below is much faster, although it requires O(n) space.
'''


def twoNumberSum(input_list, target_sum):
    cache = {}
    for i, num in enumerate(input_list):
        if target_sum - num in cache:
            return[num, target_sum - num]
        cache[num] = i
    return []


'''
Time: O(n)
Space: O(n)
'''


my_list = [3, 5, -4, 8, 11, 1, -1, 6]
my_target_sum = 10
print(twoNumberSum(my_list, my_target_sum))
