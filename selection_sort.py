'''
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort algorithm to sort the array.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output
[2, 3, 5, 5, 6, 8, 9]
'''

def selection_sort(input_list):
    for i, num_one in enumerate(input_list[:len(input_list) - 1]):
        min_idx = i
        for j, num_two in enumerate(input_list[i + 1:], i + 1):
            if num_two < input_list[min_idx]:
                min_idx = j
        input_list[i], input_list[min_idx] = input_list[min_idx], input_list[i]
    return input_list


my_list = [8, 5, 2, 9, 5, 6, 3]
print(selection_sort(my_list))


'''
Time: O(n^2)
Space: O(1)
'''

