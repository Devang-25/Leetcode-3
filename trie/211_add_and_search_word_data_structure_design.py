"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

"""

class WordDictionary_1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if not "." in word:
            return word in self.word_dict[len(word)]
        # if you encounter any break, return False
        for v in self.word_dict[len(word)]:
            for i, char in enumerate(word):
                if char != v[i] and char != ".":
                    break
            # when all the char has been match with a particular v in word_dict WITHOUT break:
            # return True
            else:
                return True
        return False

class WordDictionary_2(object):

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[None] = None
#         print(node[None])
#         return node[None]

    def search(self, word):
        def find(word, node):
            if not word:
                # print(bool(None in node))
                # print(type(None in node))
                # print(node.keys())
                return None in node
            char, word = word[0], word[1:]
            print('char:{}, word:{}'.format(char, word))
            if char != ".":
                return char in node and find(word, node[char])
            return any(find(word, kid) for kid in node.values if kid)
        return find(word, self.root)

'''
For solution 2:

the structure is dictionayr in dictionayr {{}}

eg. word = "ape"
self.root = {}
{{"a":{"p":{"e":{None:None}}}}}
'''


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
