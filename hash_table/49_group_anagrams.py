"""

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: list[str]
        :rtype: List[List[str]]
        anagrams = collections.defaultdict(list)
        for word in strs:
            key = set(sorted(word))
            anagrams[key].append(word)
        return anagrams.values()
        
