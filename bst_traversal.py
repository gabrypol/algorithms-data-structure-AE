'''
Write three functions that take in a Binary Search Tree (BST) and an empty array, traverse the BST, add its nodes' values to the input array, and return that array. The three functions should traverse the BST using the in-order, pre-order, and post-order tree-traversal techniques, respectively.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

Sample Input
tree =   10
       /     \
      5      15
    /   \       \
   2     5       22
 /
1
array = []
Sample Output
inOrderTraverse: [1, 2, 5, 5, 10, 15, 22] // where the array is the input array
preOrderTraverse: [10, 5, 2, 1, 5, 15, 22] // where the array is the input array
postOrderTraverse: [1, 2, 5, 5, 22, 15, 10] // where the array is the input array
'''


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# INORDER TRAVERSAL: Left --> Root --> Right
def inorder_traversal(tree, traversal):
    if tree is not None:
        inorder_traversal(tree.left, traversal)
        traversal.append(tree.value)
        inorder_traversal(tree.right, traversal)
    return traversal


# PREORDER TRAVERSAL: Root --> Left --> Right
def preorder_traversal(tree, traversal):
    if tree is not None:
        traversal.append(tree.value)
        preorder_traversal(tree.left, traversal)
        preorder_traversal(tree.right, traversal)
    return traversal


# POSTORDER TRAVERSAL: Left --> Right --> Root
def postorder_traversal(tree, traversal):
    if tree is not None:
        postorder_traversal(tree.left, traversal)
        postorder_traversal(tree.right, traversal)
        traversal.append(tree.value)
    return traversal

'''
Time: O(n) Since we need to traverse all the nodes, the runtime will be at least linear.
      At each node, we append its value to the "traversal" list, which is a constant time operation.
      Therefore, the total time complexity is O(n).

Space: O(n) The memory on the call stack takes O(h), where h is the height of the tree.
       But we also need to allocate memory for the traversal list, which contains all the nodes.
       Therefore the total space complexity is O(n).
'''

#          10
#        /     \
#       5      15
#     /   \       \
#    2     5       22
#  /
# 1

bst = BST(10)
bst.left = BST(5)
bst.right = BST(15)
bst.left.left = BST(2)
bst.left.right = BST(5)
bst.right.right = BST(22)
bst.left.left.left = BST(1)
print("Inorder traversal: ", inorder_traversal(bst, []))
print("Preorder traversal: ", preorder_traversal(bst, []))
print("Postorder traversal: ", postorder_traversal(bst, []))