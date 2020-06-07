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
SOLUTION 1:
    This can be solved with a brute force approach. In that case the time complexity would be O(n^2) and the space complexity O(1).
    The solution shown below is much faster, although it requires O(n) space.
        Time: O(n^2)
        Space: O(1)

SOLUTION 2:
    A second solution is to sort the input_list first and then use a left_pointer and right_pointer. If the current sum is greater than target_sum, then move the right pointer by one to the left. If the current sum is less than target_sum, then move the left pointer by one to the right. Else, if the current sum is equal to target_sum, then return the items of the list at left_pointer and right_pointer.
    The time complexity is nlogn, because good sorting algorithms sort in nlogn time. Space complexity is constant O(1).
        Time: O(nlogn)
        Space: O(1)


def twoNumberSum(input_list, target_sum):
    input_list.sort()

    left_pointer = 0
    right_pointer = len(input_list) - 1
    while (left_pointer < right_pointer):
        if input_list[left_pointer] + input_list[right_pointer] < target_sum:
            left_pointer += 1
        elif input_list[left_pointer] + input_list[right_pointer] > target_sum:
            right_pointer -= 1
        else:
            return [input_list[left_pointer], input_list[right_pointer]]
    return []


SOLUTION 3 (see below):
    We use dynamic programming and store the visited items in a dictionary. This is the fastest solution, although it needs linear space.
        Time: O(n)
        Space: O(n)
'''


def twoNumberSum(input_list, target_sum):
    cache = {}
    for i, num in enumerate(input_list):
        if target_sum - num in cache:
            return[num, target_sum - num]
        cache[num] = i
    return []


my_list = [3, 5, -4, 8, 11, 1, -1, 6]
my_target_sum = 10
print(twoNumberSum(my_list, my_target_sum))
