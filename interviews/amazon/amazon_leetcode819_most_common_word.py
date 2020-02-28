"""
Leetcode819: Most common word

some people use: 1) collection.Counter + 2)counter.most_common
but Counter.most_common has a time complexity of O(NlogN)

上面的方法比用方法2快： 因为1）top_frequncy + 2）top_word + 扫一遍单词快。方法二需要 O(N) > O(NlogN)


========

Regular Expression
https://developers.google.com/edu/python/regular-expressions


==========

r'\w+'

r\:  in python means "raw" string, passes into through backslashes \

\w : (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. 

+ : one or more occurrence of the pattern to the left of it  (in this case: it's \w)


=========

re.findall(pattern, string)
https://docs.python.org/2/library/re.html


Use: to find a word without space
Example: 你有各种符号，及不等数量的空格在单词之间，但是你只想要单词。
”A,a,a,a, bp apple, banan    ! Bear"

Example:  re.findall(r'\w+", text)

==========

most_common([n])
Return a list of the n most common elements and their counts from the most common to the least. If n is omitted or None, most_common() returns all elements in the counter. Elements with equal counts are ordered arbitrarily:

>>> Counter('abracadabra').most_common(3)
[('a', 5), ('r', 2), ('b', 2)]

https://docs.python.org/2/library/collections.html


"""

import collections
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)

        data = re.findall(r'\w+', paragraph.lower())
        # print("data", data)

        top_word = collections.Counter(w for w in data if w not in banned).most_common(1)[0][0]


        return top_word
