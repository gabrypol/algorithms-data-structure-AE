'''
Write a function that takes in a potentially invalid Binary Search Tree (BST) and returns a boolean representing whether the BST is valid.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

A BST is valid if and only if all of its nodes are valid BST nodes.

Sample Input
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
Sample Output
true
'''

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ITERATIVE SOLUTION:
# def validate_bst(root):

#     if root is None:
#         return True

#     stack = [(root, float('-inf'), float('inf')), ]
#     while stack:
#         root, lower, upper = stack.pop()
#         if root is None:
#             continue
#         value = root.value
#         if value < lower or value >= upper:
#             return False
#         stack.append((root.right, value, upper))
#         stack.append((root.left, lower, value))
#     return True
'''
Time: O(n)
Space: O(n)
'''



# RECURSIVE SOLUTION:
def validate_bst(root):
    return helper_validator(root, float('-inf'), float('inf'))


def helper_validator(tree, min_value, max_value):
    if tree is None:
        return True

    if tree.value < min_value or tree.value >= max_value:
        return False

    left_is_valid = helper_validator(tree.left, min_value, tree.value)
    right_is_valid = helper_validator(tree.right, tree.value, max_value)
    return left_is_valid and right_is_valid

'''
Time: O(n)
Space: O(d) where d is the height of the tree. This is the space allocated on the stack.
'''

#          10
#        /     \
#       5      15
#     /   \   /   \
#    2     5 13   22
#  /           \
# 1            14

bst = BST(10)
bst.left = BST(5)
bst.right = BST(15)
bst.left.left = BST(2)
bst.left.right = BST(5)
bst.left.left.left = BST(1)
bst.right.left = BST(13)
bst.right.right = BST(22)
bst.right.left.right = BST(14)
print(validate_bst(bst))


