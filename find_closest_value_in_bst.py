'''
Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest value.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

Sample Input
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
target = 12
Sample Output
13
'''

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def find_closest_value_in_bst(self, target):
        closest = float('inf')
        while self is not None:
            if abs(target - closest) > abs(target - self.value):
                closest = self.value
            if target < self.value:
                self = self.left
            elif target > self.value:
                self = self.right
            else:
                break
        return closest
    '''
    Time: Average (balanced tree) --> O(log(n)) /---/ Worst case (unbalanced tree) --> O(n)
    Space: O(1)
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
print(bst.find_closest_value_in_bst(12))