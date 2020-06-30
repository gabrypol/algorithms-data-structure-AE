'''
Write a function that takes in a non-empty sorted array of distinct integers, constructs a BST from the integers, and returns the root of the BST.

The function should minimize the height of the BST.

You've been provided with a BST class that you'll have to use to construct the BST.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

A BST is valid if and only if all of its nodes are valid BST nodes.

Note that the BST class already has an insert method which you can use if you want.

Sample Input
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
Sample Output
         10
       /     \
      2      14
    /   \   /   \
   1     5 13   15
          \       \
           7      22
// This is one example of a BST with min height
// that you could create from the input array.
// You could create other BSTs with min height
// from the same array; for example:
         10
       /     \
      5      15
    /   \   /   \
   2     7 13   22
 /           \
1            14
'''

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def min_height_bst(input_list):
	return build_min_height_bst(input_list, 0, len(input_list) - 1)

def build_min_height_bst(input_list, left_idx, right_idx):
	if left_idx > right_idx:
		return
	mid_idx = (left_idx + right_idx) // 2
	bst = BST(input_list[mid_idx])
	bst.left = build_min_height_bst(input_list, left_idx, mid_idx - 1)
	bst.right = build_min_height_bst(input_list, mid_idx + 1, right_idx)
	return bst


my_list = [1, 2, 5, 7, 10, 13, 14, 15, 22]
print(min_height_bst(my_list).value)
print(min_height_bst(my_list).left.value)
print(min_height_bst(my_list).right.value)