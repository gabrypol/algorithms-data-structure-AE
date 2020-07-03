'''
Write a function that takes in an array of unique integers and returns an array of all permutations of those integers in no particular order.

If the input array is empty, the function should return an empty array.

Sample Input
array = [1, 2, 3]
Sample Output
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''

def permutations(input_list):
    def directed_permutations(i):
        if i == len(input_list) - 1:
            result.append(input_list.copy())
            return

        for j in range(i, len(input_list)):
            input_list[i], input_list[j] = input_list[j], input_list[i]
            directed_permutations(i + 1)
            input_list[i], input_list[j] = input_list[j], input_list[i]

    result = []
    directed_permutations(0)
    return result


my_list = [1, 2, 3]
print(permutations(my_list))

'''
Time: O(n * n!)
Space: O(n * n!)
'''