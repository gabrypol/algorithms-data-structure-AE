'''
Write a function that takes in an array of integers and, without sorting the input array, returns a sorted array of the three largest integers in the input array.

The function should return duplicate integers if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].

Sample Input
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample Output
[18, 141, 541]
'''

def find_three_largest_numbers(input_list):
    three_largest = []
    first_largest = input_list[0]
    for i, num in enumerate(input_list[1:], 1):
        if num > first_largest:
            first_largest = num
    input_list.remove(first_largest)

    second_largest = input_list[0]
    for i, num in enumerate(input_list[1:], 1):
        if num > second_largest:
            second_largest = num
    input_list.remove(second_largest)

    third_largest = input_list[0]
    for i, num in enumerate(input_list[1:], 1):
        if num > third_largest:
            third_largest = num

    three_largest.extend([third_largest, second_largest, first_largest])
    return three_largest


my_list = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(find_three_largest_numbers(my_list))


'''
Time: O(n)
Space: O(1)
'''