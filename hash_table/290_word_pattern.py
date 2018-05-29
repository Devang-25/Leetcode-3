"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        print(str)
        mapping = {}
        used = []
        word_list = str.split()
        if len(pattern) != len(word_list):
            return False
        for i, word in enumerate(word_list):
            if word not in mapping:
                if pattern[i] in used:
                    return False
                mapping[word] = pattern[i]
                used.append(pattern[i])
            elif mapping[word] != pattern[i]:
                return False
        return True


    
