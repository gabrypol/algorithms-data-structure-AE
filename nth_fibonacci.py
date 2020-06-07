'''
The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number.

Important note: the Fibonacci sequence is often defined with its first two numbers as F0 = 0 and F1 = 1. For the purpose of this question, the first Fibonacci number is F0; therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc..

Sample Input #1
n = 2
Sample Output #1
1 // 0, 1

Sample Input #2
n = 6
Sample Output #2
5 // 0, 1, 1, 2, 3, 5
'''

'''
Possible solutions:
    This problem can be solved also with recursion, although the time complexity would we O(2^n), with space complexity being O(n).

    An improvement to this solution is using dynamic programming: we store the result of nth_fibonacci(0), nth_fibonacci(1), nth_fibonacci(2), nth_fibonacci(3) and so on in a dictionary. This way, the time complexity is O(n) and the space complexity is also O(n). (Space complexity would be O(2n), one n for the call stack and one for the dictionary. Of course, 0(2n) is reduced to O(n) for our complexity analysis).

    An even better solution is to work up to the solution in a bottom-up fashion (see below). This way the runtime stays linear, but without additional space cost.
'''


def nth_fibonacci(n):
    if n <= 0:
        raise ValueError('Number is negative or equal to zero.')
    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


number = 6
print(nth_fibonacci(number))


'''
Time: O(n)
Space: O(1)
'''
