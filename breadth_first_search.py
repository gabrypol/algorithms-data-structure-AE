'''
You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form an acyclic tree-like structure.

Implement the breadthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in the input array, and returns it.

If you're unfamiliar with Breadth-first Search, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.

Sample Input
graph = A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K
Sample Output
["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
'''

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self):
        output_list = []
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            output_list.append(current.name)
            for child in current.children:
                queue.append(child)
        return output_list



bfs = Node('A')
bfs.addChild('B')
bfs.addChild('C')
bfs.addChild('D')
bfs.children[0].addChild('E')
bfs.children[0].addChild('F')
bfs.children[0].children[1].addChild('I')
bfs.children[0].children[1].addChild('J')
bfs.children[2].addChild('G')
bfs.children[2].addChild('H')
bfs.children[2].children[0].addChild('K')
print(bfs.breadthFirstSearch())

'''
Time: O(v + e) where v is the number of nodes and e the number of edges.
Space: O(v) we need to store in a output_list all the nodes, therefore the space complexity is linear.
'''