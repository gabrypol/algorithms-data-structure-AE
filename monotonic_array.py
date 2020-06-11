'''
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Sample Input
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
Sample Output
true
'''

def monotonic_list(input_list):
    is_monotonic_ascending = True
    is_monotonic_descending = True
    for i, num in enumerate(input_list[1:], 1):
        if input_list[i] > input_list[i - 1]:
            is_monotonic_descending = False
        elif input_list[i] < input_list[i - 1]:
            is_monotonic_ascending = False
        # Runtime optimization: the following two lines of code break the for loop returning False if the list in not monotonic ascending AND descending. If both conditions materialize, the statement below avoids going through the whole list.
        if not is_monotonic_descending and not is_monotonic_ascending:
            return False
    return is_monotonic_ascending or is_monotonic_descending

my_list = [1, 5, 10, 1100, 1100, 1101, 1102, 9001]
print(monotonic_list(my_list))

'''
Time: O(n)
Space: O(1)
'''