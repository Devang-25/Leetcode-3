"""
438. Find All Anagrams in a String
Easy
1161
84


Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

import collections

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        results = []
        need = len(p)

        if p == s:
            return s

        elif len(s) >= len(p):
            pdict = collections.Counter(p)
            # print("inital", pdict)

            for i in range(0, len(p)):
                need -= pdict[s[i]] > 0
                pdict[s[i]] -= 1
            if need == 0:
                results.append(0)
                # print("results", results, "pdict", pdict, "need", need)
            for i in range(len(p), len(s)):
                # print("pre", s[i - len(p)])
                # print("cur", i, s[i])
                need += pdict[s[i - len(p)]] >= 0
                pdict[s[i - len(p)]] += 1
#                 if s[i - len(p)] in pdict:
#                     print("pre", s[i - len(p)])
#                     pdict[s[i - len(p)]] += 1
#                     if pdict[s[i - len(p)]] > 0:
#                         need += 1
                need -= pdict[s[i]] > 0
                pdict[s[i]] -= 1
#                 if s[i] in pdict:
#                     print("new", s[i])
#                     pdict[s[i]] -= 1
#                     if pdict[s[i]] >= 0:
#                         need -= 1
                # print("cur", pdict)
                # print(pdict.values())
                if need == 0:
                    results.append(i - len(p) +1)
                    # print("results", results, "pdict", pdict, "need", need)
        return(results)
