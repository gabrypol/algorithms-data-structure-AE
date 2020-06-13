'''
Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array.

If a sum can't be generated, the function should return 0.

Sample Input
array = [75, 105, 120, 75, 90, 135]
Sample Output
330 // 75, 120, 135
'''

def max_subset_sum_no_adjacent(input_list):
    if len(input_list) == 0:
        return 0
    if len(input_list) == 1:
        return input_list[0]

    input_list[1] = max(input_list[:2])
    for i, num in enumerate(input_list[2:], 2):
        input_list[i] = max(input_list[i - 2] + input_list[i], input_list[i - 1])
    return input_list[-1]

my_list = [75, 105, 120, 75, 90, 135]
my_list = [4, 3, 5, 200, 5, 3]
print(max_subset_sum_no_adjacent(my_list))


'''
Time: O(n)
Space: O(1)
'''