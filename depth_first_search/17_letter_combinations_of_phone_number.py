class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {"2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}

        def dp(word, rest_digits, results):
            digit = rest_digits[0]
            d_rest = rest_digits[1:]

            chars = mapping[digit]
            for char in chars:
                if len(d_rest) == 0:
                    results.append(word + char)
                else:
                    dp(word+char, d_rest, results)


        results = []
        if digits:
            dp("", digits, results)
        return results

Solution().letterCombinations("23")
