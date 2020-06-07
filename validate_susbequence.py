'''
Validate Subsequence
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
Sample Output
true
'''


def validate_subsequence(input_list, input_sequence):
    sequence_idx = 0
    for i, num in enumerate(input_list):
        if sequence_idx == len(input_sequence):
            break
        if num == input_sequence[sequence_idx]:
            sequence_idx += 1

    return sequence_idx == len(input_sequence)


my_list = [1, 1, 1, 1, 1, 1]
my_sequence = [1, 1, 1]
print(validate_subsequence(my_list, my_sequence))


'''
Time: O(n)
Space: O(1)
'''
