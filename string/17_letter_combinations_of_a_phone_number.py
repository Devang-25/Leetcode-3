class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        results = [""]
        letters = "abcdefghijklmnopqrstuvwxyz"
        digit_list = []
        for digit in digits:
            start = (int(digit) - 2) * 3
            if digit == "7":
                digit_list.append(letters[start: start+4])
            elif digit == "8":
                digit_list.append(letters[start+1: start+4])
            elif digit == "9":
                digit_list.append(letters[start+1: start+4])
            else:
                digit_list.append(letters[start: start+3])
        #print(digit_list)
        for sub_list in digit_list:
            results = [result+w for w in sub_list for result in results]
        return results if results != [""] else []

Solution().letterCombinations("")
Solution().letterCombinations("79")


# time complexity: O(4^n)
