'''
Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.

Sample Input
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
Sample Output
6 // 0, 10, 6, 5, -1, -3
'''

def longest_peak(input_list):
    length_of_longest_peak = 0
    for i, num in enumerate(input_list[1:len(input_list) - 1], 1):
        left_idx = i - 1
        right_idx = i + 1
        if input_list[left_idx] < input_list[i] and input_list[right_idx] < input_list[i]:
            current_peak_length = 3
            while left_idx > 0 and input_list[left_idx] > input_list[left_idx - 1]:
                current_peak_length += 1
                left_idx -= 1
                if left_idx < 1:
                    break
            while right_idx < len(input_list) - 1 and input_list[right_idx] > input_list[right_idx + 1]:
                current_peak_length += 1
                right_idx += 1
                if right_idx > len(input_list) - 1:
                    break
        else:
            continue
        length_of_longest_peak = max(length_of_longest_peak, current_peak_length)
    return length_of_longest_peak


my_list = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longest_peak(my_list))


'''
Time: O(n)
Space: O(1)
'''