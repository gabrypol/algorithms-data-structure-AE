'''
Write a function that takes in a string made up of brackets ((, [, {, ), ], and }) and other optional characters. The function should return a boolean representing whether the string is balanced with regards to brackets.

A string is said to be balanced if it has as many opening brackets of a certain type as it has closing brackets of that type and if no bracket is unmatched. Note that an opening bracket can't match a corresponding closing bracket that comes before it, and similarly, a closing bracket can't match a corresponding opening bracket that comes after it. Also, brackets can't overlap each other as in [(]).

Sample Input
string = "([])(){}(())()()"
Sample Output
true // it's balanced
'''


def balancedBrackets(string):
    stack = []
    opening_brackets = "{[("
    for i, bracket in enumerate(string):
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket == ")":
            if len(stack) == 0 or stack[-1] != "(":
                return False
            else:
                stack.pop()
        elif bracket == "]":
            if len(stack) == 0 or stack[-1] != "[":
                return False
            else:
                stack.pop()
        elif bracket == "}":
            if len(stack) == 0 or stack[-1] != "{":
                return False
            else:
                stack.pop()
    return len(stack) == 0


brackets = "([])(){}(())()()"
print(balancedBrackets(brackets))


'''
Time: O(n)
Space: O(n)
'''