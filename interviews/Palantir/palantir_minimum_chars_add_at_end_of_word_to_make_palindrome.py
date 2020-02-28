"""
Given a string str we need to tell minimum characters to be added at front of string to make string palindrome.

Examples:

Input  : str = "ABC"
Output : 2
We can make above string palindrome as "CBABC"
by adding 'B' and 'C' at front.

Input  : str = "AACECAAAA";
Output : 2
We can make above string palindrome as AAAACECAAAA
by adding two A's at front of string.

"""

class MakeIntoPalindrome:
    def make_word_into_palindrome(self, s):
        if not s:
            return 0

        results = []
        start = (len(string) - 1) // 2

        for i in range(start, len(s)):
            print("[{}]: {}".format(i, s[i]))
            # odd case: # abc(ba), start=1 (1,1)
            addition_length_1 = self.complete_palindrome(i, i, s)
            # even case: abb, start=1 -> (1, 2)
            addition_length_2 = self.complete_palindrome(i, i+1, s)
            print("addition_length_1: {}, addition_length_2: {}".format(addition_length_1, addition_length_2), "\n")
            results.append(min(addition_length_1, addition_length_2))

        return min(results)

    def complete_palindrome(self, l, r, s):
        """
        inputs:
            l: int, the index of left
            r: int, the index of right
            s: string
        ouput:
            addition_length : int
        """
        # base case, reach the boundary where l == 0
        if l == 0:
            if r == (len(s) - 1) and s[l] == s[r]:
                return 0
            elif r >= len(s):
                return (r - len(s)) + 1

        if l > 0:
            if (r < len(s) and s[l] == s[r]) or r >= len(s):
                    return self.complete_palindrome(l-1, r+1, s)

        return float("inf")

string = "ab"
s = MakeIntoPalindrome()
r = s.make_word_into_palindrome(string)
assert r == 1
print("s: {} / r: {}".format(string, r))

string = ""
s = MakeIntoPalindrome()
r = s.make_word_into_palindrome(string)
assert r == 0
print("s: {} / r: {}".format(string, r))

string = "aba"
s = MakeIntoPalindrome()
r = s.make_word_into_palindrome(string)
assert r == 0
print("s: {} / r: {}".format(string, r))

string = "abba"
s = MakeIntoPalindrome()
r = s.make_word_into_palindrome(string)
assert r == 0
print("s: {} / r: {}".format(string, r))

string = "abb"
s = MakeIntoPalindrome()
r = s.make_word_into_palindrome(string)
assert r == 1
print("s: {} / r: {}".format(string, r))

string = "abc"
s = MakeIntoPalindrome()
r = s.make_word_into_palindrome(string)
assert r == 2
print("s: {} / r: {}".format(string, r))
