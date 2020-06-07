
'''
Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key.

Note that letters should "wrap" around the alphabet; in other words, the letter z shifted by one returns the letter a.

Sample Input
string = "xyz"
key = 2
Sample Output
"zab"
'''


def caesar_cipher_encryptor(string, key):

    chars_in_string = [''] * len(string)

    for i, char in enumerate(string):
        chars_in_string[i] = chr(
            ord('a') + (ord(char) - ord('a') + key) % (1 + ord('z') - ord('a')))

    return ''.join(chars_in_string)


my_string = "abc"
my_key = 3
print(caesar_cipher_encryptor(my_string, my_key))

'''
Time: O(n)
Space: O(n)
'''
