'''
Write a function that takes in a "special" array and returns its product sum. A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed themselves and then multiplied by their level of depth.

For example, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2y + 2z.

Sample Input
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
Sample Output
12 // calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
'''

def product_sum(input_list, depth = 1):
    sum = 0
    for elem in input_list:
        if isinstance(elem, int):
            sum += elem
        else:
            sum += product_sum(elem, depth + 1)

    return depth * sum


my_list = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(product_sum(my_list))


'''
Time: O(n) where n is the number of elements and sub-elements.
Space: O(d) where d is the maximum depth of the sub-lists. This space is used by the call stack, since we are using recursion.
'''