'''
Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =     1
        /     \
       2       3
     /   \    /  \
    4     5  6    7
  /   \  /
 8    9 10
Sample Output
[15, 16, 18, 10, 11]
'''


class BinaryTreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def branch_sums(root):
    branch_sums = []
    calculate_branch_sum(root, 0, branch_sums)
    return branch_sums


def calculate_branch_sum(node, sum_above, sum_list):
    sum_included_current = sum_above + node.value
    if not node.right and not node.left:
        sum_list.append(sum_included_current)
        return
    elif not node.right and node.left:
        calculate_branch_sum(node.left, sum_included_current, sum_list)
    elif node.right and not node.left:
        calculate_branch_sum(node.right, sum_included_current, sum_list)
    else:
        calculate_branch_sum(node.left, sum_included_current, sum_list)
        calculate_branch_sum(node.right, sum_included_current, sum_list)


tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)
tree.left.left.left = BinaryTreeNode(8)
tree.left.left.right = BinaryTreeNode(9)
tree.left.right.left = BinaryTreeNode(10)
print(branch_sums(tree))


'''
Time: O(n) Since we need to traverse the whole tree in order to calculate the branch sums, the runtime is n, where n is the number of nodes on the tree.
Space: O(n) We are using recursion, therefore we need the space for the call stack. The number of recursive calls made is equal to the height of the tree,
       which is log(n) if the tree is balanced, but n in the worst case of the tree being unbalanced.
       Also, we need to consider the space for the branch_sums list, which has as many elements as the number of leaves.
       The number of leaves is roughly equal to half of the number of nodes (n/2), which is linear.
       Therefore the total space complexity is linear O(n).
'''
