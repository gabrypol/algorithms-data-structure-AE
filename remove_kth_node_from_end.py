'''
Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth node from the end of the list.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

You can assume that the input Linked List will always have at least 2 nodes and, more specifically, at least k nodes.

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 // the head node with value 0
k = 4
Sample Output
// No output required.
// The 4th node from the end of the list (the node with value 6) is removed.
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
'''

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def removeKthNodeFromEnd(self, head, k):
        list_length = 0

        dummy_head = head
        while dummy_head:
            list_length += 1
            dummy_head = dummy_head.next
        position_elem_to_remove = list_length - k + 1


        if list_length == position_elem_to_remove:
            dummy_head = head
            for i in range(1, position_elem_to_remove + 1):
                if i == position_elem_to_remove - 1:
                    dummy_head.next = None
                    return
                dummy_head = dummy_head.next
        else:
            dummy_head = head
            for i in range(1, position_elem_to_remove + 1):

                if i == position_elem_to_remove:
                    dummy_head.value = dummy_head.next.value
                    dummy_head.next = dummy_head.next.next
                dummy_head = dummy_head.next


singly_linked_list = LinkedList(1)
singly_linked_list.next = LinkedList(2)
singly_linked_list.next.next = LinkedList(3)
singly_linked_list.next.next.next = LinkedList(4)
singly_linked_list.next.next.next.next = LinkedList(5)
print("head: ", singly_linked_list.value)
print("2nd node: ", singly_linked_list.next.value)
print("3rd node: ", singly_linked_list.next.next.value)
print("4th node: ", singly_linked_list.next.next.next.value)
print("tail: ", singly_linked_list.next.next.next.next.value)
singly_linked_list.removeKthNodeFromEnd(singly_linked_list, 5)

print("\nhead: ", singly_linked_list.value)
print("2nd node: ", singly_linked_list.next.value)
print("3rd node: ", singly_linked_list.next.next.value)
print("tail: ", singly_linked_list.next.next.next.value)


'''
Time: O(n)
Space: O(1)
'''