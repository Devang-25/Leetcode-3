class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # o(N) for building the dict
        # 0(1) for getting the key
        # 0(N) or less for counting length of dict keys
        count_dict = {}
        max_length = 0
        flag = 0
        for letter in s:
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1
        keys = count_dict.keys()
        for key in keys:
            if count_dict[key] % 2 == 0:
                max_length += count_dict[key]
            else:
                max_length += count_dict[key] - 1
                flag = 1
        return max_length + flag
