'''
Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.

Sample Input
string = "abcdcba"
Sample Output
true // it's written the same forward and backward
'''


def palindrome_checker(string):
    for i, char in enumerate(string[:len(string) // 2]):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


my_string = "abcdddcba"
print(palindrome_checker(my_string))


'''
Time: O(n)
Space: O(1)
'''
