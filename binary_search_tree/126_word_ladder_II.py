"""

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        dic = set(wordList)
        level = {beginWord}
        parents = collections.defaultdict(set)
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(beginWord)):
                        n = node[:i] + char + node[i+1:]
                        if n in dic and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
#             new_res = []
#             for r in res:
#                 for p in parents[r[0]]:
#                     new_res.append([p] + r)
#             res = new_res
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res

beginWord = "hit"
endWord = "cog"
wordList1 = ["hot","dot","dog","lot","log"]
wordList2 = ["hot","dot","dog","lot","log","cog"]

Solution().findLadders(beginWord, endWord, wordList1)
Solution().findLadders(beginWord, endWord, wordList2)
