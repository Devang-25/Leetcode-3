"""

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        length = 2
        front, back, wordDict = set([beginWord]), set([endWord]), set(wordList)
        wordDict.discard(beginWord)
        while front:
            # generate all valid transformation
            front = wordDict & (set(word[:index] + ch + word[index+1:]
                                    for word in front
                                    for index in range(len(beginWord))
                                    for  ch in 'abcdefghijklmnopqrstuvwxyz'))
            print('front', front)
            if front & back:
                print('front', front,'back', back)
                return length
            length += 1
            if len(front) > len(back):
                print('front', len(front), 'back', len(back))
                print('swap')
                # swap back and back for better peformance
                # fewer choice in generate nextSet for front
                front, back = back, front
            # remove transformation from wordDict to avoid cycle
            wordDict -= front
        return 0

beginWord = "hit"
endWord = "cog"
wordList1 = ["hot","dot","dog","lot","log"]

Solution().ladderLength(beginWord, endWord, wordList1)
