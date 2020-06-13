'''
Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.

Sample Input
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
Sample Output
3
'''

'''
SOLUTION:
  This is the implementation of binary search. We use a "divide and conquer" approach, dividing the problem in half at each iteration.
  Therefore the time complexity is logarithmic. Space complexity is constant, since we will always need to store only three variables (left_idx, right_idx and guess_idx).

    Time: O(log(n))
    Space: O(1)
'''


def binary_search(input_list, target):
    left_idx = -1
    right_idx = len(input_list)

    while left_idx + 1 < right_idx:
        guess_idx = left_idx + (right_idx - left_idx) // 2
        if target < input_list[guess_idx]:
            right_idx = guess_idx
        elif target > input_list[guess_idx]:
            left_idx = guess_idx
        else:
            return guess_idx

    return -1


my_list = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
my_target = 73
print(binary_search(my_list, my_target))
