'''
Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

Your function should return a list of anagram groups in no particular order.

Sample Input
words = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
Sample Output
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"]]
'''

def group_anagrams(input_list):
    cache = {}
    for word in input_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in cache:
            cache[sorted_word].append(word)
        else:
            cache[sorted_word] = [word]
    return list(cache.values())

my_words = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
print(group_anagrams(my_words))


'''
Time: O(w * n * log(n)) where w is the number of words in "my_words" and n the length of the longest word
Space: O(w * n)