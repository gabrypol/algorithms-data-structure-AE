'''
You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.

Sample Input
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
Sample Output
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently
'''

def move_element_to_the_end(input_list, number_to_move):
    numbers_occurrences = 0
    idx_elem_replaced = 0
    for i, num in enumerate(input_list):
        if num == number_to_move:
            numbers_occurrences += 1
        else:
            input_list[idx_elem_replaced] = num
            idx_elem_replaced += 1
    for i in range(numbers_occurrences):
        input_list[idx_elem_replaced + i] = number_to_move
    return input_list

my_list = [2, 1, 2, 2, 2, 3, 4, 2]
my_number = 2
print(move_element_to_the_end(my_list, my_number))

'''
Time: O(n)
Space: O(1)
'''