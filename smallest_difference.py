'''
Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

You can assume that there will only be one pair of numbers with the smallest difference.

Sample Input
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
Sample Output
[28, 26]
'''


'''
SOLUTIONS:
    This problem can be solved using the brute force approach, comparing each of the elements of the first list to each of the elements of the second list. The time complexity would be O(mn), because of the two nested for loops. The space complexity would be O(1). (m and n are the lengths of the two lists).

    Can we do better??
    Yes, the solution below has time complexity O(mlogm + nlogn), where m and n are the lengths of the two lists. Space complexity is O(1).
'''
def smallest_difference(input_list_1, input_list_2):
    list_one.sort()
    list_two.sort()
    list_one_idx = 0
    list_two_idx = 0

    smallest_difference = abs(list_one[list_one_idx] - list_two[list_two_idx])
    smallest_difference_pair = [list_one[list_one_idx], list_two[list_two_idx]]
    while list_one_idx < len(list_one) and list_two_idx < len(list_two):
        if abs(list_one[list_one_idx] - list_two[list_two_idx]) < smallest_difference:
            smallest_difference = abs(list_one[list_one_idx] - list_two[list_two_idx])
            smallest_difference_pair = [list_one[list_one_idx], list_two[list_two_idx]]

        if list_one[list_one_idx] - list_two[list_two_idx] < 0:
            list_one_idx += 1
        elif list_one[list_one_idx] - list_two[list_two_idx] > 0:
            list_two_idx += 1
        else:
            return smallest_difference_pair
    return smallest_difference_pair


list_one = [-1, 5, 10, 20, 28, 3]
list_two = [26, 134, 135, 15, 17]
print(smallest_difference(list_one, list_two))


'''
Time: O(mlogm + nlogn) The runtime of the sorting algorithm, which is linearithmic, dwarfs the linear runtime O(m + n) of the while loop.
Space: O(1) We only store a constant number of variables: list_one_idx, list_two_idx, smallest_difference and smallest_difference_pair.
'''