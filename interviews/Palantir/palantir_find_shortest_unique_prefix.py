"""
Given an array of words, find all shortest unique prefixes to represent each word in the given array. Assume that no word is prefix of another.

Examples:

Input: arr[] = {"zebra", "dog", "duck", "dove"}
Output: dog, dov, du, z
Explanation: dog => dog
             dove = dov
             duck = du
             z   => zebra

Input: arr[] =  {"geeksgeeks", "geeksquiz", "geeksforgeeks"};
Output: geeksf, geeksg, geeksq}


Solution:

building a trie.

For each word: the time complexity for building it into the trie is O(N), N = num of chars in word
For n words: the time complexity is O(N^2).

And for travesing through the trie to get all the prefix, the time complexity is O(N), where N is being the number of nodes in the trie.

The overall time complexity is O(N^2).

"""


from collections import defaultdict
class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1
        self.prefix_finished = False


class FindShortestUniquePrefix:
    def __init__(self):
        self.root = TrieNode("")
        self.results = []

    def shortest_unique_prefix(self, words):
        for word in words:
            self.add_word(word)
        self.get_all_prefix("", self.root)
        return self.results


    def add_word(self, word):
        node = self.root
        has_prefix = False
        for char in word:
            found_in_child = False
            for child in node.children:
                if char == child.char:
                    child.counter += 1
                    if child.prefix_finished: # if it is prefix of another word
                        child.prefix_finished = False
                        for grand_child in child.children:
                            grand_child.prefix_finished = True
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                if not has_prefix:
                    new_node.prefix_finished = True
                node.children.append(new_node)
                node = new_node
        node.word_finished = True

    def get_all_prefix(self, prefix, node):
        new_prefix = prefix + node.char
        if node.prefix_finished:
            self.results.append(new_prefix)
            return
        for child in node.children:
            self.get_all_prefix(new_prefix, child)


words = ["zebra", "dog", "duck", "dove"]
s = FindShortestUniquePrefix()
r = s.shortest_unique_prefix(words)
print(r)


words = []
s = FindShortestUniquePrefix()
r = s.shortest_unique_prefix(words)
print(r)

words = ["geeksgeeks", "geeksquiz", "geeksforgeeks"]
s = FindShortestUniquePrefix()
r = s.shortest_unique_prefix(words)
print(r)
