'''
The distance between a node in a Binary Tree and the tree's root is called the node's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =    1
       /     \
      2       3
    /   \   /   \
   4     5 6     7
 /   \
8     9
Sample Output
16
// The depth of the node with value 2 is 1.
// The depth of the node with value 3 is 1.
// The depth of the node with value 4 is 2.
// The depth of the node with value 5 is 2.
// Etc..
// Summing all of these depths yields 16.
'''


class BinaryTreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def nodes_depth_sum(root, depth = 0):
	if not root:
		return 0
	return depth + nodes_depth_sum(root.left, depth + 1) + nodes_depth_sum(root.right, depth + 1)

tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)
tree.left.left.left = BinaryTreeNode(8)
tree.left.left.right = BinaryTreeNode(9)
print(nodes_depth_sum(tree))

'''
Time: O(n) Since we need to traverse the whole tree in order to know the node depths, the runtime is n, where n is the number of nodes on the tree.
Space: O(n) It's the height of the tree. O(n) is in the worst case of having an unbalanced binary tree. If the tree is balanced, then the space complexity is O(log(n))
'''