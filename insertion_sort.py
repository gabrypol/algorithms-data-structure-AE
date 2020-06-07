'''
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Insertion Sort algorithm to sort the array.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output
[2, 3, 5, 5, 6, 8, 9]
'''


def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        for j in range(i - 1, -1, -1):
            if input_list[j + 1] < input_list[j]:
                input_list[j + 1], input_list[j] = input_list[j], input_list[j + 1]

    return input_list


my_list = [8, 5, 2, 9, 5, 6, 3]
print(insertion_sort(my_list))

'''
Time: O(n^2)
Space: O(1)
'''
