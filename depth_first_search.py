'''
You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form an acyclic tree-like structure.

Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in the input array, and returns it.

If you're unfamiliar with Depth-first Search, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.

Sample Input
graph = A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K
Sample Output
["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
'''

class Graph:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Graph(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for i, child in enumerate(self.children):
            child.depthFirstSearch(array)
        return array


graph = Graph('A')
graph.addChild('B').addChild('C').addChild('D')
graph.children[0].addChild('E').addChild('F')
graph.children[2].addChild('G').addChild('H')
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")
print(graph.depthFirstSearch([]))

'''
Time: O(v + e) where v is the number of vertices (nodes) and e is the number of edges.
Space: O(v) -- The space complexity is O(v) because we need to output a new list containing all vertices.
               Also, in the worst case of a graph being a single line of nodes, we would need v frames on the call stack.
'''
