'''
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

Sample Input
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
Sample Output
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
'''


def three_number_sum(input_list, target_sum):
    input_list.sort()

    triplets_list = []
    for i, num in enumerate(input_list[1:-1], 1):
        left_idx = 0
        right_idx = len(input_list) - 1
        while left_idx < i and right_idx > i:
            if input_list[left_idx] + num + input_list[right_idx] == target_sum:
                triplets_list.append([input_list[left_idx], num, input_list[right_idx]])
                right_idx -= 1
                left_idx += 1
            elif input_list[left_idx] + num + input_list[right_idx] > target_sum:
                right_idx -= 1
            else:
                left_idx += 1
    triplets_list.sort()
    return triplets_list


my_list = [12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5]
my_target_sum = 0
print(three_number_sum(my_list, my_target_sum))

'''
Time: O(n^2)
Space: O(n)
'''
