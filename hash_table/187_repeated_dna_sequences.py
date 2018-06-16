"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]

"""

class Solution(object):
    def findRepeatedDnaSequences_set_sol(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        show_set = set()
        res = set()
        for i in xrange(len(s) - 10 + 1):
            sub_dna = s[i:i+10]
            if sub_dna in show_set:
                res.add(sub_dna)
            else:
                show_set.add(sub_dna)
        return list(res)

    def findRepeatedDnaSequences_dict_sol(self, s):
        dna_dict = collections.Counter()
        for i in range(len(s) - 10 + 1):
            sub_dna = s[i: i+10]
            dna_dict[sub_dna] += 1
        return [dna for dna in dna_dict.keys() if dna_dict[dna] > 1]
