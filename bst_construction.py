'''
Write a BST class for a Binary Search Tree. The class should support:

- Inserting values with the insert method.
- Removing values with the remove method; this method should only remove the first instance of a given value.
- Searching for values with the contains method.
Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single-node tree should simply not do anything.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

Sample Usage
// Assume the following BST has already been created:
         10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14

// All operations below are performed sequentially.
insert(12):   10
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /        /  \
     1        12  14

remove(10):   12
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /           \
     1            14

contains(15): true
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
        return self
    '''
    Time: Average (balanced tree) --> O(log(n)) /---/ Worst case (unbalanced tree) --> O(n)
    Space: Average (balanced tree) --> O(log(n)) /---/ Worst case (unbalanced tree) --> O(n)
    '''


    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True
    '''
    Time: Average (balanced tree) --> O(log(n)) /---/ Worst case (unbalanced tree) --> O(n)
    Space: Average (balanced tree) --> O(log(n)) /---/ Worst case (unbalanced tree) --> O(n)
    '''


    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.get_min_value()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self
    '''
    Time: Average (balanced tree) --> O(log(n)) /---/ Worst case (unbalanced tree) --> O(n)
    Space: Average (balanced tree) --> O(log(n)) /---/ Worst case (unbalanced tree) --> O(n)
    '''

    def get_min_value(self):
	    if self.left is None:
		    return self.value
	    else:
		    return self.left.get_min_value()


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
bst.insert(12)
bst.remove(10)
print("New root value of the tree, after inserting and removing the items above: ", bst.value)
print("Check if the tree contains a node with value equal to 12: ", bst.contains(12))