'''
Write a function that, given a string, returns its longest palindromic substring.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.

You can assume that there will only be one longest palindromic substring.

Sample Input
string = "abaxyzzyxf"
Sample Output
"xyzzyx"
'''


def longest_palindromic_substring(input_string):
    max_length = 1
    start = 0
    low = 0
    high = 0

    for i, char in enumerate(input_string[1:len(input_string)], 1):
        # Longest even palindromic substring
        low = i - 1
        high = i
        while low >= 0 and high < len(input_string) and input_string[low] == input_string[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

        # Longest odd palindromic substring
        low = i - 1
        high = i + 1
        while low >= 0 and high < len(input_string) and input_string[low] == input_string[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1
    return input_string[start:start + max_length]


my_string = "abaxyzzyxf"
print(longest_palindromic_substring(my_string))


'''
Time: O(n^2)
Space: O(1)
'''