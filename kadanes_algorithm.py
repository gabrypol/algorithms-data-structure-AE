'''
Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by summing up all of the integers in a non-empty subarray of the input array. A subarray must only contain adjacent numbers.

Sample Input
array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
Sample Output
19 // [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]
'''

def kadanes_algorithm(input_list):
    max_so_far = input_list[0]
    max_ending_at_current = input_list[0]
    for i, num in enumerate(input_list[1:], 1):
        max_ending_at_current = max(num, max_ending_at_current + num)
        max_so_far = max(max_so_far , max_ending_at_current)
    return max_so_far


my_list = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanes_algorithm(my_list))

'''
Time: O(n)
Space: O(1)
'''