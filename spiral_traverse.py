'''
Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n === m) and returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral pattern all the way until every element has been visited.

Sample Input
array = [
  [1, 2, 3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10, 9, 8, 7],
]
Sample Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
'''

def spiral_traverse(matrix):
    output_list = []

    starting_row = 0
    ending_row = len(matrix) - 1
    starting_column = 0
    ending_column = len(matrix[0]) - 1

    while starting_row <= ending_row and starting_column <= ending_column:
        for i in range(starting_column, ending_column + 1):
            output_list.append(matrix[starting_row][i])
        starting_row += 1

        for i in range(starting_row, ending_row + 1):
            output_list.append(matrix[i][ending_column])
        ending_column -= 1

        for i in range(ending_column, starting_column - 1, -1):
            if starting_row > ending_row:
                break
            output_list.append(matrix[ending_row][i])
        ending_row -= 1

        for i in range(ending_row, starting_row - 1, -1):
            if starting_column > ending_column:
                break
            output_list.append(matrix[i][starting_column])
        starting_column += 1

    return output_list


my_matrix = [
  [1, 2, 3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10, 9, 8, 7],
]
print(spiral_traverse(my_matrix))

'''
Time: O(n)
Space: O(n)
'''