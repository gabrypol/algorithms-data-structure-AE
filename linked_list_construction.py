'''
Write a DoublyLinkedList class that has a head and a tail, both of which point to either a linked list Node or None / null. The class should support:

- Setting the head and tail of the linked list.
- Inserting nodes before and after other nodes as well as at given positions.
- Removing given nodes and removing nodes with given values;
- Searching for nodes with given values.
Each Node has an integer value as well as a prev node and a next node, both of which can point to either another node or None / null.

Sample Usage
// Assume the following linked list has already been created:
1 <-> 2 <-> 3 <-> 4 <-> 5
setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 // set the existing node with value 4 as the head
setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the existing node with value 6 as the tail
insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the existing node with value 3 before the existing node with value 6
insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a new node with value 3 after the existing node with value 6
insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a new node with value 3 in position 1
removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all nodes with value 3
remove(2): 4 <-> 1 <-> 5 <-> 6 // remove the existing node with value 2
containsNodeWithValue(5): true
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Time: O(1), Space: O(1)
    def set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insert_before(self.head, node)


    # Time: O(1), Space: O(1)
    def set_tail(self, node):
        if self.tail is None:
            self.set_head(node)
            return
        self.insert_after(self.tail, node)


    # Time: O(1), Space: O(1)
    def insert_before(self, node, node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev = node.prev
        node_to_insert.next = node
        if node.prev is None:
            self.head = node_to_insert
        else:
            node.prev.next = node_to_insert
        node.prev = node_to_insert


    # Time: O(1), Space: O(1)
    def insert_after(self, node, node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev = node
        node_to_insert.next = node.next
        if node.next is None:
            self.tail = node_to_insert
        else:
            node.next.prev = node_to_insert
        node.next = node_to_insert


    # Time: O(p), Space: O(1) where p is the position where to insert the node
    def insert_at_position(self, position, node_to_insert):
        if position == 1:
            self.set_head(node_to_insert)
            return
        node = self.head
        current_position = 1
        while node is not None and current_position != position:
            node = node.next
            current_position += 1
        if node is not None:
            self.insert_before(node, node_to_insert)
        else:
            self.set_tail(node_to_insert)


    # Time: O(n), Space: O(1)
    def remove_nodes_with_value(self, value):
        node = self.head
        while node is not None:
            node_to_remove = node
            node = node.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)


    # Time: O(1), Space: O(1)
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


    # Time: O(n), Space: O(1)
    def contains_node_with_value(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.head = Node(1)
doubly_linked_list.head.next = Node(2)
doubly_linked_list.head.next.next = Node(3)
doubly_linked_list.head.next.next.next = Node(4)
doubly_linked_list.head.next.next.next.next = Node(5)
print("head: ", doubly_linked_list.head.value)
print("2nd node: ", doubly_linked_list.head.next.value)
print("3rd node: ", doubly_linked_list.head.next.next.value)
print("4th node: ", doubly_linked_list.head.next.next.next.value)
print("tail: ", doubly_linked_list.head.next.next.next.next.value)