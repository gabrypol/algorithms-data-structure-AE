'''
Write a MinMaxStack class for a Min Max Stack. The class should support:

- Pushing and popping values on and off the stack.
- Peeking at the value at the top of the stack.
- Getting both the minimum and the maximum values in the stack at any given point in time.
All class methods, when considered independently, should run in constant time and with constant space.

Sample Usage
// All operations below are performed sequentially.
MinMaxStack(): - // instantiate a MinMaxStack
push(5): -
getMin(): 5
getMax(): 5
peek(): 5
push(7): -
getMin(): 5
getMax(): 7
peek(): 7
push(2): -
getMin(): 2
getMax(): 7
peek(): 2
pop(): 2
pop(): 7
getMin(): 5
getMax(): 5
peek(): 5
'''


class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_max_stack = []


    # Time: O(1), Space: O(1)
    def peek(self):
        return self.stack[-1]


    # Time: O(1), Space: O(1)
    def pop(self):
        self.min_max_stack.pop()
        return self.stack.pop()


    # Time: O(1), Space: O(1)
    def push(self, number):
        new_min_max = {"min": number, "max": number}
        if (self.min_max_stack):
            new_min_max["min"] = min(self.min_max_stack[-1]["min"], number)
            new_min_max["max"] = max(self.min_max_stack[-1]["max"], number)
        self.min_max_stack.append(new_min_max)
        self.stack.append(number)


    # Time: O(1), Space: O(1)
    def get_min(self):
        return self.min_max_stack[-1]["min"]


    # Time: O(1), Space: O(1)
    def get_max(self):
        return self.min_max_stack[-1]["max"]


min_max_stack = MinMaxStack()
min_max_stack.push(5)
print("max, min:", min_max_stack.get_min(), min_max_stack.get_max())
print("peek:", min_max_stack.peek())
min_max_stack.push(7)
print("max, min:", min_max_stack.get_min(), min_max_stack.get_max())
print("peek:", min_max_stack.peek())
min_max_stack.push(2)
print("max, min:", min_max_stack.get_min(), min_max_stack.get_max())
print("peek:", min_max_stack.peek())
min_max_stack.pop()
min_max_stack.pop()
print("max, min:", min_max_stack.get_min(), min_max_stack.get_max())
print("peek:", min_max_stack.peek())
