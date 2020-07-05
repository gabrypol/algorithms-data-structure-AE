'''
Implement a MinHeap class that supports:

- Building a Min Heap from an input array of integers.
- Inserting integers in the heap.
- Removing the heap's minimum / root value.
- Peeking at the heap's minimum / root value.
- Sifting integers up and down the heap, which is to be used when inserting and removing values.
Note that the heap should be represented in the form of an array.

Sample Usage
array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

// All operations below are performed sequentially.
MinHeap(array): - // instantiate a MinHeap (calls the buildHeap method and populates the heap)
buildHeap(array): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
insert(76): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
peek(): -5
remove(): -5 [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
peek(): 2
remove(): 2 [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]
peek(): 6
insert(87): - [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]
'''

class MinHeap:
    def __init__(self, input_list):
        self.heap = self.build_heap(input_list)


    # Time: O(n), Space: O(1)
    def build_heap(self, input_list):
        last_parent_idx = (len(input_list) - 2) // 2
        for current_idx in range(last_parent_idx, -1, -1):
            self.sift_down(current_idx, len(input_list) - 1, input_list)
        return input_list


    # Time: O(log(n)), Space: O(1)
    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idx_elem_to_swap = child_two_idx
            else:
                idx_elem_to_swap = child_one_idx
            if heap[idx_elem_to_swap] < heap[current_idx]:
                heap[idx_elem_to_swap], heap[current_idx] = heap[current_idx], heap[idx_elem_to_swap]
                current_idx = idx_elem_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                break


    # Time: O(log(n)), Space: O(1)
    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[current_idx] < heap[parent_idx]:
            heap[current_idx], heap[parent_idx] = heap[parent_idx], heap[current_idx]
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2


    # Time: O(1), Space: O(1)
    def peek(self):
        return self.heap[0]


    # Time: O(log(n)), Space: O(1)
    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove


    # Time: O(log(n)), Space: O(1)
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)


my_list = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
min_heap = MinHeap(my_list)
print(min_heap.build_heap(my_list))
print(min_heap.peek())
print(min_heap.remove())
print(min_heap.build_heap(my_list))