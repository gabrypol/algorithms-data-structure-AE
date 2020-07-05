'''
Write a SuffixTrie class for a Suffix-Trie-like data structure. The class should have a root property set to be the root node of the trie and should support:

- Creating the trie from a string; this will be done by calling the populateSuffixTrieFrom method upon class instantiation, which should populate the root of the class.
- Searching for strings in the trie.
Note that every string added to the trie should end with the special endSymbol character: "*".

Sample Input (for creation)
string = "babc"
Sample Output (for creation)
The structure below is the root of the trie.
{
  "c": {"*": true},
  "b": {
    "c": {"*": true},
    "a": {"b": {"c": {"*": true}}},
  },
  "a": {"b": {"c": {"*": true}}},
}
Sample Input (for searching in the suffix trie above)
string = "abc"
Sample Output (for searching in the suffix trie above)
true
'''

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insert_substring_starting_at(i, string)

    def insert_substring_starting_at(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node


my_string = "babc"
suffix_trie = SuffixTrie(my_string)
print(suffix_trie.contains("abc")) # True
print(suffix_trie.contains("babc")) # True
print(suffix_trie.contains("bab")) # False