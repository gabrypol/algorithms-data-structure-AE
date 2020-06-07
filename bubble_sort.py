'''
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort algorithm to sort the array.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output
[2, 3, 5, 5, 6, 8, 9]
'''


def bubble_sort(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
      return input_list

    while True:
        sorted_pairs = 0
        for i, num in enumerate(input_list[1:], 1):
            if input_list[i] < input_list[i - 1]:
                input_list[i], input_list[i - 1] = input_list[i - 1], input_list[i]
                sorted_pairs += 1
        if sorted_pairs == 0:
            return input_list


my_list = [8, 5, 2, 9, 5, 6, 3]
print(bubble_sort(my_list))


'''
Time: O(n^2)
Space: O(1) We store only the variable "sorted_pairs", therefore the space complexity is constant.
'''
